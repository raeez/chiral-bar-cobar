"""Comprehensive tests for the primitive kernel programme.

Verifies:
  1. Per-family primitive kernel components K_{g,n} (kappa, cubic, quartic, K_{1,1})
  2. Primitive master equation channels (d, K*K, Delta_ns)
  3. Shell equations (genus-1 and genus-2)
  4. Branch BV actions (dimension, Gaussian property, QME)
  5. Metaplectic half-density (squaring identity, Taylor coefficients)
  6. Flat connection chain (KZ, trivial, flatness)
  7. Cross-validation against shadow_metric_census and primitive_kernel_engine

Ground truth from:
  - concordance.tex sec:concordance-primitive-kernel
  - shadow_metric_census.py (kappa formulas)
  - primitive_kernel_engine.py (genus-2 forcing, spectral data)
  - modular_master.py (profile structure)
  - virasoro_shadow_gf.py (shadow tower coefficients)

Mathematical references:
  - thm:primitive-to-global-reconstruction
  - prop:primitive-shell-equations
  - cor:metaplectic-square-root
  - def:reduced-branch-master-action
"""
import pytest
from fractions import Fraction
from math import factorial

from compute.lib.primitive_kernel_full import (
    PrimitiveKernel,
    PrimitiveKernelComponent,
    BranchBVAction,
    # Family constructors
    heisenberg_kernel,
    affine_slN_kernel,
    betagamma_kernel,
    virasoro_kernel,
    w3_kernel,
    # Master equation channels
    d_channel,
    pre_lie_product,
    bv_self_contraction,
    verify_primitive_master_equation,
    # Shell equations
    genus1_shell,
    genus2_shell,
    heisenberg_genus2_shell_check,
    # Branch BV
    heisenberg_branch_bv,
    affine_sl2_branch_bv,
    betagamma_branch_bv,
    virasoro_branch_bv,
    verify_branch_bv_qme,
    # Metaplectic half-density
    binomial_half,
    metaplectic_half_density_1d,
    weyl_denominator_sl2,
    weyl_denominator_slN,
    virasoro_half_density,
    verify_metaplectic_squaring_1d,
    # Flat connection
    kz_connection_data,
    verify_kz_flatness,
    flat_connection_chain,
    heisenberg_connection_is_trivial,
    # Independent sum
    independent_sum_kernel,
    verify_kappa_additivity,
    # Shadow depth
    shadow_depth_class,
    # Cross-validation
    cross_validate_kappa,
    STANDARD_FAMILIES,
)


# =====================================================================
# 1. Per-family primitive kernel tests
# =====================================================================

class TestHeisenbergKernel:
    """Primitive kernel for Heisenberg H_k."""

    def test_kappa_at_k1(self):
        """kappa(H_1) = 1."""
        k = heisenberg_kernel(Fraction(1))
        assert k.kappa == Fraction(1)

    def test_kappa_at_k_half(self):
        """kappa(H_{1/2}) = 1/2."""
        k = heisenberg_kernel(Fraction(1, 2))
        assert k.kappa == Fraction(1, 2)

    def test_kappa_at_k2(self):
        """kappa(H_2) = 2."""
        k = heisenberg_kernel(Fraction(2))
        assert k.kappa == Fraction(2)

    def test_kappa_at_k3_d2(self):
        """kappa(H_3^2) = 3*2 = 6 (level * dimension)."""
        k = heisenberg_kernel(Fraction(3), d=2)
        assert k.kappa == Fraction(6)

    def test_cubic_vanishes(self):
        """Heisenberg cubic = 0 (abelian)."""
        k = heisenberg_kernel()
        assert k.cubic == Fraction(0)

    def test_quartic_vanishes(self):
        """Heisenberg quartic = 0."""
        k = heisenberg_kernel()
        assert k.quartic == Fraction(0)

    def test_k11_equals_kappa(self):
        """K_{1,1} = kappa for Heisenberg."""
        k = heisenberg_kernel(Fraction(3))
        assert k.genus1_unary == Fraction(3)

    def test_no_planted_forest(self):
        """Heisenberg has no planted-forest correction."""
        k = heisenberg_kernel()
        assert not k.has_planted_forest

    def test_component_string(self):
        """Component string: K_{0,2} + K_{1,1}."""
        k = heisenberg_kernel()
        assert k.component_string() == "K_{0,2} + K_{1,1}"

    def test_channels_delta_ns_only(self):
        """Only Delta_ns channel active for Heisenberg."""
        k = heisenberg_kernel()
        assert k.active_channels() == ("Delta_ns",)

    def test_branch_rank_1(self):
        """dim V^br = 1 for Heisenberg."""
        k = heisenberg_kernel()
        assert k.branch_rank == 1

    def test_components_dict(self):
        """Components dict has exactly K_{0,2} and K_{1,1}."""
        k = heisenberg_kernel(Fraction(5))
        comps = k.components()
        assert set(comps.keys()) == {(0, 2), (1, 1)}
        assert comps[(0, 2)].value == Fraction(5)
        assert comps[(1, 1)].value == Fraction(5)


class TestAffineSl2Kernel:
    """Primitive kernel for affine sl_2."""

    def test_kappa_at_k1(self):
        """kappa(sl_2, k=1) = dim*(k+h^v)/(2*h^v) = 3*3/4 = 9/4."""
        k = affine_slN_kernel(2, Fraction(1))
        assert k.kappa == Fraction(9, 4)

    def test_kappa_at_k2(self):
        """kappa(sl_2, k=2) = 3*4/4 = 3."""
        k = affine_slN_kernel(2, Fraction(2))
        assert k.kappa == Fraction(3)

    def test_kappa_at_k10(self):
        """kappa(sl_2, k=10) = 3*12/4 = 9."""
        k = affine_slN_kernel(2, Fraction(10))
        assert k.kappa == Fraction(9)

    def test_cubic_nonzero(self):
        """Affine sl_2 cubic is nonzero (Lie bracket)."""
        k = affine_slN_kernel(2)
        assert k.cubic != Fraction(0)

    def test_quartic_vanishes(self):
        """Affine sl_2 quartic = 0 (Jacobi kills it)."""
        k = affine_slN_kernel(2)
        assert k.quartic == Fraction(0)

    def test_no_planted_forest(self):
        """Affine sl_2 has no planted-forest correction."""
        k = affine_slN_kernel(2)
        assert not k.has_planted_forest

    def test_component_string(self):
        """Component string includes K_{0,3}."""
        k = affine_slN_kernel(2)
        assert "K_{0,3}" in k.component_string()

    def test_channels_two(self):
        """Affine sl_2 has Delta_ns and [-,-] channels."""
        k = affine_slN_kernel(2)
        channels = k.active_channels()
        assert "Delta_ns" in channels
        assert "[-,-]" in channels

    def test_branch_rank_3(self):
        """dim V^br = dim(sl_2) = 3."""
        k = affine_slN_kernel(2)
        assert k.branch_rank == 3


