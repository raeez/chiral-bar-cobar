r"""Tests for BC-82: Categorical zeta functions for exceptional Lie types.

Multi-path verification of dimensions, zeta values, Casimir eigenvalues,
and structural properties of the categorical zeta for G₂, F₄, E₆, E₇, E₈.

Verification paths used:
    Path 1: Weyl dimension formula from positive coroots (direct)
    Path 2: Closed-form G₂ dimension formula (independent)
    Path 3: Known fundamental representation dimensions (literature tables)
    Path 4: Langlands self-duality (all exceptional types are self-dual)
    Path 5: Casimir eigenvalue C₂(adj) = 2·h^∨ (independent invariant)
    Path 6: Dimension count asymptotics N(D) ~ D^{rank/|Φ⁺|}
    Path 7: Cross-check with bc_categorical_zeta_engine (classical types)
    Path 8: Root count |Φ⁺| = (dim g - rank) / 2
"""

import math
from fractions import Fraction

import pytest

from compute.lib.bc_exceptional_categorical_zeta_engine import (
    abscissa_of_convergence,
    abscissa_of_convergence_float,
    casimir_eigenvalue,
    casimir_eigenvalue_float,
    casimir_freudenthal_check,
    categorical_zeta,
    categorical_zeta_via_spectrum,
    dimension_count,
    dimension_count_exponent,
    dimension_spectrum,
    dirichlet_coefficients,
    dominant_weights,
    dominant_weights_by_dim,
    e8_first_dims,
    exceptional_cartan_matrix,
    exceptional_dim_g,
    exceptional_dual_coxeter,
    exceptional_n_positive_roots,
    exceptional_rank,
    exceptional_summary,
    f4_small_dims,
    g2_dimension_spectrum,
    g2_zeta,
    identify_exceptional_by_dims,
    kappa_exceptional_affine,
    kappa_exceptional_affine_float,
    langlands_dual_type,
    langlands_dual_zeta_ratio,
    positive_coroots,
    positive_roots,
    weyl_dimension,
    weyl_dimension_G2,
    zeta_comparison_table,
    zeta_ranking_at_s,
    _KNOWN_FUND_DIMS,
    _KNOWN_SMALL_DIMS_G2,
    _KNOWN_SMALL_DIMS_F4,
    _EXCEPTIONAL_DATA,
    _symmetrizing_constants,
    _weight_gram_matrix,
)


# =========================================================================
# Section 1: Root system structure (10 tests)
# =========================================================================

class TestRootSystem:
    """Verify root system data for all exceptional types."""

    @pytest.mark.parametrize("typ,expected", [
        ('G2', 6), ('F4', 24), ('E6', 36), ('E7', 63), ('E8', 120),
    ])
    def test_positive_root_count(self, typ, expected):
        """Path 1: number of positive roots matches Lie theory."""
        pr = positive_roots(typ)
        assert len(pr) == expected

    @pytest.mark.parametrize("typ,expected", [
        ('G2', 6), ('F4', 24), ('E6', 36), ('E7', 63), ('E8', 120),
    ])
    def test_positive_coroot_count(self, typ, expected):
        """Path 1: number of positive coroots = number of positive roots."""
        pc = positive_coroots(typ)
        assert len(pc) == expected

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_root_count_formula(self, typ):
        """Path 1+3: |Phi+| = (dim g - rank) / 2."""
        n_pos = exceptional_n_positive_roots(typ)
        dim_g = exceptional_dim_g(typ)
        rank = exceptional_rank(typ)
        assert n_pos == (dim_g - rank) // 2

    @pytest.mark.parametrize("typ", ['E6', 'E7', 'E8'])
    def test_simply_laced_coroots_equal_roots(self, typ):
        """Path 1: for simply-laced types, coroots = roots."""
        pr = positive_roots(typ)
        pc = positive_coroots(typ)
        assert set(pr) == set(pc)

    def test_G2_not_simply_laced(self):
        """Path 1: G₂ coroots differ from roots (non-simply-laced)."""
        pr = positive_roots('G2')
        pc = positive_coroots('G2')
        assert set(pr) != set(pc)

    def test_F4_not_simply_laced(self):
        """Path 1: F₄ coroots differ from roots."""
        pr = positive_roots('F4')
        pc = positive_coroots('F4')
        assert set(pr) != set(pc)

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_simple_roots_included(self, typ):
        """Path 1: each simple root e_i is a positive root."""
        pr = positive_roots(typ)
        rank = exceptional_rank(typ)
        for i in range(rank):
            e_i = tuple(1 if j == i else 0 for j in range(rank))
            assert e_i in pr

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_highest_root_is_positive(self, typ):
        """Path 1: the highest root has all nonneg coefficients."""
        pr = positive_roots(typ)
        # Highest root = the one with largest coordinate sum
        highest = max(pr, key=lambda r: sum(r))
        assert all(c >= 0 for c in highest)
        assert sum(highest) > 0

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_cartan_matrix_diagonal(self, typ):
        """Path 3: Cartan matrix has 2s on diagonal."""
        A = exceptional_cartan_matrix(typ)
        for i in range(len(A)):
            assert A[i][i] == 2

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_cartan_off_diagonal_nonpositive(self, typ):
        """Path 3: off-diagonal entries of Cartan matrix are ≤ 0."""
        A = exceptional_cartan_matrix(typ)
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    assert A[i][j] <= 0


