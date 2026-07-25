"""Regression tests for the ordered-to-symmetric averaging audit.

The tests keep three surfaces separate:

* exact linear invariant/coinvariant splitting, including ``qR=q``;
* compatibility criteria for brackets, differentials, and coproducts;
* independent representation-theoretic ranks and finite Casimir formulas.

Equivariance and closure of the invariant image are tested as their own
statements.  Bracket preservation is tested by its actual morphism equation
and by the kernel-ideal criterion.
"""

import math
from fractions import Fraction

import numpy as np
import pytest
from numpy import linalg as la

from compute.lib.e1_primacy_theorem_engine import (
    E1PrimacyTheorem,
    SplittingAnalysis,
    all_permutations,
    casimir_sl2,
    convolution_bracket_descent_surface,
    descent_count,
    dim_end_sn_invariant_formula,
    eulerian_idempotent_matrix,
    eulerian_number,
    exact_deconcatenation_surface,
    exact_reynolds_coinvariant_surface,
    exact_reynolds_lie_surface,
    information_loss_arity2,
    information_loss_arity_n,
    is_sn_invariant,
    kernel_contains_antisymmetric,
    kernel_dimension,
    kernel_projection,
    kappa_from_r_matrix_heisenberg,
    kappa_from_r_matrix_sl2,
    permutation_matrix,
    quantum_group_data_in_kernel,
    reynolds_complement_in_kernel,
    reynolds_operator,
    r_matrix_minus_kappa_in_kernel,
    sgn,
    transported_concatenation_surface,
    verify_av_commutes_with_differential,
    verify_av_preserves_bracket,
    verify_av_preserves_bracket_equivariant,
    verify_cybe_fails_for_casimir,
    verify_dim_formula_against_computation,
    verify_kappa_recovery_heisenberg,
    verify_kappa_recovery_sl2,
    verify_mc_projection_arity2,
    verify_surjectivity,
)


class TestSymmetricGroupMachinery:
    def test_permutation_representation_and_sign(self):
        swap = permutation_matrix((1, 0), 2)
        assert np.allclose(swap @ swap, np.eye(4))
        assert sgn((1, 0)) == -1
        assert sgn((0, 1)) == 1
        assert len(all_permutations(3)) == math.factorial(3)

    def test_descent_count(self):
        assert descent_count((0, 1, 2)) == 0
        assert descent_count((2, 1, 0)) == 2
        assert descent_count((1, 0, 2)) == 1


class TestLinearReynoldsSurface:
    def test_reynolds_is_projection(self):
        for n, dim in [(2, 2), (2, 3), (3, 2)]:
            rng = np.random.default_rng(42 + 10 * n + dim)
            size = dim**n
            matrix = rng.normal(size=(size, size))
            averaged = reynolds_operator(matrix, n, dim)
            assert la.norm(reynolds_operator(averaged, n, dim) - averaged) < 1e-10

    def test_reynolds_image_is_invariant(self):
        rng = np.random.default_rng(137)
        for n in (2, 3):
            size = 2**n
            matrix = rng.normal(size=(size, size))
            assert is_sn_invariant(reynolds_operator(matrix, n, 2), n, 2)

    @pytest.mark.parametrize("dim,n", [(2, 2), (2, 3), (3, 2)])
    def test_exact_coinvariant_identity(self, dim, n):
        surface = exact_reynolds_coinvariant_surface(dim, n)
        assert surface['idempotent'] is True
        assert surface['quotient_after_reynolds_equals_quotient'] is True
        assert surface['invariant_dimension'] == surface['expected_symmetric_dimension']
        assert surface['status'] == 'PROVED_EXACT_FINITE_MODEL'

    @pytest.mark.parametrize(
        "n,dim,expected",
        [(2, 2, 10), (2, 3, 45), (3, 2, 20)],
    )
    def test_surjectivity_onto_invariant_image(self, n, dim, expected):
        surjective, image_dimension, total_dimension = verify_surjectivity(n, dim)
        assert surjective
        assert image_dimension == expected
        assert total_dimension == dim ** (2 * n)

    def test_schur_weyl_formulas_match_superoperator_ranks(self):
        for n, dimensions in [(2, (2, 3, 4)), (3, (2, 3))]:
            for dim in dimensions:
                assert verify_dim_formula_against_computation(n, dim)
                assert dim_end_sn_invariant_formula(n, dim) > 0