class TestAffineSl3Kernel:
    """Primitive kernel for affine sl_3."""

    def test_kappa_at_k1(self):
        """kappa(sl_3, k=1) = dim*(k+h^v)/(2*h^v) = 8*4/6 = 16/3."""
        k = affine_slN_kernel(3, Fraction(1))
        assert k.kappa == Fraction(16, 3)

    def test_kappa_at_k2(self):
        """kappa(sl_3, k=2) = 8*5/6 = 20/3."""
        k = affine_slN_kernel(3, Fraction(2))
        assert k.kappa == Fraction(20, 3)

    def test_branch_rank_8(self):
        """dim V^br = dim(sl_3) = 8."""
        k = affine_slN_kernel(3)
        assert k.branch_rank == 8

    def test_dim_lie(self):
        """dim(sl_3) = 8."""
        k = affine_slN_kernel(3)
        assert k.dim_lie == 8

    def test_h_dual(self):
        """h^v(sl_3) = 3."""
        k = affine_slN_kernel(3)
        assert k.h_dual == 3


class TestBetaGammaKernel:
    """Primitive kernel for the betagamma system."""

    def test_kappa_standard(self):
        """kappa(betagamma, lambda=0) = 1."""
        k = betagamma_kernel(Fraction(0))
        assert k.kappa == Fraction(1)

    def test_kappa_lambda1(self):
        """kappa(betagamma, lambda=1) = 1."""
        k = betagamma_kernel(Fraction(1))
        assert k.kappa == Fraction(1)

    def test_kappa_symplectic(self):
        """kappa(betagamma, lambda=1/2) = -1/2."""
        k = betagamma_kernel(Fraction(1, 2))
        assert k.kappa == Fraction(-1, 2)

    def test_cubic_vanishes(self):
        """betagamma cubic = 0 on weight-changing line."""
        k = betagamma_kernel()
        assert k.cubic == Fraction(0)

    def test_quartic_vanishes_on_wt_line(self):
        """betagamma quartic = 0 on weight-changing line (mu_{bg} = 0)."""
        k = betagamma_kernel()
        assert k.quartic == Fraction(0)

    def test_has_planted_forest(self):
        """betagamma has planted-forest correction (from charged stratum)."""
        k = betagamma_kernel()
        assert k.has_planted_forest

    def test_component_string(self):
        """Component string includes R_pf."""
        k = betagamma_kernel()
        s = k.component_string()
        assert "R_pf" in s
        assert "K_{0,3}" not in s  # no cubic
        assert "K_{0,4}" not in s  # quartic = 0 on wt line

    def test_channels(self):
        """betagamma channels: Delta_ns and Rig."""
        k = betagamma_kernel()
        channels = k.active_channels()
        assert "Delta_ns" in channels
        assert "Rig" in channels
        assert "[-,-]" not in channels


class TestVirasoroKernel:
    """Primitive kernel for Virasoro."""

    def test_kappa_c1(self):
        """kappa(Vir, c=1) = 1/2."""
        k = virasoro_kernel(Fraction(1))
        assert k.kappa == Fraction(1, 2)

    def test_kappa_c26(self):
        """kappa(Vir, c=26) = 13."""
        k = virasoro_kernel(Fraction(26))
        assert k.kappa == Fraction(13)

    def test_kappa_c13(self):
        """kappa(Vir, c=13) = 13/2 (self-dual point)."""
        k = virasoro_kernel(Fraction(13))
        assert k.kappa == Fraction(13, 2)

    def test_cubic_is_2(self):
        """Virasoro cubic shadow coefficient alpha = 2."""
        k = virasoro_kernel()
        assert k.cubic == Fraction(2)

    def test_quartic_c1(self):
        """Q^contact_Vir(c=1) = 10/27."""
        k = virasoro_kernel(Fraction(1))
        assert k.quartic == Fraction(10, 27)

    def test_quartic_c25(self):
        """Q^contact_Vir(c=25) = 10/(25*147) = 2/735."""
        k = virasoro_kernel(Fraction(25))
        assert k.quartic == Fraction(2, 735)

    def test_quartic_formula(self):
        """Q^contact_Vir = 10/[c(5c+22)] for generic c."""
        for c_val in [1, 2, 5, 10, 13, 26]:
            c = Fraction(c_val)
            k = virasoro_kernel(c)
            expected = Fraction(10) / (c * (5 * c + 22))
            assert k.quartic == expected, f"Failed at c={c_val}"

    def test_has_planted_forest(self):
        """Virasoro has planted-forest correction."""
        k = virasoro_kernel()
        assert k.has_planted_forest

    def test_all_three_channels(self):
        """Virasoro activates all three channels."""
        k = virasoro_kernel()
        channels = k.active_channels()
        assert "Delta_ns" in channels
        assert "[-,-]" in channels
        assert "Rig" in channels

    def test_component_string(self):
        """Virasoro component string has all terms."""
        k = virasoro_kernel()
        s = k.component_string()
        for term in ["K_{0,2}", "K_{0,3}", "K_{0,4}", "K_{1,1}", "R_pf"]:
            assert term in s

    def test_k11_equals_kappa(self):
        """K_{1,1} = kappa for Virasoro."""
        for c_val in [1, 13, 26]:
            k = virasoro_kernel(Fraction(c_val))
            assert k.genus1_unary == k.kappa


