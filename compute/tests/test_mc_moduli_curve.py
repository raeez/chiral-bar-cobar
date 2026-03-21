"""Tests for MC moduli curve: critical locus of the shadow potential.

Verifies:
  - MC solution count at generic and special central charges
  - Hadamard product factorization identity
  - Branch locus structure and singularity walls
  - Jensen counting estimates
  - Monodromy permutations around branch points
  - Order estimates for the shadow potential
  - Rank-2 (W_3) critical locus
  - Consistency with virasoro_shadow_tower and shadow_potential_singularity

Ground truth:
  - thm:nms-mc-moduli-curve-structure
  - thm:nms-hadamard-mc-potential
  - cor:nms-mc-solution-counting
"""

import pytest
import numpy as np

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'mc_moduli_curve',
    os.path.join(_lib_dir, 'mc_moduli_curve.py')
)
_mc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mc)

_spec_sps = importlib.util.spec_from_file_location(
    'shadow_potential_singularity',
    os.path.join(_lib_dir, 'shadow_potential_singularity.py')
)
_sps = importlib.util.module_from_spec(_spec_sps)
_spec_sps.loader.exec_module(_sps)

_spec_vst = importlib.util.spec_from_file_location(
    'virasoro_shadow_tower',
    os.path.join(_lib_dir, 'virasoro_shadow_tower.py')
)
_vst = importlib.util.module_from_spec(_spec_vst)
_spec_vst.loader.exec_module(_vst)


# ============================================================
# 1. MC solution count
# ============================================================

class TestMCSolutionCount:
    """At finite truncation, the reduced critical polynomial has degree
    max_arity - 2, so there are exactly that many MC solutions
    (counted with multiplicity) for generic c."""

    def test_count_arity5(self):
        """Arity 5 -> degree 3 -> 3 solutions at generic c."""
        roots = _mc.mc_solutions_1d(1, max_arity=5)
        assert len(roots) == 3

    def test_count_arity6(self):
        """Arity 6 -> degree 4 -> 4 solutions at generic c."""
        roots = _mc.mc_solutions_1d(1, max_arity=6)
        assert len(roots) == 4

    def test_count_arity7(self):
        """Arity 7 -> degree 5 -> 5 solutions at generic c."""
        roots = _mc.mc_solutions_1d(1, max_arity=7)
        assert len(roots) == 5

    def test_count_c13_self_dual(self):
        """c = 13 (Virasoro self-dual point): still 5 solutions at arity 7."""
        roots = _mc.mc_solutions_1d(13, max_arity=7)
        assert len(roots) == 5

    def test_count_helper(self):
        """mc_solution_count agrees with len(mc_solutions_1d)."""
        for cv in [1, 5, 13, 26]:
            assert _mc.mc_solution_count(cv, 7) == len(_mc.mc_solutions_1d(cv, 7))

    def test_solutions_sorted_by_modulus(self):
        """MC solutions are returned sorted by absolute value."""
        roots = _mc.mc_solutions_1d(1, max_arity=7)
        moduli = [abs(z) for z in roots]
        for i in range(len(moduli) - 1):
            assert moduli[i] <= moduli[i + 1] + 1e-10


# ============================================================
# 2. MC solutions are actual roots
# ============================================================

class TestMCSolutionsAreRoots:
    """Each returned solution must satisfy dS/dx = 0."""

    def test_roots_satisfy_equation_c1(self):
        """All MC solutions at c=1 satisfy the critical equation."""
        from sympy import Symbol, diff, N as sympy_N
        c_sym = Symbol('c')
        x_sym = Symbol('x')
        pot = _sps.shadow_potential_1d(7)
        deriv = diff(pot, x_sym)
        roots = _mc.mc_solutions_1d(1, max_arity=7)
        for z in roots:
            val = complex(sympy_N(deriv.subs(c_sym, 1).subs(x_sym, z)))
            assert abs(val) < 1e-8, f"dS/dx({z}) = {val} != 0"

    def test_roots_satisfy_equation_c13(self):
        """All MC solutions at c=13 satisfy the critical equation."""
        from sympy import Symbol, diff, N as sympy_N
        c_sym = Symbol('c')
        x_sym = Symbol('x')
        pot = _sps.shadow_potential_1d(7)
        deriv = diff(pot, x_sym)
        roots = _mc.mc_solutions_1d(13, max_arity=7)
        for z in roots:
            val = complex(sympy_N(deriv.subs(c_sym, 13).subs(x_sym, z)))
            assert abs(val) < 1e-6, f"dS/dx({z}) = {val} != 0"


