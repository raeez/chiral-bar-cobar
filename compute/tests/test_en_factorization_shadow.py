"""Tests for E_n factorization algebra shadows: bar complex, shadow obstruction tower, stabilization.

Verifies:
1. E_n operad invariants: Koszul shift, propagator degree, dual operad
2. Configuration space Betti numbers: H*(Conf_k(R^n)) for all n
3. E_n bar complex dimensions
4. Shadow obstruction tower: kappa_{E_n} for standard families
5. Formality: E_n operad and algebra formality
6. Factorization homology: S^1, T^d, S^d
7. Stabilization: E_n -> E_infty as n -> infty
8. Dunn additivity: E_{m+n} = E_m tensor E_n
9. Swiss-cheese connection: SC inside E_2
10. Graph complex: GC_n Euler characteristics
11. E_2 and E_3 bar complexes for specific algebras
12. Cross-consistency with Vol I chiral (E_1) computations

Each test performs ACTUAL computation from first principles.

Ground truth:
    Fresse: Modules over Operads and Functors
    Loday-Vallette: Algebraic Operads
    Kontsevich: Operads and Motives (1999)
    Francis: Tangent Complex and Hochschild Cohomology of E_n Rings (2013)
    Willwacher: M. Kontsevich's Graph Complex... (2015)
    Lambrechts-Volic: Formality of the Little N-Disks Operad (2014)
    CLAUDE.md: AP14, AP19, AP20
"""

import pytest
from fractions import Fraction
from math import factorial, comb

from compute.lib.en_factorization_shadow import (
    # E_n operad invariants
    en_generator_degree,
    en_koszul_shift,
    en_dual_operad_name,
    # Configuration spaces
    conf_space_betti,
    conf_space_euler,
    conf_space_total_betti,
    # Bar complex dimensions
    en_bar_chain_dimension,
    en_bar_chain_dimension_weighted,
    # Shadow obstruction tower
    kappa_en_free,
    kappa_en_affine,
    kappa_en_virasoro,
    cubic_shadow_en,
    quartic_shadow_en,
    shadow_depth_en,
    # Formality
    en_operad_formal,
    en_algebra_formal,
    # Factorization homology
    factorization_homology_circle,
    factorization_homology_torus,
    factorization_homology_sphere,
    # Stabilization
    kappa_stabilization_sequence,
    higher_shadow_stabilization_threshold,
    shadow_en_stabilized_value,
    # Dunn additivity
    dunn_additivity_check,
    kappa_dunn_additivity,
    # Swiss-cheese
    swiss_cheese_e2_decomposition,
    swiss_cheese_shadow_heisenberg,
    # Graph complex
    graph_complex_euler_char,
    willwacher_grt_dimension,
    # Specific algebras
    e2_bar_polynomial_algebra,
    e3_bar_free_algebra,
    # Summary
    en_shadow_summary,
    en_comparison_table,
)


# =========================================================================
# 1.  E_n operad invariants
# =========================================================================

class TestEnOperadInvariants:
    """Basic E_n operad numerical invariants."""

    def test_propagator_degree_e1(self):
        """E_1 propagator degree = 0 (no topology in Conf_k(R))."""
        assert en_generator_degree(1) == 0

    def test_propagator_degree_e2(self):
        """E_2 propagator degree = 1 (from S^1 = Conf_2(R^2) - {0})."""
        assert en_generator_degree(2) == 1

    def test_propagator_degree_e3(self):
        """E_3 propagator degree = 2 (from S^2)."""
        assert en_generator_degree(3) == 2

    def test_propagator_degree_general(self):
        """E_n propagator degree = n-1."""
        for n in range(1, 10):
            assert en_generator_degree(n) == n - 1

    def test_koszul_shift_e1(self):
        """E_1^! = E_1{-1}: shift = 1."""
        assert en_koszul_shift(1) == 1

    def test_koszul_shift_e2(self):
        """E_2^! = E_2{-2}: shift = 2."""
        assert en_koszul_shift(2) == 2

    def test_koszul_shift_e3(self):
        """E_3^! = E_3{-3}: shift = 3."""
        assert en_koszul_shift(3) == 3

    def test_koszul_shift_equals_n(self):
        """E_n^! = E_n{-n}: shift = n for all n."""
        for n in range(1, 10):
            assert en_koszul_shift(n) == n

    def test_dual_operad_names(self):
        """Dual operad is E_n{-n} for each n."""
        assert en_dual_operad_name(1) == "E_1{-1}"
        assert en_dual_operad_name(2) == "E_2{-2}"
        assert en_dual_operad_name(3) == "E_3{-3}"

    def test_invalid_n(self):
        """n < 1 should raise ValueError."""
        with pytest.raises(ValueError):
            en_generator_degree(0)
        with pytest.raises(ValueError):
            en_koszul_shift(0)
        with pytest.raises(ValueError):
            en_dual_operad_name(0)


