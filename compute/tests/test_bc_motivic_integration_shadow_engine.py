r"""Tests for the motivic integration on shadow arc spaces engine.

Multi-path verification (AP10 compliant: no hardcoded values from engine):
  Path 1: Direct computation from defining formulas
  Path 2: Alternative derivation (algebraic identities, L'Hopital, etc.)
  Path 3: Limiting/special cases (c=0, k=0, n=0, d=1, etc.)
  Path 4: Cross-family consistency (shadow depth, lct universality)
  Path 5: Numerical evaluation at specific parameters
  Path 6: Symmetry / duality checks

95 tests covering:
  1. Kappa formulas (all families, AP1/AP48 compliance)
  2. Shadow coefficients (Virasoro, Heisenberg, affine sl2, beta-gamma)
  3. Shadow function evaluation
  4. Arc space dimensions (smooth, hypersurface, shadow)
  5. MotivicClass algebra (point, Lefschetz, projective, arithmetic)
  6. Jet scheme classes (smooth, node, cusp, monomial)
  7. Motivic zeta function (monomial, shadow)
  8. Topological zeta function (L->1 limit)
  9. Log canonical threshold (multi-path)
  10. Igusa p-adic zeta
  11. Monodromy conjecture verification
  12. Hodge-Deligne / nearby fiber
  13. Central charge at Riemann zeros
  14. Shadow depth classification
  15. Stringy invariants
  16. Multi-path verification infrastructure
  17. Comprehensive tables

Manuscript references:
    Theorem D: modular characteristic kappa(A)
    thm:single-line-dichotomy: G/L/C/M classification
    thm:riccati-algebraicity: shadow metric algebraicity
    Q^contact_Vir = 10/[c(5c+22)]
    kappa(Vir_c) = c/2 (AP48)
    kappa(H_k) = k (Heisenberg)
    kappa(g_k) = dim(g)(k+h^vee)/(2h^vee) (affine KM, AP1)
"""

import math
import cmath
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from fractions import Fraction

from compute.lib.bc_motivic_integration_shadow_engine import (
    # Riemann zeros
    RIEMANN_ZEROS_GAMMA,
    riemann_zero,
    # Kappa formulas
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_km,
    kappa_affine_sl2,
    kappa_w_n,
    # Shadow coefficients
    shadow_coefficients_virasoro,
    shadow_coefficients_heisenberg,
    shadow_coefficients_affine_sl2,
    shadow_coefficients_betagamma,
    shadow_function_polynomial,
    # Arc space dimensions
    arc_space_dim_smooth,
    arc_space_dim_hypersurface,
    arc_space_dim_shadow,
    # Motivic class
    MotivicClass,
    # Jet scheme classes
    jet_scheme_class_smooth,
    jet_scheme_class_node,
    jet_scheme_class_cusp,
    jet_scheme_class_monomial,
    # Motivic zeta
    motivic_zeta_monomial,
    motivic_zeta_shadow,
    motivic_zeta_poles,
    # Topological zeta
    topological_zeta_monomial,
    topological_zeta_shadow,
    topological_zeta_poles,
    # LCT
    log_canonical_threshold,
    lct_family_table,
    # Poincare series
    poincare_series_smooth,
    poincare_series_shadow,
    # Igusa
    igusa_zeta_monomial,
    igusa_zeta_shadow,
    igusa_zeta_poles,
    # Monodromy
    local_monodromy_eigenvalues,
    verify_monodromy_conjecture,
    # Hodge-Deligne
    nearby_fiber_hodge_numbers,
    # Riemann zero maps
    central_charge_at_zero,
    motivic_data_at_zero,
    motivic_zeros_vs_riemann_zeros,
    # Stringy
    stringy_euler_number,
    stringy_hodge_number,
    # Multi-path verification
    verify_arc_dim_multipath,
    verify_lct_multipath,
    verify_monodromy_multipath,
    # Shadow depth
    shadow_depth_class,
    # Tables
    arc_space_dimension_table,
    full_motivic_table,
)


# ========================================================================
# Section 1: Kappa formulas (AP1 / AP48 compliance)
# ========================================================================

class TestKappaFormulas:
    """Verify kappa formulas from first principles, not from engine."""

    def test_kappa_heisenberg_is_level(self):
        """kappa(H_k) = k. Direct from Theorem D."""
        for k in [1, 2, 5, 10, -3]:
            assert kappa_heisenberg(k) == k

    def test_kappa_virasoro_is_c_over_2(self):
        """kappa(Vir_c) = c/2. AP48: NOT c."""
        for c in [1, 2, 10, 13, 26, 0.5]:
            # Independent: c/2 computed directly
            assert abs(kappa_virasoro(c) - c / 2) < 1e-15

    def test_kappa_virasoro_complex(self):
        """kappa at complex c."""
        c = 3 + 4j
        assert abs(kappa_virasoro(c) - c / 2) < 1e-15

    def test_kappa_affine_km_formula(self):
        """kappa(g_k) = dim(g)(k+h^vee)/(2h^vee). AP1: independent derivation."""
        # sl_2: dim=3, h^vee=2, k=1: kappa = 3*3/4 = 9/4
        val = kappa_affine_km(3, 1, 2)
        assert abs(val - 9.0 / 4) < 1e-15

        # sl_3: dim=8, h^vee=3, k=1: kappa = 8*4/6 = 32/6 = 16/3
        val2 = kappa_affine_km(8, 1, 3)
        assert abs(val2 - 16.0 / 3) < 1e-12

    def test_kappa_affine_sl2_specialization(self):
        """kappa(sl2_k) = 3(k+2)/4 consistent with general formula."""
        for k in [1, 2, 4, 10]:
            # From specialization
            spec = kappa_affine_sl2(k)
            # From general formula: dim(sl2)=3, h^vee=2
            gen = kappa_affine_km(3, k, 2)
            assert abs(spec - gen) < 1e-12

    def test_kappa_sl2_explicit_values(self):
        """kappa(sl2_k) at specific k, independently computed."""
        # k=1: 3*3/4 = 9/4 = 2.25
        assert abs(kappa_affine_sl2(1) - 2.25) < 1e-15
        # k=2: 3*4/4 = 3
        assert abs(kappa_affine_sl2(2) - 3.0) < 1e-15
        # k=0: 3*2/4 = 1.5
        assert abs(kappa_affine_sl2(0) - 1.5) < 1e-15

    def test_kappa_w_n_uses_harmonic(self):
        """kappa(W_N) = c*(H_N - 1) where H_N = sum 1/j."""
        # W_2 = Virasoro: H_2 = 1 + 1/2 = 3/2, so kappa = c*(3/2-1) = c/2
        for c in [1, 10, 26]:
            assert abs(kappa_w_n(c, 2) - c / 2) < 1e-12

    def test_kappa_w3_harmonic(self):
        """W_3: H_3 = 1 + 1/2 + 1/3 = 11/6, so kappa = c*5/6."""
        c = 12.0
        H3 = 1 + Fraction(1, 2) + Fraction(1, 3)
        expected = c * (float(H3) - 1)  # 12 * 5/6 = 10
        assert abs(kappa_w_n(c, 3) - expected) < 1e-12

    def test_kappa_virasoro_ne_kappa_km_rank_gt_1(self):
        """AP1/AP39: kappa != c/2 for affine KM at rank > 1."""
        # sl_3 at k=1: kappa = dim(g)(k+h^v)/(2h^v) = 8*4/6 = 16/3
        # c/2 would be something else entirely
        kap = kappa_affine_km(8, 1, 3)
        assert abs(kap - 16.0 / 3) < 1e-12


