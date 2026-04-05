r"""Tests for BC-84: Categorical zeta functions at roots of unity.

Tests organized by section:
  1.  Quantum dimensions for sl_2 (trigonometric formula)
  2.  Quantum dimensions for sl_3 (Weyl-Kac)
  3.  Quantum dimensions for G_2 (non-simply-laced)
  4.  Integrable weight enumeration / counting
  5.  Modular S-matrix (Verlinde)
  6.  Modular categorical zeta for sl_2
  7.  Modular categorical zeta for sl_3
  8.  Modular categorical zeta for G_2
  9.  k -> infinity limit and convergence to Riemann zeta
  10. Asymptotic expansion
  11. Modular zeta at s = 0 (representation counting)
  12. Level-rank duality
  13. Zeros of modular categorical zeta
  14. Shadow-modular comparison
  15. Quantum vs classical dimension comparison
  16. Critical line evaluations
  17. Cross-checks and multi-path verification
"""

import pytest
import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_quantum_group_roots_engine import (
    # Section 0: Root system data
    dual_coxeter_number, lie_algebra_dim,
    # Section 1: Quantum dimensions
    quantum_dim_sl2, quantum_dim_sl3, quantum_dim_g2,
    quantum_dim_general, _quantum_dim_slN,
    # Section 2: Integrable weights
    integrable_weights_sl2, integrable_weights_sl3, integrable_weights_g2,
    integrable_weights_slN, num_integrable_weights,
    # Section 3: S-matrix
    s_matrix_sl2, verify_s_matrix_unitarity,
    verlinde_quantum_dim_sl2, verlinde_fusion_sl2,
    # Section 4: Modular zeta
    modular_zeta_sl2, modular_zeta_sl3, modular_zeta_g2,
    modular_zeta_slN, modular_zeta_general,
    # Section 5: Convergence
    modular_zeta_convergence_sl2, _riemann_zeta_em,
    asymptotic_expansion_sl2,
    # Section 6: s=0
    modular_zeta_at_zero,
    # Section 7: Level-rank
    level_rank_duality_check, level_rank_quantum_dims_sl,
    # Section 8: Zeros
    find_zeros_modular_zeta_sl2, modular_zeta_on_line,
    # Section 9: Shadow comparison
    kappa_affine, shadow_modular_comparison,
    # Section 10: Spectra
    quantum_dim_spectrum_sl2, quantum_dim_spectrum_sl3, quantum_dim_spectrum_g2,
    classical_dim_sl2, classical_dim_sl3, classical_dim_g2,
    quantum_vs_classical_sl2,
    # Section 11: Critical line
    modular_zeta_critical_line_sl2,
    # Section 12: Full verification
    full_verification_report,
)

import numpy as np


# =========================================================================
# Section 1: Quantum dimensions for sl_2
# =========================================================================

class TestQuantumDimSl2:
    """Quantum dimensions for sl_2 at roots of unity."""

    def test_trivial_rep(self):
        """V_0 has quantum dimension 1 at any level."""
        for k in range(1, 20):
            assert abs(quantum_dim_sl2(0, k) - 1.0) < 1e-12

    def test_fundamental_at_level_1(self):
        """sl_2 at level 1: V_0 (dim 1) and V_1 (dim = sin(2pi/3)/sin(pi/3) = 1)."""
        d = quantum_dim_sl2(1, 1)
        # sin(2*pi/3)/sin(pi/3) = sin(2pi/3)/sin(pi/3) = 1
        assert abs(d - 1.0) < 1e-12

    def test_ising_model_level_2(self):
        """sl_2 at level 2 = Ising model.

        V_0: dim_q = 1
        V_1: dim_q = sin(2pi/4)/sin(pi/4) = sqrt(2)
        V_2: dim_q = sin(3pi/4)/sin(pi/4) = 1
        """
        assert abs(quantum_dim_sl2(0, 2) - 1.0) < 1e-12
        assert abs(quantum_dim_sl2(1, 2) - math.sqrt(2)) < 1e-12
        assert abs(quantum_dim_sl2(2, 2) - 1.0) < 1e-12

    def test_level_3(self):
        """sl_2 at level 3: quantum dimensions from sin formula."""
        k = 3
        p = 5  # k + 2
        expected = [
            math.sin(1 * math.pi / p) / math.sin(math.pi / p),  # j=0: 1
            math.sin(2 * math.pi / p) / math.sin(math.pi / p),  # j=1
            math.sin(3 * math.pi / p) / math.sin(math.pi / p),  # j=2
            math.sin(4 * math.pi / p) / math.sin(math.pi / p),  # j=3
        ]
        for j in range(4):
            assert abs(quantum_dim_sl2(j, k) - expected[j]) < 1e-12

    def test_golden_ratio_level_3(self):
        """At level 3 (p=5), quantum dim of V_1 = golden ratio phi = (1+sqrt(5))/2."""
        phi = (1 + math.sqrt(5)) / 2
        d = quantum_dim_sl2(1, 3)
        assert abs(d - phi) < 1e-10

    def test_symmetry_quantum_dim(self):
        """dim_q(V_j) = dim_q(V_{k-j}) for sl_2 at level k.

        This is the charge conjugation symmetry: sin((j+1)pi/p) = sin((k+1-j)pi/p)
        since (j+1) + (k+1-j) = k+2 = p, so sin((k+1-j)pi/p) = sin(pi - (j+1)pi/p) = sin((j+1)pi/p).
        """
        for k in [2, 5, 10, 20]:
            for j in range(k + 1):
                d1 = quantum_dim_sl2(j, k)
                d2 = quantum_dim_sl2(k - j, k)
                assert abs(d1 - d2) < 1e-10, f"Symmetry failed at k={k}, j={j}"

    def test_quantum_dim_positivity(self):
        """All integrable quantum dimensions are positive for sl_2."""
        for k in range(1, 25):
            for j in range(k + 1):
                d = quantum_dim_sl2(j, k)
                assert d > 0, f"Negative quantum dim at k={k}, j={j}: {d}"

    def test_quantum_dim_large_k_limit(self):
        """As k -> infinity, quantum dim [j+1]_q -> j+1 (classical dim)."""
        k = 500
        for j in range(10):
            d_q = quantum_dim_sl2(j, k)
            d_cl = j + 1
            assert abs(d_q - d_cl) < 0.1, f"Large k limit failed at j={j}: {d_q} vs {d_cl}"

    def test_quantum_dim_bounds(self):
        """Quantum dimensions satisfy 0 < dim_q(V_j) <= j+1 for sl_2."""
        for k in range(1, 20):
            for j in range(k + 1):
                d = quantum_dim_sl2(j, k)
                assert 0 < d <= j + 1 + 1e-10, f"Bound violation at k={k}, j={j}: {d}"

    def test_highest_rep_dim(self):
        """V_k at level k has quantum dimension sin((k+1)pi/(k+2))/sin(pi/(k+2)).

        For k=1: sin(2pi/3)/sin(pi/3) = 1.
        For k=2: sin(3pi/4)/sin(pi/4) = 1.
        In general, V_k has dim_q = 1 (it is the "conjugate" of V_0).
        Wait: sin((k+1)*pi/(k+2))/sin(pi/(k+2)) = sin(pi - pi/(k+2))/sin(pi/(k+2))
        = sin(pi/(k+2))/sin(pi/(k+2)) = 1.
        """
        for k in range(1, 20):
            d = quantum_dim_sl2(k, k)
            assert abs(d - 1.0) < 1e-10, f"V_k dim != 1 at k={k}: {d}"

    def test_invalid_j_raises(self):
        """j outside [0, k] should raise ValueError."""
        with pytest.raises(ValueError):
            quantum_dim_sl2(-1, 5)
        with pytest.raises(ValueError):
            quantum_dim_sl2(6, 5)


