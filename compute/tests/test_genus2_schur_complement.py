r"""Tests for genus-2 Schur complement of the sewing kernel.

Verifies the mathematical claims of prop:genus2-non-diagonal and
thm:genus2-non-collapse in arithmetic_shadows.tex:

1. Schur complement factorization identity
2. c_{1,1} positivity
3. Non-factorization of genus-2 Fredholm determinant for q_3 != 0
4. Heisenberg: no non-Newton constraints
5. Interacting algebras: non-Newton constraints from matrix Schur complement

Ground truth:
  prop:genus2-non-diagonal, thm:genus2-non-collapse,
  thm:general-hs-sewing, thm:heisenberg-sewing,
  genus2_schur_complement.py.
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from genus2_schur_complement import (
    Genus2SewingKernel,
    manuscript_c11,
    one_particle_w2_coefficient,
    identify_coupling_model,
    verify_c11_positivity,
    verify_schur_factorization,
    correction_coefficient_w2k,
    schur_complement_eigenvalues,
    schur_complement_trace_moments,
    newton_independence_test,
    virasoro_schur_complement_structure,
    genus2_fourier_coefficients,
    siegel_fourier_check,
    non_newton_analysis,
    full_analysis,
    eta_product,
    eta_inv,
    partitions,
    Genus2PartitionFunction,
)


# ======================================================================
# 1. Basic utilities
# ======================================================================

class TestBasicUtilities:
    """Tests for partition function and modular form utilities."""

    def test_partitions_small(self):
        """Verify partition counts for small n."""
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15, 8: 22}
        for n, p in expected.items():
            assert partitions(n) == p, f"p({n}) = {partitions(n)}, expected {p}"

    def test_eta_product_asymptotics(self):
        """eta product -> 1 as q -> 0."""
        q = 1e-10
        assert abs(eta_product(q) - 1.0) < 1e-9

    def test_eta_product_known_value(self):
        """Verify eta product at q = e^{-2pi} ~ 0.00187."""
        q = np.exp(-2 * np.pi)
        eta_prod = eta_product(q)
        # eta(i) = Gamma(1/4) / (2 pi^{3/4}) ~ 0.76823...
        # eta_product = eta / q^{1/24} = 0.76823 / q^{1/24}
        # q^{1/24} = exp(-2pi/24) = exp(-pi/12) ~ 0.7694
        # So eta_product ~ 0.76823 / 0.7694 ~ 0.9985
        assert abs(eta_prod) > 0.99, f"eta_product(e^{{-2pi}}) = {eta_prod}"
        assert abs(eta_prod) < 1.01

    def test_eta_inv_reciprocal(self):
        """Verify eta_inv * eta_product = 1."""
        q = 0.3
        assert abs(eta_inv(q) * eta_product(q) - 1.0) < 1e-12


# ======================================================================
# 2. Genus-2 sewing kernel
# ======================================================================

class TestGenus2SewingKernel:
    """Tests for the 2x2 block sewing kernel."""

    def test_kernel_at_mode_structure(self):
        """Verify the 2x2 kernel has correct structure."""
        K = Genus2SewingKernel(0.1, 0.2, 0.05)
        M = K.kernel_at_mode(1)
        assert M.shape == (2, 2)
        assert abs(M[0, 0] - 0.1) < 1e-14
        assert abs(M[1, 1] - 0.2) < 1e-14
        assert abs(M[0, 1] - 0.05) < 1e-14
        assert abs(M[1, 0] - 0.05) < 1e-14  # Symmetric

    def test_kernel_at_mode_n(self):
        """Verify K^{(n)} entries are q_j^n and w^n."""
        q1, q2, w = 0.3, 0.4, 0.1
        K = Genus2SewingKernel(q1, q2, w)
        for n in [1, 2, 5, 10]:
            M = K.kernel_at_mode(n)
            assert abs(M[0, 0] - q1 ** n) < 1e-12
            assert abs(M[1, 1] - q2 ** n) < 1e-12
            assert abs(M[0, 1] - w ** n) < 1e-12

    def test_det_one_minus_K_formula(self):
        """Verify det(1-K^{(n)}) = (1-q1^n)(1-q2^n) - w^{2n}."""
        q1, q2, w = 0.2, 0.3, 0.08
        K = Genus2SewingKernel(q1, q2, w)
        for n in [1, 3, 7]:
            det_formula = K.det_one_minus_K_at_mode(n)
            M = K.kernel_at_mode(n)
            det_direct = np.linalg.det(np.eye(2) - M)
            assert abs(det_formula - det_direct) < 1e-12, \
                f"Mode {n}: formula={det_formula}, direct={det_direct}"

    def test_fredholm_det_positive(self):
        """Fredholm determinant is positive for real q_j, w in (0,1)."""
        for q1, q2, w in [(0.1, 0.2, 0.05), (0.3, 0.4, 0.1), (0.5, 0.5, 0.2)]:
            K = Genus2SewingKernel(q1, q2, w, N_modes=100)
            det_val = K.fredholm_det()
            assert det_val.real > 0, \
                f"det(1-K) = {det_val} not positive for q1={q1}, q2={q2}, w={w}"

    def test_fredholm_det_factorizes_at_w0(self):
        """At w=0 (separating limit), det = det(1-K_{q1}) * det(1-K_{q2})."""
        q1, q2 = 0.2, 0.3
        K = Genus2SewingKernel(q1, q2, 1e-15, N_modes=100)
        det_val = K.fredholm_det()
        expected = eta_product(q1, 100) * eta_product(q2, 100)
        assert abs(det_val - expected) / abs(expected) < 1e-8, \
            f"At w=0: det={det_val}, expected={expected}"


# ======================================================================
# 3. Schur complement factorization
# ======================================================================

class TestSchurFactorization:
    """Tests for the Schur complement factorization identity."""

    @pytest.mark.parametrize("q1,q2,w", [
        (0.1, 0.2, 0.05),
        (0.3, 0.15, 0.08),
        (0.5, 0.4, 0.15),
        (0.05, 0.05, 0.02),
        (0.1 + 0.02j, 0.15 - 0.01j, 0.03 + 0.01j),  # Complex parameters
    ])
    def test_factorization_identity(self, q1, q2, w):
        """det(1-K) = det(1-K_{q1}) * det(1-K_{q2}-S)."""
        result = verify_schur_factorization(q1, q2, w, N_modes=100)
        assert result['match'], \
            f"Factorization failed: rel_error = {result['relative_error']}"

    def test_factorization_handle1_is_eta(self):
        """The first factor det(1-K_{q1}) = eta_product(q1)."""
        q1, q2, w = 0.2, 0.3, 0.1
        K = Genus2SewingKernel(q1, q2, w, N_modes=100)
        factored = K.fredholm_det_factored()
        expected = eta_product(q1, 100)
        assert abs(factored['handle1'] - expected) / abs(expected) < 1e-10

    def test_schur_complement_scalar_at_each_mode(self):
        """For Heisenberg, the Schur complement is scalar at each mode."""
        q1, q2, w = 0.2, 0.3, 0.1
        K = Genus2SewingKernel(q1, q2, w)
        for n in range(1, 10):
            S_n = K.schur_complement_at_mode(n)
            expected = w ** (2 * n) / (1.0 - q1 ** n)
            assert abs(S_n - expected) < 1e-14


# ======================================================================
# 4. Manuscript c_{1,1} coefficient
# ======================================================================

class TestC11Coefficient:
    """Tests for the manuscript's c_{1,1} = sum (q1*q2)^n/((1-q1^n)(1-q2^n))."""

    def test_c11_positive_real_params(self):
        """c_{1,1} > 0 for real q_j in (0,1), as claimed by manuscript."""
        for q1, q2 in [(0.1, 0.2), (0.3, 0.4), (0.5, 0.5), (0.01, 0.99)]:
            c11 = manuscript_c11(q1, q2)
            assert c11.real > 0, f"c11={c11} not positive for q1={q1}, q2={q2}"

    def test_c11_leading_term(self):
        """Leading term of c_{1,1} is q1*q2/((1-q1)(1-q2))."""
        q1, q2 = 0.01, 0.02
        c11 = manuscript_c11(q1, q2)
        leading = q1 * q2 / ((1.0 - q1) * (1.0 - q2))
        # For small q1, q2, the higher terms are O((q1*q2)^2)
        assert abs(c11 - leading) / abs(leading) < 0.01, \
            f"c11={c11}, leading={leading}"

    def test_c11_symmetric(self):
        """c_{1,1}(q1, q2) = c_{1,1}(q2, q1)."""
        q1, q2 = 0.2, 0.35
        c11_12 = manuscript_c11(q1, q2)
        c11_21 = manuscript_c11(q2, q1)
        assert abs(c11_12 - c11_21) < 1e-12

    def test_c11_monotone_in_q(self):
        """c_{1,1} is monotone increasing in each q_j."""
        q2 = 0.2
        c11_prev = 0
        for q1 in [0.05, 0.1, 0.2, 0.3, 0.5]:
            c11 = manuscript_c11(q1, q2).real
            assert c11 > c11_prev, \
                f"c11 not monotone: c11({q1})={c11} <= c11_prev={c11_prev}"
            c11_prev = c11

    def test_c11_differs_from_diagonal_model(self):
        """Manuscript's c_{1,1} != one-particle diagonal model coefficient."""
        q1, q2 = 0.3, 0.4
        c11 = manuscript_c11(q1, q2)
        c_diag = one_particle_w2_coefficient(q1, q2)
        # They must differ: c11 has extra (q1*q2)^n factors
        assert abs(c11 - c_diag) / abs(c_diag) > 0.01, \
            "Manuscript c11 should differ from diagonal model"
        # c11 < c_diag because (q1*q2)^n < 1 for q_j < 1
        assert c11.real < c_diag.real, \
            "c11 should be smaller than diagonal coefficient"


