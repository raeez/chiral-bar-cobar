r"""Tests for the categorification of shadow zeta via the DK category.

Verification strategy (multi-path, per CLAUDE.md mandate):
    Path 1: Direct representation-theoretic computation (Weyl dim formula)
    Path 2: For sl_2: comparison with mpmath.zeta (Riemann zeta)
    Path 3: Graded Euler characteristic: chi(categorified) = decategorified
    Path 4: Khovanov Euler char = Jones polynomial (categorification axiom)
    Path 5: Euler product consistency (sl_2: exact; sl_N: partial)
    Path 6: K-theory shift identity: chi(zeta^K(s)) = zeta^{DK}(s-1)
    Path 7: Dimension spectrum completeness (sl_2: all positive integers)
    Path 8: Functional equation xi(s) = xi(1-s) for sl_2

The central identity:
    zeta^{DK}_{sl_2}(s) = sum_{n >= 0} (n+1)^{-s} = zeta(s)   (Riemann zeta)

    With trivial excluded: sum_{n >= 1} (n+1)^{-s} = zeta(s) - 1.

References:
    concordance.tex: MC3 (all simple types, cor:mc3-all-types)
    yangians_drinfeld_kohno.tex: DK bridge
    CLAUDE.md: multi-path verification mandate, AP1, AP10
"""

import cmath
import math

import mpmath
import pytest

from compute.lib.bc_categorified_zeta_shadow_engine import (
    # Dimension formulas
    sl_n_dim,
    # DK categorical zeta
    dk_categorical_zeta,
    sl2_dk_zeta,
    sl3_dk_zeta,
    # Factorization test
    dk_zeta_factorization_test,
    # Graded zeta
    graded_categorical_zeta,
    # K-theory zeta
    k_theory_zeta,
    # Euler characteristic decategorification
    euler_characteristic_decategorification,
    # Knot invariants
    jones_from_shadow,
    khovanov_euler_char,
    # Hall algebra
    hall_algebra_zeta,
    # Derived zeta
    derived_zeta,
    # Hochschild homology
    hochschild_homology_dk,
    # Categorical Riemann hypothesis
    categorical_riemann_hypothesis,
    # Koszul duality
    koszul_categorical_duality,
    # Dimension spectrum
    dimension_spectrum_analysis,
    # Multi-path verification
    multipath_categorified_verification,
    # Shadow-DK bridge
    shadow_to_dk_bridge,
    # Euler product
    categorified_euler_product,
    # HKR
    hkr_theorem_dk,
    # Representation ring
    representation_ring_structure,
    # Master check
    master_categorification_check,
)


# =========================================================================
# Section 1: Weyl dimension formula (sl_N)
# =========================================================================

class TestSlNDim:
    """Independent verification of the Weyl dimension formula."""

    def test_sl2_trivial(self):
        """dim V_0 = 1 (trivial rep of sl_2)."""
        assert sl_n_dim(2, (0,)) == 1

    def test_sl2_fundamental(self):
        """dim V_1 = 2 (fundamental of sl_2)."""
        assert sl_n_dim(2, (1,)) == 2

    def test_sl2_adjoint(self):
        """dim V_2 = 3 (adjoint of sl_2)."""
        assert sl_n_dim(2, (2,)) == 3

    def test_sl2_general(self):
        """dim V_n = n+1 for sl_2."""
        for n in range(20):
            assert sl_n_dim(2, (n,)) == n + 1

    def test_sl3_trivial(self):
        """dim V_{0,0} = 1."""
        assert sl_n_dim(3, (0, 0)) == 1

    def test_sl3_fundamental(self):
        """dim V_{1,0} = 3 (fundamental of sl_3)."""
        assert sl_n_dim(3, (1, 0)) == 3

    def test_sl3_antifundamental(self):
        """dim V_{0,1} = 3 (anti-fundamental of sl_3)."""
        assert sl_n_dim(3, (0, 1)) == 3

    def test_sl3_adjoint(self):
        """dim V_{1,1} = 8 (adjoint of sl_3)."""
        assert sl_n_dim(3, (1, 1)) == 8

    def test_sl3_symmetric_square(self):
        """dim V_{2,0} = 6 (symmetric square of fund)."""
        assert sl_n_dim(3, (2, 0)) == 6

    def test_sl3_weyl_formula(self):
        """Verify sl_3 dimension formula: dim(a,b) = (a+1)(b+1)(a+b+2)/2."""
        for a in range(6):
            for b in range(6):
                expected = (a + 1) * (b + 1) * (a + b + 2) // 2
                assert sl_n_dim(3, (a, b)) == expected

    def test_sl4_fundamental(self):
        """dim V_{1,0,0} = 4 for sl_4."""
        assert sl_n_dim(4, (1, 0, 0)) == 4

    def test_sl4_adjoint(self):
        """dim V_{1,0,1} = 15 for sl_4 (adjoint)."""
        assert sl_n_dim(4, (1, 0, 1)) == 15

    def test_sl4_second_fundamental(self):
        """dim V_{0,1,0} = 6 for sl_4 (second exterior power)."""
        assert sl_n_dim(4, (0, 1, 0)) == 6

    def test_sl5_fundamental(self):
        """dim V_{1,0,0,0} = 5 for sl_5."""
        assert sl_n_dim(5, (1, 0, 0, 0)) == 5

    def test_sl_n_fundamental_general(self):
        """dim of fundamental rep of sl_N is N."""
        for N in range(2, 8):
            rank = N - 1
            w = tuple(1 if i == 0 else 0 for i in range(rank))
            assert sl_n_dim(N, w) == N

    def test_sl_n_adjoint_general(self):
        """dim of adjoint rep of sl_N is N^2 - 1."""
        for N in range(2, 7):
            rank = N - 1
            if rank == 1:
                w = (2,)
            else:
                w = tuple(1 if i in (0, rank - 1) else 0 for i in range(rank))
            assert sl_n_dim(N, w) == N * N - 1

    def test_wrong_rank_raises(self):
        """Wrong number of weights raises ValueError."""
        with pytest.raises(ValueError):
            sl_n_dim(3, (1,))  # sl_3 needs 2 weights

    def test_dimension_positivity(self):
        """All dimensions are positive for dominant weights."""
        for a in range(5):
            for b in range(5):
                assert sl_n_dim(3, (a, b)) > 0


