"""Tests for hook-type W-algebra duality computations.

Covers the sl_4 hook pair W_k(sl_4, f_{(3,1)}) <-> W_k(sl_4, f_{(2,1,1)})
and the self-dual partition (2,2), with general hook-type verification
up to sl_6.
"""

import pytest

from sympy import Rational, Symbol, simplify

from compute.lib.hook_type_w_duality import (
    bar_cohomology_h1_generators,
    bar_cohomology_h2_estimate,
    c_complementarity_22,
    c_complementarity_31_211,
    c_sl4_211,
    c_sl4_22,
    c_sl4_31,
    c_sl4_principal,
    complementarity_constant,
    ds_kappa_from_affine,
    ghost_constant,
    ghost_constant_hook,
    hook_dual_level_sl4,
    hook_dual_level_sl_n,
    hook_kappa_anti_symmetry_catalog,
    hook_kappa_anti_symmetry_sl_n,
    kappa_anti_symmetry_22,
    kappa_anti_symmetry_31_211,
    kappa_sl4_211,
    kappa_sl4_22,
    kappa_sl4_31,
    kappa_sl4_principal,
    krw_central_charge,
    krw_central_charge_data,
    levi_rho_norm_squared,
    rho_shift_norm_squared,
    sl4_22_generators,
    sl4_hook_211_generators,
    sl4_hook_31_generators,
    sl4_hook_duality_data,
    sl4_principal_generators,
    verify_hook_type_w_duality,
    w_algebra_generator_data,
    weyl_vector_norm_squared_sl_n,
    weyl_vector_sl_n,
)


class TestPartitionTranspose:
    def test_31_transpose(self):
        from compute.lib.nonprincipal_ds_orbits import transpose_partition
        assert transpose_partition((3, 1)) == (2, 1, 1)

    def test_211_transpose(self):
        from compute.lib.nonprincipal_ds_orbits import transpose_partition
        assert transpose_partition((2, 1, 1)) == (3, 1)

    def test_22_self_dual(self):
        from compute.lib.nonprincipal_ds_orbits import transpose_partition
        assert transpose_partition((2, 2)) == (2, 2)


class TestWeylVector:
    def test_sl4_rho(self):
        assert weyl_vector_sl_n(4) == (
            Rational(3, 2), Rational(1, 2), Rational(-1, 2), Rational(-3, 2)
        )

    def test_sl4_rho_norm(self):
        assert weyl_vector_norm_squared_sl_n(4) == Rational(5)

    def test_sl3_rho_norm(self):
        assert weyl_vector_norm_squared_sl_n(3) == Rational(2)

    def test_sl2_rho_norm(self):
        assert weyl_vector_norm_squared_sl_n(2) == Rational(1, 2)

    def test_general_formula(self):
        """||rho||^2 = N(N^2-1)/12."""
        for N in range(2, 8):
            assert weyl_vector_norm_squared_sl_n(N) == Rational(N * (N * N - 1), 12)


class TestLeviRho:
    def test_principal(self):
        assert levi_rho_norm_squared((4,)) == Rational(4 * 15, 12)

    def test_trivial(self):
        assert levi_rho_norm_squared((1, 1, 1, 1)) == Rational(0)

    def test_211(self):
        # Block (2): 2*3/12 = 1/2. Blocks (1),(1): 0.
        assert levi_rho_norm_squared((2, 1, 1)) == Rational(1, 2)

    def test_31(self):
        # Block (3): 3*8/12 = 2. Block (1): 0.
        assert levi_rho_norm_squared((3, 1)) == Rational(2)

    def test_22(self):
        # Two blocks (2): 2*(2*3/12) = 1.
        assert levi_rho_norm_squared((2, 2)) == Rational(1)


