"""Tests for the Kac-Moody vacuum module.

Verifies the KMVacuumModule class against known results:
  - Vacuum module character: prod_{n>=1} (1-q^n)^{-dim(g)}
  - Zero modes form a representation of g
  - Commutation relations [J^a_m, J^b_n] = f^c_{ab} J^c_{m+n} + k*kappa*m*delta
  - g-invariant dimensions match spectral_sequence.adjoint_invariant_dim

CONVENTIONS:
  - sl_2 basis: e=0, h=1, f=2
  - PBW states: tuples of (mode, gen_index) pairs
"""

import pytest

from sympy import Rational, Symbol, eye, zeros

from compute.lib.km_vacuum_module import (
    KMVacuumModule,
    SL2_VACUUM_DIMS,
    casimir_eigenvalues_at_weight,
    casimir_matrix_at_weight,
    invariant_dim_at_weight,
    invariant_dims_through_weight,
    irrep_decomposition_at_weight,
    km_pbw_basis,
    lowest_weight_dim_at_weight,
    sl2_data,
    sugawara_l0_matrix,
    vacuum_module_dims,
    verify_creation_annihilation,
    verify_sugawara_l0,
    verify_vacuum_dims,
    verify_zero_mode_commutation,
)


class TestPBWBasis:
    """PBW basis of the KM vacuum module."""

    def test_weight0(self):
        """Weight 0 is the vacuum state."""
        assert km_pbw_basis(3, 0) == [()]

    def test_weight1_sl2(self):
        """Weight 1: three generators J^a_{-1}|0>."""
        basis = km_pbw_basis(3, 1)
        assert len(basis) == 3
        assert basis == [((1, 0),), ((1, 1),), ((1, 2),)]

    def test_weight2_sl2(self):
        """Weight 2: 3 (mode 2) + 6 (mode 1,1) = 9."""
        basis = km_pbw_basis(3, 2)
        assert len(basis) == 9

    def test_weight3_sl2(self):
        """Weight 3: 3 + 9 + 10 = 22."""
        basis = km_pbw_basis(3, 3)
        assert len(basis) == 22

    def test_dims_match_character_sl2(self):
        """PBW basis dims match prod_{n>=1} (1-q^n)^{-3}."""
        for h in range(8):
            assert len(km_pbw_basis(3, h)) == SL2_VACUUM_DIMS[h]

    def test_character_formula(self):
        """Character formula implementation matches known values."""
        dims = vacuum_module_dims(3, 12)
        assert dims == SL2_VACUUM_DIMS

    def test_dim1_single_generator(self):
        """Single generator (Heisenberg-like): dims = partition numbers."""
        # prod_{n>=1} 1/(1-q^n) = partition function p(n)
        dims = vacuum_module_dims(1, 8)
        assert dims == [1, 1, 2, 3, 5, 7, 11, 15, 22]

    def test_verification_bundle(self):
        for ok in verify_vacuum_dims(3, 6).values():
            assert ok


class TestModeMatrices:
    """Basic mode matrix properties."""

    def test_annihilation_on_vacuum(self):
        """J^a_n |0> = 0 for n >= 0."""
        module = KMVacuumModule.sl2(max_weight=4)
        for a in range(3):
            for n in range(0, 3):
                mat = module.mode_matrix(a, n, 0)
                # V_0 is 1-dim, target V_{-n} is empty for n > 0
                if n > 0:
                    assert mat.rows == 0 or mat.cols == 0 or mat.is_zero_matrix
                else:
                    # J^a_0 on V_0: 1x1 zero matrix
                    assert mat.is_zero_matrix

    def test_creation_on_vacuum(self):
        """J^a_{-1} |0> = basis of V_1."""
        module = KMVacuumModule.sl2(max_weight=2)
        for a in range(3):
            mat = module.mode_matrix(a, -1, 0)
            assert mat.shape == (3, 1)
            # Should be unit vector e_a
            for i in range(3):
                assert mat[i, 0] == (Rational(1) if i == a else Rational(0))

    def test_l0_is_weight(self):
        """L_0 on V_h is implemented by sum of mode*count.

        For the KM vacuum module, L_0 = sum_a sum_{n>0} :J^a_{-n} J^a_n: / (2(k+h^v))
        but on PBW states, L_0 acts as the conformal weight h.
        We can verify indirectly that mode_matrix shapes are correct.
        """
        module = KMVacuumModule.sl2(max_weight=4)
        # Verify all weight spaces have correct dimension
        assert module.weight_dim(0) == 1
        assert module.weight_dim(1) == 3
        assert module.weight_dim(2) == 9
        assert module.weight_dim(3) == 22