# =========================================================================
# 2.  Configuration space Betti numbers
# =========================================================================

class TestConfSpaceBetti:
    """H*(Conf_k(R^n)) Betti numbers via Totaro/Arnold."""

    def test_conf1_any_n(self):
        """Conf_1(R^n) = R^n: contractible, b_0 = 1."""
        for n in range(1, 6):
            assert conf_space_betti(1, n) == [1]

    def test_conf2_r1(self):
        """Conf_2(R) = two half-lines: b_0 = 2."""
        assert conf_space_betti(2, 1) == [2]

    def test_conf2_r2(self):
        """Conf_2(R^2) ~ S^1: P(t) = 1 + t."""
        betti = conf_space_betti(2, 2)
        assert betti[0] == 1
        assert betti[1] == 1

    def test_conf2_r3(self):
        """Conf_2(R^3) ~ S^2: P(t) = 1 + t^2."""
        betti = conf_space_betti(2, 3)
        assert betti[0] == 1
        assert betti[1] == 0  # no degree-1 class
        assert betti[2] == 1

    def test_conf3_r2_arnold(self):
        """Conf_3(R^2): Arnold algebra, P = 1 + 3t + 2t^2."""
        betti = conf_space_betti(3, 2)
        assert betti[0] == 1
        assert betti[1] == 3
        assert betti[2] == 2

    def test_conf3_r3(self):
        """Conf_3(R^3): generators in degree 2, P = 1 + 3t^2 + 2t^4."""
        betti = conf_space_betti(3, 3)
        assert betti[0] == 1
        assert betti[2] == 3
        assert betti[4] == 2

    def test_conf4_r2(self):
        """Conf_4(R^2): P = (1+t)(1+2t)(1+3t) = 1 + 6t + 11t^2 + 6t^3."""
        betti = conf_space_betti(4, 2)
        assert betti[0] == 1
        assert betti[1] == 6
        assert betti[2] == 11
        assert betti[3] == 6

    def test_total_betti_conf_r2(self):
        """sum b_k(Conf_k(R^2)) = k! (total Betti = k!)."""
        for k in range(1, 6):
            total = conf_space_total_betti(k, 2)
            assert total == factorial(k)

    def test_total_betti_conf_r3(self):
        """sum b_k(Conf_k(R^3)) = k! (same formula for all n >= 2)."""
        for k in range(1, 6):
            total = conf_space_total_betti(k, 3)
            assert total == factorial(k)

    def test_euler_char_r2(self):
        """chi(Conf_k(R^2)) = 0 for k >= 2 (factor 1-1=0 in product)."""
        assert conf_space_euler(1, 2) == 1
        for k in range(2, 6):
            assert conf_space_euler(k, 2) == 0

    def test_euler_char_r3_odd(self):
        """chi(Conf_k(R^3)) = prod(1+j) = k! (n odd: all signs positive)."""
        for k in range(1, 6):
            assert conf_space_euler(k, 3) == factorial(k)

    def test_euler_char_r1(self):
        """chi(Conf_k(R)) = k! (k! discrete points)."""
        for k in range(1, 6):
            assert conf_space_euler(k, 1) == factorial(k)