class TestRhoShift:
    def test_211(self):
        assert rho_shift_norm_squared((2, 1, 1)) == Rational(9, 2)

    def test_31(self):
        assert rho_shift_norm_squared((3, 1)) == Rational(3)

    def test_22(self):
        assert rho_shift_norm_squared((2, 2)) == Rational(4)

    def test_principal(self):
        assert rho_shift_norm_squared((4,)) == Rational(0)

    def test_trivial(self):
        assert rho_shift_norm_squared((1, 1, 1, 1)) == Rational(5)


class TestGeneratorData:
    def test_211_f_centralizer_dim(self):
        g = sl4_hook_211_generators()
        assert g.f_centralizer_dimension == 9

    def test_31_f_centralizer_dim(self):
        g = sl4_hook_31_generators()
        assert g.f_centralizer_dimension == 5

    def test_22_f_centralizer_dim(self):
        g = sl4_22_generators()
        assert g.f_centralizer_dimension == 7

    def test_principal_f_centralizer_dim(self):
        g = sl4_principal_generators()
        assert g.f_centralizer_dimension == 3

    def test_211_grades(self):
        g = sl4_hook_211_generators()
        assert g.f_centralizer_grades == {0: 4, -1: 4, -2: 1}

    def test_31_grades(self):
        g = sl4_hook_31_generators()
        assert g.f_centralizer_grades == {0: 1, -2: 3, -4: 1}

    def test_22_grades(self):
        g = sl4_22_generators()
        assert g.f_centralizer_grades == {0: 3, -2: 4}

    def test_principal_grades(self):
        g = sl4_principal_generators()
        assert g.f_centralizer_grades == {-2: 1, -4: 1, -6: 1}

    def test_211_has_fermions(self):
        g = sl4_hook_211_generators()
        assert g.n_fermionic == 4
        assert g.n_bosonic == 5

    def test_31_no_fermions(self):
        g = sl4_hook_31_generators()
        assert g.n_fermionic == 0
        assert g.n_bosonic == 5

    def test_22_no_fermions(self):
        g = sl4_22_generators()
        assert g.n_fermionic == 0
        assert g.n_bosonic == 7

    def test_centralizer_dim_matches_partition_formula(self):
        """dim(g^f) = sum (lambda'_i)^2 - 1."""
        from compute.lib.nonprincipal_ds_orbits import centralizer_dimension_sl_n
        for part in [(2, 1, 1), (3, 1), (2, 2), (4,)]:
            g = w_algebra_generator_data(part)
            assert g.f_centralizer_dimension == centralizer_dimension_sl_n(part)


class TestCentralCharge:
    def test_211_data(self):
        cc = krw_central_charge_data((2, 1, 1))
        assert cc.dim_g0 == 5
        assert cc.dim_g_half == 4
        assert cc.leading_term == 3
        assert cc.quadratic_coeff == 54

    def test_31_data(self):
        cc = krw_central_charge_data((3, 1))
        assert cc.dim_g0 == 5
        assert cc.dim_g_half == 0
        assert cc.leading_term == 5
        assert cc.quadratic_coeff == 36

    def test_22_data(self):
        cc = krw_central_charge_data((2, 2))
        assert cc.dim_g0 == 7
        assert cc.dim_g_half == 0
        assert cc.leading_term == 7
        assert cc.quadratic_coeff == 48

    def test_principal_data(self):
        cc = krw_central_charge_data((4,))
        assert cc.dim_g0 == 3
        assert cc.dim_g_half == 0
        assert cc.leading_term == 3
        assert cc.quadratic_coeff == 0

    def test_principal_at_k0(self):
        """c(W_4, k=0) = 3 (unshifted, no quadratic term for principal)."""
        assert simplify(c_sl4_principal(0) - 3) == 0

    def test_211_at_k0(self):
        assert simplify(c_sl4_211(0) + Rational(21, 2)) == 0

    def test_31_at_k0(self):
        assert simplify(c_sl4_31(0) + 4) == 0

    def test_22_at_k0(self):
        assert simplify(c_sl4_22(0) + 5) == 0


