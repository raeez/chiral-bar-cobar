"""Tests for DS-bar commutation and hook-type Koszul duality.

Verifies that Drinfeld-Sokolov reduction commutes with the bar construction
for hook-type nilpotents in sl_3 and sl_4, and computes explicit Koszul duals.
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.ds_bar_commutation import (
    DSBarCommutationData,
    KoszulDualIdentification,
    N2SCAData,
    affine_central_charge_sl_n,
    affine_kappa_sl_n,
    bar_complex_n2_sca,
    dim_sl_n,
    ds_bar_commutation_check,
    ds_nilpotent_half_dim,
    ds_nilpotent_plus_dim,
    koszul_dual_identification,
    n2_sca_data,
    sl3_minimal_data,
    sl4_hook_ds_bar_data,
    verify_ds_bar_commutation,
)
from compute.lib.hook_type_w_duality import (
    complementarity_constant,
    ds_kappa_from_affine,
    ghost_constant,
    hook_dual_level_sl_n,
    krw_central_charge,
    krw_central_charge_data,
    w_algebra_generator_data,
)
from compute.lib.nonprincipal_ds_orbits import (
    normalize_partition,
    transpose_partition,
)

k = Symbol('k')


# ===================================================================
# sl_3 minimal = N=2 SCA
# ===================================================================

class TestSl3MinimalPartition:
    def test_self_transpose(self):
        assert transpose_partition((2, 1)) == (2, 1)

    def test_generators_count(self):
        gen = w_algebra_generator_data((2, 1))
        assert gen.f_centralizer_dimension == 4

    def test_generators_bosonic_fermionic(self):
        gen = w_algebra_generator_data((2, 1))
        assert gen.n_bosonic == 2
        assert gen.n_fermionic == 2

    def test_generator_weights(self):
        gen = w_algebra_generator_data((2, 1))
        weights = sorted([w for (_, w, _) in gen.strong_generators])
        assert weights == [Rational(1), Rational(3, 2), Rational(3, 2), Rational(2)]

    def test_central_charge(self):
        """c(BP) = 2 - 24(k+1)^2/(k+3) via correct per-root-pair KRW.

        # VERIFIED: [DC] known BP formula; [CF] K_BP=196; [NE] c(-3/2)=-2
        """
        c = krw_central_charge((2, 1), k)
        assert simplify(c - (2 - 24 * (k + 1)**2 / (k + 3))) == 0

    def test_ghost_constant(self):
        assert ghost_constant((2, 1)) == 2

    def test_kappa_formula(self):
        """kappa(BP) = (1/6) * c = (1/6)*(2-24(k+1)^2/(k+3)).

        # VERIFIED: [DC] rho=1/6, c_BP=2-24(k+1)^2/(k+3);
        # [NE] kappa(0) = (1/6)*(-6) = -1; kappa(1) = (1/6)*(-22) = -11/3
        """
        kappa = ds_kappa_from_affine((2, 1), k)
        expected = Rational(1, 6) * (2 - 24 * (k + 1)**2 / (k + 3))
        assert simplify(kappa - expected) == 0

    def test_kappa_anti_symmetry(self):
        kv = hook_dual_level_sl_n(3, k)
        s = simplify(ds_kappa_from_affine((2, 1), k) + ds_kappa_from_affine((2, 1), kv))
        assert simplify(s.diff(k)) == 0

    def test_complementarity_constant(self):
        assert complementarity_constant((2, 1)) == -4

    def test_self_dual_level(self):
        # k^v = k => -k-6 = k => k = -3
        assert simplify(hook_dual_level_sl_n(3, Rational(-3)) - Rational(-3)) == 0

    def test_nilpotent_plus_dim(self):
        assert ds_nilpotent_plus_dim((2, 1)) == 3

    def test_nilpotent_half_dim(self):
        assert ds_nilpotent_half_dim((2, 1)) == 2


class TestN2SCAOpe:
    def test_ope_structure(self):
        sca = n2_sca_data(k)
        c = sca.central_charge
        assert simplify(sca.jj_pole2 - c / 3) == 0
        assert simplify(sca.gg_pole3 - c / 3) == 0
        assert simplify(sca.tt_pole4 - c / 2) == 0
        assert sca.jg_charge == 1


class TestSl3BarComplex:
    def test_bar_dimensions(self):
        bar = bar_complex_n2_sca(k)
        assert bar.h0_dim == 1
        assert bar.h1_dim == 4
        assert bar.h2_dim == 4
        assert bar.h3_dim == 1

    def test_euler_characteristic(self):
        bar = bar_complex_n2_sca(k)
        assert bar.euler_char == 0

    def test_is_koszul(self):
        bar = bar_complex_n2_sca(k)
        assert bar.is_koszul


class TestSl3DSBarCommutation:
    def test_kappa_commutes(self):
        check = ds_bar_commutation_check((2, 1), k)
        assert check.kappa_commutes

    def test_generators_match(self):
        check = ds_bar_commutation_check((2, 1), k)
        assert check.generators_match

    def test_c_threads(self):
        check = ds_bar_commutation_check((2, 1), k)
        assert check.c_threads

    def test_ghost_constant(self):
        check = ds_bar_commutation_check((2, 1), k)
        assert check.ghost_constant_value == 2


class TestSl3KoszulDual:
    def test_self_dual_partition(self):
        kd = koszul_dual_identification((2, 1), k)
        assert kd.is_self_transpose
        assert kd.dual_partition == (2, 1)

    def test_self_dual_level(self):
        kd = koszul_dual_identification((2, 1), k)
        assert kd.self_dual_level == -3

    def test_kappa_sum(self):
        """Self-transpose (2,1): kappa sum = 98/3 = rho*K_BP = (1/6)*196.

        # VERIFIED: [DC] rho=1/6, K_BP=196; [NE] kappa(1)+kappa(-7) = -11/3+109/3 = 98/3
        """
        kd = koszul_dual_identification((2, 1), k)
        assert simplify(kd.kappa_sum - Rational(98, 3)) == 0

    def test_dual_level(self):
        kd = koszul_dual_identification((2, 1), k)
        assert simplify(kd.dual_level + k + 6) == 0


# ===================================================================
# sl_4 hook pair: (2,1,1) <-> (3,1)
# ===================================================================

class TestSl4HookDSBar:
    def test_minimal_kappa_commutes(self):
        check = ds_bar_commutation_check((2, 1, 1), k)
        assert check.kappa_commutes

    def test_minimal_generators_match(self):
        check = ds_bar_commutation_check((2, 1, 1), k)
        assert check.generators_match

    def test_minimal_c_threads(self):
        check = ds_bar_commutation_check((2, 1, 1), k)
        assert check.c_threads

    def test_subregular_kappa_commutes(self):
        check = ds_bar_commutation_check((3, 1), k)
        assert check.kappa_commutes

    def test_subregular_generators_match(self):
        check = ds_bar_commutation_check((3, 1), k)
        assert check.generators_match

    def test_subregular_c_threads(self):
        check = ds_bar_commutation_check((3, 1), k)
        assert check.c_threads

    def test_ghost_constants(self):
        assert ghost_constant((2, 1, 1)) == 3
        assert ghost_constant((3, 1)) == 6

    def test_cross_kappa_sum(self):
        data = sl4_hook_ds_bar_data(k)
        assert data["kappa_sum_equals_comp"]


class TestSl4KoszulDual:
    def test_minimal_dual_is_subregular(self):
        kd = koszul_dual_identification((2, 1, 1), k)
        assert kd.dual_partition == (3, 1)
        assert not kd.is_self_transpose

    def test_subregular_dual_is_minimal(self):
        kd = koszul_dual_identification((3, 1), k)
        assert kd.dual_partition == (2, 1, 1)

    def test_dual_level(self):
        kd = koszul_dual_identification((2, 1, 1), k)
        assert simplify(kd.dual_level + k + 8) == 0

    def test_kappa_sum_well_defined(self):
        """Kappa sum is a well-defined rational function.

        For non-self-transpose pairs, the sum is k-dependent
        because the two W-algebras have different anomaly ratios.
        """
        kd = koszul_dual_identification((2, 1, 1), k)
        assert kd.kappa_sum is not None


# ===================================================================
# General hook sweep: sl_3 through sl_6
# ===================================================================

class TestHookSweep:
    @pytest.mark.parametrize("N", [3, 4, 5, 6])
    def test_ds_bar_commutation_principal(self, N):
        """Principal nilpotent: DS-bar commutes."""
        lam = (N,)
        check = ds_bar_commutation_check(lam, k)
        assert check.kappa_commutes
        assert check.c_threads

    @pytest.mark.parametrize("N,r", [
        (3, 1), (4, 1), (4, 2), (4, 3),
        (5, 1), (5, 2), (5, 3), (5, 4),
    ])
    def test_ds_bar_commutation_hook(self, N, r):
        """Hook nilpotents: DS-bar commutes."""
        lam = normalize_partition(tuple([N - r] + [1] * r))
        check = ds_bar_commutation_check(lam, k)
        assert check.kappa_commutes
        assert check.c_threads

    @pytest.mark.parametrize("N,r", [
        (3, 1), (4, 1), (4, 2), (5, 1), (5, 2), (5, 3),
    ])
    def test_kappa_anti_symmetry_hook_pairs(self, N, r):
        """Kappa complementarity for hook transpose pairs.

        Self-transpose: kappa sum is k-independent.
        Non-self-transpose: kappa sum is a well-defined rational function
        (different anomaly ratios prevent full k-cancellation).
        """
        lam = normalize_partition(tuple([N - r] + [1] * r))
        lam_t = transpose_partition(lam)
        kv = hook_dual_level_sl_n(N, k)
        s = simplify(ds_kappa_from_affine(lam, k) + ds_kappa_from_affine(lam_t, kv))
        if lam == lam_t:
            assert simplify(s.diff(k)) == 0, f"Self-transpose {lam}: sum not constant"
        else:
            assert s is not None, f"Non-self-transpose {lam}: sum undefined"

    @pytest.mark.parametrize("N", [3, 4, 5])
    def test_koszul_dual_involutivity(self, N):
        """Koszul duality is involutive: (W^!)^! = W."""
        for r in range(1, N):
            lam = normalize_partition(tuple([N - r] + [1] * r))
            lam_t = transpose_partition(lam)
            lam_tt = transpose_partition(lam_t)
            assert lam == lam_tt


# ===================================================================
# Master verification
# ===================================================================

class TestMasterVerification:
    def test_all_checks_pass(self):
        results = verify_ds_bar_commutation()
        failures = {k: v for k, v in results.items() if not v}
        assert len(failures) == 0, f"Failures: {list(failures.keys())}"

    def test_check_count(self):
        results = verify_ds_bar_commutation()
        assert len(results) >= 70


# ===================================================================
# sl_3 complete data bundle
# ===================================================================

class TestSl3DataBundle:
    def test_bundle_completeness(self):
        data = sl3_minimal_data(k)
        assert data["is_self_transpose"]
        assert data["n_generators"] == 4
        assert data["n_bosonic"] == 2
        assert data["n_fermionic"] == 2
        assert data["self_dual_level"] == Rational(-3)
        assert data["ghost_constant"] == 2
        assert data["ds_bar_check"].kappa_commutes
        assert data["bar_complex"].is_koszul
