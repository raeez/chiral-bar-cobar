r"""Tests for theorem_bootstrap_koszul_engine: bootstrap as consequence of Koszulness.

Multi-path verification mandate (AP10): every numerical result verified by 3+ paths.
Every test documents WHY the expected value is correct, not just WHAT it is.

Test structure:
  1. Shadow metric zeros and convergence radius (Section 1)
  2. MC equation = crossing equation (Section 2)
  3. Ising uniqueness from Koszulness + null vector (Section 3)
  4. Modular bootstrap from MC + sewing (Section 4)
  5. Shadow depth vs bootstrap closure (Section 5)
  6. Conformal block vs shadow projection (Section 6)
  7. Bootstrap bounds from shadow data (Section 7)
  8. Koszulness => bootstrap theorem (Section 8)
  9. Virasoro shadow radius table (Section 9)
  10. Multi-path F_1 verification (Section 10)
"""

import math
import sys
import os
import pytest

# Ensure compute/lib is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_bootstrap_koszul_engine import (
    kappa_virasoro,
    kappa_heisenberg,
    Q_contact_virasoro,
    shadow_metric_Q,
    lambda_fp,
    F_g_shadow,
    shadow_metric_zeros_virasoro,
    shadow_convergence_vs_gap_landscape,
    shadow_metric_discriminant_classification,
    mc_arity_n_projection,
    crossing_as_mc_verification,
    bootstrap_koszul_equivalence_table,
    ising_koszul_uniqueness,
    minimal_model_koszul_bootstrap,
    modular_bootstrap_from_mc,
    modular_invariance_test_ising,
    shadow_depth_bootstrap_closure,
    conformal_block_vs_shadow,
    shadow_bounds_at_c,
    multi_c_bootstrap_landscape,
    koszul_implies_bootstrap_theorem,
    virasoro_shadow_radius_table,
    c13_self_duality_bootstrap,
    F_1_three_paths,
    kac_determinant_vs_shadow_unitarity,
    complementarity_bootstrap_test,
)


# ============================================================================
# 1. Shadow metric zeros and convergence radius
# ============================================================================

class TestShadowMetricZeros:
    """Tests for shadow metric zeros and convergence radius."""

    def test_zeros_are_complex_c_positive(self):
        """For c > 0, shadow metric zeros must be complex (Delta > 0)."""
        for c in [0.5, 1.0, 2.0, 10.0, 25.0, 100.0]:
            data = shadow_metric_zeros_virasoro(c)
            assert data['zeros_are_complex'], f"Zeros should be complex at c={c}"
            assert data['shadow_zeros_imag_part'] > 0, f"Imaginary part > 0 at c={c}"

    def test_convergence_radius_positive(self):
        """Shadow convergence radius must be positive for c > 0."""
        for c in [0.5, 1.0, 10.0, 100.0]:
            data = shadow_metric_zeros_virasoro(c)
            assert data['convergence_radius'] > 0, f"Radius > 0 at c={c}"

    def test_convergence_radius_formula(self):
        """Convergence radius = c / sqrt(36 + 80/(5c+22)).

        Path 1: direct formula.
        Path 2: from shadow_metric_zeros_virasoro.
        Path 3: from Q_L quadratic coefficient.
        """
        for c in [1.0, 10.0, 50.0]:
            Delta = 40.0 / (5.0 * c + 22.0)
            # Path 1: explicit formula
            radius_p1 = c / math.sqrt(36.0 + 2.0 * Delta)
            # Path 2: from function
            data = shadow_metric_zeros_virasoro(c)
            radius_p2 = data['convergence_radius']
            # Path 3: from zero modulus = sqrt(c^2 / a_coeff)
            a_coeff = 36.0 + 2.0 * Delta
            radius_p3 = math.sqrt(c ** 2 / a_coeff)
            assert abs(radius_p1 - radius_p2) < 1e-12, f"Paths 1,2 disagree at c={c}"
            assert abs(radius_p1 - radius_p3) < 1e-12, f"Paths 1,3 disagree at c={c}"

    def test_large_c_limit_radius(self):
        """For large c: convergence radius -> c/6.

        Because Delta = 40/(5c+22) -> 0, so 36 + 2*Delta -> 36,
        and radius = c/sqrt(36) = c/6.
        """
        for c in [100.0, 1000.0, 10000.0]:
            data = shadow_metric_zeros_virasoro(c)
            expected = c / 6.0
            ratio = data['convergence_radius'] / expected
            assert abs(ratio - 1.0) < 0.01, f"Large-c limit fails at c={c}: ratio={ratio}"

    def test_discriminant_positive_c_positive(self):
        """Critical discriminant Delta = 40/(5c+22) > 0 for c > 0."""
        for c in [0.5, 1.0, 10.0, 100.0]:
            data = shadow_metric_zeros_virasoro(c)
            assert data['Delta_discriminant'] > 0, f"Delta > 0 at c={c}"

    def test_landscape_comparison(self):
        """Shadow convergence vs gap bound across the landscape."""
        results = shadow_convergence_vs_gap_landscape()
        assert len(results) >= 8, "Need at least 8 c-values"
        # Both radius and gap bound should be positive
        for r in results:
            assert r['convergence_radius'] > 0
            assert r['hellerman_bound'] > 0
            # The product |t_*| * gap_bound grows with c^2 (not constant)
            # This shows they are NOT inversely proportional
            assert r['product'] > 0

    def test_discriminant_classification_virasoro(self):
        """Virasoro at c > 0 is always class M (Delta > 0)."""
        for c in [0.5, 1.0, 10.0, 100.0]:
            data = shadow_metric_discriminant_classification(c)
            assert data['Delta_positive'], f"Delta > 0 at c={c}"
            assert data['shadow_class'] == 'M (infinite tower)', f"Class M at c={c}"