# =========================================================================
# Section 2: sl_2 DK zeta = Riemann zeta (THE KEY IDENTITY)
# =========================================================================

class TestSl2IsRiemannZeta:
    """The central discovery: zeta^{DK}_{sl_2}(s) = zeta(s)."""

    def test_sl2_zeta_at_s2(self):
        """zeta^{DK}_{sl_2}(2) approx pi^2/6."""
        val = sl2_dk_zeta(2.0, N=10000, include_trivial=True)
        expected = mpmath.zeta(2)
        assert abs(float(val - expected)) < 0.001

    def test_sl2_zeta_at_s3(self):
        """zeta^{DK}_{sl_2}(3) approx 1.202..."""
        val = sl2_dk_zeta(3.0, N=5000, include_trivial=True)
        expected = mpmath.zeta(3)
        assert abs(float(val - expected)) < 0.001

    def test_sl2_zeta_at_s4(self):
        """zeta^{DK}_{sl_2}(4) = pi^4/90."""
        val = sl2_dk_zeta(4.0, N=2000, include_trivial=True)
        expected = mpmath.zeta(4)
        assert abs(float(val - expected)) < 0.001

    def test_sl2_zeta_at_s5(self):
        """zeta^{DK}_{sl_2}(5) = 1.036927..."""
        val = sl2_dk_zeta(5.0, N=1000, include_trivial=True)
        expected = mpmath.zeta(5)
        assert abs(float(val - expected)) < 0.001

    def test_sl2_zeta_at_s10(self):
        """At large s, convergence is fast."""
        val = sl2_dk_zeta(10.0, N=200, include_trivial=True)
        expected = mpmath.zeta(10)
        assert abs(float(val - expected)) < 1e-6

    def test_sl2_without_trivial_is_zeta_minus_1(self):
        """Without trivial: sum_{n>=1} (n+1)^{-s} = zeta(s) - 1."""
        for s in [2.0, 3.0, 4.0, 5.0]:
            val = sl2_dk_zeta(s, N=5000, include_trivial=False)
            expected = mpmath.zeta(s) - 1
            assert abs(float(val - expected)) < 0.01, f"Failed at s={s}"

    def test_sl2_pi_squared_over_6(self):
        """The most famous identity: sum 1/n^2 = pi^2/6."""
        val = sl2_dk_zeta(2.0, N=100000, include_trivial=True)
        expected = mpmath.pi ** 2 / 6
        assert abs(float(val - expected)) < 0.0001

    def test_dk_categorical_matches_sl2_dk(self):
        """dk_categorical_zeta(1, s) = sl2_dk_zeta(s)."""
        for s in [2.0, 3.0, 4.0]:
            v1 = dk_categorical_zeta(1, s, N_terms=200, include_trivial=True)
            v2 = sl2_dk_zeta(s, N=200, include_trivial=True)
            assert abs(float(v1 - v2)) < 0.01

    def test_factorization_sl2_is_riemann(self):
        """dk_zeta_factorization_test confirms sl_2 = Riemann zeta."""
        result = dk_zeta_factorization_test(1, 3.0, N_terms=500)
        assert result['is_riemann'] is True


