r"""Tests for Swiss-cheese m_4^{SC} vanishing for affine sl_2 at generic level.

Verifies:
  1.  sl_2 Lie algebra identities (Jacobi, Killing invariance)
  2.  Affine sl_2 data (central charge, kappa, r-matrix)
  3.  m_3^{SC} is NONZERO (class L has depth 3)
  4.  m_4^{SC} = 0 (all 243 tensor components vanish)
  5.  Individual tree topologies do NOT vanish (nontrivial cancellation)
  6.  m_4 = 0 as polynomial in k (algebraic + 15 spot checks)
  7.  Shadow classification (class L, depth 3, S_4 = 0)
  8.  Discriminant Delta = 0
  9.  Cross-family consistency: Heisenberg limit k -> 0

Multi-path verification (AP10): m_4 = 0 verified by 3 independent methods:
  [DC] Direct tensor computation (all 243 components)
  [LT] Shadow coefficient S_4 = 0 (quartic Casimir argument, rank 1)
  [NE] Numerical evaluation at 15 values of k

Convention: exact rational arithmetic via sympy.Rational. No floating point.

References:
  thm:koszul-equivalences-meta, item (iii) (chiral_koszul_pairs.tex)
  prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
  theorem_ainfty_nonformality_class_m_engine.py (swiss_cheese_m3_affine_sl2)
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.sc_m4_sl2_koszul_engine import (
    DIM_SL2,
    GENERATOR_NAMES,
    H_DUAL_SL2,
    KILLING_FORM,
    RANK_SL2,
    STRUCTURE_CONSTANTS,
    central_charge,
    compute_m3_full_tensor,
    compute_m4_full_tensor,
    compute_m4_tensor_channel,
    discriminant_sl2,
    f_abc,
    f_abc_upper,
    full_verification,
    kappa_affine_sl2,
    killing,
    killing_inv,
    r_matrix_sl2,
    shadow_S3,
    shadow_S4_symbolic,
    shadow_classification,
    verify_jacobi,
    verify_killing_invariance,
    verify_m3_nonzero,
    verify_m4_at_specific_k,
    verify_m4_polynomial_in_k,
    verify_m4_vanishes,
    verify_m4_vanishes_per_topology,
)

k = Symbol('k')


# ===================================================================
# A. sl_2 Lie algebra identities (5 tests)
# ===================================================================

class TestSl2LieAlgebra:
    """Verify sl_2 Lie algebra data is consistent."""

    def test_generators(self):
        """Three generators: e, f, h."""
        assert GENERATOR_NAMES == ("e", "f", "h")
        assert DIM_SL2 == 3

    def test_killing_form_symmetry(self):
        """Killing form is symmetric: (a,b) = (b,a)."""
        for a in range(DIM_SL2):
            for b in range(DIM_SL2):
                assert killing(a, b) == killing(b, a), (
                    f"Killing form not symmetric at ({a},{b})"
                )

    def test_killing_form_values(self):
        """Killing form values: (e,f)=1, (h,h)=2, others=0.

        # VERIFIED: [DC] direct from Chevalley basis normalization,
        #           [LT] Humphreys "Introduction to Lie Algebras" Ch.8
        """
        assert killing(0, 1) == Rational(1)   # (e, f) = 1
        assert killing(1, 0) == Rational(1)   # (f, e) = 1
        assert killing(2, 2) == Rational(2)   # (h, h) = 2
        assert killing(0, 0) == Rational(0)   # (e, e) = 0
        assert killing(1, 1) == Rational(0)   # (f, f) = 0
        assert killing(0, 2) == Rational(0)   # (e, h) = 0

    def test_jacobi_identity(self):
        """Jacobi identity: [a,[b,c]] + [b,[c,a]] + [c,[a,b]] = 0.

        # VERIFIED: [DC] exhaustive check over all 3^4 = 81 quadruples,
        #           [LT] sl_2 is a Lie algebra (Serre relations)
        """
        assert verify_jacobi() is True

    def test_killing_invariance(self):
        """Killing form ad-invariance: f^{abc} is totally antisymmetric.

        # VERIFIED: [DC] exhaustive check over all 3^3 = 27 triples,
        #           [LT] Cartan criterion for semisimplicity
        """
        assert verify_killing_invariance() is True

    def test_structure_constants_specific(self):
        """Spot-check structure constants.

        [h, e] = 2e, [h, f] = -2f, [e, f] = h.

        # VERIFIED: [DC] direct from definition,
        #           [LT] Humphreys Ch.7
        """
        # [e, f] = h: f^{ef}_h = 1
        assert f_abc(0, 1, 2) == Rational(1)
        # [f, e] = -h: f^{fe}_h = -1
        assert f_abc(1, 0, 2) == Rational(-1)
        # [h, e] = 2e: f^{he}_e = 2
        assert f_abc(2, 0, 0) == Rational(2)
        # [h, f] = -2f: f^{hf}_f = -2
        assert f_abc(2, 1, 1) == Rational(-2)

    def test_structure_constants_antisymmetry(self):
        """f^{ab}_c = -f^{ba}_c."""
        for a in range(DIM_SL2):
            for b in range(DIM_SL2):
                for c in range(DIM_SL2):
                    assert f_abc(a, b, c) == -f_abc(b, a, c), (
                        f"Antisymmetry failed at ({a},{b},{c})"
                    )


# ===================================================================
# B. Affine sl_2 data (6 tests)
# ===================================================================

class TestAffineSl2Data:
    """Affine sl_2 constants and formulas."""

    def test_dual_coxeter(self):
        """h^v(sl_2) = 2.

        # VERIFIED: [DC] from root system, [LT] Kac "Infinite-dim Lie algebras" Table Aff 1
        """
        assert H_DUAL_SL2 == 2

    def test_central_charge_formula(self):
        """c(k) = 3k/(k+2).

        # VERIFIED: [DC] Sugawara: c = k*dim/(k+h^v) = 3k/(k+2),
        #           [LT] Kac-Wakimoto, [LC] c(0)=0 (abelian), c(1)=1
        """
        assert simplify(central_charge(k) - 3*k/(k+2)) == 0

    def test_central_charge_k0(self):
        """c(0) = 0 (abelian limit).

        # VERIFIED: [DC] 3*0/(0+2) = 0, [LC] abelian -> c=0
        """
        assert central_charge(Rational(0)) == Rational(0)

    def test_central_charge_k1(self):
        """c(1) = 1.

        # VERIFIED: [DC] 3*1/(1+2) = 1, [LT] level 1 sl_2 = free fermion
        """
        assert central_charge(Rational(1)) == Rational(1)

    def test_kappa_formula(self):
        r"""kappa(V_k(sl_2)) = 3(k+2)/4.

        % AP1: from landscape_census.tex
        % k=0 -> 3/2 (NOT zero)
        % k=-2 -> 0 (critical level)

        # VERIFIED: [DC] dim(sl_2)*(k+h^v)/(2*h^v) = 3*(k+2)/4,
        #           [LC] k=0 -> 3/2, k=-2 -> 0 (critical)
        """
        assert simplify(kappa_affine_sl2(k) - Rational(3)*(k+2)/4) == 0
        assert kappa_affine_sl2(Rational(0)) == Rational(3, 2)
        assert kappa_affine_sl2(Rational(-2)) == Rational(0)

    def test_r_matrix_k0_vanishes(self):
        r"""r-matrix at k=0 vanishes (AP126/AP141 check).

        % AP126: r(z) = k * Omega / z. At k=0, r=0.
        % AP141: mandatory vanishing check.

        # VERIFIED: [DC] r(0) = 0 * Omega / z = 0, [SY] abelian limit
        """
        assert r_matrix_sl2(Rational(0)) == Rational(0)


# ===================================================================
# C. Shadow coefficients (4 tests)
# ===================================================================

class TestShadowCoefficients:
    """Shadow coefficients S_3, S_4 for affine sl_2."""

    def test_S3_formula(self):
        """S_3 = 4/(k+2) = 2*h^v/(k+h^v).

        # VERIFIED: [DC] 2*2/(k+2) = 4/(k+2),
        #           [LT] prop:shadow-formality-low-arity
        """
        assert simplify(shadow_S3(k) - 4/(k+2)) == 0

    def test_S3_at_k1(self):
        """S_3(k=1) = 4/3.

        # VERIFIED: [DC] 4/(1+2) = 4/3, [NE] numerical check
        """
        assert shadow_S3(Rational(1)) == Rational(4, 3)

    def test_S3_nonzero_generic(self):
        """S_3 != 0 for k != -2 (generic level)."""
        for kv in [Rational(1), Rational(2), Rational(10), Rational(1, 2)]:
            assert shadow_S3(kv) != Rational(0), f"S_3 should be nonzero at k={kv}"

    def test_S4_zero(self):
        """S_4 = 0 identically (class L, no quartic Casimir for rank 1).

        # VERIFIED: [DC] direct computation via compute_m4_full_tensor,
        #           [LT] sl_2 rank 1 => only quadratic Casimir,
        #           [SY] class L terminates at depth 3
        """
        assert shadow_S4_symbolic() == Rational(0)


# ===================================================================
# D. m_3^{SC} nonvanishing (3 tests)
# ===================================================================

class TestM3Nonzero:
    """Verify m_3^{SC} != 0 for affine sl_2 (class L has depth 3)."""

    def test_m3_has_nonzero_components(self):
        """m_3^{SC} tensor has at least one nonzero component.

        # VERIFIED: [DC] explicit tensor computation,
        #           [LT] class L defined by m_3 != 0
        """
        result = verify_m3_nonzero()
        assert result["m3_nonzero"] is True

    def test_m3_nonzero_count(self):
        """Count of nonzero m_3 components is positive."""
        result = verify_m3_nonzero()
        assert result["nonzero_count"] > 0

    def test_m3_specific_component(self):
        """m_3(e, f, e)_e = [[e,f],e] + [e,[f,e]] = [h,e] + [e,-h] = 2e + 2e = 4e.

        Wait: [[e,f],e]_e = sum_g f^{ef}_g f^{ge}_e.
        f^{ef}_h = 1. f^{he}_e = 2. So [[e,f],e]_e = 1*2 = 2.
        [e,[f,e]]_e = sum_g f^{fe}_g f^{eg}_e.
        f^{fe}_h = -1. f^{eh}_e = -2. So [e,[f,e]]_e = (-1)*(-2) = 2.
        Total: 2 + 2 = 4.

        # VERIFIED: [DC] direct structure constant computation,
        #           [LC] matches Jacobi identity consequence
        """
        tensor = compute_m3_full_tensor()
        # m_3(e, f, e)_e = (0, 1, 0, 0)
        assert tensor[(0, 1, 0, 0)] == Rational(4)


# ===================================================================
# E. m_4^{SC} vanishing -- main result (6 tests)
# ===================================================================

class TestM4Vanishes:
    """Core verification: m_4^{SC} = 0 for sl_2."""

    def test_m4_all_components_zero(self):
        """All 243 components of m_4^{SC} tensor are zero.

        # VERIFIED: [DC] exhaustive computation of 3^5 = 243 components,
        #           [LT] quartic Casimir decomposable for rank 1,
        #           [SY] class L terminates at depth 3
        """
        result = verify_m4_vanishes()
        assert result["m4_vanishes"] is True
        assert result["nonzero_count"] == 0
        assert result["total_components"] == 243

    def test_m4_individual_topologies_nonzero(self):
        """Individual tree topologies do NOT vanish; only the SUM does.

        This confirms the cancellation is NONTRIVIAL (not topology-by-topology).

        # VERIFIED: [DC] per-topology tensor computation
        """
        results = verify_m4_vanishes_per_topology()
        # At least one topology should have nonzero components
        has_nonzero = any(
            results[t]["nonzero_count"] > 0 for t in ["cat_L", "cat_R", "bal"]
        )
        assert has_nonzero, "Expected nontrivial cancellation between topologies"

    def test_m4_catL_nonzero_alone(self):
        """Left caterpillar [[[a1,a2],a3],a4] alone is nonzero."""
        results = verify_m4_vanishes_per_topology()
        assert results["cat_L"]["nonzero_count"] > 0

    def test_m4_balanced_nonzero_alone(self):
        """Balanced tree [[a1,a2],[a3,a4]] alone is nonzero."""
        results = verify_m4_vanishes_per_topology()
        assert results["bal"]["nonzero_count"] > 0

    def test_m4_specific_component_zero(self):
        """Spot check: m_4(e,f,e,f)_h = 0.

        # VERIFIED: [DC] explicit computation of cat_L + cat_R + bal
        """
        tensor = compute_m4_full_tensor()
        assert tensor[(0, 1, 0, 1, 2)] == Rational(0)

    def test_m4_another_component_zero(self):
        """Spot check: m_4(h,e,f,h)_e = 0."""
        tensor = compute_m4_full_tensor()
        assert tensor[(2, 0, 1, 2, 0)] == Rational(0)


# ===================================================================
# F. Polynomial vanishing in k (4 tests)
# ===================================================================

class TestPolynomialVanishing:
    """Verify m_4 = 0 as polynomial in k (not just at specific values)."""

    def test_polynomial_verification(self):
        """Full polynomial verification: algebraic + spot checks + S_4.

        # VERIFIED: [DC] algebraic (tensor contraction),
        #           [NE] 15 numerical spot checks,
        #           [LT] S_4 = 0 as rational function
        """
        result = verify_m4_polynomial_in_k()
        assert result["polynomial_zero"] is True
        assert result["algebraic_zero"] is True
        assert result["spot_checks_all_zero"] is True
        assert result["S4_rational_zero"] is True

    def test_spot_check_k1(self):
        """m_4 = 0 at k = 1."""
        result = verify_m4_at_specific_k(Rational(1))
        assert result["m4_vanishes"] is True

    def test_spot_check_k_large(self):
        """m_4 = 0 at k = 100 (large level limit)."""
        result = verify_m4_at_specific_k(Rational(100))
        assert result["m4_vanishes"] is True

    def test_spot_check_k_fractional(self):
        """m_4 = 0 at k = 1/3 (non-integer level)."""
        result = verify_m4_at_specific_k(Rational(1, 3))
        assert result["m4_vanishes"] is True


# ===================================================================
# G. Shadow classification (4 tests)
# ===================================================================

class TestShadowClassification:
    """Shadow classification for affine sl_2."""

    def test_class_L(self):
        """Affine sl_2 is class L (shadow depth 3).

        # VERIFIED: [DC] S_3 != 0, S_4 = 0 => depth 3 = class L,
        #           [LT] all affine KM are class L
        """
        result = shadow_classification()
        assert result["shadow_class"] == "L"
        assert result["shadow_depth"] == 3

    def test_S3_nonzero_S4_zero(self):
        """S_3 != 0 and S_4 = 0: defining property of class L."""
        result = shadow_classification()
        assert result["S3_nonzero"] is True
        assert result["S4_zero"] is True

    def test_m3_nonzero_m4_zero(self):
        """m_3^{SC} != 0 and m_4^{SC} = 0: operational definition of class L."""
        result = shadow_classification()
        assert result["m3_SC_nonzero"] is True
        assert result["m4_SC_zero"] is True

    def test_discriminant_zero(self):
        """Delta = 8 * kappa * S_4 = 0 (class L has Delta = 0).

        % AP21: Delta = 8*kappa*S_4, LINEAR in kappa

        # VERIFIED: [DC] S_4 = 0 => Delta = 0,
        #           [LT] Delta = 0 <=> finite tower
        """
        assert discriminant_sl2() == Rational(0)


# ===================================================================
# H. Cross-family consistency (3 tests)
# ===================================================================

class TestCrossFamilyConsistency:
    """Cross-checks with other families and engines."""

    def test_heisenberg_limit_S3(self):
        """As k -> 0 (abelian limit), S_3 -> 2 (finite, nonzero).

        But at k=0, the algebra becomes Heisenberg (class G, depth 2).
        S_3(k=0) = 4/2 = 2, but the CLASS changes from L to G.
        The shadow depth classification is NOT continuous in k.

        # VERIFIED: [DC] S_3(0) = 4/2 = 2, [LC] matches Heisenberg limit
        """
        S3_at_0 = shadow_S3(Rational(0))
        assert S3_at_0 == Rational(2)

    def test_kappa_at_k0_matches_dim_over_2(self):
        r"""kappa(V_0(sl_2)) = dim(sl_2)/2 = 3/2.

        At k=0 (abelian limit): kappa = dim(g)(0+h^v)/(2h^v) = dim(g)/2.
        % AP1: k=0 -> kappa = dim(g)/2 (NOT zero)

        # VERIFIED: [DC] 3*(0+2)/4 = 3/2 = dim(sl_2)/2,
        #           [LC] matches general formula
        """
        assert kappa_affine_sl2(Rational(0)) == Rational(3, 2)
        assert kappa_affine_sl2(Rational(0)) == Rational(DIM_SL2, 2)

    def test_critical_level_kappa_zero(self):
        r"""kappa(V_{-2}(sl_2)) = 0 (critical level).

        % AP1: k=-h^v -> kappa = 0 (critical level)

        # VERIFIED: [DC] 3*(-2+2)/4 = 0,
        #           [LT] critical level: Sugawara tensor undefined
        """
        assert kappa_affine_sl2(Rational(-2)) == Rational(0)


# ===================================================================
# I. Full integration test (1 test)
# ===================================================================

class TestFullVerification:
    """Integration test: run everything."""

    def test_full_verification_passes(self):
        """All verifications pass."""
        result = full_verification()
        assert result["all_passed"] is True
        assert result["jacobi_identity"] is True
        assert result["killing_invariance"] is True
        assert result["m3_verification"]["m3_nonzero"] is True
        assert result["m4_verification"]["m4_vanishes"] is True
        assert result["m4_polynomial"]["polynomial_zero"] is True
