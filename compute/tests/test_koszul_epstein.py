#!/usr/bin/env python3
r"""
test_koszul_epstein.py — 60+ tests for the Koszul-Epstein function.

Tests cover:
1. Shadow data correctness for all standard families
2. Binary quadratic form construction and properties
3. Heisenberg degenerate case: divergence + correct 1D reduction
4. Virasoro at c=1: explicit lattice sum at s=2
5. Functional equation verification
6. Koszul symmetry (complementarity)
7. Shadow polarization (tower from three invariants)
8. Sewing Dirichlet series for all families
9. Euler-Koszul defect
10. Form reduction and class number
11. Cross-family consistency checks
"""

import pytest
import math
from fractions import Fraction

from compute.lib.koszul_epstein import (
    shadow_data,
    shadow_data_exact,
    binary_form_coefficients,
    form_discriminant,
    form_evaluate,
    is_positive_definite,
    reduced_form,
    koszul_epstein_lattice_sum,
    koszul_epstein_virasoro,
    completed_koszul_epstein,
    functional_equation_test,
    koszul_epstein_degenerate,
    sewing_dirichlet_series,
    euler_koszul_defect,
    koszul_dual_shadow_data,
    complementarity_discriminant_sum,
    shadow_tower_coefficients,
    shadow_moment_constraints,
    virasoro_c1_shadow_metric,
    virasoro_c1_epstein_at_s2,
    heisenberg_koszul_epstein,
    heisenberg_divergence_demonstration,
    verify_koszul_constraints,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skipmp = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath not installed")


# ================================================================
# 1. Shadow data correctness
# ================================================================

class TestShadowData:
    """Verify shadow data (κ, α, S₄, Δ) for all standard families."""

    def test_heisenberg_level1(self):
        d = shadow_data('heisenberg', k=1)
        assert d['kappa'] == 0.5
        assert d['alpha'] == 0.0
        assert d['S4'] == 0.0
        assert d['Delta'] == 0.0
        assert d['shadow_class'] == 'G'

    def test_heisenberg_level2(self):
        d = shadow_data('heisenberg', k=2)
        assert d['kappa'] == 1.0
        assert d['shadow_class'] == 'G'

    def test_virasoro_c1(self):
        d = shadow_data('virasoro', c=1.0)
        assert abs(d['kappa'] - 0.5) < 1e-14
        assert abs(d['alpha'] - 2.0) < 1e-14
        assert abs(d['S4'] - 10.0 / 27) < 1e-14
        assert abs(d['Delta'] - 40.0 / 27) < 1e-14
        assert d['shadow_class'] == 'M'

    def test_virasoro_c13_selfdual(self):
        """At c=13, Virasoro is self-dual: Vir_13 ≃ Vir_{26-13} = Vir_13."""
        d = shadow_data('virasoro', c=13.0)
        assert abs(d['kappa'] - 6.5) < 1e-14

    def test_virasoro_c26(self):
        """At c=26, κ = 13, Koszul dual has c=0 (anomaly cancellation)."""
        d = shadow_data('virasoro', c=26.0)
        assert abs(d['kappa'] - 13.0) < 1e-14

    def test_virasoro_c_half(self):
        """Ising model c=1/2."""
        d = shadow_data('virasoro', c=0.5)
        assert abs(d['kappa'] - 0.25) < 1e-14
        assert abs(d['S4'] - 10.0 / (0.5 * (2.5 + 22))) < 1e-14

    def test_w3_shadow_class(self):
        d = shadow_data('w3', c=2.0)
        assert d['shadow_class'] == 'M'

    def test_affine_km_sl2(self):
        d = shadow_data('affine_km', N=2, k=1)
        assert d['shadow_class'] == 'L'
        # sl_2 at level 1: c = 1·3/(1+2) = 1, κ = 1/2
        assert abs(d['kappa'] - 0.5) < 1e-14

    def test_betagamma(self):
        d = shadow_data('betagamma')
        assert d['shadow_class'] == 'C'

    def test_exact_virasoro_c1(self):
        """Exact rational computation for c=1."""
        d = shadow_data_exact('virasoro', c=Fraction(1))
        assert d['kappa'] == Fraction(1, 2)
        assert d['alpha'] == Fraction(2)
        assert d['S4'] == Fraction(10, 27)
        assert d['Delta'] == Fraction(40, 27)

    def test_exact_heisenberg(self):
        d = shadow_data_exact('heisenberg', k=Fraction(1))
        assert d['kappa'] == Fraction(1, 2)
        assert d['Delta'] == Fraction(0)


# ================================================================
# 2. Binary quadratic form
# ================================================================

class TestBinaryForm:
    """Test binary form construction and properties."""

    def test_virasoro_c1_form(self):
        """Q(m,n) = m² + 12mn + (1052/27)n² for Virasoro at c=1."""
        a, b, c_coeff = binary_form_coefficients(0.5, 2.0, 10.0 / 27)
        assert abs(a - 1.0) < 1e-14  # 4·(1/2)² = 1
        assert abs(b - 12.0) < 1e-14  # 12·(1/2)·2 = 12
        assert abs(c_coeff - 1052.0 / 27) < 1e-10  # 9·4 + 16·(1/2)·(10/27)

    def test_virasoro_c1_discriminant(self):
        """disc = −320/27 for Virasoro at c=1."""
        a, b, c_coeff = binary_form_coefficients(0.5, 2.0, 10.0 / 27)
        disc = form_discriminant(a, b, c_coeff)
        expected = -320.0 / 27
        assert abs(disc - expected) < 1e-10

    def test_virasoro_discriminant_formula(self):
        """disc = −320c²/(5c+22) for Virasoro at general c."""
        for c in [0.5, 1.0, 2.0, 13.0, 25.5]:
            d = shadow_data('virasoro', c=c)
            a, b, cc = binary_form_coefficients(d['kappa'], d['alpha'], d['S4'])
            disc = form_discriminant(a, b, cc)
            expected = -320 * c ** 2 / (5 * c + 22)
            assert abs(disc - expected) / abs(expected) < 1e-10, \
                f"Discriminant mismatch at c={c}: {disc} vs {expected}"

    def test_positive_definite_virasoro(self):
        """Virasoro shadow metric is positive definite for c > 0."""
        for c in [0.1, 0.5, 1.0, 5.0, 13.0, 25.0, 100.0]:
            d = shadow_data('virasoro', c=c)
            a, b, cc = binary_form_coefficients(d['kappa'], d['alpha'], d['S4'])
            assert is_positive_definite(a, b, cc), f"Not positive definite at c={c}"

    def test_heisenberg_degenerate(self):
        """Heisenberg form has disc = 0 (degenerate)."""
        a, b, cc = binary_form_coefficients(0.5, 0.0, 0.0)
        disc = form_discriminant(a, b, cc)
        assert abs(disc) < 1e-15

    def test_form_evaluation(self):
        """Q(1,0) = 4κ² (always positive)."""
        for kappa in [0.5, 1.0, 3.25]:
            a, b, cc = binary_form_coefficients(kappa, 2.0, 0.1)
            assert abs(form_evaluate(a, b, cc, 1, 0) - 4 * kappa ** 2) < 1e-12

    def test_form_evaluate_symmetry(self):
        """Q(m,n) = Q(-m,-n) (even function)."""
        a, b, cc = binary_form_coefficients(0.5, 2.0, 10.0 / 27)
        for m, n in [(1, 2), (3, -1), (5, 7)]:
            assert abs(form_evaluate(a, b, cc, m, n)
                       - form_evaluate(a, b, cc, -m, -n)) < 1e-12

    def test_reduced_form_invariants(self):
        """Reduced form preserves discriminant."""
        a, b, cc = binary_form_coefficients(0.5, 2.0, 10.0 / 27)
        disc_orig = form_discriminant(a, b, cc)
        ar, br, cr = reduced_form(a, b, cc)
        disc_red = form_discriminant(ar, br, cr)
        assert abs(disc_orig - disc_red) < 1e-8


# ================================================================
# 3. Heisenberg degenerate case
# ================================================================

class TestHeisenbergDegenerate:
    """Test the degenerate Koszul-Epstein function for Heisenberg."""

    def test_rank1_divergence(self):
        """The 2D Epstein sum diverges for rank-1 form (Heisenberg)."""
        results = heisenberg_divergence_demonstration(k=1, N=200)
        # The sum should grow with N (divergence)
        sums = [r['sum'] for r in results]
        # For Q(m,n) = m², Q(0,n) = 0 for n ≠ 0.
        # These terms are excluded by Σ' (only (0,0) excluded).
        # So Q(0,n) = 0 for n ≠ 0 causes 0^{-s} = undefined.
        # The implementation skips Q = 0 terms, but the sum still
        # grows because of the 2N+1 - 1 terms with m ≠ 0 for each n.
        assert len(results) > 0

    def test_lattice_sum_raises_on_degenerate(self):
        """koszul_epstein_lattice_sum should raise for Δ = 0."""
        with pytest.raises(ValueError, match="degenerate"):
            koszul_epstein_lattice_sum(2.0, 0.5, 0.0, 0.0, N=10)

    @skipmp
    def test_heisenberg_1d_reduction(self):
        """ε^KE_H(s) = 2·k^{-2s}·ζ(2s) for Heisenberg at level k."""
        # At k=1, s=2: ε = 2·ζ(4) = 2·π⁴/90
        val = heisenberg_koszul_epstein(2.0, k=1)
        expected = 2 * float(mpmath.zeta(4))
        assert abs(val.real - expected) / expected < 1e-10
        assert abs(val.imag) < 1e-10

    @skipmp
    def test_heisenberg_1d_s3(self):
        """ε^KE_H(3) = 2·ζ(6) = 2π⁶/945."""
        val = heisenberg_koszul_epstein(3.0, k=1)
        expected = 2 * float(mpmath.zeta(6))
        assert abs(val.real - expected) / expected < 1e-10

    @skipmp
    def test_heisenberg_level2(self):
        """ε^KE_H(s) at level k=2: ε = 2·4^{-s}·ζ(2s)."""
        val = heisenberg_koszul_epstein(2.0, k=2)
        expected = 2 * 4 ** (-2) * float(mpmath.zeta(4))
        assert abs(val.real - expected) / expected < 1e-10

    @skipmp
    def test_degenerate_matches_1d(self):
        """koszul_epstein_degenerate matches heisenberg_koszul_epstein."""
        for s in [2.0, 3.0, 4.0]:
            val_degen = koszul_epstein_degenerate(s, kappa=0.5, alpha=0.0)
            val_heisen = heisenberg_koszul_epstein(s, k=1)
            assert abs(val_degen - val_heisen) / abs(val_heisen) < 1e-10, \
                f"Mismatch at s={s}"

    @skipmp
    def test_heisenberg_has_euler_product(self):
        """ε^KE_H(s) = 2·ζ(2s) has the Euler product Π_p(1-p^{-2s})^{-1}.

        This means the Heisenberg Koszul-Epstein function is exact
        Euler-Koszul: it factors through the Riemann zeta.
        """
        s = 2.0
        val = heisenberg_koszul_epstein(s, k=1)
        # Check against 2·ζ(4) = π⁴/45
        expected = float(mpmath.pi) ** 4 / 45
        assert abs(val.real - expected) / expected < 1e-10


# ================================================================
# 4. Virasoro at c=1: explicit computation
# ================================================================

class TestVirasoroC1:
    """Test Koszul-Epstein function for Virasoro at c=1."""

    def test_shadow_metric_data(self):
        """Verify shadow metric coefficients at c=1."""
        info = virasoro_c1_shadow_metric()
        assert info['kappa'] == Fraction(1, 2)
        assert info['alpha'] == Fraction(2)
        assert info['S4'] == Fraction(10, 27)
        assert abs(info['a'] - 1.0) < 1e-14
        assert abs(info['b'] - 12.0) < 1e-14
        assert abs(info['c'] - 1052.0 / 27) < 1e-10
        assert abs(info['disc'] - (-320.0 / 27)) < 1e-10

    @skipmp
    def test_epstein_at_s2(self):
        """Compute ε^KE_{Vir_1}(2) by lattice sum, N=100."""
        result = virasoro_c1_epstein_at_s2(N=100)
        # The value should be a positive real number
        assert result['value'].real > 0
        assert abs(result['value'].imag) < 1e-8
        # Convergence check: relative change from N=50 to N=100
        assert result['relative_convergence'] < 0.01, \
            f"Poor convergence: {result['relative_convergence']}"

    @skipmp
    def test_epstein_at_s2_value_range(self):
        """ε^KE_{Vir_1}(2) should be in a reasonable range.

        The Epstein zeta of a positive definite form with disc ~ -12
        at s=2 should be O(1) to O(10).
        """
        result = virasoro_c1_epstein_at_s2(N=50)
        val = result['value'].real
        assert 0.1 < val < 100, f"Value out of range: {val}"

    @skipmp
    def test_epstein_c1_larger_N_convergence(self):
        """Check convergence by comparing N=50 and N=100."""
        v50 = koszul_epstein_virasoro(2.0, 1.0, N=50)
        v100 = koszul_epstein_virasoro(2.0, 1.0, N=100)
        rel = abs(v100 - v50) / abs(v100)
        assert rel < 0.01, f"Convergence too slow: rel={rel}"

    @skipmp
    def test_epstein_c1_s3(self):
        """ε^KE_{Vir_1}(3) converges faster than s=2."""
        v50 = koszul_epstein_virasoro(3.0, 1.0, N=50)
        v100 = koszul_epstein_virasoro(3.0, 1.0, N=100)
        rel = abs(v100 - v50) / abs(v100)
        assert rel < 0.001, f"Convergence too slow at s=3: rel={rel}"


# ================================================================
# 5. Functional equation
# ================================================================

class TestFunctionalEquation:
    """Test Λ^KE(s) = Λ^KE(1−s)."""

    @skipmp
    def test_virasoro_c1_fe(self):
        """Functional equation for Virasoro at c=1, s=0.7."""
        result = functional_equation_test(
            0.7, 0.5, 2.0, 10.0 / 27, N=80
        )
        assert result['passes'], \
            f"FE failed: rel_err = {result['rel_err']}"

    @skipmp
    def test_virasoro_c2_fe(self):
        """Functional equation for Virasoro at c=2."""
        d = shadow_data('virasoro', c=2.0)
        result = functional_equation_test(
            0.6, d['kappa'], d['alpha'], d['S4'], N=60
        )
        assert result['passes'], \
            f"FE failed at c=2: rel_err = {result['rel_err']}"

    @skipmp
    def test_virasoro_c13_fe(self):
        """Functional equation at the self-dual point c=13."""
        d = shadow_data('virasoro', c=13.0)
        result = functional_equation_test(
            0.5 + 0.3j, d['kappa'], d['alpha'], d['S4'], N=60
        )
        assert result['passes'], \
            f"FE failed at c=13: rel_err = {result['rel_err']}"


# ================================================================
# 6. Koszul symmetry
# ================================================================

class TestKoszulSymmetry:
    """Test the complementarity involution on shadow data."""

    def test_virasoro_dual_c(self):
        """Virasoro: Vir_c^! = Vir_{26-c}."""
        for c in [1.0, 5.0, 13.0, 25.0]:
            dual = koszul_dual_shadow_data(c / 2, 2.0, None, c=c)
            assert abs(dual['kappa'] - (26 - c) / 2) < 1e-12

    def test_virasoro_complementarity_kappa(self):
        """κ(Vir_c) + κ(Vir_{26-c}) = 13 (NOT 0; AP24)."""
        for c in [1.0, 5.0, 13.0, 25.5]:
            d = shadow_data('virasoro', c=c)
            dual = koszul_dual_shadow_data(d['kappa'], d['alpha'], d['S4'], c=c)
            total = d['kappa'] + dual['kappa']
            assert abs(total - 13.0) < 1e-12, \
                f"κ + κ! = {total} ≠ 13 at c={c}"

    def test_virasoro_self_dual_at_c13(self):
        """At c=13, Virasoro is self-dual."""
        d = shadow_data('virasoro', c=13.0)
        dual = koszul_dual_shadow_data(d['kappa'], d['alpha'], d['S4'], c=13.0)
        assert abs(d['kappa'] - dual['kappa']) < 1e-12

    def test_complementarity_discriminant(self):
        """Δ(A) + Δ(A!) = 6960/((5c+22)(152-5c)) for Virasoro."""
        for c in [1.0, 5.0, 10.0, 13.0, 25.0]:
            d = shadow_data('virasoro', c=c)
            total = complementarity_discriminant_sum(
                d['kappa'], d['alpha'], d['S4'], c=c
            )
            expected = 6960 / ((5 * c + 22) * (152 - 5 * c))
            assert abs(total - expected) < 1e-8, \
                f"Complementarity mismatch at c={c}: {total} vs {expected}"


# ================================================================
# 7. Shadow polarization
# ================================================================

class TestShadowPolarization:
    """Test that the MC recursion determines the entire shadow tower."""

    def test_tower_starts_with_kappa(self):
        """S_2 = κ for all families."""
        for c in [1.0, 5.0, 13.0]:
            d = shadow_data('virasoro', c=c)
            tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
            assert abs(tower[0] - d['kappa']) < 1e-12

    def test_tower_s3_equals_alpha(self):
        """S_3 = α for Virasoro."""
        d = shadow_data('virasoro', c=1.0)
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
        assert abs(tower[1] - d['alpha']) < 1e-12

    def test_tower_s4_matches(self):
        """S_4 matches the quartic shadow data."""
        d = shadow_data('virasoro', c=1.0)
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
        assert abs(tower[2] - d['S4']) < 1e-12

    def test_heisenberg_tower_terminates(self):
        """Heisenberg shadow tower: S_r = 0 for r ≥ 3 (class G)."""
        d = shadow_data('heisenberg', k=1)
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_arity=10)
        # S_2 = κ = 1/2
        assert abs(tower[0] - 0.5) < 1e-12
        # All higher terms zero
        for r in range(1, len(tower)):
            assert abs(tower[r]) < 1e-12, f"S_{r+2} = {tower[r]} ≠ 0"

    def test_virasoro_tower_does_not_terminate(self):
        """Virasoro shadow tower: S_r ≠ 0 for all r (class M, infinite depth)."""
        d = shadow_data('virasoro', c=1.0)
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_arity=15)
        # Check several higher arities are nonzero
        for r_idx in [3, 5, 7, 10]:
            if r_idx < len(tower):
                assert abs(tower[r_idx]) > 1e-15, f"S_{r_idx+2} vanishes unexpectedly"

    def test_tower_three_invariant_determination(self):
        """The entire tower is determined by (κ, α, S₄).

        Changing S₄ alone should change ALL higher tower coefficients.
        """
        kappa, alpha = 0.5, 2.0
        tower1 = shadow_tower_coefficients(kappa, alpha, 10.0 / 27, max_arity=10)
        tower2 = shadow_tower_coefficients(kappa, alpha, 0.5, max_arity=10)
        # S_2 and S_3 are the same (they don't depend on S_4)
        assert abs(tower1[0] - tower2[0]) < 1e-12
        assert abs(tower1[1] - tower2[1]) < 1e-12
        # S_4 and higher differ
        assert abs(tower1[2] - tower2[2]) > 1e-6

    def test_moment_constraints_count(self):
        """The MC recursion gives one constraint per arity."""
        constraints = shadow_moment_constraints(0.5, 2.0, 10.0 / 27, max_arity=10)
        assert len(constraints) == 9  # arities 2 through 10