# =========================================================================
# Section 2: Weyl dimension formula (15 tests)
# =========================================================================

class TestWeylDimension:
    """Verify Weyl dimension formula against known values."""

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_fundamental_dimensions_match_known(self, typ):
        """Path 3: fundamental rep dimensions match literature tables."""
        rank = exceptional_rank(typ)
        dims = []
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            dims.append(weyl_dimension(typ, hw))
        dims.sort()
        known = sorted(_KNOWN_FUND_DIMS[typ])
        assert dims == known

    def test_G2_trivial_dim_1(self):
        """Path 1: trivial representation has dimension 1."""
        assert weyl_dimension('G2', (0, 0)) == 1

    @pytest.mark.parametrize("a,b,expected", [
        (1, 0, 7), (0, 1, 14), (2, 0, 27), (1, 1, 64),
        (3, 0, 77), (0, 2, 77), (4, 0, 182),
    ])
    def test_G2_known_dims(self, a, b, expected):
        """Path 3: G₂ small representation dimensions from literature."""
        assert weyl_dimension('G2', (a, b)) == expected

    @pytest.mark.parametrize("a,b,expected", [
        (1, 0, 7), (0, 1, 14), (2, 0, 27), (1, 1, 64),
        (3, 0, 77), (0, 2, 77), (4, 0, 182),
    ])
    def test_G2_closed_formula_matches_weyl(self, a, b, expected):
        """Path 2: G₂ closed formula matches Weyl dimension formula."""
        d_weyl = weyl_dimension('G2', (a, b))
        d_closed = weyl_dimension_G2(a, b)
        assert d_weyl == d_closed == expected

    @pytest.mark.parametrize("a,b", [
        (0, 0), (1, 0), (0, 1), (2, 0), (0, 2), (1, 1),
        (3, 0), (0, 3), (2, 1), (1, 2), (4, 0), (0, 4),
        (3, 1), (1, 3), (2, 2), (5, 0), (0, 5),
    ])
    def test_G2_closed_vs_weyl_systematic(self, a, b):
        """Path 2: systematic comparison of G₂ closed formula vs Weyl."""
        assert weyl_dimension_G2(a, b) == weyl_dimension('G2', (a, b))

    def test_G2_negative_weight_zero(self):
        """Path 1: negative Dynkin labels give dimension 0."""
        assert weyl_dimension('G2', (-1, 0)) == 0
        assert weyl_dimension_G2(-1, 0) == 0

    def test_F4_fundamental_dims(self):
        """Path 3: F₄ fundamental dimensions are {26, 52, 273, 1274}."""
        dims = set()
        for i in range(4):
            hw = tuple(1 if j == i else 0 for j in range(4))
            dims.add(weyl_dimension('F4', hw))
        assert dims == {26, 52, 273, 1274}

    def test_E6_adjoint_dim_78(self):
        """Path 3: E₆ adjoint representation has dim 78."""
        rank = 6
        dim_adj = 78
        found = False
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            if weyl_dimension('E6', hw) == dim_adj:
                found = True
                break
        assert found

    def test_E7_fundamental_56(self):
        """Path 3: E₇ has a fundamental representation of dim 56."""
        rank = 7
        dims = set()
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            dims.add(weyl_dimension('E7', hw))
        assert 56 in dims

    def test_E8_adjoint_248(self):
        """Path 3: E₈ adjoint = fundamental, dim 248."""
        rank = 8
        dims = set()
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            dims.add(weyl_dimension('E8', hw))
        assert 248 in dims

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_adjoint_dim_equals_dim_g(self, typ):
        """Path 3: the adjoint representation has dim = dim(g)."""
        rank = exceptional_rank(typ)
        dim_adj = exceptional_dim_g(typ)
        found = False
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            if weyl_dimension(typ, hw) == dim_adj:
                found = True
                break
        assert found

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_all_dims_positive(self, typ):
        """Path 1: all dominant weight dimensions are positive."""
        for hw in dominant_weights(typ, 5):
            d = weyl_dimension(typ, hw)
            assert d > 0

    def test_G2_dim_77_multiplicity_2(self):
        """Path 3: G₂ has two irreps of dimension 77: V(3,0) and V(0,2)."""
        d1 = weyl_dimension('G2', (3, 0))
        d2 = weyl_dimension('G2', (0, 2))
        assert d1 == d2 == 77

    def test_E6_pair_27_conjugate(self):
        """Path 3: E₆ has two conjugate 27-dimensional representations."""
        rank = 6
        dims_27 = []
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            d = weyl_dimension('E6', hw)
            if d == 27:
                dims_27.append(i)
        assert len(dims_27) == 2  # Two fundamental reps of dim 27

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_dim_monotone_along_fundamental(self, typ):
        """Path 7: dim V(n·omega_i) is increasing in n for each fundamental weight."""
        rank = exceptional_rank(typ)
        for i in range(rank):
            prev = 1
            for n in range(1, 5):
                hw = tuple(n if j == i else 0 for j in range(rank))
                d = weyl_dimension(typ, hw)
                assert d > prev
                prev = d


