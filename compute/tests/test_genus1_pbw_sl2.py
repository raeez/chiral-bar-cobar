"""Tests for genus-1 PBW spectral sequence verification (MC1).

Verifies all claims in Theorem thm:pbw-genus1-km (higher_genus.tex:8517):
PBW degeneration for affine KM algebras at genus 1.

Ground truth: the enrichment from H^1(E_tau) at each weight is killed
by the combination of:
  (a) Whitehead vanishing (non-trivial g-modules)

.. note:: Marked slow — heavy symbolic computation.  Run via ``make test-full``.
  (b) Level-k Killing contraction (invariant part)

Tests organized by claim number matching the computation module.
"""

import pytest

pytestmark = pytest.mark.slow

from sympy import Rational, Matrix

from compute.lib.genus1_pbw_sl2 import (
    CASIMIR_EXACT_CUTOFF,
    CASIMIR_MODULAR_PRIMES,
    CASIMIR_MODULAR_STRATEGY,
    DIM_SL2,
    lie_bracket,
    killing,
    bracket_on_tensor_square,
    bracket_d1_on_tensor_power,
    bracket_d1_rank_on_tensor_power,
    bracket_d1_kernel_dim_on_tensor_power,
    d1_equivariance_residual_on_tensor_power,
    d1_is_equivariant_on_tensor_power,
    casimir_d1_commutator_on_tensor_power,
    killing_form_element,
    structure_constant_invariant_tensor_cube,
    adjoint_casimir_on_tensor_square,
    adjoint_casimir_on_tensor_power,
    casimir_method_for_tensor_power,
    casimir_modular_strategy_for_tensor_power,
    casimir_eigenspace_multiplicities_exact_sparse_on_tensor_power,
    casimir_eigenspace_multiplicities_modular_on_tensor_power,
    casimir_eigenspace_multiplicities_modular_weight_block_on_tensor_power,
    casimir_eigenspace_multiplicities_on_tensor_power,
    expected_casimir_eigenspace_multiplicities_on_tensor_power,
    staged_frontier_diagnostics_on_tensor_power,
    sl2_spin1_tensor_power_copy_multiplicities,
    invariant_subspace_dimension_on_tensor_power,
    ce_differential_1_to_2,
    ce_differential_2_to_3,
    verify_enrichment_claims,
    verify_ce_complex,
)


# ---------------------------------------------------------------------------
# sl2 structure constants
# ---------------------------------------------------------------------------

class TestSL2StructureConstants:
    """Verify sl2 bracket and Killing form data."""

    def test_bracket_ef(self):
        assert lie_bracket(0, 2) == {1: Rational(1)}   # [e, f] = h

    def test_bracket_fe(self):
        assert lie_bracket(2, 0) == {1: Rational(-1)}  # [f, e] = -h

    def test_bracket_he(self):
        assert lie_bracket(1, 0) == {0: Rational(2)}   # [h, e] = 2e

    def test_bracket_hf(self):
        assert lie_bracket(1, 2) == {2: Rational(-2)}  # [h, f] = -2f

    def test_bracket_ee_vanishes(self):
        assert lie_bracket(0, 0) == {}

    def test_bracket_hh_vanishes(self):
        assert lie_bracket(1, 1) == {}

    def test_bracket_ff_vanishes(self):
        assert lie_bracket(2, 2) == {}

    def test_killing_ef(self):
        assert killing(0, 2) == Rational(1)

    def test_killing_hh(self):
        assert killing(1, 1) == Rational(2)

    def test_killing_ee_vanishes(self):
        assert killing(0, 0) == Rational(0)

    def test_jacobi_identity(self):
        """Verify [[e_a, e_b], e_c] + cyclic = 0 for all triples."""
        d = DIM_SL2
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    # [[a,b],c]
                    total = [Rational(0)] * d
                    for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)]:
                        ab = lie_bracket(x, y)
                        for m, coeff1 in ab.items():
                            mc = lie_bracket(m, z)
                            for n, coeff2 in mc.items():
                                total[n] += coeff1 * coeff2
                    assert all(t == 0 for t in total), \
                        f"Jacobi fails for ({a},{b},{c}): {total}"


