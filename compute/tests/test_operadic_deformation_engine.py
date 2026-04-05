#!/usr/bin/env python3
r"""Tests for the operadic deformation engine.

T1-T7:   Modular operad M = {C_*(M_bar_{g,n})} — Euler characteristics, Betti, stability
T8-T13:  Feynman transform FCom — graph enumeration, B(A) as FCom-algebra
T14-T18: Deformation complex Def(A) — dimensions, MC equation at each arity
T19-T24: Operadic Rankin-Selberg — L-function multiplicativity, direct sum
T25-T31: Newton's identities from MC — Virasoro through r=6, single atom
T32-T37: Operadic deformation quantization — first-order, obstruction = kappa
T38-T44: Shadow depth classification — G/L/C/M classes, shadow metric
T45-T50: Full engine integration — all families, cross-checks

MAIN STRUCTURAL INSIGHT: The modular operad M controls everything.
Algebras over M = factorization algebras. MC in Hom(M!, End_A) = shadow obstruction tower.
The operadic Rankin-Selberg converts shadow data to L-functions.
Kappa = simultaneously curvature, shadow, obstruction, anomaly.

References:
  thm:bar-modular-operad (bar_cobar_adjunction_curved.tex)
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  thm:operadic-rankin-selberg (arithmetic_shadows.tex)
  prop:mc-bracket-determines-atoms (arithmetic_shadows.tex)
  prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
"""

import math
import os
import sys

import pytest
from sympy import Rational, S, Symbol, oo, simplify

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from operadic_deformation_engine import (
    # Modular operad
    euler_characteristic_mbar,
    mbar_0n_betti,
    mbar_homology_rank,
    modular_operad_component,
    gluing_composition_rank,
    self_sewing_rank,
    list_stable_pairs,
    # FCom
    stable_graph_count,
    fcom_component_dim,
    enumerate_fcom_graphs,
    verify_bar_fcom_algebra,
    FComGraph,
    # Deformation complex
    deformation_complex_dimension,
    mc_equation_at_arity,
    # Standard families
    heisenberg_family_data,
    affine_km_family_data,
    virasoro_family_data,
    beta_gamma_family_data,
    w_algebra_family_data,
    all_family_data,
    StandardFamilyData,
    # Rankin-Selberg
    tensor_product_kappa,
    direct_sum_shadows,
    verify_l_function_multiplicativity,
    rank_n_heisenberg_from_tensor,
    # Newton
    newton_identities_from_shadow,
    virasoro_newton_check,
    # Deformation quantization
    first_order_deformation,
    obstruction_to_second_order,
    # Koszul dual
    koszul_dual_kappa,
    # Shadow depth
    classify_shadow_depth,
    shadow_metric,
    # Full engine
    operadic_deformation_analysis,
)


# ============================================================================
# T1-T7: Modular operad M = {C_*(M_bar_{g,n})}
# ============================================================================

