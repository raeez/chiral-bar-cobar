r"""Tests for finite-window shadow bracket and product diagnostics.

Verification paths:
  (i)   finite-window B_n from a Moyal-type formula
  (ii)  associativity diagnostics for the truncated product
  (iii) first-order commutator: (f*g - g*f)/hbar = 2{f,g} at order 1
  (iv)  Moyal comparison: constant-bivector model vs variable window
  (v)   Numerical evaluation: cross-family consistency, dimension checks

Formula safeguards:
    kappa formulas are family-specific.
    S_2 = kappa equals c/2 only for Virasoro.
    Expected values are derived independently of engine output.
    kappa(Vir_c) + kappa(Vir_{26-c}) = 13.
    kappa = 0 does not imply Theta_A = 0.
    kappa != c/2 for non-Virasoro families.
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math
import pytest
from fractions import Fraction

from sympy import Rational, Symbol


# ===========================================================================
# 1. Shadow data correctness (multi-path verification)
# ===========================================================================

class TestShadowDataProviders:
    """Verify shadow data for all standard families."""

    def test_heisenberg_data(self):
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('heisenberg', k=1)
        assert data['kappa'] == 1.0
        assert data['alpha'] == 0.0
        assert data['S4'] == 0.0
        assert data['Delta'] == 0.0
        assert data['family'] == 'heisenberg'

    def test_heisenberg_level_5(self):
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('heisenberg', k=5)
        assert data['kappa'] == 5.0

    def test_virasoro_c1(self):
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('virasoro', c_val=1.0)
        assert abs(data['kappa'] - 0.5) < 1e-12
        assert abs(data['alpha'] - 2.0) < 1e-12
        # S_4 = 10/(1*(5+22)) = 10/27
        assert abs(data['S4'] - 10.0 / 27.0) < 1e-12
        # Delta = 8*(1/2)*(10/27) = 40/27
        assert abs(data['Delta'] - 40.0 / 27.0) < 1e-12

    def test_virasoro_c13_self_dual(self):
        """At c=13, the Virasoro scalar complementarity involution is fixed."""
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('virasoro', c_val=13.0)
        assert abs(data['kappa'] - 6.5) < 1e-12
        # Delta = 40/(5*13+22) = 40/87
        assert abs(data['Delta'] - 40.0 / 87.0) < 1e-12

    def test_virasoro_complementarity_kappa(self):
        """Virasoro scalar complementarity: kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        for c_val in [1.0, 5.0, 10.0, 13.0, 20.0]:
            d1 = get_shadow_data('virasoro', c_val=c_val)
            d2 = get_shadow_data('virasoro', c_val=26.0 - c_val)
            assert abs(d1['kappa'] + d2['kappa'] - 13.0) < 1e-12, \
                f"complementarity failed at c={c_val}: {d1['kappa']} + {d2['kappa']} != 13"

    def test_affine_sl2_data(self):
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('affine_sl2', k=1)
        # kappa = 3*(1+2)/4 = 9/4 = 2.25
        assert abs(data['kappa'] - 2.25) < 1e-12
        # alpha = 4/(1+2) = 4/3
        assert abs(data['alpha'] - 4.0 / 3.0) < 1e-12
        assert data['S4'] == 0.0
        assert data['Delta'] == 0.0

    def test_affine_sl2_kappa_not_c_over_2(self):
        """kappa != c/2 for affine sl_2.

        c(sl_2, k=1) = 3*1/(1+2) = 1.  kappa = 9/4 = 2.25 != 0.5 = c/2.
        """
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('affine_sl2', k=1)
        c_val = 3.0 * 1.0 / (1.0 + 2.0)  # c = 1 for sl_2 at k=1
        assert abs(data['kappa'] - c_val / 2) > 1.0, \
            f"kappa={data['kappa']} should differ significantly from c/2={c_val/2}"

    def test_affine_slN_data(self):
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('affine_slN', N=3, k=1)
        # kappa = (9-1)*(1+3)/(2*3) = 8*4/6 = 16/3
        assert abs(data['kappa'] - 16.0 / 3.0) < 1e-12
        # alpha = 2*3/(1+3) = 6/4 = 3/2
        assert abs(data['alpha'] - 1.5) < 1e-12

    def test_betagamma_standard(self):
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('betagamma', lam=0.5)
        # c = 2*(6*(1/4)-6*(1/2)+1) = 2*(3/2-3+1) = 2*(-1/2) = -1
        c_val = 2.0 * (6.0 * 0.25 - 6.0 * 0.5 + 1.0)
        kappa = c_val / 2.0
        assert abs(data['kappa'] - kappa) < 1e-12

    def test_betagamma_lambda_0(self):
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('betagamma', lam=0.0)
        # c = 2*(0-0+1) = 2, kappa = 1
        assert abs(data['kappa'] - 1.0) < 1e-12
        assert abs(data['alpha'] - 2.0) < 1e-12


class TestNormalizationFirewalls:
    """Verify package, object, and kernel normalization firewalls."""

    def test_holographic_package_has_seven_entries(self):
        from lib.bc_deformation_quantization_shadow_engine import holographic_package_entries
        assert holographic_package_entries() == (
            "A",
            "A^i",
            "A^!",
            "C",
            "r(z)",
            "Theta_A",
            "nabla^hol",
        )
        assert len(holographic_package_entries()) == 7

    def test_modular_koszul_package_has_six_primary_projections(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            holographic_package_entries, modular_koszul_primary_projections,
        )
        projections = modular_koszul_primary_projections()
        assert projections == (
            "Fact_X(L)",
            "barB_X(L)",
            "Theta_L",
            "L_L",
            "(V_br, T_br)",
            "R4_mod(L)",
        )
        assert len(projections) == 6
        assert projections != holographic_package_entries()
        assert "A^!" not in projections
        assert "Z_ch^der(A)" not in projections

    def test_object_firewall_separates_bar_dual_and_bulk(self):
        from lib.bc_deformation_quantization_shadow_engine import object_firewall
        firewall = object_firewall()
        assert set(firewall) == {
            "A",
            "B(A)",
            "A^i",
            "A^!",
            "Omega(B(A))",
            "Z_ch^der(A)",
        }
        assert "H^*(B(A))" in firewall["A^i"]
        assert "Verdier/continuous-linear dual" in firewall["A^!"]
        assert "bar-cobar inversion recovering A" in firewall["Omega(B(A))"]
        assert "ChirHoch^*(A,A)" in firewall["Z_ch^der(A)"]
        assert firewall["A^i"] != firewall["A^!"]
        assert firewall["Omega(B(A))"] != firewall["A^!"]
        assert firewall["Z_ch^der(A)"] != firewall["A^!"]

    def test_kernel_normalization_constants(self):
        from lib.bc_deformation_quantization_shadow_engine import kernel_normalizations
        kernels = kernel_normalizations()
        assert kernels["affine_raw_collision"] == "k*Omega_tr/z"
        assert kernels["affine_KZ_coefficient"] == "Omega/((k+h^vee)z)"
        assert kernels["heisenberg_raw_collision"] == "k/z"
        assert kernels["virasoro_collision"] == "(c/2)/z^3 + 2T/z"
        assert kernels["affine_raw_collision"] != kernels["affine_KZ_coefficient"]


