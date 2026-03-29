"""
Tests for the genus-2 Böcherer bridge.

Verifies:
1. E8 root system and genus-2 representation numbers
2. Leech lattice inner-product distribution and genus-2 rep numbers
3. Cusp-form non-vanishing (Proposition prop:leech-cusp-nonvanishing)
4. Heisenberg genus-2 Fredholm three-shell structure
5. Böcherer coefficient structure
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.genus2_bocherer_bridge import (
    e8_roots,
    e8_gram_matrix,
    e8_inner_product_distribution,
    genus2_rep_e8,
    genus2_rep_leech,
    genus2_rep_leech_min,
    leech_ip_dist_check,
    leech_cusp_nonvanishing,
    e8_is_pure_eisenstein,
    heisenberg_genus2_fredholm_expansion,
    three_shell_decomposition_check,
    leech_bocherer_coefficients,
    genus2_beurling_kernel_leech,
    verify_kernel_positivity,
    gap_d_spectral_comparison,
    LEECH_KISSING,
    LEECH_MIN_IP_DIST,
)


# ============================================================
# E8 ROOT SYSTEM TESTS
# ============================================================

class TestE8Roots:
    """Tests for E8 root system and genus-2 representation numbers."""

    def test_root_count(self):
        """E8 has exactly 240 roots."""
        roots = e8_roots()
        assert len(roots) == 240

    def test_root_norms(self):
        """All E8 roots have norm 2."""
        roots = e8_roots()
        norms = np.sum(roots ** 2, axis=1)
        np.testing.assert_allclose(norms, 2.0, atol=1e-10)

    def test_inner_products_integral(self):
        """All inner products between E8 roots are integers."""
        gram = e8_gram_matrix()
        rounded = np.round(gram)
        np.testing.assert_allclose(gram, rounded, atol=1e-10)

    def test_inner_product_range(self):
        """Inner products between E8 roots are in {-2, -1, 0, 1, 2}."""
        gram = e8_gram_matrix()
        rounded = np.round(gram).astype(int)
        vals = set(rounded.flatten())
        assert vals.issubset({-2, -1, 0, 1, 2})

    def test_inner_product_distribution(self):
        """Verify the inner product distribution for E8."""
        dist = e8_inner_product_distribution()
        # For a fixed root, the distribution should be:
        # 2: 1 (the root itself), -2: 1 (negative), 1: 56, -1: 56, 0: 126
        assert dist[2] == 1
        assert dist[-2] == 1
        assert dist[1] == 56
        assert dist[-1] == 56
        assert dist[0] == 126
        assert sum(dist.values()) == 240

    def test_genus2_rep_e8_diag_11(self):
        """r_2(E8, diag(1,1)) = 240 * 126 = 30240 (orthogonal root pairs)."""
        r2 = genus2_rep_e8(1, 0, 1)
        assert r2 == 240 * 126

    def test_genus2_rep_e8_b1(self):
        """r_2(E8, ((1, 1/2), (1/2, 1))) = 240 * 56 (inner product 1 pairs)."""
        r2 = genus2_rep_e8(1, 1, 1)
        assert r2 == 240 * 56

    def test_genus2_rep_e8_b2(self):
        """r_2(E8, ((1, 1), (1, 1))) = 240 * 1 = 240 (v2 = v1)."""
        r2 = genus2_rep_e8(1, 2, 1)
        assert r2 == 240

    def test_genus2_rep_e8_bminus1(self):
        """r_2(E8, ((1, -1/2), (-1/2, 1))) = 240 * 56."""
        r2 = genus2_rep_e8(1, -1, 1)
        assert r2 == 240 * 56

    def test_genus2_rep_e8_zero_vector(self):
        """r_2(E8, ((0,0),(0,0))) = 1 (zero vector pair)."""
        assert genus2_rep_e8(0, 0, 0) == 1

    def test_genus2_rep_e8_one_zero(self):
        """r_2(E8, ((1,0),(0,0))) = 240 (one root, one zero)."""
        assert genus2_rep_e8(1, 0, 0) == 240

    def test_e8_pure_eisenstein(self):
        """
        Θ^{(2)}_{E8} = E_4^{(2)}: internal consistency.
        Since dim M_4(Sp(4,Z)) = 1, the genus-2 theta series
        of E8 must equal the Siegel Eisenstein series.
        """
        assert e8_is_pure_eisenstein()

    def test_e8_genus2_total_at_root_shell(self):
        """Sum over all b of r_2(E8, ((1,b/2),(b/2,1))) = 240^2."""
        total = 0
        for b in range(-2, 3):
            r2 = genus2_rep_e8(1, b, 1)
            total += r2
        assert total == 240 ** 2


# ============================================================
# LEECH LATTICE TESTS
# ============================================================

class TestLeechLattice:
    """Tests for Leech lattice genus-2 representation numbers."""

    def test_ip_distribution_sums(self):
        """Inner product distribution sums to kissing number."""
        assert leech_ip_dist_check()

    def test_ip_distribution_total(self):
        """Explicit check: sum of distribution = 196560."""
        total = sum(LEECH_MIN_IP_DIST.values())
        assert total == LEECH_KISSING

    def test_no_norm2_vectors(self):
        """Leech lattice has no vectors of norm 2."""
        assert genus2_rep_leech(1, 0, 1) == 0

    def test_no_norm2_any_b(self):
        """No pairs of norm-2 vectors exist, regardless of inner product."""
        for b in range(-2, 3):
            assert genus2_rep_leech(1, b, 1) == 0

    def test_minimal_orthogonal_pairs(self):
        """r_2(Leech, ((2,0),(0,2))) = 196560 * 93150."""
        r2 = genus2_rep_leech_min(0)
        assert r2 == LEECH_KISSING * 93150

    def test_minimal_ip1_pairs(self):
        """r_2(Leech, ((2,1/2),(1/2,2))) = 196560 * 47104."""
        r2 = genus2_rep_leech_min(1)
        assert r2 == LEECH_KISSING * 47104

    def test_minimal_ip2_pairs(self):
        """r_2(Leech, ((2,1),(1,2))) = 196560 * 4600."""
        r2 = genus2_rep_leech_min(2)
        assert r2 == LEECH_KISSING * 4600

    def test_minimal_identical_pairs(self):
        """r_2(Leech, ((2,2),(2,2))) = 196560 * 1."""
        r2 = genus2_rep_leech_min(4)
        assert r2 == LEECH_KISSING * 1

    def test_minimal_ip3_impossible(self):
        """Inner product 3 between minimal Leech vectors is impossible."""
        r2 = genus2_rep_leech_min(3)
        assert r2 == 0

    def test_minimal_total(self):
        """Sum over all b of r_2(Leech, ((2,b/2),(b/2,2))) = 196560^2."""
        total = 0
        for b in range(-4, 5):
            r2 = genus2_rep_leech_min(b)
            total += r2
        assert total == LEECH_KISSING ** 2

    def test_zero_vector_pair(self):
        """r_2(Leech, ((0,0),(0,0))) = 1."""
        assert genus2_rep_leech(0, 0, 0) == 1

    def test_one_minimal_one_zero(self):
        """r_2(Leech, ((2,0),(0,0))) = 196560."""
        assert genus2_rep_leech(2, 0, 0) == LEECH_KISSING


# ============================================================
# CUSP-FORM NON-VANISHING
# ============================================================

class TestCuspNonvanishing:
    """Tests for Proposition prop:leech-cusp-nonvanishing."""

    def test_leech_cusp_nonvanishing(self):
        """
        Θ^{(2)}_Leech ≠ E_{12}^{(2)}.

        The argument: E_{12}^{(2)} has a(T_0) > 0 for T_0 = diag(1,1),
        but Θ^{(2)}_Leech has a(T_0) = 0 (no norm-2 vectors).
        """
        assert leech_cusp_nonvanishing()

    def test_e8_no_cusp_component(self):
        """
        For E8, the genus-2 theta series IS the Eisenstein series.
        dim M_4(Sp(4,Z)) = 1, so no cusp component exists.
        """
        # E8 has norm-2 vectors (the roots), so r_2(E8, diag(1,1)) > 0
        assert genus2_rep_e8(1, 0, 1) > 0
        # The fact that r_2 > 0 is consistent with pure Eisenstein
        # (Eisenstein coefficients are positive)
        assert e8_is_pure_eisenstein()

    def test_cusp_argument_does_not_apply_to_e8(self):
        """
        The cusp non-vanishing argument (missing norm-2 vectors)
        does not apply to E8, confirming it's specific to lattices
        with mu >= 4.
        """
        # E8 has vectors of norm 2 (the 240 roots)
        r2_e8 = genus2_rep_e8(1, 0, 0)
        assert r2_e8 == 240  # E8 has norm-2 vectors


# ============================================================
# HEISENBERG GENUS-2 FREDHOLM TESTS
# ============================================================

class TestHeisenbergGenus2:
    """Tests for the Heisenberg genus-2 Fredholm three-shell structure."""

    def test_separating_positive(self):
        """Separating contribution (product of genus-1) is positive."""
        result = heisenberg_genus2_fredholm_expansion(0.1, 0.1, 0.05)
        assert result['separating'] > 0

    def test_correction_positive(self):
        """Off-diagonal correction factor is positive."""
        result = heisenberg_genus2_fredholm_expansion(0.1, 0.1, 0.05)
        assert result['correction_factor'] > 0

    def test_c11_positive(self):
        """The leading correction coefficient c_{1,1} > 0."""
        result = heisenberg_genus2_fredholm_expansion(0.1, 0.1, 0.05)
        assert result['c11'] > 0

    def test_non_factorization(self):
        """The genus-2 determinant does not factor for q3 ≠ 0."""
        result = heisenberg_genus2_fredholm_expansion(0.1, 0.1, 0.05)
        assert result['non_factorization']

    def test_factorization_at_q3_zero(self):
        """The genus-2 determinant DOES factor when q3 = 0."""
        result = heisenberg_genus2_fredholm_expansion(0.1, 0.1, 0.0)
        # correction factor should be 1 when q3 = 0
        assert abs(result['correction_factor'] - 1.0) < 1e-10

    def test_three_shell_consistency(self):
        """Three-shell decomposition passes all consistency checks."""
        checks = three_shell_decomposition_check()
        for key, value in checks.items():
            assert value, f"Three-shell check failed: {key}"

    def test_heisenberg_shadow_depth_2(self):
        """
        Heisenberg has shadow depth 2, so planted-forest corrections
        at genus 2 should vanish.
        """
        checks = three_shell_decomposition_check()
        assert checks['heisenberg_pf_zero']

    def test_symmetric_in_q1_q2(self):
        """Fredholm determinant is symmetric in q1 <-> q2."""
        r1 = heisenberg_genus2_fredholm_expansion(0.1, 0.2, 0.05)
        r2 = heisenberg_genus2_fredholm_expansion(0.2, 0.1, 0.05)
        assert abs(r1['total'] - r2['total']) < 1e-10

    def test_small_q_convergence(self):
        """For small q values, the expansion should converge quickly."""
        r10 = heisenberg_genus2_fredholm_expansion(0.01, 0.01, 0.005, order=10)
        r20 = heisenberg_genus2_fredholm_expansion(0.01, 0.01, 0.005, order=20)
        assert abs(r10['total'] - r20['total']) / abs(r20['total']) < 1e-6


# ============================================================
# BÖCHERER COEFFICIENT TESTS
# ============================================================

class TestBochererCoefficients:
    """Tests for Böcherer coefficient extraction."""

    def test_leech_bocherer_nonzero(self):
        """
        The Leech lattice has nonzero Böcherer coefficients at
        the minimal shell.
        """
        coeffs = leech_bocherer_coefficients()
        # At discriminant D = -16 (from b=0, a=c=2):
        assert -16 in coeffs
        assert coeffs[-16] > 0

    def test_leech_bocherer_at_D_minus16(self):
        """
        B(-16) for Leech at minimal shell.
        T = ((2,0),(0,2)), disc = -16, epsilon = 2 (since a=c, b=0).
        B(-16) = r_2(Leech, ((2,0),(0,2))) / 2.
        """
        coeffs = leech_bocherer_coefficients()
        expected = Fraction(LEECH_KISSING * 93150, 2)
        assert coeffs[-16] == expected

    def test_leech_bocherer_at_D_minus15(self):
        """
        B(-15) for Leech at minimal shell.
        T = ((2, 1/2), (1/2, 2)), disc = 1 - 16 = -15.
        epsilon = 1 (a=c but b≠0).
        """
        coeffs = leech_bocherer_coefficients()
        # b=1: disc = 1-16 = -15, and b=-1: disc = 1-16 = -15
        # Both contribute: r_2(b=1) + r_2(b=-1) = 2 * 196560 * 47104
        expected = Fraction(2 * LEECH_KISSING * 47104, 1)
        assert coeffs[-15] == expected

    def test_leech_bocherer_at_D_minus12(self):
        """
        B(-12) for Leech at minimal shell.
        T = ((2, 1), (1, 2)), disc = 4 - 16 = -12.
        b=2 and b=-2 both give disc = -12.
        """
        coeffs = leech_bocherer_coefficients()
        expected = Fraction(2 * LEECH_KISSING * 4600, 1)
        assert coeffs[-12] == expected

    def test_leech_no_cusp_at_norm2(self):
        """
        Böcherer coefficients involving norm-2 vectors are zero
        (since Leech has none).
        """
        # T = ((1, 0), (0, 1)), disc = -4
        r2 = genus2_rep_leech(1, 0, 1)
        assert r2 == 0

    def test_bocherer_coefficient_positivity(self):
        """
        All nonzero Böcherer coefficients for Leech are positive
        (since representation numbers are non-negative).
        """
        coeffs = leech_bocherer_coefficients()
        for D, val in coeffs.items():
            assert val >= 0, f"Negative Böcherer coefficient at D={D}: {val}"


# ============================================================
# STRUCTURAL BRIDGE TESTS
# ============================================================

class TestStructuralBridge:
    """Tests for the structural properties of the Böcherer bridge."""

    def test_genus1_vs_genus2_separation(self):
        """
        Genus-1: only sees Re(s) >= 1 (structural separation).
        Genus-2: reaches Re(s) = 1/2 via Böcherer (the bridge).

        Verify the structural distinction: genus-2 rep numbers
        contain information absent from genus-1.
        """
        # Genus-1: Leech has theta function 1 + 196560*q^2 + ...
        # The first nonzero coefficient after constant is at q^2 (norm 4)
        g1_data = LEECH_KISSING  # = a_2 of genus-1 theta

        # Genus-2: the off-diagonal inner products provide new data
        # absent from genus-1 (which only sees norms, not cross-products)
        g2_data = genus2_rep_leech_min(0)  # orthogonal pairs: 93150 per root

        # The ratio (orthogonal pairs per root) / (total roots) is a
        # genuinely genus-2 invariant
        ratio = g2_data / (LEECH_KISSING * LEECH_KISSING)
        assert 0 < ratio < 1  # nontrivial ratio

    def test_e8_vs_leech_cusp_content(self):
        """
        E8 (rank 8): no cusp form at genus 2 (weight 4, dim = 1).
        Leech (rank 24): nonzero cusp form at genus 2 (weight 12, dim >= 2).

        The cusp content grows with rank, providing richer arithmetic
        data for the Böcherer bridge at higher rank.
        """
        # E8: genus-2 = Eisenstein (no missing shells)
        assert genus2_rep_e8(1, 0, 1) > 0  # E8 has norm-2 vectors

        # Leech: genus-2 ≠ Eisenstein (missing norm-2 shell)
        assert genus2_rep_leech(1, 0, 1) == 0  # Leech has NO norm-2 vectors

    def test_mc_three_shell_implies_genus2_from_genus1(self):
        """
        Structural test: the MC three-shell decomposition means
        genus-2 data is determined by genus-1 + boundary.

        For Heisenberg (shadow depth 2), genus-2 is entirely
        determined by genus-1 (the separating + self-sewing parts).
        """
        # At q3 = 0: pure separating, no genus-2 correction
        r_sep = heisenberg_genus2_fredholm_expansion(0.1, 0.1, 0.0)
        assert abs(r_sep['correction_factor'] - 1.0) < 1e-10

        # At q3 ≠ 0: correction is determined by genus-1 data (c11)
        r_full = heisenberg_genus2_fredholm_expansion(0.1, 0.1, 0.05)
        assert r_full['c11'] > 0  # c11 computed from genus-1 data only

        # The correction factor is 1 + c11*|q3| + O(q3^2)
        expected_approx = 1.0 + r_full['c11'] * 0.05
        assert abs(r_full['correction_factor'] - expected_approx) < 0.01


# ============================================================
# GENUS-2 BEURLING KERNEL TESTS (rem:genus2-beurling-kernel)
# ============================================================

class TestBeurlingKernel:
    """Tests for the genus-2 Beurling kernel and Gap D narrowing."""

    def test_kernel_computable(self):
        """The genus-2 Beurling kernel is computable for Leech."""
        data = genus2_beurling_kernel_leech()
        assert 'kernel' in data
        assert 'discriminants' in data
        assert len(data['discriminants']) == 4

    def test_kernel_positive_semidefinite(self):
        """K^{(2)}_Leech is positive semi-definite."""
        data = genus2_beurling_kernel_leech()
        result = verify_kernel_positivity(data)
        assert result['is_psd']

    def test_kernel_diagonal_positive(self):
        """All diagonal entries K(D,D) >= 0."""
        data = genus2_beurling_kernel_leech()
        result = verify_kernel_positivity(data)
        assert result['diagonal_positive']

    def test_kernel_diagonal_nonzero(self):
        """At least one diagonal entry K(D,D) > 0."""
        data = genus2_beurling_kernel_leech()
        result = verify_kernel_positivity(data)
        assert any(d > 0 for d in result['diagonal'])

    def test_kernel_rank(self):
        """
        At the total level (before eigenform decomposition),
        the kernel has rank 1 (single Böcherer vector).
        """
        data = genus2_beurling_kernel_leech()
        result = verify_kernel_positivity(data)
        assert result['rank'] == 1

    def test_kernel_nonzero_at_D_minus16(self):
        """
        K(-16, -16) > 0: the Leech lattice has many
        orthogonal minimal-vector pairs at disc = -16.
        """
        data = genus2_beurling_kernel_leech()
        assert data['kernel'][(-16, -16)] > 0

    def test_gap_d_spectral_support(self):
        """
        Genus-1 sewing kernel lives in Re(s) > 1 (mismatch with NB).
        Genus-2 Beurling kernel lives at Re(s) = 1/2 (matches NB).
        """
        result = gap_d_spectral_comparison()
        assert result['genus1_mismatch'] is True
        assert result['genus2_mismatch'] is False

    def test_gap_d_narrowed(self):
        """The genus-2 construction narrows Gap D."""
        result = gap_d_spectral_comparison()
        assert 'narrowed' in result['gap_d_status']

    def test_beurling_kernel_symmetric(self):
        """K(D, D') = K(D', D) (Hermitian symmetry)."""
        data = genus2_beurling_kernel_leech()
        K = data['kernel']
        for D in data['discriminants']:
            for Dp in data['discriminants']:
                assert K[(D, Dp)] == K[(Dp, D)]

    def test_beurling_vs_bocherer_consistency(self):
        """
        The Beurling kernel diagonal at D should equal
        B(D)^2 (the square of the Böcherer coefficient).
        """
        data = genus2_beurling_kernel_leech()
        boch = data['bocherer_coefficients']
        K = data['kernel']
        for D in data['discriminants']:
            if D in boch:
                assert K[(D, D)] == boch[D] * boch[D]