class TestModularOperad:
    def test_euler_char_mbar_03(self):
        """T1: chi(M_bar_{0,3}) = 1 (point)."""
        assert euler_characteristic_mbar(0, 3) == 1

    def test_euler_char_mbar_04(self):
        """T2: chi(M_bar_{0,4}) = 2 (P^1)."""
        assert euler_characteristic_mbar(0, 4) == 2

    def test_euler_char_mbar_05(self):
        """T3: chi(M_bar_{0,5}) = 7 (del Pezzo surface)."""
        assert euler_characteristic_mbar(0, 5) == 7

    def test_betti_mbar_04(self):
        """T4: M_bar_{0,4} = P^1: b_0 = b_2 = 1, all others 0."""
        betti = mbar_0n_betti(4)
        assert betti == {0: 1, 2: 1}

    def test_betti_mbar_05(self):
        """T5: M_bar_{0,5}: b_0 = 1, b_2 = 5, b_4 = 1.

        NOTE: b_2 = 5, NOT 10. The 10 boundary divisors do not all
        give independent homology classes (AP3: verify, don't pattern-match).
        """
        betti = mbar_0n_betti(5)
        assert betti == {0: 1, 2: 5, 4: 1}
        assert sum(betti.values()) == 7  # matches Euler characteristic

    def test_stability_condition(self):
        """T6: Unstable pairs (g, n) with 2g - 2 + n <= 0 raise ValueError."""
        with pytest.raises(ValueError):
            euler_characteristic_mbar(0, 2)  # 0 - 2 + 2 = 0
        with pytest.raises(ValueError):
            euler_characteristic_mbar(0, 1)  # 0 - 2 + 1 = -1

    def test_stable_pairs_small(self):
        """T7: Enumerate stable pairs with g <= 2, n <= 4."""
        pairs = list_stable_pairs(2, 4)
        # (0,3), (0,4) at genus 0; (1,1), (1,2), (1,3), (1,4) at genus 1;
        # (2,0), (2,1), (2,2), (2,3), (2,4) at genus 2
        assert (0, 3) in pairs
        assert (0, 4) in pairs
        assert (1, 1) in pairs
        assert (2, 0) in pairs
        assert (0, 2) not in pairs  # unstable


# ============================================================================
# T8-T13: Feynman transform FCom
# ============================================================================

class TestFCom:
    def test_stable_graph_count_03(self):
        """T8: FCom(0,3) has 1 stable graph (single vertex)."""
        assert stable_graph_count(0, 3) == 1

    def test_stable_graph_count_04(self):
        """T9: FCom(0,4) has 4 stable graphs (1 + 3 binary trees)."""
        assert stable_graph_count(0, 4) == 4

    def test_stable_graph_count_11(self):
        """T10: FCom(1,1) has 2 stable graphs (genus-1 vertex + self-loop)."""
        assert stable_graph_count(1, 1) == 2

    def test_enumerate_graphs_04(self):
        """T11: Enumerate FCom(0,4) graphs: verify genera and arities."""
        graphs = enumerate_fcom_graphs(0, 4)
        assert len(graphs) == 4
        for gr in graphs:
            assert gr.total_genus == 0, f"{gr.name}: genus {gr.total_genus} != 0"
            assert gr.total_arity == 4, f"{gr.name}: arity {gr.total_arity} != 4"
            assert gr.is_stable, f"{gr.name} not stable"

    def test_enumerate_graphs_11(self):
        """T12: Enumerate FCom(1,1) graphs: verify genera and arities."""
        graphs = enumerate_fcom_graphs(1, 1)
        assert len(graphs) == 2
        for gr in graphs:
            assert gr.total_genus == 1
            assert gr.total_arity == 1

    def test_bar_fcom_verification_03(self):
        """T13: Verify B(A) is FCom-algebra at (0,3)."""
        result = verify_bar_fcom_algebra(0, 3)
        assert result['all_pass']
        assert result['num_graphs'] == 1


# ============================================================================
# T14-T18: Deformation complex Def(A)
# ============================================================================

class TestDeformationComplex:
    def test_def_dim_03_sl2(self):
        """T14: Def^(0,3)(sl2) = Hom(FCom(0,3), End_{sl2}(3))."""
        data = deformation_complex_dimension(0, 3, algebra_dim=3)
        assert data.fcom_dim == 1
        assert data.endomorphism_dim == 27  # 3^3
        assert data.deformation_dim == 27

    def test_def_dim_04_heisenberg(self):
        """T15: Def^(0,4)(H) = Hom(FCom(0,4), End_H(4))."""
        data = deformation_complex_dimension(0, 4, algebra_dim=1)
        assert data.fcom_dim == 4
        assert data.endomorphism_dim == 1  # 1^4
        assert data.deformation_dim == 4

    def test_mc_arity_2(self):
        """T16: MC at arity 2: d(kappa) = 0 (kappa is cocycle)."""
        result = mc_equation_at_arity(2, kappa=2.5)
        assert result['cocycle']
        assert result['shadow_value'] == 2.5

    def test_mc_arity_3_heisenberg(self):
        """T17: MC at arity 3 for Heisenberg: cubic shadow = 0 (gauge trivial)."""
        result = mc_equation_at_arity(3, kappa=1.0, alpha=0.0)
        assert result['gauge_triviality']

    def test_mc_arity_4_virasoro(self):
        """T18: MC at arity 4 for Virasoro: discriminant nonzero."""
        c_val = 25.0
        kappa = c_val / 2
        alpha = -3.0 / c_val
        S4 = 10.0 / (c_val * (5 * c_val + 22))
        result = mc_equation_at_arity(4, kappa, alpha, S4)
        assert not result['discriminant_zero_iff_terminates']
        assert abs(result['critical_discriminant']) > 1e-10