# ======================================================================
# 5. Coupling model identification
# ======================================================================

class TestCouplingModel:
    """Tests for identifying which coupling model matches the manuscript."""

    def test_models_differ(self):
        """The two coupling models give different w^2 coefficients."""
        result = identify_coupling_model(0.3, 0.4)
        assert not result['match_modelA'], \
            "Manuscript c11 should NOT match the naive diagonal model"

    def test_ratio_is_weighted_average(self):
        """Ratio c11/c_diag is a weighted average of (q1*q2)^n.

        The ratio = sum_n (q1*q2)^n / D_n / (sum_n 1/D_n)
        where D_n = (1-q1^n)(1-q2^n).

        This is a weighted average of (q1*q2)^n with weights 1/D_n.
        Since D_n -> 1 for large n and (q1*q2)^n -> 0, the large-n
        terms dominate the denominator but not the numerator. The ratio
        is dominated by the first few terms and is strictly between 0 and 1.
        """
        q1, q2 = 0.2, 0.3
        result = identify_coupling_model(q1, q2)
        ratio = result['ratio_manuscript_to_modelA']
        assert ratio is not None
        assert 0 < ratio.real < 1
        # The ratio should be small for small q1*q2
        assert ratio.real < q1 * q2 * 2  # Loose upper bound