class TestBracketCompatibilitySurface:
    def test_commutator_action_is_equivariant(self):
        for n in (2, 3):
            rng = np.random.default_rng(200 + n)
            size = 2**n
            left = rng.normal(size=(size, size))
            right = rng.normal(size=(size, size))
            equivariant, error = verify_av_preserves_bracket_equivariant(
                n, 2, left, right
            )
            assert equivariant
            assert error < 1e-10

    def test_exact_equivariance_does_not_supply_lie_morphism(self):
        surface = exact_reynolds_lie_surface()
        assert surface['action_is_bracket_equivariant'] is True
        assert surface['reynolds_is_lie_morphism'] is False
        assert surface['kernel_is_lie_ideal'] is False
        assert surface['defect_norm'] > 0
        assert surface['status'] == 'REFUTED_BY_EXACT_COUNTEREXAMPLE'

    def test_tensor_swap_reynolds_has_explicit_commutator_defect(self):
        symmetric = np.array([0.0, 1.0, 1.0, 0.0])
        antisymmetric = np.array([0.0, 1.0, -1.0, 0.0])
        left = np.outer(symmetric, antisymmetric)
        right = np.outer(antisymmetric, symmetric)

        assert la.norm(reynolds_operator(left, 2, 2)) < 1e-10
        assert la.norm(reynolds_operator(right, 2, 2)) < 1e-10
        preserves, defect = verify_av_preserves_bracket(2, 2, 2, left, right)
        assert preserves is False
        assert defect > 1.0

    def test_convolution_bracket_requires_its_own_certificate(self):
        undecided = convolution_bracket_descent_surface()
        assert undecided['status'] == 'KERNEL_IDEAL_CERTIFICATE_REQUIRED'
        assert undecided['raw_reynolds_preserves_bracket'] is False

        refuted = convolution_bracket_descent_surface(kernel_is_lie_ideal=False)
        assert refuted['status'] == 'REFUTED_BY_KERNEL_IDEAL_FAILURE'

        certified = convolution_bracket_descent_surface(kernel_is_lie_ideal=True)
        assert certified['status'] == 'CERTIFIED_BY_KERNEL_IDEAL'
        assert certified['raw_reynolds_preserves_bracket'] is True

    def test_chain_map_test_requires_explicit_differential(self):
        matrix = np.arange(16, dtype=float).reshape(4, 4)
        with pytest.raises(ValueError, match="explicit differential"):
            verify_av_commutes_with_differential(2, 2, matrix, matrix)

        identity_differential = lambda value: value
        passed, error = verify_av_commutes_with_differential(
            2, 2, matrix, matrix, differential=identity_differential
        )
        assert passed
        assert error < 1e-10


class TestKernelAndCoalgebraSurface:
    @pytest.mark.parametrize(
        "n,dim,total,image,kernel",
        [(2, 2, 16, 10, 6), (2, 3, 81, 45, 36), (3, 2, 64, 20, 44)],
    )
    def test_kernel_dimensions(self, n, dim, total, image, kernel):
        assert kernel_dimension(n, dim) == (total, image, kernel)
        assert information_loss_arity_n(n, dim) == (total, image, kernel)

    def test_antisymmetric_elements_are_in_linear_kernel(self):
        assert kernel_contains_antisymmetric(2, 2)
        assert kernel_contains_antisymmetric(3, 2)

    def test_kernel_superoperator_is_projection_of_expected_rank(self):
        projection = kernel_projection(2, 2)
        assert la.norm(projection @ projection - projection) < 1e-10
        assert np.linalg.matrix_rank(projection, tol=1e-9) == 6

    def test_raw_deconcatenation_kernel_is_not_coideal(self):
        surface = exact_deconcatenation_surface()
        assert surface['quotient_of_kernel_vector_is_zero'] is True
        assert surface['reduced_deconcatenation_survives'] is True
        assert surface['kernel_is_coideal'] is False
        assert surface['status'] == 'RAW_DECONCATENATION_REQUIRES_REPLACEMENT'

    def test_concatenation_descends_and_fixed_points_use_transport(self):
        surface = transported_concatenation_surface(2, 2, 2)
        assert surface['concatenation_descends_to_coinvariants'] is True
        assert surface['fixed_point_operation'] == 'R_{p+q}(concatenate(x,y))'


class TestImplementedDescentProjections:
    def test_symmetrizer_and_binary_antisymmetrizer(self):
        symmetric = eulerian_idempotent_matrix(2, 0, 2)
        antisymmetric = eulerian_idempotent_matrix(2, 1, 2)
        identity = np.eye(4)
        assert la.norm(symmetric @ symmetric - symmetric) < 1e-10
        assert la.norm(antisymmetric @ antisymmetric - antisymmetric) < 1e-10
        assert la.norm(symmetric @ antisymmetric) < 1e-10
        assert la.norm(symmetric + antisymmetric - identity) < 1e-10

    def test_higher_eulerian_idempotents_are_explicitly_unimplemented(self):
        with pytest.raises(NotImplementedError, match="Solomon"):
            eulerian_idempotent_matrix(3, 1, 2)
        with pytest.raises(NotImplementedError, match="Solomon"):
            eulerian_idempotent_matrix(3, 2, 2)


class TestFiniteCasimirIdentities:
    def test_sl2_casimir_satisfies_infinitesimal_braid_relation(self):
        holds, error = verify_mc_projection_arity2(dim=2)
        assert holds
        assert error < 1e-10

    def test_sl2_casimir_has_nonzero_cybe_tensor(self):
        fails, norm = verify_cybe_fails_for_casimir(dim=2)
        assert fails
        assert norm > 0.5

    def test_casimir_is_swap_invariant(self):
        assert is_sn_invariant(casimir_sl2(), 2, 2)

    def test_reynolds_complement_lies_in_kernel(self):
        holds, error = reynolds_complement_in_kernel()
        assert holds
        assert error < 1e-10

        alias_holds, alias_error = r_matrix_minus_kappa_in_kernel()
        assert alias_holds
        assert alias_error < 1e-10