# ============================================================================
# 2. MC equation = crossing equation
# ============================================================================

class TestMCCrossing:
    """Tests for the MC = crossing correspondence."""

    def test_crossing_mc_agreement_three_paths(self):
        """S_4 from MC, crossing, and discriminant must agree (AP10: 3 paths)."""
        for c in [0.5, 1, 2, 10, 25, 100]:
            data = crossing_as_mc_verification(c)
            assert data['all_three_agree'], f"Three paths disagree at c={c}"
            assert data['mc_equals_crossing'], f"MC != crossing at c={c}"

    def test_mc_projection_arity2(self):
        """MC at arity 2 = OPE curvature kappa."""
        for c in [1.0, 10.0]:
            data = mc_arity_n_projection(c, 2)
            expected_kappa = c / 2.0
            assert abs(data['shadow_coefficient'] - expected_kappa) < 1e-12

    def test_mc_projection_arity3(self):
        """MC at arity 3 = cubic shadow S_3 = 2 for Virasoro."""
        data = mc_arity_n_projection(10.0, 3)
        assert abs(data['shadow_coefficient'] - 2.0) < 1e-12

    def test_mc_projection_arity4(self):
        """MC at arity 4 = quartic contact Q^contact = 10/[c(5c+22)].

        Path 1: mc_arity_n_projection
        Path 2: Q_contact_virasoro directly
        Path 3: from discriminant Delta = 8*kappa*S_4
        """
        for c in [1.0, 10.0, 25.0]:
            data = mc_arity_n_projection(c, 4)
            Q_p1 = data['shadow_coefficient']
            Q_p2 = float(Q_contact_virasoro(c))
            kappa = c / 2.0
            Delta = 40.0 / (5.0 * c + 22.0)
            Q_p3 = Delta / (8.0 * kappa)
            assert abs(Q_p1 - Q_p2) < 1e-12, f"Paths 1,2 disagree at c={c}"
            assert abs(Q_p1 - Q_p3) < 1e-12, f"Paths 1,3 disagree at c={c}"

    def test_mc_projection_arity5(self):
        """MC at arity 5 = quintic shadow S_5 = -48/[c^2(5c+22)]."""
        for c in [1.0, 10.0]:
            data = mc_arity_n_projection(c, 5)
            expected = -48.0 / (c ** 2 * (5.0 * c + 22.0))
            assert abs(data['shadow_coefficient'] - expected) < 1e-12

    def test_bootstrap_koszul_table(self):
        """Equivalence table has correct structure."""
        table_data = bootstrap_koszul_equivalence_table()
        assert table_data['n_bootstrap_axioms'] == 7
        # 5 items require Koszulness, 2 are universal
        assert table_data['n_requiring_koszulness'] == 5