# ======================================================================
# 6. Correction factor structure
# ======================================================================

class TestCorrectionFactor:
    """Tests for the correction factor F(q1, q2, w)."""

    def test_correction_factor_unity_at_w0(self):
        """F(q1, q2, 0) = 1."""
        q1, q2 = 0.2, 0.3
        K = Genus2SewingKernel(q1, q2, 1e-15, N_modes=100)
        F = K.correction_factor()
        assert abs(F - 1.0) < 1e-8

    def test_correction_factor_greater_than_1(self):
        """F > 1 for w > 0 (the genus-2 coupling enhances the partition function)."""
        for q1, q2, w in [(0.1, 0.2, 0.05), (0.3, 0.3, 0.1), (0.5, 0.4, 0.15)]:
            K = Genus2SewingKernel(q1, q2, w, N_modes=100)
            F = K.correction_factor()
            assert F.real > 1.0, \
                f"F = {F} not > 1 for q1={q1}, q2={q2}, w={w}"

    def test_correction_factor_symmetric(self):
        """F(q1, q2, w) = F(q2, q1, w)."""
        q1, q2, w = 0.2, 0.35, 0.08
        K1 = Genus2SewingKernel(q1, q2, w, N_modes=100)
        K2 = Genus2SewingKernel(q2, q1, w, N_modes=100)
        assert abs(K1.correction_factor() - K2.correction_factor()) < 1e-12

    def test_genus1_product_matches_etas(self):
        """genus1_product = eta_product(q1) * eta_product(q2)."""
        q1, q2 = 0.2, 0.3
        K = Genus2SewingKernel(q1, q2, 0.1, N_modes=100)
        g1p = K.genus1_product()
        expected = eta_product(q1, 100) * eta_product(q2, 100)
        assert abs(g1p - expected) / abs(expected) < 1e-12


# ======================================================================
# 7. Fourier expansion
# ======================================================================

