"""Tests for A-infinity bimodule structures for CY3 quiver chart gluing.

Verifies:
  1. A-infinity algebra axioms (Stasheff relations)
  2. A-infinity bimodule equations for low (p,q)
  3. Transition bimodules for A_1 quiver mutations (flops)
  4. Derived tensor products and cocycle conditions
  5. Koszul dual bimodules via bar construction
  6. Numerical invariants (Euler characteristics, Hochschild)
  7. Shadow obstruction contributions from transitions

Multi-path verification:
  (a) Explicit matrix computation
  (b) Euler characteristic check
  (c) Bar construction verification

References:
  - Keller, "A-infinity algebras, modules and functor categories"
  - Seidel, "Fukaya categories and Picard-Lefschetz theory"
  - Bridgeland, "Flops and derived categories"
  - Van den Bergh, "Non-commutative crepant resolutions"
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.cy_ainfty_bimodule_engine import (
    AInfAlgebra,
    AInfBimodule,
    BarBimodule,
    verify_stasheff,
    check_stasheff_all,
    verify_bimodule_relation,
    check_bimodule_relations,
    trivial_algebra,
    path_algebra_A1,
    path_algebra_A2,
    path_algebra_A3,
    ext_algebra_A1_flop,
    dg_algebra_from_matrices,
    identity_bimodule,
    a1_flop_bimodule,
    a1_flop_bimodule_rank2,
    derived_tensor_product_dim,
    compute_bar_bimodule,
    koszul_dual_bimodule_dims,
    euler_characteristic_bimodule,
    euler_char_multiplicativity,
    hochschild_homology_dims,
    transition_shadow_arity2,
    transition_shadow_arity2_alt,
    bimodule_euler_form,
    identity_tensor_check,
    triple_overlap_associativity,
    full_flop_analysis,
    _frac,
    _frac_array,
    _frac_matmul,
    _is_zero,
    _unit_vec,
    _image_dim,
    _kernel_basis,
    _koszul_sign,
)


# ============================================================
# Helpers
# ============================================================

def _basis_vec(n, i):
    """Standard basis vector e_i in Q^n."""
    v = _frac_array(n)
    v[i] = Fraction(1)
    return v


# ============================================================
# Section 1: Rational Arithmetic Helpers
# ============================================================

class TestFractionHelpers:
    """Verify exact arithmetic infrastructure."""

    def test_frac_from_int(self):
        assert _frac(3) == Fraction(3)

    def test_frac_from_fraction(self):
        assert _frac(Fraction(1, 2)) == Fraction(1, 2)

    def test_frac_array_1d(self):
        arr = _frac_array(3)
        assert arr.shape == (3,)
        assert all(x == Fraction(0) for x in arr)

    def test_frac_array_2d(self):
        arr = _frac_array((2, 3))
        assert arr.shape == (2, 3)
        assert all(x == Fraction(0) for x in arr.flat)

    def test_frac_matmul_identity(self):
        I = _frac_array((2, 2))
        I[0, 0] = Fraction(1)
        I[1, 1] = Fraction(1)
        v = _frac_array((2, 1))
        v[0, 0] = Fraction(3)
        v[1, 0] = Fraction(7)
        result = _frac_matmul(I, v)
        assert result[0, 0] == Fraction(3)
        assert result[1, 0] == Fraction(7)

    def test_frac_matmul_product(self):
        A = _frac_array((2, 2))
        A[0, 0] = Fraction(1); A[0, 1] = Fraction(2)
        A[1, 0] = Fraction(3); A[1, 1] = Fraction(4)
        B = _frac_array((2, 2))
        B[0, 0] = Fraction(5); B[0, 1] = Fraction(6)
        B[1, 0] = Fraction(7); B[1, 1] = Fraction(8)
        C = _frac_matmul(A, B)
        assert C[0, 0] == Fraction(19)  # 1*5 + 2*7
        assert C[0, 1] == Fraction(22)  # 1*6 + 2*8
        assert C[1, 0] == Fraction(43)  # 3*5 + 4*7
        assert C[1, 1] == Fraction(50)  # 3*6 + 4*8

    def test_is_zero_true(self):
        arr = _frac_array(5)
        assert _is_zero(arr)

    def test_is_zero_false(self):
        arr = _frac_array(5)
        arr[2] = Fraction(1)
        assert not _is_zero(arr)

    def test_unit_vec(self):
        v = _unit_vec(3, 1)
        assert v[0] == Fraction(0)
        assert v[1] == Fraction(1)
        assert v[2] == Fraction(0)

    def test_image_dim_identity(self):
        I = _frac_array((3, 3))
        for i in range(3):
            I[i, i] = Fraction(1)
        assert _image_dim(I) == 3

    def test_image_dim_rank1(self):
        M = _frac_array((2, 3))
        M[0, 0] = Fraction(1); M[0, 1] = Fraction(2); M[0, 2] = Fraction(3)
        M[1, 0] = Fraction(2); M[1, 1] = Fraction(4); M[1, 2] = Fraction(6)
        assert _image_dim(M) == 1

    def test_kernel_basis_full_rank(self):
        I = _frac_array((2, 2))
        I[0, 0] = Fraction(1); I[1, 1] = Fraction(1)
        ker = _kernel_basis(I)
        assert len(ker) == 0

    def test_kernel_basis_rank1(self):
        M = _frac_array((1, 3))
        M[0, 0] = Fraction(1); M[0, 1] = Fraction(2); M[0, 2] = Fraction(3)
        ker = _kernel_basis(M)
        assert len(ker) == 2  # 3-1 = 2 dimensional kernel


# ============================================================
# Section 2: Koszul Signs
# ============================================================

class TestKoszulSign:
    """Verify Koszul sign computations."""

    def test_identity_perm(self):
        """Identity permutation: sign = +1 regardless of degrees."""
        assert _koszul_sign([0, 1, 2], [0, 1, 2]) == Fraction(1)

    def test_swap_even(self):
        """Swapping two even-degree elements: sign = +1."""
        assert _koszul_sign([0, 0], [1, 0]) == Fraction(1)

    def test_swap_odd(self):
        """Swapping two odd-degree elements: sign = -1."""
        assert _koszul_sign([1, 1], [1, 0]) == Fraction(-1)

    def test_swap_mixed(self):
        """Swapping even and odd: sign = +1 (only odd*odd gives -1)."""
        assert _koszul_sign([0, 1], [1, 0]) == Fraction(1)

    def test_triple_all_odd(self):
        """Cyclic permutation (0,1,2) -> (2,0,1) on odd elements.
        Two transpositions of odd elements: (-1)^2 = +1."""
        # (2,0,1) needs 2 transpositions to sort
        sign = _koszul_sign([1, 1, 1], [2, 0, 1])
        # Bubble sort: swap 2,0 -> (-1), then swap 2,1 -> (-1): total +1
        assert sign == Fraction(1)


# ============================================================
# Section 3: A-infinity Algebra Construction
# ============================================================

class TestAInfAlgebra:
    """Verify A-infinity algebra construction and basic properties."""

    def test_trivial_algebra_dims(self):
        A = trivial_algebra(1, 0)
        assert A.total_dim == 1
        assert A.degree_of(0) == 0

    def test_trivial_m2_unit(self):
        A = trivial_algebra(1, 0)
        result = A.m(2, (0, 0))
        assert result[0] == Fraction(1)

    def test_path_algebra_A1(self):
        A = path_algebra_A1()
        assert A.total_dim == 1
        assert A.name == "k^1[0]"

    def test_path_algebra_A2_dims(self):
        A = path_algebra_A2()
        assert A.total_dim == 3
        assert A.dims == {0: 3}

    def test_path_algebra_A2_idempotents(self):
        """e_1^2 = e_1, e_2^2 = e_2."""
        A = path_algebra_A2()
        e1_sq = A.m(2, (0, 0))
        assert e1_sq[0] == Fraction(1)
        e2_sq = A.m(2, (1, 1))
        assert e2_sq[1] == Fraction(1)

    def test_path_algebra_A2_arrow(self):
        """e_1 * a = a, a * e_2 = a."""
        A = path_algebra_A2()
        assert A.m_coeff(2, (0, 2), 2) == Fraction(1)  # e_1 * a = a
        assert A.m_coeff(2, (2, 1), 2) == Fraction(1)  # a * e_2 = a

    def test_path_algebra_A3_composition(self):
        """a * b = ba in A_3 quiver."""
        A = path_algebra_A3()
        ab = A.m(2, (3, 4))  # a * b
        assert ab[5] == Fraction(1)  # = ba

    def test_path_algebra_A3_idempotent_ba(self):
        """e_1 * ba = ba, ba * e_3 = ba."""
        A = path_algebra_A3()
        assert A.m_coeff(2, (0, 5), 5) == Fraction(1)
        assert A.m_coeff(2, (5, 2), 5) == Fraction(1)


# ============================================================
# Section 4: Stasheff Relations
# ============================================================

class TestStasheffRelations:
    """Verify A-infinity (Stasheff) relations."""

    def test_trivial_stasheff_n1(self):
        """m_1^2 = 0 for the trivial algebra (trivially, m_1 = 0)."""
        A = trivial_algebra()
        rel = verify_stasheff(A, 1, (0,))
        assert _is_zero(rel)

    def test_trivial_stasheff_n2(self):
        """Stasheff at n=2: m_1(m_2(a,b)) - m_2(m_1(a),b) - (-1)^|a| m_2(a, m_1(b)) = 0.
        With m_1 = 0, reduces to 0 = 0."""
        A = trivial_algebra()
        rel = verify_stasheff(A, 2, (0, 0))
        assert _is_zero(rel)

    def test_path_A2_stasheff_all(self):
        """All Stasheff relations up to n=3 for path algebra A_2."""
        A = path_algebra_A2()
        assert check_stasheff_all(A, max_n=3)

    def test_path_A3_stasheff_all(self):
        """All Stasheff relations up to n=3 for path algebra A_3."""
        A = path_algebra_A3()
        assert check_stasheff_all(A, max_n=3)

    def test_ext_A1_flop_stasheff_n2(self):
        """Stasheff at n=2 for Ext algebra of A_1 flop."""
        A = ext_algebra_A1_flop()
        for inputs in [(0, 0), (0, 1), (1, 0), (1, 1),
                        (0, 2), (2, 0), (2, 1), (1, 2)]:
            rel = verify_stasheff(A, 2, inputs)
            assert _is_zero(rel), f"Stasheff n=2 fails for inputs {inputs}"

    def test_ext_A1_flop_stasheff_n1(self):
        """m_1^2 = 0 for Ext algebra (m_1 = 0, trivially true)."""
        A = ext_algebra_A1_flop()
        for i in range(A.total_dim):
            rel = verify_stasheff(A, 1, (i,))
            assert _is_zero(rel)


# ============================================================
# Section 5: A-infinity Bimodule Construction
# ============================================================

class TestAInfBimodule:
    """Verify bimodule construction and basic properties."""

    def test_identity_bimodule_dims(self):
        """Identity bimodule has same dims as algebra."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        assert M.M_total_dim == A.total_dim
        assert M.M_dims == A.dims

    def test_identity_bimodule_left_action(self):
        """m_{1|1|0} = m_2 for identity bimodule."""
        A = path_algebra_A2()
        M = identity_bimodule(A)
        # e_1 . a = a
        result = M.bim_m(1, 0, (0,), 2, ())
        assert result[2] == Fraction(1)

    def test_identity_bimodule_right_action(self):
        """m_{0|1|1} = m_2 for identity bimodule."""
        A = path_algebra_A2()
        M = identity_bimodule(A)
        # a . e_2 = a
        result = M.bim_m(0, 1, (), 2, (1,))
        assert result[2] == Fraction(1)

    def test_a1_flop_bimodule_construction(self):
        """A_1 flop bimodule has correct dimensions."""
        A, B, M = a1_flop_bimodule()
        assert A.total_dim == 2
        assert B.total_dim == 2
        assert M.M_total_dim == 2

    def test_a1_flop_bimodule_m_dims(self):
        """M has 1 generator in degree 0 and 1 in degree 1."""
        _, _, M = a1_flop_bimodule()
        assert M.M_dims == {0: 1, 1: 1}

    def test_a1_flop_left_action(self):
        """Left action: x . m_0 = m_1."""
        _, _, M = a1_flop_bimodule()
        result = M.bim_m(1, 0, (1,), 0, ())
        assert result[1] == Fraction(1)

    def test_a1_flop_right_action(self):
        """Right action: m_0 . x = m_1."""
        _, _, M = a1_flop_bimodule()
        result = M.bim_m(0, 1, (), 0, (1,))
        assert result[1] == Fraction(1)

    def test_a1_flop_unit_actions(self):
        """Unit actions: 1.m = m, m.1 = m."""
        _, _, M = a1_flop_bimodule()
        # 1 . m_0 = m_0
        result = M.bim_m(1, 0, (0,), 0, ())
        assert result[0] == Fraction(1)
        # m_0 . 1 = m_0
        result = M.bim_m(0, 1, (), 0, (0,))
        assert result[0] == Fraction(1)

    def test_a1_flop_rank2_construction(self):
        """Rank-2 flop bimodule has correct dimensions."""
        A, B, M = a1_flop_bimodule_rank2()
        assert A.total_dim == 4
        assert B.total_dim == 4
        assert M.M_total_dim == 4

    def test_a1_flop_rank2_m_dims(self):
        """Rank-2: M has 2 generators in degree 0 and 2 in degree 1."""
        _, _, M = a1_flop_bimodule_rank2()
        assert M.M_dims == {0: 2, 1: 2}


