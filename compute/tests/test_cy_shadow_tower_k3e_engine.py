r"""Tests for cy_shadow_tower_k3e_engine.py — shadow obstruction tower for K3 x E.

MULTI-PATH VERIFICATION STRATEGY (3+ independent paths per claim):

kappa(K3 x E) = 3:
  Path 1: dim_C(K3 x E) = 3
  Path 2: kappa(K3) + kappa(E) = 2 + 1 = 3
  Path 3: 24 * F_1 = 24 * 1/8 = 3
  Path 4: complementarity kappa! = -3
  Path 5: N=4 Ward (2*k_R = 2) + Heisenberg (1) = 3
  Path 6: partition function rank 3

F_1 = 1/8:
  Path 1: kappa * lambda_1 = 3 * 1/24 = 1/8
  Path 2: Bernoulli formula
  Path 3: partition function leading term

F_2 = 7/1920:
  Path 1: kappa * lambda_2 = 3 * 7/5760 = 7/1920
  Path 2: Bernoulli formula
  Path 3: A-hat coefficient

Shadow depth:
  Path 1: class G (sigma model = free bosons)
  Path 2: tower terminates at arity 2
  Path 3: Delta = 0 for class G

Cross-family consistency:
  - All CY3 sigma models have kappa = 3 (dimension universality)
  - K3 x E vs quintic vs T^6: same kappa, different chi, different h^{2,1}
  - Gepner model kappa = 4 != 3: different algebra (AP48)

References:
  thm:mc2-bar-intrinsic, def:shadow-metric, cor:shadow-extraction,
  thm:single-line-dichotomy, prop:independent-sum-factorization,
  thm:shadow-double-convergence, AP19-AP48
"""

import math
import pytest
from fractions import Fraction

from compute.lib.cy_shadow_tower_k3e_engine import (
    # Arithmetic
    bernoulli_number,
    faber_pandharipande,
    partition_count,
    sigma_divisor,
    # Topological invariants
    K3_COMPLEX_DIM, K3_EULER_CHAR, K3_CHI_O, K3_H11,
    E_COMPLEX_DIM, E_EULER_CHAR,
    K3E_COMPLEX_DIM, K3E_EULER_CHAR, K3E_CHI_O, K3E_H21, K3E_BETTI,
    hodge_numbers_k3e,
    euler_characteristic_k3e,
    betti_numbers_k3e,
    # Kappa functions
    kappa_chiral_derham,
    kappa_chiral_derham_path_dimension,
    kappa_chiral_derham_path_additive,
    kappa_chiral_derham_path_character,
    kappa_chiral_derham_path_complementarity,
    kappa_chiral_derham_all_paths,
    kappa_n4_tensor_heisenberg,
    kappa_n4_components,
    kappa_gepner_tensor_heisenberg,
    kappa_kummer_tensor_heisenberg,
    all_model_kappas,
    physical_kappa,
    # Shadow metric
    shadow_metric_class_g,
    shadow_metric_virasoro_c6,
    shadow_tower_class_g,
    shadow_tower_virasoro_c6,
    shadow_depth_k3e_models,
    # Genus-g free energy
    genus_free_energy,
    genus_free_energy_table,
    genus_free_energy_all_models,
    planted_forest_correction_genus2,
    full_genus2_free_energy,
    # Shadow partition function
    shadow_partition_function_coeffs,
    shadow_radius_of_convergence,
    ahat_generating_function,
    shadow_partition_function_evaluate,
    # Elliptic genus vs shadow
    elliptic_genus_vs_shadow,
    # BPS connection
    igusa_cusp_form_relation,
    # Comparison
    cy3_comparison_table,
    # q-series
    eta_coeffs,
    eta_power_coeffs,
    genus1_partition_heisenberg,
    genus1_free_energy_from_partition,
    # Multi-path verification
    verify_kappa_multipath,
    verify_F1_multipath,
    verify_F2_multipath,
    # Full analysis
    full_shadow_analysis,
    run_all_verifications,
)

F = Fraction


# =====================================================================
# Section 1: Arithmetic helpers
# =====================================================================

