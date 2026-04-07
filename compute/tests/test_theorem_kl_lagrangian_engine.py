r"""Tests for theorem_kl_lagrangian_engine.py.

Verification strategy (multi-path, per CLAUDE.md mandate):
  1. Symplectic form properties (antisymmetry, nondegeneracy)
  2. Verdier involution properties (involution, anti-commutativity)
  3. Lagrangian isotropy (code, error, cross-pairing)
  4. Path 1: Verdier anti-involution proof
  5. Path 2: Lagrangian geometry proof
  6. Path 3: Shadow depth = redundancy channels
  7. Path 4: Bar-cobar adjunction = QEC recovery
  8. Four-path synthesis and consistency
  9. Explicit numerical KL verification (1D and multi-D)
  10. Off-diagonal KL condition
  11. Cross-family census
  12. Complementarity kappa constraint
  13. SymPy exact verification
  14. Genus tower and entanglement wedge
  15. Cross-engine consistency checks
"""

import pytest
from fractions import Fraction
from sympy import Rational
import numpy as np

from compute.lib.theorem_kl_lagrangian_engine import (
    # Foundations
    verdier_symplectic_form,
    verdier_involution,
    verify_anti_commutativity,
    lagrangian_subspaces,
    verify_isotropy,
    # Path 1
    path1_verdier_proof,
    # Path 2
    shifted_symplectic_degree,
    lagrangian_dimension_check,
    path2_lagrangian_proof,
    # Path 3
    mc_redundancy_at_arity,
    path3_shadow_depth_proof,
    SHADOW_DEPTH_TABLE,
    # Path 4
    bar_cobar_recovery_structure,
    path4_barcobar_proof,
    # Numerical
    explicit_kl_verification_1d,
    explicit_kl_verification_lagrangian,
    explicit_kl_off_diagonal,
    # Synthesis
    verify_kl_four_paths,
    kl_family_census,
    # Complementarity
    complementarity_kl_constraint,
    # SymPy
    sympy_verdier_isotropy,
    sympy_kl_scalar_automatic,
    # Entanglement wedge
    entanglement_wedge_from_bar,
    # Genus
    genus_dependent_code_dimension,
    genus_tower_kl_status,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    shadow_depth_class,
    STANDARD_KAPPAS,
)


# ===================================================================
# 1. SYMPLECTIC FORM PROPERTIES
# ===================================================================

class TestSymplecticForm:
    """Verify the symplectic form J has the correct algebraic properties."""

    def test_antisymmetric_n1(self):
        J = verdier_symplectic_form(1)
        assert np.allclose(J + J.T, 0), "J should be antisymmetric"

    def test_antisymmetric_n5(self):
        J = verdier_symplectic_form(5)
        assert np.allclose(J + J.T, 0)

    def test_nondegenerate_n1(self):
        J = verdier_symplectic_form(1)
        assert np.linalg.matrix_rank(J) == 2

    def test_nondegenerate_n10(self):
        J = verdier_symplectic_form(10)
        assert np.linalg.matrix_rank(J) == 20

    def test_shape(self):
        for n in [1, 3, 7]:
            J = verdier_symplectic_form(n)
            assert J.shape == (2 * n, 2 * n)

    def test_det_is_one(self):
        """det(J) = 1 for the standard symplectic form."""
        for n in [1, 2, 3, 4]:
            J = verdier_symplectic_form(n)
            assert abs(np.linalg.det(J) - 1.0) < 1e-10

    def test_J_squared(self):
        """J^2 = -I_{2n} for the standard symplectic form."""
        for n in [1, 2, 5]:
            J = verdier_symplectic_form(n)
            assert np.allclose(J @ J, -np.eye(2 * n))


# ===================================================================
# 2. VERDIER INVOLUTION PROPERTIES
# ===================================================================