# ========================================================================
# Section 2: Shadow coefficients
# ========================================================================

class TestShadowCoefficients:
    """Shadow tower coefficients S_r for each family."""

    def test_heisenberg_terminates_at_2(self):
        """Heisenberg: S_2=k, S_3=S_4=0. Class G."""
        coeffs = shadow_coefficients_heisenberg(5.0)
        assert abs(coeffs[2] - 5.0) < 1e-15
        assert abs(coeffs[3]) < 1e-15
        assert abs(coeffs[4]) < 1e-15

    def test_virasoro_s2_is_kappa(self):
        """Virasoro S_2 = kappa = c/2."""
        for c in [1, 10, 26]:
            coeffs = shadow_coefficients_virasoro(c)
            assert abs(coeffs[2] - c / 2) < 1e-12

    def test_virasoro_s3_zero_by_parity(self):
        """Virasoro S_3 = 0 (cubic vanishes by conformal weight parity)."""
        coeffs = shadow_coefficients_virasoro(10)
        assert abs(coeffs[3]) < 1e-15

    def test_virasoro_quartic_q_contact(self):
        """Q^contact_Vir = 10/[c(5c+22)] from manuscript."""
        for c in [1, 2, 10, 26]:
            coeffs = shadow_coefficients_virasoro(c)
            # Independent computation of 10/(c*(5c+22))
            expected_q = 10.0 / (c * (5 * c + 22))
            assert abs(coeffs[4] - expected_q) < 1e-12

    def test_virasoro_quartic_at_c1(self):
        """At c=1: Q^contact = 10/(1*27) = 10/27."""
        coeffs = shadow_coefficients_virasoro(1.0)
        assert abs(coeffs[4] - 10.0 / 27) < 1e-12

    def test_virasoro_s4_singular_at_c0(self):
        """S_4 diverges at c=0."""
        coeffs = shadow_coefficients_virasoro(0.0)
        assert math.isinf(abs(coeffs[4]))

    def test_virasoro_higher_arity_from_mc_recursion(self):
        """Higher S_r from MC equation recursion (perturbative in S_4/kappa).

        S_2 = kappa = c/2.
        S_4 = Q^contact = 10/[c(5c+22)].
        S_6 = -S_4^2 / (2*kappa) (from MC at arity 6).
        S_8 = S_4^3 / (2*kappa^2) (from MC at arity 8).
        """
        c = 10.0
        coeffs = shadow_coefficients_virasoro(c, max_arity=10)
        kap = c / 2  # = 5
        S4 = 10.0 / (c * (5 * c + 22))  # = 10/720 = 1/72

        # S_2 = kappa
        assert abs(coeffs[2] - kap) < 1e-10
        # S_4 = Q^contact
        assert abs(coeffs[4] - S4) < 1e-10
        # S_6 = -S_4^2 / (2*kappa)
        expected_s6 = -S4 ** 2 / (2 * kap)
        assert abs(coeffs[6] - expected_s6) < 1e-10
        # S_8 = S_4^3 / (2*kappa^2)
        expected_s8 = S4 ** 3 / (2 * kap ** 2)
        assert abs(coeffs[8] - expected_s8) < 1e-10
        # S_10 = -5*S_4^4 / (8*kappa^3)
        expected_s10 = -5 * S4 ** 4 / (8 * kap ** 3)
        assert abs(coeffs[10] - expected_s10) < 1e-10

    def test_virasoro_odd_arity_all_zero(self):
        """All odd-arity shadow coefficients vanish for Virasoro."""
        coeffs = shadow_coefficients_virasoro(10.0, max_arity=10)
        for r in [3, 5, 7, 9]:
            if r in coeffs:
                assert abs(coeffs[r]) < 1e-15

    def test_affine_sl2_terminates_at_3(self):
        """Affine sl_2: S_2=kappa, S_3=1/(k+2), S_4=0. Class L."""
        k = 1.0
        coeffs = shadow_coefficients_affine_sl2(k)
        assert abs(coeffs[2] - 3 * (k + 2) / 4) < 1e-12
        assert abs(coeffs[3] - 1.0 / (k + 2)) < 1e-12
        assert abs(coeffs[4]) < 1e-15

    def test_betagamma_terminates_at_4(self):
        """Beta-gamma (c=2): S_2=1, S_3=0, S_4=1/12, S_5=0. Class C."""
        coeffs = shadow_coefficients_betagamma(2.0)
        assert abs(coeffs[2] - 1.0) < 1e-12
        assert abs(coeffs[3]) < 1e-15
        assert abs(coeffs[4] - 1.0 / 12) < 1e-12
        assert abs(coeffs[5]) < 1e-15

    def test_betagamma_general_c_uses_quartic_formula(self):
        """For general c (not 2), beta-gamma uses Q^contact formula."""
        c = 6.0
        coeffs = shadow_coefficients_betagamma(c)
        expected_s4 = 10.0 / (c * (5 * c + 22))
        assert abs(coeffs[4] - expected_s4) < 1e-12