# =========================================================================
# 3.  E_n bar complex dimensions
# =========================================================================

class TestEnBarComplex:
    """Bar complex B_{E_n}(A) dimensions."""

    def test_bar_arity0(self):
        """Arity 0: ground field, dim = 1."""
        for n in range(1, 5):
            assert en_bar_chain_dimension(0, n) == 1

    def test_bar_arity1(self):
        """Arity 1: Conf_1 = point, dim = 1."""
        for n in range(1, 5):
            assert en_bar_chain_dimension(1, n) == 1

    def test_bar_arity2_e1(self):
        """E_1 arity 2: Conf_2(R) = 2 points, dim = 2."""
        assert en_bar_chain_dimension(2, 1) == 2

    def test_bar_arity2_e2(self):
        """E_2 arity 2: Conf_2(R^2) ~ S^1, total dim = 2."""
        assert en_bar_chain_dimension(2, 2) == 2

    def test_bar_arity3_e1(self):
        """E_1 arity 3: Conf_3(R) = 6 points, dim = 6."""
        assert en_bar_chain_dimension(3, 1) == 6

    def test_bar_arity3_e2(self):
        """E_2 arity 3: Conf_3(R^2), total dim = 6 = 3!."""
        assert en_bar_chain_dimension(3, 2) == 6

    def test_bar_arity_k_total_is_k_factorial(self):
        """For n >= 2: total dim of arity-k bar = k!."""
        for n in range(2, 5):
            for k in range(1, 6):
                assert en_bar_chain_dimension(k, n) == factorial(k)

    def test_bar_weighted_e2_arity2(self):
        """E_2 bar at arity 2: degree 0 has dim 1, degree 1 has dim 1."""
        assert en_bar_chain_dimension_weighted(2, 2, 0) == 1
        assert en_bar_chain_dimension_weighted(2, 2, 1) == 1

    def test_bar_weighted_e3_arity2(self):
        """E_3 bar at arity 2: degree 0 has dim 1, degree 2 has dim 1."""
        assert en_bar_chain_dimension_weighted(2, 3, 0) == 1
        assert en_bar_chain_dimension_weighted(2, 3, 1) == 0  # no degree-1
        assert en_bar_chain_dimension_weighted(2, 3, 2) == 1


# =========================================================================
# 4.  Shadow obstruction tower: kappa_{E_n}
# =========================================================================

class TestKappaEn:
    """Modular characteristic kappa_{E_n} for standard families."""

    def test_kappa_heisenberg_e1(self):
        """kappa_{E_1}(H_k) = k/2 (standard chiral result)."""
        assert kappa_en_free(1, Fraction(1)) == Fraction(1, 2)
        assert kappa_en_free(1, Fraction(2)) == Fraction(1)

    def test_kappa_heisenberg_e2(self):
        """kappa_{E_2}(H_k) = k/2 (same as E_1 at binary level)."""
        assert kappa_en_free(2, Fraction(1)) == Fraction(1, 2)

    def test_kappa_universal_across_n(self):
        """kappa_{E_n}(H_k) = k/2 for ALL n >= 1 (binary universality)."""
        for n in range(1, 10):
            assert kappa_en_free(n, Fraction(1)) == Fraction(1, 2)
            assert kappa_en_free(n, Fraction(3)) == Fraction(3, 2)

    def test_kappa_affine_sl2_e1(self):
        """kappa_{E_1}(sl2_k) = dim(g)*(k+h^v)/(2*h^v) = 3*(k+2)/4."""
        # dim(sl2) = 3, h_dual = 2
        # k=1: 3*(1+2)/(2*2) = 9/4
        assert kappa_en_affine(1, 3, Fraction(1), 2) == Fraction(9, 4)
        # k=4: 3*(4+2)/(2*2) = 18/4 = 9/2
        assert kappa_en_affine(1, 3, Fraction(4), 2) == Fraction(9, 2)

    def test_kappa_affine_universal_n(self):
        """kappa_{E_n}(sl2_k) = 3*(k+2)/4 for all n (binary universality)."""
        for n in range(1, 6):
            assert kappa_en_affine(n, 3, Fraction(1), 2) == Fraction(9, 4)

    def test_kappa_virasoro_e1(self):
        """kappa_{E_1}(Vir_c) = c/2."""
        assert kappa_en_virasoro(1, Fraction(26)) == Fraction(13)
        assert kappa_en_virasoro(1, Fraction(1)) == Fraction(1, 2)

    def test_kappa_virasoro_self_dual_point(self):
        """Virasoro self-dual at c=13: kappa(Vir_13) = 13/2."""
        for n in range(1, 5):
            assert kappa_en_virasoro(n, Fraction(13)) == Fraction(13, 2)


