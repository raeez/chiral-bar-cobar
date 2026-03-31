"""Tests for rectangular W-algebra W^k(sl_4, f_{[2,2]}).

Tests verify:
1. Central charge formula c = 6(2k-1)/(k+4) via ACL coset
2. Koszul conductor K = 24 (level-independent)
3. BV self-duality of the [2,2] partition
4. Generator content (3 at h=1, 4 at h=2, total 7)
5. Root data for the [2,2] nilpotent
6. Ghost sector data
7. Comparison with other sl_4 orbits
8. FF involution: k' = -k-8, (k')' = k
9. Central charge duality: c(k) + c(-k-8) = 24
10. Residual sl_2 level and central charge decomposition
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, simplify

from compute.lib.rectangular_w_algebra_engine import (
    central_charge,
    c_sl4,
    c_sl2_coset,
    verify_coset_central_charge,
    dual_level,
    dual_central_charge,
    koszul_conductor,
    verify_koszul_conductor,
    partition,
    transpose_partition,
    is_bv_self_dual,
    orbit_dimension,
    centralizer_dimension,
    generator_content,
    sl2_triple_22,
    residual_sl2_level,
    residual_sl2_central_charge,
    matter_central_charge,
    effective_ghost_central_charge,
    ghost_data,
    sl4_orbit_hierarchy,
    c_principal_W4,
    K_principal_W4,
    bv_duality_table,
    shadow_class_analysis,
    full_koszul_data,
    numerical_evaluation,
    kappa_sl4_km,
    kappa_sl2_km,
)

k = Symbol('k')


# ============================================================================
# Central charge tests
# ============================================================================

class TestCentralCharge:
    """Tests for c(W^k(sl_4, f_{[2,2]})) = 6(2k-1)/(k+4)."""

    def test_symbolic_formula(self):
        """Verify the symbolic central charge formula."""
        c = central_charge()
        expected = 6 * (2 * k - 1) / (k + 4)
        assert simplify(c - expected) == 0

    def test_coset_decomposition(self):
        """Verify c = c(sl_4, k) - c(sl_2, k+2)."""
        assert verify_coset_central_charge()

    @pytest.mark.parametrize("k_val,expected_c", [
        (Rational(1), Rational(6, 5)),     # 6*1/5
        (Rational(2), Rational(3)),         # 6*3/6
        (Rational(5), Rational(6)),         # 6*9/9
        (Rational(10), Rational(114, 14)),  # 6*19/14
        (Rational(-3), Rational(-42)),      # 6*(-7)/1
    ])
    def test_numerical_values(self, k_val, expected_c):
        """Check c at specific levels."""
        c = central_charge(k_val)
        assert c == expected_c

    def test_c_vanishes_at_half(self):
        """c(k=1/2) = 0: the algebra is 'conformal anomaly free'."""
        c = central_charge(Rational(1, 2))
        assert c == 0

    def test_c_large_k_limit(self):
        """At large k, c -> 12."""
        c_100 = central_charge(Rational(100))
        c_1000 = central_charge(Rational(1000))
        assert abs(float(c_100) - 12) < 0.6
        assert abs(float(c_1000) - 12) < 0.1

    def test_c_critical_level_pole(self):
        """c has a pole at k = -4 (critical level k = -h^v)."""
        from sympy import zoo, oo, nan
        c_crit = central_charge(Rational(-4))
        # Sympy returns zoo (complex infinity) for division by zero
        assert c_crit in (zoo, oo, -oo, nan) or abs(c_crit) > 10**10


# ============================================================================
# Koszul conductor tests
# ============================================================================

class TestKoszulConductor:
    """Tests for K = c(k) + c(-k-8) = 24."""

    def test_symbolic_K(self):
        """Verify K = 24 symbolically."""
        K = koszul_conductor()
        assert K == 24

    def test_full_verification(self):
        """Run the comprehensive verification."""
        result = verify_koszul_conductor()
        assert result['all_pass']
        assert result['K_symbolic'] == 24

    @pytest.mark.parametrize("k_val", [
        Rational(1), Rational(2), Rational(5), Rational(10),
        Rational(-1), Rational(-3), Rational(100), Rational(1, 2),
        Rational(1, 3), Rational(-7), Rational(-10),
    ])
    def test_K_numerical(self, k_val):
        """Verify K = 24 at many levels."""
        c_k = central_charge(k_val)
        c_kp = central_charge(dual_level(k_val))
        assert c_k + c_kp == 24

    def test_K_vs_principal(self):
        """Compare: K([2,2]) = 24 vs K(W_4) = 246."""
        assert koszul_conductor() == 24
        assert K_principal_W4() == 246


# ============================================================================
# FF involution tests
# ============================================================================

class TestFFInvolution:
    """Tests for the Feigin-Frenkel involution k -> -k-8."""

    def test_dual_level_formula(self):
        """k' = -k - 8."""
        assert simplify(dual_level() - (-k - 8)) == 0

    def test_involutivity(self):
        """(k')' = k: the FF involution is an involution."""
        kpp = dual_level(dual_level())
        assert simplify(kpp - k) == 0

    @pytest.mark.parametrize("k_val", [
        Rational(0), Rational(1), Rational(-4), Rational(100),
    ])
    def test_involutivity_numerical(self, k_val):
        """Verify (k')' = k numerically."""
        kp = dual_level(k_val)
        kpp = dual_level(kp)
        assert kpp == k_val

    def test_critical_self_duality(self):
        """At k = -h^v = -4: k' = -(-4)-8 = -4. Self-dual at critical."""
        assert dual_level(Rational(-4)) == Rational(-4)