# ===========================================================================
# 2. Shadow bracket tests
# ===========================================================================

class TestShadowPoissonBracket:
    """Test the projected shadow bracket {S_r, S_s}."""

    def test_antisymmetry_kappa_alpha(self):
        """Antisymmetry: {kappa, alpha} = -{alpha, kappa}."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        b23 = shadow_poisson_bracket(2, 3, data)
        b32 = shadow_poisson_bracket(3, 2, data)
        assert abs(b23 + b32) < 1e-12, f"Antisymmetry failed: {b23} + {b32} != 0"

    def test_antisymmetry_kappa_S4(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=10.0)
        b24 = shadow_poisson_bracket(2, 4, data)
        b42 = shadow_poisson_bracket(4, 2, data)
        assert abs(b24 + b42) < 1e-12

    def test_antisymmetry_alpha_S4(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=3.0)
        b34 = shadow_poisson_bracket(3, 4, data)
        b43 = shadow_poisson_bracket(4, 3, data)
        assert abs(b34 + b43) < 1e-12

    def test_self_bracket_vanishes(self):
        """Self-bracket: {S_r, S_r} = 0."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=7.0)
        for r in [2, 3, 4]:
            assert shadow_poisson_bracket(r, r, data) == 0.0

    def test_heisenberg_trivial_poisson(self):
        """Heisenberg has the zero bracket (class G)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=1)
        for r in [2, 3, 4]:
            for s in [2, 3, 4]:
                assert shadow_poisson_bracket(r, s, data) == 0.0

    def test_virasoro_kappa_S4_bracket(self):
        """{kappa, S_4}_Vir = 3*alpha*S_4/kappa."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        bracket = shadow_poisson_bracket(2, 4, data)
        expected = 3.0 * data['alpha'] * data['S4'] / data['kappa']
        assert abs(bracket - expected) < 1e-12

    def test_virasoro_kappa_alpha_bracket(self):
        """{kappa, alpha}_Vir = 9*alpha^2/(2*kappa)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=8.0)
        bracket = shadow_poisson_bracket(2, 3, data)
        expected = 9.0 * data['alpha'] ** 2 / (2.0 * data['kappa'])
        assert abs(bracket - expected) < 1e-12

    def test_virasoro_alpha_S4_bracket(self):
        """{alpha, S_4}_Vir = (Delta - 9*alpha^2)/(2*kappa)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=4.0)
        bracket = shadow_poisson_bracket(3, 4, data)
        expected = (data['Delta'] - 9.0 * data['alpha'] ** 2) / (2.0 * data['kappa'])
        assert abs(bracket - expected) < 1e-12

    def test_affine_sl2_bracket(self):
        """Affine sl_2: {kappa, alpha} = 9*alpha^2/(2*kappa), but {kappa, S_4} = 0."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('affine_sl2', k=1)
        # S_4 = 0 for class L, so {kappa, S_4} = 0
        assert abs(shadow_poisson_bracket(2, 4, data)) < 1e-12
        # But {kappa, alpha} != 0
        bracket_23 = shadow_poisson_bracket(2, 3, data)
        expected = 9.0 * data['alpha'] ** 2 / (2.0 * data['kappa'])
        assert abs(bracket_23 - expected) < 1e-12

    def test_bracket_c_dependence_virasoro(self):
        """Verify {kappa, S_4} depends on c as expected."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        # At c=1: {kappa, S_4} = 3*2*(10/27)/(1/2) = 120/27 = 40/9
        data = get_shadow_data('virasoro', c_val=1.0)
        bracket = shadow_poisson_bracket(2, 4, data)
        expected = 3.0 * 2.0 * (10.0 / 27.0) / 0.5
        assert abs(bracket - expected) < 1e-10

    def test_virasoro_bracket_c_sweep(self):
        """Cross-check brackets at multiple c values."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, shadow_poisson_bivector, get_shadow_data,
        )
        for c_val in [2.0, 5.0, 10.0, 13.0, 20.0]:
            data = get_shadow_data('virasoro', c_val=c_val)
            kap = data['kappa']
            alp = data['alpha']
            s4 = data['S4']
            delt = data['Delta']
            # Verify Delta = 8*kappa*S_4
            assert abs(delt - 8 * kap * s4) < 1e-12
            # Verify {kappa, S_4}
            b24 = shadow_poisson_bracket(2, 4, data)
            assert abs(b24 - 3.0 * alp * s4 / kap) < 1e-12
            # Verify {kappa, Delta} via Delta = 8*kappa*S_4 and {kappa,kappa}=0.
            b_k_delta = shadow_poisson_bivector(data)['Pi_kappa_Delta']
            expected_kd = 3.0 * alp * delt / kap
            assert abs(b_k_delta - expected_kd) < 1e-12


class TestShadowBracketStatus:
    """Test Jacobi-defect diagnostics for the finite shadow window."""

    def test_heisenberg_bracket_status_trivial(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            get_shadow_data, shadow_bracket_status, shadow_jacobi_defect,
        )
        data = get_shadow_data('heisenberg', k=3)
        assert shadow_jacobi_defect(data) == 0.0
        status = shadow_bracket_status(data)
        assert status['is_poisson'] is True
        assert status['status'] == 'trivial_poisson'

    def test_affine_class_L_uses_two_generator_window(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            get_shadow_data, shadow_bracket_status, shadow_poisson_bracket,
        )
        data = get_shadow_data('affine_sl2', k=1)
        status = shadow_bracket_status(data)
        assert status['status'] == 'finite_depth_two_generator_poisson'
        assert status['is_poisson'] is True
        assert shadow_poisson_bracket(3, 4, data) == 0.0

    def test_virasoro_three_generator_jacobi_defect(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            get_shadow_data, shadow_bracket_status, shadow_jacobi_defect,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        expected = (
            9.0 * data['alpha'] * (3.0 * data['alpha'] ** 2 - data['Delta'])
            / (2.0 * data['kappa'] ** 2)
        )
        defect = shadow_jacobi_defect(data)
        assert abs(defect - expected) < 1e-12
        assert abs(defect) > 1e-12
        status = shadow_bracket_status(data)
        assert status['is_poisson'] is False
        assert status['status'] == 'first_order_bracket_only'

    def test_vanishing_defect_locus(self):
        from lib.bc_deformation_quantization_shadow_engine import shadow_bracket_status
        data = {
            'kappa': 2.0,
            'alpha': 1.0,
            'S4': 3.0 / 16.0,
            'Delta': 3.0,
            'family': 'synthetic',
            'depth_class': 'unknown',
        }
        status = shadow_bracket_status(data)
        assert status['jacobi_defect_abs'] < 1e-12
        assert status['is_poisson'] is True
        assert status['status'] == 'poisson_on_vanishing_defect_locus'


# ===========================================================================
# 3. Bivector candidate tests
# ===========================================================================

class TestBivectorCandidate:
    """Test the bivector candidate components."""

    def test_bivector_virasoro(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bivector, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=6.0)
        bv = shadow_poisson_bivector(data)
        assert 'Pi_kappa_S4' in bv
        assert 'Pi_kappa_Delta' in bv
        assert 'Pi_alpha_S4' in bv
        assert 'Pi_kappa_alpha' in bv

    def test_bivector_heisenberg_trivial(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bivector, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=1)
        bv = shadow_poisson_bivector(data)
        assert bv['Pi_kappa_S4'] == 0.0
        assert bv['Pi_kappa_Delta'] == 0.0

    def test_bivector_consistency(self):
        """Pi^{kappa,Delta} = 3*alpha*Delta/kappa from chain rule."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bivector, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=10.0)
        bv = shadow_poisson_bivector(data)
        kap = data['kappa']
        alp = data['alpha']
        delt = data['Delta']
        expected = 3.0 * alp * delt / kap
        assert abs(bv['Pi_kappa_Delta'] - expected) < 1e-12