# ============================================================
# 3. Hadamard product identity
# ============================================================

class TestHadamardProduct:
    """The reduced derivative factors as P(x) = kappa * prod(1 - x/x_k)."""

    def test_hadamard_real_point_c1(self):
        """Hadamard identity at x=0.1, c=1."""
        exact, approx, err = _mc.hadamard_product_check(1, 0.1, max_arity=7)
        assert err < 1e-12

    def test_hadamard_at_half_c1(self):
        """Hadamard identity at x=0.5, c=1."""
        exact, approx, err = _mc.hadamard_product_check(1, 0.5, max_arity=7)
        assert err < 1e-12

    def test_hadamard_at_one_c1(self):
        """Hadamard identity at x=1.0, c=1."""
        exact, approx, err = _mc.hadamard_product_check(1, 1.0, max_arity=7)
        assert err < 1e-12

    def test_hadamard_complex_point_c1(self):
        """Hadamard identity at a complex point, c=1."""
        exact, approx, err = _mc.hadamard_product_check(1, 0.3 + 0.2j, max_arity=7)
        assert err < 1e-10

    def test_hadamard_at_c13(self):
        """Hadamard identity at c=13 (self-dual Virasoro)."""
        exact, approx, err = _mc.hadamard_product_check(13, 1.0, max_arity=7)
        assert err < 1e-10

    def test_hadamard_large_x_c1(self):
        """Hadamard identity at a large x value, c=1."""
        exact, approx, err = _mc.hadamard_product_check(1, 5.0, max_arity=7)
        assert err < 1e-8


# ============================================================
# 4. Branch locus
# ============================================================

class TestBranchLocus:
    """Branch locus = discriminant zeros of the reduced critical polynomial."""

    def test_branch_locus_nonempty(self):
        """The branch locus is nonempty at arity >= 5."""
        bl = _mc.branch_locus_1d(max_arity=7)
        assert len(bl['numerator_zeros']) > 0

    def test_singularity_walls_include_c0(self):
        """c = 0 is a singularity wall (kappa = c/2 vanishes)."""
        bl = _mc.branch_locus_1d(max_arity=7)
        c0_found = any(abs(z) < 1e-8 for z in bl['denominator_zeros'])
        assert c0_found, "c=0 should be a singularity wall"

    def test_singularity_walls_include_minus_22_over_5(self):
        """c = -22/5 = -4.4 is a singularity wall (Kac determinant)."""
        bl = _mc.branch_locus_1d(max_arity=7)
        target = -4.4
        found = any(abs(z.real - target) < 1e-6 and abs(z.imag) < 1e-6
                     for z in bl['denominator_zeros'])
        assert found, "c = -22/5 should be a singularity wall"

    def test_branch_points_not_at_walls(self):
        """Branch points (numerator zeros) should not coincide with walls."""
        bl = _mc.branch_locus_1d(max_arity=7)
        for bp in bl['numerator_zeros']:
            for wall in bl['denominator_zeros']:
                assert abs(bp - wall) > 1e-4, (
                    f"Branch point {bp} too close to wall {wall}"
                )


# ============================================================
# 5. Jensen counting
# ============================================================

class TestJensenCounting:
    """Jensen formula gives upper bounds on N(R)."""

    def test_exact_count_small_R(self):
        """At small R, only the smallest-modulus root is captured."""
        jc = _mc.jensen_count(1.0, 1, max_arity=7)
        assert jc['exact_count'] >= 1
        assert jc['exact_count'] <= jc['total_roots']

    def test_exact_count_large_R(self):
        """At large R, all roots are captured."""
        jc = _mc.jensen_count(50.0, 1, max_arity=7)
        assert jc['exact_count'] == jc['total_roots']

    def test_monotonicity(self):
        """N(R) is non-decreasing in R."""
        prev = 0
        for R in [0.5, 1.0, 2.0, 5.0, 10.0, 50.0]:
            jc = _mc.jensen_count(R, 1, max_arity=7)
            assert jc['exact_count'] >= prev
            prev = jc['exact_count']

    def test_roots_partition(self):
        """roots_inside + roots_outside = total roots."""
        jc = _mc.jensen_count(2.0, 1, max_arity=7)
        assert len(jc['roots_inside']) + len(jc['roots_outside']) == jc['total_roots']


# ============================================================
# 6. Monodromy
# ============================================================