# =========================================================================
# 5.  Shadow depth
# =========================================================================

class TestShadowDepth:
    """Shadow depth classification at E_n."""

    def test_gaussian_depth(self):
        """Class G: r_max = 2 (Heisenberg, free fields)."""
        assert shadow_depth_en(2, 'G') == 2

    def test_lie_depth(self):
        """Class L: r_max = 3 (KM algebras)."""
        assert shadow_depth_en(2, 'L') == 3

    def test_contact_depth(self):
        """Class C: r_max = 4 (beta-gamma, bc)."""
        assert shadow_depth_en(2, 'C') == 4

    def test_mixed_depth(self):
        """Class M: r_max = infinity (Virasoro, W_N)."""
        assert shadow_depth_en(2, 'M') == -1  # -1 = infinity

    def test_depth_independent_of_n(self):
        """Shadow depth is the same for all n (for formal E_n algebras)."""
        for cls in ('G', 'L', 'C', 'M'):
            depths = [shadow_depth_en(n, cls) for n in range(1, 6)]
            assert len(set(depths)) == 1  # all the same

    def test_invalid_class(self):
        """Unknown class raises ValueError."""
        with pytest.raises(ValueError):
            shadow_depth_en(2, 'X')


# =========================================================================
# 6.  Cubic and quartic shadows
# =========================================================================

class TestHigherShadows:
    """Cubic and quartic shadow invariants."""

    def test_cubic_free_vanishes(self):
        """S_3 = 0 for free (Heisenberg) E_n algebra at all n."""
        for n in range(1, 6):
            assert cubic_shadow_en(n) == 0

    def test_quartic_free_vanishes(self):
        """S_4 = 0 for free algebra with S_3 = 0 (class G)."""
        for n in range(1, 6):
            assert quartic_shadow_en(n, Fraction(1, 2)) == 0


# =========================================================================
# 7.  Formality
# =========================================================================

class TestFormality:
    """E_n operad and algebra formality."""

    def test_all_en_operads_formal(self):
        """E_n operad is formal for all n >= 1."""
        for n in range(1, 10):
            assert en_operad_formal(n) is True

    def test_free_algebra_formal(self):
        """Free E_n algebras are formal."""
        for n in range(1, 6):
            assert en_algebra_formal(n, 'free') is True
            assert en_algebra_formal(n, 'heisenberg') is True
            assert en_algebra_formal(n, 'polynomial') is True

    def test_virasoro_not_formal_as_e1(self):
        """Virasoro is NOT formal as E_1 algebra (shadow depth = infinity)."""
        # Virasoro is NOT in the formal list
        assert en_algebra_formal(1, 'virasoro') is False

    def test_formal_implies_gaussian(self):
        """Formal E_n algebra => class G (shadow depth 2)."""
        summary = en_shadow_summary(2, 'heisenberg')
        assert summary['algebra_formal'] is True
        assert summary['class'] == 'G'
        assert summary['shadow_depth'] == 2


# =========================================================================
# 8.  Factorization homology
# =========================================================================