class TestZeroModes:
    """Zero modes J^a_0 form a representation of g."""

    def test_zero_mode_shape(self):
        """J^a_0: V_h -> V_h (preserves weight)."""
        module = KMVacuumModule.sl2(max_weight=4)
        for h in range(1, 5):
            d = module.weight_dim(h)
            for a in range(3):
                mat = module.adjoint_action_matrix(a, h)
                assert mat.shape == (d, d)

    def test_zero_mode_on_weight1(self):
        """J^a_0 on V_1 should be the adjoint representation.

        Basis of V_1: J^0_{-1}|0>, J^1_{-1}|0>, J^2_{-1}|0> = e, h, f
        J^0_0(J^b_{-1}|0>) = [J^0_0, J^b_{-1}]|0> = f^c_{0b} J^c_{-1}|0>
        """
        module = KMVacuumModule.sl2(max_weight=2)
        # ad(e) on {e, h, f}: [e,e]=0, [e,h]=-2e, [e,f]=h
        ad_e = module.adjoint_action_matrix(0, 1)
        assert ad_e[0, 1] == Rational(-2)  # [e,h] = -2e
        assert ad_e[1, 2] == Rational(1)   # [e,f] = h
        # ad(h): [h,e]=2e, [h,h]=0, [h,f]=-2f
        ad_h = module.adjoint_action_matrix(1, 1)
        assert ad_h[0, 0] == Rational(2)   # [h,e] = 2e
        assert ad_h[2, 2] == Rational(-2)  # [h,f] = -2f

    def test_commutation_verification_bundle(self):
        """[J^a_0, J^b_0] = f^c_{ab} J^c_0 on all weight spaces."""
        for ok in verify_zero_mode_commutation(5).values():
            assert ok


class TestCommutationRelations:
    """Full commutation relations [J^a_m, J^b_n]."""

    def test_creation_annihilation_bundle(self):
        """[J^a_1, J^a_{-1}] verified on low weights."""
        for ok in verify_creation_annihilation(3).values():
            assert ok

    def test_eh_commutation_on_weight1(self):
        """[J^e_1, J^h_{-1}] on V_1.

        [J^0_1, J^1_{-1}] = f^c_{01} J^c_0 + k*kappa(0,1)*1*delta_{1,1}
        = -2 J^0_0 + 0 = -2 ad(e)

        Acting on V_1: J^0_1 J^1_{-1} - J^1_{-1} J^0_1
        """
        module = KMVacuumModule.sl2(max_weight=3)
        # J^0_1: V_2 -> V_1; J^1_{-1}: V_1 -> V_2
        j0_1 = module.mode_matrix(0, 1, 2)     # 3x9
        j1_m1 = module.mode_matrix(1, -1, 1)   # 9x3
        term1 = j0_1 * j1_m1  # 3x3

        # J^1_{-1}: V_0 -> V_1; J^0_1: V_1 -> V_0
        j0_1_from1 = module.mode_matrix(0, 1, 1)     # ? x 3
        j1_m1_from0 = module.mode_matrix(1, -1, 0)   # 3 x 1
        if j0_1_from1.rows > 0 and j1_m1_from0.cols > 0:
            term2 = j1_m1_from0 * j0_1_from1
        else:
            term2 = zeros(3, 3)

        comm = term1 - term2
        # Expected: -2 * ad(e) = -2 * J^0_0
        expected = Rational(-2) * module.adjoint_action_matrix(0, 1)
        assert comm == expected

    def test_ef_commutation_on_weight1(self):
        """[J^e_1, J^f_{-1}] on V_1.

        [J^0_1, J^2_{-1}] = f^c_{02} J^c_0 + k*kappa(0,2)*1
        = J^1_0 + k*1*Id = ad(h) + k*Id
        """
        k = Symbol("k")
        module = KMVacuumModule.sl2(level=k, max_weight=3)

        j0_1 = module.mode_matrix(0, 1, 2)       # V_2 -> V_1
        j2_m1 = module.mode_matrix(2, -1, 1)     # V_1 -> V_2
        term1 = j0_1 * j2_m1

        j0_1_from1 = module.mode_matrix(0, 1, 1)
        j2_m1_from0 = module.mode_matrix(2, -1, 0)
        if j0_1_from1.rows > 0 and j2_m1_from0.rows > 0:
            term2 = j2_m1_from0 * j0_1_from1
        else:
            term2 = zeros(3, 3)

        comm = term1 - term2
        expected = module.adjoint_action_matrix(1, 1) + k * eye(3)
        assert comm == expected