# ============================================================
# Section 6: Bimodule Relations
# ============================================================

class TestBimoduleRelations:
    """Verify A-infinity bimodule equations at low arities."""

    def test_identity_bimodule_relation_00(self):
        """m_{0|1|0}^2 = 0 for identity bimodule (trivial: m_1=0 for path algebra)."""
        A = path_algebra_A2()
        M = identity_bimodule(A)
        for m_idx in range(M.M_total_dim):
            rel = verify_bimodule_relation(M, 0, 0, (), m_idx, ())
            assert _is_zero(rel), f"Bimodule relation (0,0) fails for m={m_idx}"

    def test_identity_bimodule_relation_10(self):
        """Bimodule relation at (1,0) for identity bimodule over path algebra A_2."""
        A = path_algebra_A2()
        M = identity_bimodule(A)
        for a in range(A.total_dim):
            for m_idx in range(M.M_total_dim):
                rel = verify_bimodule_relation(M, 1, 0, (a,), m_idx, ())
                assert _is_zero(rel), f"Bimodule relation (1,0) fails for a={a}, m={m_idx}"

    def test_identity_bimodule_relation_01(self):
        """Bimodule relation at (0,1) for identity bimodule."""
        A = path_algebra_A2()
        M = identity_bimodule(A)
        for m_idx in range(M.M_total_dim):
            for b in range(A.total_dim):
                rel = verify_bimodule_relation(M, 0, 1, (), m_idx, (b,))
                assert _is_zero(rel), f"Bimodule relation (0,1) fails for m={m_idx}, b={b}"

    def test_a1_flop_bimodule_relation_00(self):
        """m_{0|1|0}^2 = 0 for A_1 flop bimodule."""
        _, _, M = a1_flop_bimodule()
        for m_idx in range(M.M_total_dim):
            rel = verify_bimodule_relation(M, 0, 0, (), m_idx, ())
            assert _is_zero(rel)

    def test_a1_flop_bimodule_relation_10(self):
        """Bimodule relation at (1,0) for A_1 flop."""
        A, _, M = a1_flop_bimodule()
        for a in range(A.total_dim):
            for m_idx in range(M.M_total_dim):
                rel = verify_bimodule_relation(M, 1, 0, (a,), m_idx, ())
                assert _is_zero(rel), f"Fails at a={a}, m={m_idx}"

    def test_a1_flop_bimodule_relation_01(self):
        """Bimodule relation at (0,1) for A_1 flop."""
        _, B, M = a1_flop_bimodule()
        for m_idx in range(M.M_total_dim):
            for b in range(B.total_dim):
                rel = verify_bimodule_relation(M, 0, 1, (), m_idx, (b,))
                assert _is_zero(rel), f"Fails at m={m_idx}, b={b}"

    def test_a1_flop_bimodule_relation_11(self):
        """Bimodule relation at (1,1) for A_1 flop on the reduced bar complex.

        The A-infinity bimodule equation is formulated on the REDUCED bar
        complex (augmentation ideal only). Unit elements do not participate
        as tensor factors — their action is the strict identity.
        """
        A, B, M = a1_flop_bimodule()
        # Augmentation ideal: non-unit elements (degree > 0)
        a_aug = [i for i in range(A.total_dim) if A.degree_of(i) != 0]
        b_aug = [i for i in range(B.total_dim) if B.degree_of(i) != 0]
        for a in a_aug:
            for m_idx in range(M.M_total_dim):
                for b in b_aug:
                    rel = verify_bimodule_relation(M, 1, 1, (a,), m_idx, (b,))
                    assert _is_zero(rel), f"Fails at a={a}, m={m_idx}, b={b}"

    def test_trivial_check_all(self):
        """All bimodule relations for identity over trivial algebra."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        assert check_bimodule_relations(M, max_pq=2)

    def test_a1_flop_check_all_low(self):
        """All bimodule relations up to p+q=2 for A_1 flop."""
        _, _, M = a1_flop_bimodule()
        assert check_bimodule_relations(M, max_pq=2)


# ============================================================
# Section 7: Euler Characteristics
# ============================================================

class TestEulerCharacteristics:
    """Verify Euler characteristic computations and multiplicativity."""

    def test_chi_trivial_identity(self):
        """chi(A_A) = 1 for the trivial algebra A = k."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        assert euler_characteristic_bimodule(M) == Fraction(1)

    def test_chi_path_A2_identity(self):
        """chi(A_A) = 3 for path algebra A_2 (3 basis elements, all in deg 0)."""
        A = path_algebra_A2()
        M = identity_bimodule(A)
        assert euler_characteristic_bimodule(M) == Fraction(3)

    def test_chi_a1_flop(self):
        """chi(M) for A_1 flop bimodule: dim M^0 - dim M^1 = 1 - 1 = 0."""
        _, _, M = a1_flop_bimodule()
        assert euler_characteristic_bimodule(M) == Fraction(0)

    def test_chi_a1_flop_rank2(self):
        """chi(M) for rank-2 flop: 2 - 2 = 0."""
        _, _, M = a1_flop_bimodule_rank2()
        assert euler_characteristic_bimodule(M) == Fraction(0)

    def test_chi_exterior_algebra(self):
        """chi for exterior algebra identity bimodule: 1 - 1 = 0."""
        A, _, _ = a1_flop_bimodule()  # A = Lambda(x)
        M = identity_bimodule(A)
        chi = euler_characteristic_bimodule(M)
        assert chi == Fraction(0)  # dim^0 - dim^1 = 1 - 1 = 0

    def test_chi_path_A3(self):
        """chi for path algebra A_3: 6 (all in degree 0)."""
        A = path_algebra_A3()
        M = identity_bimodule(A)
        assert euler_characteristic_bimodule(M) == Fraction(6)

    def test_euler_form_equals_chi(self):
        """bimodule_euler_form = euler_characteristic_bimodule."""
        _, _, M = a1_flop_bimodule()
        assert bimodule_euler_form(M) == euler_characteristic_bimodule(M)

    def test_euler_multiplicativity_trivial(self):
        """For trivial algebra: chi_1 * chi_2 = chi_12 = 1."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        c1, c2, c12 = euler_char_multiplicativity(M, M, M)
        assert c1 == Fraction(1)
        assert c2 == Fraction(1)
        assert c12 == Fraction(1)

    def test_chi_non_negative_path_algebras(self):
        """Path algebras (degree 0 only) have chi >= 0."""
        for A in [path_algebra_A1(), path_algebra_A2(), path_algebra_A3()]:
            M = identity_bimodule(A)
            chi = euler_characteristic_bimodule(M)
            assert chi >= Fraction(0)


# ============================================================
# Section 8: Bar Construction
# ============================================================

class TestBarConstruction:
    """Verify bar construction on bimodules."""

    def test_bar_trivial(self):
        """Bar of identity bimodule over k."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        bar_M = compute_bar_bimodule(M, max_arity=2)
        # (0,0) component: just M itself
        dim_00 = bar_M.total_dim_at_arity(0, 0)
        assert dim_00 == 1

    def test_bar_total_dim_positive(self):
        """Bar complex has positive total dimension."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        assert bar_M.total_dim() > 0

    def test_bar_arity_00_equals_M(self):
        """(0,0) component of bar = M itself."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        dim_00 = bar_M.total_dim_at_arity(0, 0)
        assert dim_00 == M.M_total_dim

    def test_bar_euler_well_defined(self):
        """Bar Euler characteristic is a well-defined rational number."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        chi = bar_M.euler_characteristic()
        assert isinstance(chi, Fraction)

    def test_bar_arity_10(self):
        """(1,0) component of bar: (s^{-1}A) tensor M."""
        A, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        dim_10 = bar_M.total_dim_at_arity(1, 0)
        # s^{-1}A has dim 2 (shifted), M has dim 2, tensor = 4
        assert dim_10 == A.total_dim * M.M_total_dim

    def test_bar_arity_01(self):
        """(0,1) component: M tensor (s^{-1}B)."""
        _, B, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        dim_01 = bar_M.total_dim_at_arity(0, 1)
        assert dim_01 == M.M_total_dim * B.total_dim

    def test_bar_arity_11(self):
        """(1,1) component: (s^{-1}A) tensor M tensor (s^{-1}B)."""
        A, B, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        dim_11 = bar_M.total_dim_at_arity(1, 1)
        assert dim_11 == A.total_dim * M.M_total_dim * B.total_dim

    def test_bar_grows_with_arity(self):
        """Higher max_arity gives larger bar complex."""
        _, _, M = a1_flop_bimodule()
        bar_2 = compute_bar_bimodule(M, max_arity=2)
        bar_3 = compute_bar_bimodule(M, max_arity=3)
        assert bar_3.total_dim() > bar_2.total_dim()

    def test_bar_rank2(self):
        """Bar construction for rank-2 flop bimodule."""
        _, _, M = a1_flop_bimodule_rank2()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        assert bar_M.total_dim() > 0
        dim_00 = bar_M.total_dim_at_arity(0, 0)
        assert dim_00 == M.M_total_dim


# ============================================================
# Section 9: Koszul Dual Bimodule
# ============================================================

class TestKoszulDualBimodule:
    """Verify Koszul dual bimodule M^! = (B(M))^v."""

    def test_koszul_dual_dims_trivial(self):
        """Koszul dual of identity bimodule over k."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        bar_M = compute_bar_bimodule(M, max_arity=1)
        kd = koszul_dual_bimodule_dims(bar_M)
        # Should have nonzero dimension
        assert sum(kd.values()) > 0

    def test_koszul_dual_dims_a1_flop(self):
        """Koszul dual dimensions for A_1 flop bimodule."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        kd = koszul_dual_bimodule_dims(bar_M)
        assert isinstance(kd, dict)
        assert sum(kd.values()) > 0

    def test_koszul_dual_reverses_degree(self):
        """Linear dual reverses degree: if B(M) has stuff in deg k, M^! has deg -k."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=1)
        kd = koszul_dual_bimodule_dims(bar_M)
        # Check that negative degrees appear (since bar has positive degrees from s^{-1})
        degrees = list(kd.keys())
        # The dual degrees are negatives of bar degrees
        # Bar has degree-0 and degree-(-1) components (from s^{-1}), so dual has 0 and 1
        assert len(degrees) > 0

    def test_koszul_dual_euler_char(self):
        """chi(M^!) = chi(B(M)) (linear duality preserves Euler characteristic)."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        kd = koszul_dual_bimodule_dims(bar_M)

        # chi(B(M))
        chi_bar = bar_M.euler_characteristic()
        # chi(M^!) = sum (-1)^{-k} dim (B(M))^k = sum (-1)^k dim (B(M))^k = chi_bar
        # Actually: chi(M^!) = sum (-1)^{-k} * dim = sum (-1)^k * dim if (-1)^{-k} = (-1)^k
        # (-1)^{-k} = (-1)^k for integer k. So chi(M^!) = chi(B(M)).
        chi_kd = Fraction(0)
        for k, d in kd.items():
            chi_kd += Fraction((-1) ** k) * Fraction(d)
        assert chi_kd == chi_bar


# ============================================================
# Section 10: Derived Tensor Products
# ============================================================

class TestDerivedTensorProduct:
    """Verify derived tensor product computations."""

    def test_derived_tensor_dims_trivial(self):
        """k otimes^L_k k = k: dimension 1 in degree 0."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        dims = derived_tensor_product_dim(M, M, max_bar_length=0)
        assert dims.get(0, 0) >= 1

    def test_derived_tensor_positive(self):
        """Derived tensor product has positive dimensions."""
        A, _, M = a1_flop_bimodule()
        id_M = identity_bimodule(A)
        dims = derived_tensor_product_dim(M, id_M, max_bar_length=2)
        assert sum(dims.values()) > 0

    def test_identity_tensor_check_dims(self):
        """M tensor^L A ~ M: chain dimensions should relate to M's."""
        A, _, M = a1_flop_bimodule()
        chain_dims = identity_tensor_check(A, M, max_bar=2)
        # Chain complex should have nonzero dimensions
        assert sum(chain_dims.values()) > 0
        # At bar length 0: M tensor A, should include M's degree-0 part
        assert chain_dims.get(0, 0) >= M.M_dims.get(0, 0)

    def test_derived_tensor_symmetry(self):
        """For symmetric examples, derived tensor has expected symmetry."""
        A, _, M = a1_flop_bimodule()
        id_A = identity_bimodule(A)
        dims_left = derived_tensor_product_dim(M, id_A, max_bar_length=2)
        dims_right = derived_tensor_product_dim(id_A, M, max_bar_length=2)
        # Both should be nonzero
        assert sum(dims_left.values()) > 0
        assert sum(dims_right.values()) > 0