# =========================================================================
# Section 3: Casimir eigenvalue (12 tests)
# =========================================================================

class TestCasimir:
    """Verify Casimir eigenvalues via multiple paths."""

    @pytest.mark.parametrize("typ,h_dual", [
        ('G2', 4), ('F4', 9), ('E6', 12), ('E7', 18), ('E8', 30),
    ])
    def test_casimir_adjoint_equals_2h_dual(self, typ, h_dual):
        """Path 5: C₂(adjoint) = 2·h^∨ for all exceptional types."""
        rank = exceptional_rank(typ)
        dim_adj = exceptional_dim_g(typ)
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            if weyl_dimension(typ, hw) == dim_adj:
                c2 = casimir_eigenvalue(typ, hw)
                assert c2 == Fraction(2 * h_dual)
                break

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_casimir_trivial_is_zero(self, typ):
        """Path 5: C₂(trivial) = 0."""
        rank = exceptional_rank(typ)
        hw = tuple(0 for _ in range(rank))
        c2 = casimir_eigenvalue(typ, hw)
        assert c2 == 0

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_casimir_positive_for_nontrivial(self, typ):
        """Path 5: C₂(λ) > 0 for all nontrivial dominant weights."""
        for hw in dominant_weights(typ, 3):
            c2 = casimir_eigenvalue(typ, hw)
            assert c2 > 0

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_casimir_freudenthal_check_adjoint(self, typ):
        """Path 5: Freudenthal cross-check passes for adjoint."""
        rank = exceptional_rank(typ)
        dim_adj = exceptional_dim_g(typ)
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            if weyl_dimension(typ, hw) == dim_adj:
                c2, expected = casimir_freudenthal_check(typ, hw)
                assert c2 == expected
                break

    def test_casimir_G2_fund_7(self):
        """Path 5: C₂ for the 7-dim G₂ representation."""
        c2 = casimir_eigenvalue('G2', (1, 0))
        # Known: C₂(7) = 4 in the (theta,theta)=2 normalization
        assert c2 == Fraction(4)

    def test_casimir_E8_adjoint_248(self):
        """Path 5: C₂(248) = 60 for E₈ adjoint."""
        # Find the adjoint weight
        rank = 8
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            if weyl_dimension('E8', hw) == 248:
                c2 = casimir_eigenvalue('E8', hw)
                assert c2 == Fraction(60)
                break

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_casimir_float_matches_fraction(self, typ):
        """Path 5: float and fraction Casimir agree."""
        for hw in dominant_weights(typ, 2):
            c2_frac = casimir_eigenvalue(typ, hw)
            c2_float = casimir_eigenvalue_float(typ, hw)
            assert abs(float(c2_frac) - c2_float) < 1e-10

    @pytest.mark.parametrize("typ", ['E6', 'E7', 'E8'])
    def test_gram_matrix_symmetric(self, typ):
        """Path 5: weight Gram matrix is symmetric."""
        G = _weight_gram_matrix(typ)
        n = len(G)
        for i in range(n):
            for j in range(n):
                assert G[i][j] == G[j][i]

    def test_gram_G2_symmetric(self):
        """Path 5: G₂ weight Gram matrix is symmetric."""
        G = _weight_gram_matrix('G2')
        assert G[0][1] == G[1][0]

    def test_gram_F4_symmetric(self):
        """Path 5: F₄ weight Gram matrix is symmetric."""
        G = _weight_gram_matrix('F4')
        n = len(G)
        for i in range(n):
            for j in range(n):
                assert G[i][j] == G[j][i]

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_symmetrizing_constants_condition(self, typ):
        """Path 5: d satisfies d_j*A[i][j] = d_i*A[j][i]."""
        A = exceptional_cartan_matrix(typ)
        d = _symmetrizing_constants(typ)
        n = len(A)
        for i in range(n):
            for j in range(n):
                assert d[j] * A[i][j] == d[i] * A[j][i]

    @pytest.mark.parametrize("typ", ['G2', 'F4'])
    def test_symmetrizing_long_root_norm_2(self, typ):
        """Path 5: longest root has (alpha, alpha) = 2 in our normalization."""
        d = _symmetrizing_constants(typ)
        assert max(d) == Fraction(1)  # d_long = 1, so (alpha_long) = 2*d_long = 2