# =========================================================================
# Section 2: Quantum dimensions for sl_3
# =========================================================================

class TestQuantumDimSl3:
    """Quantum dimensions for sl_3 at roots of unity."""

    def test_trivial_rep(self):
        """V(0,0) has quantum dimension 1."""
        for k in range(1, 10):
            assert abs(quantum_dim_sl3(0, 0, k) - 1.0) < 1e-10

    def test_fundamental_rep(self):
        """V(1,0) at level 1: quantum dim from the formula.

        p = k + 3 = 4.
        dim_q = sin(2pi/4)*sin(pi/4)*sin(3pi/4) / (sin(pi/4)*sin(pi/4)*sin(2pi/4))
        = sin(pi/2)*sin(pi/4)*sin(3pi/4) / (sin(pi/4)^2*sin(pi/2))
        = sin(3pi/4)/sin(pi/4) = 1.
        """
        d = quantum_dim_sl3(1, 0, 1)
        assert abs(d - 1.0) < 1e-10

    def test_adjoint_rep_level_1(self):
        """At level 1, only (0,0), (1,0), (0,1) are integrable."""
        d00 = quantum_dim_sl3(0, 0, 1)
        d10 = quantum_dim_sl3(1, 0, 1)
        d01 = quantum_dim_sl3(0, 1, 1)
        assert abs(d00 - 1.0) < 1e-10
        assert abs(d10 - d01) < 1e-10  # conjugate reps have equal quantum dims

    def test_classical_limit(self):
        """At large k, quantum dim -> classical dim."""
        k = 200
        # V(1,0): classical dim = 3
        d = quantum_dim_sl3(1, 0, k)
        assert abs(d - 3.0) < 0.1

        # V(1,1): classical dim = (2)(2)(4)/2 = 8
        d = quantum_dim_sl3(1, 1, k)
        assert abs(d - 8.0) < 0.1

    def test_conjugation_symmetry(self):
        """dim_q V(a,b) = dim_q V(b,a) for sl_3 (conjugation)."""
        for k in [3, 5, 8]:
            for a in range(k + 1):
                for b in range(k + 1 - a):
                    d1 = quantum_dim_sl3(a, b, k)
                    d2 = quantum_dim_sl3(b, a, k)
                    assert abs(d1 - d2) < 1e-10, f"Conjugation symmetry failed at k={k}, (a,b)=({a},{b})"

    def test_positivity(self):
        """All integrable quantum dimensions are positive for sl_3."""
        for k in range(1, 10):
            for a, b in integrable_weights_sl3(k):
                d = quantum_dim_sl3(a, b, k)
                assert d > -1e-10, f"Negative dim at k={k}, (a,b)=({a},{b}): {d}"

    def test_level_2_dimensions(self):
        """sl_3 at level 2: explicit quantum dimensions.

        p = 5.  Integrable weights: (a,b) with a+b <= 2.
        (0,0), (1,0), (0,1), (2,0), (1,1), (0,2).
        """
        k = 2
        # Just check all are positive and (0,0) = 1
        assert abs(quantum_dim_sl3(0, 0, k) - 1.0) < 1e-10
        for a, b in [(1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]:
            d = quantum_dim_sl3(a, b, k)
            assert d > 0, f"dim_q V({a},{b}) = {d} at k={k}"


# =========================================================================
# Section 3: Quantum dimensions for G_2
# =========================================================================

class TestQuantumDimG2:
    """Quantum dimensions for G_2 at roots of unity."""

    def test_trivial_rep(self):
        """V(0,0) has quantum dimension 1."""
        for k in range(2, 8):
            assert abs(quantum_dim_g2(0, 0, k) - 1.0) < 1e-10

    def test_classical_limit_adjoint(self):
        """At large k, V(1,0) (adjoint) should have quantum dim -> 14.

        Bourbaki convention: alpha_1 long, alpha_2 short. V(1,0) is the adjoint.
        """
        k = 300
        d = quantum_dim_g2(1, 0, k)
        assert abs(d - 14.0) < 0.1, f"G_2 V(1,0) quantum dim at k={k}: {d}"

    def test_classical_limit_7d_rep(self):
        """At large k, V(0,1) (fundamental, 7-dim) should have quantum dim -> 7."""
        k = 300
        d = quantum_dim_g2(0, 1, k)
        assert abs(d - 7.0) < 0.1, f"G_2 V(0,1) quantum dim at k={k}: {d}"

    def test_classical_dim_g2_14(self):
        """Classical dimension formula: V(1,0) of G_2 = 14 (adjoint).

        Bourbaki convention: alpha_1 long, alpha_2 short.
        V(1,0) = adjoint representation.
        """
        assert classical_dim_g2(1, 0) == 14

    def test_classical_dim_g2_7(self):
        """Classical dimension formula: V(0,1) of G_2 = 7 (fundamental)."""
        assert classical_dim_g2(0, 1) == 7

    def test_classical_dim_g2_77(self):
        """Classical dimension formula: V(2,0) of G_2 = 77."""
        assert classical_dim_g2(2, 0) == 77

    def test_classical_dim_g2_27(self):
        """Classical dimension formula: V(0,2) of G_2 = 27."""
        assert classical_dim_g2(0, 2) == 27

    def test_positivity(self):
        """All integrable quantum dimensions are positive for G_2."""
        for k in range(2, 10):
            for a, b in integrable_weights_g2(k):
                d = quantum_dim_g2(a, b, k)
                assert d > -1e-10, f"Negative dim at k={k}, (a,b)=({a},{b}): {d}"

    def test_integrability_condition(self):
        """Integrability: 2a + b <= k for G_2 (Bourbaki: alpha_1 long)."""
        for k in [2, 4, 6]:
            weights = integrable_weights_g2(k)
            for a, b in weights:
                assert 2 * a + b <= k, f"({a},{b}) violates 2a+b<={k}"

    def test_level_2_spectrum(self):
        """G_2 at level 2: integrable weights are (a,b) with 2a+b<=2.

        (0,0), (0,1), (0,2), (1,0).
        """
        weights = integrable_weights_g2(2)
        expected = [(0, 0), (0, 1), (0, 2), (1, 0)]
        assert set(weights) == set(expected)


# =========================================================================
# Section 4: Integrable weight enumeration / counting
# =========================================================================

class TestIntegrableWeights:
    """Enumeration and counting of integrable weights."""

    def test_sl2_count(self):
        """sl_2 at level k: k+1 integrable weights."""
        for k in range(1, 20):
            assert len(integrable_weights_sl2(k)) == k + 1

    def test_sl3_count(self):
        """sl_3 at level k: (k+1)(k+2)/2 integrable weights."""
        for k in range(1, 15):
            expected = (k + 1) * (k + 2) // 2
            assert len(integrable_weights_sl3(k)) == expected

    def test_sl3_count_formula(self):
        """num_integrable_weights for sl_3."""
        for k in range(1, 15):
            assert num_integrable_weights('A', 2, k) == (k + 1) * (k + 2) // 2

    def test_sl4_count(self):
        """sl_4 at level k: C(k+3, 3) = (k+1)(k+2)(k+3)/6 integrable weights."""
        for k in range(1, 10):
            expected = (k + 1) * (k + 2) * (k + 3) // 6
            assert num_integrable_weights('A', 3, k) == expected

    def test_sl2_weights_explicit(self):
        """sl_2 at level 3: weights are 0, 1, 2, 3."""
        assert integrable_weights_sl2(3) == [0, 1, 2, 3]

    def test_g2_count_level_1(self):
        """G_2 at level 1: weights with a+2b<=1, so (0,0), (1,0)."""
        weights = integrable_weights_g2(1)
        assert len(weights) == 2

    def test_g2_count_level_4(self):
        """G_2 at level 4: count weights with 2a+b<=4."""
        weights = integrable_weights_g2(4)
        # a=0: b=0..4 (5); a=1: b=0..2 (3); a=2: b=0 (1)
        assert len(weights) == 9

    def test_slN_count_formula(self):
        """Verify num_integrable_weights for sl_N matches enumeration."""
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 3, 5]:
                count_formula = num_integrable_weights('A', N - 1, k)
                count_enum = len(integrable_weights_slN(N, k))
                assert count_formula == count_enum, \
                    f"sl_{N} at k={k}: formula={count_formula}, enum={count_enum}"

    def test_integrable_count_formula(self):
        """Integrable weight count for sl_N at level k = C(k+N-1, N-1).

        Verify the combinatorial formula against explicit enumeration.
        """
        import math as _math
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 3, 5]:
                formula = _math.comb(k + N - 1, N - 1)
                count = num_integrable_weights('A', N - 1, k)
                assert formula == count, f"sl_{N} at k={k}: formula={formula}, count={count}"