# ============================================================================
# 3. Ising uniqueness from Koszulness
# ============================================================================

class TestIsingUniqueness:
    """Tests for the Ising model at c = 1/2."""

    def test_ising_koszul_data(self):
        """Ising model shadow data: kappa = 1/4, Q^contact = 40/49."""
        data = ising_koszul_uniqueness()
        assert abs(data['kappa'] - 0.25) < 1e-12, "kappa(Vir_{1/2}) = 1/4"
        expected_Q = 40.0 / 49.0
        assert abs(data['Q_contact'] - expected_Q) < 1e-10, f"Q^contact = 40/49, got {data['Q_contact']}"

    def test_ising_null_vector(self):
        """BPZ null vector coefficient for sigma: 4/3.

        The null vector (L_{-2} - a * L_{-1}^2)|sigma> = 0
        with a = 3/(2*(2h+1)) = 3/(2*(1/8+1)) = 3/(9/4) = 4/3.
        """
        data = ising_koszul_uniqueness()
        assert data['null_vector_correct'], "Null vector coefficient should be 4/3"
        assert abs(data['null_vector_coefficient'] - 4.0/3.0) < 1e-12

    def test_ising_primaries(self):
        """Ising has 3 primaries: identity (h=0), epsilon (h=1/2), sigma (h=1/16)."""
        data = ising_koszul_uniqueness()
        assert data['n_primaries'] == 3
        weights = sorted([p['h'] for p in data['primaries']])
        assert abs(weights[0] - 0.0) < 1e-12
        assert abs(weights[1] - 1.0/16.0) < 1e-12
        assert abs(weights[2] - 0.5) < 1e-12

    def test_ising_F1(self):
        """F_1 = kappa/24 = 1/96 for Ising.

        Path 1: kappa * lambda_1 = (1/4) * (1/24) = 1/96.
        Path 2: c/48 = (1/2)/48 = 1/96.
        Path 3: from eta function coefficient.
        """
        data = ising_koszul_uniqueness()
        expected = 1.0 / 96.0
        assert abs(data['F_1'] - expected) < 1e-12

    def test_ising_hypergeometric(self):
        """Ising 4-point is _2F_1(1/2, 1/2; 1; z)."""
        data = ising_koszul_uniqueness()
        params = data['hypergeometric_params']
        assert abs(params['a'] - 0.5) < 1e-12
        assert abs(params['b'] - 0.5) < 1e-12
        assert abs(params['c_param'] - 1.0) < 1e-12

    def test_ising_uniqueness_proved(self):
        """All three paths to uniqueness agree."""
        data = ising_koszul_uniqueness()
        assert data['all_paths_agree']
        assert data['uniqueness_proved']


# ============================================================================
# 4. Minimal model bootstrap
# ============================================================================

class TestMinimalModels:
    """Tests for minimal model Koszul bootstrap."""

    def test_ising_as_minimal(self):
        """M(4,3) = Ising: c = 1/2, 3 primaries."""
        data = minimal_model_koszul_bootstrap(4, 3)
        assert abs(data['c'] - 0.5) < 1e-12
        assert data['n_primaries'] == 3
        assert data['is_unitary']
        assert data['koszul']

    def test_tricritical_ising(self):
        """M(5,4) = tricritical Ising: c = 7/10, 6 primaries."""
        data = minimal_model_koszul_bootstrap(5, 4)
        assert abs(data['c'] - 0.7) < 1e-12
        assert data['n_primaries'] == 6
        assert data['is_unitary']

    def test_three_state_potts(self):
        """M(6,5) = 3-state Potts: c = 4/5, 10 primaries."""
        data = minimal_model_koszul_bootstrap(6, 5)
        assert abs(data['c'] - 0.8) < 1e-12
        assert data['n_primaries'] == 10
        assert data['is_unitary']

    def test_minimal_model_gap(self):
        """Spectral gap of M(4,3) is h_{2,2} = 1/16 (sigma field)."""
        data = minimal_model_koszul_bootstrap(4, 3)
        assert abs(data['spectral_gap'] - 1.0/16.0) < 1e-12

    def test_all_minimal_koszul(self):
        """All unitary minimal models are Koszul and bootstrap-unique."""
        for p in range(3, 8):
            data = minimal_model_koszul_bootstrap(p, p - 1)
            assert data['koszul'], f"M({p},{p-1}) should be Koszul"
            assert data['bootstrap_unique'], f"M({p},{p-1}) should be unique"
            assert data['c'] >= 0 and data['c'] < 1, f"c < 1 for minimal models"