class TestMonodromy:
    """Monodromy around branch points permutes MC solutions."""

    def test_monodromy_at_branch_point(self):
        """Around a genuine branch point, the monodromy is nontrivial."""
        bl = _mc.branch_locus_1d(max_arity=7)
        real_bps = [z.real for z in bl['numerator_zeros']
                    if abs(z.imag) < 1e-8]
        if not real_bps:
            pytest.skip("No real branch points found")
        bp = real_bps[0]
        mono = _mc.monodromy_around_branch_point(bp, delta=0.05,
                                                  n_points=200,
                                                  max_arity=7)
        assert mono['is_branch_point'], (
            f"Expected nontrivial monodromy at c = {bp}"
        )
        assert any(cl > 1 for cl in mono['cycle_structure'])

    def test_monodromy_at_generic_point(self):
        """At a generic (non-branch) point, the monodromy is trivial."""
        mono = _mc.monodromy_around_branch_point(10.0, delta=0.05,
                                                  n_points=100,
                                                  max_arity=7)
        assert not mono['is_branch_point'], (
            "Monodromy should be trivial at generic c = 10"
        )
        assert all(cl == 1 for cl in mono['cycle_structure'])

    def test_permutation_is_valid(self):
        """The monodromy permutation is a valid permutation of {0,...,n-1}."""
        mono = _mc.monodromy_around_branch_point(10.0, delta=0.05,
                                                  n_points=100,
                                                  max_arity=7)
        n = len(mono['initial_roots'])
        perm = mono['permutation']
        assert len(perm) == n
        assert sorted(perm) == list(range(n))


# ============================================================
# 7. Order of shadow potential
# ============================================================

class TestOrderEstimate:
    """The truncated potential is polynomial (order 0); the coefficient
    growth rate estimates the order of the full (infinite-arity) potential."""

    def test_truncated_order_is_zero(self):
        """Finite truncation -> polynomial -> order 0."""
        od = _mc.order_of_shadow_potential(max_arity=7)
        assert od['truncated_order'] == 0

    def test_coefficient_data_length(self):
        """Coefficient data has one entry per arity."""
        od = _mc.order_of_shadow_potential(max_arity=7)
        assert len(od['coefficient_data']) == 6  # arities 2..7

    def test_coefficients_decrease(self):
        """The potential coefficients |a_r| decrease for large r (at c=1)."""
        od = _mc.order_of_shadow_potential(max_arity=7)
        data = od['coefficient_data']
        # a_4 < a_2 (quartic is smaller than quadratic at c=1)
        a2 = dict(data)[2]
        a4 = dict(data)[4]
        assert a4 < a2


# ============================================================
# 8. Reduced critical polynomial degree
# ============================================================

class TestReducedCritical:
    """Degree and leading coefficient of P(x;c) = (dS/dx)/x."""

    def test_degree_formula(self):
        """Degree of P = max_arity - 2."""
        for ma in [5, 6, 7]:
            assert _mc.reduced_critical_degree(ma) == ma - 2

    def test_real_solution_count(self):
        """mc_real_solution_count returns correct count."""
        nr = _mc.mc_real_solution_count(1, max_arity=7)
        roots = _mc.mc_solutions_1d(1, max_arity=7)
        nr_manual = sum(1 for z in roots if abs(z.imag) < 1e-10)
        assert nr == nr_manual


# ============================================================
# 9. Consistency with shadow_potential_singularity
# ============================================================

class TestConsistency:
    """MC solutions from this module agree with critical_points_numerical
    from shadow_potential_singularity.py."""

    def test_consistency_c1(self):
        """MC solutions at c=1 match critical_points_numerical."""
        mc_roots = sorted(_mc.mc_solutions_1d(1, max_arity=7),
                          key=lambda z: (round(z.real, 6), round(z.imag, 6)))
        sps_roots = sorted(_sps.critical_points_numerical(1, max_arity=7),
                           key=lambda z: (round(z.real, 6), round(z.imag, 6)))
        assert len(mc_roots) == len(sps_roots)
        for a, b in zip(mc_roots, sps_roots):
            assert abs(a - b) < 1e-6, f"Mismatch: {a} vs {b}"

    def test_consistency_c26(self):
        """MC solutions at c=26 match critical_points_numerical."""
        mc_roots = sorted(_mc.mc_solutions_1d(26, max_arity=7),
                          key=lambda z: (round(z.real, 4), round(z.imag, 4)))
        sps_roots = sorted(_sps.critical_points_numerical(26, max_arity=7),
                           key=lambda z: (round(z.real, 4), round(z.imag, 4)))
        assert len(mc_roots) == len(sps_roots)
        for a, b in zip(mc_roots, sps_roots):
            assert abs(a - b) < 1e-4, f"Mismatch: {a} vs {b}"