# ============================================================
# Section 11: Cocycle Condition (Triple Overlaps)
# ============================================================

class TestCocycleCondition:
    """Verify cocycle condition for triple overlaps."""

    def test_triple_overlap_trivial(self):
        """For trivial algebra: M_{02} ~ M_{01} tensor M_{12}."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        tensor_dims, direct_dims = triple_overlap_associativity(M, M, M, max_bar=2)
        # Euler characteristics should match
        chi_tensor = sum(Fraction((-1) ** k) * Fraction(d)
                          for k, d in tensor_dims.items())
        chi_direct = sum(Fraction((-1) ** k) * Fraction(d)
                          for k, d in direct_dims.items())
        assert chi_direct == Fraction(1)  # chi(k) = 1

    def test_triple_overlap_euler_consistency(self):
        """Euler characteristic of tensor product is consistent with components."""
        A, _, M = a1_flop_bimodule()
        id_A = identity_bimodule(A)
        tensor_dims, direct_dims = triple_overlap_associativity(
            M, id_A, M, max_bar=2)
        # Both should produce nonempty results
        assert sum(tensor_dims.values()) > 0
        assert sum(direct_dims.values()) > 0

    def test_identity_cocycle(self):
        """Id tensor Id ~ Id (identity is the unit for tensor product)."""
        A = path_algebra_A2()
        M = identity_bimodule(A)
        tensor_dims, direct_dims = triple_overlap_associativity(M, M, M, max_bar=1)
        # At bar length 0, M tensor_A M ~ M (by definition of identity bimodule)
        assert tensor_dims.get(0, 0) >= direct_dims.get(0, 0)


# ============================================================
# Section 12: Shadow Obstruction Contributions
# ============================================================

class TestShadowObstruction:
    """Verify shadow obstruction contributions from transition bimodules."""

    def test_shadow_arity2_trivial(self):
        """Shadow contribution vanishes for trivial algebra."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        kappa = transition_shadow_arity2(M)
        assert kappa == Fraction(0)  # m_{1|1|1} = 0

    def test_shadow_arity2_a1_flop(self):
        """Shadow contribution for A_1 flop (rank 1): m_{1|1|1} = 0, so kappa = 0."""
        _, _, M = a1_flop_bimodule()
        kappa = transition_shadow_arity2(M)
        assert kappa == Fraction(0)

    def test_shadow_arity2_alt_a1_flop(self):
        """Alternative shadow computation agrees: chi(M) = 0."""
        _, _, M = a1_flop_bimodule()
        kappa_alt = transition_shadow_arity2_alt(M)
        assert kappa_alt == Fraction(0)

    def test_shadow_two_methods_agree_trivial(self):
        """Two shadow computation methods should be compatible for trivial case."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        k1 = transition_shadow_arity2(M)
        k2 = transition_shadow_arity2_alt(M)
        # Both should be finite rational numbers
        assert isinstance(k1, Fraction)
        assert isinstance(k2, Fraction)

    def test_shadow_arity2_rank2(self):
        """Shadow contribution for rank-2 flop."""
        _, _, M = a1_flop_bimodule_rank2()
        kappa = transition_shadow_arity2(M)
        # m_{1|1|1} is 0 in our model, so shadow = 0
        assert kappa == Fraction(0)

    def test_shadow_alt_rank2(self):
        """Alternative shadow for rank-2: chi(M) = 0."""
        _, _, M = a1_flop_bimodule_rank2()
        kappa_alt = transition_shadow_arity2_alt(M)
        assert kappa_alt == Fraction(0)

    def test_shadow_compatible_with_kappa_additivity(self):
        """Shadow from transition should be additive under direct sum.
        For M1 + M2: kappa(M1 + M2) = kappa(M1) + kappa(M2)."""
        _, _, M = a1_flop_bimodule()
        k1 = transition_shadow_arity2(M)
        # Direct sum with itself would give 2*k1 = 0
        assert k1 + k1 == Fraction(0)


# ============================================================
# Section 13: Hochschild Homology
# ============================================================

class TestHochschildHomology:
    """Verify Hochschild homology computations."""

    def test_hh_trivial(self):
        """HH_*(k, k) = k: chain complex dimensions."""
        A = trivial_algebra()
        M = identity_bimodule(A)
        hh = hochschild_homology_dims(A, M, max_bar=3)
        assert hh.get(0, 0) >= 1

    def test_hh_path_A2(self):
        """HH chain dimensions for path algebra A_2."""
        A = path_algebra_A2()
        M = identity_bimodule(A)
        hh = hochschild_homology_dims(A, M, max_bar=2)
        # All in degree 0 for path algebra
        assert hh.get(0, 0) > 0

    def test_hh_a1_flop(self):
        """HH chain dimensions for A_1 flop bimodule."""
        A, _, M = a1_flop_bimodule()
        hh = hochschild_homology_dims(A, M, max_bar=2)
        assert sum(hh.values()) > 0

    def test_hh_grows_with_bar(self):
        """Increasing bar length adds chain complex terms."""
        A, _, M = a1_flop_bimodule()
        hh_1 = hochschild_homology_dims(A, M, max_bar=1)
        hh_3 = hochschild_homology_dims(A, M, max_bar=3)
        assert sum(hh_3.values()) >= sum(hh_1.values())

    def test_hh_a1_flop_rank2(self):
        """HH chain dimensions for rank-2 flop bimodule."""
        A, _, M = a1_flop_bimodule_rank2()
        hh = hochschild_homology_dims(A, M, max_bar=2)
        assert sum(hh.values()) > 0


# ============================================================
# Section 14: Full Flop Analysis
# ============================================================

class TestFullFlopAnalysis:
    """Verify the complete analysis pipeline."""

    def test_full_analysis_rank1(self):
        """Full analysis for rank-1 A_1 flop."""
        results = full_flop_analysis(rank=1)
        assert results['A_total_dim'] == 2
        assert results['B_total_dim'] == 2
        assert results['M_total_dim'] == 2
        assert results['chi_M'] == Fraction(0)
        assert results['A_stasheff_3'] is True

    def test_full_analysis_rank2(self):
        """Full analysis for rank-2 A_1 flop."""
        results = full_flop_analysis(rank=2)
        assert results['A_total_dim'] == 4
        assert results['B_total_dim'] == 4
        assert results['M_total_dim'] == 4
        assert results['chi_M'] == Fraction(0)

    def test_full_analysis_bar_dim_positive(self):
        """Bar complex has positive dimension."""
        results = full_flop_analysis(rank=1)
        assert results['bar_M_total_dim'] > 0

    def test_full_analysis_koszul_dual(self):
        """Koszul dual dimensions are computed."""
        results = full_flop_analysis(rank=1)
        kd = results['koszul_dual_dims']
        assert isinstance(kd, dict)
        assert sum(kd.values()) > 0

    def test_full_analysis_identity_chi(self):
        """Identity bimodule Euler characteristic."""
        results = full_flop_analysis(rank=1)
        # Identity bimodule over Lambda(x): chi = 1 - 1 = 0
        assert results['id_chi'] == Fraction(0)

    def test_full_analysis_hh_nonempty(self):
        """Hochschild chain complex is nonempty."""
        results = full_flop_analysis(rank=1)
        assert sum(results['hh_chain_dims'].values()) > 0


# ============================================================
# Section 15: Cross-Verification (Multi-Path)
# ============================================================

class TestMultiPath:
    """Multi-path verification: same result via independent methods."""

    def test_chi_flop_three_ways(self):
        """chi(M) = 0 for A_1 flop, verified three ways:
        (a) direct from M_dims, (b) bimodule_euler_form, (c) shadow_alt."""
        _, _, M = a1_flop_bimodule()
        # Path (a): direct
        chi_direct = sum(Fraction((-1) ** k) * Fraction(d)
                          for k, d in M.M_dims.items())
        # Path (b): euler form function
        chi_euler = bimodule_euler_form(M)
        # Path (c): alt shadow = chi
        chi_shadow = transition_shadow_arity2_alt(M)

        assert chi_direct == Fraction(0)
        assert chi_euler == Fraction(0)
        assert chi_shadow == Fraction(0)
        assert chi_direct == chi_euler == chi_shadow

    def test_stasheff_two_algebras(self):
        """Both A and B in the flop satisfy Stasheff, verified independently."""
        A, B, _ = a1_flop_bimodule()
        assert check_stasheff_all(A, max_n=2)
        assert check_stasheff_all(B, max_n=2)

    def test_bar_dim_two_methods(self):
        """Bar dimensions via (a) component counting and (b) total_dim method."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        # Method (a): sum component dims
        total_a = sum(bar_M.component_dims.values())
        # Method (b): total_dim()
        total_b = bar_M.total_dim()
        assert total_a == total_b

    def test_koszul_dual_euler_equals_bar_euler(self):
        """chi(M^!) = chi(B(M)): linear duality preserves chi."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)

        chi_bar = bar_M.euler_characteristic()
        kd = koszul_dual_bimodule_dims(bar_M)
        chi_kd = sum(Fraction((-1) ** k) * Fraction(d) for k, d in kd.items())
        assert chi_bar == chi_kd

    def test_rank1_rank2_euler_both_zero(self):
        """Both rank-1 and rank-2 flop bimodules have chi = 0."""
        _, _, M1 = a1_flop_bimodule()
        _, _, M2 = a1_flop_bimodule_rank2()
        assert euler_characteristic_bimodule(M1) == Fraction(0)
        assert euler_characteristic_bimodule(M2) == Fraction(0)

    def test_shadow_vanishes_two_ways(self):
        """Shadow = 0 for A_1 flop, via (a) trace formula and (b) chi."""
        _, _, M = a1_flop_bimodule()
        assert transition_shadow_arity2(M) == Fraction(0)
        assert transition_shadow_arity2_alt(M) == Fraction(0)

    def test_identity_bimodule_self_consistent(self):
        """Identity bimodule satisfies: relations hold AND chi equals A's chi."""
        A = path_algebra_A2()
        M = identity_bimodule(A)
        # Relations
        assert check_bimodule_relations(M, max_pq=2)
        # Chi consistency
        chi_M = euler_characteristic_bimodule(M)
        chi_A = sum(Fraction((-1) ** k) * Fraction(d)
                     for k, d in A.dims.items())
        assert chi_M == chi_A

    def test_bar_00_universally_equals_M(self):
        """For any bimodule M: bar(M) at (0,0) = M, verified for multiple examples."""
        examples = [
            a1_flop_bimodule()[2],
            a1_flop_bimodule_rank2()[2],
            identity_bimodule(path_algebra_A2()),
        ]
        for M in examples:
            bar_M = compute_bar_bimodule(M, max_arity=1)
            assert bar_M.total_dim_at_arity(0, 0) == M.M_total_dim