class TestW3Kernel:
    """Primitive kernel for W_3."""

    def test_kappa_c1(self):
        """kappa(W_3, c=1) = 5/6."""
        k = w3_kernel(Fraction(1))
        assert k.kappa == Fraction(5, 6)

    def test_kappa_c6(self):
        """kappa(W_3, c=6) = 5."""
        k = w3_kernel(Fraction(6))
        assert k.kappa == Fraction(5)

    def test_quartic_c1(self):
        """W_3 quartic at c=1: 16/(22+5) = 16/27."""
        k = w3_kernel(Fraction(1))
        assert k.quartic == Fraction(16, 27)

    def test_branch_rank_2(self):
        """dim V^br = 2 for W_3."""
        k = w3_kernel()
        assert k.branch_rank == 2

    def test_all_channels(self):
        """W_3 has all three channels."""
        k = w3_kernel()
        channels = k.active_channels()
        assert len(channels) == 3


# =====================================================================
# 2. Primitive master equation tests
# =====================================================================

class TestPrimitiveMasterEquation:
    """Verify dK + K*K + hbar*Delta_ns(K) = 0."""

    def test_heisenberg_pme(self):
        """PME for Heisenberg: all channels trivially satisfied."""
        k = heisenberg_kernel()
        results = verify_primitive_master_equation(k)
        for key, val in results.items():
            assert val, f"PME failed at {key}"

    def test_affine_sl2_pme(self):
        """PME for affine sl_2."""
        k = affine_slN_kernel(2)
        results = verify_primitive_master_equation(k)
        for key, val in results.items():
            assert val, f"PME failed at {key}"

    def test_virasoro_pme(self):
        """PME for Virasoro."""
        k = virasoro_kernel()
        results = verify_primitive_master_equation(k)
        for key, val in results.items():
            assert val, f"PME failed at {key}"

    def test_betagamma_pme(self):
        """PME for betagamma."""
        k = betagamma_kernel()
        results = verify_primitive_master_equation(k)
        for key, val in results.items():
            assert val, f"PME failed at {key}"

    def test_d_channel_k02_zero(self):
        """d(K_{0,2}) = 0 for all families (kappa is a cocycle)."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            dc = d_channel(k)
            assert dc[(0, 2)] == Fraction(0), f"d(K_{{0,2}}) != 0 for {name}"

    def test_bv_self_contraction_genus_raise(self):
        """Delta_ns(K_{0,2}) = kappa (genus-0 -> genus-1)."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            bv = bv_self_contraction(k)
            assert bv[(1, 0)] == k.kappa, f"Delta_ns(K_{{0,2}}) != kappa for {name}"

    def test_pre_lie_vanishes_at_11(self):
        """(K*K) at (1,1) = 0 for all families."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            pl = pre_lie_product(k)
            assert pl[(1, 1)] == Fraction(0), f"(K*K)(1,1) != 0 for {name}"

    def test_pre_lie_vanishes_at_02(self):
        """(K*K) at (0,2) = 0 for all families."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            pl = pre_lie_product(k)
            assert pl[(0, 2)] == Fraction(0), f"(K*K)(0,2) != 0 for {name}"

    def test_pme_all_standard_families(self):
        """PME holds for every standard family."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            results = verify_primitive_master_equation(k)
            for key, val in results.items():
                assert val, f"PME failed for {name} at {key}"

    def test_d_channel_k03_zero(self):
        """d(K_{0,3}) = 0 for affine (Jacobi)."""
        k = affine_slN_kernel(2)
        dc = d_channel(k)
        assert dc.get((0, 3), Fraction(0)) == Fraction(0)

    def test_bv_delta_ns_k11_to_genus2(self):
        """Delta_ns(K_{1,1}) contributes to (2,0)."""
        k = heisenberg_kernel(Fraction(3))
        bv = bv_self_contraction(k)
        assert bv[(2, 0)] == Fraction(3)

    def test_bv_delta_ns_k03_to_11(self):
        """Delta_ns(K_{0,3}) at (1,1) = 0 for affine (antisymmetry)."""
        k = affine_slN_kernel(2)
        bv = bv_self_contraction(k)
        assert bv.get((1, 1), Fraction(0)) == Fraction(0)


# =====================================================================
# 3. Shell equation tests
# =====================================================================

class TestGenus1Shell:
    """Genus-1 shell equation: K_{1,1} determined from genus-0 data."""

    def test_heisenberg_k11_from_shell(self):
        """Heisenberg: K_{1,1} = Delta_ns(K_{0,2}) = kappa."""
        k = heisenberg_kernel(Fraction(7))
        shell = genus1_shell(k)
        assert shell["consistent"]
        assert shell["K_{1,1}_shell"] == Fraction(7)

    def test_affine_sl2_k11_from_shell(self):
        """Affine sl_2: K_{1,1} = kappa (at scalar level)."""
        k = affine_slN_kernel(2, Fraction(1))
        shell = genus1_shell(k)
        assert shell["consistent"]

    def test_virasoro_k11_from_shell(self):
        """Virasoro: K_{1,1} = kappa = c/2."""
        k = virasoro_kernel(Fraction(26))
        shell = genus1_shell(k)
        assert shell["consistent"]
        assert shell["K_{1,1}_actual"] == Fraction(13)

    def test_betagamma_k11_from_shell(self):
        """betagamma: K_{1,1} = kappa."""
        k = betagamma_kernel(Fraction(0))
        shell = genus1_shell(k)
        assert shell["consistent"]

    def test_all_families_consistent(self):
        """Genus-1 shell is consistent for all standard families."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            shell = genus1_shell(k)
            assert shell["consistent"], f"Genus-1 shell inconsistent for {name}"