# ---------------------------------------------------------------------------
# Enrichment differential d_1 (Claims 1-5)
# ---------------------------------------------------------------------------

class TestEnrichmentD1:
    """Verify d_1: g^{otimes 2} -> g (Lie bracket map)."""

    def test_d1_shape(self):
        D = bracket_on_tensor_square()
        assert D.shape == (3, 9)

    def test_d1_rank_3(self):
        """Claim (1): d_1 is surjective (rank 3)."""
        D = bracket_on_tensor_square()
        assert D.rank() == 3

    def test_kernel_dim_6(self):
        """Claim (2): ker(d_1) has dimension 6."""
        D = bracket_on_tensor_square()
        assert 9 - D.rank() == 6

    def test_antisymmetric_isomorphism(self):
        """Claim (3): d_1 restricted to Lambda^2(g) = V_3 is an isomorphism."""
        D = bracket_on_tensor_square()
        d = DIM_SL2
        # Build antisymmetric basis vectors
        antisym_cols = []
        for a in range(d):
            for b in range(a + 1, d):
                v = Matrix([Rational(0)] * d**2)
                v[a * d + b] = Rational(1)
                v[b * d + a] = Rational(-1)
                antisym_cols.append(v)
        D_antisym = D * Matrix([list(v) for v in antisym_cols]).T
        assert D_antisym.rank() == 3


class TestKillingFormInvariant:
    """Verify claims about the Killing form element kappa^{ab}."""

    def test_killing_element_correct(self):
        """kappa = e tensor f + f tensor e + (1/2) h tensor h."""
        kappa = killing_form_element()
        # e tensor f = index 0*3+2 = 2
        assert kappa[2] == Rational(1)
        # f tensor e = index 2*3+0 = 6
        assert kappa[6] == Rational(1)
        # h tensor h = index 1*3+1 = 4
        assert kappa[4] == Rational(1, 2)
        # All others zero
        for i in [0, 1, 3, 5, 7, 8]:
            assert kappa[i] == Rational(0)

    def test_kappa_in_kernel(self):
        """Claim (4): kappa lies in ker(d_1)."""
        D = bracket_on_tensor_square()
        kappa = killing_form_element()
        result = D * kappa
        assert result.is_zero_matrix

    def test_kappa_is_invariant(self):
        """kappa is g-invariant (Casimir eigenvalue 0)."""
        C2 = adjoint_casimir_on_tensor_square()
        kappa = killing_form_element()
        assert (C2 * kappa).is_zero_matrix

    def test_killing_contraction_nonzero(self):
        """Claim (5): kappa^{ab} kappa_{ab} = dim(g) = 3 (nonzero)."""
        # This is the scalar that d_2 produces
        inv_killing = {
            (0, 2): Rational(1),
            (2, 0): Rational(1),
            (1, 1): Rational(1, 2),
        }
        contraction = sum(
            coeff * killing(a, b)
            for (a, b), coeff in inv_killing.items()
        )
        assert contraction == Rational(3)  # = dim(sl2)

    def test_symmetry_argument(self):
        """Verify kappa^{ab} f^c_{ab} = 0 (why kappa survives d_1).

        This is the key identity: the Killing form contracted with
        structure constants vanishes by symmetry vs antisymmetry.
        """
        inv_killing = {
            (0, 2): Rational(1),
            (2, 0): Rational(1),
            (1, 1): Rational(1, 2),
        }
        d = DIM_SL2
        for c in range(d):
            total = Rational(0)
            for (a, b), coeff in inv_killing.items():
                bracket = lie_bracket(a, b)
                total += coeff * bracket.get(c, Rational(0))
            assert total == 0, f"kappa^ab f^{c}_ab = {total} != 0"


# ---------------------------------------------------------------------------
# Casimir decomposition of g tensor g
# ---------------------------------------------------------------------------