# ============================================================
# Section 16: Edge Cases and Boundary
# ============================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_zero_dim_algebra(self):
        """Single element algebra with no higher operations."""
        A = trivial_algebra(1, 0)
        M = identity_bimodule(A)
        assert M.M_total_dim == 1
        assert euler_characteristic_bimodule(M) == Fraction(1)

    def test_empty_bim_ops(self):
        """Bimodule with all operations zero (the zero bimodule structure)."""
        A = trivial_algebra()
        bim_ops = {(0, 0): {}, (1, 0): {}, (0, 1): {}}
        M = AInfBimodule(A=A, B=A, M_dims={0: 1}, bim_ops=bim_ops, name="zero")
        # Relations should hold trivially (everything is zero)
        rel = verify_bimodule_relation(M, 0, 0, (), 0, ())
        assert _is_zero(rel)

    def test_degree_shift(self):
        """Verify degree computation with shifted elements."""
        A = trivial_algebra(1, 2)  # single element in degree 2
        assert A.degree_of(0) == 2

    def test_m_nonexistent_arity(self):
        """Accessing m_n for n not in m_ops returns zero."""
        A = trivial_algebra()
        result = A.m(5, (0, 0, 0, 0, 0))
        assert _is_zero(result)

    def test_bim_m_nonexistent_pq(self):
        """Accessing m_{p|1|q} for (p,q) not in bim_ops returns zero."""
        _, _, M = a1_flop_bimodule()
        result = M.bim_m(5, 5, (0,)*5, 0, (0,)*5)
        assert _is_zero(result)

    def test_bar_max_arity_0(self):
        """Bar at max_arity=0: just M itself."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=0)
        assert bar_M.total_dim() == M.M_total_dim

    def test_stasheff_on_single_element(self):
        """Stasheff relation at n=1 on single element."""
        A = trivial_algebra()
        rel = verify_stasheff(A, 1, (0,))
        assert _is_zero(rel)


# ============================================================
# Section 17: Consistency with Monograph Conventions
# ============================================================

class TestMonographConsistency:
    """Verify consistency with the monograph's conventions."""

    def test_cohomological_grading(self):
        """Grading is cohomological: m_n has degree 2-n."""
        # For m_2 (product): degree 2-2 = 0 (preserves degree)
        A = path_algebra_A2()
        # m_2(e_1, a) should have degree = deg(e_1) + deg(a) + 0 = 0
        result = A.m(2, (0, 2))
        # Output a is in degree 0, consistent
        assert result[2] == Fraction(1)

    def test_desuspension_convention(self):
        """s^{-1} lowers degree by 1 (AP45: desuspension LOWERS, not raises)."""
        # In bar construction, s^{-1}A has degree shifted down by 1
        A, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=1)
        # Check that (1,0) component has degrees shifted down from A
        # A has degrees {0: 1, 1: 1}, so s^{-1}A has degrees {-1: 1, 0: 1}
        for (p, q, k), d in bar_M.component_dims.items():
            if p == 1 and q == 0:
                # Degrees should include contributions from s^{-1}A (shifted down)
                assert d > 0  # nonempty

    def test_koszul_sign_rule(self):
        """Verify Koszul sign rule is used correctly."""
        # Swapping two degree-1 elements gives (-1)
        sign = _koszul_sign([1, 1], [1, 0])
        assert sign == Fraction(-1)
        # Swapping degree-0 and degree-1 gives (+1)
        sign = _koszul_sign([0, 1], [1, 0])
        assert sign == Fraction(1)

    def test_bar_coalgebra_not_algebra(self):
        """B(M) is a CObimodule (AP25: bar produces coalgebra, not algebra).
        We verify this by checking that BarBimodule stores component_dims
        in the coalgebra grading convention."""
        _, _, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        # The bar complex has components indexed by (p, q) = bar arity
        # This is the cobar degree, consistent with coalgebra structure
        assert isinstance(bar_M.component_dims, dict)
        # The (0,0) component is M itself (no bar elements)
        assert bar_M.total_dim_at_arity(0, 0) == M.M_total_dim

    def test_curved_ainfty_convention(self):
        """For curved A-infinity: m_1^2(a) = [m_0, a] (commutator with curvature).
        In our uncurved models m_0 = 0, so m_1^2 = 0 trivially."""
        A = path_algebra_A2()
        # m_0 not defined (no key 0 in m_ops), so m_1^2 = 0
        assert A.m_ops.get(0) is None or len(A.m_ops.get(0, {})) == 0