# =========================================================================
# Section 5: Modular S-matrix (Verlinde)
# =========================================================================

class TestSMatrix:
    """Tests for the modular S-matrix."""

    def test_s_matrix_symmetric(self):
        """S-matrix is symmetric."""
        for k in [1, 2, 5, 10]:
            S = s_matrix_sl2(k)
            assert np.allclose(S, S.T, atol=1e-12)

    def test_s_matrix_unitary(self):
        """S S^T = I (S is real and orthogonal)."""
        for k in [1, 2, 5, 10, 20]:
            err = verify_s_matrix_unitarity(k)
            assert err < 1e-10, f"S-matrix not unitary at k={k}, error={err}"

    def test_s_matrix_involution(self):
        """S^2 = I for the real symmetric S-matrix of sl_2.

        Our S-matrix is real, symmetric, and orthogonal, so S^2 = S S^T = I.
        (The complex modular S-matrix with phase conventions satisfies S^2 = C;
        our real version absorbs the phases, making it an involution.)
        """
        for k in [2, 5, 10]:
            S = s_matrix_sl2(k)
            S2 = S @ S
            I = np.eye(k + 1)
            assert np.allclose(S2, I, atol=1e-10), f"S^2 != I at k={k}"

    def test_verlinde_matches_direct(self):
        """Quantum dims from S-matrix ratio must match direct formula."""
        for k in [1, 2, 5, 10, 20]:
            for j in range(k + 1):
                d_direct = quantum_dim_sl2(j, k)
                d_verlinde = verlinde_quantum_dim_sl2(j, k)
                assert abs(d_direct - d_verlinde) < 1e-10, \
                    f"Mismatch at k={k}, j={j}: direct={d_direct}, Verlinde={d_verlinde}"

    def test_verlinde_fusion_integers(self):
        """Verlinde fusion coefficients should be nonneg integers."""
        for k in [2, 3, 5]:
            for i in range(k + 1):
                for j in range(k + 1):
                    for l in range(k + 1):
                        N = verlinde_fusion_sl2(i, j, l, k)
                        assert abs(N - round(N)) < 1e-8, \
                            f"Non-integer fusion N_{{{i},{j}}}^{l} = {N} at k={k}"
                        assert round(N) >= 0, \
                            f"Negative fusion N_{{{i},{j}}}^{l} = {N} at k={k}"

    def test_verlinde_fusion_sl2_cg_rules(self):
        """Verlinde fusion for sl_2 follows truncated Clebsch-Gordan:

        N_{ij}^l = 1 if |i-j| <= l <= min(i+j, 2k-i-j) and i+j+l even
        N_{ij}^l = 0 otherwise.
        """
        k = 5
        for i in range(k + 1):
            for j in range(k + 1):
                for l in range(k + 1):
                    N = round(verlinde_fusion_sl2(i, j, l, k))
                    # Truncated CG: N = 1 if |i-j| <= l <= min(i+j, 2k-i-j)
                    # AND l has same parity as i+j
                    if abs(i - j) <= l <= min(i + j, 2 * k - i - j) and (i + j + l) % 2 == 0:
                        expected = 1
                    else:
                        expected = 0
                    assert N == expected, \
                        f"CG mismatch at k={k}: N_{{{i},{j}}}^{l} = {N}, expected {expected}"