class TestInvariants:
    """g-invariants in each weight space."""

    def test_weight0_invariant(self):
        """Vacuum is always g-invariant."""
        module = KMVacuumModule.sl2(max_weight=2)
        assert invariant_dim_at_weight(module, 0) == 1

    def test_weight1_no_invariant(self):
        """V_1 = adjoint has no invariants for simple g."""
        module = KMVacuumModule.sl2(max_weight=2)
        assert invariant_dim_at_weight(module, 1) == 0

    def test_weight2_one_invariant(self):
        """V_2 has one invariant (the Casimir/Killing element)."""
        module = KMVacuumModule.sl2(max_weight=3)
        assert invariant_dim_at_weight(module, 2) == 1

    def test_invariant_sequence_sl2(self):
        """g-invariant sequence matches known values.

        Should agree with adjoint_invariant_dim from spectral_sequence.py:
        1, 0, 1, 1, 3, 3, 8, 9, 19, ...
        """
        expected = [1, 0, 1, 1, 3, 3, 8, 9]
        dims = invariant_dims_through_weight(3, max_weight=7)
        assert dims == expected

    @pytest.mark.slow
    def test_invariant_sequence_sl2_extended(self):
        """Extended invariant sequence to weight 9."""
        expected = [1, 0, 1, 1, 3, 3, 8, 9, 19, 25]
        dims = invariant_dims_through_weight(3, max_weight=9)
        assert dims == expected


class TestCasimir:
    """Casimir C_2 decomposition of vacuum module weight spaces."""

    def test_casimir_weight1(self):
        """V_1 = adjoint (spin 1): C_2 = 4."""
        module = KMVacuumModule.sl2(max_weight=2)
        C = casimir_matrix_at_weight(module, 1)
        assert C == Rational(4) * eye(3)

    def test_casimir_weight2_eigenvalues(self):
        """V_2 decomposes as V_5 + V_3 + V_1.

        Eigenvalues: 12 (spin 2, dim 5), 4 (spin 1, dim 3), 0 (spin 0, dim 1).
        """
        module = KMVacuumModule.sl2(max_weight=3)
        eigenvals = casimir_eigenvalues_at_weight(module, 2)
        assert eigenvals == {Rational(12): 5, Rational(4): 3, Rational(0): 1}

    def test_casimir_weight3_has_invariant(self):
        """V_3 contains a g-invariant (Casimir eigenvalue 0)."""
        module = KMVacuumModule.sl2(max_weight=4)
        eigenvals = casimir_eigenvalues_at_weight(module, 3)
        assert Rational(0) in eigenvals
        assert eigenvals[Rational(0)] == 1

    def test_irrep_decomposition_weight1(self):
        """V_1 = adjoint = 1 copy of spin 1."""
        module = KMVacuumModule.sl2(max_weight=2)
        decomp = irrep_decomposition_at_weight(module, 1)
        assert decomp == {1: 1}

    def test_irrep_decomposition_weight2(self):
        """V_2 = V_5 + V_3 + V_1 = spin 2 + spin 1 + spin 0."""
        module = KMVacuumModule.sl2(max_weight=3)
        decomp = irrep_decomposition_at_weight(module, 2)
        assert decomp == {2: 1, 1: 1, 0: 1}

    def test_irrep_dims_sum_to_total(self):
        """Sum of irrep dimensions equals dim V_h."""
        module = KMVacuumModule.sl2(max_weight=5)
        for h in range(1, 6):
            decomp = irrep_decomposition_at_weight(module, h)
            total = sum(copies * (2 * j + 1) for j, copies in decomp.items())
            assert total == module.weight_dim(h), \
                f"Dim mismatch at weight {h}: {total} vs {module.weight_dim(h)}"

    def test_invariant_from_casimir(self):
        """Number of spin-0 copies = invariant dimension."""
        module = KMVacuumModule.sl2(max_weight=5)
        for h in range(6):
            decomp = irrep_decomposition_at_weight(module, h)
            inv_casimir = decomp.get(0, 0)
            inv_kernel = invariant_dim_at_weight(module, h)
            assert inv_casimir == inv_kernel, \
                f"Mismatch at weight {h}: casimir={inv_casimir}, kernel={inv_kernel}"