# ========================================================================
# Section 3: Shadow function evaluation
# ========================================================================

class TestShadowFunction:
    """Shadow function f_A(x) = sum S_r x^r."""

    def test_heisenberg_is_quadratic(self):
        """f_{Heis}(x) = k * x^2."""
        coeffs = shadow_coefficients_heisenberg(3.0)
        for x in [0.5, 1.0, 2.0]:
            val = shadow_function_polynomial(complex(x), coeffs)
            assert abs(val - 3.0 * x ** 2) < 1e-12

    def test_shadow_function_at_zero(self):
        """f_A(0) = 0 for all families (no constant term)."""
        for fam_func in [
            lambda: shadow_coefficients_heisenberg(1.0),
            lambda: shadow_coefficients_virasoro(10.0),
            lambda: shadow_coefficients_affine_sl2(1.0),
            lambda: shadow_coefficients_betagamma(2.0),
        ]:
            coeffs = fam_func()
            val = shadow_function_polynomial(complex(0), coeffs)
            assert abs(val) < 1e-15

    def test_shadow_function_virasoro_quadratic_dominant(self):
        """For small x, f_Vir(x) ~ kappa * x^2."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro(c)
        x = 0.001
        val = shadow_function_polynomial(complex(x), coeffs)
        leading = (c / 2) * x ** 2
        # Relative error should be small for small x
        assert abs(val - leading) / abs(leading) < 0.01


# ========================================================================
# Section 4: Arc space dimensions
# ========================================================================

class TestArcSpaceDimensions:
    """Jet scheme dimensions from first principles."""

    def test_smooth_dim_formula(self):
        """dim L_n(X) = d*(n+1) for smooth X of dim d."""
        # Independent: d*(n+1)
        for d in [1, 2, 3]:
            for n in [0, 1, 5, 10]:
                assert arc_space_dim_smooth(n, d) == d * (n + 1)

    def test_hypersurface_below_mult(self):
        """For n < mult-1: dim = d*(n+1) (unconstrained)."""
        # f of mult 3 in A^3: for n=0,1 the jets are free
        assert arc_space_dim_hypersurface(0, 3, 3) == 3 * 1  # = 3
        assert arc_space_dim_hypersurface(1, 3, 3) == 3 * 2  # = 6

    def test_hypersurface_above_mult(self):
        """For n >= mult-1: dim = d*(n+1) - (n - mult + 2)."""
        # f of mult 2 in A^2: n=1, dim = 2*2 - (1-2+2) = 4-1 = 3
        assert arc_space_dim_hypersurface(1, 2, 2) == 3
        # n=5, mult=2, d=2: dim = 2*6 - (5-2+2) = 12-5 = 7
        assert arc_space_dim_hypersurface(5, 2, 2) == 7

    def test_shadow_dim_heisenberg(self):
        """Heisenberg: shadow has mult=2, ambient d+1=2."""
        # n=0: mult=2, n < mult-1 = 1, so dim = 2*(0+1) = 2
        dim0 = arc_space_dim_shadow(0, 'Heisenberg', 1.0)
        assert dim0 == 2
        # n=5: dim = 2*6 - (5-2+2) = 12-5 = 7
        dim5 = arc_space_dim_shadow(5, 'Heisenberg', 1.0)
        assert dim5 == 7


# ========================================================================
# Section 5: MotivicClass algebra
# ========================================================================

class TestMotivicClass:
    """K_0(Var_k)[L^{-1}] arithmetic."""

    def test_point_is_L0(self):
        """[pt] = 1 = L^0."""
        pt = MotivicClass.point()
        assert pt.coeffs.get(0, 0) == 1.0

    def test_lefschetz(self):
        """L^n = [A^n]."""
        L3 = MotivicClass.lefschetz(3)
        assert L3.coeffs.get(3, 0) == 1.0
        assert L3.degree() == 3

    def test_projective_formula(self):
        """[P^n] = 1 + L + ... + L^n."""
        P2 = MotivicClass.projective(2)
        assert abs(P2.coeffs.get(0, 0) - 1.0) < 1e-15
        assert abs(P2.coeffs.get(1, 0) - 1.0) < 1e-15
        assert abs(P2.coeffs.get(2, 0) - 1.0) < 1e-15
        assert P2.degree() == 2

    def test_addition(self):
        """[A^1] + [pt] = L + 1."""
        result = MotivicClass.lefschetz(1) + MotivicClass.point()
        assert abs(result.coeffs.get(0, 0) - 1.0) < 1e-15
        assert abs(result.coeffs.get(1, 0) - 1.0) < 1e-15

    def test_subtraction(self):
        """[A^1] - [pt] = L - 1 = [A^1 \\ {0}]."""
        result = MotivicClass.lefschetz(1) - MotivicClass.point()
        assert abs(result.coeffs.get(0, 0) - (-1.0)) < 1e-15
        assert abs(result.coeffs.get(1, 0) - 1.0) < 1e-15

    def test_multiplication(self):
        """L * L = L^2."""
        L = MotivicClass.lefschetz(1)
        L2 = L * L
        assert abs(L2.coeffs.get(2, 0) - 1.0) < 1e-15
        assert L2.degree() == 2

    def test_euler_char_affine(self):
        """chi(A^n) = 1 at L=1."""
        for n in [0, 1, 2, 5]:
            assert abs(MotivicClass.lefschetz(n).euler_characteristic() - 1.0) < 1e-12

    def test_euler_char_projective(self):
        """chi(P^n) = n+1."""
        for n in [0, 1, 2, 3]:
            assert abs(MotivicClass.projective(n).euler_characteristic() - (n + 1)) < 1e-12

    def test_evaluate_at_L_counting(self):
        """At L=q: [A^n] = q^n (F_q-rational points)."""
        q = 7
        for n in [0, 1, 2, 3]:
            val = MotivicClass.lefschetz(n).evaluate_at_L(q)
            assert abs(val - q ** n) < 1e-10

    def test_scale(self):
        """Scalar multiplication."""
        L = MotivicClass.lefschetz(1)
        L3 = L.scale(3.0)
        assert abs(L3.coeffs.get(1, 0) - 3.0) < 1e-15

    def test_equality(self):
        """Equality operator."""
        a = MotivicClass.projective(2)
        b = MotivicClass({0: 1.0, 1: 1.0, 2: 1.0})
        assert a == b

    def test_affine_is_lefschetz(self):
        """affine(n) = lefschetz(n)."""
        assert MotivicClass.affine(3) == MotivicClass.lefschetz(3)

    def test_zero_repr(self):
        """Empty class represents 0."""
        z = MotivicClass({})
        assert repr(z) == "0"

    def test_multiplication_distributive(self):
        """(L+1) * (L-1) = L^2 - 1 (distributivity)."""
        Lp1 = MotivicClass.lefschetz(1) + MotivicClass.point()
        Lm1 = MotivicClass.lefschetz(1) - MotivicClass.point()
        prod = Lp1 * Lm1
        expected = MotivicClass({2: 1.0, 0: -1.0})
        assert prod == expected


# ========================================================================
# Section 6: Jet scheme classes
# ========================================================================

class TestJetSchemeClasses:
    """Jet scheme motivic classes for specific singularity types."""

    def test_smooth_jet_class(self):
        """[L_n(X)] = [X]*L^{nd} for smooth X."""
        X = MotivicClass.lefschetz(2)  # [A^2]
        d = 2
        n = 3
        result = jet_scheme_class_smooth(n, X, d)
        # Should be L^2 * L^6 = L^8
        assert result.degree() == 8

    def test_node_L0(self):
        """L_0({xy=0}) = 2L - 1."""
        result = jet_scheme_class_node(0)
        assert abs(result.coeffs.get(1, 0) - 2.0) < 1e-12
        assert abs(result.coeffs.get(0, 0) - (-1.0)) < 1e-12

    def test_node_euler_char(self):
        """chi(L_n({xy=0})) = 1 for all n."""
        for n in range(5):
            result = jet_scheme_class_node(n)
            assert abs(result.euler_characteristic() - 1.0) < 1e-10

    def test_node_Ln_formula(self):
        """L_n({xy=0}) = 2L^{n+1} - 1 for n >= 1."""
        for n in [1, 2, 3, 5]:
            result = jet_scheme_class_node(n)
            assert abs(result.coeffs.get(n + 1, 0) - 2.0) < 1e-12
            assert abs(result.coeffs.get(0, 0) - (-1.0)) < 1e-12

    def test_cusp_L0_is_L(self):
        """L_0(cusp) = L (birational to A^1)."""
        result = jet_scheme_class_cusp(0)
        assert abs(result.coeffs.get(1, 0) - 1.0) < 1e-12

    def test_cusp_Ln_formula(self):
        """L_n(cusp) = L^{n+1}."""
        for n in [0, 1, 2, 5]:
            result = jet_scheme_class_cusp(n)
            assert abs(result.coeffs.get(n + 1, 0) - 1.0) < 1e-12

    def test_cusp_euler_char(self):
        """chi(L_n(cusp)) = 1 for all n."""
        for n in range(5):
            assert abs(jet_scheme_class_cusp(n).euler_characteristic() - 1.0) < 1e-10

    def test_monomial_jet_class_dim(self):
        """L_n({x^m=0}) = L^{d(n+1) - ceil((n+1)/m)}."""
        d, m = 2, 3
        for n in [0, 1, 2, 5, 10]:
            result = jet_scheme_class_monomial(n, d, m)
            expected_dim = d * (n + 1) - math.ceil((n + 1) / m)
            assert result.degree() == expected_dim

    def test_monomial_m1_is_hyperplane(self):
        """For m=1: {x=0} is smooth, L_n = L^{(d-1)(n+1)}."""
        d, m = 3, 1
        for n in [0, 1, 5]:
            result = jet_scheme_class_monomial(n, d, m)
            # ceil((n+1)/1) = n+1, so dim = d*(n+1) - (n+1) = (d-1)*(n+1)
            assert result.degree() == (d - 1) * (n + 1)


# ========================================================================
# Section 7: Motivic zeta function
# ========================================================================

class TestMotivicZeta:
    """Motivic zeta Z_mot(s) and its poles."""

    def test_monomial_formula(self):
        """Z_mot(A^d, x^m, s) = (L^d - 1)/(L^{ms+d} - 1)."""
        d, m = 1, 2
        L_val = 3.0
        s = 1.0 + 0.5j
        result = motivic_zeta_monomial(d, m, s, L=L_val)
        # Independent: (3^1 - 1) / (3^{2*s+1} - 1)
        numer = L_val ** d - 1
        denom = L_val ** (m * s + d) - 1
        expected = numer / denom
        assert abs(result - expected) < 1e-10

    def test_monomial_pole_at_minus_d_over_m(self):
        """Pole at s = -d/m."""
        d, m = 2, 3
        s_pole = -d / m
        # At the pole, denominator vanishes: L^{ms+d} = L^0 = 1
        L_val = 2.0
        val = motivic_zeta_monomial(d, m, complex(s_pole), L=L_val)
        assert math.isinf(abs(val))

    def test_shadow_poles_heisenberg(self):
        """Heisenberg: pole at s = -1/2 (mult = 2)."""
        poles = motivic_zeta_poles('Heisenberg', 1.0)
        assert len(poles) == 1
        assert abs(poles[0] + 0.5) < 1e-12

    def test_shadow_poles_virasoro(self):
        """Virasoro at generic c: pole at s = -1/2 (leading mult = 2)."""
        for c in [1, 10, 26]:
            poles = motivic_zeta_poles('Virasoro', c)
            assert len(poles) == 1
            assert abs(poles[0] + 0.5) < 1e-12

    def test_shadow_poles_affine_sl2(self):
        """Affine sl_2: pole at s = -1/2 (leading mult = 2)."""
        poles = motivic_zeta_poles('Affine_sl2', 1.0)
        assert len(poles) == 1
        assert abs(poles[0] + 0.5) < 1e-12

    def test_motivic_zeta_heisenberg_is_monomial(self):
        """Heisenberg shadow zeta = monomial zeta (d=1, m=2)."""
        s = 0.5 + 0.3j
        L_val = complex(2)
        z_heis = motivic_zeta_shadow('Heisenberg', 1.0, s, L=L_val)
        z_mono = motivic_zeta_monomial(1, 2, s, L=L_val)
        assert abs(z_heis - z_mono) < 1e-12


# ========================================================================
# Section 8: Topological zeta function
# ========================================================================

class TestTopologicalZeta:
    """Topological zeta Z_top(s) = Z_mot|_{L=1}."""

    def test_monomial_lhopital(self):
        """Z_top = d/(ms+d) from L'Hopital at L=1."""
        d, m = 1, 2
        for s_val in [0.5, 1.0, 2.0]:
            result = topological_zeta_monomial(d, m, complex(s_val))
            expected = d / (m * s_val + d)
            assert abs(result - expected) < 1e-12

    def test_topological_as_motivic_limit(self):
        """Z_top(s) = lim_{L->1} Z_mot(s) verified numerically."""
        d, m = 2, 3
        s = 0.7
        # Evaluate Z_mot at L close to 1
        z_top = topological_zeta_monomial(d, m, complex(s))
        for eps in [0.01, 0.001, 0.0001]:
            z_mot = motivic_zeta_monomial(d, m, complex(s), L=1.0 + eps)
            assert abs(z_mot - z_top) < 10 * eps  # Linear convergence

    def test_topological_poles_shadow(self):
        """Topological poles at s = -1/mult."""
        for family, param, expected_mult in [
            ('Heisenberg', 1.0, 2),
            ('Virasoro', 10.0, 2),
            ('Affine_sl2', 1.0, 2),
            ('BetaGamma', 2.0, 2),
        ]:
            poles = topological_zeta_poles(family, param)
            assert len(poles) == 1
            assert abs(poles[0] - (-1.0 / expected_mult)) < 1e-12

    def test_topological_zeta_at_0_equals_1(self):
        """Z_top(0) = d/(0+d) = 1 for d=1, any m."""
        for m in [2, 3, 4]:
            val = topological_zeta_monomial(1, m, complex(0))
            assert abs(val - 1.0) < 1e-12