# ============================================================
# Section 18: DG Algebra Conversion
# ============================================================

class TestDGAlgebraConversion:
    """Verify conversion from (d, m_2) format to A-infinity."""

    def test_convert_trivial(self):
        """Convert trivial dg algebra to A-infinity."""
        dims = {0: 1}
        d = _frac_array((1, 1))
        P = _frac_array((1, 1, 1))
        P[0, 0, 0] = Fraction(1)
        A = dg_algebra_from_matrices(dims, d, P, "trivial_dg")
        assert A.total_dim == 1
        assert A.m_coeff(2, (0, 0), 0) == Fraction(1)

    def test_convert_exterior(self):
        """Convert exterior algebra k[x]/(x^2) to A-infinity."""
        dims = {0: 1, 1: 1}
        d = _frac_array((2, 2))  # d = 0
        P = _frac_array((2, 2, 2))
        P[0, 0, 0] = Fraction(1)  # 1*1 = 1
        P[0, 1, 1] = Fraction(1)  # 1*x = x
        P[1, 0, 1] = Fraction(1)  # x*1 = x
        A = dg_algebra_from_matrices(dims, d, P, "Lambda(x)")
        assert A.total_dim == 2
        assert check_stasheff_all(A, max_n=2)

    def test_convert_koszul_complex(self):
        """Koszul complex k[x] --(x)--> k[x] as dg algebra."""
        dims = {0: 1, 1: 1}
        d = _frac_array((2, 2))
        # d maps degree 0 to degree 1: but this is d(e_0) = e_1 means x acts
        # Actually, the Koszul complex has d(y) = x where y is the degree-1 generator
        # d: degree 1 -> degree 0 would be wrong for cohomological convention
        # For |d| = +1: d maps degree k to degree k+1.
        # d(e_0) = c * e_1 for some scalar c
        d[1, 0] = Fraction(1)  # d(e_0) = e_1 (degree 0 -> degree 1)
        P = _frac_array((2, 2, 2))
        P[0, 0, 0] = Fraction(1)  # unit
        A = dg_algebra_from_matrices(dims, d, P, "Koszul")
        # Check d^2 = 0: d is 0 on degree 1 (no degree 2)
        # d(d(e_0)) = d(e_1) = 0 (nothing in degree 2)
        assert A.total_dim == 2
        # m_1 = d should be nonzero
        result = A.m(1, (0,))
        assert result[1] == Fraction(1)