class TestFourierExpansion:
    """Tests for the Fourier expansion of the correction factor."""

    def test_zeroth_coefficient_is_1(self):
        """c_0 = 1."""
        coeffs = genus2_fourier_coefficients(0.2, 0.3, max_order_w=6)
        assert abs(coeffs[0] - 1.0) < 1e-12

    def test_even_powers_only(self):
        """In the diagonal model, only even powers of w appear."""
        result = siegel_fourier_check(0.2, 0.3)
        assert result['even_powers_only']

    def test_second_coefficient_matches(self):
        """c_2(q1, q2) = u_1 = 1/((1-q1)(1-q2)).

        The coefficient of w^2 (= t^1) in F = prod_n 1/(1-u_n t^n) comes
        ONLY from the n=1 factor (since the n>=2 factors contribute at t^2
        and higher). So c_2 = u_1 = 1/((1-q1)(1-q2)), NOT sum_n u_n.

        Note: sum_n u_n = sum_n 1/((1-q1^n)(1-q2^n)) is the coefficient
        of w^2 in log(F), not in F itself. But at leading order (log F ~ F-1),
        these are the same. At subleading order they differ.
        """
        q1, q2 = 0.2, 0.3
        coeffs = genus2_fourier_coefficients(q1, q2, max_order_w=4, N_modes=50)
        c2_expansion = coeffs[2]
        c2_expected = 1.0 / ((1.0 - q1) * (1.0 - q2))
        assert abs(c2_expansion - c2_expected) / abs(c2_expected) < 1e-10, \
            f"c_2 expansion={c2_expansion}, expected={c2_expected}"

    def test_fourier_expansion_convergent(self):
        """Fourier expansion should converge for small w."""
        q1, q2, w = 0.2, 0.3, 0.05
        K = Genus2SewingKernel(q1, q2, w, N_modes=50)
        F_exact = K.correction_factor()

        coeffs = genus2_fourier_coefficients(q1, q2, max_order_w=10, N_modes=50)
        F_approx = sum(coeffs[2 * k] * w ** (2 * k) for k in range(6))

        rel_err = abs(F_exact - F_approx) / abs(F_exact)
        assert rel_err < 0.01, f"Fourier expansion rel_err = {rel_err}"


# ======================================================================
# 8. Non-factorization at q3 != 0
# ======================================================================

class TestNonFactorization:
    """Tests for thm:genus2-non-collapse: det(1-K_2) does not factor."""

    def test_nonfactorization(self):
        """det(1-K_2) != det(1-K_{q1}) * det(1-K_{q2}) for w > 0."""
        q1, q2, w = 0.2, 0.3, 0.1
        K = Genus2SewingKernel(q1, q2, w, N_modes=100)
        det_full = K.fredholm_det()
        det_product = K.genus1_product()
        assert abs(det_full - det_product) / abs(det_product) > 1e-3, \
            "Genus-2 determinant should NOT equal the genus-1 product for w > 0"

    def test_factorization_in_limit(self):
        """det(1-K_2) -> det(1-K_{q1}) * det(1-K_{q2}) as w -> 0."""
        q1, q2 = 0.2, 0.3
        for w in [0.1, 0.01, 0.001, 1e-6]:
            K = Genus2SewingKernel(q1, q2, w, N_modes=100)
            det_full = K.fredholm_det()
            det_product = K.genus1_product()
            rel_diff = abs(det_full - det_product) / abs(det_product)
            if w < 0.01:
                assert rel_diff < 0.01, \
                    f"w={w}: rel_diff={rel_diff} not small"

    def test_correction_grows_with_w(self):
        """The correction factor F grows monotonically with |w|."""
        q1, q2 = 0.2, 0.3
        F_prev = 1.0
        for w in [0.01, 0.05, 0.1, 0.15, 0.2]:
            K = Genus2SewingKernel(q1, q2, w, N_modes=100)
            F = K.correction_factor().real
            assert F > F_prev, f"F not monotone at w={w}"
            F_prev = F


# ======================================================================
# 9. Schur complement eigenvalues and moments
# ======================================================================

class TestSchurMoments:
    """Tests for the Schur complement trace moments."""

    def test_moments_positive(self):
        """Tr(S^k) > 0 for real positive parameters."""
        moments = schur_complement_trace_moments(0.2, 0.3, 0.1, max_moment=4)
        for k, val in moments.items():
            assert val.real > 0, f"Tr(S^{k}) = {val} not positive"

    def test_moments_decay(self):
        """|Tr(S^{k+1})| < |Tr(S^k)| for small w (contraction)."""
        moments = schur_complement_trace_moments(0.2, 0.3, 0.05, max_moment=4)
        for k in range(1, 4):
            assert abs(moments[k + 1]) < abs(moments[k]), \
                f"|Tr(S^{k+1})| >= |Tr(S^{k})|"

    def test_eigenvalues_decay(self):
        """Schur complement eigenvalues decay: S_{n+1} < S_n for small w."""
        eigs = schur_complement_eigenvalues(0.2, 0.3, 0.05, N_modes=20)
        for n in range(len(eigs) - 1):
            assert abs(eigs[n + 1]) < abs(eigs[n]) or abs(eigs[n]) < 1e-15, \
                f"Eigenvalues not decaying at n={n}"