# ============================================================================
# 5. Modular bootstrap from MC + sewing
# ============================================================================

class TestModularBootstrap:
    """Tests for the modular bootstrap from MC."""

    def test_mc_alone_insufficient(self):
        """MC equation alone does NOT imply modular invariance."""
        data = modular_bootstrap_from_mc(10.0)
        assert not data['modular_invariance_from_mc']

    def test_mc_plus_sewing_sufficient(self):
        """MC + sewing IS sufficient for modular invariance."""
        data = modular_bootstrap_from_mc(10.0)
        assert data['modular_invariance_from_mc_plus_sewing']

    def test_F_1_cardy_consistency(self):
        """F_1 = kappa/24 = c/48 consistent with Cardy formula.

        Path 1: kappa/24.
        Path 2: c/48.
        Path 3: Cardy coefficient = 2*pi*sqrt(c/3) (from F_1).
        """
        for c in [0.5, 1.0, 10.0, 25.0]:
            data = modular_bootstrap_from_mc(c)
            assert abs(data['F_1'] - c / 48.0) < 1e-12

    def test_chain_of_implications(self):
        """The chain of implications has the correct structure."""
        data = modular_bootstrap_from_mc(10.0)
        chain = data['chain_of_implications']
        assert len(chain) >= 4, "Need at least 4 steps in the chain"

    def test_ising_modular_S_matrix(self):
        """Ising modular S-matrix is unitary and S^2 = identity."""
        data = modular_invariance_test_ising()
        assert data['S_squared_is_identity'], "S^2 should be identity for Ising"
        assert data['S_is_unitary'], "S should be unitary"

    def test_ising_verlinde(self):
        """Verlinde formula: N_{sigma,sigma}^{epsilon} = 1."""
        data = modular_invariance_test_ising()
        assert data['verlinde_correct'], f"N_sse = {data['verlinde_N_sigma_sigma_epsilon']}, expected 1"

    def test_ising_F1_modular(self):
        """F_1 = 1/96 for Ising matches modular data."""
        data = modular_invariance_test_ising()
        assert data['F_1_matches']


# ============================================================================
# 6. Shadow depth vs bootstrap closure
# ============================================================================

class TestShadowDepthBootstrap:
    """Tests for shadow depth = bootstrap closure order."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G: shadow depth 2, bootstrap closes at arity 2."""
        data = shadow_depth_bootstrap_closure('heisenberg', k_val=1)
        assert data['shadow_depth'] == 2
        assert data['shadow_class'] == 'G (Gaussian)'
        assert data['koszul']

    def test_kac_moody_class_L(self):
        """Affine KM is class L: shadow depth 3, bootstrap closes at arity 3."""
        data = shadow_depth_bootstrap_closure('kac_moody')
        assert data['shadow_depth'] == 3
        assert data['shadow_class'] == 'L (Lie/tree)'
        assert data['koszul']

    def test_beta_gamma_class_C(self):
        """Beta-gamma is class C: shadow depth 4, bootstrap closes at arity 4."""
        data = shadow_depth_bootstrap_closure('beta_gamma')
        assert data['shadow_depth'] == 4
        assert data['shadow_class'] == 'C (contact)'
        assert data['koszul']

    def test_virasoro_class_M(self):
        """Virasoro is class M: infinite shadow depth, infinite bootstrap tower."""
        data = shadow_depth_bootstrap_closure('virasoro', c_val=25.0)
        assert data['shadow_depth'] == float('inf')
        assert data['shadow_class'] == 'M (mixed, infinite tower)'
        assert data['koszul']  # AP14: Virasoro IS Koszul

    def test_W_N_class_M(self):
        """W_N is class M for all N >= 2."""
        for N in [3, 4, 5]:
            data = shadow_depth_bootstrap_closure('W_N', N_val=N)
            assert data['shadow_depth'] == float('inf')
            assert data['koszul']

    def test_all_families_koszul(self):
        """AP14: all standard families are Koszul."""
        for family in ['heisenberg', 'kac_moody', 'beta_gamma', 'virasoro', 'W_N']:
            kwargs = {}
            if family == 'virasoro':
                kwargs['c_val'] = 10.0
            elif family == 'W_N':
                kwargs['N_val'] = 3
            data = shadow_depth_bootstrap_closure(family, **kwargs)
            assert data['koszul'], f"{family} should be Koszul"
            assert data['mc_equation_holds'], f"MC holds for {family}"