# ============================================================================
# T19-T24: Operadic Rankin-Selberg
# ============================================================================

class TestOperadicRankinSelberg:
    def test_kappa_additivity_heisenberg(self):
        """T19: kappa(H_k + H_k) = 2*kappa(H_k) (additivity)."""
        data_A = heisenberg_family_data(k=S(3))
        data_B = heisenberg_family_data(k=S(3))
        result = direct_sum_shadows(data_A, data_B)
        assert simplify(result['kappa'] - 6) == 0

    def test_kappa_additivity_mixed(self):
        """T20: kappa(H_k + sl2) = k + 3(k+2)/4 (additivity)."""
        k = Symbol('k')
        data_H = heisenberg_family_data(k)
        data_sl2 = affine_km_family_data('sl2', k)
        result = direct_sum_shadows(data_H, data_sl2)
        expected = k + Rational(3, 4) * (k + 2)
        assert simplify(result['kappa'] - expected) == 0

    def test_depth_class_max(self):
        """T21: Depth class of (G + L) = L (max of the two)."""
        data_H = heisenberg_family_data()
        data_sl2 = affine_km_family_data('sl2')
        result = direct_sum_shadows(data_H, data_sl2)
        assert result['depth_class'] == 'L'

    def test_rank_2_heisenberg(self):
        """T22: H_k tensor H_k = rank-2 Heisenberg: kappa = 2k."""
        result = rank_n_heisenberg_from_tensor(2, k=5.0)
        assert result['match']
        assert abs(result['kappa_sum'] - 10.0) < 1e-14
        assert result['depth_class'] == 'G'

    def test_rank_8_heisenberg(self):
        """T23: Rank-8 Heisenberg: kappa = 8k, still class G."""
        result = rank_n_heisenberg_from_tensor(8, k=1.0)
        assert result['match']
        assert abs(result['kappa_sum'] - 8.0) < 1e-14

    def test_l_function_multiplicativity(self):
        """T24: L-function multiplicativity for Heisenberg + Heisenberg."""
        result = verify_l_function_multiplicativity('Heisenberg', 'Heisenberg',
                                                     k_val=1.0)
        assert result['kappa_additivity']


# ============================================================================
# T25-T31: Newton's identities from MC
# ============================================================================