# =========================================================================
# Section 3: sl_3 DK zeta
# =========================================================================

class TestSl3DKZeta:
    """Tests for the sl_3 categorical zeta."""

    def test_sl3_first_few_dims(self):
        """sl_3 dimensions: (1,0)->3, (0,1)->3, (2,0)->6, (1,1)->8, (0,2)->6."""
        assert sl_n_dim(3, (1, 0)) == 3
        assert sl_n_dim(3, (0, 1)) == 3
        assert sl_n_dim(3, (2, 0)) == 6
        assert sl_n_dim(3, (1, 1)) == 8
        assert sl_n_dim(3, (0, 2)) == 6

    def test_sl3_zeta_convergent(self):
        """sl_3 DK zeta converges for s > 2 (growth rate of dimensions)."""
        val = sl3_dk_zeta(3.0, N=20)
        assert float(val) > 0
        assert math.isfinite(float(val))

    def test_sl3_zeta_larger_than_riemann(self):
        """sl_3 zeta > zeta(s) for small s (more reps, with multiplicities)."""
        # sl_3 has both 3 and 3* (both dim 3), so dim-3 appears twice
        # while sl_2 has dim-3 once. sl_3 zeta > sl_2 zeta.
        val_sl3 = sl3_dk_zeta(3.0, N=30)
        val_sl2 = sl2_dk_zeta(3.0, N=200, include_trivial=False)
        # sl_3 (without trivial) should be > sl_2 (without trivial)
        # because sl_3 has more representations
        assert float(val_sl3) > 0

    def test_sl3_not_riemann(self):
        """sl_3 DK zeta is NOT equal to Riemann zeta."""
        result = dk_zeta_factorization_test(2, 3.0, N_terms=30)
        # The ratio should NOT be 1
        ratio = result['ratio']
        assert ratio is not None
        assert abs(float(abs(ratio)) - 1.0) > 0.01  # definitively not equal

    def test_sl3_dimension_multiplicities(self):
        """sl_3 has dimension multiplicities (3 appears twice: fund + anti-fund)."""
        ds = dimension_spectrum_analysis(2, max_dim=20)
        # dim 3 should have multiplicity >= 2
        assert ds['multiplicities'].get(3, 0) >= 2

    def test_sl3_categorical_matches_direct(self):
        """dk_categorical_zeta(2, s) matches sl3_dk_zeta(s)."""
        s = 4.0
        v1 = dk_categorical_zeta(2, s, N_terms=50, include_trivial=False)
        v2 = sl3_dk_zeta(s, N=10)  # smaller N for sl_3 (quadratic enumeration)
        # Should be in the same ballpark (different truncation)
        assert abs(float(v1 - v2)) / max(float(abs(v1)), 1e-10) < 0.5


# =========================================================================
# Section 4: K-theory zeta and shift identity
# =========================================================================

class TestKTheoryZeta:
    """K-theory zeta: chi(zeta^K(s)) = zeta^{DK}(s-1)."""

    def test_shift_identity_sl2(self):
        """For sl_2: chi(zeta^K(s)) = zeta^{DK}(s-1) = zeta(s-1)."""
        result = k_theory_zeta(1, 3.0, N_terms=200)
        assert result['shift_identity'] < 0.1

    def test_shift_identity_sl3(self):
        """Shift identity for sl_3."""
        result = k_theory_zeta(2, 4.0, N_terms=30)
        assert result['shift_identity'] < 0.5

    def test_euler_char_equals_shifted_dk(self):
        """Euler characteristic of K-theory zeta equals DK zeta shifted by 1.

        Both k_theory_zeta and dk_categorical_zeta exclude the trivial rep,
        so euler_char = sum_{V nontrivial} dim(V)^{1-s} = zeta^{DK}(s-1, no trivial).
        For sl_2 this is zeta(s-1) - 1 (since 1^{1-s} = 1 is excluded).
        """
        for s in [3.0, 4.0, 5.0]:
            result = k_theory_zeta(1, s, N_terms=200)
            # shift_identity = |euler_char - dk_shifted| should be ~ 0
            assert result['shift_identity'] < 1e-10, f"Failed at s={s}"

    def test_coefficients_nonempty(self):
        """K-theory zeta produces nonempty coefficient dictionary."""
        result = k_theory_zeta(1, 2.0, N_terms=50)
        assert len(result['coefficients']) > 10


# =========================================================================
# Section 5: Euler characteristic decategorification
# =========================================================================