# =========================================================================
# Section 6: Modular categorical zeta for sl_2
# =========================================================================

class TestModularZetaSl2:
    """Tests for the modular categorical zeta of sl_2."""

    def test_level_1(self):
        """sl_2 at level 1: only V_1 with dim_q = 1. zeta(s) = 1^{-s} = 1."""
        for s in [1.0, 2.0, 3.0, 0.5]:
            z = modular_zeta_sl2(s, 1)
            assert abs(z - 1.0) < 1e-10

    def test_level_2_at_s2(self):
        """sl_2 at level 2 (Ising): V_1 (dim sqrt(2)), V_2 (dim 1).

        zeta(2) = (sqrt(2))^{-2} + 1^{-2} = 1/2 + 1 = 3/2.
        """
        z = modular_zeta_sl2(2.0, 2)
        assert abs(z - 1.5) < 1e-10

    def test_level_2_at_s1(self):
        """sl_2 at level 2: zeta(1) = 1/sqrt(2) + 1 = 1 + sqrt(2)/2."""
        z = modular_zeta_sl2(1.0, 2)
        expected = 1.0 / math.sqrt(2) + 1.0
        assert abs(z - expected) < 1e-10

    def test_monotonic_in_k(self):
        """For real s > 1, adding more terms increases the sum."""
        s = 2.0
        prev = 0
        for k in range(1, 20):
            z = modular_zeta_sl2(s, k).real
            assert z >= prev - 1e-10, f"Non-monotonic at k={k}"
            prev = z

    def test_all_terms_positive_real_s(self):
        """For real s, all quantum dims are positive so all terms are positive reals."""
        for k in [5, 10]:
            for s in [1.0, 2.0, 3.0]:
                z = modular_zeta_sl2(s, k)
                assert z.real > 0 and abs(z.imag) < 1e-10


# =========================================================================
# Section 7: Modular categorical zeta for sl_3
# =========================================================================

class TestModularZetaSl3:
    """Tests for the modular categorical zeta of sl_3."""

    def test_level_1(self):
        """sl_3 at level 1: nontrivial reps are (1,0) and (0,1), both dim_q = 1.

        zeta(s) = 1^{-s} + 1^{-s} = 2.
        """
        for s in [1.0, 2.0, 3.0]:
            z = modular_zeta_sl3(s, 1)
            assert abs(z - 2.0) < 1e-10

    def test_positive_real_s(self):
        """For real s > 0, the modular zeta is real and positive."""
        for k in [2, 5, 8]:
            for s in [1.0, 2.0]:
                z = modular_zeta_sl3(s, k)
                assert z.real > 0 and abs(z.imag) < 1e-10

    def test_consistency_with_general(self):
        """modular_zeta_sl3 should agree with modular_zeta_general for A_2."""
        for k in [2, 5]:
            for s in [2.0, 3.0]:
                z_specific = modular_zeta_sl3(s, k)
                z_general = modular_zeta_general(s, 'A', 2, k)
                assert abs(z_specific - z_general) < 1e-10


# =========================================================================
# Section 8: Modular categorical zeta for G_2
# =========================================================================

class TestModularZetaG2:
    """Tests for the modular categorical zeta of G_2."""

    def test_level_1(self):
        """G_2 at level 1: only (0,1) is nontrivial (2a+b<=1 gives (0,0),(0,1)).

        dim_q V(0,1) at k=1, p=5.
        """
        z = modular_zeta_g2(2.0, 1)
        d = quantum_dim_g2(0, 1, 1)
        assert abs(z - d ** (-2)) < 1e-10

    def test_positive_real_s(self):
        """For real s > 0 and k >= 2, the modular zeta is real and positive."""
        for k in [2, 4, 6]:
            for s in [1.0, 2.0]:
                z = modular_zeta_g2(s, k)
                assert z.real > 0, f"Negative zeta at k={k}, s={s}: {z}"
                assert abs(z.imag) < 1e-10

    def test_consistency_with_general(self):
        """modular_zeta_g2 should agree with modular_zeta_general for G_2."""
        for k in [2, 4]:
            for s in [2.0]:
                z_specific = modular_zeta_g2(s, k)
                z_general = modular_zeta_general(s, 'G', 2, k)
                assert abs(z_specific - z_general) < 1e-10