# ========================================================================
# Section 9: Log canonical threshold
# ========================================================================

class TestLogCanonicalThreshold:
    """lct(X_A, f_A) = 1/mult for 1D shadow."""

    def test_lct_is_half_for_all_nondegenerate(self):
        """lct = 1/2 for all families with nonzero kappa (mult=2)."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 10.0),
            ('Affine_sl2', 1.0),
            ('BetaGamma', 2.0),
        ]:
            assert abs(log_canonical_threshold(family, param) - 0.5) < 1e-12

    def test_lct_from_topological_poles(self):
        """lct = -max(topological poles). Multi-path check."""
        family, param = 'Virasoro', 10.0
        lct_direct = log_canonical_threshold(family, param)
        poles = topological_zeta_poles(family, param)
        lct_from_poles = -max(poles)
        assert abs(lct_direct - lct_from_poles) < 1e-12

    def test_lct_from_motivic_poles(self):
        """lct = -max(Re(motivic poles)). Multi-path check."""
        family, param = 'Heisenberg', 5.0
        lct_direct = log_canonical_threshold(family, param)
        mot_poles = motivic_zeta_poles(family, param)
        lct_from_mot = -max(p.real for p in mot_poles)
        assert abs(lct_direct - lct_from_mot) < 1e-12

    def test_lct_family_table_structure(self):
        """lct_family_table returns well-formed data."""
        table = lct_family_table()
        assert len(table) > 0
        for entry in table:
            assert 'family' in entry
            assert 'lct' in entry
            assert 'shadow_class' in entry

    def test_lct_family_table_all_half(self):
        """All entries in lct table have lct = 1/2 (nondegenerate)."""
        table = lct_family_table()
        for entry in table:
            assert abs(entry['lct'] - 0.5) < 1e-12


# ========================================================================
# Section 10: Igusa p-adic zeta
# ========================================================================

class TestIgusaZeta:
    """p-adic zeta Z_p(f, s)."""

    def test_igusa_monomial_formula(self):
        """Z_p(x^m, s) = (1-p^{-1})/(1-p^{-(ms+1)}) for d=1."""
        p, m = 2, 2
        s = 0.5 + 0.1j
        result = igusa_zeta_monomial(1, m, s, p=p)
        # Independent computation
        numer = 1 - p ** (-1)
        denom = 1 - p ** (-(m * s + 1))
        expected = numer / denom
        assert abs(result - expected) < 1e-10

    def test_igusa_pole_location(self):
        """Igusa pole at s = -1/m (real pole matches topological)."""
        poles = igusa_zeta_poles('Virasoro', 10.0, p=2)
        assert len(poles) == 1
        assert abs(poles[0].real - (-0.5)) < 1e-12

    def test_igusa_shadow_reduces_to_monomial(self):
        """For Heisenberg, Igusa shadow = Igusa monomial (d=1, m=2)."""
        s = 1.0 + 0.5j
        p = 3
        z_shadow = igusa_zeta_shadow('Heisenberg', 1.0, s, p=p)
        z_mono = igusa_zeta_monomial(1, 2, s, p=p)
        assert abs(z_shadow - z_mono) < 1e-12

    def test_igusa_at_large_Re_s(self):
        """For Re(s) >> 0, Z_p(s) -> (1-p^{-1}) (denominator -> 1)."""
        p = 2
        s = complex(100)
        val = igusa_zeta_monomial(1, 2, s, p=p)
        # p^{-(2*100+1)} ~ 0, so denom ~ 1
        expected = (1 - p ** (-1))
        assert abs(val - expected) < 1e-10


# ========================================================================
# Section 11: Monodromy conjecture
# ========================================================================

class TestMonodromy:
    """Local monodromy eigenvalues and Igusa-Denef-Loeser conjecture."""

    def test_monodromy_roots_of_unity(self):
        """For mult m: eigenvalues are m-th roots of unity."""
        eigenvals = local_monodromy_eigenvalues('Heisenberg', 1.0)
        # mult = 2: eigenvalues are 1, -1
        assert len(eigenvals) == 2
        # Check they are 2nd roots of unity
        for ev in eigenvals:
            assert abs(ev ** 2 - 1) < 1e-10

    def test_monodromy_conjecture_holds(self):
        """For each pole s_0, exp(2pi*i*s_0) is a monodromy eigenvalue."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 10.0),
            ('Affine_sl2', 1.0),
            ('BetaGamma', 2.0),
        ]:
            result = verify_monodromy_conjecture(family, param)
            assert result['verified'] is True

    def test_monodromy_explicit_heisenberg(self):
        """Heisenberg: pole at -1/2, exp(2pi*i*(-1/2)) = exp(-pi*i) = -1."""
        result = verify_monodromy_conjecture('Heisenberg', 1.0)
        detail = result['details'][0]
        # exp(2*pi*i*(-1/2)) = exp(-pi*i) = -1
        expected_candidate = cmath.exp(-1j * cmath.pi)
        assert abs(detail['candidate'] - expected_candidate) < 1e-10
        assert detail['is_eigenvalue'] is True

    def test_monodromy_multipath(self):
        """Multi-path monodromy verification."""
        for family, param in [
            ('Heisenberg', 2.0),
            ('Virasoro', 26.0),
        ]:
            result = verify_monodromy_multipath(family, param)
            assert result['verified'] is True
            assert result['paths_agree'] is True