class TestVerdierInvolution:
    """Verify properties of the Verdier involution sigma."""

    def test_involution_n1(self):
        sigma = verdier_involution(1)
        assert np.allclose(sigma @ sigma, np.eye(2))

    def test_involution_n10(self):
        sigma = verdier_involution(10)
        assert np.allclose(sigma @ sigma, np.eye(20))

    def test_eigenvalues(self):
        """sigma has eigenvalues +1 (n times) and -1 (n times)."""
        for n in [1, 3, 5]:
            sigma = verdier_involution(n)
            evals = np.linalg.eigvalsh(sigma)
            evals_sorted = sorted(evals)
            expected = [-1.0] * n + [1.0] * n
            assert np.allclose(evals_sorted, expected)

    def test_anti_commutativity_small(self):
        for n in [1, 2, 3, 4, 5]:
            assert verify_anti_commutativity(n)

    def test_anti_commutativity_large(self):
        assert verify_anti_commutativity(50)

    def test_anti_commutativity_identity(self):
        """sigma^T J sigma = -J, verified explicitly."""
        n = 3
        J = verdier_symplectic_form(n)
        sigma = verdier_involution(n)
        product = sigma.T @ J @ sigma
        assert np.allclose(product, -J)


# ===================================================================
# 3. LAGRANGIAN ISOTROPY
# ===================================================================

class TestLagrangianIsotropy:
    """Verify isotropy and Lagrangian properties of code/error spaces."""

    def test_isotropy_n1(self):
        result = verify_isotropy(1)
        assert result['code_isotropic']
        assert result['error_isotropic']
        assert result['cross_pairing_nondegenerate']

    def test_isotropy_n5(self):
        result = verify_isotropy(5)
        assert result['code_isotropic']
        assert result['error_isotropic']

    def test_isotropy_n20(self):
        result = verify_isotropy(20)
        assert result['code_isotropic']
        assert result['error_isotropic']
        assert result['cross_pairing_nondegenerate']

    def test_code_rate(self):
        for n in [1, 3, 7, 10]:
            result = verify_isotropy(n)
            assert result['code_rate'] == Fraction(1, 2)

    def test_lagrangian_subspace_dimensions(self):
        for n in [1, 3, 5]:
            Vp, Vm = lagrangian_subspaces(n)
            assert Vp.shape == (2 * n, n)
            assert Vm.shape == (2 * n, n)

    def test_complementarity_span(self):
        """V+ and V- span the full space."""
        for n in [1, 3, 5]:
            Vp, Vm = lagrangian_subspaces(n)
            full = np.hstack([Vp, Vm])
            assert np.linalg.matrix_rank(full) == 2 * n


# ===================================================================
# 4. PATH 1: VERDIER ANTI-INVOLUTION
# ===================================================================

class TestPath1Verdier:
    """Path 1: Knill-Laflamme from Verdier anti-involution."""

    def test_verdier_proof_n1(self):
        result = path1_verdier_proof(1)
        assert result['anti_commutativity']
        assert result['isotropy_proved']
        assert result['kl_genus_1']

    def test_verdier_proof_n5(self):
        result = path1_verdier_proof(5)
        assert result['anti_commutativity']
        assert result['isotropy_proved']
        assert result['kl_genus_1']
        assert result['kl_genus_1_violations'] == 0

    def test_verdier_proof_n10(self):
        result = path1_verdier_proof(10)
        assert result['isotropy_proved']
        assert result['cross_pairing']

    def test_verdier_mechanism(self):
        result = path1_verdier_proof(3)
        assert 'sigma^T J sigma = -J' in result['mechanism']


# ===================================================================
# 5. PATH 2: LAGRANGIAN GEOMETRY
# ===================================================================