class TestFactorizationHomology:
    """Factorization homology on standard manifolds."""

    def test_circle_genus1_shadow(self):
        """integral_{S^1} A: genus-1 shadow = kappa/24."""
        kappa = Fraction(1, 2)
        result = factorization_homology_circle(2, kappa)
        assert result['genus_1_shadow'] == kappa / 24

    def test_circle_independent_of_n(self):
        """S^1 factorization homology sees only E_1 structure."""
        kappa = Fraction(1, 2)
        for n in range(1, 6):
            result = factorization_homology_circle(n, kappa)
            assert result['genus_1_shadow'] == kappa / 24
            assert result['dimension'] == 1

    def test_torus_requires_sufficient_n(self):
        """T^d requires E_n with n >= d."""
        kappa = Fraction(1, 2)
        # T^3 with E_2: should flag error
        result = factorization_homology_torus(2, 3, kappa)
        assert 'error' in result

    def test_torus_valid(self):
        """T^2 with E_2: valid, genus-1 shadow = kappa/24."""
        kappa = Fraction(1, 2)
        result = factorization_homology_torus(2, 2, kappa)
        assert 'error' not in result
        assert result['genus_1_shadow'] == kappa / 24

    def test_sphere_requires_sufficient_n(self):
        """S^d requires E_n with n >= d."""
        kappa = Fraction(1, 2)
        result = factorization_homology_sphere(2, 3, kappa)
        assert 'error' in result

    def test_sphere_valid(self):
        """S^2 with E_2: valid, trace contribution = kappa."""
        kappa = Fraction(1, 2)
        result = factorization_homology_sphere(2, 2, kappa)
        assert 'error' not in result
        assert result['trace_contribution'] == kappa

    def test_sphere_cotrace_shift(self):
        """S^d has cotrace in degree d."""
        result = factorization_homology_sphere(3, 2, Fraction(1))
        assert result['cotrace_shift'] == 2

    def test_torus_dim0_is_algebra(self):
        """T^0 = point: factorization homology = A itself."""
        result = factorization_homology_torus(2, 0, Fraction(1))
        assert result['invariant'] == 'A itself'


# =========================================================================
# 9.  Stabilization: E_n -> E_infty
# =========================================================================

class TestStabilization:
    """E_n shadow invariants stabilize as n -> infinity."""

    def test_kappa_constant_in_n(self):
        """kappa_{E_n} is constant in n (binary universality)."""
        seq = kappa_stabilization_sequence(10, Fraction(1))
        values = list(seq.values())
        assert all(v == Fraction(1, 2) for v in values)

    def test_kappa_stabilization_different_k(self):
        """kappa_{E_n}(H_k) = k/2 constant for different k values."""
        for k_val in [Fraction(1), Fraction(2), Fraction(7, 3)]:
            seq = kappa_stabilization_sequence(5, k_val)
            expected = k_val / 2
            assert all(v == expected for v in seq.values())

    def test_stabilization_threshold_arity2(self):
        """Arity 2: threshold = 2 (stabilizes immediately for n >= 2)."""
        assert higher_shadow_stabilization_threshold(2) == 2

    def test_stabilization_threshold_arity3(self):
        """Arity 3: threshold = 3."""
        assert higher_shadow_stabilization_threshold(3) == 3

    def test_stabilization_threshold_monotone(self):
        """Threshold is nondecreasing in arity."""
        for r in range(2, 10):
            assert (higher_shadow_stabilization_threshold(r)
                    <= higher_shadow_stabilization_threshold(r + 1))

    def test_gaussian_stabilized_zero(self):
        """Class G: stabilized S_r = 0 for all r >= 3."""
        for r in range(3, 8):
            assert shadow_en_stabilized_value(r, 'G') == 0


# =========================================================================
# 10.  Dunn additivity: E_{m+n} = E_m tensor E_n
# =========================================================================