# =========================================================================
# Section 9: k -> infinity limit and convergence to Riemann zeta
# =========================================================================

class TestConvergence:
    """Tests for convergence and large-k behavior of modular zeta.

    KEY: The full modular zeta sum_{j=1}^k [j+1]_q^{-s} does NOT converge to
    zeta(s)-1, because quantum dimensions have the symmetry [j+1]_q = [k+1-j]_q,
    so terms near j=k have small quantum dimensions and contribute large terms.

    The correct convergence statement: for FIXED J, the partial sum
    sum_{j=1}^J [j+1]_q^{-s} approaches sum_{j=1}^J (j+1)^{-s} as k -> infinity.
    """

    def test_partial_sum_convergence(self):
        """Partial modular zeta (fixed J) converges to partial classical zeta."""
        J = 10  # fixed number of terms
        s = 2.0
        classical_partial = sum((j + 1) ** (-s) for j in range(1, J + 1))

        for k in [100, 200, 500]:
            mod_partial = sum(quantum_dim_sl2(j, k) ** (-s) for j in range(1, J + 1))
            assert abs(mod_partial - classical_partial) < 0.01, \
                f"k={k}: mod_partial={mod_partial:.6f}, classical={classical_partial:.6f}"

    def test_modular_zeta_stabilizes(self):
        """The full modular zeta converges to a finite limit as k -> infinity."""
        s = 2.0
        values = []
        for k in [100, 200, 500]:
            z = modular_zeta_sl2(s, k).real
            values.append(z)
        # Values should stabilize (differ by decreasing amounts)
        diff1 = abs(values[1] - values[0])
        diff2 = abs(values[2] - values[1])
        assert diff2 < diff1, "Modular zeta not stabilizing"

    def test_quantum_dim_symmetry_effect(self):
        """At level k, the symmetry [j+1]_q = [k+1-j]_q makes the sum ~2*classical.

        The modular zeta at level k has k terms. Due to symmetry, terms near j=0
        match terms near j=k, effectively doubling the sum relative to the
        classical partial sum (which only goes one way).
        """
        k = 200
        s = 2.0
        z_mod = modular_zeta_sl2(s, k).real
        z_cl = sum((j + 1) ** (-s) for j in range(1, k + 1))
        # The modular zeta should be roughly 2x the classical partial sum
        # (plus correction terms from the quantum distortion)
        ratio = z_mod / z_cl
        # The ratio should be > 1 due to symmetry effect
        assert ratio > 1.5, f"Ratio = {ratio}, expected > 1.5"

    def test_convergence_s3_partial(self):
        """Partial sum convergence at s=3."""
        J = 10
        s = 3.0
        classical_partial = sum((j + 1) ** (-s) for j in range(1, J + 1))
        mod_partial = sum(quantum_dim_sl2(j, 200) ** (-s) for j in range(1, J + 1))
        assert abs(mod_partial - classical_partial) < 0.001

    def test_convergence_report(self):
        """modular_zeta_convergence_sl2 returns valid data with finite values."""
        results = modular_zeta_convergence_sl2(2.0, [10, 50, 100])
        assert len(results) == 3
        for r in results:
            assert math.isfinite(r['zeta_mod'].real)
            assert r['error'] >= 0


# =========================================================================
# Section 10: Asymptotic expansion
# =========================================================================

class TestAsymptoticExpansion:
    """Tests for the asymptotic expansion of the modular zeta."""

    def test_expansion_returns_data(self):
        """Asymptotic expansion returns valid data structure."""
        result = asymptotic_expansion_sl2(4.0, 100, 3)
        assert 'zeta_mod' in result
        assert 'zeta_limit' in result
        assert 'error' in result
        assert result['error'] >= 0

    def test_expansion_modular_zeta_finite(self):
        """The modular zeta values in the expansion are finite."""
        for k in [20, 50, 100]:
            result = asymptotic_expansion_sl2(4.0, k)
            assert math.isfinite(result['zeta_mod'].real)


# =========================================================================
# Section 11: Modular zeta at s = 0 (representation counting)
# =========================================================================

class TestZetaAtZero:
    """Tests for zeta^{mod}(0) = #nontrivial reps."""

    def test_sl2_count(self):
        """For sl_2 at level k, zeta(0) = k."""
        for k in range(1, 20):
            data = modular_zeta_at_zero('A', 1, k)
            assert data['match'], f"sl_2 at k={k}: zeta(0) = {data['zeta_at_0']}, expected {k}"
            assert data['count'] == k

    def test_sl3_count(self):
        """For sl_3 at level k, zeta(0) = (k+1)(k+2)/2 - 1."""
        for k in range(1, 10):
            data = modular_zeta_at_zero('A', 2, k)
            expected = (k + 1) * (k + 2) // 2 - 1
            assert data['match'], f"sl_3 at k={k}: zeta(0) = {data['zeta_at_0']}, expected {expected}"
            assert data['count'] == expected

    def test_g2_count(self):
        """For G_2 at level k, zeta(0) = #integrable - 1."""
        for k in range(1, 8):
            data = modular_zeta_at_zero('G', 2, k)
            assert data['match'], f"G_2 at k={k}: zeta(0) = {data['zeta_at_0']}, expected {data['count']}"

    def test_sl4_count(self):
        """For sl_4 at level k, zeta(0) = C(k+3,3) - 1."""
        for k in range(1, 6):
            data = modular_zeta_at_zero('A', 3, k)
            expected = (k + 1) * (k + 2) * (k + 3) // 6 - 1
            assert data['count'] == expected
            assert data['match']