class TestPath2Lagrangian:
    """Path 2: Knill-Laflamme from Lagrangian geometry."""

    def test_shifted_degree_g1(self):
        assert shifted_symplectic_degree(1) == 0

    def test_shifted_degree_g2(self):
        assert shifted_symplectic_degree(2) == -3

    def test_shifted_degree_g3(self):
        assert shifted_symplectic_degree(3) == -6

    def test_shifted_degree_formula(self):
        for g in range(1, 10):
            assert shifted_symplectic_degree(g) == -(3 * g - 3)

    def test_lagrangian_dimension(self):
        for n in [1, 3, 5, 10]:
            result = lagrangian_dimension_check(n)
            assert result['lagrangian']
            assert result['rate'] == Fraction(1, 2)
            assert result['maximally_isotropic']

    def test_lagrangian_proof_g1(self):
        result = path2_lagrangian_proof(3, g=1)
        assert result['lagrangian_verified']
        assert result['kl_from_isotropy']
        assert result['code_rate'] == Fraction(1, 2)
        assert result['shifted_symplectic_degree'] == 0

    def test_lagrangian_proof_g2(self):
        result = path2_lagrangian_proof(5, g=2)
        assert result['lagrangian_verified']
        assert result['shifted_symplectic_degree'] == -3


# ===================================================================
# 6. PATH 3: SHADOW DEPTH
# ===================================================================

class TestPath3ShadowDepth:
    """Path 3: Shadow depth = redundancy channels."""

    def test_mc_redundancy_arity2(self):
        assert mc_redundancy_at_arity(2) == 0

    def test_mc_redundancy_arity3(self):
        assert mc_redundancy_at_arity(3) == 1

    def test_mc_redundancy_arity4(self):
        assert mc_redundancy_at_arity(4) == 2

    def test_mc_redundancy_general(self):
        for r in range(2, 20):
            assert mc_redundancy_at_arity(r) == r - 2

    def test_mc_redundancy_low(self):
        assert mc_redundancy_at_arity(0) == 0
        assert mc_redundancy_at_arity(1) == 0

    def test_heisenberg_class_G(self):
        result = path3_shadow_depth_proof('heisenberg')
        assert result['shadow_class'] == 'G'
        assert result['redundancy_channels'] == 0
        assert result['arity_distance'] == 2
        assert result['channels_consistent']

    def test_affine_class_L(self):
        result = path3_shadow_depth_proof('affine')
        assert result['shadow_class'] == 'L'
        assert result['redundancy_channels'] == 1
        assert result['channels_consistent']

    def test_betagamma_class_C(self):
        result = path3_shadow_depth_proof('betagamma')
        assert result['shadow_class'] == 'C'
        assert result['redundancy_channels'] == 2
        assert result['channels_consistent']

    def test_virasoro_class_M(self):
        result = path3_shadow_depth_proof('virasoro')
        assert result['shadow_class'] == 'M'
        assert result['redundancy_channels'] == -1  # infinite

    def test_arity_distance_universal(self):
        """Arity filtration distance is 2 for ALL families."""
        for fam in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            result = path3_shadow_depth_proof(fam)
            assert result['arity_distance'] == 2


# ===================================================================
# 7. PATH 4: BAR-COBAR ADJUNCTION
# ===================================================================

class TestPath4BarCobar:
    """Path 4: Bar-cobar adjunction as QEC recovery."""

    def test_barcobar_heisenberg(self):
        result = path4_barcobar_proof('heisenberg')
        assert result['exact_recovery']
        assert result['koszulness_iff_recovery']

    def test_barcobar_virasoro(self):
        result = path4_barcobar_proof('virasoro')
        assert result['exact_recovery']

    def test_barcobar_affine(self):
        result = path4_barcobar_proof('affine')
        assert result['exact_recovery']

    def test_barcobar_betagamma(self):
        result = path4_barcobar_proof('betagamma')
        assert result['exact_recovery']

    def test_recovery_structure(self):
        result = bar_cobar_recovery_structure('heisenberg')
        assert result['is_koszul']
        assert result['exact_recovery']
        assert result['koszulness_characterizations'] == 12

    def test_ap25_note(self):
        """Verify AP25 is respected: Omega(B(A)) = A, not A!."""
        result = bar_cobar_recovery_structure('heisenberg')
        assert 'Omega(B(A)) = A' in result['note_ap25']
        assert 'D_Ran(B(A)) = B(A!)' in result['note_ap25']


# ===================================================================
# 8. FOUR-PATH SYNTHESIS
# ===================================================================