class TestDunnAdditivity:
    """Dunn additivity at the shadow level."""

    def test_koszul_shift_additive(self):
        """Koszul shift: shift(E_{m+n}) = shift(E_m) + shift(E_n)."""
        for m in range(1, 5):
            for n_val in range(1, 5):
                result = dunn_additivity_check(m, n_val)
                assert result['koszul_shift_additive'] is True

    def test_propagator_degree_additive(self):
        """Propagator degree: deg(E_{m+n}) = deg(E_m) + deg(E_n).
        Since deg(E_k) = k-1: (m+n-1) = (m-1) + (n-1) iff m+n-1 = m+n-2,
        which is FALSE.  Propagator degree is NOT additive."""
        result = dunn_additivity_check(1, 1)
        # E_2 propagator degree = 1, E_1 + E_1 = 0 + 0 = 0
        assert result['propagator_degree_additive'] is False

    def test_kappa_dunn_trivially_equal(self):
        """kappa is the same for all E_n, so Dunn is trivially satisfied."""
        for m in range(1, 4):
            for n_val in range(1, 4):
                result = kappa_dunn_additivity(m, n_val, Fraction(1))
                assert result['all_equal'] is True
                assert result['value'] == Fraction(1, 2)


# =========================================================================
# 11.  Swiss-cheese connection
# =========================================================================

class TestSwissCheese:
    """Swiss-cheese operad inside E_2."""

    def test_sc_ambient_is_e2(self):
        """Swiss-cheese sits inside E_2."""
        info = swiss_cheese_e2_decomposition()
        assert info['ambient'] == 'E_2'

    def test_sc_has_two_e1_factors(self):
        """SC has chiral and topological E_1 factors."""
        info = swiss_cheese_e2_decomposition()
        assert 'E_1^{ch}' in info['chiral_factor']
        assert 'E_1^{top}' in info['topological_factor']

    def test_sc_novel_at_arity3(self):
        """Mixed operations first appear at arity 3."""
        info = swiss_cheese_e2_decomposition()
        assert info['novel_at_arity'] == 3

    def test_heisenberg_sc_kappa(self):
        """Heisenberg SC shadow: kappa = k/2."""
        data = swiss_cheese_shadow_heisenberg(Fraction(1))
        assert data['kappa_total'] == Fraction(1, 2)
        assert data['kappa_chiral'] == Fraction(1, 2)

    def test_heisenberg_sc_class_G(self):
        """Heisenberg is class G under SC decomposition."""
        data = swiss_cheese_shadow_heisenberg(Fraction(1))
        assert data['class'] == 'G'
        assert data['shadow_depth'] == 2
        assert data['S3'] == 0


# =========================================================================
# 12.  Graph complex
# =========================================================================

class TestGraphComplex:
    """GC_n Euler characteristics and grt dimensions."""

    def test_gc_n_odd_acyclic(self):
        """GC_n is acyclic for n odd, loop order > 0."""
        for n in [3, 5, 7]:
            for L in range(1, 5):
                assert graph_complex_euler_char(n, L) == 0

    def test_gc2_loop0(self):
        """GC_2 at loop 0: chi = 1."""
        assert graph_complex_euler_char(2, 0) == 1

    def test_gc2_loop1(self):
        """GC_2 at loop 1: chi = 0 (wheels cancel)."""
        assert graph_complex_euler_char(2, 1) == 0

    def test_gc2_loop2(self):
        """GC_2 at loop 2: chi = 1."""
        assert graph_complex_euler_char(2, 2) == 1

    def test_grt_even_degree_zero(self):
        """grt has no even-degree elements."""
        for d in range(0, 20, 2):
            assert willwacher_grt_dimension(d) == 0

    def test_grt_degree1_zero(self):
        """grt has no degree-1 element."""
        assert willwacher_grt_dimension(1) == 0

    def test_grt_degree3_one(self):
        """grt has exactly one element in degree 3 (related to zeta(3))."""
        assert willwacher_grt_dimension(3) == 1

    def test_grt_degree5_one(self):
        """grt has exactly one element in degree 5 (related to zeta(5))."""
        assert willwacher_grt_dimension(5) == 1

    def test_grt_degree11_two(self):
        """grt has two elements in degree 11 (depth-2 appears)."""
        assert willwacher_grt_dimension(11) == 2


