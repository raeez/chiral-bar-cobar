"""Tests for sp₄ Hochschild-Serre E₁ computation."""

import pytest
import numpy as np

from compute.lib.sp4_hochschild_serre import (
    lie_exponents,
    lie_dimension,
    generator_loop_degrees,
    e1_dims_from_generators,
    e1_dims,
    e1_dims_sl2,
    e1_dims_sl3,
    e1_dims_sp4,
    polynomial_growth_bound,
    structure_constants_sp4_int,
    adjoint_matrices_from_sc,
    verify_jacobi_generic,
    killing_form,
    sp4_ad_mats,
    sl2_ad_mats,
    ce_cohomology_dims,
    exterior_power_action,
    structure_constants_sl2_int,
)


# ===== Lie algebra data =====

class TestLieExponents:
    def test_a1(self):
        assert lie_exponents('A', 1) == [1]

    def test_a2(self):
        assert lie_exponents('A', 2) == [1, 2]

    def test_a3(self):
        assert lie_exponents('A', 3) == [1, 2, 3]

    def test_b2(self):
        assert lie_exponents('B', 2) == [1, 3]

    def test_c2(self):
        assert lie_exponents('C', 2) == [1, 3]

    def test_b2_equals_c2(self):
        """B₂ ≅ C₂ as Lie algebras."""
        assert lie_exponents('B', 2) == lie_exponents('C', 2)

    def test_d4(self):
        assert lie_exponents('D', 4) == [1, 3, 3, 5]

    def test_g2(self):
        assert lie_exponents('G', 2) == [1, 5]

    def test_f4(self):
        assert lie_exponents('F', 4) == [1, 5, 7, 11]

    def test_e6(self):
        assert lie_exponents('E', 6) == [1, 4, 5, 7, 8, 11]

    def test_e8(self):
        assert lie_exponents('E', 8) == [1, 7, 11, 13, 17, 19, 23, 29]

    def test_exponent_count_equals_rank(self):
        """Number of exponents = rank."""
        for t, r in [('A', 5), ('B', 3), ('C', 4), ('D', 5), ('G', 2), ('E', 6)]:
            assert len(lie_exponents(t, r)) == r, f"{t}_{r}"

    def test_sum_of_exponents(self):
        """Sum of exponents = number of positive roots = (dim - rank)/2."""
        for t, r in [('A', 3), ('B', 3), ('C', 3), ('D', 4)]:
            exps = lie_exponents(t, r)
            dim = lie_dimension(t, r)
            assert sum(exps) == (dim - r) // 2


class TestLieDimension:
    def test_sl2(self):
        assert lie_dimension('A', 1) == 3

    def test_sl3(self):
        assert lie_dimension('A', 2) == 8

    def test_sp4(self):
        assert lie_dimension('C', 2) == 10

    def test_g2(self):
        assert lie_dimension('G', 2) == 14


# ===== Generator loop degrees =====

class TestGeneratorDegrees:
    def test_sl2_generators(self):
        """sl₂ generators at odd degrees ≥ 3."""
        gens = generator_loop_degrees([1], 15)
        assert gens == [3, 5, 7, 9, 11, 13, 15]

    def test_sp4_generators(self):
        """sp₄ has two towers: {3,5,7,...} and {7,9,11,...}."""
        gens = generator_loop_degrees([1, 3], 11)
        assert gens == [3, 5, 7, 7, 9, 9, 11, 11]

    def test_sl3_generators(self):
        """sl₃ has two towers: {3,5,7,...} and {5,7,9,...}."""
        gens = generator_loop_degrees([1, 2], 9)
        assert gens == [3, 5, 5, 7, 7, 9, 9]

    def test_empty_below_threshold(self):
        """No generators below 2e+1."""
        gens = generator_loop_degrees([1], 2)
        assert gens == []


# ===== E₁ dimensions (main computation) =====

class TestE1Dims:
    def test_sl2_ground_truth(self):
        """Manuscript table: E₁^{0,p}(sl₂) = [1,0,0,1,0,1]."""
        assert e1_dims_sl2(5) == [1, 0, 0, 1, 0, 1]

    def test_sl2_extended(self):
        """Extended sl₂ values."""
        vals = e1_dims_sl2(15)
        assert vals == [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 2, 1, 2, 2]

    def test_sp4_low_degrees(self):
        """sp₄ matches sl₂ up to p=6 (second exponent kicks in at p=7)."""
        sl2 = e1_dims_sl2(6)
        sp4 = e1_dims_sp4(6)
        assert sl2 == sp4

    def test_sp4_first_divergence(self):
        """sp₄ first differs from sl₂ at p=7 (two generators vs one)."""
        assert e1_dims_sp4(7)[7] == 2
        assert e1_dims_sl2(7)[7] == 1

    def test_sp4_values(self):
        """sp₄ E₁ values up to p=15."""
        vals = e1_dims_sp4(15)
        assert vals == [1, 0, 0, 1, 0, 1, 0, 2, 1, 2, 2, 2, 4, 2, 5, 4]

    def test_sl3_first_divergence(self):
        """sl₃ first differs from sl₂ at p=5 (two generators vs one)."""
        assert e1_dims_sl3(5)[5] == 2
        assert e1_dims_sl2(5)[5] == 1

    def test_sl3_values(self):
        """sl₃ E₁ values up to p=10."""
        vals = e1_dims_sl3(10)
        assert vals == [1, 0, 0, 1, 0, 2, 0, 2, 2, 2, 3]

    def test_e1_p0_always_1(self):
        """E₁^{0,0} = 1 for all Lie types (the constant)."""
        for t, r in [('A', 1), ('A', 3), ('B', 2), ('C', 3), ('D', 4), ('G', 2)]:
            assert e1_dims(t, r, 0) == [1], f"{t}_{r}"

    def test_e1_p1_p2_always_0(self):
        """E₁^{0,1} = E₁^{0,2} = 0 for all types (no generators below degree 3)."""
        for t, r in [('A', 1), ('A', 3), ('B', 2), ('C', 3), ('G', 2)]:
            vals = e1_dims(t, r, 2)
            assert vals[1] == 0 and vals[2] == 0, f"{t}_{r}"

    def test_e1_p3_always_1(self):
        """E₁^{0,3} = 1 for all types (the CE 3-cocycle, exponent 1 universal)."""
        for t, r in [('A', 1), ('A', 3), ('B', 2), ('C', 3), ('D', 4), ('G', 2)]:
            assert e1_dims(t, r, 3)[3] == 1, f"{t}_{r}"