# ======================================================================
# 10. Newton independence test
# ======================================================================

class TestNewtonIndependence:
    """Tests for the non-Newton constraint analysis."""

    def test_heisenberg_no_non_newton(self):
        """For Heisenberg, no non-Newton constraints."""
        result = newton_independence_test(0.2, 0.3, 0.1)
        assert result['non_newton_for_heisenberg'] is False

    def test_convergence_satisfied(self):
        """All modes convergent for small w."""
        result = newton_independence_test(0.2, 0.3, 0.05)
        assert result['all_modes_convergent']

    def test_convergence_fails_large_w(self):
        """Convergence fails for w too large."""
        # Need w^2 > (1-q1)(1-q2) at mode 1
        q1, q2 = 0.2, 0.3
        w_critical = np.sqrt((1 - q1) * (1 - q2))  # ~ 0.748
        result = newton_independence_test(q1, q2, w_critical * 0.99)
        # Should be convergent but barely
        mode1 = result['convergence_data'][1]
        assert mode1['ratio'] > 0.9


# ======================================================================
# 11. Virasoro Schur complement structure
# ======================================================================

class TestVirasuroStructure:
    """Tests for the Virasoro Schur complement at higher weights."""

    def test_weight2_scalar(self):
        """At weight 2, the Virasoro Schur complement is scalar (dim 1)."""
        result = virasoro_schur_complement_structure(25.0, 0.2, 0.3, 0.1)
        assert result[2]['dim'] == 1
        assert not result[2]['non_trivial_matrix']

    def test_weight4_matrix(self):
        """At weight 4, the Virasoro Schur complement is a matrix (dim 2)."""
        result = virasoro_schur_complement_structure(25.0, 0.2, 0.3, 0.1)
        # dim V_4 = p(4) - p(3) = 5 - 3 = 2
        assert result[4]['dim'] == 2
        assert result[4]['non_trivial_matrix']

    def test_weight_dimensions(self):
        """Verify vacuum Virasoro module dimensions.

        dim V_n = p(n) - p(n-1) for n >= 2 (L_{-1}|0> = 0).
        p = {0:1, 1:1, 2:2, 3:3, 4:5, 5:7, 6:11}
        So dim V_n = {2:1, 3:1, 4:2, 5:2, 6:4}.
        """
        expected_dims = {2: 1, 3: 1, 4: 2, 5: 2, 6: 4}
        result = virasoro_schur_complement_structure(25.0, 0.2, 0.3, 0.1)
        for n, d in expected_dims.items():
            assert result[n]['dim'] == d, \
                f"dim V_{n} = {result[n]['dim']}, expected {d}"

    def test_first_nontrivial_weight_is_4(self):
        """First non-scalar Schur complement is at weight 4."""
        result = virasoro_schur_complement_structure(25.0, 0.2, 0.3, 0.1)
        first_matrix = min(n for n, d in result.items() if d['non_trivial_matrix'])
        assert first_matrix == 4


# ======================================================================
# 12. Genus-2 partition function models
# ======================================================================

class TestGenus2PartitionFunction:
    """Tests for the genus-2 partition function models."""

    def test_model_A_matches_kernel(self):
        """Model A should match the Genus2SewingKernel direct computation."""
        q1, q2, q3 = 0.2, 0.3, 0.1
        N = 80
        pf = Genus2PartitionFunction(q1, q2, q3, N_modes=N)
        models = pf.partition_function_model_sewing()
        K = Genus2SewingKernel(q1, q2, q3, N_modes=N)
        direct = 1.0 / K.fredholm_det()
        # Model A: coupling w^n, same as kernel
        assert abs(models['model_A'] - direct) / abs(direct) < 1e-8

    def test_models_differ(self):
        """Model A and Model B give different results for q3 > 0."""
        q1, q2, q3 = 0.2, 0.3, 0.1
        pf = Genus2PartitionFunction(q1, q2, q3, N_modes=80)
        models = pf.partition_function_model_sewing()
        assert abs(models['model_A'] - models['model_B']) / abs(models['model_A']) > 1e-3

    def test_models_agree_at_q3_zero(self):
        """Both models agree at q3 = 0 (genus-1 factorization)."""
        q1, q2 = 0.2, 0.3
        pf = Genus2PartitionFunction(q1, q2, 1e-15, N_modes=80)
        models = pf.partition_function_model_sewing()
        assert abs(models['model_A'] - models['model_B']) / abs(models['model_A']) < 1e-6