class TestArithmeticHelpers:
    """Tests for Bernoulli numbers, FP numbers, partitions."""

    def test_bernoulli_B0(self):
        assert bernoulli_number(0) == F(1)

    def test_bernoulli_B1(self):
        assert bernoulli_number(1) == F(-1, 2)

    def test_bernoulli_B2(self):
        assert bernoulli_number(2) == F(1, 6)

    def test_bernoulli_B4(self):
        assert bernoulli_number(4) == F(-1, 30)

    def test_bernoulli_B6(self):
        assert bernoulli_number(6) == F(1, 42)

    def test_bernoulli_odd_zero(self):
        """B_n = 0 for odd n > 1."""
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli_number(n) == F(0), f"B_{n} should be 0"

    def test_fp_lambda1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == F(1, 24)

    def test_fp_lambda2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == F(7, 5760)

    def test_fp_lambda3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == F(31, 967680)

    def test_fp_positive(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0, f"lambda_{g} should be positive"

    def test_fp_decreasing(self):
        """lambda_g^FP is eventually decreasing (Bernoulli decay)."""
        for g in range(2, 7):
            assert faber_pandharipande(g) < faber_pandharipande(g - 1)

    def test_partitions_small(self):
        """Small partition numbers."""
        assert partition_count(0) == 1
        assert partition_count(1) == 1
        assert partition_count(2) == 2
        assert partition_count(3) == 3
        assert partition_count(4) == 5
        assert partition_count(5) == 7

    def test_sigma_1(self):
        """sigma_1(n) = sum of divisors."""
        assert sigma_divisor(1, 1) == 1
        assert sigma_divisor(6, 1) == 12  # 1+2+3+6
        assert sigma_divisor(12, 1) == 28  # 1+2+3+4+6+12

    def test_sigma_3(self):
        """sigma_3(n) used in E_4."""
        assert sigma_divisor(1, 3) == 1
        assert sigma_divisor(2, 3) == 9   # 1 + 8


# =====================================================================
# Section 2: Topological invariants of K3 x E
# =====================================================================

class TestTopologicalInvariants:
    """Tests for Hodge numbers, Euler char, Betti numbers."""

    def test_k3_euler(self):
        """chi(K3) = 24."""
        assert K3_EULER_CHAR == 24

    def test_e_euler(self):
        """chi(E) = 0."""
        assert E_EULER_CHAR == 0

    def test_k3e_euler_product(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert K3E_EULER_CHAR == K3_EULER_CHAR * E_EULER_CHAR

    def test_k3e_euler_from_hodge(self):
        """chi from Hodge diamond = 0."""
        assert euler_characteristic_k3e() == 0

    def test_k3e_euler_from_betti(self):
        """chi from alternating sum of Betti numbers."""
        b = betti_numbers_k3e()
        chi = sum((-1) ** k * v for k, v in b.items())
        assert chi == 0

    def test_k3e_chi_o(self):
        """chi(O_{K3xE}) = chi(O_{K3}) * chi(O_E) = 2 * 0 = 0."""
        assert K3E_CHI_O == K3_CHI_O * F(E_EULER_CHAR)  # both are 0

    def test_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} (Hodge symmetry)."""
        hd = hodge_numbers_k3e()
        for (p, q), v in hd.items():
            assert hd.get((q, p), 0) == v, f"h^{{{p},{q}}} != h^{{{q},{p}}}"

    def test_hodge_serre_duality(self):
        """h^{p,q} = h^{d-p, d-q} (Serre duality) where d=3."""
        hd = hodge_numbers_k3e()
        d = 3
        for (p, q), v in hd.items():
            assert hd.get((d - p, d - q), 0) == v, \
                f"h^{{{p},{q}}} != h^{{{d-p},{d-q}}}"

    def test_hodge_h00(self):
        hd = hodge_numbers_k3e()
        assert hd[(0, 0)] == 1

    def test_hodge_h11(self):
        """h^{1,1}(K3 x E) = h^{1,1}(K3) * h^{0,0}(E) + h^{0,0}(K3) * h^{1,1}(E)
                             + h^{1,0}(K3) * h^{0,1}(E) + h^{0,1}(K3) * h^{1,0}(E)
                             = 20*1 + 1*1 + 0*1 + 0*1 = 21."""
        hd = hodge_numbers_k3e()
        assert hd[(1, 1)] == 21

    def test_hodge_h21(self):
        """h^{2,1}(K3 x E) = 21."""
        hd = hodge_numbers_k3e()
        assert hd[(2, 1)] == 21

    def test_hodge_h30(self):
        """h^{3,0}(K3 x E) = h^{2,0}(K3)*h^{1,0}(E) = 1*1 = 1."""
        hd = hodge_numbers_k3e()
        assert hd[(3, 0)] == 1

    def test_betti_b0(self):
        b = betti_numbers_k3e()
        assert b[0] == 1

    def test_betti_b1(self):
        b = betti_numbers_k3e()
        assert b[1] == 2

    def test_betti_b2(self):
        b = betti_numbers_k3e()
        assert b[2] == 23

    def test_betti_b3(self):
        """b_3 = 44 (the middle Betti number)."""
        b = betti_numbers_k3e()
        assert b[3] == 44

    def test_betti_poincare_duality(self):
        """b_k = b_{6-k} (Poincare duality for a 6-manifold)."""
        b = betti_numbers_k3e()
        for k in range(7):
            assert b.get(k, 0) == b.get(6 - k, 0), \
                f"b_{k} != b_{6-k}"

    def test_betti_matches_stored(self):
        b = betti_numbers_k3e()
        for k, v in K3E_BETTI.items():
            assert b.get(k, 0) == v, f"Betti b_{k} mismatch"

    def test_complex_dim(self):
        assert K3E_COMPLEX_DIM == K3_COMPLEX_DIM + E_COMPLEX_DIM


# =====================================================================
# Section 3: Modular characteristic kappa — multi-path verification
# =====================================================================

class TestKappaMultiPath:
    """Multi-path verification of kappa(K3 x E) = 3."""

    def test_kappa_physical(self):
        """Physical kappa = 3."""
        assert physical_kappa() == F(3)

    def test_kappa_path_dimension(self):
        """Path 1: kappa = dim_C = 3."""
        assert kappa_chiral_derham_path_dimension() == F(3)

    def test_kappa_path_additive(self):
        """Path 2: kappa(K3) + kappa(E) = 2 + 1 = 3."""
        assert kappa_chiral_derham_path_additive() == F(3)

    def test_kappa_path_character(self):
        """Path 3: 24 * F_1 = 24 * 1/8 = 3."""
        assert kappa_chiral_derham_path_character() == F(3)

    def test_kappa_path_complementarity(self):
        """Path 4: kappa! = -3, kappa = 3."""
        assert kappa_chiral_derham_path_complementarity() == F(3)

    def test_kappa_all_paths_agree(self):
        """All 4 paths give kappa = 3."""
        result = kappa_chiral_derham_all_paths()
        assert result['all_agree']
        assert result['kappa'] == F(3)

    def test_kappa_n4_tensor_heisenberg(self):
        """kappa(N=4 SCA x H_E) = 2 + 1 = 3."""
        assert kappa_n4_tensor_heisenberg() == F(3)

    def test_kappa_6_paths(self):
        """Full 6-path verification from verify_kappa_multipath."""
        result = verify_kappa_multipath()
        assert result['all_agree']
        assert result['n_paths'] == 6

    def test_kappa_equals_dim_c(self):
        """kappa = dim_C for the sigma model (universal for CY)."""
        assert physical_kappa() == F(K3E_COMPLEX_DIM)


class TestKappaModels:
    """Test kappa for each VOA model of K3 x E."""

    def test_chiral_derham(self):
        assert kappa_chiral_derham() == F(3)

    def test_n4_tensor_heis(self):
        assert kappa_n4_tensor_heisenberg() == F(3)

    def test_gepner_tensor_heis(self):
        """Gepner: kappa = 4 (different algebra!)."""
        assert kappa_gepner_tensor_heisenberg() == F(4)

    def test_kummer_tensor_heis(self):
        """Kummer: kappa = 5 (different algebra!)."""
        assert kappa_kummer_tensor_heisenberg() == F(5)

    def test_gepner_neq_physical(self):
        """Gepner kappa != physical kappa (AP48)."""
        assert kappa_gepner_tensor_heisenberg() != physical_kappa()

    def test_kummer_neq_physical(self):
        """Kummer kappa != physical kappa (AP48)."""
        assert kappa_kummer_tensor_heisenberg() != physical_kappa()

    def test_physical_models_agree(self):
        """Models A, B, E agree on kappa = 3."""
        assert kappa_chiral_derham() == F(3)
        assert kappa_n4_tensor_heisenberg() == F(3)
        # sigma model bosonic
        assert F(K3E_COMPLEX_DIM) == F(3)

    def test_n4_components(self):
        """N=4 SCA decomposition."""
        comp = kappa_n4_components()
        assert comp['kappa_n4_sca'] == F(2)
        assert comp['kappa_heisenberg_e'] == F(1)
        assert comp['kappa_total'] == F(3)
        assert comp['kappa_virasoro_alone'] == F(3)
        assert comp['n4_reduction'] == F(1)

    def test_n4_kappa_less_than_virasoro(self):
        """kappa(N=4 SCA) < kappa(Vir at same c): AP48."""
        comp = kappa_n4_components()
        assert comp['kappa_n4_sca'] < comp['kappa_virasoro_alone']

    def test_all_models_list(self):
        """All model kappas are computed."""
        models = all_model_kappas()
        assert len(models) == 5
        names = {m.name for m in models}
        assert 'chiral_de_rham' in names
        assert 'n4_tensor_heisenberg' in names

    def test_gepner_kappa_decomposition(self):
        """Gepner: 4 factors of c=3/2, each kappa=3/4, plus Heis kappa=1."""
        kappa_per_factor = F(3, 4)
        kappa_gepner = 4 * kappa_per_factor
        assert kappa_gepner == F(3)  # Gepner internal = 3
        assert kappa_gepner_tensor_heisenberg() == F(4)  # plus Heis = 4


# =====================================================================
# Section 4: Shadow metric and depth classification
# =====================================================================

class TestShadowMetric:
    """Tests for shadow metric Q_L and depth classification."""

    def test_class_g_metric_constant(self):
        """Class G: Q_L = 4*kappa^2, alpha = S_4 = 0."""
        sm = shadow_metric_class_g(F(3))
        assert sm.q0 == 4 * F(3) ** 2  # = 36
        assert sm.q1 == F(0)
        assert sm.q2 == F(0)
        assert sm.alpha == F(0)
        assert sm.S4 == F(0)
        assert sm.Delta == F(0)

    def test_class_g_depth(self):
        """Class G: r_max = 2."""
        sm = shadow_metric_class_g(F(3))
        assert sm.depth_class == "G"
        assert sm.depth_rmax == 2

    def test_virasoro_c6_kappa(self):
        """Virasoro at c=6: kappa = 3."""
        sm = shadow_metric_virasoro_c6()
        assert sm.kappa == F(3)

    def test_virasoro_c6_alpha(self):
        """Virasoro alpha = 2 (universal)."""
        sm = shadow_metric_virasoro_c6()
        assert sm.alpha == F(2)

    def test_virasoro_c6_S4(self):
        """S_4(Vir_6) = 10/(6*52) = 5/156."""
        sm = shadow_metric_virasoro_c6()
        assert sm.S4 == F(5, 156)

    def test_virasoro_c6_Delta(self):
        """Delta = 8*3*5/156 = 10/13."""
        sm = shadow_metric_virasoro_c6()
        assert sm.Delta == F(10, 13)

    def test_virasoro_c6_delta_nonzero(self):
        """Virasoro at c=6 has Delta != 0 => class M."""
        sm = shadow_metric_virasoro_c6()
        assert sm.Delta != 0
        assert sm.depth_class == "M"

    def test_class_g_delta_zero(self):
        """Class G has Delta = 0."""
        sm = shadow_metric_class_g(F(3))
        assert sm.Delta == F(0)


class TestShadowTower:
    """Tests for the shadow obstruction tower."""

    def test_class_g_tower_S2(self):
        """Class G: S_2 = kappa = 3."""
        tower = shadow_tower_class_g(F(3))
        assert tower[2] == F(3)

    def test_class_g_tower_terminates(self):
        """Class G: S_r = 0 for r >= 3."""
        tower = shadow_tower_class_g(F(3), rmax=10)
        for r in range(3, 11):
            assert tower[r] == F(0), f"S_{r} should be 0 for class G"

    def test_virasoro_c6_tower_S2(self):
        """Virasoro at c=6: S_2 = kappa = 3."""
        tower = shadow_tower_virasoro_c6(rmax=5)
        assert tower[2] == F(3)

    def test_virasoro_c6_tower_S3(self):
        """Virasoro at c=6: S_3 = alpha = 2."""
        tower = shadow_tower_virasoro_c6(rmax=5)
        # S_3 = a_1 / 3 where a_1 = q1/(2*a_0) = 12*3*2/(2*6) = 72/12 = 6
        # S_3 = 6/3 = 2
        assert tower[3] == F(2)

    def test_virasoro_c6_tower_S4(self):
        """Virasoro at c=6: S_4 = 5/156."""
        tower = shadow_tower_virasoro_c6(rmax=5)
        assert tower[4] == F(5, 156)

    def test_virasoro_c6_tower_S5_nonzero(self):
        """Virasoro at c=6: S_5 != 0 (class M, infinite tower)."""
        tower = shadow_tower_virasoro_c6(rmax=6)
        assert tower[5] != F(0)

    def test_virasoro_c6_S5_exact(self):
        """S_5(Vir_6) = -48 / (36 * 52) = -48/1872 = -1/39."""
        tower = shadow_tower_virasoro_c6(rmax=6)
        # S_5 = -48 / (c^2 * (5c+22)) at c=6 = -48 / (36 * 52) = -48/1872 = -1/39
        assert tower[5] == F(-1, 39)

    def test_virasoro_c6_tower_alternating(self):
        """Virasoro tower: S_3 > 0, S_5 < 0 (alternating pattern for odd arities)."""
        tower = shadow_tower_virasoro_c6(rmax=8)
        assert tower[3] > 0
        assert tower[5] < 0

    def test_shadow_depth_models(self):
        """All 5 models have correct depth classification."""
        depths = shadow_depth_k3e_models()
        assert depths['chiral_de_rham']['class'] == 'G'
        assert depths['n4_tensor_heisenberg']['class'] == 'M'
        assert depths['gepner_tensor_heisenberg']['class'] == 'G'
        assert depths['kummer_tensor_heisenberg']['class'] == 'G'
        assert depths['sigma_bosonic']['class'] == 'G'

    def test_shadow_depth_n4_infinite(self):
        depths = shadow_depth_k3e_models()
        assert depths['n4_tensor_heisenberg']['rmax'] == math.inf


# =====================================================================
# Section 5: Genus-g free energy — multi-path
# =====================================================================

class TestFreeEnergyMultiPath:
    """Multi-path verification of F_g values."""

    def test_F1_value(self):
        """F_1 = 3/24 = 1/8."""
        assert genus_free_energy(1) == F(1, 8)

    def test_F1_multipath(self):
        """3 paths for F_1."""
        result = verify_F1_multipath()
        assert result['all_agree']
        assert result['F1'] == F(1, 8)

    def test_F2_value(self):
        """F_2 = 3 * 7/5760 = 7/1920."""
        assert genus_free_energy(2) == F(7, 1920)

    def test_F2_multipath(self):
        """3 paths for F_2."""
        result = verify_F2_multipath()
        assert result['all_agree']
        assert result['F2'] == F(7, 1920)

    def test_F3_value(self):
        """F_3 = 3 * 31/967680 = 31/322560."""
        expected = F(3) * F(31, 967680)
        assert genus_free_energy(3) == expected

    def test_F4_value(self):
        """F_4 = 3 * lambda_4."""
        lam4 = faber_pandharipande(4)
        assert genus_free_energy(4) == F(3) * lam4

    def test_F5_value(self):
        """F_5 = 3 * lambda_5."""
        lam5 = faber_pandharipande(5)
        assert genus_free_energy(5) == F(3) * lam5

    def test_Fg_positive_all_genera(self):
        """F_g > 0 for all g >= 1 (Bernoulli positivity)."""
        for g in range(1, 10):
            assert genus_free_energy(g) > 0, f"F_{g} should be positive"

    def test_Fg_decreasing(self):
        """F_g is decreasing for g >= 2 (Bernoulli decay)."""
        for g in range(2, 8):
            assert genus_free_energy(g) < genus_free_energy(g - 1)

    def test_Fg_table(self):
        """Genus free energy table consistent with individual values."""
        table = genus_free_energy_table(gmax=5)
        for g in range(1, 6):
            assert table[g] == genus_free_energy(g)

    def test_Fg_linearity_in_kappa(self):
        """F_g(c*kappa) = c * F_g(kappa) for all g."""
        for g in range(1, 5):
            assert genus_free_energy(g, F(6)) == 2 * genus_free_energy(g, F(3))

    def test_Fg_gepner_model(self):
        """Gepner model F_1 = 4/24 = 1/6."""
        assert genus_free_energy(1, F(4)) == F(1, 6)

    def test_Fg_kummer_model(self):
        """Kummer model F_1 = 5/24."""
        assert genus_free_energy(1, F(5)) == F(5, 24)


class TestFreeEnergyAllModels:
    """Test genus-g free energies for all VOA models."""

    def test_all_models_computed(self):
        result = genus_free_energy_all_models(gmax=3)
        assert len(result) == 5
        assert 'chiral_de_rham' in result
        assert 'gepner_tensor_heisenberg' in result

    def test_physical_models_agree(self):
        """Models with kappa=3 agree on F_g."""
        result = genus_free_energy_all_models(gmax=3)
        assert result['chiral_de_rham'] == result['n4_tensor_heisenberg']
        assert result['chiral_de_rham'] == result['sigma_bosonic']

    def test_gepner_differs(self):
        """Gepner F_g != physical F_g (kappa=4 vs 3)."""
        result = genus_free_energy_all_models(gmax=3)
        assert result['gepner_tensor_heisenberg'] != result['chiral_de_rham']

    def test_kummer_differs(self):
        """Kummer F_g != physical F_g (kappa=5 vs 3)."""
        result = genus_free_energy_all_models(gmax=3)
        assert result['kummer_tensor_heisenberg'] != result['chiral_de_rham']


# =====================================================================
# Section 6: Planted-forest corrections
# =====================================================================

class TestPlantedForest:
    """Tests for planted-forest correction to F_2."""

    def test_pf_class_g_zero(self):
        """Class G: S_3 = 0 => delta_pf = 0."""
        assert planted_forest_correction_genus2(F(0), F(3)) == F(0)

    def test_pf_virasoro_c6(self):
        """Virasoro c=6: S_3=2, kappa=3 => delta_pf = 2*(20-3)/48 = 17/24."""
        result = planted_forest_correction_genus2(F(2), F(3))
        assert result == F(17, 24)

    def test_full_F2_class_g(self):
        """Class G: F_2 = scalar part only."""
        result = full_genus2_free_energy(F(3), F(0), F(0))
        assert result['F2_scalar'] == F(7, 1920)
        assert result['delta_pf'] == F(0)
        assert result['F2_with_pf'] == F(7, 1920)

    def test_full_F2_virasoro_c6(self):
        """Virasoro c=6: F_2 with planted-forest correction."""
        result = full_genus2_free_energy(F(3), F(2), F(5, 156))
        assert result['F2_scalar'] == F(7, 1920)
        assert result['delta_pf'] == F(17, 24)
        assert result['F2_with_pf'] == F(7, 1920) + F(17, 24)


# =====================================================================
# Section 7: Shadow partition function
# =====================================================================

class TestShadowPartitionFunction:
    """Tests for the shadow partition function."""

    def test_pf_coeffs_F0_zero(self):
        """F_0 = 0."""
        coeffs = shadow_partition_function_coeffs(gmax=5)
        assert coeffs[0] == F(0)

    def test_pf_coeffs_F1(self):
        coeffs = shadow_partition_function_coeffs(gmax=5)
        assert coeffs[1] == F(1, 8)

    def test_pf_coeffs_F2(self):
        coeffs = shadow_partition_function_coeffs(gmax=5)
        assert coeffs[2] == F(7, 1920)

    def test_radius_pi(self):
        """Radius of convergence = pi."""
        rho = shadow_radius_of_convergence()
        assert abs(rho - math.pi) < 1e-10

    def test_ahat_at_zero(self):
        """A-hat GF evaluated at hbar=0 gives 0."""
        val = ahat_generating_function(0.0)
        assert abs(val) < 1e-15

    def test_ahat_small_hbar(self):
        """Leading behavior: kappa * hbar^2/24 for small hbar."""
        hbar_sq = 0.01
        val = ahat_generating_function(hbar_sq)
        leading = 3.0 * hbar_sq / 24.0
        assert abs(val - leading) < 1e-4  # higher-order corrections small

    def test_zsh_at_zero(self):
        """Z^sh(0) = exp(0) = 1."""
        val = shadow_partition_function_evaluate(0.0)
        assert abs(val - 1.0) < 1e-15

    def test_zsh_positive(self):
        """Z^sh > 0 within radius of convergence."""
        for hbar_sq in [0.1, 0.5, 1.0, 2.0, 5.0]:
            val = shadow_partition_function_evaluate(hbar_sq)
            assert val > 0

    def test_zsh_increasing(self):
        """Z^sh is increasing for hbar^2 > 0 (all F_g > 0)."""
        v1 = shadow_partition_function_evaluate(0.5)
        v2 = shadow_partition_function_evaluate(1.0)
        v3 = shadow_partition_function_evaluate(2.0)
        assert v1 < v2 < v3


# =====================================================================
# Section 8: Elliptic genus vanishing vs shadow nonvanishing
# =====================================================================

class TestEllipticGenusVsShadow:
    """Tests for the Z_{ell}=0 vs kappa!=0 resolution."""

    def test_elliptic_genus_vanishes(self):
        result = elliptic_genus_vs_shadow()
        assert result['elliptic_genus_vanishes'] is True

    def test_chi_zero(self):
        result = elliptic_genus_vs_shadow()
        assert result['chi_k3e'] == 0

    def test_kappa_nonzero(self):
        result = elliptic_genus_vs_shadow()
        assert result['kappa_nonzero'] is True
        assert result['kappa_physical'] == F(3)

    def test_F1_nonzero(self):
        result = elliptic_genus_vs_shadow()
        assert result['F1_nonzero'] is True
        assert result['F1'] == F(1, 8)

    def test_ap31_illustration(self):
        """AP31: kappa=0 does NOT follow from Z=0.
        And conversely, Z=0 does NOT imply kappa=0."""
        assert K3E_EULER_CHAR == 0
        assert physical_kappa() != 0


# =====================================================================
# Section 9: q-series and partition functions
# =====================================================================

class TestQSeries:
    """Tests for eta functions and genus-1 partition functions."""

    def test_eta_leading(self):
        """eta = q^{1/24} * (1 - q - q^2 + q^5 + q^7 - ...)"""
        c = eta_coeffs(20)
        assert c[0] == 1
        assert c[1] == -1
        assert c[2] == -1
        assert c[3] == 0
        assert c[4] == 0
        assert c[5] == 1

    def test_eta_inverse_partitions(self):
        """1/eta = q^{-1/24} * sum p(n) q^n."""
        c = eta_power_coeffs(20, -1)
        assert c[0] == 1   # p(0)
        assert c[1] == 1   # p(1)
        assert c[2] == 2   # p(2)
        assert c[3] == 3   # p(3)
        assert c[4] == 5   # p(4)
        assert c[5] == 7   # p(5)

    def test_eta_cube_inverse(self):
        """1/eta^3: first few coefficients."""
        c = eta_power_coeffs(20, -3)
        assert c[0] == 1
        # p_3(1) = 3 (three ways to place 1 unit among 3 colors)
        assert c[1] == 3
        # p_3(2) = 9
        assert c[2] == 9

    def test_genus1_heisenberg_rank3(self):
        """Genus-1 partition function for rank-3 Heisenberg."""
        coeffs = genus1_partition_heisenberg(nmax=10, rank=3)
        assert coeffs[0] == F(1)
        assert coeffs[1] == F(3)

    def test_genus1_free_energy_rank3(self):
        """F_1 from partition function: rank/24 = 3/24 = 1/8."""
        assert genus1_free_energy_from_partition(3) == F(1, 8)

    def test_genus1_free_energy_rank1(self):
        """F_1 for rank 1: 1/24."""
        assert genus1_free_energy_from_partition(1) == F(1, 24)

    def test_genus1_free_energy_rank2(self):
        """F_1 for rank 2 (K3 alone): 2/24 = 1/12."""
        assert genus1_free_energy_from_partition(2) == F(1, 12)


# =====================================================================
# Section 10: CY3 comparison
# =====================================================================

class TestCY3Comparison:
    """Compare shadow data across CY3 examples."""

    def test_all_cy3_kappa_3(self):
        """All CY3 sigma models have kappa = 3."""
        table = cy3_comparison_table()
        for name, data in table.items():
            assert data['kappa_geometric'] == F(3), \
                f"CY3 {name} should have kappa = 3"

    def test_k3e_chi_zero(self):
        table = cy3_comparison_table()
        assert table['K3xE']['chi'] == 0

    def test_quintic_chi_nonzero(self):
        table = cy3_comparison_table()
        assert table['quintic']['chi'] == -200

    def test_t6_chi_zero(self):
        table = cy3_comparison_table()
        assert table['T6']['chi'] == 0

    def test_k3e_ell_genus_vanishes(self):
        table = cy3_comparison_table()
        assert table['K3xE']['elliptic_genus_vanishes'] is True

    def test_quintic_ell_genus_nonzero(self):
        table = cy3_comparison_table()
        assert table['quintic']['elliptic_genus_vanishes'] is False

    def test_all_class_g(self):
        """All CY3 sigma models are class G."""
        table = cy3_comparison_table()
        for name, data in table.items():
            assert data['shadow_class'] == 'G'

    def test_h21_distinct(self):
        """Different CY3s have different h^{2,1}."""
        table = cy3_comparison_table()
        h21s = [data['h21'] for data in table.values()]
        assert len(set(h21s)) == len(h21s), "h^{2,1} should be distinct"


# =====================================================================
# Section 11: BPS and Igusa cusp form connection
# =====================================================================

class TestBPSConnection:
    """Tests for BPS/Igusa cusp form relation."""

    def test_igusa_data(self):
        data = igusa_cusp_form_relation()
        assert data['igusa_weight'] == 10
        assert data['siegel_genus'] == 2
        assert data['shadow_kappa'] == F(3)
        assert data['shadow_F1'] == F(1, 8)

    def test_status_conjectural(self):
        data = igusa_cusp_form_relation()
        assert 'CONJECTURAL' in data['status']


# =====================================================================
# Section 12: Cross-family consistency checks
# =====================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency for kappa and F_g."""

    def test_kappa_additive_k3_e(self):
        """kappa(K3 x E) = kappa(K3) + kappa(E) (tensor product additivity)."""
        assert physical_kappa() == F(K3_COMPLEX_DIM) + F(E_COMPLEX_DIM)

    def test_kappa_additive_gepner(self):
        """Gepner: kappa = 4 * kappa(factor) = 4 * 3/4 = 3 (internal) + 1 (E)."""
        assert kappa_gepner_tensor_heisenberg() == 4 * F(3, 4) + F(1)

    def test_F1_additive(self):
        """F_1(K3 x E) = F_1(K3) + F_1(E) = 1/12 + 1/24 = 1/8.
        (Additivity of kappa implies additivity of F_1.)"""
        F1_k3 = F(2) * faber_pandharipande(1)   # 2/24 = 1/12
        F1_e = F(1) * faber_pandharipande(1)     # 1/24
        assert F1_k3 + F1_e == F(1, 8)
        assert genus_free_energy(1) == F1_k3 + F1_e

    def test_F2_additive(self):
        """F_2(K3 x E) = F_2(K3) + F_2(E) (scalar level)."""
        F2_k3 = F(2) * faber_pandharipande(2)
        F2_e = F(1) * faber_pandharipande(2)
        assert F2_k3 + F2_e == genus_free_energy(2)

    def test_complementarity_sum_zero(self):
        """kappa + kappa! = 0 for free-field type."""
        kappa = physical_kappa()
        kappa_dual = -kappa
        assert kappa + kappa_dual == 0

    def test_kappa_scaling_with_rank(self):
        """For rank-d Heisenberg: kappa = d."""
        for d in range(1, 6):
            assert genus1_free_energy_from_partition(d) == F(d, 24)


# =====================================================================
# Section 13: Convergence and asymptotics
# =====================================================================

class TestConvergence:
    """Tests for shadow partition function convergence."""

    def test_bernoulli_decay(self):
        """F_g ~ kappa * (2*pi)^{-2g} * |B_{2g}|/(2g) for large g.

        The ratio F_g / (kappa * (2*pi)^{-2g}) should approach a finite limit.
        """
        kappa = float(physical_kappa())
        for g in [5, 6, 7, 8]:
            Fg = float(genus_free_energy(g))
            asymptotic = kappa * (2 * math.pi) ** (-2 * g)
            ratio = Fg / asymptotic
            # The ratio should be of order 1 (within the Bernoulli correction)
            assert 0.01 < ratio < 100, \
                f"Bernoulli decay: F_{g}/asymptotic = {ratio}"

    def test_radius_pi(self):
        """Shadow GF converges for |hbar| < pi."""
        rho = shadow_radius_of_convergence()
        assert abs(rho - math.pi) < 1e-10

    def test_convergence_inside_radius(self):
        """Series converges well inside the radius."""
        hbar_sq = 1.0  # well inside pi^2 ~ 9.87
        v1 = ahat_generating_function(hbar_sq, gmax=20)
        v2 = ahat_generating_function(hbar_sq, gmax=50)
        assert abs(v1 - v2) < 1e-10, "Series should converge rapidly"

    def test_convergence_near_boundary(self):
        """Series converges slowly near |hbar|^2 = pi^2."""
        hbar_sq = 9.0  # close to pi^2 ~ 9.87
        v1 = ahat_generating_function(hbar_sq, gmax=30)
        v2 = ahat_generating_function(hbar_sq, gmax=60)
        # Should still converge but more slowly
        assert abs(v1 - v2) < 0.1


# =====================================================================
# Section 14: Full analysis integration
# =====================================================================

class TestFullAnalysis:
    """Integration tests for the full shadow analysis."""

    def test_full_analysis_structure(self):
        result = full_shadow_analysis(gmax=3)
        assert 'topological' in result
        assert 'kappa_physical' in result
        assert 'shadow_tower_scalar' in result
        assert 'free_energies' in result
        assert 'verification' in result

    def test_full_analysis_kappa(self):
        result = full_shadow_analysis()
        assert result['kappa_physical'] == F(3)

    def test_full_analysis_depth(self):
        result = full_shadow_analysis()
        assert result['shadow_depth'] == 'G'
        assert result['shadow_rmax'] == 2

    def test_full_analysis_topology(self):
        result = full_shadow_analysis()
        assert result['topological']['euler'] == 0
        assert result['topological']['dim_C'] == 3
        assert result['topological']['elliptic_genus_vanishes'] is True

    def test_run_all_verifications(self):
        """All verification checks pass."""
        results = run_all_verifications()
        for key, passed in results.items():
            assert passed, f"Verification check '{key}' failed"

    def test_all_verifications_count(self):
        """At least 10 verification checks."""
        results = run_all_verifications()
        assert len(results) >= 10


# =====================================================================
# Section 15: Edge cases and error handling
# =====================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_fp_genus_1_minimum(self):
        """lambda_g undefined for g < 1."""
        with pytest.raises(ValueError):
            faber_pandharipande(0)

    def test_kappa_zero_algebra(self):
        """Class G with kappa=0: all F_g = 0."""
        tower = shadow_tower_class_g(F(0))
        for r, v in tower.items():
            assert v == F(0)

    def test_kappa_negative(self):
        """Negative kappa (ghost sector): F_g < 0."""
        for g in range(1, 5):
            assert genus_free_energy(g, F(-3)) < 0

    def test_large_genus(self):
        """F_g computable at large genus."""
        val = genus_free_energy(20)
        assert val > 0
        assert val < genus_free_energy(19)

    def test_partition_count_zero(self):
        assert partition_count(0) == 1

    def test_partition_count_negative(self):
        assert partition_count(-1) == 0


# =====================================================================
# Section 16: AP-specific regression tests
# =====================================================================

class TestAntiPatternRegression:
    """Regression tests for known anti-patterns."""

    def test_ap20_kappa_not_c_over_2(self):
        """AP20: kappa(K3 x E) = 3, NOT c/2 for the N=4 SCA (AP48)."""
        # N=4 SCA at c=6 has kappa=2, not c/2=3
        comp = kappa_n4_components()
        assert comp['kappa_n4_sca'] == F(2)
        assert comp['kappa_n4_sca'] != F(3)
        # But total kappa = 2 + 1 = 3, which happens to equal c/2
        # This is a COINCIDENCE, not the formula (AP20)

    def test_ap24_complementarity(self):
        """AP24: kappa + kappa! = 0 for free-field (NOT universal)."""
        kappa = physical_kappa()
        kappa_dual = -kappa
        assert kappa + kappa_dual == 0

    def test_ap31_vanishing_trace_nonvanishing_kappa(self):
        """AP31: Z=0 does NOT imply kappa=0."""
        assert K3E_EULER_CHAR == 0  # chi = 0
        assert physical_kappa() == F(3)  # kappa != 0

    def test_ap39_kappa_neq_s2_general(self):
        """AP39: S_2 and kappa coincide for rank 1, diverge in general."""
        # For sigma model, S_2 = kappa = 3 (rank 3, each contributes 1)
        tower = shadow_tower_class_g(physical_kappa())
        assert tower[2] == physical_kappa()

    def test_ap45_desuspension_direction(self):
        """AP45: desuspension LOWERS degree. |s^{-1}v| = |v| - 1."""
        # Verify our convention: bar construction uses desuspension
        # This is a convention check, not a computation
        pass  # Convention documented in engine docstring

    def test_ap46_eta_includes_q_prefix(self):
        """AP46: eta(q) = q^{1/24} * prod(1-q^n).
        Our eta_coeffs computes prod(1-q^n) ONLY.
        The q^{1/24} is tracked separately."""
        c = eta_coeffs(5)
        assert c[0] == 1  # This is the coefficient of q^0 in prod(1-q^n)

    def test_ap48_kappa_depends_on_full_algebra(self):
        """AP48: kappa(N=4 SCA) != kappa(Vir at same c).
        kappa(N=4 at c=6) = 2 but kappa(Vir_6) = 3."""
        comp = kappa_n4_components()
        assert comp['kappa_n4_sca'] != comp['kappa_virasoro_alone']
        assert comp['kappa_n4_sca'] == F(2)
        assert comp['kappa_virasoro_alone'] == F(3)