class TestNewtonIdentities:
    def test_virasoro_newton_c25(self):
        """T25: Virasoro c=25: Newton's identities through r=6."""
        result = virasoro_newton_check(25.0, r_max=6)
        assert result['all_pass']
        assert abs(result['lambda_effective'] - (-6.0 / 25.0)) < 1e-14

    def test_virasoro_newton_c1(self):
        """T26: Virasoro c=1: Newton's identities (lambda = -6)."""
        result = virasoro_newton_check(1.0, r_max=6)
        assert result['all_pass']
        assert abs(result['lambda_effective'] - (-6.0)) < 1e-14

    def test_virasoro_newton_c_half(self):
        """T27: Virasoro c=1/2 (Ising): Newton's identities."""
        result = virasoro_newton_check(0.5, r_max=6)
        assert result['all_pass']

    def test_single_atom_ratio(self):
        """T28: Single-atom check: all mu_{r+1}/mu_r = lambda."""
        c_val = 10.0
        P = 2.0 / c_val
        lam = -6.0 / c_val
        coeffs = {}
        for r in range(2, 9):
            coeffs[r] = (2.0 / r) * (-3.0) ** (r - 4) * P ** (r - 2)
        moments = {r: -r * S for r, S in coeffs.items()}
        for r in range(3, 8):
            ratio = moments[r] / moments[r - 1]
            assert abs(ratio - lam) < 1e-12, f"Ratio at r={r}: {ratio} != {lam}"

    def test_newton_from_shadow_coeffs(self):
        """T29: Newton identities from shadow coefficients (generic)."""
        c_val = 30.0
        P = 2.0 / c_val
        shadow = {}
        for r in range(2, 8):
            shadow[r] = (2.0 / r) * (-3.0) ** (r - 4) * P ** (r - 2)
        result = newton_identities_from_shadow(shadow, 7)
        for r, check in result.items():
            assert check['passes'], f"Newton at r={r}: defect={check['defect']}"

    def test_virasoro_newton_c13_selfdual(self):
        """T30: Virasoro c=13 (self-dual point): Newton check."""
        result = virasoro_newton_check(13.0, r_max=8)
        assert result['all_pass']
        # At c=13: lambda = -6/13 ~ -0.4615
        assert abs(result['lambda_effective'] - (-6.0 / 13.0)) < 1e-14

    def test_virasoro_newton_large_c(self):
        """T31: Virasoro large c (classical limit): Newton check."""
        result = virasoro_newton_check(1000.0, r_max=10)
        assert result['all_pass']
        # At large c: lambda = -6/c -> 0, tower suppressed
        assert abs(result['lambda_effective']) < 0.01


# ============================================================================
# T32-T37: Operadic deformation quantization
# ============================================================================

class TestDeformationQuantization:
    def test_heisenberg_deformation(self):
        """T32: Heisenberg first-order deformation: kappa = k."""
        deformation = first_order_deformation('Heisenberg')
        assert deformation.family_name == 'Heisenberg'
        assert deformation.obstruction_kappa == Symbol('k')

    def test_sl2_deformation(self):
        """T33: Affine sl_2 first-order deformation: kappa = 3(k+2)/4."""
        deformation = first_order_deformation('sl2')
        k = Symbol('k')
        expected = Rational(3, 4) * (k + 2)
        assert simplify(deformation.obstruction_kappa - expected) == 0

    def test_virasoro_deformation(self):
        """T34: Virasoro first-order deformation: kappa = c/2."""
        deformation = first_order_deformation('Virasoro')
        c = Symbol('c')
        assert simplify(deformation.obstruction_kappa - c / 2) == 0

    def test_obstruction_equals_kappa(self):
        """T35: Obstruction to 2nd order = kappa for all families."""
        for family in ['Heisenberg', 'sl2', 'Virasoro', 'beta-gamma']:
            obs = obstruction_to_second_order(family)
            assert obs['four_faces_of_kappa']
            assert 'bar_complex' in obs['interpretation']
            assert 'shadow_tower' in obs['interpretation']
            assert 'deformation' in obs['interpretation']
            assert 'anomaly' in obs['interpretation']

    def test_four_faces_of_kappa(self):
        """T36: The four faces: curvature, shadow, obstruction, anomaly."""
        obs = obstruction_to_second_order('Virasoro')
        interp = obs['interpretation']
        # All four faces must be present
        assert 'genus-1 curvature' in interp['bar_complex']
        assert 'arity-2 shadow' in interp['shadow_tower']
        assert 'HH^3' in interp['deformation']
        assert 'anomaly' in interp['anomaly']

    def test_obstruction_vanishes_critical(self):
        """T37: At critical level (kappa = 0), obstruction vanishes."""
        # For sl_2 at k = -h^v = -2: kappa = 3*(-2+2)/4 = 0
        obs = obstruction_to_second_order('sl2', k=-2)
        kappa_val = simplify(obs['kappa'].subs(Symbol('k'), -2))
        assert kappa_val == 0