class TestGhostConstant:
    def test_principal(self):
        assert ghost_constant((4,)) == 10

    def test_31(self):
        assert ghost_constant((3, 1)) == 6

    def test_22(self):
        assert ghost_constant((2, 2)) == 4

    def test_211(self):
        assert ghost_constant((2, 1, 1)) == 3

    def test_trivial(self):
        assert ghost_constant((1, 1, 1, 1)) == 0

    def test_hook_formula_matches_direct(self):
        for N in range(3, 7):
            for r in range(N):
                direct = ghost_constant((N - r,) + (1,) * r)
                hook = ghost_constant_hook(N, r)
                assert direct == hook, f"N={N}, r={r}: {direct} != {hook}"

    def test_principal_formula(self):
        """C_principal(N) = N(N^2-1)/6."""
        for N in range(2, 8):
            assert ghost_constant((N,)) == Rational(N * (N * N - 1), 6)


class TestComplementarityConstant:
    def test_31_211(self):
        assert complementarity_constant((3, 1)) == -9

    def test_22(self):
        assert complementarity_constant((2, 2)) == -8

    def test_principal(self):
        assert complementarity_constant((4,)) == -10

    def test_symmetric_in_transpose(self):
        assert complementarity_constant((3, 1)) == complementarity_constant((2, 1, 1))


class TestKappa:
    def test_principal_explicit(self):
        k = Symbol('k')
        kappa = kappa_sl4_principal(k)
        expected = Rational(15, 8) * (k + 4) - 10
        assert simplify(kappa - expected) == 0

    def test_211_explicit(self):
        k = Symbol('k')
        kappa = kappa_sl4_211(k)
        expected = Rational(15, 8) * (k + 4) - 3
        assert simplify(kappa - expected) == 0

    def test_31_explicit(self):
        k = Symbol('k')
        kappa = kappa_sl4_31(k)
        expected = Rational(15, 8) * (k + 4) - 6
        assert simplify(kappa - expected) == 0

    def test_22_explicit(self):
        k = Symbol('k')
        kappa = kappa_sl4_22(k)
        expected = Rational(15, 8) * (k + 4) - 4
        assert simplify(kappa - expected) == 0

    def test_kappa_linear_in_k(self):
        k = Symbol('k')
        for part in [(2, 1, 1), (3, 1), (2, 2), (4,)]:
            kappa = ds_kappa_from_affine(part, k)
            # Check linearity: second derivative = 0
            assert simplify(kappa.diff(k, 2)) == 0

    def test_universal_slope(self):
        """All sl_4 W-algebras have the same kappa slope = 15/8."""
        k = Symbol('k')
        for part in [(2, 1, 1), (3, 1), (2, 2), (4,)]:
            kappa = ds_kappa_from_affine(part, k)
            assert simplify(kappa.diff(k) - Rational(15, 8)) == 0


class TestKappaAntiSymmetry:
    def test_31_211_constant_sum(self):
        """kappa(3,1; k) + kappa(2,1,1; -k-8) = -9."""
        k = Symbol('k')
        assert simplify(kappa_anti_symmetry_31_211(k) + 9) == 0

    def test_22_constant_sum(self):
        """kappa(2,2; k) + kappa(2,2; -k-8) = -8."""
        k = Symbol('k')
        assert simplify(kappa_anti_symmetry_22(k) + 8) == 0

    def test_principal_constant_sum(self):
        k = Symbol('k')
        kv = hook_dual_level_sl4(k)
        s = simplify(kappa_sl4_principal(k) + kappa_sl4_principal(kv))
        assert simplify(s + 20) == 0

    def test_sum_equals_complementarity_constant(self):
        """kappa sum = complementarity_constant for each partition."""
        k = Symbol('k')
        for part in [(3, 1), (2, 1, 1), (2, 2), (4,)]:
            from compute.lib.nonprincipal_ds_orbits import transpose_partition
            lam_t = transpose_partition(part)
            N = sum(part)
            kv = -k - 2 * N
            s = simplify(ds_kappa_from_affine(part, k) + ds_kappa_from_affine(lam_t, kv))
            assert simplify(s - complementarity_constant(part)) == 0