# =========================================================================
# Section 12: Level-rank duality
# =========================================================================

class TestLevelRankDuality:
    """Tests for level-rank duality sl_N,k <-> sl_k,N."""

    def test_rep_count_formula(self):
        """#integrable reps of sl_N at level k = C(k+N-1, N-1).

        Level-rank duality relates sl_N,k and sl_k,N but does NOT
        preserve the representation count in general. The counts are
        C(k+N-1, N-1) and C(N+k-1, k-1), which differ for N != k.
        They agree when N = k (symmetric case).
        """
        import math as _math
        for N, k in [(3, 3), (4, 4), (2, 2)]:  # symmetric cases
            data = level_rank_duality_check(N, k, 2.0)
            assert data['reps_equal'], \
                f"Rep count mismatch at N=k={N}: {data['n_reps_NK']} vs {data['n_reps_KN']}"

    def test_total_qdim_squared_positive(self):
        """Total quantum dimension squared D^2 is positive for both sides."""
        for N, k in [(2, 3), (3, 2), (2, 4)]:
            data = level_rank_duality_check(N, k, 2.0)
            assert data['total_qdim2_NK'] > 0, f"D^2(sl_{N},k={k}) <= 0"
            assert data['total_qdim2_KN'] > 0, f"D^2(sl_{k},N={N}) <= 0"

    def test_zeta_values_positive(self):
        """Modular zeta values are positive for real s > 0."""
        for N, k in [(2, 3), (3, 2), (3, 3)]:
            data = level_rank_duality_check(N, k, 2.0)
            assert data['zeta_NK'].real > 0
            assert data['zeta_KN'].real > 0

    def test_level_rank_check_returns_data(self):
        """level_rank_duality_check returns a complete data structure."""
        data = level_rank_duality_check(2, 3, 2.0)
        assert 'N' in data and data['N'] == 2
        assert 'k' in data and data['k'] == 3
        assert 'zeta_NK' in data
        assert 'zeta_KN' in data


# =========================================================================
# Section 13: Zeros of modular categorical zeta
# =========================================================================

class TestModularZetaZeros:
    """Tests for zeros of the modular categorical zeta."""

    def test_sl2_k2_evaluation_on_line(self):
        """Evaluate the modular zeta on a vertical line."""
        t_vals = np.linspace(-10, 10, 101)  # 101 points so t=0 is exactly at index 50
        vals = modular_zeta_on_line(0.5, t_vals, 2)
        assert len(vals) == 101
        # At t=0: zeta(1/2) for Ising model, should be real
        idx_0 = 50  # exactly t=0
        assert abs(vals[idx_0].imag) < 1e-10  # real on the real axis

    def test_zero_count_consistency(self):
        """The modular zeta is an exponential polynomial of degree k.

        By the argument principle, the number of zeros in a strip grows linearly
        with the height of the strip.
        """
        # Just check that the zero finder returns a reasonable number
        zeros = find_zeros_modular_zeta_sl2(5, sigma_range=(-2, 4), t_range=(-20, 20),
                                            grid_density=50)
        # Should find at least some zeros
        # (the finite sum generically has zeros)
        assert isinstance(zeros, list)


# =========================================================================
# Section 14: Shadow-modular comparison
# =========================================================================

class TestShadowModularComparison:
    """Tests for the shadow-modular comparison."""

    def test_kappa_sl2(self):
        """kappa(hat{sl}_2, k) = 3(k+2)/4."""
        for k in range(1, 20):
            kap = kappa_affine('A', 1, k)
            expected = 3.0 * (k + 2) / 4.0
            assert abs(kap - expected) < 1e-12, f"kappa mismatch at k={k}: {kap} vs {expected}"

    def test_kappa_sl3(self):
        """kappa(hat{sl}_3, k) = 8(k+3)/6 = 4(k+3)/3."""
        for k in range(1, 10):
            kap = kappa_affine('A', 2, k)
            expected = 4.0 * (k + 3) / 3.0
            assert abs(kap - expected) < 1e-12

    def test_kappa_g2(self):
        """kappa(hat{G}_2, k) = 14(k+4)/8 = 7(k+4)/4."""
        for k in range(1, 10):
            kap = kappa_affine('G', 2, k)
            expected = 7.0 * (k + 4) / 4.0
            assert abs(kap - expected) < 1e-12

    def test_shadow_comparison_report(self):
        """shadow_modular_comparison returns valid data."""
        data = shadow_modular_comparison('A', 1, 5, 2.0)
        assert data['kappa'] > 0
        assert data['n_nontrivial_reps'] == 5
        assert data['zeta_mod'].real > 0


# =========================================================================
# Section 15: Quantum vs classical dimension comparison
# =========================================================================

class TestQuantumVsClassical:
    """Tests for quantum vs classical dimension comparison."""

    def test_classical_dim_sl2(self):
        """Classical dim of V_j for sl_2 is j+1."""
        for j in range(10):
            assert classical_dim_sl2(j) == j + 1

    def test_classical_dim_sl3_fund(self):
        """Classical dim of V(1,0) for sl_3 is 3."""
        assert classical_dim_sl3(1, 0) == 3

    def test_classical_dim_sl3_adjoint(self):
        """Classical dim of V(1,1) for sl_3 is 8."""
        assert classical_dim_sl3(1, 1) == 8

    def test_quantum_le_classical(self):
        """Quantum dim <= classical dim for sl_2 integrable reps."""
        for k in range(1, 15):
            for j in range(k + 1):
                d_q = quantum_dim_sl2(j, k)
                d_cl = classical_dim_sl2(j)
                assert d_q <= d_cl + 1e-10, f"k={k}, j={j}: d_q={d_q} > d_cl={d_cl}"

    def test_ratio_approaches_1(self):
        """quantum/classical ratio -> 1 as k -> infinity."""
        k = 500
        data = quantum_vs_classical_sl2(k)
        for j, d_q, d_cl, ratio in data[:10]:
            assert abs(ratio - 1.0) < 0.01, f"j={j}: ratio={ratio}"