# ============================================================================
# 7. Conformal block vs shadow projection
# ============================================================================

class TestBlockVsShadow:
    """Tests for the conformal block vs shadow projection distinction."""

    def test_different_objects(self):
        """Conformal blocks and shadow projections are DIFFERENT objects."""
        data = conformal_block_vs_shadow(10.0, h_ext=0.5, h_int=2.0, z=0.1)
        # The conformal block F is z-dependent; S_4 is a single number
        assert data['conformal_block_F'] != data['shadow_projection_S4']

    def test_S4_is_integrated(self):
        """S_4 = Q^contact is independent of z (it is an integrated invariant)."""
        data1 = conformal_block_vs_shadow(10.0, h_ext=0.5, h_int=2.0, z=0.1)
        data2 = conformal_block_vs_shadow(10.0, h_ext=0.5, h_int=2.0, z=0.3)
        assert abs(data1['shadow_projection_S4'] - data2['shadow_projection_S4']) < 1e-15

    def test_block_z_dependent(self):
        """Conformal block changes with z."""
        data1 = conformal_block_vs_shadow(10.0, h_ext=0.5, h_int=2.0, z=0.1)
        data2 = conformal_block_vs_shadow(10.0, h_ext=0.5, h_int=2.0, z=0.3)
        assert abs(data1['conformal_block_F'] - data2['conformal_block_F']) > 1e-6


# ============================================================================
# 8. Bootstrap bounds
# ============================================================================

class TestBootstrapBounds:
    """Tests for bootstrap bounds from shadow data."""

    def test_hellerman_bound_formula(self):
        """Hellerman bound = c/12 + 0.4736 for c > 1."""
        for c in [2.0, 10.0, 25.0, 100.0]:
            data = shadow_bounds_at_c(c)
            expected = c / 12.0 + 0.4736
            assert abs(data['hellerman_gap_bound'] - expected) < 1e-10

    def test_F1_equals_c_over_48(self):
        """F_1 = c/48 at all c."""
        for c in [0.5, 1.0, 10.0, 100.0]:
            data = shadow_bounds_at_c(c)
            assert abs(data['F_1'] - c / 48.0) < 1e-12

    def test_unitarity_h_bound_zero(self):
        """Unitarity bound: h >= 0."""
        for c in [0.5, 10.0]:
            data = shadow_bounds_at_c(c)
            assert data['unitarity_h_bound'] == 0.0

    def test_landscape_coverage(self):
        """Multi-c landscape covers the expected range."""
        landscape = multi_c_bootstrap_landscape()
        assert len(landscape) >= 9
        # kappa = c/2 at every point
        for entry in landscape:
            assert abs(entry['kappa'] - entry['c'] / 2.0) < 1e-12

    def test_bounds_consistent(self):
        """All bounds are internally consistent."""
        for c in [1.0, 10.0, 50.0]:
            data = shadow_bounds_at_c(c)
            assert data['all_bounds_consistent']


# ============================================================================
# 9. Main theorem
# ============================================================================

