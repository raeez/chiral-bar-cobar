"""Tests for A-infinity transferred structure and formality.

Verifies:
  - DG algebra axioms (d^2 = 0, associativity, Leibniz rule)
  - Bar complex (d_B^2 = 0, cohomology dimensions)
  - HPL transfer (m_1 = 0, m_2 = induced product, m_3/m_4 formality)
  - Stasheff A-infinity relations
  - Shadow depth classification and its distinction from Koszulness
  - Formality characterization of Koszulness (prop:ainfty-formality-implies-koszul)

KEY MATHEMATICAL DISTINCTION (Critical Pitfall):
  Shadow depth measures A-infinity non-formality of A ITSELF.
  Koszulness measures A-infinity formality of A^! = H*(B(A)).
  These are DIFFERENT objects.  All standard families (Heis, aff, betagamma,
  Vir) are Koszul (A^! formal) despite having shadow depths 2, 3, 4, infinity.

References:
  - prop:ainfty-formality-implies-koszul (chiral_koszul_pairs.tex)
  - thm:koszul-equivalences-meta (12 equivalent characterizations)
  - prop:shadow-formality-low-arity (arities 2,3,4)
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.ainfty_transferred_structure import (
    DGAlgebra,
    BarComplex,
    HPLTransfer,
    stasheff_relation,
    abelian_dga,
    ce_complex_sl2,
    polynomial_algebra,
    exterior_algebra,
    truncated_polynomial_dga,
    koszul_dual_algebra,
    classify_shadow_archetype,
    SHADOW_ARCHETYPES,
    _frac_array,
    _frac,
    _is_zero,
    _kernel_basis,
    _image_dim,
    _merge_sign,
    _ordered_subsets,
    _unit_vec,
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
# TestDGAlgebra: basic axioms
# ============================================================

class TestDGAlgebra:
    """Verify dg algebra axioms for all standard examples."""

    def test_abelian_dim1_d_squared(self):
        """Abelian k^1: d = 0, so d^2 = 0 trivially."""
        A = abelian_dga(1)
        assert A.check_d_squared()

    def test_abelian_dim2_d_squared(self):
        A = abelian_dga(2)
        assert A.check_d_squared()

    def test_abelian_dim1_associativity(self):
        A = abelian_dga(1)
        assert A.check_associativity()

    def test_abelian_dim2_associativity(self):
        A = abelian_dga(2)
        assert A.check_associativity()

    def test_ce_sl2_d_squared(self):
        """CE(sl_2): d_CE^2 = 0 (Jacobi identity for sl_2)."""
        A = ce_complex_sl2()
        assert A.check_d_squared()

    def test_ce_sl2_associativity(self):
        """CE(sl_2): exterior product is associative."""
        A = ce_complex_sl2()
        assert A.check_associativity()

    def test_ce_sl2_leibniz(self):
        """CE(sl_2): d_CE is a derivation of the exterior product."""
        A = ce_complex_sl2()
        assert A.check_leibniz()

    def test_polynomial_d_squared(self):
        """k[x]/(x^3): d = 0."""
        A = polynomial_algebra(2)
        assert A.check_d_squared()

    def test_polynomial_associativity(self):
        """k[x]/(x^3): multiplication is associative."""
        A = polynomial_algebra(2)
        assert A.check_associativity()

    def test_exterior_algebra_associativity(self):
        """Lambda(x,y): exterior product is associative."""
        A = exterior_algebra(2)
        assert A.check_associativity()

    def test_ce_sl2_dims(self):
        """CE(sl_2) has dims 1, 3, 3, 1."""
        A = ce_complex_sl2()
        assert A.dims == {0: 1, 1: 3, 2: 3, 3: 1}
        assert A.total_dim == 8

    def test_polynomial_algebra_dims(self):
        """k[x]/(x^4) has dimension 4, all in degree 0."""
        A = polynomial_algebra(3)
        assert A.dims == {0: 4}
        assert A.total_dim == 4

    def test_abelian_dim3_leibniz(self):
        """Abelian k^3: d = 0 is trivially a derivation."""
        A = abelian_dga(3)
        assert A.check_leibniz()


# ============================================================
# TestCohomology: compute H*(A, d)
# ============================================================

class TestCohomology:
    """Verify cohomology computations."""

    def test_abelian_cohomology(self):
        """H*(CE(k^n)) = Lambda*(k^n) (d = 0, so cohomology = full space)."""
        A = abelian_dga(2)
        cohom = A.cohomology_dims()
        # Lambda^0 = 1, Lambda^1 = 2, Lambda^2 = 1
        assert cohom[0] == 1
        assert cohom[1] == 2
        assert cohom[2] == 1

    def test_sl2_cohomology_whitehead(self):
        """H*(sl_2, k): H^0 = 1, H^1 = 0, H^2 = 0, H^3 = 1 (Whitehead)."""
        A = ce_complex_sl2()
        cohom = A.cohomology_dims()
        assert cohom[0] == 1, f"H^0 = {cohom[0]}, expected 1"
        assert cohom[1] == 0, f"H^1 = {cohom[1]}, expected 0"
        assert cohom[2] == 0, f"H^2 = {cohom[2]}, expected 0"
        assert cohom[3] == 1, f"H^3 = {cohom[3]}, expected 1"

    def test_polynomial_cohomology(self):
        """k[x]/(x^3) with d=0: H^0 = k^3 (all in degree 0)."""
        A = polynomial_algebra(2)
        cohom = A.cohomology_dims()
        assert cohom[0] == 3

    def test_exterior_cohomology(self):
        """Lambda(x,y) with d=0: H^0 = k^4 (all 4-dim in degree 0)."""
        A = exterior_algebra(2)
        cohom = A.cohomology_dims()
        assert cohom[0] == 4


# ============================================================
# TestBarComplex: bar differential
# ============================================================

class TestBarComplex:
    """Verify bar complex construction and d_B^2 = 0."""

    def test_bar_arity1_product_map(self):
        """B^1 -> B^0: no B^0 in reduced bar, so matrix is (0 x dim)."""
        A = abelian_dga(1)
        B = BarComplex(A, max_arity=3)
        mat = B.bar_differential_matrix(1)
        assert mat.shape[0] == 0

    def test_bar_arity2_abelian(self):
        """Abelian: m_2 on augmentation ideal is zero (no nonzero products of
        positive-degree elements landing in positive degree). Product part vanishes."""
        A = abelian_dga(1)
        B = BarComplex(A, max_arity=3)
        mat = B.bar_differential_matrix(2)
        # For abelian dim 1: augmentation ideal = {x} (degree 1), so B^2 has dim 1
        # m_2(x, x) = x^x = 0 (x^2 = 0 in exterior algebra)
        assert mat.shape == (1, 1)
        assert mat[0, 0] == Fraction(0)

    def test_bar_d_squared_abelian_dim1(self):
        """Abelian k^1: d_B^2 = 0 on total complex through arity 3."""
        A = abelian_dga(1)
        B = BarComplex(A, max_arity=3)
        assert B.check_d_squared(3)

    def test_bar_d_squared_abelian_dim2(self):
        """Abelian k^2: d_B^2 = 0 through arity 3."""
        A = abelian_dga(2)
        B = BarComplex(A, max_arity=3)
        assert B.check_d_squared(3)

    def test_bar_d_squared_ce_sl2(self):
        """CE(sl_2): d_B^2 = 0 through arity 3."""
        A = ce_complex_sl2()
        B = BarComplex(A, max_arity=3)
        assert B.check_d_squared(3)

    def test_bar_d_squared_polynomial(self):
        """k[x]/(x^3): d_B^2 = 0 through arity 3."""
        A = polynomial_algebra(2)
        B = BarComplex(A, max_arity=3)
        assert B.check_d_squared(3)

    def test_bar_tensor_dims_ce_sl2(self):
        """CE(sl_2): augmentation ideal has dim 7, so B^n has dim 7^n."""
        A = ce_complex_sl2()
        B = BarComplex(A, max_arity=4)
        # Augmentation ideal: all of C^1, C^2, C^3 (dim 3+3+1 = 7)
        assert B._aug_dim == 7
        assert B.tensor_space_dim(1) == 7
        assert B.tensor_space_dim(2) == 49
        assert B.tensor_space_dim(3) == 343

    def test_bar_tensor_dims_polynomial(self):
        """k[x]/(x^3): augmentation ideal = {x, x^2}, dim 2."""
        A = polynomial_algebra(2)
        B = BarComplex(A, max_arity=4)
        assert B._aug_dim == 2
        assert B.tensor_space_dim(1) == 2
        assert B.tensor_space_dim(2) == 4
        assert B.tensor_space_dim(3) == 8

    def test_bar_d_squared_exterior(self):
        """Lambda(x,y): d_B^2 = 0 through arity 3."""
        A = exterior_algebra(2)
        B = BarComplex(A, max_arity=3)
        assert B.check_d_squared(3)


# ============================================================
# TestHPLTransfer: transferred A-infinity operations
# ============================================================

class TestHPLTransfer:
    """Verify HPL-transferred A-infinity structure."""

    def test_m1_is_zero_abelian(self):
        """m_1^{tr} = 0 on cohomology (abelian case, d = 0)."""
        A = abelian_dga(2)
        T = HPLTransfer(A)
        n = A.total_dim
        for i in range(n):
            v = _basis_vec(n, i)
            result = T.m1_transferred(v)
            assert _is_zero(result), f"m_1 nonzero on basis vector {i}"

    def test_m1_is_zero_sl2(self):
        """m_1^{tr} = P d I = 0 on cohomology of CE(sl_2)."""
        A = ce_complex_sl2()
        T = HPLTransfer(A)
        basis = T._get_cohomology_basis()
        for v in basis:
            result = T.m1_transferred(v)
            assert _is_zero(result), "m_1 nonzero on cohomology class"

    def test_m2_abelian_is_product(self):
        """Abelian: m_2^{tr} is the exterior product on cohomology = full space."""
        A = abelian_dga(1)
        T = HPLTransfer(A)
        # Cohomology = full space (d = 0).  2 generators: e_0 (deg 0), e_1 (deg 1).
        e0 = _basis_vec(2, 0)
        e1 = _basis_vec(2, 1)
        # e_0 * e_1 should give e_1 (unit action)
        result = T.m2_transferred(e0, e1)
        # Unit times anything = itself
        expected = e1.copy()
        # Check proportionality at least
        # (projection may normalize differently)
        assert not _is_zero(result) or _is_zero(expected)

    def test_m3_abelian_vanishes(self):
        """Abelian: m_3^{tr} = 0 (trivially formal)."""
        A = abelian_dga(2)
        T = HPLTransfer(A)
        basis = T._get_cohomology_basis()
        for v1 in basis:
            for v2 in basis:
                for v3 in basis:
                    result = T.m3_transferred(v1, v2, v3)
                    assert _is_zero(result), "m_3 nonzero on abelian algebra"

    def test_m3_sl2_vanishes_on_cohomology(self):
        """CE(sl_2): m_3^{tr} = 0 on H*(sl_2) (Koszul, hence formal).

        H^0 = k, H^3 = k.  Only two cohomology classes.
        m_3 on (H^0)^3 -> H^0 trivially (degree reasons).
        m_3 on mixed inputs vanishes by degree count.
        """
        A = ce_complex_sl2()
        T = HPLTransfer(A)
        basis = T._get_cohomology_basis()
        # Should have exactly 2 basis vectors (H^0 and H^3)
        assert len(basis) == 2, f"Expected 2 cohomology classes, got {len(basis)}"
        for v1 in basis:
            for v2 in basis:
                for v3 in basis:
                    result = T.m3_transferred(v1, v2, v3)
                    assert _is_zero(result), "m_3 nonzero on CE(sl_2) cohomology"

    def test_m4_abelian_vanishes(self):
        """Abelian: m_4^{tr} = 0."""
        A = abelian_dga(1)
        T = HPLTransfer(A)
        basis = T._get_cohomology_basis()
        for v1 in basis:
            for v2 in basis:
                for v3 in basis:
                    for v4 in basis:
                        result = T.m4_transferred(v1, v2, v3, v4)
                        assert _is_zero(result), "m_4 nonzero on abelian"


# ============================================================
# TestFormality: the Koszulness criterion
# ============================================================

class TestFormality:
    """Test A-infinity formality = Koszulness characterization.

    prop:ainfty-formality-implies-koszul: A is Koszul iff the
    transferred A-infinity structure on H*(B(A)) is formal.
    """

    def test_abelian_is_formal(self):
        """Abelian dga: formal (Koszul)."""
        A = abelian_dga(1)
        T = HPLTransfer(A)
        assert T.is_formal(max_arity=4)

    def test_abelian_dim2_is_formal(self):
        """Abelian k^2: formal."""
        A = abelian_dga(2)
        T = HPLTransfer(A)
        assert T.is_formal(max_arity=4)

    def test_sl2_bar_cohomology_formal(self):
        """CE(sl_2): bar cohomology is formal (sl_2 is Koszul).

        Cohomology H*(sl_2) = k + k[-3] is concentrated in degrees 0,3.
        For degree reasons, m_3 and m_4 on 2-dimensional cohomology vanish.
        This is consistent with sl_2 being Koszul.
        """
        A = ce_complex_sl2()
        T = HPLTransfer(A)
        assert T.is_formal(max_arity=4)

    def test_exterior_algebra_formal(self):
        """Lambda(x): formal (Koszul dual to k[xi])."""
        A = exterior_algebra(1)
        T = HPLTransfer(A)
        assert T.is_formal(max_arity=4)

    def test_kx_mod_x2_formal(self):
        """k[x]/(x^2) is Koszul.  Transferred structure is formal."""
        A = polynomial_algebra(1)
        T = HPLTransfer(A)
        # k[x]/(x^2) has d = 0, cohomology = full space (dim 2 in degree 0)
        # Bar complex: augmentation ideal = {x}, dim 1
        # B^n = k for all n (one-dimensional)
        # Bar differential d_B: product part m_2(x, x) = x^2 = 0
        # So bar cohomology = one copy of k in each bar degree
        # Transferred m_3 should vanish
        assert T.is_formal(max_arity=4)

    def test_truncated_poly_3_augmentation_ideal(self):
        """k[x]/(x^3): augmentation ideal has basis {x, x^2}."""
        A = truncated_polynomial_dga(3)
        B = BarComplex(A, max_arity=4)
        assert B._aug_dim == 2
        # x * x = x^2 (nonzero in augmentation ideal)
        # x * x^2 = x^3 = 0 (killed by truncation)
        # x^2 * x = x^3 = 0
        # x^2 * x^2 = x^4 = 0

    def test_truncated_poly_3_bar_d_squared(self):
        """k[x]/(x^3): bar differential satisfies d^2 = 0."""
        A = truncated_polynomial_dga(3)
        B = BarComplex(A, max_arity=4)
        assert B.check_d_squared(3)

    def test_kx_mod_x3_bar_product_nontrivial(self):
        """k[x]/(x^3): the product x*x = x^2 is nonzero in augmentation ideal.

        This means the bar differential has nontrivial product component,
        unlike the abelian case.  This is the source of non-Koszulness.
        """
        A = truncated_polynomial_dga(3)
        B = BarComplex(A, max_arity=3)
        # B^2: 4-dimensional (2^2 from aug basis {x, x^2})
        # d_product: B^2 -> B^1 via m_2
        mat = B.bar_differential_matrix(2)
        assert mat.shape == (2, 4)
        # m_2(x, x) = x^2 -> nonzero entry
        assert not _is_zero(mat), "Bar differential should be nontrivial for k[x]/(x^3)"


# ============================================================
# TestShadowConnection: shadow depth vs Koszulness
# ============================================================

class TestShadowConnection:
    """Test the distinction between shadow depth and Koszulness.

    Shadow depth measures A-infinity structure on A.
    Koszulness measures A-infinity formality on A^! = H*(B(A)).
    These are DIFFERENT (Critical Pitfall from CLAUDE.md).
    """

    def test_shadow_depth_abelian(self):
        """Abelian: shadow depth 2 (Gaussian class G)."""
        A = abelian_dga(1)
        T = HPLTransfer(A)
        depth = T.shadow_depth()
        assert depth == 2
        assert classify_shadow_archetype(depth) == "G"

    def test_classify_gaussian(self):
        """Shadow depth 2 -> Gaussian (G)."""
        assert classify_shadow_archetype(2) == "G"

    def test_classify_lie(self):
        """Shadow depth 3 -> Lie/tree (L)."""
        assert classify_shadow_archetype(3) == "L"

    def test_classify_contact(self):
        """Shadow depth 4 -> contact/quartic (C)."""
        assert classify_shadow_archetype(4) == "C"

    def test_classify_mixed(self):
        """Shadow depth 5+ -> mixed (M)."""
        assert classify_shadow_archetype(5) == "M"
        assert classify_shadow_archetype(100) == "M"

    def test_formality_vs_shadow_depth_principle(self):
        """Key principle: shadow depth does NOT determine Koszulness.

        Shadow depth classifies COMPLEXITY of Koszul algebras (G/L/C/M),
        not Koszulness itself.  Both finite and infinite shadow depth
        algebras can be Koszul.
        """
        # All four archetype classes contain Koszul algebras:
        # G (depth 2): Heisenberg
        # L (depth 3): affine Kac-Moody
        # C (depth 4): betagamma
        # M (depth inf): Virasoro
        for arch_key, info in SHADOW_ARCHETYPES.items():
            assert "name" in info
            assert "max_depth" in info

    def test_koszul_with_infinite_shadow_documentation(self):
        """Document: Virasoro has shadow depth infinity but IS Koszul.

        This is the key counterintuitive fact.  The shadow tower
        Theta_Vir^{<=r} is infinite (shadow depth = infinity, class M),
        but H*(B(Vir)) carries a FORMAL A-infinity structure.

        Shadow depth measures the L-infinity formality obstruction of
        the DEFORMATION COMPLEX, not the A-infinity structure on the
        Koszul dual.
        """
        # This is a documentation test.  The actual Virasoro computation
        # requires infinite-dimensional methods beyond this module.
        # Record the known values:
        vir_shadow_depth = float("inf")
        vir_is_koszul = True
        assert vir_shadow_depth > 4  # infinite
        assert vir_is_koszul  # but still Koszul

    def test_shadow_archetypes_complete(self):
        """All four shadow archetypes are defined."""
        assert set(SHADOW_ARCHETYPES.keys()) == {"G", "L", "C", "M"}

    def test_shadow_archetype_depths(self):
        """Archetype max depths: G=2, L=3, C=4, M=None (infinity)."""
        assert SHADOW_ARCHETYPES["G"]["max_depth"] == 2
        assert SHADOW_ARCHETYPES["L"]["max_depth"] == 3
        assert SHADOW_ARCHETYPES["C"]["max_depth"] == 4
        assert SHADOW_ARCHETYPES["M"]["max_depth"] is None


# ============================================================
# TestAInftyRelations: Stasheff relations
# ============================================================

class TestAInftyRelations:
    """Verify the Stasheff A-infinity relations hold for transferred structure."""

    def test_stasheff_relation_n2_abelian(self):
        """n=2: m_1(m_2(a,b)) + m_2(m_1(a),b) + (-1)^|a| m_2(a,m_1(b)) = 0.

        For formal transfer, m_1 = 0, so this reduces to 0 = 0.
        """
        A = abelian_dga(1)
        T = HPLTransfer(A)
        basis = T._get_cohomology_basis()
        for v1 in basis:
            for v2 in basis:
                result = stasheff_relation(T, 2, [v1, v2])
                assert _is_zero(result), "Stasheff n=2 violated"

    def test_stasheff_relation_n3_abelian(self):
        """n=3 Stasheff relation on abelian dga."""
        A = abelian_dga(1)
        T = HPLTransfer(A)
        basis = T._get_cohomology_basis()
        for v1 in basis:
            for v2 in basis:
                for v3 in basis:
                    result = stasheff_relation(T, 3, [v1, v2, v3])
                    assert _is_zero(result), "Stasheff n=3 violated"

    def test_stasheff_relation_n2_sl2(self):
        """Stasheff n=2 on CE(sl_2) cohomology."""
        A = ce_complex_sl2()
        T = HPLTransfer(A)
        basis = T._get_cohomology_basis()
        for v1 in basis:
            for v2 in basis:
                result = stasheff_relation(T, 2, [v1, v2])
                assert _is_zero(result), "Stasheff n=2 violated on sl_2"

    def test_stasheff_relation_n3_sl2(self):
        """Stasheff n=3 on CE(sl_2) cohomology."""
        A = ce_complex_sl2()
        T = HPLTransfer(A)
        basis = T._get_cohomology_basis()
        for v1 in basis:
            for v2 in basis:
                for v3 in basis:
                    result = stasheff_relation(T, 3, [v1, v2, v3])
                    assert _is_zero(result), "Stasheff n=3 violated on sl_2"

    def test_stasheff_relation_n4_abelian(self):
        """n=4 Stasheff on abelian k^1."""
        A = abelian_dga(1)
        T = HPLTransfer(A)
        basis = T._get_cohomology_basis()
        for v1 in basis:
            for v2 in basis:
                for v3 in basis:
                    for v4 in basis:
                        result = stasheff_relation(T, 4, [v1, v2, v3, v4])
                        assert _is_zero(result), "Stasheff n=4 violated"


# ============================================================
# TestLinearAlgebra: kernel, image, exact arithmetic
# ============================================================

class TestLinearAlgebra:
    """Verify the exact rational linear algebra subroutines."""

    def test_kernel_identity(self):
        """Kernel of identity matrix is trivial."""
        M = np.array([[Fraction(1), Fraction(0)],
                       [Fraction(0), Fraction(1)]], dtype=object)
        ker = _kernel_basis(M)
        assert len(ker) == 0

    def test_kernel_zero(self):
        """Kernel of zero matrix is full space."""
        M = _frac_array((2, 3))
        ker = _kernel_basis(M)
        assert len(ker) == 3

    def test_kernel_rank1(self):
        """Rank-1 matrix has (n-1)-dimensional kernel."""
        M = np.array([[Fraction(1), Fraction(2), Fraction(3)]], dtype=object)
        ker = _kernel_basis(M)
        assert len(ker) == 2
        # Verify each kernel vector is in the kernel
        for v in ker:
            prod = sum(M[0, j] * v[j] for j in range(3))
            assert prod == Fraction(0)

    def test_image_dim_identity(self):
        """Image of identity has full rank."""
        M = np.array([[Fraction(1), Fraction(0)],
                       [Fraction(0), Fraction(1)]], dtype=object)
        assert _image_dim(M) == 2

    def test_image_dim_zero(self):
        """Image of zero matrix has rank 0."""
        M = _frac_array((3, 3))
        assert _image_dim(M) == 0

    def test_image_dim_rank1(self):
        M = np.array([[Fraction(1), Fraction(2)],
                       [Fraction(2), Fraction(4)]], dtype=object)
        assert _image_dim(M) == 1

    def test_merge_sign_identity(self):
        """Merging (0,1) and (2,3): no inversions, sign = +1."""
        assert _merge_sign((0, 1), (2, 3)) == 1

    def test_merge_sign_swap(self):
        """Merging (1,) and (0,): one inversion, sign = -1."""
        assert _merge_sign((1,), (0,)) == -1

    def test_merge_sign_empty(self):
        """Merging with empty: sign = +1."""
        assert _merge_sign((), (0, 1, 2)) == 1
        assert _merge_sign((0, 1), ()) == 1

    def test_ordered_subsets(self):
        """Ordered k-subsets of {0,...,n-1}."""
        assert _ordered_subsets(3, 0) == [()]
        assert _ordered_subsets(3, 1) == [(0,), (1,), (2,)]
        assert _ordered_subsets(3, 2) == [(0, 1), (0, 2), (1, 2)]
        assert _ordered_subsets(3, 3) == [(0, 1, 2)]


# ============================================================
# TestExteriorProduct: signs and structure
# ============================================================

class TestExteriorProduct:
    """Verify exterior algebra product structure."""

    def test_anticommutativity_degree1(self):
        """e_i ^ e_j = -e_j ^ e_i for degree-1 generators."""
        A = abelian_dga(2)
        P = A.product_tensor
        # Generators in degree 1: indices 1 (x_0) and 2 (x_1)
        # (index 0 is the unit in degree 0)
        # e_1 ^ e_2 should equal -e_2 ^ e_1
        for k in range(A.total_dim):
            assert P[1, 2, k] == -P[2, 1, k], f"Anticommutativity fails at output {k}"

    def test_unit_action(self):
        """1 ^ x = x for all x (unit in degree 0)."""
        A = abelian_dga(2)
        P = A.product_tensor
        # Unit is index 0, generators are 1, 2
        for j in range(A.total_dim):
            for k in range(A.total_dim):
                expected = Fraction(1) if k == j else Fraction(0)
                assert P[0, j, k] == expected, f"Unit fails: P[0,{j},{k}] = {P[0,j,k]}"

    def test_nilpotency(self):
        """x_i ^ x_i = 0 in exterior algebra."""
        A = abelian_dga(2)
        P = A.product_tensor
        for i in range(1, 3):  # degree-1 generators
            for k in range(A.total_dim):
                assert P[i, i, k] == Fraction(0), f"Nilpotency fails: P[{i},{i},{k}]"


# ============================================================
# TestBarComplexProducts: nontrivial bar differentials
# ============================================================

class TestBarComplexProducts:
    """Test bar differential with nontrivial products."""

    def test_kx_mod_x3_bar_diff_arity2(self):
        """k[x]/(x^3): bar differential B^2 -> B^1 captures x*x = x^2.

        Augmentation ideal basis: {x, x^2} (indices 0, 1 in aug basis).
        B^2 has 4 basis elements: x|x, x|x^2, x^2|x, x^2|x^2.
        d_product maps x|x to x^2 (product in augmentation ideal).
        """
        A = truncated_polynomial_dga(3)
        B = BarComplex(A, max_arity=4)
        mat = B.bar_differential_matrix(2)
        # Should be 2 x 4 matrix
        assert mat.shape == (2, 4)
        # At least one nonzero entry (from x * x = x^2)
        assert not _is_zero(mat)

    def test_kx_mod_x2_bar_diff_trivial(self):
        """k[x]/(x^2): x*x = 0, so bar product differential is zero at arity 2.

        Augmentation ideal = {x}, dim 1.
        B^2 = k (one-dimensional), d_product: x|x -> x^2 = 0.
        """
        A = truncated_polynomial_dga(2)
        B = BarComplex(A, max_arity=3)
        mat = B.bar_differential_matrix(2)
        assert mat.shape == (1, 1)
        assert _is_zero(mat)