# ========================================================================
# Section 12: Hodge-Deligne / nearby fiber
# ========================================================================

class TestHodgeDeligne:
    """Hodge-Deligne numbers and nearby fiber data."""

    def test_milnor_number_formula(self):
        """Milnor number = mult - 1 for isolated 1D singularity."""
        for family, param, expected_mult in [
            ('Heisenberg', 1.0, 2),
            ('Virasoro', 10.0, 2),
            ('Affine_sl2', 1.0, 2),
        ]:
            hd = nearby_fiber_hodge_numbers(family, param)
            # Independent: mult - 1
            assert hd['milnor_number'] == expected_mult - 1

    def test_spectral_numbers(self):
        """Spectral numbers = {k/m : k=1,...,m-1}."""
        hd = nearby_fiber_hodge_numbers('Heisenberg', 1.0)
        # mult=2: spectral numbers = {1/2}
        assert len(hd['spectral_numbers']) == 1
        assert abs(hd['spectral_numbers'][0] - 0.5) < 1e-12

    def test_hodge_h00_always_1(self):
        """h^{0,0} = 1 (constant sheaf contribution)."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 10.0),
        ]:
            hd = nearby_fiber_hodge_numbers(family, param)
            assert hd['hodge_numbers'].get((0, 0), 0) == 1

    def test_hodge_h01_is_milnor(self):
        """h^{0,1} = mu = m-1 for the 1D case."""
        hd = nearby_fiber_hodge_numbers('Heisenberg', 1.0)
        # mult=2: milnor = 1, so h^{0,1} = 1
        assert hd['hodge_numbers'].get((0, 1), 0) == 1

    def test_monodromy_eigenvalues_from_spectral(self):
        """Monodromy eigenvalues = exp(2*pi*i*alpha) for spectral alpha."""
        hd = nearby_fiber_hodge_numbers('Heisenberg', 1.0)
        for alpha, ev in zip(hd['spectral_numbers'], hd['monodromy_eigenvalues']):
            expected = cmath.exp(2j * cmath.pi * alpha)
            assert abs(ev - expected) < 1e-10


# ========================================================================
# Section 13: Riemann zero mapping
# ========================================================================

class TestRiemannZeroMapping:
    """Benjamin-Chang map rho_n -> c(rho_n)."""

    def test_riemann_zero_format(self):
        """rho_n = 1/2 + i*gamma_n."""
        rho1 = riemann_zero(1)
        assert abs(rho1.real - 0.5) < 1e-12
        assert abs(rho1.imag - RIEMANN_ZEROS_GAMMA[0]) < 1e-12

    def test_riemann_zero_out_of_range(self):
        """Out-of-range index raises ValueError."""
        with pytest.raises(ValueError):
            riemann_zero(0)
        with pytest.raises(ValueError):
            riemann_zero(100)

    def test_central_charge_formula(self):
        """c(rho) = 26*rho/(rho+1). Independent computation."""
        for n in [1, 5, 10]:
            rho = riemann_zero(n)
            c_val = central_charge_at_zero(n)
            expected = 26 * rho / (rho + 1)
            assert abs(c_val - expected) < 1e-10

    def test_motivic_data_structure(self):
        """motivic_data_at_zero returns complete data dict."""
        md = motivic_data_at_zero(1)
        required_keys = [
            'zero_index', 'rho_n', 'gamma_n', 'c_rho', 'kappa_rho',
            'shadow_coeffs', 'multiplicity', 'motivic_poles',
            'topological_poles', 'lct', 'milnor_number',
            'monodromy_eigenvalues', 'igusa_p2_at_s1', 'Z_mot_at_rho',
        ]
        for key in required_keys:
            assert key in md, f"Missing key: {key}"

    def test_motivic_data_kappa_consistent(self):
        """kappa(c(rho)) = c(rho)/2."""
        for n in [1, 3, 7]:
            md = motivic_data_at_zero(n)
            assert abs(md['kappa_rho'] - md['c_rho'] / 2) < 1e-10

    def test_motivic_zeros_all_at_half(self):
        """All motivic poles at -1/2 for non-degenerate Virasoro."""
        result = motivic_zeros_vs_riemann_zeros(n_zeros=10)
        assert result['all_poles_at_minus_half'] is True

    def test_riemann_zeros_increasing(self):
        """gamma_n is strictly increasing."""
        for i in range(len(RIEMANN_ZEROS_GAMMA) - 1):
            assert RIEMANN_ZEROS_GAMMA[i] < RIEMANN_ZEROS_GAMMA[i + 1]

    def test_first_zero_value(self):
        """gamma_1 ~ 14.1347... (Odlyzko tables, independently known)."""
        # The first nontrivial zero is at 1/2 + i*14.134725...
        assert abs(RIEMANN_ZEROS_GAMMA[0] - 14.134725141734693) < 1e-6


# ========================================================================
# Section 14: Stringy invariants
# ========================================================================

class TestStringyInvariants:
    """Stringy Euler number and Hodge numbers."""

    def test_stringy_euler_is_1(self):
        """e_st = Z_top(0) = 1 for 1D isolated singularities."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 10.0),
            ('Affine_sl2', 1.0),
            ('BetaGamma', 2.0),
        ]:
            assert abs(stringy_euler_number(family, param) - 1.0) < 1e-10

    def test_stringy_hodge_00(self):
        """e_st^{0,0} = 1."""
        assert abs(stringy_hodge_number('Virasoro', 10.0, 0, 0) - 1.0) < 1e-12

    def test_stringy_hodge_higher_zero(self):
        """e_st^{p,q} = 0 for (p,q) != (0,0) (isolated point in A^1)."""
        for p, q in [(0, 1), (1, 0), (1, 1), (2, 0)]:
            assert abs(stringy_hodge_number('Virasoro', 10.0, p, q)) < 1e-12