class TestCasimirDecomposition:
    """Verify g tensor g = V_5 + V_3 + V_1 via Casimir eigenvalues."""

    def test_casimir_eigenvalues(self):
        """Eigenvalues should be {12: 5, 4: 3, 0: 1}.

        With our Killing form normalization (kappa(h,h)=2),
        the Casimir eigenvalue on spin-j rep is 2j(j+1).
        """
        C2 = adjoint_casimir_on_tensor_square()
        eigenvals = C2.eigenvals()
        assert eigenvals == {
            Rational(12): 5,  # V_5 (spin 2): 2*2*3 = 12
            Rational(4): 3,   # V_3 (spin 1): 2*1*2 = 4
            Rational(0): 1,   # V_1 (spin 0): 0
        }

    def test_dimension_sum(self):
        """5 + 3 + 1 = 9 = dim(g tensor g)."""
        C2 = adjoint_casimir_on_tensor_square()
        eigenvals = C2.eigenvals()
        total = sum(eigenvals.values())
        assert total == 9

    def test_tensor_power_helpers_at_degree_2(self):
        """Generic tensor-power diagnostics match the degree-2 specialization."""
        assert casimir_eigenspace_multiplicities_on_tensor_power(2) == {
            Rational(12): 5,
            Rational(4): 3,
            Rational(0): 1,
        }
        assert bracket_d1_rank_on_tensor_power(2) == 3
        assert bracket_d1_kernel_dim_on_tensor_power(2) == 6

    def test_rep_theoretic_copy_multiplicities(self):
        """(V_3)^{otimes n} multiplicities for n=1..6."""
        assert sl2_spin1_tensor_power_copy_multiplicities(1) == {1: 1}
        assert sl2_spin1_tensor_power_copy_multiplicities(2) == {2: 1, 1: 1, 0: 1}
        assert sl2_spin1_tensor_power_copy_multiplicities(3) == {3: 1, 2: 2, 1: 3, 0: 1}
        assert sl2_spin1_tensor_power_copy_multiplicities(4) == {4: 1, 3: 3, 2: 6, 1: 6, 0: 3}
        assert sl2_spin1_tensor_power_copy_multiplicities(5) == {
            5: 1, 4: 4, 3: 10, 2: 15, 1: 15, 0: 6
        }
        assert sl2_spin1_tensor_power_copy_multiplicities(6) == {
            6: 1, 5: 5, 4: 15, 3: 29, 2: 40, 1: 36, 0: 15
        }

    def test_expected_vs_computed_casimir_multiplicities(self):
        """Computed Casimir eigenspaces agree with representation-theoretic expectations."""
        for power in range(1, 6):
            assert casimir_eigenspace_multiplicities_on_tensor_power(power) == \
                expected_casimir_eigenspace_multiplicities_on_tensor_power(power)

    def test_invariant_dimensions(self):
        """Dimensions of sl2-invariants in tensor powers through n=6."""
        assert invariant_subspace_dimension_on_tensor_power(1) == 0
        assert invariant_subspace_dimension_on_tensor_power(2) == 1
        assert invariant_subspace_dimension_on_tensor_power(3) == 1
        assert invariant_subspace_dimension_on_tensor_power(4) == 3
        assert invariant_subspace_dimension_on_tensor_power(5) == 6
        assert invariant_subspace_dimension_on_tensor_power(6) == 15

    def test_tensor_power_helpers_at_degree_5(self):
        """Explicit n=5 regression point for the generalized MC1 diagnostics."""
        assert casimir_eigenspace_multiplicities_on_tensor_power(5) == {
            Rational(60): 11,
            Rational(40): 36,
            Rational(24): 70,
            Rational(12): 75,
            Rational(4): 45,
            Rational(0): 6,
        }
        assert bracket_d1_rank_on_tensor_power(5) == 80
        assert bracket_d1_kernel_dim_on_tensor_power(5) == 163

    def test_tensor_power_helpers_at_degree_6(self):
        """Explicit n=6 regression point plus first performance-frontier checkpoint."""
        assert casimir_eigenspace_multiplicities_on_tensor_power(6) == {
            Rational(84): 13,
            Rational(60): 55,
            Rational(40): 135,
            Rational(24): 203,
            Rational(12): 200,
            Rational(4): 108,
            Rational(0): 15,
        }
        assert bracket_d1_rank_on_tensor_power(6) == 243
        assert bracket_d1_kernel_dim_on_tensor_power(6) == 486

    def test_casimir_auto_policy_switches_after_cutoff(self):
        """Default policy: exact through n<=6, modular path for n>=7."""
        assert CASIMIR_EXACT_CUTOFF == 6
        assert CASIMIR_MODULAR_STRATEGY == "auto"
        assert casimir_method_for_tensor_power(6) == "exact"
        assert casimir_method_for_tensor_power(7) == "modular"
        assert casimir_modular_strategy_for_tensor_power(6) == "global"
        assert casimir_modular_strategy_for_tensor_power(7) == "weight_block"

    def test_tensor_power_helpers_at_degree_7_staged_frontier(self):
        """n=7 uses the fast Casimir path by default; exact remains opt-in."""
        auto_vals = casimir_eigenspace_multiplicities_on_tensor_power(7)
        theory_vals = expected_casimir_eigenspace_multiplicities_on_tensor_power(7)
        assert auto_vals == theory_vals
        assert auto_vals == {
            Rational(112): 15,
            Rational(84): 78,
            Rational(60): 231,
            Rational(40): 441,
            Rational(24): 588,
            Rational(12): 525,
            Rational(4): 273,
            Rational(0): 36,
        }

    def test_casimir_method_validation(self):
        with pytest.raises(ValueError):
            casimir_method_for_tensor_power(3, method="unsupported")

    def test_exact_sparse_method_resolution(self):
        assert casimir_method_for_tensor_power(3, method="exact_sparse") == "exact_sparse"

    def test_exact_sparse_matches_exact_on_small_power(self):
        exact = casimir_eigenspace_multiplicities_on_tensor_power(5, method="exact")
        exact_sparse = casimir_eigenspace_multiplicities_on_tensor_power(5, method="exact_sparse")
        assert exact_sparse == exact

    def test_exact_sparse_function_matches_expected(self):
        exact_sparse = casimir_eigenspace_multiplicities_exact_sparse_on_tensor_power(4)
        assert exact_sparse == expected_casimir_eigenspace_multiplicities_on_tensor_power(4)

    def test_modular_path_matches_exact_on_small_power(self):
        """Modular nullity extraction agrees with exact eigenspaces on small powers."""
        exact = casimir_eigenspace_multiplicities_on_tensor_power(4, method="exact")
        modular = casimir_eigenspace_multiplicities_on_tensor_power(4, method="modular")
        assert modular == exact

    def test_modular_weight_block_matches_exact_on_small_power(self):
        """Weight-block modular extraction agrees with exact eigenspaces."""
        exact = casimir_eigenspace_multiplicities_on_tensor_power(4, method="exact")
        modular_weight_block = casimir_eigenspace_multiplicities_modular_weight_block_on_tensor_power(
            4,
            primes=CASIMIR_MODULAR_PRIMES,
        )
        assert modular_weight_block == exact

    def test_modular_path_at_degree_7(self):
        """Modular n=7 path recovers the full expected eigenspace multiplicities."""
        modular = casimir_eigenspace_multiplicities_modular_on_tensor_power(
            7,
            primes=CASIMIR_MODULAR_PRIMES,
        )
        modular_weight_block = casimir_eigenspace_multiplicities_modular_weight_block_on_tensor_power(
            7,
            primes=CASIMIR_MODULAR_PRIMES,
        )
        assert modular_weight_block == modular
        assert modular == {
            Rational(112): 15,
            Rational(84): 78,
            Rational(60): 231,
            Rational(40): 441,
            Rational(24): 588,
            Rational(12): 525,
            Rational(4): 273,
            Rational(0): 36,
        }

    def test_staged_frontier_report_n7_without_casimir(self):
        """n=7 staged report supports lightweight frontier checks without eigenspaces."""
        report = staged_frontier_diagnostics_on_tensor_power(7, include_casimir=False)
        assert report["power"] == 7
        assert report["rank_d1"] == 728
        assert report["kernel_dim_d1"] == 1459
        assert report["invariant_dim"] == 36
        assert report["equivariant"] is True
        assert report["casimir_commutator_zero"] is True
        assert report["casimir_mode"] == "modular"
        assert report["casimir_modular_strategy"] == "weight_block"
        assert report["casimir_eigenspaces"] is None
        assert report["casimir_matches_expected"] is None
        assert report["all_enabled_checks_pass"] is True

    def test_staged_frontier_report_small_power_with_casimir(self):
        """Full staged report agrees with expected eigenspaces on small powers."""
        report = staged_frontier_diagnostics_on_tensor_power(4, include_timings=True)
        assert report["power"] == 4
        assert report["rank_d1"] == 27
        assert report["kernel_dim_d1"] == 54
        assert report["invariant_dim"] == 3
        assert report["equivariant"] is True
        assert report["casimir_commutator_zero"] is True
        assert report["casimir_mode"] == "exact"
        assert report["casimir_eigenspaces"] == {
            Rational(40): 9,
            Rational(24): 21,
            Rational(12): 30,
            Rational(4): 18,
            Rational(0): 3,
        }
        assert report["casimir_matches_expected"] is True
        assert report["all_enabled_checks_pass"] is True
        assert report["timings"]["total"] >= 0