class TestFourPathSynthesis:
    """Verify consistency across all four proof paths."""

    def test_heisenberg_four_paths(self):
        result = verify_kl_four_paths('heisenberg', n=3, g=1)
        assert result['all_paths_agree']
        assert result['num_paths'] == 4

    def test_affine_four_paths(self):
        result = verify_kl_four_paths('affine', n=3, g=1)
        assert result['all_paths_agree']

    def test_betagamma_four_paths(self):
        result = verify_kl_four_paths('betagamma', n=3, g=1)
        assert result['all_paths_agree']

    def test_virasoro_four_paths(self):
        result = verify_kl_four_paths('virasoro', n=3, g=1)
        assert result['all_paths_agree']

    def test_four_paths_multiple_dims(self):
        for n in [1, 2, 5, 10]:
            result = verify_kl_four_paths('heisenberg', n=n, g=1)
            assert result['all_paths_agree']


# ===================================================================
# 9. EXPLICIT NUMERICAL KL VERIFICATION
# ===================================================================

class TestExplicitKLNumerical:
    """Explicit numerical verification of KL conditions."""

    def test_1d_kl_100_errors(self):
        result = explicit_kl_verification_1d(100)
        assert result['kl_satisfied']
        assert result['max_residual'] < 1e-10

    def test_1d_kl_500_errors(self):
        result = explicit_kl_verification_1d(500, seed=123)
        assert result['kl_satisfied']

    def test_1d_c_values_nonneg(self):
        """c(E^dag E) >= 0 for all errors (positive semidefiniteness)."""
        result = explicit_kl_verification_1d(100)
        assert result['c_values_all_nonneg']

    def test_lagrangian_kl_n2(self):
        result = explicit_kl_verification_lagrangian(2, 50)
        assert result['kl_satisfied']

    def test_lagrangian_kl_n5(self):
        result = explicit_kl_verification_lagrangian(5, 30)
        assert result['kl_satisfied']

    def test_lagrangian_kl_n10(self):
        result = explicit_kl_verification_lagrangian(10, 20)
        assert result['kl_satisfied']

    def test_off_diagonal_n2(self):
        result = explicit_kl_off_diagonal(2, 50)
        assert result['off_diag_vanish']

    def test_off_diagonal_n5(self):
        result = explicit_kl_off_diagonal(5, 30)
        assert result['off_diag_vanish']

    def test_off_diagonal_n10(self):
        result = explicit_kl_off_diagonal(10, 20)
        assert result['off_diag_vanish']


# ===================================================================
# 10. CROSS-FAMILY CENSUS
# ===================================================================

class TestCrossFamilyCensus:
    """Cross-family consistency checks."""

    def test_census_all_agree(self):
        census = kl_family_census()
        for fam, data in census.items():
            assert data['all_paths_agree'], f"KL failed for {fam}"

    def test_census_code_rate(self):
        """All families have code rate 1/2 (Lagrangian)."""
        census = kl_family_census()
        for fam, data in census.items():
            assert data['code_rate'] == Fraction(1, 2), f"Rate wrong for {fam}"

    def test_census_arity_distance(self):
        """All families have arity distance 2."""
        census = kl_family_census()
        for fam, data in census.items():
            assert data['arity_distance'] == 2, f"Distance wrong for {fam}"

    def test_census_class_consistency(self):
        """Shadow class matches expected for each family."""
        expected = {
            'heisenberg': 'G',
            'affine': 'L',
            'betagamma': 'C',
            'virasoro': 'M',
        }
        census = kl_family_census()
        for fam, data in census.items():
            assert data['shadow_class'] == expected[fam], \
                f"Class mismatch for {fam}: {data['shadow_class']} != {expected[fam]}"

    def test_census_redundancy_channels(self):
        expected = {
            'heisenberg': 0,
            'affine': 1,
            'betagamma': 2,
            'virasoro': -1,  # infinite
        }
        census = kl_family_census()
        for fam, data in census.items():
            assert data['redundancy_channels'] == expected[fam]