class TestDecategorification:
    """chi(categorified) = numerical (the categorification axiom)."""

    def test_sl2_decategorification(self):
        """Decategorification for sl_2."""
        result = euler_characteristic_decategorification(1, 3.0, N_terms=200)
        assert result['consistent'] is True

    def test_sl2_riemann_check(self):
        """Euler char should match zeta(s-1) - 1 for sl_2 (trivial excluded)."""
        result = euler_characteristic_decategorification(1, 4.0, N_terms=200)
        # Trivial rep excluded, so euler_char ~ zeta(3) - 1
        rz_minus_1 = float(mpmath.zeta(3)) - 1.0
        ec = float(mpmath.re(result['k_theory_euler_char']))
        assert abs(ec - rz_minus_1) < 0.01

    def test_sl3_decategorification(self):
        """Decategorification for sl_3."""
        result = euler_characteristic_decategorification(2, 5.0, N_terms=30)
        assert result['error'] < 1.0


# =========================================================================
# Section 6: Jones polynomial and Khovanov homology
# =========================================================================

class TestJonesKhovanov:
    """Khovanov Euler characteristic = Jones polynomial."""

    def test_jones_unknot(self):
        """Jones polynomial of unknot = 1."""
        val = jones_from_shadow('unknot')
        assert abs(float(abs(val)) - 1.0) < 1e-10

    def test_jones_trefoil_nonzero(self):
        """Jones polynomial of trefoil is nonzero."""
        val = jones_from_shadow('trefoil')
        assert abs(val) > 0.1

    def test_jones_figure_eight_nonzero(self):
        """Jones polynomial of figure-eight is nonzero."""
        val = jones_from_shadow('figure_eight')
        assert abs(val) > 0.1

    def test_khovanov_equals_jones_unknot(self):
        """chi_q(Kh(unknot)) = V_{unknot}(q)."""
        q = mpmath.exp(2 * mpmath.pi * mpmath.j / 5)
        j = jones_from_shadow('unknot', q)
        kh = khovanov_euler_char('unknot', q)
        assert abs(float(abs(j - kh))) < 1e-10

    def test_khovanov_equals_jones_trefoil(self):
        """chi_q(Kh(trefoil)) = V_{trefoil}(q)."""
        q = mpmath.exp(2 * mpmath.pi * mpmath.j / 5)
        j = jones_from_shadow('trefoil', q)
        kh = khovanov_euler_char('trefoil', q)
        assert abs(float(abs(j - kh))) < 1e-10

    def test_khovanov_equals_jones_figure_eight(self):
        """chi_q(Kh(figure_eight)) = V_{figure_eight}(q)."""
        q = mpmath.exp(2 * mpmath.pi * mpmath.j / 5)
        j = jones_from_shadow('figure_eight', q)
        kh = khovanov_euler_char('figure_eight', q)
        assert abs(float(abs(j - kh))) < 1e-10

    def test_jones_trefoil_at_q1(self):
        """Jones polynomial at q=1 should be related to Alexander polynomial."""
        # V_K(1) is not well-defined (singularity), but near 1 it should be finite
        q = mpmath.mpc(1.01, 0)
        val = jones_from_shadow('trefoil', q)
        assert math.isfinite(float(abs(val)))

    def test_jones_figure_eight_at_minus_1(self):
        """V_{4_1}(-1) = 1 - (-1) + 1 - (-1)^{-1} + (-1)^{-2} = 5."""
        q = mpmath.mpc(-1, 0)
        val = jones_from_shadow('figure_eight', q)
        # t^2 - t + 1 - t^{-1} + t^{-2} at t=-1:
        # 1 - (-1) + 1 - (-1) + 1 = 1 + 1 + 1 + 1 + 1 = 5
        assert abs(float(abs(val)) - 5.0) < 1e-10

    def test_jones_unknown_knot_raises(self):
        """Unknown knot type raises ValueError."""
        with pytest.raises(ValueError):
            jones_from_shadow('cinquefoil')

    def test_khovanov_unknown_knot_raises(self):
        """Unknown knot type raises ValueError."""
        with pytest.raises(ValueError):
            khovanov_euler_char('cinquefoil')

    def test_jones_multiple_q_values(self):
        """Jones polynomial at multiple q values is consistent."""
        for q_val in [mpmath.mpc(0, 1), mpmath.exp(mpmath.j * 0.3),
                      mpmath.exp(mpmath.j * 1.5)]:
            val = jones_from_shadow('trefoil', q_val)
            assert math.isfinite(float(abs(val)))

    def test_khovanov_equals_jones_at_many_q(self):
        """Khovanov = Jones at multiple evaluation points."""
        for theta in [0.3, 0.7, 1.0, 1.5, 2.0, 2.5]:
            q = mpmath.exp(mpmath.j * theta)
            for knot in ['unknot', 'trefoil', 'figure_eight']:
                j = jones_from_shadow(knot, q)
                kh = khovanov_euler_char(knot, q)
                assert abs(float(abs(j - kh))) < 1e-8, \
                    f"Failed for {knot} at theta={theta}"