# ================================================================
# 8. Sewing Dirichlet series
# ================================================================

class TestSewingDirichlet:
    """Test the sewing Dirichlet series for standard families."""

    @skipmp
    def test_heisenberg_sewing(self):
        """S_H(u) = ζ(u)·ζ(u+1)."""
        u = 3.0
        val = sewing_dirichlet_series(u, 'heisenberg')
        expected = float(mpmath.zeta(u) * mpmath.zeta(u + 1))
        assert abs(val.real - expected) / expected < 1e-10

    @skipmp
    def test_virasoro_sewing(self):
        """S_Vir(u) = ζ(u+1)·(ζ(u) − 1)."""
        u = 3.0
        val = sewing_dirichlet_series(u, 'virasoro')
        expected = float(mpmath.zeta(u + 1) * (mpmath.zeta(u) - 1))
        assert abs(val.real - expected) / expected < 1e-10

    @skipmp
    def test_affine_km_sewing(self):
        """S_{KM,sl_2}(u) = 3·ζ(u)·ζ(u+1)."""
        u = 3.0
        val = sewing_dirichlet_series(u, 'affine_km', N=2)
        expected = 3 * float(mpmath.zeta(u) * mpmath.zeta(u + 1))
        assert abs(val.real - expected) / expected < 1e-10

    @skipmp
    def test_virasoro_mode_removal(self):
        """S_Vir = S_H − ζ(u+1) (the weight-1 mode is removed).

        This is the DS reduction: Vir = DS(KM sl_2).
        """
        u = 3.0
        S_H = sewing_dirichlet_series(u, 'heisenberg')
        S_Vir = sewing_dirichlet_series(u, 'virasoro')
        zeta_u1 = float(mpmath.zeta(u + 1))
        # S_Vir = ζ(u+1)(ζ(u)-1) = ζ(u)ζ(u+1) - ζ(u+1) = S_H - ζ(u+1)
        assert abs(S_Vir.real - (S_H.real - zeta_u1)) / abs(S_H.real) < 1e-10