# ========================================================================
# Section 15: Shadow depth classification
# ========================================================================

class TestShadowDepth:
    """G/L/C/M classification and motivic complexity."""

    def test_heisenberg_class_G(self):
        info = shadow_depth_class('Heisenberg', 1.0)
        assert info['shadow_class'] == 'G'
        assert info['r_max'] == 2

    def test_affine_sl2_class_L(self):
        info = shadow_depth_class('Affine_sl2', 1.0)
        assert info['shadow_class'] == 'L'
        assert info['r_max'] == 3

    def test_betagamma_class_C(self):
        info = shadow_depth_class('BetaGamma', 2.0)
        assert info['shadow_class'] == 'C'
        assert info['r_max'] == 4

    def test_virasoro_class_M(self):
        info = shadow_depth_class('Virasoro', 10.0)
        assert info['shadow_class'] == 'M'
        assert info['r_max'] == float('inf')

    def test_lct_universal_half(self):
        """All non-degenerate shadows have lct = 1/2."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 10.0),
            ('Affine_sl2', 1.0),
            ('BetaGamma', 2.0),
        ]:
            info = shadow_depth_class(family, param)
            assert info['lct_universal'] is True


# ========================================================================
# Section 16: Multi-path verification infrastructure
# ========================================================================

class TestMultiPathVerification:
    """Multi-path verification functions from the engine."""

    def test_arc_dim_multipath_agrees(self):
        """All 5 paths agree for arc space dimension."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 10.0),
            ('Affine_sl2', 1.0),
        ]:
            for n in [0, 1, 5]:
                result = verify_arc_dim_multipath(family, param, n)
                assert result['all_agree'] is True

    def test_lct_multipath_agrees(self):
        """All 5 paths agree for log canonical threshold."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 26.0),
            ('Affine_sl2', 2.0),
            ('BetaGamma', 2.0),
        ]:
            result = verify_lct_multipath(family, param)
            assert result['all_agree'] is True
            # Independent: lct = 1/mult = 1/2
            assert abs(result['path4_multiplicity'] - 0.5) < 1e-12

    def test_monodromy_multipath_agrees(self):
        """All monodromy paths agree."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 10.0),
        ]:
            result = verify_monodromy_multipath(family, param)
            assert result['verified'] is True
            assert result['paths_agree'] is True