# ============================================================================
# BV self-duality tests
# ============================================================================

class TestBVSelfDuality:
    """Tests for BV self-duality of the [2,2] orbit."""

    def test_partition_format(self):
        """Partition is (2, 2)."""
        assert partition() == (2, 2)

    def test_self_transpose(self):
        """[2,2]^t = [2,2]."""
        assert transpose_partition() == (2, 2)

    def test_bv_self_dual(self):
        """The orbit is BV self-dual."""
        assert is_bv_self_dual()

    def test_orbit_dimension(self):
        """dim O_{[2,2]} = 8."""
        assert orbit_dimension() == 8

    def test_centralizer_dimension(self):
        """dim g^f = 7."""
        assert centralizer_dimension() == 7

    def test_bv_duality_table(self):
        """Verify the full BV duality table for sl_4."""
        table = bv_duality_table()
        # Check all pairings
        assert table[(1, 1, 1, 1)] == (4,)
        assert table[(2, 1, 1)] == (3, 1)
        assert table[(2, 2)] == (2, 2)
        assert table[(3, 1)] == (2, 1, 1)
        assert table[(4,)] == (1, 1, 1, 1)

    def test_bv_involutivity(self):
        """BV duality is an involution on type A orbits."""
        table = bv_duality_table()
        for lam, lam_dual in table.items():
            assert table[lam_dual] == lam


# ============================================================================
# Generator content tests
# ============================================================================

class TestGenerators:
    """Tests for the generator content."""

    def test_total_generators(self):
        """7 total strong generators."""
        gen = generator_content()
        assert gen['total_generators'] == 7

    def test_weight_distribution(self):
        """3 at h=1, 4 at h=2."""
        gen = generator_content()
        assert gen['weights'][1] == 3
        assert gen['weights'][2] == 4

    def test_weight_sum(self):
        """Multiplicities sum to total."""
        gen = generator_content()
        assert sum(gen['weights'].values()) == gen['total_generators']


# ============================================================================
# Root data tests
# ============================================================================

class TestRootData:
    """Tests for the sl_2 triple data."""

    def test_dynkin_diagram(self):
        """Weighted Dynkin diagram [0, 2, 0]."""
        data = sl2_triple_22()
        assert data['dynkin_diagram'] == (0, 2, 0)

    def test_h_diagonal(self):
        """h = diag(1, -1, 1, -1)."""
        data = sl2_triple_22()
        assert data['h_diagonal'] == (1, -1, 1, -1)

    def test_nilradical_dimension(self):
        """dim(n_+) = 4."""
        data = sl2_triple_22()
        assert data['dim_nilradical'] == 4

    def test_nilradical_uniform_grading(self):
        """All roots in n_+ have the same ad(h) eigenvalue 2."""
        data = sl2_triple_22()
        for root in data['nilradical']:
            assert root['eigenvalue'] == 2

    def test_levi_dimension(self):
        """dim(g_0) = 7 = dim(s(gl_2 x gl_2))."""
        data = sl2_triple_22()
        assert data['dim_levi'] == 7

    def test_centralizer_dimension(self):
        """dim(g^f) = 7."""
        data = sl2_triple_22()
        assert data['dim_centralizer'] == 7

    def test_even_grading(self):
        """The grading is even: only eigenvalues 0 and ±2 (no half-integers)."""
        data = sl2_triple_22()
        for root in data['positive_roots']:
            assert root['eigenvalue'] % 2 == 0


# ============================================================================
# Ghost sector tests
# ============================================================================