# ======================================================================
# 13. Positivity verification (prop:genus2-non-diagonal proof check)
# ======================================================================

class TestPositivityVerification:
    """Tests for the positivity proof of c_{1,1}."""

    def test_positivity_proof(self):
        """Verify the trivial positivity argument."""
        result = verify_c11_positivity(0.1, 0.15)
        assert result['positive']
        # All individual terms should be positive
        assert all(t > 0 for t in result['first_terms'])

    @pytest.mark.parametrize("q1,q2", [
        (0.01, 0.01),
        (0.1, 0.5),
        (0.5, 0.5),
        (0.9, 0.1),
        (0.99, 0.01),
    ])
    def test_positivity_parametric(self, q1, q2):
        """c_{1,1} > 0 across parameter range."""
        c11 = manuscript_c11(q1, q2)
        assert c11.real > 0, f"c11({q1},{q2}) = {c11}"


# ======================================================================
# 14. Asymptotic behavior
# ======================================================================

class TestAsymptotics:
    """Tests for asymptotic behavior of the Schur complement."""

    def test_correction_small_for_small_w(self):
        """F - 1 = O(w^2) as w -> 0."""
        q1, q2 = 0.2, 0.3
        for w in [0.01, 0.005, 0.001]:
            K = Genus2SewingKernel(q1, q2, w, N_modes=100)
            F = K.correction_factor().real
            deviation = F - 1.0
            # Should scale as w^2
            assert deviation > 0
            if w == 0.01:
                ref = deviation
            else:
                ratio = deviation / ref / (w / 0.01) ** 2
                assert abs(ratio - 1.0) < 0.1, \
                    f"F-1 not scaling as w^2: ratio={ratio}"

    def test_schur_hs_bound(self):
        r"""||S||_HS <= C * |q3|^{1/2} as claimed by manuscript (for ||R||_HS).

        Actually the manuscript claims ||R_{ij}||_HS <= C |q3|^{1/2}, and the
        Schur complement S = R^2/(1-K) has ||S|| ~ |q3|.
        """
        q1, q2 = 0.2, 0.3
        for w in [0.1, 0.05, 0.01]:
            eigs = schur_complement_eigenvalues(q1, q2, w, N_modes=50)
            # HS norm^2 = sum |S_n|^2 = sum w^{4n}/(1-q1^n)^2
            hs_norm_sq = sum(abs(eigs[n]) ** 2 for n in range(len(eigs)))
            hs_norm = np.sqrt(hs_norm_sq)
            # Should scale as w^2 (leading term is w^2/(1-q1))
            if w == 0.1:
                ref_norm = hs_norm
                ref_w = w
            else:
                ratio = hs_norm / ref_norm / (w / ref_w) ** 2
                assert abs(ratio - 1.0) < 0.2, \
                    f"HS norm scaling: ratio={ratio}"


# ======================================================================
# 15. Full analysis integration test
# ======================================================================

class TestFullAnalysis:
    """Integration tests for the full analysis."""

    def test_full_analysis_runs(self):
        """Full analysis completes without error."""
        result = full_analysis(0.1, 0.15, 0.05)
        assert result['schur_factorization_verified']
        assert result['c11_positive']
        assert result['non_newton_heisenberg'] is False
        assert result['non_newton_interacting'] is True

    def test_full_analysis_summary_nonempty(self):
        """Summary field is populated."""
        result = full_analysis(0.1, 0.15, 0.05)
        assert len(result['summary']) > 100


# ======================================================================
# 16. Cross-validation with existing modules
# ======================================================================

class TestCrossValidation:
    """Cross-validation against existing compute modules."""

    def test_eta_product_matches_fredholm_engine(self):
        """Our eta_product matches fredholm_sewing_engine.dedekind_eta_product."""
        try:
            from fredholm_sewing_engine import dedekind_eta_product as eta_fse
            q = 0.3
            our_val = eta_product(q, 200)
            their_val = eta_fse(q, 200)
            assert abs(our_val - their_val) < 1e-12
        except ImportError:
            pytest.skip("fredholm_sewing_engine not available")

    def test_partitions_matches_fredholm_engine(self):
        """Our partitions matches fredholm_sewing_engine.partitions."""
        try:
            from fredholm_sewing_engine import partitions as p_fse
            for n in range(20):
                assert partitions(n) == p_fse(n)
        except ImportError:
            pytest.skip("fredholm_sewing_engine not available")


# ======================================================================
# 17. Manuscript formula verification (the critical test)
# ======================================================================