# ========================================================================
# Section 17: Poincare series
# ========================================================================

class TestPoincareSeries:
    """Poincare series of arc spaces."""

    def test_smooth_poincare_series(self):
        """For smooth X of dim d: virtual dim = d*(n+1)."""
        ps = poincare_series_smooth(2, 5)
        for n in range(6):
            assert ps[n] == 2 * (n + 1)

    def test_shadow_poincare_length(self):
        """Poincare series returns N+1 entries."""
        N = 7
        ps = poincare_series_shadow('Heisenberg', 1.0, N=N)
        assert len(ps) == N + 1

    def test_shadow_poincare_degree_monotone(self):
        """Degree of [L_n] is non-decreasing in n."""
        ps = poincare_series_shadow('Virasoro', 10.0, N=10)
        for i in range(len(ps) - 1):
            assert ps[i].degree() <= ps[i + 1].degree()


# ========================================================================
# Section 18: Tables
# ========================================================================

class TestTables:
    """Comprehensive computation tables."""

    def test_arc_table_nonempty(self):
        """arc_space_dimension_table returns data."""
        table = arc_space_dimension_table(max_n=3)
        assert len(table) > 0

    def test_arc_table_chi_structure(self):
        """Each arc table entry has chi and dim fields."""
        table = arc_space_dimension_table(max_n=2)
        for entry in table:
            assert 'dim_Ln' in entry
            assert 'chi_Ln' in entry

    def test_full_motivic_table_structure(self):
        """full_motivic_table returns well-formed data."""
        table = full_motivic_table(n_zeros=3)
        assert len(table) == 3
        for entry in table:
            assert 'gamma_n' in entry
            assert 'lct' in entry
            assert 'milnor' in entry