# ===================================================================
# 11. COMPLEMENTARITY KAPPA CONSTRAINT
# ===================================================================

class TestComplementarityConstraint:
    """Complementarity constraints on the QEC code."""

    def test_kappa_sum_13(self):
        """kappa + kappa' = 13 for Virasoro (AP24)."""
        for c in [1, Rational(1, 2), 10, 13, 25, Rational(7, 10)]:
            result = complementarity_kl_constraint(c)
            assert result['kappa_sum_is_13']

    def test_self_dual_c13(self):
        result = complementarity_kl_constraint(Rational(13))
        assert result['self_dual']
        assert result['code_fraction'] == Rational(1, 2)

    def test_code_fraction_c1(self):
        result = complementarity_kl_constraint(Rational(1))
        assert result['kappa'] == Rational(1, 2)
        assert result['kappa_dual'] == Rational(25, 2)
        assert result['code_fraction'] == Rational(1, 26)

    def test_code_fraction_c26(self):
        """At c = 26 (critical string): kappa = 13, kappa' = 0."""
        result = complementarity_kl_constraint(Rational(26))
        assert result['kappa'] == 13
        assert result['kappa_dual'] == 0
        assert result['code_fraction'] == 1

    def test_code_rate_always_half(self):
        """Code rate is 1/2 regardless of c (Lagrangian)."""
        for c in [1, 5, 13, 26]:
            result = complementarity_kl_constraint(Rational(c))
            assert result['code_rate'] == Fraction(1, 2)


# ===================================================================
# 12. SYMPY EXACT VERIFICATION
# ===================================================================

class TestSympyExact:
    """Exact algebraic verification using SymPy."""

    def test_exact_isotropy_n1(self):
        result = sympy_verdier_isotropy(1)
        assert result['anti_commutativity_exact']
        assert result['code_isotropy_exact']
        assert result['error_isotropy_exact']
        assert result['cross_pairing_exact']

    def test_exact_isotropy_n3(self):
        result = sympy_verdier_isotropy(3)
        assert result['anti_commutativity_exact']
        assert result['code_isotropy_exact']

    def test_exact_isotropy_n5(self):
        result = sympy_verdier_isotropy(5)
        assert result['anti_commutativity_exact']
        assert result['cross_pairing_exact']

    def test_kl_scalar_automatic(self):
        result = sympy_kl_scalar_automatic()
        assert result['kl_automatic']
        assert result['dim_code'] == 1


# ===================================================================
# 13. ENTANGLEMENT WEDGE
# ===================================================================

class TestEntanglementWedge:
    """Entanglement wedge from bar-cobar."""

    def test_rt_virasoro_c26(self):
        result = entanglement_wedge_from_bar('virasoro', Rational(26))
        assert result['rt_coefficient'] == Rational(26, 3)

    def test_rt_virasoro_c1(self):
        result = entanglement_wedge_from_bar('virasoro', Rational(1))
        assert result['rt_coefficient'] == Rational(1, 3)

    def test_rt_virasoro_c13(self):
        """Self-dual point."""
        result = entanglement_wedge_from_bar('virasoro', Rational(13))
        assert result['rt_coefficient'] == Rational(13, 3)

    def test_maximal_wedge(self):
        for fam in ['heisenberg', 'virasoro', 'affine', 'betagamma']:
            result = entanglement_wedge_from_bar(fam)
            assert result['wedge_maximal']
            assert result['exact_reconstruction']


# ===================================================================
# 14. GENUS TOWER
# ===================================================================

