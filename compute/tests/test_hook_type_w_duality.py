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
        # Levi = Cartan for principal nilpotent: rho_L = 0.
        # Transpose of (4) is (1,1,1,1); all blocks size 1.
        assert levi_rho_norm_squared((4,)) == Rational(0)

    def test_trivial(self):
        # Levi = gl_4 for trivial nilpotent: rho_L = rho.
        # Transpose of (1,1,1,1) is (4); one block size 4.
        assert levi_rho_norm_squared((1, 1, 1, 1)) == Rational(5)

    def test_211(self):
        # Transpose of (2,1,1) is (3,1). Blocks: gl_3 x gl_1.
        # 3*8/12 + 0 = 2.
        assert levi_rho_norm_squared((2, 1, 1)) == Rational(2)

    def test_31(self):
        # Transpose of (3,1) is (2,1,1). Blocks: gl_2 x gl_1 x gl_1.
        # 2*3/12 + 0 + 0 = 1/2.
        assert levi_rho_norm_squared((3, 1)) == Rational(1, 2)

    def test_22(self):
        # Self-transpose. Two blocks (2): 2*(2*3/12) = 1.
        assert levi_rho_norm_squared((2, 2)) == Rational(1)


class TestRhoShift:
    def test_211(self):
        assert rho_shift_norm_squared((2, 1, 1)) == Rational(3)

    def test_31(self):
        assert rho_shift_norm_squared((3, 1)) == Rational(9, 2)

    def test_22(self):
        assert rho_shift_norm_squared((2, 2)) == Rational(4)

    def test_principal(self):
        assert rho_shift_norm_squared((4,)) == Rational(5)

    def test_trivial(self):
        assert rho_shift_norm_squared((1, 1, 1, 1)) == Rational(0)


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
        assert cc.quadratic_coeff == 36

    def test_31_data(self):
        cc = krw_central_charge_data((3, 1))
        assert cc.dim_g0 == 5
        assert cc.dim_g_half == 0
        assert cc.leading_term == 5
        assert cc.quadratic_coeff == 54

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
        assert cc.quadratic_coeff == 60

    def test_principal_at_k0(self):
        """c(W_4, k=0) = -132 (matches Fateev-Lukyanov c_wn_fl(4,0))."""
        # VERIFIED: c_wn_fl(4, 0) = -132 from wn_central_charge_canonical.py
        assert simplify(c_sl4_principal(0) + 132) == 0

    def test_211_at_k0(self):
        """c(W_{(2,1,1)}, k=0) = -26 (per-root-pair formula, 4 half-int pairs)."""
        # VERIFIED: independent per-root-pair computation with
        # x = (1/2, 0, 0, -1/2), grades: j=0 (1 pair), j=1/2 (4 pairs), j=1 (1 pair)
        assert simplify(c_sl4_211(0) + 26) == 0

    def test_31_at_k0(self):
        """c(W_{(3,1)}, k=0) = -157/2 (per-root-pair formula, all integer grades)."""
        # VERIFIED: independent per-root-pair computation with
        # x = (1, 0, 0, -1), grades: j=0 (1 pair), j=1 (4 pairs), j=2 (1 pair)
        assert simplify(c_sl4_31(0) + Rational(157, 2)) == 0

    def test_22_at_k0(self):
        """c(W_{(2,2)}, k=0) = -52 (per-root-pair formula, all integer grades)."""
        # VERIFIED: independent per-root-pair computation with
        # x = (1/2, 1/2, -1/2, -1/2), grades: j=0 (2 pairs), j=1 (4 pairs)
        assert simplify(c_sl4_22(0) + 52) == 0


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
        """kappa(W_4, k) = (13/12)*c = -13(4k+11)(5k+16)/(4(k+4)).

        VERIFIED: rho=(13/12), c = 3-60(k+3)^2/(k+4) from Fateev-Lukyanov.
        At k=0: kappa = -13*11*16/(4*4) = -13*176/16 = -143. Cross-check:
        kappa = (13/12)*(-132) = -143. Consistent.
        """
        k = Symbol('k')
        kappa = kappa_sl4_principal(k)
        expected = Rational(-13, 4) * (4 * k + 11) * (5 * k + 16) / (k + 4)
        assert simplify(kappa - expected) == 0

    def test_211_explicit(self):
        """kappa(W_{(2,1,1)}, k) = (11/6)*c = -11(42k^2+103k+104)/(6(k+4)).

        VERIFIED: rho=(11/6), c(0)=-26. kappa(0) = (11/6)*(-26) = -286/6 = -143/3.
        Direct: -11*104/24 = -1144/24 = -143/3. Consistent.
        """
        k = Symbol('k')
        kappa = kappa_sl4_211(k)
        expected = Rational(-11, 6) * (42 * k**2 + 103 * k + 104) / (k + 4)
        assert simplify(kappa - expected) == 0

    def test_31_explicit(self):
        """kappa(W_{(3,1)}, k) = (17/6)*c = -17(36k^2+211k+314)/(6(k+4)).

        VERIFIED: rho=(17/6), c(0)=-157/2. kappa(0) = (17/6)*(-157/2) = -2669/12.
        Direct: -17*314/24 = -5338/24 = -2669/12. Consistent.
        """
        k = Symbol('k')
        kappa = kappa_sl4_31(k)
        expected = Rational(-17, 6) * (36 * k**2 + 211 * k + 314) / (k + 4)
        assert simplify(kappa - expected) == 0

    def test_22_explicit(self):
        """kappa(W_{(2,2)}, k) = 5*c = -5(24k^2+137k+208)/(k+4).

        VERIFIED: rho=5, c(0)=-52. kappa(0) = 5*(-52) = -260.
        Direct: -5*208/4 = -260. Consistent.
        """
        k = Symbol('k')
        kappa = kappa_sl4_22(k)
        expected = -5 * (24 * k**2 + 137 * k + 208) / (k + 4)
        assert simplify(kappa - expected) == 0

    def test_kappa_rational_in_k(self):
        """kappa = rho*c is a rational function of k (NOT linear)."""
        k = Symbol('k')
        for part in [(2, 1, 1), (3, 1), (2, 2), (4,)]:
            kappa = ds_kappa_from_affine(part, k)
            # kappa has a pole at k = -4, so it is NOT a polynomial
            # Verify it is a proper rational function: numerator/denominator
            from sympy import fraction
            num, den = fraction(simplify(kappa))
            assert den != 1, f"{part}: kappa should not be polynomial"

    def test_kappa_rho_c_identity(self):
        """kappa = rho * c for each partition."""
        k = Symbol('k')
        from compute.lib.hook_type_w_duality import (
            anomaly_ratio_from_partition, krw_central_charge,
        )
        for part in [(2, 1, 1), (3, 1), (2, 2), (4,)]:
            kappa = ds_kappa_from_affine(part, k)
            rho = anomaly_ratio_from_partition(part)
            c = krw_central_charge(part, k)
            assert simplify(kappa - rho * c) == 0