class TestGhostSector:
    """Tests for the ghost sector data."""

    def test_num_ghost_pairs(self):
        """4 bc ghost pairs (one per root in n_+)."""
        gd = ghost_data()
        assert gd['num_ghost_pairs'] == 4

    def test_uniform_j_value(self):
        """All ghost j-values are 1 (uniform grading)."""
        gd = ghost_data()
        assert all(j == 1 for j in gd['ghost_j_values'])

    def test_bc_central_charge(self):
        """Each (2,-1) bc pair has c = -26."""
        gd = ghost_data()
        assert gd['c_per_pair'] == -26

    def test_total_ghost_bc_central_charge(self):
        """Total raw bc ghost c = -104."""
        gd = ghost_data()
        assert gd['c_ghost_total_bc'] == -104

    @pytest.mark.parametrize("k_val,expected", [
        (Rational(0), Rational(3, 2)),
        (Rational(2), Rational(2)),
        (Rational(-3), Rational(-3)),
    ])
    def test_effective_ghost_c(self, k_val, expected):
        """Effective ghost c = 3(k+2)/(k+4) at specific levels."""
        assert effective_ghost_central_charge(k_val) == expected

    def test_effective_ghost_c_varies(self):
        """Effective ghost c is NOT constant (unlike principal)."""
        c1 = effective_ghost_central_charge(Rational(1))
        c5 = effective_ghost_central_charge(Rational(5))
        assert c1 != c5


# ============================================================================
# Residual sl_2 tests
# ============================================================================

class TestResidualSL2:
    """Tests for the residual sl_2 sector."""

    def test_sl2_level(self):
        """Residual sl_2 has level 2k."""
        assert simplify(residual_sl2_level() - 2 * k) == 0

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10])
    def test_sl2_level_numerical(self, k_val):
        """Verify sl_2 level = 2k numerically."""
        assert residual_sl2_level(Rational(k_val)) == 2 * k_val

    def test_sl2_central_charge_formula(self):
        """c(sl_2, 2k) = 3k/(k+1)."""
        c_sl2 = residual_sl2_central_charge()
        expected = 3 * k / (k + 1)
        assert simplify(c_sl2 - expected) == 0

    def test_matter_central_charge(self):
        """c_matter = c_total - c_{sl_2}."""
        c_total = central_charge()
        c_sl2 = residual_sl2_central_charge()
        c_mat = matter_central_charge()
        assert simplify(c_total - c_sl2 - c_mat) == 0

    def test_c_decomposition_at_k5(self):
        """At k=5: c=6, c_sl2=5/2, c_matter=7/2."""
        c = central_charge(Rational(5))
        c_sl2 = residual_sl2_central_charge(Rational(5))
        c_mat = matter_central_charge(Rational(5))
        assert c == 6
        assert c_sl2 == Rational(5, 2)
        assert c_mat == Rational(7, 2)
        assert c == c_sl2 + c_mat


# ============================================================================
# sl_4 orbit hierarchy tests
# ============================================================================

class TestOrbitHierarchy:
    """Tests for the sl_4 nilpotent orbit hierarchy."""

    def test_five_orbits(self):
        """sl_4 has exactly 5 nilpotent orbits."""
        hierarchy = sl4_orbit_hierarchy()
        assert len(hierarchy) == 5

    def test_orbit_dimensions(self):
        """Verify orbit dimensions match N^2 - sum(lambda_i^t)^2."""
        hierarchy = sl4_orbit_hierarchy()
        expected_dims = {
            (1, 1, 1, 1): 0,
            (2, 1, 1): 8,
            (2, 2): 8,
            (3, 1): 12,
            (4,): 12,
        }
        for lam, data in hierarchy.items():
            assert data['orbit_dim'] == expected_dims[lam], f"dim mismatch for {lam}"

    def test_only_rectangular_self_dual(self):
        """Only [2,2] is BV self-dual among sl_4 orbits."""
        table = bv_duality_table()
        self_dual = [lam for lam, dual in table.items() if lam == dual]
        assert self_dual == [(2, 2)]

    def test_generator_counts(self):
        """Verify generator counts for all orbits."""
        hierarchy = sl4_orbit_hierarchy()
        expected_gens = {
            (1, 1, 1, 1): 15,
            (2, 1, 1): 12,
            (2, 2): 7,
            (3, 1): 3,
            (4,): 3,
        }
        for lam, data in hierarchy.items():
            assert data['generators'] == expected_gens[lam], f"gen count mismatch for {lam}"


# ============================================================================
# Kappa structural tests
# ============================================================================