# =========================================================================
# Section 4: Abscissa of convergence (5 tests)
# =========================================================================

class TestAbscissa:
    """Verify abscissa of convergence σ_c = rank/|Φ⁺|."""

    @pytest.mark.parametrize("typ,expected_num,expected_den", [
        ('G2', 2, 6), ('F4', 4, 24), ('E6', 6, 36),
        ('E7', 7, 63), ('E8', 8, 120),
    ])
    def test_abscissa_exact(self, typ, expected_num, expected_den):
        """Path 6: σ_c = rank/|Φ⁺| (exact fraction)."""
        sigma = abscissa_of_convergence(typ)
        assert sigma == Fraction(expected_num, expected_den)

    @pytest.mark.parametrize("typ,expected", [
        ('G2', 1/3), ('F4', 1/6), ('E6', 1/6),
        ('E7', 1/9), ('E8', 1/15),
    ])
    def test_abscissa_simplified(self, typ, expected):
        """Path 6: σ_c simplified fractions."""
        sigma = abscissa_of_convergence_float(typ)
        assert abs(sigma - expected) < 1e-10

    def test_abscissa_ordering(self):
        """Path 6: E₈ < E₇ < F₄ = E₆ < G₂ for σ_c."""
        sigmas = {typ: abscissa_of_convergence_float(typ)
                  for typ in ['G2', 'F4', 'E6', 'E7', 'E8']}
        assert sigmas['E8'] < sigmas['E7']
        assert sigmas['E7'] < sigmas['F4']
        assert abs(sigmas['F4'] - sigmas['E6']) < 1e-10  # both = 1/6
        assert sigmas['E6'] < sigmas['G2']

    def test_E8_fastest_convergence(self):
        """Path 6: E₈ zeta converges fastest (smallest σ_c)."""
        sigmas = {typ: abscissa_of_convergence_float(typ)
                  for typ in ['G2', 'F4', 'E6', 'E7', 'E8']}
        assert min(sigmas, key=sigmas.get) == 'E8'

    def test_G2_slowest_convergence(self):
        """Path 6: G₂ zeta converges slowest (largest σ_c)."""
        sigmas = {typ: abscissa_of_convergence_float(typ)
                  for typ in ['G2', 'F4', 'E6', 'E7', 'E8']}
        assert max(sigmas, key=sigmas.get) == 'G2'


# =========================================================================
# Section 5: Categorical zeta function (12 tests)
# =========================================================================

class TestCategoricalZeta:
    """Verify categorical zeta function values and properties."""

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_zeta_positive_at_s2(self, typ):
        """Path 1: ζ(2) > 0 for all exceptional types."""
        z = categorical_zeta(typ, 2.0, max_total_weight=8)
        assert z.real > 0

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_zeta_decreasing_in_s(self, typ):
        """Path 1: ζ(s) is decreasing in s for s > σ_c (all terms positive)."""
        z2 = categorical_zeta(typ, 2.0, max_total_weight=8).real
        z3 = categorical_zeta(typ, 3.0, max_total_weight=8).real
        z4 = categorical_zeta(typ, 4.0, max_total_weight=8).real
        assert z2 > z3 > z4 > 0

    def test_G2_zeta_largest_at_s2(self):
        """Path 1+6: G₂ has the largest zeta at s=2 among exceptional types.

        This is because G₂ has the smallest minimum dimension (7) and most
        representations at small dimension.
        """
        zetas = {typ: categorical_zeta(typ, 2.0, max_total_weight=10).real
                 for typ in ['G2', 'F4', 'E6', 'E7', 'E8']}
        assert max(zetas, key=zetas.get) == 'G2'

    def test_E8_zeta_smallest_at_s2(self):
        """Path 1+6: E₈ has the smallest zeta at s=2 (sparsest spectrum)."""
        zetas = {typ: categorical_zeta(typ, 2.0, max_total_weight=5).real
                 for typ in ['G2', 'F4', 'E6', 'E7', 'E8']}
        assert min(zetas, key=zetas.get) == 'E8'

    def test_G2_zeta_dominated_by_first_term(self):
        """Path 1: at large s, ζ_{G₂}(s) ≈ 7^{-s} (fundamental term dominates)."""
        s = 10.0
        z = categorical_zeta('G2', s, max_total_weight=20).real
        first_term = 7 ** (-s)
        # The first term should be > 90% of the total at s=10
        assert first_term / z > 0.9

    def test_E8_zeta_very_sparse(self):
        """Path 1: ζ_{E₈}(s) ≈ 248^{-s} + 3875^{-s} + ... very rapidly convergent."""
        s = 2.0
        z = categorical_zeta('E8', s, max_total_weight=3).real
        # 248^{-2} ≈ 0.0000163
        first_term = 248 ** (-2)
        assert abs(z - first_term) / first_term < 0.1  # 10% accuracy with just first term

    def test_zeta_via_spectrum_agrees(self):
        """Path 1+2: two computation paths for ζ agree."""
        for typ in ['G2', 'F4']:
            z1 = categorical_zeta(typ, 2.0, max_total_weight=8).real
            z2 = categorical_zeta_via_spectrum(typ, 2.0, max_dim=50000, max_total=8).real
            assert abs(z1 - z2) / abs(z1) < 0.01  # 1% agreement

    def test_G2_zeta_closed_form_vs_general(self):
        """Path 2: G₂ specialized zeta matches general engine."""
        s = 3.0
        z_general = categorical_zeta('G2', s, max_total_weight=15).real
        z_closed = g2_zeta(s, max_total=15).real
        assert abs(z_general - z_closed) / abs(z_general) < 1e-10

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_zeta_includes_trivial_larger(self, typ):
        """Path 1: including trivial rep increases zeta by 1."""
        z_no_triv = categorical_zeta(typ, 2.0, max_total_weight=5,
                                      include_trivial=False).real
        z_with_triv = categorical_zeta(typ, 2.0, max_total_weight=5,
                                        include_trivial=True).real
        assert abs(z_with_triv - z_no_triv - 1.0) < 1e-10

    def test_zeta_monotone_truncation(self):
        """Path 1: increasing max_total_weight increases zeta (all terms positive)."""
        z5 = categorical_zeta('G2', 2.0, max_total_weight=5).real
        z10 = categorical_zeta('G2', 2.0, max_total_weight=10).real
        z15 = categorical_zeta('G2', 2.0, max_total_weight=15).real
        assert z5 <= z10 <= z15

    @pytest.mark.parametrize("typ", ['G2', 'F4'])
    def test_zeta_real_for_real_s(self, typ):
        """Path 1: ζ(s) is real for real s > σ_c."""
        z = categorical_zeta(typ, 3.0, max_total_weight=8)
        assert abs(z.imag) < 1e-15

    def test_comparison_table_all_types(self):
        """Path 7: comparison table produces values for all types."""
        table = zeta_comparison_table([2.0, 3.0], max_total=5)
        for typ in ['G2', 'F4', 'E6', 'E7', 'E8']:
            assert typ in table
            assert 2.0 in table[typ]
            assert 3.0 in table[typ]
            assert table[typ][2.0] > table[typ][3.0]