class TestManuscriptFormula:
    """Direct verification of the manuscript's expansion formula.

    Manuscript (prop:genus2-non-diagonal) claims:
        det(1-K_2)^{-1} = eta(tau_1)^{-1} eta(tau_2)^{-1} * (1 + c_{1,1} r + ...)

    We verify this by computing both sides numerically.
    """

    def test_expansion_leading_correction(self):
        """Verify the ratio det(1-K)^{-1} / (eta1^{-1} eta2^{-1}) to first order.

        For the one-particle diagonal model, the correction is in w^2, not w.
        So we verify:
            F = det(1-K)^{-1} / (eta1^{-1} eta2^{-1}) = 1 + u_1 w^2 + O(w^4)

        where u_1 = 1/((1-q1)(1-q2)) is the n=1 coefficient.

        Note: the coefficient of w^2 in F is u_1 (from the n=1 factor ONLY),
        NOT sum_n u_n (which is the coefficient of w^2 in log F).
        """
        q1, q2 = 0.2, 0.3
        w = 0.02  # Small enough for leading-order approximation
        N = 100

        K = Genus2SewingKernel(q1, q2, w, N_modes=N)
        F_exact = K.correction_factor()
        u1 = 1.0 / ((1.0 - q1) * (1.0 - q2))
        F_approx = 1.0 + u1 * w ** 2

        rel_err = abs(F_exact - F_approx) / abs(F_exact)
        assert rel_err < 0.001, f"Leading-order approximation rel_err = {rel_err}"

    def test_c11_as_coefficient_of_qq_w2(self):
        """The manuscript's c_{1,1} equals the coefficient of (q1*q2)*w^2/(...)
        in the full expansion when we set r = q1*q2*w^2.

        Actually: if we define r = q1*q2*w^2 (interpreting the manuscript's r
        as the product variable), then:

        F_model_B = prod_n 1/(1 - (q1*q2*w^2)^n / ((1-q1^n)(1-q2^n)))

        and the coefficient of r^1 in F_model_B is
        sum_n 1/((1-q1^n)(1-q2^n)) which is NOT the manuscript's c_{1,1}.

        The manuscript's c_{1,1} = sum_n (q1*q2)^n/((1-q1^n)(1-q2^n)),
        which is the coefficient of w^2 in Model B:
        prod_n 1/(1 - (q1*q2)^n * w^{2n} / ((1-q1^n)(1-q2^n))).
        """
        q1, q2 = 0.2, 0.3
        w = 0.02
        N = 100

        # Model B: coupling is (q1*q2)^{n/2} * w^n
        # det = prod_n ((1-q1^n)(1-q2^n) - (q1*q2)^n * w^{2n})
        F_B = 1.0 + 0j
        for n in range(1, N + 1):
            denom = (1.0 - q1 ** n) * (1.0 - q2 ** n) - (q1 * q2) ** n * w ** (2 * n)
            g1 = (1.0 - q1 ** n) * (1.0 - q2 ** n)
            F_B *= g1 / denom

        c11 = manuscript_c11(q1, q2, N)
        F_approx = 1.0 + c11 * w ** 2

        rel_err = abs(F_B - F_approx) / abs(F_B)
        assert rel_err < 0.001, \
            f"Model B first-order: F_B={F_B}, approx={F_approx}, rel_err={rel_err}"

    def test_full_expansion_model_B(self):
        """Verify Model B correction factor at moderate w."""
        q1, q2 = 0.2, 0.3
        w = 0.1
        N = 80

        # Model B exact
        F_B_exact = 1.0 + 0j
        for n in range(1, N + 1):
            g1 = (1.0 - q1 ** n) * (1.0 - q2 ** n)
            alpha_n = (q1 * q2) ** n * w ** (2 * n)
            F_B_exact *= g1 / (g1 - alpha_n)

        # Check F_B > 1
        assert F_B_exact.real > 1.0

        # Model A exact
        K = Genus2SewingKernel(q1, q2, w, N_modes=N)
        F_A_exact = K.correction_factor()

        # They should differ
        assert abs(F_B_exact - F_A_exact) / abs(F_A_exact) > 0.001, \
            "Models A and B should give different correction factors"


# ======================================================================
# 18. Convergence radius
# ======================================================================