# ============================================================================
# T38-T44: Shadow depth classification
# ============================================================================

class TestShadowDepth:
    def test_class_G_heisenberg(self):
        """T38: Heisenberg: kappa != 0, alpha = 0, S4 = 0 => class G, depth 2."""
        result = classify_shadow_depth(1.0, 0.0, 0.0)
        assert result['class'] == 'G'
        assert result['depth'] == 2

    def test_class_L_affine(self):
        """T39: Affine KM: kappa != 0, alpha != 0, Delta = 0 => class L, depth 3."""
        # S4 = 0 so Delta = 8*kappa*0 = 0; alpha != 0
        result = classify_shadow_depth(1.5, -0.5, 0.0)
        assert result['class'] == 'L'
        assert result['depth'] == 3

    def test_class_M_virasoro(self):
        """T40: Virasoro: Delta != 0 => class M or C, depth infinity (generically)."""
        c_val = 25.0
        kappa = c_val / 2
        S4 = 10.0 / (c_val * (5 * c_val + 22))
        alpha = -3.0 / c_val
        result = classify_shadow_depth(kappa, alpha, S4)
        assert 'M' in result['class']

    def test_shadow_metric_heisenberg(self):
        """T41: Shadow metric Q_L = 4*kappa^2 for Heisenberg (constant)."""
        kappa = 3.0
        Q_0 = shadow_metric(kappa, 0.0, 0.0, t=0.0)
        Q_1 = shadow_metric(kappa, 0.0, 0.0, t=1.0)
        Q_5 = shadow_metric(kappa, 0.0, 0.0, t=5.0)
        expected = 4 * kappa ** 2  # = 36
        assert abs(Q_0 - expected) < 1e-14
        assert abs(Q_1 - expected) < 1e-14
        assert abs(Q_5 - expected) < 1e-14

    def test_shadow_metric_positive(self):
        """T42: Shadow metric Q_L(t) >= 0 (sum of squares)."""
        for kappa, alpha, S4 in [(1.0, 0.0, 0.0), (2.5, -0.3, 0.01),
                                  (12.5, -0.12, 0.003)]:
            for t in [0.0, 0.5, 1.0, 2.0, -1.0]:
                Q = shadow_metric(kappa, alpha, S4, t)
                assert Q >= -1e-14, f"Q_L({t}) = {Q} < 0"

    def test_discriminant_zero_gaussian(self):
        """T43: Delta = 0 for Heisenberg and affine KM (S4 = 0)."""
        # Heisenberg: S4 = 0
        result = classify_shadow_depth(5.0, 0.0, 0.0)
        assert abs(result['Delta']) < 1e-14

    def test_discriminant_nonzero_virasoro(self):
        """T44: Delta != 0 for Virasoro (generic c)."""
        c_val = 25.0
        kappa = c_val / 2
        S4 = 10.0 / (c_val * (5 * c_val + 22))
        Delta = 8 * kappa * S4
        assert abs(Delta) > 1e-10


# ============================================================================
# T45-T50: Full engine integration
# ============================================================================