class TestCComplementarity:
    def test_22_k_independent(self):
        """c(2,2; k) + c(2,2; -k-8) is constant."""
        k = Symbol('k')
        s = c_complementarity_22(k)
        assert simplify(s.diff(k)) == 0
        assert simplify(s - 14) == 0

    def test_31_211_k_dependent(self):
        """c(3,1; k) + c(2,1,1; -k-8) is NOT constant (different rho_L)."""
        k = Symbol('k')
        s = c_complementarity_31_211(k)
        assert simplify(s.diff(k)) != 0


class TestDualLevel:
    def test_sl4(self):
        k = Symbol('k')
        assert simplify(hook_dual_level_sl4(k) + k + 8) == 0

    def test_sl_n(self):
        k = Symbol('k')
        for N in range(2, 8):
            assert simplify(hook_dual_level_sl_n(N, k) + k + 2 * N) == 0

    def test_involutive(self):
        k = Symbol('k')
        kv = hook_dual_level_sl4(k)
        kvv = hook_dual_level_sl4(kv)
        assert simplify(kvv - k) == 0


class TestBarCohomology:
    def test_h1_dimensions(self):
        assert bar_cohomology_h1_generators((2, 1, 1)) == 9
        assert bar_cohomology_h1_generators((3, 1)) == 5
        assert bar_cohomology_h1_generators((2, 2)) == 7
        assert bar_cohomology_h1_generators((4,)) == 3

    def test_h2_estimate_211(self):
        data = bar_cohomology_h2_estimate((2, 1, 1))
        assert data["n_generators"] == 9
        assert data["n_relations_upper"] == 6  # 15 - 9

    def test_h2_estimate_31(self):
        data = bar_cohomology_h2_estimate((3, 1))
        assert data["n_generators"] == 5
        assert data["n_relations_upper"] == 10  # 15 - 5


class TestHookDualityData:
    def test_source_target(self):
        k = Symbol('k')
        d = sl4_hook_duality_data(k)
        assert d.source_partition == (3, 1)
        assert d.target_partition == (2, 1, 1)

    def test_dual_level(self):
        k = Symbol('k')
        d = sl4_hook_duality_data(k)
        assert simplify(d.dual_level + k + 8) == 0

    def test_kappa_sum_constant(self):
        k = Symbol('k')
        d = sl4_hook_duality_data(k)
        assert simplify(d.kappa_sum + 9) == 0


class TestGeneralHookAntiSymmetry:
    def test_sl3(self):
        k = Symbol('k')
        # sl_3 has one hook pair: (2,1) self-dual
        assert simplify(hook_kappa_anti_symmetry_sl_n(3, 1, k) + 4) == 0

    def test_sl4_all_hooks(self):
        k = Symbol('k')
        for r in range(1, 3):
            s = hook_kappa_anti_symmetry_sl_n(4, r, k)
            assert simplify(s - complementarity_constant((4 - r,) + (1,) * r)) == 0

    def test_sl5_all_hooks(self):
        k = Symbol('k')
        for r in range(1, 4):
            s = hook_kappa_anti_symmetry_sl_n(5, r, k)
            assert simplify(s - complementarity_constant((5 - r,) + (1,) * r)) == 0

    @pytest.mark.slow
    def test_catalog_up_to_sl6(self):
        k = Symbol('k')
        catalog = hook_kappa_anti_symmetry_catalog(max_N=6, level=k)
        for key, value in catalog.items():
            # Each sum should be a CONSTANT (k-independent)
            assert simplify(value.diff(k) if hasattr(value, 'diff') else 0) == 0


class TestVerificationBundle:
    @pytest.mark.slow
    def test_all_checks(self):
        results = verify_hook_type_w_duality()
        failures = {k: v for k, v in results.items() if not v}
        assert not failures, f"Failed checks: {list(failures.keys())}"