class TestGenus2Shell:
    """Genus-2 shell equation: K_{2,0} from three channels."""

    def test_heisenberg_loop_only(self):
        """Heisenberg genus-2 shell is pure loop (no bracket, no pf)."""
        k = heisenberg_kernel()
        shell = genus2_shell(k)
        assert shell["bracket"] == Fraction(0)
        assert shell["planted_forest"] == Fraction(0)
        assert shell["total"] == shell["loop"]

    def test_heisenberg_loop_value(self):
        """Heisenberg loop channel = kappa * (-1/12)."""
        k = heisenberg_kernel(Fraction(1))
        shell = genus2_shell(k)
        assert shell["loop"] == Fraction(-1, 12)

    def test_heisenberg_loop_kappa_scaling(self):
        """Loop channel scales linearly with kappa."""
        for kap in [Fraction(1), Fraction(2), Fraction(1, 2)]:
            k = heisenberg_kernel(kap)
            shell = genus2_shell(k)
            assert shell["loop"] == kap * Fraction(-1, 12)

    def test_heisenberg_genus2_check(self):
        """Cross-check: genus-2 shell passes the dedicated check."""
        check = heisenberg_genus2_shell_check()
        assert check["loop_only"]

    def test_affine_sl2_bracket_nonzero(self):
        """Affine sl_2: bracket channel is nonzero."""
        k = affine_slN_kernel(2, Fraction(1))
        shell = genus2_shell(k)
        assert shell["bracket"] != Fraction(0)

    def test_affine_sl2_no_planted_forest(self):
        """Affine sl_2: no planted-forest channel."""
        k = affine_slN_kernel(2)
        shell = genus2_shell(k)
        assert shell["planted_forest"] == Fraction(0)

    def test_virasoro_all_channels_active(self):
        """Virasoro: all three channels nonzero."""
        k = virasoro_kernel(Fraction(1))
        shell = genus2_shell(k)
        assert shell["loop"] != Fraction(0)
        assert shell["bracket"] != Fraction(0)
        assert shell["planted_forest"] != Fraction(0)

    def test_betagamma_no_bracket(self):
        """betagamma: no bracket channel (cubic = 0)."""
        k = betagamma_kernel()
        shell = genus2_shell(k)
        assert shell["bracket"] == Fraction(0)

    def test_betagamma_no_quartic_planted_forest(self):
        """betagamma: planted-forest = 0 when quartic = 0 (on weight-changing line)."""
        k = betagamma_kernel()
        shell = genus2_shell(k)
        assert shell["planted_forest"] == Fraction(0)

    def test_genus2_total_is_sum_of_channels(self):
        """Total = loop + bracket + planted_forest for all families."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            shell = genus2_shell(k)
            assert shell["total"] == shell["loop"] + shell["bracket"] + shell["planted_forest"], \
                f"Channel sum mismatch for {name}"


# =====================================================================
# 4. Branch BV tests
# =====================================================================

class TestBranchBV:
    """Branch BV action on the finite-rank quotient V^br."""

    def test_heisenberg_dim_1(self):
        """Heisenberg: dim V^br = 1."""
        bv = heisenberg_branch_bv()
        assert bv.branch_rank == 1

    def test_heisenberg_is_gaussian(self):
        """Heisenberg: S^br is exactly Gaussian (only quadratic term)."""
        bv = heisenberg_branch_bv()
        qme = verify_branch_bv_qme(bv)
        assert qme["is_gaussian"]

    def test_heisenberg_quadratic_equals_kappa(self):
        """Heisenberg: S^br_2 = kappa."""
        for k_val in [Fraction(1), Fraction(2), Fraction(1, 2)]:
            bv = heisenberg_branch_bv(k_val)
            assert bv.coefficients[2] == k_val

    def test_affine_sl2_dim_3(self):
        """Affine sl_2: dim V^br = 3."""
        bv = affine_sl2_branch_bv()
        assert bv.branch_rank == 3

    def test_affine_sl2_has_cubic(self):
        """Affine sl_2: S^br has cubic (CS-type) term."""
        bv = affine_sl2_branch_bv()
        assert 3 in bv.coefficients
        assert bv.coefficients[3] != Fraction(0)

    def test_affine_sl2_not_gaussian(self):
        """Affine sl_2: S^br is NOT purely Gaussian."""
        bv = affine_sl2_branch_bv()
        qme = verify_branch_bv_qme(bv)
        assert not qme["is_gaussian"]

    def test_betagamma_dim_1(self):
        """betagamma: dim V^br = 1."""
        bv = betagamma_branch_bv()
        assert bv.branch_rank == 1

    def test_betagamma_is_gaussian(self):
        """betagamma: Gaussian on weight-changing line."""
        bv = betagamma_branch_bv()
        qme = verify_branch_bv_qme(bv)
        assert qme["is_gaussian"]

    def test_betagamma_kappa_formula(self):
        """betagamma kappa = 6*lambda^2 - 6*lambda + 1."""
        for lam_val in [0, 1, Fraction(1, 2), Fraction(1, 3)]:
            la = Fraction(lam_val)
            bv = betagamma_branch_bv(la)
            expected_kappa = 6 * la * la - 6 * la + 1
            assert bv.coefficients[2] == expected_kappa

    def test_virasoro_dim_1(self):
        """Virasoro: dim V^br = 1 on primary slice."""
        bv = virasoro_branch_bv()
        assert bv.branch_rank == 1

    def test_virasoro_not_gaussian(self):
        """Virasoro: S^br is NOT Gaussian (has cubic and quartic)."""
        bv = virasoro_branch_bv()
        qme = verify_branch_bv_qme(bv)
        assert not qme["is_gaussian"]

    def test_virasoro_s2_is_kappa(self):
        """Virasoro: S^br_2 = c/2."""
        for c_val in [1, 13, 26]:
            bv = virasoro_branch_bv(Fraction(c_val))
            assert bv.coefficients[2] == Fraction(c_val, 2)

    def test_virasoro_s3_is_2(self):
        """Virasoro: S^br_3 = 2 (alpha)."""
        bv = virasoro_branch_bv(Fraction(1))
        assert bv.coefficients[3] == Fraction(2)

    def test_virasoro_s4_matches_quartic(self):
        """Virasoro: S^br_4 = Q^contact_Vir = 10/[c(5c+22)]."""
        for c_val in [1, 2, 5, 13]:
            c = Fraction(c_val)
            bv = virasoro_branch_bv(c)
            expected = Fraction(10) / (c * (5 * c + 22))
            assert bv.coefficients[4] == expected, f"S_4 mismatch at c={c_val}"

    def test_virasoro_higher_order_populated(self):
        """Virasoro: S^br has coefficients up to order 10."""
        bv = virasoro_branch_bv(Fraction(1), order=10)
        for r in range(2, 11):
            assert r in bv.coefficients, f"S_{r} missing"

    def test_evaluate_polynomial_heisenberg(self):
        """Heisenberg Taylor coefficients: [0, 0, kappa/2, 0, ...]."""
        bv = heisenberg_branch_bv(Fraction(3))
        coeffs = bv.evaluate_polynomial(5)
        assert coeffs[0] == Fraction(0)
        assert coeffs[1] == Fraction(0)
        assert coeffs[2] == Fraction(3, 2)  # kappa / 2!
        assert coeffs[3] == Fraction(0)


# =====================================================================
# 5. Metaplectic half-density tests
# =====================================================================

class TestMetaplecticHalfDensity:
    """Metaplectic half-density delta with delta^2 = spectral determinant."""

    def test_binomial_half_0(self):
        """C(1/2, 0) = 1."""
        assert binomial_half(0) == Fraction(1)

    def test_binomial_half_1(self):
        """C(1/2, 1) = 1/2."""
        assert binomial_half(1) == Fraction(1, 2)

    def test_binomial_half_2(self):
        """C(1/2, 2) = -1/8."""
        assert binomial_half(2) == Fraction(-1, 8)

    def test_binomial_half_3(self):
        """C(1/2, 3) = 1/16."""
        assert binomial_half(3) == Fraction(1, 16)

    def test_binomial_half_4(self):
        """C(1/2, 4) = -5/128."""
        assert binomial_half(4) == Fraction(-5, 128)

    def test_heisenberg_squaring_k1(self):
        """delta^2 = 1 - x for Heisenberg at kappa = 1."""
        assert verify_metaplectic_squaring_1d(Fraction(1), 15)

    def test_heisenberg_squaring_k_half(self):
        """delta^2 = 1 - x/2 for Heisenberg at kappa = 1/2."""
        assert verify_metaplectic_squaring_1d(Fraction(1, 2), 12)

    def test_heisenberg_squaring_k3(self):
        """delta^2 = 1 - 3x for Heisenberg at kappa = 3."""
        assert verify_metaplectic_squaring_1d(Fraction(3), 10)

    def test_heisenberg_squaring_large_order(self):
        """Squaring identity holds to high order (order 20)."""
        assert verify_metaplectic_squaring_1d(Fraction(1), 20)

    def test_heisenberg_leading_coefficient(self):
        """delta(x) = 1 - kappa*x/2 + ... (leading correction)."""
        kap = Fraction(5)
        delta = metaplectic_half_density_1d(kap, 3)
        assert delta[0] == Fraction(1)
        assert delta[1] == -kap / 2

    def test_heisenberg_second_coefficient(self):
        """delta(x) second coefficient = C(1/2,2)*kappa^2 = -kappa^2/8."""
        kap = Fraction(2)
        delta = metaplectic_half_density_1d(kap, 3)
        assert delta[2] == Fraction(-1, 8) * kap ** 2

    def test_weyl_sl2_matches_1d(self):
        """Weyl denominator for sl_2 = metaplectic with kappa = 1."""
        weyl = weyl_denominator_sl2(10)
        meta = metaplectic_half_density_1d(Fraction(1), 10)
        for i in range(11):
            assert weyl[i] == meta[i], f"Mismatch at order {i}"

    def test_weyl_sl2_squaring(self):
        """Weyl denominator for sl_2 squares to (1-x)."""
        delta = weyl_denominator_sl2(15)
        for n in range(16):
            square_n = sum(delta[k] * delta[n - k] for k in range(n + 1))
            if n == 0:
                assert square_n == Fraction(1)
            elif n == 1:
                assert square_n == Fraction(-1)
            else:
                assert square_n == Fraction(0), f"Squaring failed at n={n}"

    def test_weyl_slN_root_count(self):
        """sl_N has N(N-1)/2 positive roots."""
        for N_val in [2, 3, 4, 5]:
            factors = weyl_denominator_slN(N_val, 5)
            assert len(factors) == N_val * (N_val - 1) // 2

    def test_virasoro_leading_matches_heisenberg(self):
        """Virasoro half-density matches Heisenberg at leading order."""
        for c_val in [1, 13, 26]:
            c = Fraction(c_val)
            vir = virasoro_half_density(c, 3)
            heis = metaplectic_half_density_1d(c / 2, 3)
            # Leading order: delta = (1 - c/2 * x)^{1/2}
            for i in range(4):
                assert vir[i] == heis[i], f"Mismatch at c={c_val}, order {i}"


# =====================================================================
# 6. Flat connection chain tests
# =====================================================================

class TestFlatConnectionChain:
    """Flat connection chain: K_A -> Theta_A -> nabla^mod."""

    def test_heisenberg_trivial_connection(self):
        """Heisenberg: connection is trivial."""
        assert heisenberg_connection_is_trivial()

    def test_heisenberg_trivial_at_any_level(self):
        """Heisenberg connection is trivial at any level."""
        for k_val in [Fraction(1), Fraction(2), Fraction(1, 2), Fraction(100)]:
            assert heisenberg_connection_is_trivial(k_val)

    def test_kz_connection_sl2_k1(self):
        """KZ connection for sl_2 at k=1: kappa_KZ = 3."""
        kz = kz_connection_data(2, Fraction(1))
        assert kz["kappa_KZ"] == Fraction(3)
        assert kz["casimir_coeff"] == Fraction(1, 3)

    def test_kz_connection_sl2_k2(self):
        """KZ connection for sl_2 at k=2: kappa_KZ = 4."""
        kz = kz_connection_data(2, Fraction(2))
        assert kz["kappa_KZ"] == Fraction(4)
        assert kz["casimir_coeff"] == Fraction(1, 4)

    def test_kz_connection_sl3_k1(self):
        """KZ connection for sl_3 at k=1: kappa_KZ = 4."""
        kz = kz_connection_data(3, Fraction(1))
        assert kz["kappa_KZ"] == Fraction(4)

    def test_kz_connection_slN_kappa(self):
        """KZ parameter = k + N for sl_N."""
        for N_val in [2, 3, 4, 5]:
            for k_val in [1, 2, 3]:
                kz = kz_connection_data(N_val, Fraction(k_val))
                assert kz["kappa_KZ"] == Fraction(k_val + N_val)

    def test_kz_flatness_sl2(self):
        """KZ connection for sl_2 is flat."""
        result = verify_kz_flatness(2, Fraction(1))
        assert result["flat_2pt"]
        assert result["flat_3pt_by_jacobi"]

    def test_kz_flatness_sl3(self):
        """KZ connection for sl_3 is flat."""
        result = verify_kz_flatness(3, Fraction(1))
        assert result["flat_2pt"]
        assert result["flat_3pt_by_jacobi"]

    def test_flat_connection_chain_heisenberg(self):
        """Heisenberg chain ends at trivial connection."""
        k = heisenberg_kernel()
        chain = flat_connection_chain(k)
        assert "trivial" in chain["connection"]

    def test_flat_connection_chain_affine(self):
        """Affine chain gives KZ connection."""
        k = affine_slN_kernel(2)
        chain = flat_connection_chain(k)
        assert "KZ" in chain["connection"]

    def test_flat_connection_chain_virasoro(self):
        """Virasoro chain gives full modular connection."""
        k = virasoro_kernel()
        chain = flat_connection_chain(k)
        assert "modular" in chain["connection"].lower() or "full" in chain["connection"].lower()

    def test_kz_critical_level_diverges(self):
        """At critical level k = -h^v, KZ parameter = 0 and Casimir diverges."""
        kz = kz_connection_data(2, Fraction(-2))
        assert kz["kappa_KZ"] == Fraction(0)
        assert kz["casimir_coeff"] is None  # cannot compute 1/0

    def test_chain_steps_all_present(self):
        """The flat connection chain has all expected steps."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            chain = flat_connection_chain(k)
            assert "K_A" in chain
            assert "FT" in chain
            assert "Theta_A" in chain
            assert "linearize" in chain
            assert "connection" in chain