class TestLowestWeight:
    """Annihilation kernel dim(ker J^a_1) at each weight."""

    def test_weight1_killed_by_killing(self):
        """At weight 1, J^a_1: V_1 -> V_0 via Killing form, so ker = 0 generically.

        Unlike Virasoro (where V_1 = 0), the KM vacuum has V_0 = C|0>,
        and J^a_1 reaches it via the central extension: J^a_1 J^b_{-1}|0> = k*kappa(a,b)|0>.
        For generic k, the stacked J^a_1 matrices have full rank 3, giving ker = 0.
        """
        module = KMVacuumModule.sl2(max_weight=2)
        assert lowest_weight_dim_at_weight(module, 1) == 0

    def test_weight2(self):
        """ker(J^a_1) at weight 2 is non-negative."""
        module = KMVacuumModule.sl2(max_weight=3)
        lwv = lowest_weight_dim_at_weight(module, 2)
        assert lwv >= 0


class TestSugawara:
    """Sugawara construction: L_0 = h on V_h."""

    def test_sugawara_weight1(self):
        """L_0 = 1 on V_1."""
        from sympy import simplify
        k = Symbol("k")
        module = KMVacuumModule.sl2(level=k, max_weight=2)
        L0 = sugawara_l0_matrix(module, 1)
        diff = L0 - eye(3)
        for i in range(3):
            for j in range(3):
                assert simplify(diff[i, j]) == 0

    def test_sugawara_weight2(self):
        """L_0 = 2 on V_2."""
        from sympy import simplify
        k = Symbol("k")
        module = KMVacuumModule.sl2(level=k, max_weight=3)
        L0 = sugawara_l0_matrix(module, 2)
        diff = L0 - 2 * eye(9)
        for i in range(9):
            for j in range(9):
                assert simplify(diff[i, j]) == 0

    def test_sugawara_verification_bundle(self):
        for ok in verify_sugawara_l0(4).values():
            assert ok


class TestCrossValidation:
    """Cross-validate against existing infrastructure."""

    def test_invariants_match_spectral_sequence(self):
        """g-invariants match adjoint_invariant_dim from spectral_sequence.py."""
        from compute.lib.spectral_sequence import adjoint_invariant_dim

        dim_g, sc, kf = sl2_data()
        module = KMVacuumModule(dim_g, sc, kf, max_weight=6)

        for h in range(7):
            new_val = invariant_dim_at_weight(module, h)
            old_val = adjoint_invariant_dim(dim_g, sc, h)
            assert new_val == old_val, \
                f"Mismatch at weight {h}: new={new_val}, old={old_val}"

    def test_weight_dims_match_sym_module(self):
        """Vacuum module dims should match _sym_module_dim at each weight.

        Both count the same thing: colored partitions of weight h with dim_g colors.
        """
        from compute.lib.spectral_sequence import _sym_module_dim

        for h in range(8):
            pbw_dim = len(km_pbw_basis(3, h))
            sym_dim = _sym_module_dim(3, h)
            assert pbw_dim == sym_dim, \
                f"Mismatch at weight {h}: pbw={pbw_dim}, sym={sym_dim}"