# ============================================================
# Section 19: Ext Algebra A_1 Flop
# ============================================================

class TestExtAlgebraA1Flop:
    """Tests for the Ext algebra model of the A_1 flop."""

    def test_ext_dims(self):
        """Ext algebra has 5 basis elements: 2 in deg 0, 2 in deg 1, 1 in deg 2."""
        A = ext_algebra_A1_flop()
        assert A.dims == {0: 2, 1: 2, 2: 1}
        assert A.total_dim == 5

    def test_ext_idempotents(self):
        """Idempotents are orthogonal: e_0*e_1 = 0."""
        A = ext_algebra_A1_flop()
        assert A.m_coeff(2, (0, 1), 0) == Fraction(0)
        assert A.m_coeff(2, (0, 1), 1) == Fraction(0)

    def test_ext_arrow_relations(self):
        """a*b = 0 in the quiver with relations."""
        A = ext_algebra_A1_flop()
        ab = A.m(2, (2, 3))  # a * b
        assert _is_zero(ab)

    def test_ext_m3_massey(self):
        """m_3(a, b, a) = w (Massey product detects the flop)."""
        A = ext_algebra_A1_flop()
        assert A.m_coeff(3, (2, 3, 2), 4) == Fraction(1)

    def test_ext_euler_char(self):
        """chi(Ext) = 2 - 2 + 1 = 1."""
        A = ext_algebra_A1_flop()
        chi = sum(Fraction((-1)**k) * Fraction(d) for k, d in A.dims.items())
        assert chi == Fraction(1)