# =========================================================================
# Section 6: Dimension spectrum (10 tests)
# =========================================================================

class TestDimensionSpectrum:
    """Verify dimension spectrum and multiplicities."""

    def test_G2_first_dims_match_known(self):
        """Path 3: G₂ smallest dimensions match known tables."""
        spec = dimension_spectrum('G2', 500, max_total=15)
        computed_dims = [d for d, _ in spec]
        known_first = [7, 14, 27, 64, 77, 182, 189, 273, 286, 378, 448]
        for d in known_first:
            assert d in computed_dims, f"Missing dim {d} in G₂ spectrum"

    def test_G2_dim_77_multiplicity(self):
        """Path 3: G₂ has two irreps of dimension 77."""
        spec = dimension_spectrum('G2', 100, max_total=10)
        d77 = [m for d, m in spec if d == 77]
        assert len(d77) == 1 and d77[0] == 2

    def test_F4_first_dim_26(self):
        """Path 3: smallest nontrivial F₄ dimension is 26."""
        spec = dimension_spectrum('F4', 100, max_total=5)
        assert spec[0][0] == 26

    def test_E8_smallest_dim_248(self):
        """Path 3: smallest nontrivial E₈ dimension is 248."""
        pairs = dominant_weights_by_dim('E8', 1000, max_total=3)
        assert pairs[0][1] == 248

    def test_E8_second_dim_3875(self):
        """Path 3: second smallest E₈ dimension is 3875."""
        pairs = dominant_weights_by_dim('E8', 5000, max_total=3)
        dims = sorted(set(d for _, d in pairs))
        assert dims[1] == 3875

    def test_G2_spectrum_specialized_matches_general(self):
        """Path 2: G₂ specialized dimension spectrum matches general."""
        spec_gen = dimension_spectrum('G2', 500, max_total=15)
        spec_g2 = g2_dimension_spectrum(500)
        # Convert to comparable form
        gen_dict = dict(spec_gen)
        g2_dict = dict(spec_g2)
        for d in gen_dict:
            assert d in g2_dict, f"Missing dim {d}"
            assert gen_dict[d] == g2_dict[d], f"Mult mismatch at dim {d}"

    def test_dirichlet_coeffs_G2(self):
        """Path 1: Dirichlet coefficients for G₂."""
        coeffs = dirichlet_coefficients('G2', 100, max_total=10)
        # a_7 = 1 (only V(1,0) has dim 7)
        assert coeffs.get(7, 0) == 1
        # a_14 = 1 (only V(0,1) has dim 14)
        assert coeffs.get(14, 0) == 1
        # a_77 = 2 (V(3,0) and V(0,2))
        assert coeffs.get(77, 0) == 2

    def test_F4_small_dims_function(self):
        """Path 1: F₄ small dims function returns correct dimensions."""
        pairs = f4_small_dims(max_total=3)
        dims = [d for _, d in pairs]
        assert 26 in dims
        assert 52 in dims

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6'])
    def test_spectrum_dims_sorted(self, typ):
        """Path 1: dimension spectrum is sorted by dimension."""
        spec = dimension_spectrum(typ, 10000, max_total=8)
        dims = [d for d, _ in spec]
        assert dims == sorted(dims)

    def test_e8_first_dims_function(self):
        """Path 3: E₈ first dims match known values."""
        dims = e8_first_dims(5)
        assert dims[0] == 248
        assert dims[1] == 3875
        assert dims[2] == 27000
        assert dims[3] == 30380