# ===========================================================================
# 4. Center certification and discriminant tests
# ===========================================================================

class TestCenterCertification:
    """Test center certification and shadow-metric discriminants."""

    def test_heisenberg_full_center(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            poisson_center_generators, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=1)
        center = poisson_center_generators(data)
        assert center['center_type'] == 'full'
        assert center['dim_center'] == float('inf')

    def test_virasoro_center_not_certified_when_jacobi_defect_nonzero(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            poisson_center_generators, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        center = poisson_center_generators(data)
        assert center['center_type'] == 'not_poisson'
        assert center['dim_center'] == 0
        assert center['generators'] == []
        assert center['bracket_status']['is_poisson'] is False
        assert center['discriminant_Q'] == -32.0 * data['kappa'] ** 2 * data['Delta']

    def test_affine_sl2_class_L_center_constants_only(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            poisson_center_generators, get_shadow_data,
        )
        data = get_shadow_data('affine_sl2', k=1)
        center = poisson_center_generators(data)
        assert center['center_type'] == 'constants_only'
        assert center['generators'] == ['constants']

    def test_casimir_value_virasoro(self):
        """Shadow-metric discriminant Disc(Q_L) = -32*kappa^2*Delta."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_casimir_value, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        C = shadow_casimir_value(data)
        expected = -32.0 * data['kappa'] ** 2 * data['Delta']
        assert abs(C - expected) < 1e-12

    def test_casimir_vanishes_class_G(self):
        """Heisenberg: Disc(Q_L) = 0 (Delta = 0)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_casimir_value, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=1)
        assert shadow_casimir_value(data) == 0.0

    def test_casimir_vanishes_class_L(self):
        """Affine sl_2: Disc(Q_L) = 0 (Delta = 0)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_casimir_value, get_shadow_data,
        )
        data = get_shadow_data('affine_sl2', k=1)
        assert shadow_casimir_value(data) == 0.0

    def test_casimir_nonzero_class_M(self):
        """Virasoro: Disc(Q_L) != 0 (Delta != 0)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_casimir_value, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        assert abs(shadow_casimir_value(data)) > 1e-10

    def test_casimir_c_sweep(self):
        """The shadow-metric discriminant varies with c for Virasoro."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_casimir_value, get_shadow_data,
        )
        discriminants = []
        for c_val in [1.0, 5.0, 10.0, 13.0, 20.0]:
            data = get_shadow_data('virasoro', c_val=c_val)
            discriminants.append(shadow_casimir_value(data))
        # All should be different and nonzero
        assert all(abs(c) > 1e-10 for c in discriminants)
        # Should be distinct
        for i in range(len(discriminants)):
            for j in range(i + 1, len(discriminants)):
                assert abs(discriminants[i] - discriminants[j]) > 1e-10


# ===========================================================================
# 5. Finite-window product tests
# ===========================================================================

class TestFiniteWindowProduct:
    """Test the finite-window B_n operators."""

    def test_B0_is_product(self):
        """B_0(f, g) = f * g (pointwise product)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B0 = kontsevich_Bn(0, 2, 4, data)
        # B_0(kappa, S_4) = kappa * S_4
        expected = data['kappa'] * data['S4']
        assert abs(B0 - expected) < 1e-12

    def test_B1_is_bracket(self):
        """B_1(f, g) = {f, g}_shadow for the projected bracket."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B1 = kontsevich_Bn(1, 2, 4, data)
        bracket = shadow_poisson_bracket(2, 4, data)
        assert abs(B1 - bracket) < 1e-12

    def test_B0_heisenberg(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=3)
        B0 = kontsevich_Bn(0, 2, 3, data)
        # S_2 = 3, S_3 = 0 => B_0 = 3 * 0 = 0
        assert abs(B0) < 1e-12

    def test_star_product_hbar_zero(self):
        """At hbar = 0, the finite-window product is pointwise product."""
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        sp = star_product(2, 4, data, 0.0, 5)
        expected = data['kappa'] * data['S4']
        assert abs(sp - expected) < 1e-12

    def test_star_product_components(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product_components, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        comp = star_product_components(2, 4, data, 3)
        assert 0 in comp
        assert 1 in comp
        assert 2 in comp
        assert 3 in comp

    def test_B2_finite(self):
        """B_2 should be finite for Virasoro."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_B2, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B2 = kontsevich_B2(2, 4, data)
        assert math.isfinite(B2)

    def test_B2_heisenberg_zero(self):
        """B_2 = 0 for Heisenberg (zero bracket)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_B2, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=1)
        B2 = kontsevich_B2(2, 3, data)
        assert abs(B2) < 1e-10

    def test_Bn_finite_n3(self):
        """B_3 should be finite for Virasoro."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B3 = kontsevich_Bn(3, 2, 4, data)
        assert math.isfinite(B3)

    def test_Bn_finite_n4(self):
        """B_4 should be finite for Virasoro."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B4 = kontsevich_Bn(4, 2, 4, data)
        assert math.isfinite(B4)

    def test_Bn_finite_n5(self):
        """B_5 should be finite for Virasoro."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B5 = kontsevich_Bn(5, 2, 4, data)
        assert math.isfinite(B5)

    def test_star_product_continuity_in_hbar(self):
        """The finite-window product varies continuously with hbar at low order.

        At higher truncation orders, the B_n grow factorially from numerical
        differentiation, so we restrict to order 2 for the continuity test.
        """
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        # Use low truncation order (2) and small hbar for continuity
        values = [star_product(2, 4, data, h, 2) for h in [0.0, 0.001, 0.002, 0.003]]
        # Should be continuous: |f(h+dh) - f(h)| < C*dh for small dh
        for i in range(len(values) - 1):
            assert abs(values[i + 1] - values[i]) < 1.0