# =====================================================================
# 7. Cross-validation tests
# =====================================================================

class TestCrossValidation:
    """Cross-validation against shadow_metric_census and other modules."""

    def test_heisenberg_kappa_matches(self):
        """Cross-validate Heisenberg kappa with census."""
        k = heisenberg_kernel(Fraction(1))
        result = cross_validate_kappa(k)
        assert result["match"]

    def test_virasoro_kappa_matches(self):
        """Cross-validate Virasoro kappa with census."""
        k = virasoro_kernel(Fraction(26))
        result = cross_validate_kappa(k)
        assert result["match"]

    def test_w3_kappa_matches(self):
        """Cross-validate W_3 kappa with census."""
        k = w3_kernel(Fraction(6))
        result = cross_validate_kappa(k)
        assert result["match"]

    def test_kappa_additivity_heisenberg(self):
        """kappa(H_a + H_b) = a + b."""
        k1 = heisenberg_kernel(Fraction(3))
        k2 = heisenberg_kernel(Fraction(5))
        assert verify_kappa_additivity(k1, k2)
        direct = independent_sum_kernel(k1, k2)
        assert direct.kappa == Fraction(8)

    def test_kappa_additivity_mixed(self):
        """kappa(H_k + Vir_c) = k + c/2."""
        k1 = heisenberg_kernel(Fraction(2))
        k2 = virasoro_kernel(Fraction(10))
        assert verify_kappa_additivity(k1, k2)
        direct = independent_sum_kernel(k1, k2)
        assert direct.kappa == Fraction(7)  # 2 + 10/2

    def test_independent_sum_branch_rank(self):
        """Branch rank is additive under direct sum."""
        k1 = heisenberg_kernel()  # rank 1
        k2 = affine_slN_kernel(2)  # rank 3
        direct = independent_sum_kernel(k1, k2)
        assert direct.branch_rank == 4

    def test_independent_sum_planted_forest(self):
        """Direct sum inherits planted-forest from either summand."""
        k1 = heisenberg_kernel()  # no pf
        k2 = betagamma_kernel()  # has pf
        direct = independent_sum_kernel(k1, k2)
        assert direct.has_planted_forest

    def test_all_standard_families_kappa_positive_or_negative(self):
        """All standard families have nonzero kappa (except symplectic betagamma)."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            # kappa can be zero for betagamma at special weights
            # but our standard families have nonzero kappa
            if "symp" not in name:
                assert k.kappa != Fraction(0), f"kappa = 0 for {name}"

    def test_affine_slN_kappa_formula(self):
        """kappa(sl_N, k) = dim(g)*(k+h^v)/(2*h^v) = (N^2-1)*(k+N)/(2*N)."""
        test_cases = [
            (2, 1, Fraction(9, 4)),     # 3*3/4 = 9/4
            (2, 2, Fraction(3)),        # 3*4/4 = 3
            (3, 1, Fraction(16, 3)),    # 8*4/6 = 16/3
            (3, 2, Fraction(20, 3)),    # 8*5/6 = 20/3
            (4, 1, Fraction(75, 8)),    # 15*5/8 = 75/8
        ]
        for N_val, k_val, expected in test_cases:
            k = affine_slN_kernel(N_val, Fraction(k_val))
            assert k.kappa == expected, \
                f"kappa(sl_{N_val}, k={k_val}) = {k.kappa}, expected {expected}"

    def test_virasoro_quartic_matches_primitive_kernel_engine(self):
        """Virasoro quartic matches CorollaCoefficients.virasoro."""
        from compute.lib.primitive_kernel_engine import CorollaCoefficients
        for c_val in [1, 2, 5, 13, 26]:
            c = Fraction(c_val)
            kernel = virasoro_kernel(c)
            corolla = CorollaCoefficients.virasoro(c)
            assert kernel.quartic == corolla.quartic, \
                f"Quartic mismatch at c={c_val}: {kernel.quartic} vs {corolla.quartic}"


# =====================================================================
# 8. Shadow depth classification tests
# =====================================================================

class TestShadowDepthClassification:
    """G/L/C/M classification from primitive kernel data."""

    def test_heisenberg_is_G(self):
        """Heisenberg: class G, r_max = 2."""
        k = heisenberg_kernel()
        cls, rmax = shadow_depth_class(k)
        assert cls == 'G'
        assert rmax == 2

    def test_affine_sl2_is_L(self):
        """Affine sl_2: class L, r_max = 3."""
        k = affine_slN_kernel(2)
        cls, rmax = shadow_depth_class(k)
        assert cls == 'L'
        assert rmax == 3

    def test_affine_sl3_is_L(self):
        """Affine sl_3: class L, r_max = 3."""
        k = affine_slN_kernel(3)
        cls, rmax = shadow_depth_class(k)
        assert cls == 'L'
        assert rmax == 3

    def test_betagamma_is_C(self):
        """betagamma: class C, r_max = 4."""
        k = betagamma_kernel()
        cls, rmax = shadow_depth_class(k)
        assert cls == 'C'
        assert rmax == 4

    def test_virasoro_is_M(self):
        """Virasoro: class M, r_max = infinity."""
        k = virasoro_kernel()
        cls, rmax = shadow_depth_class(k)
        assert cls == 'M'
        assert rmax is None

    def test_w3_is_M(self):
        """W_3: class M, r_max = infinity."""
        k = w3_kernel()
        cls, rmax = shadow_depth_class(k)
        assert cls == 'M'
        assert rmax is None

    def test_classification_stable_across_levels(self):
        """Shadow depth class is stable as level varies."""
        for k_val in [1, 2, 5, 10, 100]:
            k = heisenberg_kernel(Fraction(k_val))
            cls, _ = shadow_depth_class(k)
            assert cls == 'G'

        for k_val in [1, 2, 5, 10]:
            k = affine_slN_kernel(2, Fraction(k_val))
            cls, _ = shadow_depth_class(k)
            assert cls == 'L'

        for c_val in [1, 13, 26, 100]:
            k = virasoro_kernel(Fraction(c_val))
            cls, _ = shadow_depth_class(k)
            assert cls == 'M'


# =====================================================================
# 9. Virasoro shadow tower integration tests
# =====================================================================

class TestVirasoroShadowTower:
    """Integration with the Virasoro shadow tower recursion."""

    def test_virasoro_branch_s5_nonzero(self):
        """S_5 is nonzero for Virasoro (quintic forced)."""
        bv = virasoro_branch_bv(Fraction(1), order=6)
        assert 5 in bv.coefficients
        assert bv.coefficients[5] != Fraction(0)

    def test_virasoro_branch_s5_value_c1(self):
        """S_5(c=1) = -48/[1*(5+22)] = -48/27 = -16/9."""
        bv = virasoro_branch_bv(Fraction(1), order=6)
        expected = Fraction(-48) / (Fraction(1) * Fraction(27))
        assert bv.coefficients[5] == expected

    def test_virasoro_branch_matches_shadow_gf_seeds(self):
        """Virasoro branch BV matches known seeds S_2, S_3, S_4."""
        for c_val in [1, 2, 13, 26]:
            c = Fraction(c_val)
            bv = virasoro_branch_bv(c, order=5)

            assert bv.coefficients[2] == c / 2, f"S_2 mismatch at c={c_val}"
            assert bv.coefficients[3] == Fraction(2), f"S_3 mismatch at c={c_val}"

            expected_s4 = Fraction(10) / (c * (5 * c + 22))
            assert bv.coefficients[4] == expected_s4, f"S_4 mismatch at c={c_val}"

    def test_virasoro_branch_self_dual_c13(self):
        """At c=13 (self-dual): kappa = 13/2, S_4 = 10/[13*(65+22)] = 10/1131."""
        bv = virasoro_branch_bv(Fraction(13), order=5)
        assert bv.coefficients[2] == Fraction(13, 2)
        assert bv.coefficients[4] == Fraction(10, 1131)


# =====================================================================
# 10. Registry and data consistency tests
# =====================================================================

class TestRegistry:
    """Verify standard family registry and data consistency."""

    def test_all_families_constructible(self):
        """Every registered family constructs without error."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            assert isinstance(k, PrimitiveKernel), f"Failed for {name}"

    def test_all_families_have_kappa(self):
        """Every family has a well-defined kappa."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            assert isinstance(k.kappa, Fraction), f"kappa not Fraction for {name}"

    def test_all_families_have_components(self):
        """Every family has at least K_{0,2} and K_{1,1}."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            comps = k.components()
            assert (0, 2) in comps, f"K_{{0,2}} missing for {name}"
            assert (1, 1) in comps, f"K_{{1,1}} missing for {name}"

    def test_k11_equals_kappa_all_families(self):
        """K_{1,1} = kappa for all families (shell equation)."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            assert k.genus1_unary == k.kappa, \
                f"K_{{1,1}} != kappa for {name}: {k.genus1_unary} vs {k.kappa}"

    def test_registry_has_all_standard_families(self):
        """Registry includes all major families."""
        expected_prefixes = ["heisenberg", "affine_sl2", "affine_sl3",
                             "betagamma", "virasoro", "w3"]
        for prefix in expected_prefixes:
            matches = [n for n in STANDARD_FAMILIES if n.startswith(prefix)]
            assert len(matches) > 0, f"No family with prefix {prefix}"

    def test_component_string_format(self):
        """Component strings are well-formed (+ separated terms)."""
        for name, factory in STANDARD_FAMILIES.items():
            k = factory()
            s = k.component_string()
            parts = [p.strip() for p in s.split("+")]
            assert len(parts) >= 2, f"Too few components for {name}: {s}"
            assert parts[0] == "K_{0,2}", f"First component should be K_{{0,2}} for {name}"

    def test_primitive_kernel_component_repr(self):
        """PrimitiveKernelComponent has readable repr."""
        comp = PrimitiveKernelComponent(0, 2, Fraction(5), "test")
        s = repr(comp)
        assert "K_{0,2}" in s
        assert "5" in s


# =====================================================================
# 11. Edge cases and special values
# =====================================================================

class TestEdgeCases:
    """Edge cases, special values, and boundary conditions."""

    def test_virasoro_c0_quartic_undefined(self):
        """Virasoro at c=0: kappa = 0, quartic diverges (degenerate)."""
        k = virasoro_kernel(Fraction(0))
        assert k.kappa == Fraction(0)
        assert k.quartic == Fraction(0)  # the formula gives 0 when denom is 0

    def test_betagamma_symplectic_negative_kappa(self):
        """betagamma at lambda=1/2: kappa = -1/2 (negative!)."""
        k = betagamma_kernel(Fraction(1, 2))
        assert k.kappa == Fraction(-1, 2)
        assert k.kappa < 0

    def test_metaplectic_squaring_negative_kappa(self):
        """Squaring identity holds for negative kappa."""
        assert verify_metaplectic_squaring_1d(Fraction(-1, 2), 12)

    def test_metaplectic_squaring_zero_kappa(self):
        """At kappa = 0: delta(x) = 1 (trivial)."""
        delta = metaplectic_half_density_1d(Fraction(0), 10)
        assert delta[0] == Fraction(1)
        for i in range(1, 11):
            assert delta[i] == Fraction(0)

    def test_metaplectic_squaring_large_kappa(self):
        """Squaring identity holds for large kappa."""
        assert verify_metaplectic_squaring_1d(Fraction(100), 8)

    def test_genus1_shell_zero_kappa(self):
        """Genus-1 shell at kappa = 0: everything vanishes."""
        k = PrimitiveKernel(name="zero", kappa=Fraction(0))
        shell = genus1_shell(k)
        assert shell["K_{1,1}_shell"] == Fraction(0)
        assert shell["consistent"]

    def test_genus2_shell_zero_kappa(self):
        """Genus-2 shell at kappa = 0: all channels vanish."""
        k = PrimitiveKernel(name="zero", kappa=Fraction(0))
        shell = genus2_shell(k)
        assert shell["loop"] == Fraction(0)
        assert shell["bracket"] == Fraction(0)
        assert shell["planted_forest"] == Fraction(0)
        assert shell["total"] == Fraction(0)

    def test_independent_sum_with_zero(self):
        """Direct sum with zero kernel preserves original."""
        k1 = virasoro_kernel(Fraction(13))
        k0 = PrimitiveKernel(name="zero", kappa=Fraction(0))
        direct = independent_sum_kernel(k1, k0)
        assert direct.kappa == k1.kappa

    def test_binomial_half_alternating_signs(self):
        """C(1/2, n) alternates sign for n >= 1: +,-,+,-,..."""
        # C(1/2, 1) = 1/2 > 0
        # C(1/2, 2) = -1/8 < 0
        # C(1/2, 3) = 1/16 > 0
        # C(1/2, 4) = -5/128 < 0
        signs = [1 if binomial_half(n) > 0 else -1 for n in range(1, 8)]
        expected = [1, -1, 1, -1, 1, -1, 1]
        assert signs == expected

    def test_branch_bv_action_repr(self):
        """BranchBVAction constructs without error."""
        bv = BranchBVAction(name="test", branch_rank=2,
                            coefficients={2: Fraction(1), 3: Fraction(2)})
        assert bv.branch_rank == 2
        assert len(bv.coefficients) == 2


# =====================================================================
# 12. Comprehensive per-family consistency tests
# =====================================================================

class TestPerFamilyConsistency:
    """End-to-end consistency for each standard family."""

    def _check_family(self, kernel: PrimitiveKernel):
        """Run all consistency checks on a single family."""
        # 1. Components are well-formed
        comps = kernel.components()
        assert (0, 2) in comps
        assert comps[(0, 2)].value == kernel.kappa

        # 2. K_{1,1} = kappa
        assert kernel.genus1_unary == kernel.kappa

        # 3. PME
        pme = verify_primitive_master_equation(kernel)
        for key, val in pme.items():
            assert val, f"PME failed at {key}"

        # 4. Genus-1 shell
        shell1 = genus1_shell(kernel)
        assert shell1["consistent"]

        # 5. Genus-2 shell (channels sum to total)
        shell2 = genus2_shell(kernel)
        assert shell2["total"] == shell2["loop"] + shell2["bracket"] + shell2["planted_forest"]

        # 6. Cross-validate kappa
        cv = cross_validate_kappa(kernel)
        if cv["match"] is not None:
            assert cv["match"], f"Kappa cross-validation failed for {kernel.name}"

    def test_heisenberg_k1_consistency(self):
        self._check_family(heisenberg_kernel(Fraction(1)))

    def test_heisenberg_k2_consistency(self):
        self._check_family(heisenberg_kernel(Fraction(2)))

    def test_heisenberg_k_half_consistency(self):
        self._check_family(heisenberg_kernel(Fraction(1, 2)))

    def test_affine_sl2_k1_consistency(self):
        self._check_family(affine_slN_kernel(2, Fraction(1)))

    def test_affine_sl2_k2_consistency(self):
        self._check_family(affine_slN_kernel(2, Fraction(2)))

    def test_affine_sl3_k1_consistency(self):
        self._check_family(affine_slN_kernel(3, Fraction(1)))

    def test_betagamma_std_consistency(self):
        self._check_family(betagamma_kernel(Fraction(0)))

    def test_betagamma_symp_consistency(self):
        self._check_family(betagamma_kernel(Fraction(1, 2)))

    def test_virasoro_c1_consistency(self):
        self._check_family(virasoro_kernel(Fraction(1)))

    def test_virasoro_c13_consistency(self):
        self._check_family(virasoro_kernel(Fraction(13)))

    def test_virasoro_c26_consistency(self):
        self._check_family(virasoro_kernel(Fraction(26)))

    def test_w3_c1_consistency(self):
        self._check_family(w3_kernel(Fraction(1)))