class TestD1Equivariance:
    """PBW d_1 is a morphism of sl2-modules across tensor powers."""

    def test_d1_is_equivariant(self):
        for power in range(2, 7):
            assert d1_is_equivariant_on_tensor_power(power)

    def test_d1_equivariance_residual_zero(self):
        for power in range(2, 7):
            for x_idx in range(DIM_SL2):
                residual = d1_equivariance_residual_on_tensor_power(power, x_idx)
                assert residual.is_zero_matrix

    def test_d1_commutes_with_casimir(self):
        for power in range(2, 7):
            comm = casimir_d1_commutator_on_tensor_power(power)
            assert comm.is_zero_matrix


# ---------------------------------------------------------------------------
# Chevalley-Eilenberg complex (Claims 6-8)
# ---------------------------------------------------------------------------

class TestCEComplex:
    """Verify CE complex of sl2: H*(sl2) = k[0] + k[3]."""

    def test_d1_rank_3(self):
        """Claim (6): d_CE^1 is injective (rank 3)."""
        d1 = ce_differential_1_to_2()
        assert d1.shape == (3, 3)
        assert d1.rank() == 3

    def test_d2_is_zero(self):
        """Claim (7): d_CE^2 = 0."""
        d2 = ce_differential_2_to_3()
        assert d2.shape == (1, 3)
        assert d2.rank() == 0

    def test_d_squared_zero(self):
        """d^2 = 0 in the CE complex."""
        d1 = ce_differential_1_to_2()
        d2 = ce_differential_2_to_3()
        assert (d2 * d1).is_zero_matrix

    def test_cohomology(self):
        """Claim (8): H*(sl2) = (1, 0, 0, 1)."""
        d1 = ce_differential_1_to_2()
        d2 = ce_differential_2_to_3()

        h0 = 1  # H^0 = k
        h1 = 3 - d1.rank()  # ker(d1) - im(d0=0) = 0
        h2 = (3 - d2.rank()) - d1.rank()  # ker(d2)/im(d1) = 0
        h3 = 1 - d2.rank()  # coker(d2) = 1

        assert (h0, h1, h2, h3) == (1, 0, 0, 1)

    def test_poincare_polynomial(self):
        """Poincare polynomial is 1 + t^3."""
        ce = verify_ce_complex()
        assert ce["total_betti"] == 2
        assert ce["H0"] == 1
        assert ce["H3"] == 1