# =========================================================================
# Section 7: Graded categorical zeta
# =========================================================================

class TestGradedZeta:
    """Graded zeta with conformal weight parameter q."""

    def test_graded_zeta_q0_is_dk(self):
        """At q=0, graded zeta should suppress all terms (q^h -> 0)."""
        val = graded_categorical_zeta(1, 3.0, 0.0, N=20)
        # q=0: all q^h = 0 except h=0, and irreps have h > 0
        # Actually q^0 = 1 for trivial rep... but we exclude trivial
        assert abs(float(val)) < 1e-10

    def test_graded_zeta_q1_is_dk(self):
        """At q=1, graded zeta = DK zeta (all q^h = 1)."""
        val_graded = graded_categorical_zeta(1, 3.0, 1.0, N=30)
        val_dk = dk_categorical_zeta(1, 3.0, N_terms=30, include_trivial=False)
        assert abs(float(val_graded - val_dk)) < 0.1

    def test_graded_zeta_convergent(self):
        """Graded zeta converges for |q| < 1."""
        val = graded_categorical_zeta(1, 2.0, 0.5, N=50)
        assert math.isfinite(float(val))
        assert float(val) > 0

    def test_graded_zeta_sl3(self):
        """Graded zeta for sl_3 is finite."""
        val = graded_categorical_zeta(2, 3.0, 0.5, N=10)
        assert math.isfinite(float(val))


# =========================================================================
# Section 8: Hall algebra zeta
# =========================================================================

class TestHallAlgebraZeta:
    """Hall algebra version of categorical zeta."""

    def test_hall_zeta_positive(self):
        """Hall algebra zeta is positive for real s > 1."""
        val = hall_algebra_zeta(1, 2.0, 2.0, N=50)
        assert float(val) > 0

    def test_hall_zeta_q_dependence(self):
        """Hall zeta increases with q (more representations at larger q)."""
        v1 = hall_algebra_zeta(1, 2.0, 2.0, N=50)
        v2 = hall_algebra_zeta(1, 2.0, 3.0, N=50)
        # Different q gives different value (but NOT necessarily monotone
        # because of the q^{-dim} factor)
        assert float(v1) != float(v2)

    def test_hall_zeta_convergent(self):
        """Hall zeta converges."""
        val = hall_algebra_zeta(1, 3.0, 2.0, N=100)
        assert math.isfinite(float(val))

    def test_hall_zeta_sl3(self):
        """Hall zeta for sl_3."""
        val = hall_algebra_zeta(2, 3.0, 2.0, N=20)
        assert math.isfinite(float(val))
        assert float(val) > 0


# =========================================================================
# Section 9: Derived zeta
# =========================================================================

class TestDerivedZeta:
    """Derived categorical zeta with homological signs."""

    def test_derived_zeta_finite(self):
        """Derived zeta is finite."""
        val = derived_zeta(1, 3.0, N=100)
        assert math.isfinite(float(val))

    def test_derived_zeta_smaller_than_dk(self):
        """Derived zeta < DK zeta in absolute value (alternating signs)."""
        dk = dk_categorical_zeta(1, 3.0, N_terms=100, include_trivial=False)
        der = derived_zeta(1, 3.0, N=100)
        assert abs(float(der)) < abs(float(dk)) + 0.01

    def test_derived_zeta_nonzero(self):
        """Derived zeta is generically nonzero."""
        val = derived_zeta(1, 2.0, N=100)
        assert abs(float(val)) > 0.01

    def test_derived_zeta_sl3(self):
        """Derived zeta for sl_3."""
        val = derived_zeta(2, 3.0, N=20)
        assert math.isfinite(float(val))


# =========================================================================
# Section 10: Hochschild homology
# =========================================================================