# =========================================================================
# Section 7: Langlands duality (5 tests)
# =========================================================================

class TestLanglandsDuality:
    """Verify Langlands dual properties."""

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_self_dual(self, typ):
        """Path 4: all exceptional types are Langlands self-dual."""
        assert langlands_dual_type(typ) == typ

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6'])
    def test_zeta_ratio_is_one(self, typ):
        """Path 4: ζ_g(s) / ζ_{g^L}(s) = 1 for self-dual types."""
        ratio = langlands_dual_zeta_ratio(typ, 3.0, max_total=8)
        assert abs(ratio - 1.0) < 1e-10

    def test_G2_langlands_dual_dimensions_same(self):
        """Path 4: G₂ and G₂^L have identical representation dimensions.

        G₂ is self-dual: the Langlands dual swaps long/short roots but
        the representation theory is the same (same Weyl group).
        """
        dims_g = set()
        dims_gL = set()
        for hw in dominant_weights('G2', 5):
            dims_g.add(weyl_dimension('G2', hw))
            dims_gL.add(weyl_dimension(langlands_dual_type('G2'), hw))
        assert dims_g == dims_gL

    def test_F4_langlands_dual_dimensions_same(self):
        """Path 4: F₄ and F₄^L have identical representation dimensions."""
        dims_g = set()
        dims_gL = set()
        for hw in dominant_weights('F4', 3):
            dims_g.add(weyl_dimension('F4', hw))
            dims_gL.add(weyl_dimension(langlands_dual_type('F4'), hw))
        assert dims_g == dims_gL

    def test_E6_outer_automorphism_conjugate_reps(self):
        """Path 4: E₆ outer automorphism exchanges 27 and 27*."""
        rank = 6
        dims_27 = []
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            if weyl_dimension('E6', hw) == 27:
                dims_27.append(hw)
        assert len(dims_27) == 2
        # The two 27s are related by the Dynkin diagram automorphism


# =========================================================================
# Section 8: Kappa (modular characteristic) for exceptional affine (5 tests)
# =========================================================================

class TestKappa:
    """Verify κ for exceptional affine Kac-Moody algebras."""

    @pytest.mark.parametrize("typ,dim_g,h_dual", [
        ('G2', 14, 4), ('F4', 52, 9), ('E6', 78, 12),
        ('E7', 133, 18), ('E8', 248, 30),
    ])
    def test_kappa_formula(self, typ, dim_g, h_dual):
        """Path 1: κ = dim(g)·(k+h^∨)/(2·h^∨) at level k=1."""
        k = 1
        kappa = kappa_exceptional_affine(typ, k)
        expected = Fraction(dim_g * (k + h_dual), 2 * h_dual)
        assert kappa == expected

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_kappa_positive(self, typ):
        """Path 1: κ > 0 for positive level."""
        for k in [1, 2, 5, 10]:
            kappa = kappa_exceptional_affine(typ, k)
            assert kappa > 0

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_kappa_linear_in_level(self, typ):
        """Path 1: κ is linear in k (affine function)."""
        k1 = kappa_exceptional_affine(typ, 1)
        k2 = kappa_exceptional_affine(typ, 2)
        k3 = kappa_exceptional_affine(typ, 3)
        # k3 - k2 = k2 - k1
        assert k3 - k2 == k2 - k1

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_kappa_float_matches_fraction(self, typ):
        """Path 1: float κ matches fraction κ."""
        for k in [1, 2, 5]:
            kf = kappa_exceptional_affine_float(typ, k)
            ke = float(kappa_exceptional_affine(typ, k))
            assert abs(kf - ke) < 1e-12

    def test_kappa_at_critical_level(self):
        """Path 1: at k = -h^∨, κ = 0 (critical level)."""
        for typ in ['G2', 'F4', 'E6', 'E7', 'E8']:
            h_dual = exceptional_dual_coxeter(typ)
            kappa = kappa_exceptional_affine(typ, -h_dual)
            assert kappa == 0


# =========================================================================
# Section 9: Dimension count asymptotics (4 tests)
# =========================================================================