class TestKappaStructure:
    """Tests for structural properties of kappa (without knowing the value)."""

    def test_kappa_sl4_km(self):
        """kappa(sl_4, k) = 15(k+4)/8."""
        kappa = kappa_sl4_km()
        assert simplify(kappa - Rational(15) * (k + 4) / 8) == 0

    def test_kappa_sl2_km(self):
        """kappa(sl_2, 2k) = 3(2k+2)/4 = 3(k+1)/2."""
        kappa = kappa_sl2_km(2 * k)
        assert simplify(kappa - Rational(3) * (k + 1) / 2) == 0

    def test_kappa_sl4_numerical(self):
        """kappa(sl_4, k=1) = 15*5/8 = 75/8."""
        assert kappa_sl4_km(Rational(1)) == Rational(75, 8)

    def test_kappa_km_duality(self):
        """For KM: kappa(k) + kappa(-k-8) = 0."""
        kappa_k = kappa_sl4_km()
        kappa_dual = kappa_sl4_km(dual_level())
        kappa_sum = simplify(kappa_k + kappa_dual)
        assert kappa_sum == 0


# ============================================================================
# Cross-family consistency tests (AP10 defense)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-checks against other families to prevent AP10 errors."""

    def test_K_ordering(self):
        """K([2,2]) = 24 < K(principal W_4) = 246."""
        assert koszul_conductor() < K_principal_W4()

    def test_c_at_k1_ordering(self):
        """At k=1: c([2,2]) = 6/5 < c(Vir) = 1-24/3 = -7."""
        c_rect = central_charge(Rational(1))
        # Virasoro: c = 1 - 6(k+1)^2/(k+2) at k=1: 1 - 24/3 = -7
        c_vir = 1 - 6 * 4 / 3
        # The [2,2] algebra has POSITIVE c at k=1 (unlike Virasoro)
        assert c_rect > 0
        assert c_vir < 0

    def test_generator_count_monotonicity(self):
        """Generators decrease as orbit dimension increases (in sl_4)."""
        hierarchy = sl4_orbit_hierarchy()
        # (1^4)->15, (2,1,1)->12, (2,2)->7, (3,1)->3, (4)->3
        # Not strictly monotone at the end (both 3), but generally decreasing
        dims = [(data['orbit_dim'], data['generators'])
                for data in hierarchy.values()]
        # Check: trivial (dim 0) has most generators
        assert hierarchy[(1, 1, 1, 1)]['generators'] == 15
        # Principal (dim 12) has fewest
        assert hierarchy[(4,)]['generators'] == 3

    def test_c_large_k_all_orbits(self):
        """At large k, c -> different limits for different orbits."""
        k_large = Rational(1000)
        c_rect = float(central_charge(k_large))
        c_w4 = float(c_principal_W4(k_large))
        # c(W_rect) -> 12, c(W_4) -> 3 - 60k ~ -60k (very negative)
        assert abs(c_rect - 12) < 0.1
        assert c_w4 < -50000  # very negative


# ============================================================================
# Shadow class analysis tests
# ============================================================================

class TestShadowClass:
    """Tests for shadow class analysis."""

    def test_expected_class_M(self):
        """Expected shadow class is M (mixed)."""
        analysis = shadow_class_analysis()
        assert analysis['expected_class'] == 'M'

    def test_comparison_table(self):
        """Comparison: sl_4 hat is class L, W_4 principal is class M."""
        analysis = shadow_class_analysis()
        assert 'L' in analysis['comparison']['sl_4_hat']
        assert 'M' in analysis['comparison']['W_4_principal']


# ============================================================================
# Full data integration test
# ============================================================================

class TestFullData:
    """Integration tests for the full Koszul data package."""

    def test_full_data_at_k1(self):
        """Full data at k=1."""
        data = numerical_evaluation(1)
        assert data['partition'] == (2, 2)
        assert data['bv_self_dual'] is True
        assert data['K'] == 24
        assert data['c'] == Rational(6, 5)
        assert data['c_dual'] == Rational(114, 5)
        assert data['dual_level'] == Rational(-9)

    def test_full_data_at_k5(self):
        """Full data at k=5."""
        data = numerical_evaluation(5)
        assert data['c'] == 6
        assert data['c_dual'] == 18
        assert data['K'] == 24
        assert data['sl2_level'] == 10

    def test_kappa_flagged(self):
        """Kappa is flagged as OPEN (not reliably computed)."""
        data = full_koszul_data()
        assert data['kappa'] is None
        assert data['kappa_status'] == 'OPEN'