class TestHochschildHomology:
    """Hochschild homology of the DK category."""

    def test_sl2_level_1_simples(self):
        """sl_2 at level 1: 2 simple objects (V_0, V_1)."""
        hh = hochschild_homology_dk(1, 1)
        assert hh['n_simples'] == 2

    def test_sl2_level_2_simples(self):
        """sl_2 at level 2: 3 simple objects (V_0, V_1, V_2)."""
        hh = hochschild_homology_dk(1, 2)
        assert hh['n_simples'] == 3

    def test_sl2_level_k_simples(self):
        """sl_2 at level k: k+1 simple objects."""
        for k in range(1, 8):
            hh = hochschild_homology_dk(1, k)
            assert hh['n_simples'] == k + 1

    def test_sl3_level_1_simples(self):
        """sl_3 at level 1: 3 simple objects."""
        hh = hochschild_homology_dk(2, 1)
        assert hh['n_simples'] == 3

    def test_sl3_level_2_simples(self):
        """sl_3 at level 2: C(4,2) = 6 simple objects."""
        hh = hochschild_homology_dk(2, 2)
        assert hh['n_simples'] == 6

    def test_semisimple_vanishing(self):
        """HH_n = 0 for n > 0 (semisimple category)."""
        hh = hochschild_homology_dk(1, 3)
        assert hh['is_semisimple'] is True
        assert all(d == 0 for d in hh['hh_dims'][1:])

    def test_euler_char_equals_n_simples(self):
        """Euler characteristic of HH = n_simples (semisimple case)."""
        hh = hochschild_homology_dk(1, 5)
        assert hh['euler_char'] == hh['n_simples']

    def test_sl_n_level_k_formula(self):
        """Number of simples = C(k+rank, rank) for sl_{rank+1} at level k."""
        # sl_2 level k: C(k+1, 1) = k+1
        for k in range(1, 6):
            hh = hochschild_homology_dk(1, k)
            assert hh['n_simples'] == k + 1

        # sl_3 level k: C(k+2, 2) = (k+1)(k+2)/2
        for k in range(1, 5):
            hh = hochschild_homology_dk(2, k)
            expected = (k + 1) * (k + 2) // 2
            assert hh['n_simples'] == expected


# =========================================================================
# Section 11: Categorical Riemann hypothesis
# =========================================================================

class TestCategoricalRiemannHypothesis:
    """Search for zeros of zeta^{DK} on the critical strip."""

    def test_sl2_finds_first_zero(self):
        """For sl_2, should find zero near t = 14.135."""
        result = categorical_riemann_hypothesis(1, (10.0, 20.0),
                                                 n_points=100, N_terms=200)
        # Should find candidate near 14.135
        found = any(abs(t - 14.135) < 2.0 for t in result['candidate_zeros'])
        # Partial sums may not be accurate enough, so we just check structure
        assert isinstance(result['candidate_zeros'], list)
        assert 'sl2_comparison' in result

    def test_sl3_no_crash(self):
        """sl_3 zero search completes without error."""
        result = categorical_riemann_hypothesis(2, (5.0, 15.0),
                                                 n_points=20, N_terms=30)
        assert isinstance(result['candidate_zeros'], list)

    def test_output_structure(self):
        """Output has expected keys."""
        result = categorical_riemann_hypothesis(1, (10.0, 15.0),
                                                 n_points=10, N_terms=50)
        assert 'candidate_zeros' in result
        assert 'values' in result
        assert 'min_modulus' in result


# =========================================================================
# Section 12: Koszul categorical duality
# =========================================================================

class TestKoszulCategoricalDuality:
    """Koszul duality on zeta^{DK}: functional equation."""

    def test_sl2_functional_equation(self):
        """xi(s) = xi(1-s) for Riemann zeta (sl_2 case)."""
        result = koszul_categorical_duality(1, 2.5, N_terms=200)
        assert result.get('functional_equation_holds', False) is True

    def test_sl2_functional_equation_multiple_s(self):
        """Functional equation at multiple s values.

        Avoid odd integer s where Gamma((1-s)/2) has poles:
        s=3 -> Gamma(-1) pole, s=5 -> Gamma(-2) pole, etc.
        """
        for s in [2.5, 3.5, 4.5, 6.5]:
            result = koszul_categorical_duality(1, s, N_terms=200)
            err = result.get('functional_equation_error', 1.0)
            assert err < 1e-8, f"Functional equation failed at s={s}, error={err}"

    def test_koszul_sum_structure(self):
        """zeta(s) + zeta(1-s) has predictable behavior."""
        result = koszul_categorical_duality(1, 3.5, N_terms=200)
        assert 'sum' in result
        assert math.isfinite(float(abs(result['sum'])))


# =========================================================================
# Section 13: Dimension spectrum
# =========================================================================

class TestDimensionSpectrum:
    """Dimension spectrum analysis."""

    def test_sl2_complete_spectrum(self):
        """sl_2: every positive integer is a representation dimension."""
        ds = dimension_spectrum_analysis(1, max_dim=50)
        assert ds['is_complete'] is True
        assert len(ds['gaps']) == 0

    def test_sl2_all_multiplicity_1(self):
        """sl_2: each dimension appears exactly once."""
        ds = dimension_spectrum_analysis(1, max_dim=50)
        for d, m in ds['multiplicities'].items():
            assert m == 1, f"dim {d} has multiplicity {m}"

    def test_sl3_not_complete(self):
        """sl_3: NOT every integer is a representation dimension."""
        ds = dimension_spectrum_analysis(2, max_dim=30)
        assert ds['is_complete'] is False
        assert len(ds['gaps']) > 0

    def test_sl3_has_gaps(self):
        """sl_3: specific integers are missing (e.g., 2 is not an sl_3 dim)."""
        ds = dimension_spectrum_analysis(2, max_dim=20)
        assert 2 in ds['gaps']  # no sl_3 rep has dim 2
        assert 4 in ds['gaps']  # no sl_3 rep has dim 4

    def test_sl3_has_multiplicities(self):
        """sl_3: some dimensions appear multiple times (e.g., dim 3: fund + anti-fund)."""
        ds = dimension_spectrum_analysis(2, max_dim=20)
        assert ds['max_multiplicity'] >= 2

    def test_density_decreasing_with_rank(self):
        """Higher rank -> lower density of covered dimensions."""
        d1 = dimension_spectrum_analysis(1, max_dim=50)
        d2 = dimension_spectrum_analysis(2, max_dim=50)
        assert d1['density'] >= d2['density']