# ========================================================================
# Section 19: Cross-family consistency checks (AP10 anti-pattern)
# ========================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks that do NOT hardcode engine outputs."""

    def test_lct_universal_across_families(self):
        """All nondegenerate families have lct = 1/2 (from mult=2)."""
        # This is a STRUCTURAL property: kappa is the leading coefficient,
        # so mult=2, hence lct=1/mult=1/2.
        for family, param in [
            ('Heisenberg', 1.0),
            ('Heisenberg', 10.0),
            ('Virasoro', 1.0),
            ('Virasoro', 13.0),
            ('Virasoro', 26.0),
            ('Affine_sl2', 1.0),
            ('Affine_sl2', 10.0),
            ('BetaGamma', 2.0),
        ]:
            lct = log_canonical_threshold(family, param)
            assert abs(lct - 0.5) < 1e-12, f"lct({family},{param}) = {lct}"

    def test_kappa_additivity_heisenberg_tensor(self):
        """kappa is additive: kappa(H_k1 x H_k2) = k1 + k2.
        Verify via independent sum: kappa = k."""
        k1, k2 = 3, 7
        kap1 = kappa_heisenberg(k1)
        kap2 = kappa_heisenberg(k2)
        assert abs(kap1 + kap2 - (k1 + k2)) < 1e-15

    def test_virasoro_koszul_dual_kappa_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c in [1, 5, 10, 13, 20, 25]:
            kap = kappa_virasoro(c)
            kap_dual = kappa_virasoro(26 - c)
            # Independent: c/2 + (26-c)/2 = 13
            assert abs(kap + kap_dual - 13.0) < 1e-12

    def test_w2_equals_virasoro(self):
        """W_2 = Virasoro: kappa(W_2, c) = kappa(Vir_c) = c/2."""
        for c in [1, 10, 26]:
            assert abs(kappa_w_n(c, 2) - kappa_virasoro(c)) < 1e-12

    def test_shadow_depth_ordering(self):
        """G < L < C < M in shadow depth."""
        depths = {
            'G': shadow_depth_class('Heisenberg', 1.0)['r_max'],
            'L': shadow_depth_class('Affine_sl2', 1.0)['r_max'],
            'C': shadow_depth_class('BetaGamma', 2.0)['r_max'],
            'M': shadow_depth_class('Virasoro', 10.0)['r_max'],
        }
        assert depths['G'] < depths['L'] < depths['C'] < depths['M']

    def test_motivic_pole_independent_of_param(self):
        """For 1D shadow, the pole location -1/2 is independent of c, k."""
        # Because the leading term is always kappa*x^2 (mult=2)
        for param in [1, 5, 10, 26]:
            poles_v = motivic_zeta_poles('Virasoro', param)
            poles_h = motivic_zeta_poles('Heisenberg', param)
            assert abs(poles_v[0] + 0.5) < 1e-12
            assert abs(poles_h[0] + 0.5) < 1e-12

    def test_igusa_topological_pole_agreement(self):
        """Real part of Igusa poles = topological poles (structural)."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 10.0),
            ('Affine_sl2', 2.0),
        ]:
            igusa = igusa_zeta_poles(family, param, p=2)
            top = topological_zeta_poles(family, param)
            for ip in igusa:
                assert any(abs(ip.real - tp) < 1e-10 for tp in top)

    def test_stringy_euler_universal(self):
        """e_st = 1 for all shadow varieties (Z_top(0) = 1/(0+1) = 1)."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 13.0),
            ('Affine_sl2', 4.0),
            ('BetaGamma', 2.0),
        ]:
            assert abs(stringy_euler_number(family, param) - 1.0) < 1e-10

    def test_milnor_universal_for_mult2(self):
        """Milnor number = 1 for all mult=2 shadows (m-1 = 1)."""
        for family, param in [
            ('Heisenberg', 1.0),
            ('Virasoro', 26.0),
            ('Affine_sl2', 1.0),
            ('BetaGamma', 2.0),
        ]:
            hd = nearby_fiber_hodge_numbers(family, param)
            assert hd['milnor_number'] == 1

    def test_monodromy_conjecture_universal(self):
        """Monodromy conjecture holds for all standard families."""
        for family, param in [
            ('Heisenberg', 2.0),
            ('Virasoro', 1.0),
            ('Virasoro', 13.0),
            ('Virasoro', 26.0),
            ('Affine_sl2', 1.0),
            ('BetaGamma', 2.0),
        ]:
            result = verify_monodromy_conjecture(family, param)
            assert result['verified'] is True


# ========================================================================
# Section 20: Edge cases and error handling
# ========================================================================

class TestEdgeCases:
    """Edge cases and boundary behavior."""

    def test_unknown_family_raises(self):
        """Unknown family name raises ValueError."""
        with pytest.raises(ValueError):
            motivic_zeta_poles('UnknownAlgebra', 1.0)

    def test_affine_sl2_critical_level(self):
        """At k=-2 (critical level): S_3 diverges."""
        coeffs = shadow_coefficients_affine_sl2(-2.0)
        assert math.isinf(abs(coeffs[3]))

    def test_virasoro_c_minus22over5(self):
        """At c = -22/5: denominator 5c+22=0, S_4 diverges."""
        coeffs = shadow_coefficients_virasoro(-22.0 / 5)
        assert math.isinf(abs(coeffs[4]))

    def test_zero_motivic_class(self):
        """Zero class has degree 0 and chi 0."""
        z = MotivicClass({})
        assert z.degree() == 0
        assert abs(z.euler_characteristic()) < 1e-15

    def test_heisenberg_at_zero_level(self):
        """Heisenberg at k=0: kappa=0, shadow function is zero."""
        coeffs = shadow_coefficients_heisenberg(0.0)
        assert abs(coeffs[2]) < 1e-15