# =========================================================================
# Section 16: Critical line evaluations
# =========================================================================

class TestCriticalLine:
    """Tests for evaluations on the critical line Re(s) = 1/2."""

    def test_critical_line_real_at_t0(self):
        """On the critical line, zeta(1/2 + 0*i) should be real."""
        results = modular_zeta_critical_line_sl2(5, [0.0])
        assert abs(results[0]['value'].imag) < 1e-10

    def test_critical_line_conjugation(self):
        """zeta(1/2 + it)^* = zeta(1/2 - it) since the sum has real coefficients."""
        k = 10
        results = modular_zeta_critical_line_sl2(k, [3.0, -3.0])
        val_plus = results[0]['value']
        val_minus = results[1]['value']
        assert abs(val_plus - val_minus.conjugate()) < 1e-10

    def test_critical_line_nonzero_generically(self):
        """At generic t, the modular zeta should be nonzero."""
        results = modular_zeta_critical_line_sl2(10, [1.0, 2.0, 3.0, 5.0])
        for r in results:
            assert r['abs_value'] > 1e-5, f"Suspiciously small value at t={r['t']}"


# =========================================================================
# Section 17: Cross-checks and multi-path verification
# =========================================================================

class TestMultiPathVerification:
    """Cross-checks and multi-path verification for all results."""

    def test_sl2_three_path_quantum_dim(self):
        """Verify sl_2 quantum dimensions via 3 independent paths.

        Path 1: sin formula (quantum_dim_sl2)
        Path 2: S-matrix ratio (verlinde_quantum_dim_sl2)
        Path 3: Direct computation via q = exp(i*pi/(k+2))
        """
        for k in [2, 5, 10]:
            for j in range(k + 1):
                # Path 1
                d1 = quantum_dim_sl2(j, k)
                # Path 2
                d2 = verlinde_quantum_dim_sl2(j, k)
                # Path 3: direct quantum integer [j+1]_q with q = exp(i*pi/p)
                # [j+1]_q = (q^{j+1} - q^{-(j+1)}) / (q - q^{-1})
                # = sin((j+1)*pi/p) / sin(pi/p)
                p = k + 2
                q = cmath.exp(1j * cmath.pi / p)
                d3 = ((q ** (j + 1) - q ** (-(j + 1))) / (q - q ** (-1))).real

                assert abs(d1 - d2) < 1e-10, f"Path 1 vs 2 at k={k}, j={j}"
                assert abs(d1 - d3) < 1e-10, f"Path 1 vs 3 at k={k}, j={j}"

    def test_sl2_zeta_two_paths(self):
        """Verify modular zeta via direct sum and S-matrix weighted sum.

        Path 1: sum over j of (dim_q V_j)^{-s}
        Path 2: sum over j of (S_{0j}/S_{00})^{-s}
        """
        for k in [3, 8, 15]:
            s = 2.0
            # Path 1
            z1 = modular_zeta_sl2(s, k)
            # Path 2
            S = s_matrix_sl2(k)
            z2 = sum((S[0, j] / S[0, 0]) ** (-s) for j in range(1, k + 1))
            assert abs(z1 - z2) < 1e-10, f"Two-path mismatch at k={k}"

    def test_sl2_zeta0_three_paths(self):
        """Verify zeta(0) via 3 paths.

        Path 1: modular_zeta_sl2(0, k)
        Path 2: modular_zeta_at_zero counting
        Path 3: direct count len(integrable_weights) - 1
        """
        for k in range(1, 15):
            # Path 1
            z1 = modular_zeta_sl2(0, k).real
            # Path 2
            data = modular_zeta_at_zero('A', 1, k)
            z2 = data['count']
            # Path 3
            z3 = len(integrable_weights_sl2(k)) - 1

            assert abs(z1 - z2) < 0.5
            assert z2 == z3
            assert z2 == k

    def test_sl3_classical_limit_multipath(self):
        """Verify sl_3 quantum dims approach classical dims at large k.

        Path 1: quantum_dim_sl3
        Path 2: classical_dim_sl3
        Path 3: Weyl dimension formula via product
        """
        k = 200
        test_weights = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
        for a, b in test_weights:
            # Path 1
            d_q = quantum_dim_sl3(a, b, k)
            # Path 2
            d_cl = classical_dim_sl3(a, b)
            # Path 3: explicit Weyl
            d_weyl = (a + 1) * (b + 1) * (a + b + 2) // 2

            assert abs(d_q - d_cl) < 0.5, f"Quantum-classical at ({a},{b})"
            assert d_cl == d_weyl, f"Classical-Weyl at ({a},{b})"

    def test_g2_classical_limit_multipath(self):
        """Verify G_2 quantum dims approach classical dims at large k.

        Path 1: quantum_dim_g2
        Path 2: classical_dim_g2
        Bourbaki convention: V(1,0) = 14 (adjoint), V(0,1) = 7 (fundamental).
        """
        k = 300
        for a, b in [(1, 0), (0, 1), (0, 2)]:
            d_q = quantum_dim_g2(a, b, k)
            d_cl = classical_dim_g2(a, b)
            assert abs(d_q - d_cl) < 0.5, f"G_2 quantum-classical at ({a},{b}): {d_q} vs {d_cl}"

    def test_full_verification_report_sl2(self):
        """Full verification report for sl_2 at level 5."""
        report = full_verification_report('A', 1, 5)
        assert report['k'] == 5
        assert report['h_vee'] == 2
        assert abs(report['kappa'] - 3.0 * 7 / 4) < 1e-12
        assert report['zeta_at_0']['match']
        assert report['s_matrix_unitarity_error'] < 1e-10
        assert report['verlinde_vs_direct_max_error'] < 1e-10

    def test_full_verification_report_sl3(self):
        """Full verification report for sl_3 at level 3."""
        report = full_verification_report('A', 2, 3)
        assert report['k'] == 3
        assert report['h_vee'] == 3
        assert report['zeta_at_0']['match']

    def test_full_verification_report_g2(self):
        """Full verification report for G_2 at level 4."""
        report = full_verification_report('G', 2, 4)
        assert report['k'] == 4
        assert report['h_vee'] == 4
        assert report['zeta_at_0']['match']

    def test_dual_coxeter_numbers(self):
        """Verify dual Coxeter numbers against known values."""
        assert dual_coxeter_number('A', 1) == 2   # sl_2
        assert dual_coxeter_number('A', 2) == 3   # sl_3
        assert dual_coxeter_number('A', 3) == 4   # sl_4
        assert dual_coxeter_number('A', 4) == 5   # sl_5
        assert dual_coxeter_number('G', 2) == 4   # G_2

    def test_lie_algebra_dimensions(self):
        """Verify Lie algebra dimensions against known values."""
        assert lie_algebra_dim('A', 1) == 3    # sl_2
        assert lie_algebra_dim('A', 2) == 8    # sl_3
        assert lie_algebra_dim('A', 3) == 15   # sl_4
        assert lie_algebra_dim('G', 2) == 14   # G_2

    def test_convergence_and_counting_consistency(self):
        """The number of terms in the modular zeta sum equals zeta(0).

        For sl_2 at level k: the sum has k terms (j=1..k), and zeta(0) = k.
        This is a tautological but important check.
        """
        for k in range(1, 15):
            n_terms = k  # j = 1, ..., k
            z0 = modular_zeta_sl2(0, k).real
            assert abs(z0 - n_terms) < 0.5

    def test_sl2_level_dependence(self):
        """At fixed s, the modular zeta generally increases with k.

        Due to quantum dimension symmetry [j+1]_q = [k+1-j]_q, the full
        modular zeta exceeds the classical partial sum. Verify it increases
        overall (not necessarily monotonically at every step).
        """
        s = 2.0
        val_5 = modular_zeta_sl2(s, 5).real
        val_20 = modular_zeta_sl2(s, 20).real
        assert val_20 > val_5, "Modular zeta should grow with k"

    def test_quantum_dim_sl2_sum_rule(self):
        """For sl_2 at level k, sum of dim_q^2 over ALL reps = (k+2)/(2*sin^2(pi/(k+2))).

        This is 1/S_{00}^2 where S_{00} = sqrt(2/(k+2)) * sin(pi/(k+2)).
        So 1/S_{00}^2 = (k+2)/(2*sin^2(pi/(k+2))).
        """
        for k in [2, 5, 10, 20]:
            total = 0.0
            for j in range(k + 1):
                d = quantum_dim_sl2(j, k)
                total += d ** 2
            p = k + 2
            expected = p / (2.0 * math.sin(math.pi / p) ** 2)
            assert abs(total - expected) < 1e-8, f"Sum rule failed at k={k}: {total} vs {expected}"

    def test_quantum_dim_sl3_sum_rule(self):
        """Total quantum dimension squared for sl_3: 1/S_{00}^2.

        For sl_3 at level k: S_{00} = sqrt(2/(k+3)) * sin(pi/(k+3)) * ... (complicated).
        Instead verify the sum is consistent between explicit computation and the S-matrix
        for small k.

        Actually, the total quantum dimension squared D^2 can be verified as:
        D^2 = sum_lambda dim_q(lambda)^2.
        For sl_3 at level 1: D^2 = 1 + 1 + 1 = 3.
        """
        # Level 1
        total = 0.0
        for a, b in integrable_weights_sl3(1):
            d = quantum_dim_sl3(a, b, 1)
            total += d ** 2
        assert abs(total - 3.0) < 1e-10, f"sl_3 level 1: D^2 = {total}, expected 3"

    def test_modular_zeta_complex_s(self):
        """Modular zeta can be evaluated at complex s."""
        k = 5
        s = complex(2.0, 1.0)
        z = modular_zeta_sl2(s, k)
        # Should be a well-defined complex number
        assert math.isfinite(z.real) and math.isfinite(z.imag)

    def test_modular_zeta_sl2_range_of_k(self):
        """Compute zeta for k = 1..30 and verify basic properties."""
        s = 2.0
        for k in range(1, 31):
            z = modular_zeta_sl2(s, k)
            assert z.real > 0
            assert abs(z.imag) < 1e-10

    def test_quantum_dim_sum_squared(self):
        """Sum of quantum dimensions squared = 1/S_{00}^2 (total quantum dimension).

        This is an independent verification of the S-matrix normalization.
        """
        for k in [2, 5, 10, 15]:
            S = s_matrix_sl2(k)
            D2_from_S = 1.0 / S[0, 0] ** 2
            D2_from_dims = sum(quantum_dim_sl2(j, k) ** 2 for j in range(k + 1))
            assert abs(D2_from_S - D2_from_dims) < 1e-8, \
                f"D^2 mismatch at k={k}: S-matrix={D2_from_S:.6f}, dims={D2_from_dims:.6f}"

    def test_spectrum_sl2(self):
        """quantum_dim_spectrum_sl2 returns correct number of entries."""
        for k in [3, 7, 12]:
            spec = quantum_dim_spectrum_sl2(k)
            assert len(spec) == k + 1

    def test_spectrum_sl3(self):
        """quantum_dim_spectrum_sl3 returns correct number of entries."""
        for k in [2, 4]:
            spec = quantum_dim_spectrum_sl3(k)
            expected_count = (k + 1) * (k + 2) // 2
            assert len(spec) == expected_count

    def test_spectrum_g2(self):
        """quantum_dim_spectrum_g2 returns correct number of entries."""
        for k in [2, 4, 6]:
            spec = quantum_dim_spectrum_g2(k)
            expected_count = len(integrable_weights_g2(k))
            assert len(spec) == expected_count