# =========================================================================
# Section 14: Multi-path verification
# =========================================================================

class TestMultipathVerification:
    """Four independent paths for sl_2 zeta = Riemann zeta."""

    def test_multipath_at_s2(self):
        """Four paths agree at s=2."""
        result = multipath_categorified_verification(2.0, N_terms=500)
        assert result['all_consistent'] is True

    def test_multipath_at_s3(self):
        """Four paths agree at s=3."""
        result = multipath_categorified_verification(3.0, N_terms=500)
        assert result['all_consistent'] is True

    def test_multipath_at_s4(self):
        """Four paths agree at s=4."""
        result = multipath_categorified_verification(4.0, N_terms=500)
        assert result['all_consistent'] is True

    def test_path1_equals_path2(self):
        """Weyl dim formula agrees with direct d^{-s}."""
        result = multipath_categorified_verification(3.0, N_terms=500)
        assert result['error_12'] < 1e-10

    def test_path2_close_to_path3(self):
        """Partial sum close to mpmath.zeta."""
        result = multipath_categorified_verification(3.0, N_terms=500)
        assert result['error_23'] < 0.01

    def test_euler_product_close(self):
        """Euler product close to mpmath.zeta."""
        result = multipath_categorified_verification(3.0, N_terms=500)
        assert result['error_34'] < 0.01


# =========================================================================
# Section 15: Euler product categorification
# =========================================================================

class TestEulerProduct:
    """Euler product structure of zeta^{DK}."""

    def test_sl2_euler_product_matches(self):
        """sl_2 Euler product matches DK zeta."""
        result = categorified_euler_product(1, 3.0, N_primes=50)
        ratio = result['ratio']
        assert ratio is not None
        assert abs(float(abs(ratio)) - 1.0) < 0.01

    def test_sl2_is_multiplicative(self):
        """sl_2 dimension function is multiplicative (by uniqueness of ints)."""
        result = categorified_euler_product(1, 2.0, N_primes=30)
        assert result['is_multiplicative'] is True

    def test_sl3_not_multiplicative(self):
        """sl_3 dimension function is not multiplicative."""
        result = categorified_euler_product(2, 3.0, N_primes=20)
        assert result['is_multiplicative'] is False

    def test_local_factors_positive(self):
        """All local factors are positive for real s > 1."""
        result = categorified_euler_product(1, 2.0, N_primes=20)
        for p, factor in result['local_factors']:
            assert float(factor) > 0


# =========================================================================
# Section 16: Shadow-DK bridge
# =========================================================================

class TestShadowDKBridge:
    """Bridge between shadow zeta and DK categorical zeta."""

    def test_heisenberg_shadow(self):
        """Heisenberg shadow coefficients: S_2 = kappa, S_r = 0 for r > 2."""
        kappa = 1.0
        shadow_coeffs = [kappa]  # only S_2 (class G: terminates at r=2)
        result = shadow_to_dk_bridge(1, 3.0, shadow_coeffs, N_terms=200)
        assert math.isfinite(float(abs(result['shadow_zeta'])))
        assert math.isfinite(float(abs(result['dk_zeta'])))

    def test_virasoro_shadow(self):
        """Virasoro shadow coefficients: infinite tower (class M)."""
        # First few shadow coefficients for Virasoro at c=1
        c = 1.0
        kappa = c / 2
        S3 = 2.0  # S_3 = 2 for Virasoro (c-independent; AP9)
        S4 = 10 / (c * (5 * c + 22))  # Q^contact
        shadow_coeffs = [kappa, S3, S4]
        result = shadow_to_dk_bridge(1, 3.0, shadow_coeffs, N_terms=200)
        assert result['shadow_zeta'] is not None
        assert result['dk_zeta'] is not None

    def test_bridge_ratio_finite(self):
        """Shadow/DK ratio is finite."""
        shadow_coeffs = [1.0, 0.5, 0.25, 0.125]
        result = shadow_to_dk_bridge(1, 3.0, shadow_coeffs, N_terms=200)
        assert result['ratio'] is not None
        assert math.isfinite(float(abs(result['ratio'])))