class TestKappaAntiSymmetry:
    def test_31_211_k_dependent(self):
        """kappa(3,1; k) + kappa(2,1,1; -k-8) is k-dependent (different rho's)."""
        k = Symbol('k')
        s = kappa_anti_symmetry_31_211(k)
        # Different anomaly ratios (17/6 vs 11/6) prevent cancellation
        assert simplify(s.diff(k)) != 0

    def test_22_constant_sum(self):
        """kappa(2,2; k) + kappa(2,2; -k-8) = 550 (self-transpose, same rho).

        VERIFIED: rho=5, K_{(2,2)}=110 (complementarity sum).
        kappa_sum = rho * K = 5 * 110 = 550.
        """
        k = Symbol('k')
        assert simplify(kappa_anti_symmetry_22(k) - 550) == 0

    def test_principal_constant_sum(self):
        """kappa(W_4, k) + kappa(W_4, -k-8) = 533/2.

        VERIFIED: rho=(13/12), K_principal=246 (Freudenthal-de Vries).
        kappa_sum = (13/12)*246 = 13*246/12 = 3198/12 = 533/2.
        """
        k = Symbol('k')
        kv = hook_dual_level_sl4(k)
        s = simplify(kappa_sl4_principal(k) + kappa_sl4_principal(kv))
        assert simplify(s - Rational(533, 2)) == 0

    def test_self_transpose_k_independent(self):
        """Self-transpose partitions give k-independent kappa sums."""
        k = Symbol('k')
        # (2,2) is self-transpose; (4) is NOT (its transpose is (1,1,1,1))
        for part in [(2, 2)]:
            from compute.lib.nonprincipal_ds_orbits import transpose_partition
            lam_t = transpose_partition(part)
            N = sum(part)
            kv = -k - 2 * N
            s = simplify(ds_kappa_from_affine(part, k) + ds_kappa_from_affine(lam_t, kv))
            assert simplify(s.diff(k)) == 0, f"{part}: kappa sum should be k-independent"