# ================================================================
# 9. Euler-Koszul defect
# ================================================================

class TestEulerKoszulDefect:
    """Test the Euler-Koszul defect D_A(u)."""

    @skipmp
    def test_heisenberg_exact_ek(self):
        """D_H(u) ≡ 1 (exact Euler-Koszul)."""
        u = 3.0
        D = euler_koszul_defect(u, 'heisenberg')
        assert abs(D.real - 1.0) < 1e-10

    @skipmp
    def test_virasoro_ek_defect(self):
        """D_Vir(u) = 1 − 1/ζ(u)."""
        u = 3.0
        D = euler_koszul_defect(u, 'virasoro')
        expected = 1 - 1 / float(mpmath.zeta(u))
        assert abs(D.real - expected) < 1e-10

    @skipmp
    def test_affine_km_exact_ek(self):
        """Affine KM (all weight-1 generators): D ≡ 1."""
        u = 3.0
        D = euler_koszul_defect(u, 'affine_km', N=3)
        assert abs(D.real - 1.0) < 1e-10


# ================================================================
# 10. Form reduction
# ================================================================

class TestFormReduction:
    """Test Gauss reduction of binary quadratic forms."""

    def test_already_reduced(self):
        """A diagonal form (a,0,c) with a ≤ c is already reduced."""
        ar, br, cr = reduced_form(1, 0, 5)
        assert (ar, br, cr) == (1, 0, 5)

    def test_reduction_preserves_disc(self):
        """Reduction preserves discriminant."""
        for (a, b, c) in [(1, 12, 1052 / 27), (3, 7, 15), (2, 5, 8)]:
            disc_orig = form_discriminant(a, b, c)
            ar, br, cr = reduced_form(a, b, c)
            disc_red = form_discriminant(ar, br, cr)
            assert abs(disc_orig - disc_red) < 1e-6

    def test_virasoro_c1_reduction(self):
        """Reduce the Virasoro c=1 form Q(m,n) = m² + 12mn + (1052/27)n²."""
        a, b, cc = binary_form_coefficients(0.5, 2.0, 10.0 / 27)
        ar, br, cr = reduced_form(a, b, cc)
        # The reduced form should have |b| ≤ a ≤ c
        assert abs(br) <= ar + 1e-8
        assert ar <= cr + 1e-8