class TestScalarFormulasAndInformationDimensions:
    def test_heisenberg_formula(self):
        for level in (1, 2, 3, 5, 10):
            assert kappa_from_r_matrix_heisenberg(level) == level
            assert verify_kappa_recovery_heisenberg(level)

    def test_sl2_formula(self):
        for level in (1, 2, 3, 5):
            expected = Fraction(3 * (level + 2), 4)
            assert kappa_from_r_matrix_sl2(level) == expected
            holds, computed = verify_kappa_recovery_sl2(level)
            assert holds
            assert computed == expected

    def test_information_loss_dimensions(self):
        fractions = []
        for dim in (2, 3, 4, 5):
            total, image, kernel = information_loss_arity2(dim)
            assert total == image + kernel
            fractions.append(kernel / total)
        assert fractions == sorted(fractions)

    def test_dimension_count_does_not_classify_quantum_group_data(self):
        data = quantum_group_data_in_kernel(dim=2)
        assert data['arity_2_total_dim'] == 16
        assert data['arity_2_image_dim'] == 10
        assert data['arity_2_kernel_dim'] == 6
        assert data['casimir_kernel_norm'] < 1e-10
        assert data['quantum_group_classification_proved'] is False
        assert data['classification_status'] == 'MAP_FROM_DEFORMATION_DATA_REQUIRED'


class TestSplittingStatus:
    def test_linear_section_and_invariant_subalgebra(self):
        analysis = SplittingAnalysis(2, 2)
        assert analysis.linear_section_exists()

        rng = np.random.default_rng(88)
        left = reynolds_operator(rng.normal(size=(4, 4)), 2, 2)
        right = reynolds_operator(rng.normal(size=(4, 4)), 2, 2)
        assert np.array_equal(analysis.linear_section(left), left)
        assert is_sn_invariant(left @ right - right @ left, 2, 2)

    def test_raw_sequence_has_no_lie_extension_status(self):
        analysis = SplittingAnalysis(2, 2)
        status = analysis.extension_status()
        assert status['linear_section_exists'] is True
        assert status['invariant_image_is_lie_subalgebra'] is True
        assert status['raw_reynolds_is_lie_morphism'] is False
        assert status['kernel_is_lie_ideal'] is False
        assert status['lie_extension_defined'] is False
        assert status['dg_lie_extension_defined'] is False
        assert status['drinfeld_obstruction_status'] == (
            'UNVERIFIED_WITHOUT_DG_LIE_EXTENSION'
        )
        assert analysis.differential_obstruction().startswith(
            'UNDEFINED_AS_DG_LIE_EXTENSION'
        )

    def test_trivial_action_has_zero_linear_kernel(self):
        analysis = SplittingAnalysis(3, 1)
        status = analysis.extension_status()
        assert analysis.kernel_dimension() == 0
        assert status['raw_reynolds_is_lie_morphism'] is True
        assert status['kernel_is_lie_ideal'] is True
        assert status['lie_extension_defined'] is True
        assert status['dg_lie_extension_defined'] is False
        assert status['lie_status'] == 'TRIVIAL_ACTION_CERTIFICATE'


class TestTypedMasterAudit:
    def test_full_audit_reports_proofs_and_obligations_separately(self):
        audit = E1PrimacyTheorem(dim=2, max_arity=3).full_verification()

        linear = audit['linear_and_lie_surface']
        assert linear['av_is_projection_n2'] is True
        assert linear['av_image_invariant_n3'] is True
        assert linear['commutator_action_equivariant'] is True
        assert linear['raw_reynolds_is_lie_morphism'] is False
        assert linear['kernel_is_lie_ideal'] is False
        assert linear['chain_map_status'] == 'EXPLICIT_DIFFERENTIAL_REQUIRED'
        assert linear['dg_lie_morphism_proved'] is False

        surjectivity = audit['linear_surjectivity']
        assert all(surjectivity.values())

        mc_surface = audit['finite_identity_and_mc_surface']
        assert mc_surface['sl2_infinitesimal_braid_identity'] is True
        assert mc_surface['general_mc_projection_proved'] is False

        extension = audit['extension_surface']
        assert extension['lie_extension_defined'] is False
        assert extension['drinfeld_obstruction_status'] == (
            'UNVERIFIED_WITHOUT_DG_LIE_EXTENSION'
        )


class TestEulerianNumbers:
    @pytest.mark.parametrize(
        "n,row",
        [
            (2, [1, 1]),
            (3, [1, 4, 1]),
            (4, [1, 11, 11, 1]),
        ],
    )
    def test_known_rows(self, n, row):
        assert [eulerian_number(n, k) for k in range(n)] == row

    def test_row_sums(self):
        for n in range(1, 7):
            assert sum(eulerian_number(n, k) for k in range(n)) == math.factorial(n)