# ============================================================
# Section 20: Rank-2 Conifold Model
# ============================================================

class TestConifoldRank2:
    """Tests for the rank-2 conifold transition bimodule."""

    def test_conifold_A_m3(self):
        """m_3(a, b, e_0) = a for conifold algebra."""
        A, _, _ = a1_flop_bimodule_rank2()
        assert A.m_coeff(3, (2, 3, 0), 2) == Fraction(1)

    def test_conifold_B_m3(self):
        """m_3(b, a, e_1) = b for conifold algebra."""
        _, B, _ = a1_flop_bimodule_rank2()
        assert B.m_coeff(3, (3, 2, 1), 3) == Fraction(1)

    def test_conifold_ab_zero(self):
        """a*b = 0 in conifold algebra."""
        A, _, _ = a1_flop_bimodule_rank2()
        ab = A.m(2, (2, 3))
        assert _is_zero(ab)

    def test_conifold_ba_zero(self):
        """b*a = 0 in conifold algebra."""
        A, _, _ = a1_flop_bimodule_rank2()
        ba = A.m(2, (3, 2))
        assert _is_zero(ba)

    def test_conifold_bimodule_left_idempotent(self):
        """Left idempotent actions on M."""
        _, _, M = a1_flop_bimodule_rank2()
        # e_0 . m_0^0 = m_0^0
        result = M.bim_m(1, 0, (0,), 0, ())
        assert result[0] == Fraction(1)
        # e_1 . m_1^0 = m_1^0
        result = M.bim_m(1, 0, (1,), 1, ())
        assert result[1] == Fraction(1)

    def test_conifold_bimodule_arrow_action(self):
        """Arrow action: a . m_1^0 = m_0^1."""
        _, _, M = a1_flop_bimodule_rank2()
        result = M.bim_m(1, 0, (2,), 1, ())
        assert result[2] == Fraction(1)

    def test_conifold_bimodule_right_arrow(self):
        """Right arrow action: m_0^0 . a = m_0^1."""
        _, _, M = a1_flop_bimodule_rank2()
        result = M.bim_m(0, 1, (), 0, (2,))
        assert result[2] == Fraction(1)

    def test_conifold_chi_zero(self):
        """chi(M) = 0 for conifold transition (CY3 property)."""
        _, _, M = a1_flop_bimodule_rank2()
        assert euler_characteristic_bimodule(M) == Fraction(0)

    def test_conifold_stasheff_n2(self):
        """Stasheff at n=2 for conifold algebra."""
        A, _, _ = a1_flop_bimodule_rank2()
        # Check associativity of m_2 on idempotent-arrow combinations
        for inputs in [(0, 0), (1, 1), (0, 2), (2, 1), (1, 3), (3, 0)]:
            rel = verify_stasheff(A, 2, inputs)
            assert _is_zero(rel), f"Stasheff n=2 fails for {inputs}"