# =========================================================================
# 13.  E_2 and E_3 bar for specific algebras
# =========================================================================

class TestSpecificAlgebras:
    """E_2 and E_3 bar complexes for polynomial and free algebras."""

    def test_e2_bar_kx_formal(self):
        """B_{E_2}(k[x]) is formal."""
        result = e2_bar_polynomial_algebra(1, 10)
        assert result['formal'] is True

    def test_e2_bar_kx_class_G(self):
        """k[x] as E_2 algebra is class G (shadow depth 2)."""
        result = e2_bar_polynomial_algebra(1, 10)
        assert result['class'] == 'G'
        assert result['shadow_depth'] == 2

    def test_e2_bar_kx_kappa(self):
        """kappa(k[x]) = 1/2 (one generator at level 1)."""
        result = e2_bar_polynomial_algebra(1, 10)
        assert result['kappa'] == Fraction(1, 2)

    def test_e2_bar_kxy_kappa(self):
        """kappa(k[x,y]) = 1 (two generators at level 1)."""
        result = e2_bar_polynomial_algebra(2, 10)
        assert result['kappa'] == Fraction(1)

    def test_e3_bar_free_formal(self):
        """Free E_3 algebra is formal."""
        result = e3_bar_free_algebra(1)
        assert result['formal'] is True

    def test_e3_bar_free_class_G(self):
        """Free E_3 algebra is class G."""
        result = e3_bar_free_algebra(1)
        assert result['class'] == 'G'
        assert result['shadow_depth'] == 2

    def test_e3_bar_free_kappa(self):
        """kappa of free E_3 on m generators = m/2."""
        for m in range(1, 5):
            result = e3_bar_free_algebra(m)
            assert result['kappa'] == Fraction(m, 2)


# =========================================================================
# 14.  Comprehensive summary and comparison table
# =========================================================================

class TestSummaryAndTable:
    """Summary and cross-n comparison."""

    def test_summary_keys(self):
        """Summary dict has expected keys."""
        s = en_shadow_summary(2, 'heisenberg')
        expected_keys = {
            'en_level', 'algebra', 'level', 'kappa', 'kappa_over_24',
            'operad_formal', 'algebra_formal', 'koszul_shift',
            'propagator_degree', 'dual_operad', 'shadow_depth', 'class',
            'stabilization_threshold_arity3',
        }
        assert expected_keys.issubset(set(s.keys()))

    def test_summary_values_e2_heisenberg(self):
        """Summary for E_2 Heisenberg at k=1."""
        s = en_shadow_summary(2, 'heisenberg', Fraction(1))
        assert s['en_level'] == 2
        assert s['kappa'] == Fraction(1, 2)
        assert s['koszul_shift'] == 2
        assert s['propagator_degree'] == 1
        assert s['operad_formal'] is True
        assert s['algebra_formal'] is True

    def test_comparison_table_length(self):
        """Comparison table for n=1..6 has 6 entries."""
        table = en_comparison_table(6)
        assert len(table) == 6

    def test_comparison_table_kappa_constant(self):
        """All entries in comparison table have kappa = k/2."""
        table = en_comparison_table(6, Fraction(1))
        for entry in table:
            assert entry['kappa'] == Fraction(1, 2)

    def test_comparison_table_propagator_degree_increasing(self):
        """Propagator degree is strictly increasing in n."""
        table = en_comparison_table(6)
        degs = [e['propagator_degree'] for e in table]
        for i in range(len(degs) - 1):
            assert degs[i] < degs[i + 1]

    def test_comparison_table_koszul_shift_increasing(self):
        """Koszul shift = n, strictly increasing."""
        table = en_comparison_table(6)
        shifts = [e['koszul_shift'] for e in table]
        for i in range(len(shifts) - 1):
            assert shifts[i] < shifts[i + 1]