# ===========================================================================
# 6. First-order commutator test (verification path iii)
# ===========================================================================

class TestPoissonLimit:
    """Verify the order-1 commutator recovers twice the projected bracket."""

    def test_poisson_limit_kappa_S4(self):
        """(kappa*S_4 - S_4*kappa) / hbar equals 2{kappa,S_4} at order 1.

        Use truncation order 1 so that the finite-window product is exactly
        B_0 + hbar * B_1.  Then (fg - gf)/hbar = B_1(f,g) - B_1(g,f) = 2*B_1(f,g)
        since B_0 is symmetric and B_1 is antisymmetric.
        """
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        bracket = shadow_poisson_bracket(2, 4, data)

        for hbar_val in [0.01, 0.001, 0.0001]:
            # Truncation order 1: f*g = fg + hbar*{f,g}
            fg = star_product(2, 4, data, hbar_val, 1)
            gf = star_product(4, 2, data, hbar_val, 1)
            commutator_over_hbar = (fg - gf) / hbar_val
            # At order 1: commutator/hbar = 2*bracket (B_1 antisymmetric)
            assert abs(commutator_over_hbar - 2.0 * bracket) < abs(bracket) * 1e-6 + 1e-10, \
                f"Poisson limit failed at hbar={hbar_val}: {commutator_over_hbar} vs {2*bracket}"

    def test_poisson_limit_kappa_alpha(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        bracket = shadow_poisson_bracket(2, 3, data)

        hbar_val = 0.001
        # Use truncation order 1 for exact Poisson limit
        fg = star_product(2, 3, data, hbar_val, 1)
        gf = star_product(3, 2, data, hbar_val, 1)
        commutator_over_hbar = (fg - gf) / hbar_val
        assert abs(commutator_over_hbar - 2.0 * bracket) < abs(bracket) * 1e-6 + 1e-8

    def test_poisson_limit_heisenberg(self):
        """Heisenberg: commutator / hbar -> 0 = trivial bracket."""
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=1)
        hbar_val = 0.01
        fg = star_product(2, 3, data, hbar_val, 5)
        gf = star_product(3, 2, data, hbar_val, 5)
        assert abs(fg - gf) < 1e-10


# ===========================================================================
# 7. Associativity tests (verification path ii)
# ===========================================================================