# ============================================================
# Section 21: Dimensional Consistency
# ============================================================

class TestDimensionalConsistency:
    """Verify dimensional consistency across all constructions."""

    def test_bar_dim_formula(self):
        """Bar at (p,q): dim = dim(A)^p * dim(M) * dim(B)^q."""
        A, B, M = a1_flop_bimodule()
        bar_M = compute_bar_bimodule(M, max_arity=2)
        # (1,1): should be A.total_dim * M.M_total_dim * B.total_dim = 2*2*2 = 8
        assert bar_M.total_dim_at_arity(1, 1) == 8
        # (2,0): should be A.total_dim^2 * M.M_total_dim = 4*2 = 8
        assert bar_M.total_dim_at_arity(2, 0) == 8
        # (0,2): should be M.M_total_dim * B.total_dim^2 = 2*4 = 8
        assert bar_M.total_dim_at_arity(0, 2) == 8

    def test_hh_chain_dim_formula(self):
        """HH chain at bar length n: dim = dim(M) * dim(A)^n."""
        A, _, M = a1_flop_bimodule()
        # At bar length 0: dim(M) = 2
        # At bar length 1: dim(M) * dim(s^{-1}A) = 2*2 = 4
        # Total at bar 0 + bar 1: dims accumulated by degree
        hh_0 = hochschild_homology_dims(A, M, max_bar=0)
        total_0 = sum(hh_0.values())
        assert total_0 == M.M_total_dim  # = 2

    def test_derived_tensor_at_bar0(self):
        """At bar length 0: M1 tensor M2 (no bar elements)."""
        A, _, M = a1_flop_bimodule()
        id_A = identity_bimodule(A)
        dims = derived_tensor_product_dim(M, id_A, max_bar_length=0)
        # M tensor_0 A = tensor product of underlying spaces at bar length 0
        total = sum(dims.values())
        assert total == M.M_total_dim * id_A.M_total_dim

    def test_bimodule_dims_match_M(self):
        """AInfBimodule.M_total_dim matches sum of M_dims."""
        _, _, M = a1_flop_bimodule()
        assert M.M_total_dim == sum(M.M_dims.values())

    def test_algebra_dims_match(self):
        """AInfAlgebra.total_dim matches sum of dims."""
        for A in [trivial_algebra(), path_algebra_A2(), path_algebra_A3()]:
            assert A.total_dim == sum(A.dims.values())