# ===== Polynomial growth =====

class TestPolynomialGrowth:
    def test_sl2_growth(self):
        """sl₂ E₁ grows polynomially (essentially like partitions into odd ≥3)."""
        vals = e1_dims_sl2(50)
        desc = polynomial_growth_bound(vals)
        assert 'polynomial' in desc or 'constant' in desc

    def test_sp4_growth(self):
        """sp₄ E₁ grows polynomially."""
        vals = e1_dims_sp4(50)
        desc = polynomial_growth_bound(vals)
        assert 'polynomial' in desc


# ===== sp₄ structure constants verification =====

class TestSp4Structure:
    def test_jacobi(self):
        """All 1000 Jacobi identities for sp₄."""
        assert verify_jacobi_generic(10, structure_constants_sp4_int())

    def test_killing_form_rank(self):
        """Killing form of sp₄ is nondegenerate (rank 10)."""
        K = killing_form(10, sp4_ad_mats())
        assert np.linalg.matrix_rank(K, tol=1e-8) == 10

    def test_killing_form_trace(self):
        """κ(h,h) = 2h^∨(2h^∨+1)... actually Tr(ad²) = 2h^∨·dim.
        For sp₄: h^∨ = 3, so Killing trace should relate to this."""
        K = killing_form(10, sp4_ad_mats())
        # Just check it's nonzero and symmetric
        assert np.allclose(K, K.T)
        assert np.trace(K) > 0

    def test_ce_cohomology_sp4(self):
        """H*(sp₄) = (1+t³)(1+t⁷), Betti numbers (1,0,0,1,0,0,0,1,0,0,1)."""
        ce = ce_cohomology_dims(10, sp4_ad_mats())
        assert ce == [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1]

    def test_ce_cohomology_sl2(self):
        """H*(sl₂) = (1,0,0,1)."""
        ce = ce_cohomology_dims(3, sl2_ad_mats())
        assert ce == [1, 0, 0, 1]


# ===== sl₂ verification =====

class TestSl2Structure:
    def test_jacobi(self):
        assert verify_jacobi_generic(3, structure_constants_sl2_int())

    def test_killing_form(self):
        K = killing_form(3, sl2_ad_mats())
        assert np.linalg.matrix_rank(K, tol=1e-8) == 3


# ===== Exterior power infrastructure =====

class TestExteriorPower:
    def test_lambda0(self):
        """Λ⁰(g) = k, trivial representation."""
        mats = exterior_power_action(0, sl2_ad_mats())
        for M in mats:
            assert M.shape == (1, 1)
            assert np.allclose(M, 0)

    def test_lambda1_same_invariants(self):
        """Λ¹(g) has same invariant dimension as adjoint (0 for semisimple)."""
        ad = sl2_ad_mats()
        ext = exterior_power_action(1, ad)
        big_ad = np.vstack(ad)
        big_ext = np.vstack(ext)
        assert np.linalg.matrix_rank(big_ad) == np.linalg.matrix_rank(big_ext)

    def test_lambda2_sl2(self):
        """Λ²(sl₂) ≅ sl₂ (adjoint, dim 3)."""
        ext = exterior_power_action(2, sl2_ad_mats())
        assert ext[0].shape == (3, 3)

    def test_lambda3_sl2_trivial(self):
        """Λ³(sl₂) = k (trivial, dim 1)."""
        ext = exterior_power_action(3, sl2_ad_mats())
        for M in ext:
            assert M.shape == (1, 1)
            assert np.allclose(M, 0)

    def test_lambda2_sp4_dim(self):
        """Λ²(sp₄) has dim C(10,2) = 45."""
        ext = exterior_power_action(2, sp4_ad_mats())
        assert ext[0].shape == (45, 45)

    @pytest.mark.slow
    def test_lambda3_sp4_invariants(self):
        """Λ³(sp₄)^{sp₄} = H³(sp₄) has dim 1."""
        ext = exterior_power_action(3, sp4_ad_mats())
        big = np.vstack(ext)
        rank = np.linalg.matrix_rank(big, tol=1e-8)
        inv_dim = ext[0].shape[0] - rank
        assert inv_dim == 1


# ===== Subset-sum DP =====

class TestSubsetSum:
    def test_empty(self):
        assert e1_dims_from_generators([], 5) == [1, 0, 0, 0, 0, 0]

    def test_single_generator(self):
        assert e1_dims_from_generators([3], 5) == [1, 0, 0, 1, 0, 0]

    def test_two_generators(self):
        assert e1_dims_from_generators([3, 5], 10) == [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0]

    def test_duplicate_generators(self):
        """Two generators at same degree: can pick 0, 1, or 2."""
        result = e1_dims_from_generators([3, 3], 6)
        assert result == [1, 0, 0, 2, 0, 0, 1]