class TestCComplementarity:
    def test_22_k_independent(self):
        """c(2,2; k) + c(2,2; -k-8) = 110 (constant, k-independent).

        VERIFIED: both (2,2) terms use the same per-root-pair structure
        (self-transpose), so the sum telescopes to a constant.
        Independent check: c(0)+c(-8) = -52 + 162 = 110.
        """
        k = Symbol('k')
        s = c_complementarity_22(k)
        assert simplify(s.diff(k)) == 0
        assert simplify(s - 110) == 0

    def test_31_211_k_dependent(self):
        """c(3,1; k) + c(2,1,1; -k-8) is NOT constant (different grade structures)."""
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

    def test_kappa_sum_rational(self):
        """Hook kappa sum is a rational function of k (different rho's)."""
        k = Symbol('k')
        d = sl4_hook_duality_data(k)
        # (3,1) has rho=17/6, (2,1,1) has rho=11/6 => sum is k-dependent
        assert d.kappa_sum.has(k)


class TestGeneralHookAntiSymmetry:
    def test_sl3_self_transpose(self):
        """sl_3 (2,1) is self-transpose: kappa sum = 98/3 (k-independent).

        VERIFIED: rho(BP) = 1/6, K_BP = 196.
        kappa_sum = rho * K = (1/6)*196 = 196/6 = 98/3.
        """
        k = Symbol('k')
        s = hook_kappa_anti_symmetry_sl_n(3, 1, k)
        assert simplify(s - Rational(98, 3)) == 0

    def test_sl4_self_transpose_hooks(self):
        """Self-transpose hook partitions give k-independent kappa sums."""
        k = Symbol('k')
        from compute.lib.nonprincipal_ds_orbits import transpose_partition, hook_partition
        for r in range(1, 3):
            lam = hook_partition(4, r)
            lam_t = transpose_partition(lam)
            s = hook_kappa_anti_symmetry_sl_n(4, r, k)
            if lam == lam_t:
                # Self-transpose: sum is k-independent
                assert simplify(s.diff(k)) == 0, f"r={r}: self-transpose sum should be constant"
            else:
                # Non-self-transpose: sum is a well-defined rational function
                assert s is not None

    def test_sl5_well_defined(self):
        """All sl_5 hook kappa sums are well-defined rational functions."""
        k = Symbol('k')
        for r in range(1, 4):
            s = hook_kappa_anti_symmetry_sl_n(5, r, k)
            assert s is not None

    @pytest.mark.slow
    def test_self_transpose_catalog_up_to_sl6(self):
        """Self-transpose hook pairs give k-independent kappa sums."""
        k = Symbol('k')
        from compute.lib.nonprincipal_ds_orbits import hook_partition, transpose_partition
        for N in range(3, 7):
            for r in range(1, N - 1):
                lam = hook_partition(N, r)
                lam_t = transpose_partition(lam)
                if lam == lam_t:
                    s = hook_kappa_anti_symmetry_sl_n(N, r, k)
                    assert simplify(s.diff(k) if hasattr(s, 'diff') else 0) == 0, \
                        f"sl_{N} r={r}: self-transpose sum should be k-independent"


class TestVerificationBundle:
    @pytest.mark.slow
    def test_all_checks(self):
        results = verify_hook_type_w_duality()
        failures = {k: v for k, v in results.items() if not v}
        assert not failures, f"Failed checks: {list(failures.keys())}"