class TestFullEngine:
    def test_heisenberg_full_analysis(self):
        """T45: Full operadic analysis for Heisenberg."""
        result = operadic_deformation_analysis('Heisenberg', k=1)
        assert result['family'] == 'Heisenberg'
        assert result['shadow_data']['depth_class'] == 'G'
        assert result['shadow_data']['shadow_depth'] == 2

    def test_virasoro_full_analysis(self):
        """T46: Full operadic analysis for Virasoro."""
        result = operadic_deformation_analysis('Virasoro', c=25)
        assert result['family'] == 'Virasoro'
        assert result['shadow_data']['depth_class'] == 'M'
        assert result['shadow_data']['shadow_depth'] == oo

    def test_sl2_full_analysis(self):
        """T47: Full operadic analysis for affine sl_2."""
        result = operadic_deformation_analysis('sl2', k=1)
        assert result['family'] == 'sl2'
        assert result['shadow_data']['depth_class'] == 'L'

    def test_fcom_in_full_analysis(self):
        """T48: FCom verification included in full analysis."""
        result = operadic_deformation_analysis('Heisenberg', k=1)
        fcom = result['fcom_verification']
        assert (0, 3) in fcom
        assert fcom[(0, 3)]['all_pass']

    def test_koszul_dual_virasoro_sum(self):
        """T49: Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        result = koszul_dual_kappa('Virasoro')
        c = Symbol('c')
        sum_val = simplify(result['sum'])
        assert sum_val == 13

    def test_koszul_dual_heisenberg_antisymmetry(self):
        """T50: Heisenberg: kappa + kappa^! = 0 (anti-symmetry)."""
        result = koszul_dual_kappa('Heisenberg')
        assert simplify(result['sum']) == 0


# ============================================================================
# Additional structural tests
# ============================================================================

class TestStructuralProperties:
    def test_gluing_composition_genus_0(self):
        """Gluing (0,3) and (0,3) gives (0,4)."""
        result = gluing_composition_rank(0, 3, 0, 3)
        assert result['target'] == (0, 4)

    def test_self_sewing_genus_increase(self):
        """Self-sewing (0,4) gives (1,2)."""
        result = self_sewing_rank(0, 4)
        assert result['target'] == (1, 2)

    def test_w3_kappa_formula(self):
        """W_3 kappa = c*(H_3 - 1) = c*(1 + 1/2 + 1/3 - 1) = c*5/6."""
        c = Symbol('c')
        data = w_algebra_family_data(3, c)
        expected = c * Rational(5, 6)
        assert simplify(data.kappa - expected) == 0

    def test_w2_equals_virasoro_kappa(self):
        """W_2 = Virasoro: kappa = c/2."""
        c = Symbol('c')
        data = w_algebra_family_data(2, c)
        expected = c / 2
        # W_2 kappa = c*(H_2 - 1) = c*(1 + 1/2 - 1) = c/2
        assert simplify(data.kappa - expected) == 0

    def test_all_families_populated(self):
        """All standard families return valid data."""
        families = all_family_data()
        assert len(families) >= 5
        for name, data in families.items():
            assert data.kappa is not None
            assert data.depth_class in ('G', 'L', 'C', 'M')

    def test_modular_operad_component_genus0(self):
        """ModularOperadComponent stores correct data for (0, 4)."""
        comp = modular_operad_component(0, 4)
        assert comp.g == 0
        assert comp.n == 4
        assert comp.homology_rank == 2  # b_0 + b_2 = 1 + 1
        assert comp.dim == 1  # dim_C(M_bar_{0,4}) = 1

    def test_beta_gamma_depth_4(self):
        """Beta-gamma: depth = 4 (contact class)."""
        data = beta_gamma_family_data()
        assert data.depth_class == 'C'
        assert data.shadow_depth == 4

    def test_kappa_never_copied_between_families(self):
        """Cross-check: each family has DISTINCT kappa formula (AP1 prevention)."""
        c = Symbol('c')
        k = Symbol('k')
        families = all_family_data(k=k, c=c)
        kappas = {name: simplify(data.kappa) for name, data in families.items()}
        # Heisenberg kappa = k, Virasoro kappa = c/2 -- these are different
        assert kappas['Heisenberg'] != kappas['Virasoro']
        # sl2 kappa = 3(k+2)/4, sl3 kappa = 4(k+3)/3 -- different
        assert kappas['sl2'] != kappas['sl3']

    def test_self_sewing_genus0_arity3_unstable_target(self):
        """Self-sewing (0, 3) would give (1, 1) -- needs n >= 2."""
        # (0, 3) with n = 3 >= 2, target (1, 1) is stable
        result = self_sewing_rank(0, 3)
        assert result['target'] == (1, 1)