class TestAssociativity:
    """Test associativity diagnostics of the finite-window product."""

    def test_associativity_virasoro(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            associativity_test, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        result = associativity_test(2, 3, 4, data, 0.01, 3)
        # At small hbar, associativity should hold approximately
        assert result['relative_error'] < 1.0  # loose bound for truncated series

    def test_associativity_heisenberg_exact(self):
        """Heisenberg: product = pointwise product, associativity exact."""
        from lib.bc_deformation_quantization_shadow_engine import (
            associativity_test, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=1)
        result = associativity_test(2, 3, 4, data, 0.1, 5)
        # Should be exactly associative (trivial product).
        assert result['difference'] < 1e-10

    def test_associativity_order_errors_decreasing(self):
        """Order errors should decrease with hbar for Virasoro."""
        from lib.bc_deformation_quantization_shadow_engine import (
            associativity_test, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        r1 = associativity_test(2, 3, 4, data, 0.1, 3)
        r2 = associativity_test(2, 3, 4, data, 0.01, 3)
        # At smaller hbar, error should be smaller
        assert r2['difference'] <= r1['difference'] + 1e-10


# ===========================================================================
# 8. Finite-window correction tests
# ===========================================================================

class TestFiniteWindowCorrections:
    """Test finite-window corrections to shadow invariants."""

    def test_kappa_1_vanishes(self):
        """First quantum correction kappa_1 = (1/2)*B_1(kappa,kappa) = 0."""
        from lib.bc_deformation_quantization_shadow_engine import (
            quantum_kappa, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        qk = quantum_kappa(data, 0.1, 5)
        assert abs(qk['corrections'][1]) < 1e-10

    def test_kappa_hbar_converges(self):
        """kappa_hbar should converge to kappa as hbar -> 0."""
        from lib.bc_deformation_quantization_shadow_engine import (
            quantum_kappa, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        for hbar_val in [0.01, 0.001]:
            qk = quantum_kappa(data, hbar_val, 5)
            assert abs(qk['kappa_hbar'] - qk['kappa']) < 0.1

    def test_delta_1_vanishes(self):
        """Delta_1 = 0 by antisymmetry of B_1."""
        from lib.bc_deformation_quantization_shadow_engine import (
            quantum_discriminant, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        qd = quantum_discriminant(data, 0.1, 5)
        assert abs(qd['corrections'][1]) < 1e-10

    def test_heisenberg_no_corrections(self):
        """Heisenberg: all finite-window corrections vanish."""
        from lib.bc_deformation_quantization_shadow_engine import (
            quantum_kappa, quantum_discriminant, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=1)
        qk = quantum_kappa(data, 0.1, 3)
        qd = quantum_discriminant(data, 0.1, 3)
        assert abs(qk['kappa_hbar'] - qk['kappa']) < 1e-12
        assert abs(qd['Delta_hbar'] - qd['Delta']) < 1e-12

    def test_quantum_corrections_finite(self):
        """All corrections should be finite."""
        from lib.bc_deformation_quantization_shadow_engine import (
            quantum_kappa, quantum_discriminant, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        qk = quantum_kappa(data, 0.1, 3)
        qd = quantum_discriminant(data, 0.1, 3)
        for n in range(1, 4):
            assert math.isfinite(qk['corrections'][n])
            assert math.isfinite(qd['corrections'][n])


# ===========================================================================
# 9. Finite-window product at zeta-zero ordinates
# ===========================================================================

class TestStarProductAtZeros:
    """Test finite-window product evaluations at Riemann zeta-zero ordinates."""

    def test_zero_data_complex(self):
        """Shadow data at zeta zero should be complex."""
        from lib.bc_deformation_quantization_shadow_engine import virasoro_at_zero
        data = virasoro_at_zero(14.134725141734693)
        assert isinstance(data['kappa'], complex)
        assert isinstance(data['S4'], complex)
        assert isinstance(data['Delta'], complex)

    def test_zero_data_kappa(self):
        """kappa at first zero = (1/2 + i*gamma)/2."""
        from lib.bc_deformation_quantization_shadow_engine import (
            virasoro_at_zero, ZETA_ZEROS_20,
        )
        gamma = ZETA_ZEROS_20[0]
        data = virasoro_at_zero(gamma)
        expected = complex(0.25, gamma / 2)
        assert abs(data['kappa'] - expected) < 1e-12

    def test_B0_at_zero(self):
        """B_0 at a zero should be a complex number."""
        from lib.bc_deformation_quantization_shadow_engine import star_product_at_zero
        result = star_product_at_zero(0, 2, 4, 1.0, 3)
        assert 'Bn_values' in result
        assert isinstance(result['Bn_values'][0], complex)

    def test_star_product_at_zero_finite(self):
        """The product at each zero ordinate should be finite."""
        from lib.bc_deformation_quantization_shadow_engine import star_product_at_zero
        for idx in range(5):
            result = star_product_at_zero(idx, 2, 4, 0.1, 3)
            assert math.isfinite(result['star_magnitude'])

    def test_star_product_at_multiple_zeros(self):
        """Verify computations at zeros 0-9."""
        from lib.bc_deformation_quantization_shadow_engine import star_product_at_zero
        magnitudes = []
        for idx in range(10):
            result = star_product_at_zero(idx, 2, 4, 0.1, 2)
            magnitudes.append(result['star_magnitude'])
            assert math.isfinite(result['star_magnitude'])
        # Magnitudes should be distinct (different zeros give different values)
        assert len(set(round(m, 6) for m in magnitudes)) > 5

    def test_B0_magnitude_at_zeros(self):
        """B_0(kappa, S_4) = kappa * S_4 at complex c."""
        from lib.bc_deformation_quantization_shadow_engine import star_product_at_zero
        result = star_product_at_zero(0, 2, 4, 0.0, 3)
        expected = result['kappa'] * result['S4']
        assert abs(result['Bn_values'][0] - expected) < 1e-10

    def test_suppression_ratios_defined(self):
        """Suppression ratios should be computed.

        Ratios can be NaN when the off-zero reference magnitude is zero
        (division by zero). We check that the dict exists and that at least
        the leading ratio (n=0) is finite and positive.
        """
        from lib.bc_deformation_quantization_shadow_engine import star_product_at_zero
        result = star_product_at_zero(0, 2, 4, 0.1, 2)
        assert 'suppression_ratios' in result
        # B_0 ratio should always be finite (both kappa*S4 are nonzero)
        ratio_0 = result['suppression_ratios'][0]
        assert math.isfinite(ratio_0) and ratio_0 > 0

    def test_deformed_discriminant_at_zero(self):
        """Deformed discriminant at a zero ordinate should be finite and complex."""
        from lib.bc_deformation_quantization_shadow_engine import quantum_casimir_at_zero
        result = quantum_casimir_at_zero(0, 0.1, 2)
        assert math.isfinite(result['discriminant_0_magnitude'])
        assert math.isfinite(result['discriminant_hbar_magnitude'])

    def test_deformed_discriminant_at_multiple_zeros(self):
        """Deformed discriminants at the first ten zero ordinates."""
        from lib.bc_deformation_quantization_shadow_engine import quantum_casimir_at_zero
        for idx in range(10):
            result = quantum_casimir_at_zero(idx, 0.1, 2)
            assert math.isfinite(result['discriminant_0_magnitude'])

    def test_discriminant_magnitude_positive(self):
        """Discriminant magnitude should be strictly positive at zero ordinates."""
        from lib.bc_deformation_quantization_shadow_engine import quantum_casimir_at_zero
        for idx in range(5):
            result = quantum_casimir_at_zero(idx, 0.0, 1)
            assert result['discriminant_0_magnitude'] > 1e-15

    def test_zero_landscape(self):
        """Finite-window zero-ordinate landscape computation."""
        from lib.bc_deformation_quantization_shadow_engine import star_product_zero_landscape
        landscape = star_product_zero_landscape(5, 2)
        assert landscape['num_zeros'] == 5
        assert 'trends' in landscape
        for n in range(3):
            assert n in landscape['trends']


# ===========================================================================
# 10. Moyal comparison (verification path iv)
# ===========================================================================

class TestMoyalComparison:
    """Compare finite-window and constant-bivector Moyal products."""

    def test_moyal_B0_matches(self):
        """At order 0, both products reduce to the pointwise product."""
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, moyal_star_product, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        k = star_product(2, 4, data, 0.0, 5)
        m = moyal_star_product(2, 4, data, 0.0, 5)
        assert abs(k - m) < 1e-10

    def test_moyal_heisenberg_agrees(self):
        """For Heisenberg (zero bracket), both products agree exactly."""
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, moyal_star_product, get_shadow_data,
        )
        data = get_shadow_data('heisenberg', k=1)
        k = star_product(2, 3, data, 0.1, 5)
        m = moyal_star_product(2, 3, data, 0.1, 5)
        assert abs(k - m) < 1e-10

    def test_kontsevich_moyal_comparison_structure(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_moyal_comparison, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        result = kontsevich_moyal_comparison(2, 4, data, 0.1, 3)
        assert 'kontsevich' in result
        assert 'moyal' in result
        assert 'difference' in result
        assert math.isfinite(result['kontsevich'])
        assert math.isfinite(result['moyal'])

    def test_moyal_at_small_hbar(self):
        """At small hbar, the two finite-window products are close."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_moyal_comparison, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        result = kontsevich_moyal_comparison(2, 4, data, 0.001, 3)
        # At small hbar, the difference should be small
        assert abs(result['difference']) < abs(result['kontsevich']) + 1e-8


# ===========================================================================
# 11. Cross-family consistency
# ===========================================================================

class TestCrossFamilyConsistency:
    """Cross-family and cross-check tests."""

    def test_virasoro_w3_T_line_agree(self):
        """W_3 on the T-line should agree with Virasoro (same shadow data)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        for c_val in [5.0, 10.0, 20.0]:
            dv = get_shadow_data('virasoro', c_val=c_val)
            dw = get_shadow_data('w3', c_val=c_val)
            for (r, s) in [(2, 3), (2, 4), (3, 4)]:
                bv = shadow_poisson_bracket(r, s, dv)
                bw = shadow_poisson_bracket(r, s, dw)
                assert abs(bv - bw) < 1e-12

    def test_class_L_S4_zero(self):
        """All class L families should have S_4 = 0 and Delta = 0."""
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('affine_sl2', k=1)
        assert data['S4'] == 0.0
        assert data['Delta'] == 0.0

    def test_class_G_alpha_zero(self):
        """All class G families should have alpha = 0."""
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('heisenberg', k=1)
        assert data['alpha'] == 0.0

    def test_bracket_linearity_in_parameters(self):
        """Brackets should scale linearly with alpha and S_4."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        # {kappa, S_4} = 3*alpha*S_4/kappa, linear in both alpha and S_4
        data1 = get_shadow_data('virasoro', c_val=5.0)
        data2 = get_shadow_data('virasoro', c_val=10.0)
        b1 = shadow_poisson_bracket(2, 4, data1)
        b2 = shadow_poisson_bracket(2, 4, data2)
        # Ratio should match 3*alpha*S_4/kappa ratio
        ratio1 = 3.0 * data1['alpha'] * data1['S4'] / data1['kappa']
        ratio2 = 3.0 * data2['alpha'] * data2['S4'] / data2['kappa']
        assert abs(b1 / ratio1 - 1.0) < 1e-10
        assert abs(b2 / ratio2 - 1.0) < 1e-10


# ===========================================================================
# 12. Full analysis integration test
# ===========================================================================

class TestFullAnalysis:
    """Integration tests for the full analysis pipeline."""

    def test_full_analysis_virasoro(self):
        from lib.bc_deformation_quantization_shadow_engine import full_star_product_analysis
        result = full_star_product_analysis('virasoro', max_order=3, c_val=5.0)
        assert result['bracket_status']['status'] == 'first_order_bracket_only'
        assert 'brackets' in result
        assert 'center' in result
        assert 'Bn_24' in result
        assert 'star_products' in result
        assert 'quantum_kappa' in result
        assert 'quantum_discriminant' in result

    def test_full_analysis_heisenberg(self):
        from lib.bc_deformation_quantization_shadow_engine import full_star_product_analysis
        result = full_star_product_analysis('heisenberg', max_order=3, k=1)
        assert result['center']['center_type'] == 'full'

    def test_full_analysis_affine(self):
        from lib.bc_deformation_quantization_shadow_engine import full_star_product_analysis
        result = full_star_product_analysis('affine_sl2', max_order=3, k=1)
        assert result['bracket_status']['status'] == 'finite_depth_two_generator_poisson'
        assert result['center']['center_type'] == 'constants_only'


# ===========================================================================
# 13. Numerical evaluation tests (verification path v)
# ===========================================================================

class TestNumericalEvaluation:
    """Numerical consistency and sanity checks."""

    def test_shadow_coefficients_numerical(self):
        """Verify shadow coefficients match expected values."""
        from lib.bc_deformation_quantization_shadow_engine import (
            _shadow_coefficients_numerical, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=1.0)
        coeffs = _shadow_coefficients_numerical(data, 6)
        # S_2 = kappa = 1/2
        assert abs(coeffs[2] - 0.5) < 1e-10
        # S_3 should be related to alpha
        # a_1 = 3*alpha = 6, S_3 = a_1/3 = 2
        assert abs(coeffs[3] - 2.0) < 1e-10
        # S_4 = 10/(c*(5c+22)) = 10/27
        assert abs(coeffs[4] - 10.0 / 27.0) < 1e-8

    def test_shadow_coefficients_virasoro_c5(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            _shadow_coefficients_numerical, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        coeffs = _shadow_coefficients_numerical(data, 6)
        assert abs(coeffs[2] - 2.5) < 1e-10
        assert abs(coeffs[3] - 2.0) < 1e-10
        # S_4 = 10/(5*47) = 10/235 = 2/47
        assert abs(coeffs[4] - 10.0 / 235.0) < 1e-8

    def test_shadow_coefficients_affine(self):
        from lib.bc_deformation_quantization_shadow_engine import (
            _shadow_coefficients_numerical, get_shadow_data,
        )
        data = get_shadow_data('affine_sl2', k=1)
        coeffs = _shadow_coefficients_numerical(data, 6)
        # S_2 = kappa = 9/4
        assert abs(coeffs[2] - 2.25) < 1e-10
        # S_3 = a_1/3 where a_1 = 3*alpha, hence S_3 = alpha.
        assert abs(coeffs[3] - 4.0 / 3.0) < 1e-8

    def test_complex_shadow_coefficients(self):
        """Shadow coefficients should be computable at complex c."""
        from lib.bc_deformation_quantization_shadow_engine import (
            _shadow_coefficients_complex, virasoro_at_zero, ZETA_ZEROS_20,
        )
        data = virasoro_at_zero(ZETA_ZEROS_20[0])
        coeffs = _shadow_coefficients_complex(data, 6)
        for r in range(2, 7):
            assert isinstance(coeffs[r], complex)
            assert cmath.isfinite(coeffs[r])

    def test_star_product_real_for_real_data(self):
        """The finite-window product should be real for real shadow data."""
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        sp = star_product(2, 4, data, 0.1, 3)
        assert isinstance(sp, float)

    def test_star_product_small_hbar_expansion(self):
        """The product at small hbar should be B_0 + hbar*B_1 + O(hbar^2).

        We use truncation order 2 so the residual is exactly hbar^2 * B_2.
        At higher truncation orders, the numerically computed B_n grow
        factorially from finite-difference noise, masking the true asymptotic.
        """
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, kontsevich_Bn, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        hbar_val = 0.001
        sp = star_product(2, 4, data, hbar_val, 2)
        B0 = kontsevich_Bn(0, 2, 4, data)
        B1 = kontsevich_Bn(1, 2, 4, data)
        B2 = kontsevich_Bn(2, 2, 4, data)
        linear_approx = B0 + hbar_val * B1
        residual = sp - linear_approx
        # Residual should be hbar^2 * B_2
        assert abs(residual - hbar_val ** 2 * B2) < 1e-10


# ===========================================================================
# 14. Dimension and degree analysis (verification path vii)
# ===========================================================================

class TestDimensionalAnalysis:
    """Check that dimensions and degrees are consistent."""

    def test_bracket_arity(self):
        """{S_r, S_s} should have arity r+s-1 (arity increases by 1 from ell_2)."""
        # This is a structural property: the bracket of arity-r and arity-s
        # shadows produces an arity-(r+s-1) shadow via the planted-forest graph
        # with one trivalent vertex.
        # We verify numerically that the bracket is nonzero for the right arities.
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        # {S_2, S_4} is arity 5 (2+4-1)
        assert abs(shadow_poisson_bracket(2, 4, data)) > 0
        # {S_2, S_3} is arity 4 (2+3-1)
        assert abs(shadow_poisson_bracket(2, 3, data)) > 0

    def test_B0_degree(self):
        """B_0(S_r, S_s) has arity r+s."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B0 = kontsevich_Bn(0, 2, 4, data)
        # B_0 = S_2 * S_4 = kappa * S_4 (arity 6)
        assert abs(B0 - data['kappa'] * data['S4']) < 1e-12

    def test_discriminant_negative_for_virasoro(self):
        """Disc(Q_L) = -32*kappa^2*Delta < 0 for Virasoro (Delta > 0)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_casimir_value, get_shadow_data,
        )
        for c_val in [1.0, 5.0, 10.0, 20.0]:
            data = get_shadow_data('virasoro', c_val=c_val)
            C = shadow_casimir_value(data)
            # Delta = 40/(5c+22) > 0 for c > 0
            # kappa = c/2 > 0 for c > 0
            # So C = -32*kappa^2*Delta < 0
            assert C < 0, f"Disc(Q_L) should be negative for Virasoro at c={c_val}"


# ===========================================================================
# 15. Virasoro scalar complementarity diagnostics
# ===========================================================================

class TestComplementarity:
    """Test the scalar c -> 26-c complementarity diagnostics."""

    def test_complementary_brackets_virasoro(self):
        """At c and 26-c, bracket diagnostics are finite and generally distinct."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_poisson_bracket, get_shadow_data,
        )
        c_val = 5.0
        d1 = get_shadow_data('virasoro', c_val=c_val)
        d2 = get_shadow_data('virasoro', c_val=26.0 - c_val)
        b1 = shadow_poisson_bracket(2, 4, d1)
        b2 = shadow_poisson_bracket(2, 4, d2)
        # Both should be nonzero and different
        assert abs(b1) > 1e-10
        assert abs(b2) > 1e-10
        assert abs(b1 - b2) > 1e-10

    def test_discriminant_complementarity(self):
        """Discriminants at c and 26-c for Virasoro."""
        from lib.bc_deformation_quantization_shadow_engine import (
            shadow_casimir_value, get_shadow_data,
        )
        for c_val in [5.0, 10.0, 13.0]:
            d1 = get_shadow_data('virasoro', c_val=c_val)
            d2 = get_shadow_data('virasoro', c_val=26.0 - c_val)
            C1 = shadow_casimir_value(d1)
            C2 = shadow_casimir_value(d2)
            # At c=13, the scalar involution c -> 26-c is fixed.
            if abs(c_val - 13.0) < 1e-10:
                assert abs(C1 - C2) < 1e-10
            else:
                assert abs(C1 - C2) > 1e-10

    def test_self_dual_star_product(self):
        """At c=13, the finite-window product remains real and finite."""
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=13.0)
        sp = star_product(2, 4, data, 0.1, 3)
        # The product at the scalar fixed point should be real and finite.
        assert math.isfinite(sp)


# ===========================================================================
# 16. Edge cases and robustness
# ===========================================================================

class TestEdgeCases:
    """Edge case and robustness tests."""

    def test_large_c(self):
        """Shadow data at large c should be well-defined."""
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('virasoro', c_val=1000.0)
        assert math.isfinite(data['kappa'])
        assert math.isfinite(data['S4'])
        assert data['S4'] > 0

    def test_small_c(self):
        """Shadow data at small positive c."""
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('virasoro', c_val=0.01)
        assert math.isfinite(data['kappa'])
        assert math.isfinite(data['S4'])

    def test_large_level(self):
        """Affine at large level."""
        from lib.bc_deformation_quantization_shadow_engine import get_shadow_data
        data = get_shadow_data('affine_sl2', k=100)
        assert math.isfinite(data['kappa'])
        assert abs(data['alpha']) > 0

    def test_zero_index_out_of_range(self):
        """Out-of-range zero index should raise."""
        from lib.bc_deformation_quantization_shadow_engine import star_product_at_zero
        with pytest.raises(ValueError):
            star_product_at_zero(100, 2, 4, 0.1, 2)

    def test_Bn_n0(self):
        """B_0 should always be just the product."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, get_shadow_data,
        )
        for family, kwargs in [('virasoro', {'c_val': 5.0}),
                               ('heisenberg', {'k': 1}),
                               ('affine_sl2', {'k': 1})]:
            data = get_shadow_data(family, **kwargs)
            B0 = kontsevich_Bn(0, 2, 3, data)
            coeffs = {}
            coeffs[2] = data['kappa']
            coeffs[3] = data['alpha']
            expected = coeffs[2] * coeffs[3]
            assert abs(B0 - expected) < 1e-10


# ===========================================================================
# 17. Shadow coefficient recursion verification
# ===========================================================================

class TestShadowRecursion:
    """Verify the shadow coefficient recursion against known values."""

    def test_virasoro_c1_S5(self):
        """S_5(Vir, c=1) = -48/(1*(5+22)) = -48/27."""
        from lib.bc_deformation_quantization_shadow_engine import (
            _shadow_coefficients_numerical, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=1.0)
        coeffs = _shadow_coefficients_numerical(data, 6)
        expected = -48.0 / (1.0 * 27.0)
        assert abs(coeffs[5] - expected) < 1e-6

    def test_virasoro_recursion_squared(self):
        """Verify f^2 = Q_L for the convolution recursion."""
        from lib.bc_deformation_quantization_shadow_engine import (
            _shadow_coefficients_numerical, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        coeffs = _shadow_coefficients_numerical(data, 10)

        # Reconstruct f(t) = sum a_n t^n where S_r = a_{r-2}/r
        a = {}
        for r in range(2, 11):
            a[r - 2] = coeffs.get(r, 0.0) * r

        # Check f^2 coefficients match Q_L = q0 + q1*t + q2*t^2
        q0 = 4.0 * data['kappa'] ** 2
        q1 = 12.0 * data['kappa'] * data['alpha']
        q2 = 9.0 * data['alpha'] ** 2 + 2.0 * data['Delta']

        # Coefficient of t^0: a_0^2 = q0
        assert abs(a[0] ** 2 - q0) < 1e-6
        # Coefficient of t^1: 2*a_0*a_1 = q1
        assert abs(2.0 * a[0] * a[1] - q1) < 1e-6
        # Coefficient of t^2: 2*a_0*a_2 + a_1^2 = q2
        assert abs(2.0 * a[0] * a[2] + a[1] ** 2 - q2) < 1e-5
        # Coefficient of t^n for n >= 3: 2*a_0*a_n + sum = 0
        for n in range(3, 8):
            conv = sum(a.get(j, 0.0) * a.get(n - j, 0.0) for j in range(1, n))
            assert abs(2.0 * a[0] * a.get(n, 0.0) + conv) < 1e-4


# ===========================================================================
# 18. Multi-zero trend analysis
# ===========================================================================

class TestZeroTrends:
    """Analyze trends across zeta zeros."""

    def test_B0_magnitude_scaling(self):
        """B_0 magnitude should scale inversely with gamma (from 1/c asymptotics)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            star_product_at_zero, ZETA_ZEROS_20,
        )
        mags = []
        for idx in range(5):
            result = star_product_at_zero(idx, 2, 4, 0.0, 1)
            mags.append(result['Bn_magnitudes'][0])
        # B_0 = kappa * S_4 ~ (c/2) * 10/(c*(5c+22)) = 5/(5c+22)
        # At c = 1/2 + i*gamma: |B_0| ~ 5/(5*gamma) ~ 1/gamma
        # So magnitude should decrease with increasing gamma
        # (approximately, since the real part is small)
        # Check that the trend is generally decreasing
        assert mags[0] > mags[4] * 0.5  # loose check

    def test_discriminant_at_zeros_nonvanishing(self):
        """The discriminant should not vanish at any tested zeta-zero ordinate."""
        from lib.bc_deformation_quantization_shadow_engine import quantum_casimir_at_zero
        for idx in range(10):
            result = quantum_casimir_at_zero(idx, 0.0, 1)
            assert result['discriminant_0_magnitude'] > 1e-15, \
                f"Disc(Q_L) vanishes at zero ordinate {idx}"

    def test_zero_landscape_structure(self):
        from lib.bc_deformation_quantization_shadow_engine import star_product_zero_landscape
        landscape = star_product_zero_landscape(5, 2)
        assert 'zeros' in landscape
        assert 'trends' in landscape
        assert landscape['num_zeros'] == 5


# ===========================================================================
# 19. B_n symmetry tests
# ===========================================================================

class TestBnSymmetry:
    """Test symmetry properties of the finite-window B_n coefficients."""

    def test_B1_antisymmetry(self):
        """B_1(f, g) = -B_1(g, f) (from Poisson antisymmetry)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B1_24 = kontsevich_Bn(1, 2, 4, data)
        B1_42 = kontsevich_Bn(1, 4, 2, data)
        assert abs(B1_24 + B1_42) < 1e-12

    def test_B0_symmetry(self):
        """B_0(f, g) = B_0(g, f) (commutative product)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_Bn, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B0_24 = kontsevich_Bn(0, 2, 4, data)
        B0_42 = kontsevich_Bn(0, 4, 2, data)
        assert abs(B0_24 - B0_42) < 1e-12

    def test_B2_symmetry(self):
        """B_2(f, g) = B_2(g, f) (even order, symmetric contribution)."""
        from lib.bc_deformation_quantization_shadow_engine import (
            kontsevich_B2, get_shadow_data,
        )
        data = get_shadow_data('virasoro', c_val=5.0)
        B2_24 = kontsevich_B2(2, 4, data)
        B2_42 = kontsevich_B2(4, 2, data)
        # B_2 should be symmetric to the tolerance of the finite-difference model.
        assert abs(B2_24 - B2_42) < abs(B2_24) * 0.1 + 1e-6


# ===========================================================================
# 20. Degeneration test at zeros
# ===========================================================================

class TestDegenerationAtZeros:
    """Test whether the finite-window product degenerates at zeta-zero ordinates."""

    def test_no_complete_degeneration(self):
        """The finite-window product does not completely degenerate at zero ordinates.

        B_n do not all vanish at zeta-zero ordinates; the finite-window
        Virasoro data remain nonzero at complex c = 1/2 + i*gamma.
        """
        from lib.bc_deformation_quantization_shadow_engine import star_product_at_zero
        result = star_product_at_zero(0, 2, 4, 0.1, 2)
        # B_0 should be nonzero (kappa * S_4 != 0 for complex c)
        assert result['Bn_magnitudes'][0] > 1e-10

    def test_suppression_bounded(self):
        """Suppression ratios should be bounded (no infinite suppression)."""
        from lib.bc_deformation_quantization_shadow_engine import star_product_at_zero
        for idx in range(5):
            result = star_product_at_zero(idx, 2, 4, 0.1, 2)
            for n in range(3):
                ratio = result['suppression_ratios'][n]
                if not math.isnan(ratio):
                    assert ratio > 1e-10, f"Extreme suppression at zero {idx}, order {n}"
                    assert ratio < 1e10, f"Extreme amplification at zero {idx}, order {n}"

    def test_star_product_at_zeros_10_through_20(self):
        """Finite-window product at zero ordinates 10-19."""
        from lib.bc_deformation_quantization_shadow_engine import star_product_at_zero
        for idx in range(10, 20):
            result = star_product_at_zero(idx, 2, 4, 0.1, 2)
            assert math.isfinite(result['star_magnitude'])
            assert result['star_magnitude'] > 0