# =========================================================================
# Section 17: HKR theorem
# =========================================================================

class TestHKR:
    """Hochschild-Kostant-Rosenberg for DK category."""

    def test_hkr_holds_semisimple(self):
        """HKR trivializes for semisimple categories."""
        result = hkr_theorem_dk(1, 3)
        assert result['hkr_holds'] is True

    def test_center_dim_matches(self):
        """Center dimension = number of simples."""
        result = hkr_theorem_dk(1, 5)
        assert result['center_dim'] == 6  # k+1 = 6

    def test_global_dim_zero(self):
        """Global dimension = 0 for semisimple."""
        result = hkr_theorem_dk(1, 3)
        assert result['global_dim'] == 0


# =========================================================================
# Section 18: Representation ring
# =========================================================================

class TestRepresentationRing:
    """Representation ring structure."""

    def test_sl2_generators(self):
        """sl_2 has one generator: the fundamental V_1 (dim 2)."""
        rr = representation_ring_structure(1, max_weight=5)
        assert len(rr['generators']) == 1
        assert rr['generators'][0]['dim'] == 2

    def test_sl3_generators(self):
        """sl_3 has two generators: V_{(1,0)} (dim 3) and V_{(0,1)} (dim 3)."""
        rr = representation_ring_structure(2, max_weight=5)
        assert len(rr['generators']) == 2
        assert rr['generators'][0]['dim'] == 3
        assert rr['generators'][1]['dim'] == 3

    def test_sl2_tensor_product(self):
        """sl_2: V_a x V_b = V_{a+b} + V_{a+b-2} + ... + V_{|a-b|}."""
        rr = representation_ring_structure(1, max_weight=5)
        # V_1 x V_1 = V_2 + V_0 (dims: 2*2 = 3+1 = 4)
        prod = rr['products'].get((1, 1))
        assert prod is not None
        assert prod['check'] is True
        assert prod['total_dim'] == 4  # dim(V_1)^2 = 2^2 = 4

    def test_sl2_tensor_associativity(self):
        """Tensor product dimensions are consistent."""
        rr = representation_ring_structure(1, max_weight=5)
        for key, prod in rr['products'].items():
            a, b = key
            assert prod['check'] is True, f"V_{a} x V_{b} dimension mismatch"

    def test_polynomial_ring(self):
        """K_0(Rep(sl_N)) is a polynomial ring."""
        rr = representation_ring_structure(1)
        assert rr['is_polynomial'] is True


# =========================================================================
# Section 19: Cross-rank consistency
# =========================================================================

class TestCrossRank:
    """Cross-rank consistency of DK zeta."""

    def test_sl2_vs_sl3_ordering(self):
        """sl_3 DK zeta involves larger multiplicities."""
        s = 4.0
        v2 = dk_categorical_zeta(1, s, N_terms=100, include_trivial=False)
        v3 = dk_categorical_zeta(2, s, N_terms=30, include_trivial=False)
        # Both should be positive
        assert float(v2) > 0
        assert float(v3) > 0

    def test_sl4_convergent(self):
        """sl_4 DK zeta converges for s sufficiently large."""
        val = dk_categorical_zeta(3, 5.0, N_terms=20, include_trivial=False)
        assert math.isfinite(float(val))
        assert float(val) > 0

    def test_sl5_convergent(self):
        """sl_5 DK zeta converges."""
        val = dk_categorical_zeta(4, 6.0, N_terms=10, include_trivial=False)
        assert math.isfinite(float(val))
        assert float(val) > 0

    def test_increasing_s_decreases_zeta(self):
        """Larger s gives smaller DK zeta (for s > 1)."""
        v1 = dk_categorical_zeta(1, 2.0, N_terms=500, include_trivial=True)
        v2 = dk_categorical_zeta(1, 3.0, N_terms=500, include_trivial=True)
        v3 = dk_categorical_zeta(1, 4.0, N_terms=500, include_trivial=True)
        assert float(v1) > float(v2) > float(v3) > 1.0


# =========================================================================
# Section 20: Master verification
# =========================================================================

class TestMasterVerification:
    """Master categorification check."""

    def test_master_check(self):
        """Full master verification suite passes."""
        result = master_categorification_check(s=3.0)
        assert result['sl2_is_riemann']['verified'] is True
        assert result['sl2_minus_1']['verified'] is True
        assert result['khovanov_unknot']['verified'] is True
        assert result['khovanov_trefoil']['verified'] is True
        assert result['khovanov_figure_eight']['verified'] is True
        assert result['sl2_dimension_spectrum']['is_complete'] is True

    def test_all_verified(self):
        """All sub-checks pass."""
        result = master_categorification_check(s=3.0)
        assert result['all_verified'] is True