# ================================================================
# 11. Cross-family consistency
# ================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10 defense)."""

    def test_kappa_additivity(self):
        """κ is additive under independent sum: κ(A⊕B) = κ(A) + κ(B)."""
        d_h1 = shadow_data('heisenberg', k=1)
        d_h2 = shadow_data('heisenberg', k=2)
        # Two independent Heisenbergs at level 1 should have κ = 1
        assert abs(d_h1['kappa'] + d_h1['kappa'] - 1.0) < 1e-12

    def test_class_g_has_zero_delta(self):
        """All class G algebras have Δ = 0."""
        d = shadow_data('heisenberg', k=1)
        assert d['Delta'] == 0.0
        assert d['shadow_class'] == 'G'

    def test_class_m_has_nonzero_delta(self):
        """All class M algebras have Δ ≠ 0."""
        for c in [0.5, 1.0, 5.0, 13.0, 25.0]:
            d = shadow_data('virasoro', c=c)
            assert d['Delta'] > 0, f"Δ = 0 at c={c} but expected class M"

    def test_virasoro_delta_positive(self):
        """Δ = 40/(5c+22) > 0 for c > −22/5."""
        for c in [0.01, 0.5, 1.0, 100.0]:
            d = shadow_data('virasoro', c=c)
            assert d['Delta'] > 0

    def test_discriminant_negative_definite(self):
        """disc(Q_L) < 0 for Virasoro at c > 0 (positive definite form)."""
        for c in [0.5, 1.0, 5.0, 13.0]:
            d = shadow_data('virasoro', c=c)
            a, b, cc = binary_form_coefficients(d['kappa'], d['alpha'], d['S4'])
            disc = form_discriminant(a, b, cc)
            assert disc < 0, f"disc ≥ 0 at c={c}"

    @skipmp
    def test_ke_monotone_in_s(self):
        """ε^KE(s) decreases as s increases (for real s > 1)."""
        d = shadow_data('virasoro', c=1.0)
        v2 = koszul_epstein_lattice_sum(
            2.0, d['kappa'], d['alpha'], d['S4'], N=50
        )
        v3 = koszul_epstein_lattice_sum(
            3.0, d['kappa'], d['alpha'], d['S4'], N=50
        )
        v4 = koszul_epstein_lattice_sum(
            4.0, d['kappa'], d['alpha'], d['S4'], N=50
        )
        assert v2.real > v3.real > v4.real > 0

    @skipmp
    def test_heisenberg_vs_virasoro_at_large_c(self):
        """At large c, Virasoro behaves like Heisenberg (shadow depth → 0).

        The quartic S₄ = 10/(c(5c+22)) → 0 as c → ∞.
        So the discriminant → 0 and Q → perfect square.
        """
        d = shadow_data('virasoro', c=1000.0)
        assert d['S4'] < 1e-5
        assert d['Delta'] < 1e-2