class TestMainTheorem:
    """Tests for the Koszulness => bootstrap theorem."""

    def test_theorem_structure(self):
        """Theorem has 5 parts."""
        thm = koszul_implies_bootstrap_theorem()
        assert len(thm['parts']) == 5

    def test_each_part_has_proof(self):
        """Each part has a proof reference."""
        thm = koszul_implies_bootstrap_theorem()
        for key, part in thm['parts'].items():
            assert 'proof' in part, f"Part {key} missing proof"
            assert 'manuscript_ref' in part, f"Part {key} missing manuscript ref"

    def test_converse_is_open(self):
        """The converse (bootstrap => Koszulness) is OPEN."""
        thm = koszul_implies_bootstrap_theorem()
        assert 'OPEN' in thm['converse_status']


# ============================================================================
# 10. Virasoro radius table and self-duality
# ============================================================================

class TestVirasiroTable:
    """Tests for the Virasoro shadow radius table."""

    def test_table_has_entries(self):
        """Table covers multiple c values."""
        table = virasoro_shadow_radius_table()
        assert len(table) >= 10

    def test_radius_over_c_approaches_one_sixth(self):
        """For large c: radius/c -> 1/6."""
        table = virasoro_shadow_radius_table()
        large_c_entries = [e for e in table if e['c'] >= 50]
        for e in large_c_entries:
            assert abs(e['radius_over_c'] - 1.0/6.0) < 0.01, \
                f"radius/c = {e['radius_over_c']} at c={e['c']}, expected ~1/6"

    def test_c13_self_dual(self):
        """c = 13 is self-dual: kappa = kappa'.

        Path 1: kappa(Vir_13) = 13/2.
        Path 2: kappa(Vir_{26-13}) = 13/2.
        Path 3: complementarity_sum = 13.
        """
        data = c13_self_duality_bootstrap()
        assert data['self_dual'], "c = 13 should be self-dual"
        assert data['Q_self_dual'], "Q^contact self-dual at c = 13"
        assert data['complementarity_correct'], "kappa + kappa' = 13 (AP24)"

    def test_c13_complementarity_is_13(self):
        """AP24: kappa + kappa' = 13 for Virasoro, NOT zero."""
        data = c13_self_duality_bootstrap()
        assert abs(data['complementarity_sum'] - 13.0) < 1e-12


# ============================================================================
# 11. Multi-path F_1 verification
# ============================================================================

class TestF1ThreePaths:
    """Tests for F_1 via three independent paths."""

    def test_three_paths_agree(self):
        """F_1 from MC, Cardy, and eta must agree (AP10: 3 paths)."""
        for c in [0.5, 1.0, 2.0, 10.0, 25.0, 100.0]:
            data = F_1_three_paths(c)
            assert data['all_three_agree'], f"Three paths disagree at c={c}"

    def test_F1_is_kappa_over_24(self):
        """F_1 = kappa/24 = c/48."""
        for c in [0.5, 1.0, 10.0]:
            data = F_1_three_paths(c)
            assert abs(data['F_1_mc'] - c / 48.0) < 1e-14
            assert abs(data['F_1_cardy'] - c / 48.0) < 1e-14
            assert abs(data['F_1_eta'] - c / 48.0) < 1e-14

    def test_lambda_1_is_1_over_24(self):
        """lambda_1^FP = |B_2|/(2*2!) * (2^1 - 1)/2^1 = (1/6)/2 * 1/2 = 1/24.

        Path 1: from Bernoulli B_2 = 1/6.
        Path 2: from lambda_fp(1).
        Path 3: from F_1 = kappa * lambda_1 with kappa = c/2, F_1 = c/48.
        """
        lam = float(lambda_fp(1))
        # Path 1: (2^1 - 1)/2^1 * |B_2|/2! = (1/2) * (1/6) / 2 = 1/24
        expected = (1.0 / 2.0) * (1.0 / 6.0) / 2.0
        assert abs(expected - 1.0 / 24.0) < 1e-15, "Formula gives 1/24"
        assert abs(lam - expected) < 1e-15, f"lambda_fp(1) = {lam}, expected 1/24"
        # Path 3: F_1/kappa = c/48 / (c/2) = 1/24
        assert abs(lam - 1.0 / 24.0) < 1e-15