class TestGenusTower:
    """Genus-dependent code structure."""

    def test_genus_1_code_dim(self):
        result = genus_dependent_code_dimension(1)
        assert result['dim_code_scalar'] == 1
        assert result['kl_automatic_at_scalar']
        assert result['code_rate'] == Fraction(1, 2)

    def test_genus_2_shifted_degree(self):
        result = genus_dependent_code_dimension(2)
        assert result['shifted_symplectic_degree'] == -3

    def test_genus_tower_structure(self):
        tower = genus_tower_kl_status()
        assert len(tower) == 5
        assert tower[0]['kl_status'] == 'automatic'
        for entry in tower[1:]:
            assert entry['kl_status'] == 'Lagrangian-preserving errors'

    def test_genus_tower_code_rate(self):
        """Code rate is 1/2 at every genus."""
        tower = genus_tower_kl_status()
        for entry in tower:
            assert entry['code_rate'] == Fraction(1, 2)

    def test_genus_tower_shifted_degrees(self):
        tower = genus_tower_kl_status()
        for entry in tower:
            g = entry['genus']
            assert entry['shifted_degree'] == -(3 * g - 3)


# ===================================================================
# 15. CROSS-ENGINE CONSISTENCY
# ===================================================================

class TestCrossEngineConsistency:
    """Cross-checks against other compute engines."""

    def test_shadow_class_matches_entanglement_engine(self):
        """Shadow classes from this engine match entanglement_shadow_engine."""
        for fam in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            from_this = path3_shadow_depth_proof(fam)['shadow_class']
            from_other = shadow_depth_class(fam)
            assert from_this == from_other, \
                f"Shadow class mismatch for {fam}: {from_this} != {from_other}"

    def test_kappa_values_match(self):
        """Kappa values are consistent with STANDARD_KAPPAS."""
        assert kappa_heisenberg(Rational(1)) == STANDARD_KAPPAS['heisenberg_1']
        assert kappa_virasoro(Rational(13)) == STANDARD_KAPPAS['virasoro_13']

    def test_complementarity_sum_13_matches(self):
        """AP24: kappa + kappa' = 13 for Virasoro, cross-checked."""
        for c in [1, Rational(1, 2), 13, 26, Rational(7, 10)]:
            kap = kappa_virasoro(c)
            kap_dual = kappa_virasoro(26 - Rational(c))
            assert kap + kap_dual == 13

    def test_code_rate_half_universal(self):
        """Universal code rate 1/2 is consistent across all constructions."""
        # From isotropy
        for n in [1, 3, 5]:
            iso = verify_isotropy(n)
            assert iso['code_rate'] == Fraction(1, 2)
        # From Lagrangian check
        for n in [1, 3, 5]:
            lag = lagrangian_dimension_check(n)
            assert lag['rate'] == Fraction(1, 2)
        # From complementarity
        for c in [1, 13, 26]:
            comp = complementarity_kl_constraint(Rational(c))
            assert comp['code_rate'] == Fraction(1, 2)
        # From genus tower
        for entry in genus_tower_kl_status():
            assert entry['code_rate'] == Fraction(1, 2)


# ===================================================================
# 16. MULTI-PATH VERIFICATION: INDEPENDENCE OF PATHS
# ===================================================================

class TestMultiPathIndependence:
    """Verify paths are genuinely independent."""

    def test_path1_uses_anti_commutativity(self):
        """Path 1 depends on sigma^T J sigma = -J."""
        result = path1_verdier_proof(3)
        assert 'sigma^T J sigma = -J' in result['mechanism']

    def test_path2_uses_lagrangian(self):
        """Path 2 depends on Lagrangian geometry."""
        result = path2_lagrangian_proof(3, g=1)
        assert 'Lagrangian' in result['mechanism']
        assert result['shifted_symplectic_degree'] == 0

    def test_path3_uses_mc_equation(self):
        """Path 3 depends on the MC equation."""
        result = path3_shadow_depth_proof('heisenberg')
        assert 'MC equation' in result['mechanism']

    def test_path4_uses_theorems_ab(self):
        """Path 4 depends on Theorems A and B."""
        result = path4_barcobar_proof('heisenberg')
        assert 'Theorems A' in result['path'] or 'Thm B' in result['mechanism']

    def test_all_paths_give_same_conclusion(self):
        """All four paths agree for every standard family."""
        for fam in ['heisenberg', 'affine', 'betagamma', 'virasoro']:
            result = verify_kl_four_paths(fam, n=3, g=1)
            assert result['all_paths_agree'], \
                f"Paths disagree for {fam}"