# =========================================================================
# 15.  Cross-consistency with E_1 (chiral) computations
# =========================================================================

class TestCrossConsistencyE1:
    """Verify E_n computations at n=1 match chiral (Vol I) results."""

    def test_e1_kappa_heisenberg_matches_vol1(self):
        """kappa_{E_1}(H_1) = 1/2, matching the chiral computation."""
        assert kappa_en_free(1, Fraction(1)) == Fraction(1, 2)

    def test_e1_kappa_virasoro_c26(self):
        """kappa_{E_1}(Vir_26) = 13, matching Vol I."""
        assert kappa_en_virasoro(1, Fraction(26)) == Fraction(13)

    def test_e1_kappa_virasoro_c0(self):
        """kappa_{E_1}(Vir_0) = 0 (uncurved bar complex)."""
        assert kappa_en_virasoro(1, Fraction(0)) == Fraction(0)

    def test_e1_kappa_sl2_level1(self):
        """kappa_{E_1}(sl2_1) = 9/4, matching Vol I kappa(KM) formula."""
        # kappa(KM) = dim(g) * (k + h_dual) / (2 * h_dual)
        # sl2: dim=3, h_dual=2, k=1: kappa = 3*(1+2)/(2*2) = 9/4
        assert kappa_en_affine(1, 3, Fraction(1), 2) == Fraction(9, 4)

    def test_conf_r2_matches_arnold(self):
        """Conf_k(R^2) Betti numbers match Arnold algebra (en_koszul_bridge)."""
        # Conf_3(R^2): should match arnold_poincare_polynomial(3) = {0:1, 1:3, 2:2}
        betti = conf_space_betti(3, 2)
        assert betti == [1, 3, 2]

    def test_conf_r2_matches_arnold_n4(self):
        """Conf_4(R^2) matches Arnold at n=4."""
        betti = conf_space_betti(4, 2)
        assert betti == [1, 6, 11, 6]

    def test_genus1_shadow_formula(self):
        """F_1 = kappa * lambda_1 = kappa / 24 at E_1."""
        kappa = Fraction(1, 2)
        result = factorization_homology_circle(1, kappa)
        assert result['genus_1_shadow'] == Fraction(1, 48)


# =========================================================================
# 16.  Edge cases and input validation
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_conf0_any_n(self):
        """Conf_0 = point for all n."""
        for n in range(1, 5):
            assert conf_space_betti(0, n) == [1]

    def test_conf_negative_k(self):
        """Negative arity defaults to single point."""
        assert conf_space_betti(-1, 2) == [1]

    def test_stabilization_threshold_arity1(self):
        """Arity 1: threshold = 1 (trivial)."""
        assert higher_shadow_stabilization_threshold(1) == 1

    def test_bar_dimension_arity0_weighted(self):
        """Bar at arity 0, degree 0 = 1; degree > 0 = 0."""
        for n in range(1, 5):
            assert en_bar_chain_dimension_weighted(0, n, 0) == 1
            assert en_bar_chain_dimension_weighted(0, n, 1) == 0

    def test_kappa_at_level_zero(self):
        """kappa(H_0) = 0 for all n (zero level = uncurved)."""
        for n in range(1, 6):
            assert kappa_en_free(n, Fraction(0)) == Fraction(0)

    def test_kappa_negative_level(self):
        """kappa at negative level (for Koszul dual)."""
        # H_{-1}^! has kappa = -1/2
        assert kappa_en_free(1, Fraction(-1)) == Fraction(-1, 2)

    def test_factorization_homology_dim_check(self):
        """Factorization homology dimension matches manifold."""
        result = factorization_homology_circle(3, Fraction(1))
        assert result['dimension'] == 1
        result = factorization_homology_sphere(3, 2, Fraction(1))
        assert result['dimension'] == 2