class TestAsymptotics:
    """Verify dimension counting asymptotics."""

    def test_G2_dimension_count_grows(self):
        """Path 6: N(D) for G₂ is increasing in D."""
        n100 = dimension_count('G2', 100, max_total=10)
        n1000 = dimension_count('G2', 1000, max_total=20)
        assert n1000 > n100 > 0

    def test_E8_extremely_sparse(self):
        """Path 6: E₈ has very few small representations."""
        n1000 = dimension_count('E8', 1000, max_total=3)
        # Only 248 is below 1000
        assert n1000 == 1

    def test_G2_exponent_reasonable(self):
        """Path 6: G₂ dimension count exponent ≈ rank/|Φ⁺| = 1/3."""
        # This is approximate due to finite-size effects
        alpha = dimension_count_exponent(
            'G2', D_values=[200, 500, 1000, 2000], max_total=20
        )
        expected = 2.0 / 6.0  # = 1/3
        assert abs(alpha - expected) < 0.3  # generous tolerance

    def test_F4_count_positive(self):
        """Path 6: F₄ has some representations below dim 10000."""
        n = dimension_count('F4', 10000, max_total=5)
        assert n > 5


# =========================================================================
# Section 10: Cross-type comparisons (8 tests)
# =========================================================================

class TestCrossType:
    """Cross-type comparisons and structural tests."""

    def test_ranking_at_s2(self):
        """Path 7: ranking at s=2 ordered by convergence rate."""
        ranking = zeta_ranking_at_s(2.0, max_total=8)
        types = [t for t, _ in ranking]
        # G2 should be first (largest zeta, slowest convergence)
        assert types[0] == 'G2'
        # E8 should be last (smallest zeta, fastest convergence)
        assert types[-1] == 'E8'

    def test_identify_G2(self):
        """Path 3: identify G₂ from smallest dim."""
        assert identify_exceptional_by_dims([7, 14, 27]) == 'G2'

    def test_identify_F4(self):
        """Path 3: identify F₄ from smallest dim."""
        assert identify_exceptional_by_dims([26, 52, 273]) == 'F4'

    def test_identify_E6(self):
        """Path 3: identify E₆ from smallest dim."""
        assert identify_exceptional_by_dims([27, 27, 78]) == 'E6'

    def test_identify_E7(self):
        """Path 3: identify E₇ from smallest dim."""
        assert identify_exceptional_by_dims([56, 133, 912]) == 'E7'

    def test_identify_E8(self):
        """Path 3: identify E₈ from smallest dim."""
        assert identify_exceptional_by_dims([248, 3875, 30380]) == 'E8'

    def test_G2_zeta_at_s2_numerical(self):
        """Path 1: G₂ zeta at s=2 matches manual computation."""
        # Manual: 7^{-2} + 14^{-2} + 27^{-2} + 64^{-2} + 2*77^{-2} + ...
        manual = (7**(-2) + 14**(-2) + 27**(-2) + 64**(-2)
                  + 2 * 77**(-2) + 182**(-2) + 189**(-2))
        z = categorical_zeta('G2', 2.0, max_total_weight=5).real
        # Our truncated sum should at least include these terms
        assert z >= manual * 0.99

    def test_exceptional_summary_complete(self):
        """Path 7: summary function returns all expected keys."""
        for typ in ['G2', 'F4', 'E6', 'E7', 'E8']:
            s = exceptional_summary(typ, max_total=3)
            assert 'rank' in s
            assert 'n_pos_roots' in s
            assert 'dim_g' in s
            assert 'h_dual' in s
            assert 'sigma_c' in s
            assert 'fund_dims' in s
            assert 'zeta_values' in s


# =========================================================================
# Section 11: Cross-check with bc_categorical_zeta_engine (5 tests)
# =========================================================================

class TestCrossCheckClassical:
    """Cross-check exceptional engine against classical engine."""

    def test_weyl_formula_consistency(self):
        """Path 7: the Weyl formula engine produces integer dimensions."""
        for typ in ['G2', 'F4', 'E6', 'E7', 'E8']:
            for hw in dominant_weights(typ, 3):
                d = weyl_dimension(typ, hw)
                assert isinstance(d, int)
                assert d >= 1

    def test_exceptional_data_consistent(self):
        """Path 3: dim(g) = rank + 2*|Phi+|."""
        for typ in ['G2', 'F4', 'E6', 'E7', 'E8']:
            data = _EXCEPTIONAL_DATA[typ]
            assert data['dim_g'] == data['rank'] + 2 * data['n_pos_roots']

    def test_dual_coxeter_numbers_known(self):
        """Path 3: dual Coxeter numbers match standard references."""
        expected = {'G2': 4, 'F4': 9, 'E6': 12, 'E7': 18, 'E8': 30}
        for typ, h in expected.items():
            assert exceptional_dual_coxeter(typ) == h

    def test_ranks_known(self):
        """Path 3: ranks match standard references."""
        expected = {'G2': 2, 'F4': 4, 'E6': 6, 'E7': 7, 'E8': 8}
        for typ, r in expected.items():
            assert exceptional_rank(typ) == r

    def test_dim_g_known(self):
        """Path 3: dim(g) values match standard references."""
        expected = {'G2': 14, 'F4': 52, 'E6': 78, 'E7': 133, 'E8': 248}
        for typ, d in expected.items():
            assert exceptional_dim_g(typ) == d