# ---------------------------------------------------------------------------
# Full MC1 verification bundle
# ---------------------------------------------------------------------------

class TestMC1FullVerification:
    """Run the complete MC1 verification and check all claims pass."""

    def test_all_enrichment_claims(self):
        results = verify_enrichment_claims()
        assert results["claim_1_surjective"]
        assert results["claim_2_ker_dim_6"]
        assert results["claim_3_V3_isomorphism"]
        assert results["claim_4_kappa_in_ker"]
        assert results["claim_5_d2_nonzero"]
        assert results["claim_adjoint_decomposition"]
        assert results["claim_kappa_is_invariant"]

    def test_all_ce_claims(self):
        results = verify_ce_complex()
        assert results["claim_6_d1_rank_3"]
        assert results["claim_7_d2_is_zero"]
        assert results["d_squared_zero"]
        assert results["claim_8_cohomology"]


# ---------------------------------------------------------------------------
# Weight h=3: g^{otimes 3} enrichment (higher weight check)
# ---------------------------------------------------------------------------

class TestWeightH3Enrichment:
    """Verify enrichment killing at conformal weight h=3, bar degree 3.

    At bar degree 3, the enrichment involves g^{otimes 3} = sl2^{otimes 3}.
    The d_1 differential acts by bracketing adjacent pairs.
    We verify the same Whitehead + Killing mechanism works.

    g^{otimes 3} decomposes under diagonal adjoint action as:
    (V_5 + V_3 + V_1) tensor V_3 = V_7 + 2*V_5 + 2*V_3 + V_1
    Total dim = 7 + 10 + 6 + 1 = ... wait, multiplicities:
    V_7(dim 7) + V_5(dim 5)*2 + V_3(dim 3)*2 + V_1(dim 1) = 7+10+6+1 = 24
    But g^{otimes 3} has dim 27. Need to recompute.

    Actually: V_3 tensor V_3 tensor V_3:
    Step 1: V_3 tensor V_3 = V_5 + V_3 + V_1
    Step 2: (V_5 + V_3 + V_1) tensor V_3:
      V_5 tensor V_3 = V_7 + V_5 + V_3
      V_3 tensor V_3 = V_5 + V_3 + V_1
      V_1 tensor V_3 = V_3
    Total: V_7 + 2*V_5 + 3*V_3 + V_1
    Dims: 7 + 10 + 9 + 1 = 27. Correct.

    Invariant part: V_1 has dim 1.
    """

    def test_triple_tensor_decomposition(self):
        """g^{otimes 3} = V_7 + 2*V_5 + 3*V_3 + V_1."""
        eigenvals = casimir_eigenspace_multiplicities_on_tensor_power(3)

        # With normalization 2j(j+1):
        # V_7 (spin 3): 2*3*4 = 24, dim 7
        # V_5 (spin 2): 2*2*3 = 12, dim 5, mult 2 => 10
        # V_3 (spin 1): 2*1*2 = 4, dim 3, mult 3 => 9
        # V_1 (spin 0): 0, dim 1, mult 1
        expected = {
            Rational(24): 7,   # V_7
            Rational(12): 10,  # 2 * V_5
            Rational(4): 9,    # 3 * V_3
            Rational(0): 1,    # V_1
        }
        assert eigenvals == expected

    def test_invariant_subspace_dim_1(self):
        """The g-invariant subspace of g^{otimes 3} is 1-dimensional."""
        eigenvals = casimir_eigenspace_multiplicities_on_tensor_power(3)
        assert eigenvals.get(Rational(0), 0) == 1

    def test_d1_bracket_on_triple(self):
        """d_1: g^{otimes 3} -> g^{otimes 2} (bracket adjacent pairs).

        d_1(a tensor b tensor c) = [a,b] tensor c + (-1) a tensor [b,c]

        Non-trivial reps in g^{otimes 3} map to non-trivial reps in g^{otimes 2},
        and Whitehead kills them at E_2.
        """
        mat = bracket_d1_on_tensor_power(3)
        assert mat.shape == (9, 27)
        # d_1 should have nontrivial rank
        rank = mat.rank()
        assert rank > 0
        # ker(d_1) should contain the invariant (V_1) but not exhaust g^{otimes 3}
        ker_dim = 27 - rank
        assert ker_dim >= 1  # at least V_1 survives

    def test_triple_killing_invariant_in_kernel(self):
        """The unique invariant in g^{otimes 3} is f_{abc} (structure constants
        contracted with Killing form), and it lies in ker(d_1).

        For sl2, f_{abc} = kappa_{ad} f^d_{bc} is totally antisymmetric.
        """
        f_tensor = structure_constant_invariant_tensor_cube()

        # f_tensor should be nonzero
        assert not f_tensor.is_zero_matrix

        # Build d_1
        mat = bracket_d1_on_tensor_power(3)

        # f_{abc} should be in ker(d_1)
        result = mat * f_tensor
        assert result.is_zero_matrix

    def test_triple_killing_is_invariant(self):
        """f_{abc} is g-invariant (lives in V_1)."""
        C2 = adjoint_casimir_on_tensor_power(3)
        f_tensor = structure_constant_invariant_tensor_cube()

        # C_2(f_{abc}) = 0
        assert (C2 * f_tensor).is_zero_matrix