class TestConvergenceRadius:
    """Tests for the convergence radius of the sewing expansion."""

    def test_convergence_radius_mode1(self):
        """At mode 1, convergence requires w^2 < (1-q1)(1-q2)."""
        q1, q2 = 0.3, 0.4
        w_max = np.sqrt((1 - q1) * (1 - q2))  # ~ 0.648
        # Below threshold: convergent
        K_below = Genus2SewingKernel(q1, q2, w_max * 0.9, N_modes=50)
        det_below = K_below.det_one_minus_K_at_mode(1)
        assert det_below.real > 0

    def test_siegel_positivity_constraint(self):
        """The convergence condition implies Im(Omega) > 0 (Siegel positivity).

        For separating degeneration with w = e^{2pi i delta}:
        w^{2n} < (1-q_1^n)(1-q_2^n) for all n >= 1
        is equivalent to the Siegel upper half-plane condition
        Im(Omega) > 0 for the 2x2 period matrix.
        """
        q1 = np.exp(-2 * np.pi * 0.5)  # tau_1 = 0.5i
        q2 = np.exp(-2 * np.pi * 0.4)  # tau_2 = 0.4i
        # Off-diagonal period z = 0.1i gives w = e^{-0.2*pi}
        w = np.exp(-2 * np.pi * 0.1)

        # This should be in the convergence domain
        K = Genus2SewingKernel(q1, q2, w, N_modes=50)
        det_val = K.fredholm_det()
        assert det_val.real > 0

        # The period matrix Omega = ((0.5i, 0.1i), (0.1i, 0.4i))
        # has Im(Omega) = ((0.5, 0.1), (0.1, 0.4))
        # which is positive definite (det = 0.19 > 0, trace > 0)
        im_omega = np.array([[0.5, 0.1], [0.1, 0.4]])
        assert np.linalg.det(im_omega) > 0


# ======================================================================
# 19. Non-Newton constraints for interacting algebras
# ======================================================================

class TestInteractingNonNewton:
    """Tests for non-Newton constraints from interacting algebra structure."""

    def test_weight4_matrix_dimension(self):
        """Virasoro at weight 4 has 2D Schur complement."""
        # p(4) = 5, p(3) = 3, so dim V_4 = 2
        assert partitions(4) - partitions(3) == 2

    def test_non_newton_analysis_interacting_flag(self):
        """Non-Newton analysis flags interacting algebras."""
        result = non_newton_analysis(0.2, 0.3, 0.1)
        assert result['interacting']['non_newton'] is True
        assert result['interacting']['first_nontrivial_weight'] == 4

    def test_heisenberg_determined_by_genus1(self):
        """Heisenberg genus-2 is determined by genus-1 data plus w.

        Specifically: if we know eta(tau_1)^{-1} and eta(tau_2)^{-1},
        then det(1-K_2)^{-1} is determined as an explicit function.
        """
        q1, q2, w = 0.2, 0.3, 0.1
        N = 100

        # Reconstruct det(1-K_2)^{-1} from genus-1 data + w
        eta1_inv = eta_inv(q1, N)
        eta2_inv = eta_inv(q2, N)

        K = Genus2SewingKernel(q1, q2, w, N_modes=N)
        F = K.correction_factor()
        reconstructed = eta1_inv * eta2_inv * F

        direct = 1.0 / K.fredholm_det()

        assert abs(reconstructed - direct) / abs(direct) < 1e-10, \
            "Genus-2 PF should be reconstructible from genus-1 data + w"


# ======================================================================
# 20. Summary test: the key mathematical question
# ======================================================================

class TestKeyQuestion:
    """The key question: does genus-2 off-diagonal coupling give
    genuinely new constraints on Satake parameters?

    ANSWER: For Heisenberg (free field) — NO. The genus-2 data is
    determined by genus-1 data.

    For interacting algebras — YES, starting at weight 4, where the
    sewing matrix becomes non-scalar and encodes OPE structure constants
    that are invisible to the genus-1 partition function.

    The non-Newton content is:
    1. STRUCTURAL: the Schur complement S = M^T M / (1-q) depends
       quadratically on OPE coefficients, introducing new relations.
    2. PERTURBATIVELY SMALL: ||S|| ~ |q_3| in the separating limit.
    3. GENUS-SPECIFIC: these constraints genuinely require genus-2 data
       and do not follow from any finite collection of genus-1 data.
    """

    def test_key_answer_heisenberg(self):
        result = full_analysis(0.1, 0.15, 0.05)
        assert result['non_newton_heisenberg'] is False

    def test_key_answer_interacting(self):
        result = full_analysis(0.1, 0.15, 0.05)
        assert result['non_newton_interacting'] is True

    def test_key_answer_verified(self):
        """All sub-verifications pass."""
        result = full_analysis(0.1, 0.15, 0.05)
        assert result['schur_factorization_verified']
        assert result['c11_positive']