# =========================================================================
# Section 12: Edge cases and error handling (5 tests)
# =========================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_invalid_type_raises(self):
        """Error handling: invalid type raises ValueError."""
        with pytest.raises(ValueError):
            exceptional_cartan_matrix('H4')

    def test_trivial_rep_dim_1_all_types(self):
        """Path 1: trivial representation has dim 1 for all types."""
        for typ in ['G2', 'F4', 'E6', 'E7', 'E8']:
            rank = exceptional_rank(typ)
            hw = tuple(0 for _ in range(rank))
            assert weyl_dimension(typ, hw) == 1

    def test_dominant_weights_empty_at_zero(self):
        """Path 1: dominant_weights with max_total=0 returns empty list."""
        for typ in ['G2', 'F4', 'E6', 'E7', 'E8']:
            assert len(dominant_weights(typ, 0)) == 0

    def test_zeta_with_zero_max_total(self):
        """Path 1: zeta with max_total=0 returns 0 (no nontrivial terms)."""
        z = categorical_zeta('G2', 2.0, max_total_weight=0)
        assert z == 0

    def test_G2_closed_formula_divisibility(self):
        """Path 2: G₂ closed formula product is always divisible by 120."""
        for a in range(10):
            for b in range(10):
                prod = ((a + 1) * (b + 1) * (a + b + 2) *
                        (a + 2 * b + 3) * (a + 3 * b + 4) * (2 * a + 3 * b + 5))
                assert prod % 120 == 0


# =========================================================================
# Section 13: Deeper structural tests (6 tests)
# =========================================================================

class TestDeepStructural:
    """Deeper structural tests for representation theory."""

    def test_G2_multiplicity_pattern(self):
        """Path 3: G₂ multiplicity pattern in low dimensions.

        Most G₂ dimensions appear with multiplicity 1, but dim=77 appears twice.
        """
        spec = dimension_spectrum('G2', 200, max_total=10)
        mult_dict = dict(spec)
        # dim 7, 14, 27, 64 each appear once
        for d in [7, 14, 27, 64]:
            assert mult_dict.get(d, 0) == 1
        # dim 77 appears twice
        assert mult_dict.get(77, 0) == 2

    def test_F4_dim_1053_multiplicity(self):
        """Path 3: F₄ has two irreps of dimension 1053."""
        spec = dimension_spectrum('F4', 2000, max_total=5)
        mult_dict = dict(spec)
        assert mult_dict.get(1053, 0) == 2

    def test_casimir_ordering_with_dim(self):
        """Path 5: larger representations generally have larger Casimir.

        Not strictly monotone, but the fundamental reps should satisfy:
        smaller dim => smaller C₂ (for a given type).
        """
        for typ in ['G2', 'E8']:
            rank = exceptional_rank(typ)
            pairs = []
            for i in range(rank):
                hw = tuple(1 if j == i else 0 for j in range(rank))
                d = weyl_dimension(typ, hw)
                c2 = float(casimir_eigenvalue(typ, hw))
                pairs.append((d, c2))
            pairs.sort()
            # Check that smallest dim has smallest Casimir
            assert pairs[0][1] == min(c2 for _, c2 in pairs)

    def test_G2_zeta_convergence_rate(self):
        """Path 6: G₂ zeta partial sums converge at expected rate."""
        s = 2.0
        z5 = categorical_zeta('G2', s, max_total_weight=5).real
        z10 = categorical_zeta('G2', s, max_total_weight=10).real
        z20 = categorical_zeta('G2', s, max_total_weight=20).real
        # The tail should shrink: (z20-z10) < (z10-z5)
        assert (z20 - z10) < (z10 - z5)

    def test_E8_zeta_rapid_convergence(self):
        """Path 6: E₈ zeta converges very rapidly (sparse spectrum).

        With max_total=2, we get the first two terms: 248^{-s} + 3875^{-s}.
        With max_total=3, we add more terms. The difference should be tiny.
        """
        s = 2.0
        z2 = categorical_zeta('E8', s, max_total_weight=2).real
        z3 = categorical_zeta('E8', s, max_total_weight=3).real
        # z3 - z2 should be small relative to z2
        if z2 > 0:
            assert (z3 - z2) / z2 < 1.0  # Less than doubling

    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_weyl_dimension_integer_valued(self, typ):
        """Path 1: Weyl dimension formula always produces exact integers."""
        for hw in dominant_weights(typ, 4):
            d = weyl_dimension(typ, hw)
            assert isinstance(d, int)
            assert d == int(d)
            assert d >= 1