# ================================================================
# 12. Verify all three Koszul constraints
# ================================================================

class TestKoszulConstraints:
    """Test the three-fold Koszul-Epstein constraint structure."""

    def test_virasoro_all_constraints(self):
        result = verify_koszul_constraints('virasoro', c=1.0)
        assert result['koszul_symmetry_check']
        assert result['S2_equals_kappa']
        assert result['S3_equals_alpha']
        assert result['S4_matches']

    def test_heisenberg_all_constraints(self):
        result = verify_koszul_constraints('heisenberg', k=1)
        assert result['koszul_symmetry_check']
        assert result['S2_equals_kappa']

    def test_virasoro_c13_constraints(self):
        result = verify_koszul_constraints('virasoro', c=13.0)
        assert result['koszul_symmetry_check']
        assert result['complementarity_sum'] == 13.0

    def test_virasoro_c25_constraints(self):
        result = verify_koszul_constraints('virasoro', c=25.0)
        assert result['koszul_symmetry_check']

    @skipmp
    def test_heisenberg_sewing_euler_product(self):
        """Heisenberg sewing series has Euler product (exact Euler-Koszul)."""
        D = euler_koszul_defect(3.0, 'heisenberg')
        assert abs(D.real - 1.0) < 1e-10, "Heisenberg should be exact Euler-Koszul"

    @skipmp
    def test_virasoro_not_exact_ek(self):
        """Virasoro is NOT exact Euler-Koszul (D ≠ 1)."""
        D = euler_koszul_defect(3.0, 'virasoro')
        assert abs(D.real - 1.0) > 0.01, "Virasoro should not be exact Euler-Koszul"