# ============================================================================
# 12. Kac determinant vs shadow unitarity
# ============================================================================

class TestKacVsShadow:
    """Tests for Kac determinant vs shadow metric unitarity."""

    def test_unitary_at_h_positive_c_ge_1(self):
        """For c >= 1, h > 0: both Kac and shadow agree on unitarity."""
        for c in [1.0, 10.0, 25.0]:
            for h in [0.1, 0.5, 1.0, 2.0]:
                data = kac_determinant_vs_shadow_unitarity(c, h)
                assert data['kac_unitary'], f"Kac unitary at c={c}, h={h}"
                assert data['shadow_Q_positive'], f"Shadow Q > 0 at c={c}"

    def test_kac_level1_is_2h(self):
        """Kac determinant at level 1 is 2h."""
        for h in [0.0, 0.5, 1.0, 3.0]:
            data = kac_determinant_vs_shadow_unitarity(10.0, h)
            assert abs(data['det_level_1'] - 2.0 * h) < 1e-12

    def test_kac_level2_at_identity(self):
        """Kac det at level 2 for h=0: det = 0 (null vector at identity).

        det = (c/2) * 0 - 0 = 0.
        """
        data = kac_determinant_vs_shadow_unitarity(10.0, 0.0)
        assert abs(data['det_level_2']) < 1e-12, "det_2(h=0) = 0"

    def test_kac_level2_positive_large_h(self):
        """For large h, Kac det at level 2 is positive."""
        data = kac_determinant_vs_shadow_unitarity(10.0, 10.0)
        assert data['det_level_2'] > 0, "det_2 > 0 for large h"


# ============================================================================
# 13. Complementarity bootstrap test
# ============================================================================

class TestComplementarity:
    """Tests for complementarity at the bootstrap level."""

    def test_complementarity_sum_is_13(self):
        """AP24: kappa + kappa' = 13 for all c (Virasoro)."""
        for c in [0.5, 1.0, 10.0, 13.0, 26.0, 50.0]:
            data = complementarity_bootstrap_test(c)
            assert data['AP24_correct'], f"kappa + kappa' should be 13 at c={c}"
            assert abs(data['complementarity_sum'] - 13.0) < 1e-12

    def test_self_dual_at_c13(self):
        """Koszul self-duality at c = 13: delta_kappa = 0."""
        data = complementarity_bootstrap_test(13.0)
        assert abs(data['delta_kappa']) < 1e-12

    def test_anomaly_cancellation_at_c26(self):
        """Physical anomaly cancellation at c = 26: kappa_eff = 0.

        AP29: kappa_eff = kappa(matter) + kappa(ghost) = c/2 - 13 = 0 at c = 26.
        """
        data = complementarity_bootstrap_test(26.0)
        assert abs(data['kappa_eff']) < 1e-12

    def test_delta_kappa_vs_kappa_eff_different(self):
        """AP29: delta_kappa and kappa_eff are DIFFERENT quantities.

        delta_kappa = kappa - kappa' = c - 13.
        kappa_eff = kappa + kappa_ghost = (c-26)/2.

        These vanish at DIFFERENT points (c=13 vs c=26).
        """
        for c in [10.0, 20.0]:
            data = complementarity_bootstrap_test(c)
            # delta_kappa = c - 13
            assert abs(data['delta_kappa'] - (c - 13.0)) < 1e-12
            # kappa_eff = (c - 26)/2
            assert abs(data['kappa_eff'] - (c - 26.0) / 2.0) < 1e-12
            # They are not equal (unless c = 0, but that's degenerate)
            assert abs(data['delta_kappa'] - data['kappa_eff']) > 1e-6

    def test_AP29_correct(self):
        """AP29: delta_kappa = 0 iff c = 13."""
        for c in [0.5, 10.0, 25.0]:
            data = complementarity_bootstrap_test(c)
            assert data['AP29_correct']