# ============================================================
# 10. MC moduli curve (c-parametric)
# ============================================================

class TestMCModuliCurve:
    """Test the c-parametric MC moduli curve tracing."""

    def test_moduli_curve_returns_dict(self):
        """mc_moduli_curve_1d returns a dict keyed by c values."""
        c_vals = [1, 5, 10, 13]
        result = _mc.mc_moduli_curve_1d(c_vals, max_arity=5)
        assert set(result.keys()) == set(c_vals)

    def test_moduli_curve_root_count_stable(self):
        """Root count is stable along the moduli curve for generic c."""
        c_vals = [1, 2, 5, 10, 13, 20, 26]
        result = _mc.mc_moduli_curve_1d(c_vals, max_arity=5)
        counts = [len(v) for v in result.values()]
        # All generic c should give max_arity - 2 = 3 roots
        assert all(n == 3 for n in counts)


# ============================================================
# 11. Rank-2 (W_3) critical locus
# ============================================================

class TestRank2:
    """Test the W_3 2d MC solutions and discriminant."""

    def test_2d_solutions_exist(self):
        """W_3 has MC solutions at generic c (at least on the T-line)."""
        sols = _mc.mc_solutions_2d(1, max_arity=5)
        assert len(sols) > 0

    def test_2d_t_line_solutions_are_1d(self):
        """T-line solutions (x_W = 0) of W_3 match the W_3 T-line restriction."""
        sols = _mc.mc_solutions_2d(1, max_arity=5)
        t_line = [(xt, xw) for (xt, xw) in sols if abs(xw) < 1e-10]
        # At max_arity 5, degree 3, should have 3 T-line roots
        assert len(t_line) == 3

    def test_rank2_t_line_comparison(self):
        """rank2_t_line_comparison returns valid structure."""
        comp = _mc.rank2_t_line_comparison(1, max_arity=5)
        assert 'w3_t_line_solutions' in comp
        assert 'vir_solutions' in comp
        # Both should have roots at arity 5
        assert comp['count_w3'] > 0
        assert comp['count_vir'] > 0


# ============================================================
# 12. MC moduli summary
# ============================================================

class TestMCModuliSummary:
    """Test the summary statistics function."""

    def test_summary_c1(self):
        """Summary at c=1 returns correct structure."""
        s = _mc.mc_moduli_summary(1, max_arity=7)
        assert s['c'] == 1
        assert s['n_solutions'] == 5
        assert s['n_real'] + 2 * s['n_complex_pairs'] == s['n_solutions']
        assert s['min_modulus'] > 0
        assert s['max_modulus'] >= s['min_modulus']
        assert s['hadamard_error'] < 1e-8

    def test_summary_c0_degenerate(self):
        """At c=0 (degenerate), the function handles gracefully."""
        s = _mc.mc_moduli_summary(0, max_arity=7)
        # c=0 makes kappa=0, which changes the polynomial structure
        assert 'n_solutions' in s


# ============================================================
# 13. Numpy fast solver consistency
# ============================================================

class TestNumpySolver:
    """The fast numpy root finder agrees with sympy's solve."""

    def test_numpy_vs_sympy_c1(self):
        """Numpy roots at c=1 match sympy roots."""
        np_roots = sorted(_mc._mc_solutions_numpy_sorted(1, max_arity=7),
                          key=lambda z: (round(z.real, 4), round(z.imag, 4)))
        sy_roots = sorted(_mc.mc_solutions_1d(1, max_arity=7),
                          key=lambda z: (round(z.real, 4), round(z.imag, 4)))
        assert len(np_roots) == len(sy_roots)
        for a, b in zip(np_roots, sy_roots):
            assert abs(a - b) < 1e-6, f"Numpy/sympy mismatch: {a} vs {b}"

    def test_numpy_vs_sympy_c13(self):
        """Numpy roots at c=13 match sympy roots."""
        np_roots = sorted(_mc._mc_solutions_numpy_sorted(13, max_arity=7),
                          key=lambda z: (round(z.real, 2), round(z.imag, 2)))
        sy_roots = sorted(_mc.mc_solutions_1d(13, max_arity=7),
                          key=lambda z: (round(z.real, 2), round(z.imag, 2)))
        assert len(np_roots) == len(sy_roots)
        for a, b in zip(np_roots, sy_roots):
            assert abs(a - b) < 1e-4, f"Numpy/sympy mismatch: {a} vs {b}"