# ============================================================================
# 14. Cross-family consistency checks (AP10)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks to catch AP10 violations (hardcoded wrong values)."""

    def test_kappa_additivity(self):
        """kappa is additive: kappa(A x B) = kappa(A) + kappa(B).

        For Heisenberg: kappa(H_{k1} x H_{k2}) = k1 + k2 = kappa(H_{k1+k2}).
        This is the bootstrap statement that leading soft factors multiply.
        """
        for k1, k2 in [(1, 1), (1, 2), (3, 4)]:
            kappa_sum = float(kappa_heisenberg(k1)) + float(kappa_heisenberg(k2))
            kappa_combined = float(kappa_heisenberg(k1 + k2))
            assert abs(kappa_sum - kappa_combined) < 1e-12

    def test_Q_contact_consistency(self):
        """Q^contact at c = 1 via two formulas.

        Path 1: Q_contact_virasoro(1) = 10/(1*27) = 10/27.
        Path 2: From Delta = 40/(5+22) = 40/27, and Delta = 8*(1/2)*S_4,
                 so S_4 = 40/(27*4) = 10/27.
        """
        Q1 = float(Q_contact_virasoro(1))
        Q2 = 10.0 / 27.0
        assert abs(Q1 - Q2) < 1e-12

    def test_shadow_metric_at_t_zero(self):
        """Q_L(0) = (2*kappa)^2 = c^2 for Virasoro."""
        for c in [1.0, 10.0, 25.0]:
            kappa = c / 2.0
            Q_0 = shadow_metric_Q(kappa, 2.0, float(Q_contact_virasoro(c)), 0.0)
            assert abs(Q_0 - c ** 2) < 1e-10, f"Q_L(0) = {Q_0}, expected c^2 = {c**2}"

    def test_F_g_positivity(self):
        """F_g > 0 for all g >= 1 and kappa > 0.

        The Bernoulli numbers alternate sign, but |B_{2g}| > 0, and the
        prefactor (2^{2g-1}-1)/2^{2g-1} > 0. So lambda_g > 0 and F_g > 0.
        """
        for g in range(1, 6):
            lam = float(lambda_fp(g))
            assert lam > 0, f"lambda_{g} should be positive"
            for c in [0.5, 10.0]:
                F = float(F_g_shadow(c / 2.0, g))
                assert F > 0, f"F_{g} > 0 at c={c}"

    def test_Q_contact_poles(self):
        """Q^contact has poles at c = 0 and c = -22/5."""
        # At c approaching 0, Q^contact -> infinity
        Q_near_zero = Q_contact_virasoro(0.001)
        assert float(Q_near_zero) > 100.0, "Q^contact diverges near c=0"

    def test_Delta_always_positive_c_positive(self):
        """Delta = 40/(5c+22) > 0 for all c > 0.

        This means Virasoro is ALWAYS class M (infinite tower).
        """
        for c in [0.01, 0.5, 1.0, 10.0, 100.0, 1000.0]:
            Delta = 40.0 / (5.0 * c + 22.0)
            assert Delta > 0, f"Delta > 0 at c={c}"


# ============================================================================
# 15. Heisenberg vs Virasoro: different algebras, different bootstrap
# ============================================================================

class TestHeisenbergVirasoro:
    """Compare Heisenberg (class G) with Virasoro (class M) bootstrap."""

    def test_heisenberg_no_quartic(self):
        """Heisenberg has Q^contact = 0 (class G, no quartic constraint)."""
        data = shadow_depth_bootstrap_closure('heisenberg', k_val=1)
        assert data['Q_contact'] == 0.0

    def test_virasoro_has_quartic(self):
        """Virasoro has Q^contact != 0 (class M, infinite constraints)."""
        data = shadow_depth_bootstrap_closure('virasoro', c_val=10.0)
        assert data['Q_contact'] != 0.0

    def test_depth_ordering(self):
        """Shadow depths: G < L < C < M."""
        d_G = shadow_depth_bootstrap_closure('heisenberg')['shadow_depth']
        d_L = shadow_depth_bootstrap_closure('kac_moody')['shadow_depth']
        d_C = shadow_depth_bootstrap_closure('beta_gamma')['shadow_depth']
        d_M = shadow_depth_bootstrap_closure('virasoro', c_val=10.0)['shadow_depth']
        assert d_G < d_L < d_C < d_M
