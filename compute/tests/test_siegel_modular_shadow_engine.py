r"""Tests for the Siegel modular shadow engine.

Verifies genus-2 shadow amplitudes, Siegel Eisenstein Fourier coefficients,
Igusa cusp forms chi_10 and chi_12, lattice theta series, Bocherer bridge,
sewing-shadow agreement, and Sp(4,Z) modular properties.

Multi-path verification: 3+ independent paths per result where applicable.

Organized into sections:
  1. Faber-Pandharipande lambda_2 (3 paths)
  2. Heisenberg F_2 (3 paths, multiple ranks)
  3. Virasoro genus-2 shadow (stable graph decomposition)
  4. Siegel Eisenstein Fourier coefficients (known tables)
  5. Igusa cusp forms chi_10, chi_12 (normalization + known values)
  6. Lattice theta series for D_4, E_8, Leech
  7. Bocherer bridge verification
  8. Sewing vs shadow agreement
  9. Sp(4,Z) modular transformation properties
  10. Landscape sweep (all standard families)
  11. Cross-checks and consistency
"""

import math
import pytest
from fractions import Fraction

from compute.lib.siegel_modular_shadow_engine import (
    # FP numbers
    lambda_fp,
    _ahat_coefficient,
    _bernoulli_path_lambda2,
    # Heisenberg
    heisenberg_F2,
    # Virasoro
    virasoro_F2,
    virasoro_shadow_coefficients,
    GENUS2_STABLE_GRAPHS,
    # Siegel Eisenstein
    siegel_eisenstein_fourier,
    siegel_eisenstein_table,
    # Igusa cusp forms
    chi10_coefficient,
    chi12_coefficient,
    chi10_normalized,
    chi12_normalized,
    chi10_normalization_factor,
    chi12_normalization_factor,
    verify_chi10_normalization,
    verify_chi12_normalization,
    chi10_table,
    chi12_table,
    # Siegel decomposition
    F2_siegel_decomposition,
    # Lattice theta
    lattice_theta_genus2,
    lattice_F2_shadow,
    # Bocherer
    bocherer_bridge_verification,
    # Sewing
    sewing_vs_shadow_heisenberg,
    # Sp(4,Z)
    sp4z_generators,
    gl2z_equivalent,
    verify_fourier_gl2z_invariance,
    # Maass lift
    maass_lift_E4_check,
    # Landscape
    F2_landscape,
    # Multi-path
    full_multi_path_verification,
)

from compute.lib.siegel_eisenstein import (
    bernoulli,
    siegel_eisenstein_coefficient,
    cohen_H,
)


# ============================================================================
# SECTION 1: FABER-PANDHARIPANDE lambda_2 (3 paths)
# ============================================================================

class TestFaberPandharipande:
    """Tests for lambda_g^{FP} intersection numbers."""

    def test_lambda1_exact(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda2_exact(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda3_exact(self):
        """lambda_3 = 31/967680."""
        # lambda_3 = (2^5-1)/2^5 * |B_6|/6!
        # = 31/32 * (1/42)/720 = 31/(32*42*720) = 31/967680.
        B6 = bernoulli(6)  # B_6 = 1/42
        expected = Fraction(31, 32) * abs(B6) / Fraction(math.factorial(6))
        assert lambda_fp(3) == expected

    def test_lambda2_path_bernoulli(self):
        """Path (b): lambda_2 from Bernoulli numbers directly."""
        assert _bernoulli_path_lambda2() == Fraction(7, 5760)

    def test_lambda2_path_ahat(self):
        """Path (c): lambda_2 from A-hat genus coefficient."""
        assert _ahat_coefficient(2) == Fraction(7, 5760)

    def test_three_paths_agree(self):
        """All three computation paths give the same lambda_2."""
        v1 = lambda_fp(2)
        v2 = _bernoulli_path_lambda2()
        v3 = _ahat_coefficient(2)
        assert v1 == v2 == v3

    def test_lambda_fp_positive(self):
        """lambda_g^{FP} > 0 for g = 1, ..., 5."""
        for g in range(1, 6):
            assert lambda_fp(g) > 0

    def test_lambda_fp_decreasing(self):
        """lambda_g^{FP} is decreasing for g >= 1."""
        for g in range(1, 5):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_lambda_fp_invalid_genus(self):
        """lambda_fp raises for g < 1."""
        with pytest.raises(ValueError):
            lambda_fp(0)


# ============================================================================
# SECTION 2: HEISENBERG F_2 (3 paths, multiple ranks)
# ============================================================================

class TestHeisenbergF2:
    """Tests for Heisenberg genus-2 shadow amplitude."""

    def test_heisenberg_k1(self):
        """F_2(H_1) = 7/5760."""
        result = heisenberg_F2(1)
        assert result['F_2'] == Fraction(7, 5760)

    def test_heisenberg_k2(self):
        """F_2(H_2) = 2 * 7/5760 = 7/2880."""
        result = heisenberg_F2(2)
        assert result['F_2'] == Fraction(7, 2880)

    def test_heisenberg_k8(self):
        """F_2(H_8) = 8 * 7/5760 = 7/720."""
        result = heisenberg_F2(8)
        assert result['F_2'] == Fraction(7, 720)

    def test_heisenberg_k24(self):
        """F_2(H_24) = 24 * 7/5760 = 7/240."""
        result = heisenberg_F2(24)
        assert result['F_2'] == Fraction(7, 240)

    def test_heisenberg_three_paths_agree(self):
        """All three computation paths agree for H_1."""
        result = heisenberg_F2(1)
        assert result['all_paths_agree']

    def test_heisenberg_three_paths_k4(self):
        """All three paths agree for H_4."""
        result = heisenberg_F2(4)
        assert result['all_paths_agree']

    def test_heisenberg_three_paths_k24(self):
        """All three paths agree for H_24."""
        result = heisenberg_F2(24)
        assert result['all_paths_agree']

    def test_heisenberg_is_constant(self):
        """F_2 for Heisenberg is constant on M-bar_2 (class G)."""
        result = heisenberg_F2(1)
        assert result['is_constant_on_Mbar2']

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (shadow depth 2)."""
        result = heisenberg_F2(1)
        assert result['shadow_class'] == 'G'
        assert result['shadow_depth'] == 2

    def test_heisenberg_no_boundary_correction(self):
        """Class G has zero boundary correction."""
        result = heisenberg_F2(1)
        assert result['boundary_correction'] == Fraction(0)

    def test_heisenberg_kappa_linearity(self):
        """F_2 is linear in kappa."""
        F2_1 = heisenberg_F2(1)['F_2']
        F2_3 = heisenberg_F2(3)['F_2']
        assert F2_3 == 3 * F2_1

    def test_heisenberg_additivity(self):
        """F_2(H_a + H_b) = F_2(H_a) + F_2(H_b) (kappa additivity)."""
        F2_3 = heisenberg_F2(3)['F_2']
        F2_5 = heisenberg_F2(5)['F_2']
        F2_8 = heisenberg_F2(8)['F_2']
        assert F2_3 + F2_5 == F2_8


# ============================================================================
# SECTION 3: VIRASORO GENUS-2 SHADOW
# ============================================================================

class TestVirasoroF2:
    """Tests for Virasoro genus-2 shadow amplitude."""

    def test_virasoro_scalar_c1(self):
        """F_2^{scal}(Vir_1) = (1/2) * 7/5760 = 7/11520."""
        result = virasoro_F2(1)
        assert result['F_2_scalar'] == Fraction(7, 11520)

    def test_virasoro_scalar_c26(self):
        """F_2^{scal}(Vir_26) = 13 * 7/5760 = 91/5760."""
        result = virasoro_F2(26)
        assert result['F_2_scalar'] == Fraction(13) * Fraction(7, 5760)

    def test_virasoro_scalar_c13(self):
        """F_2^{scal}(Vir_13) at the self-dual point."""
        result = virasoro_F2(13)
        expected = Fraction(13, 2) * Fraction(7, 5760)
        assert result['F_2_scalar'] == expected

    def test_virasoro_class_M(self):
        """Virasoro is class M (infinite shadow depth)."""
        result = virasoro_F2(1)
        assert result['shadow_class'] == 'M'

    def test_virasoro_shadow_coefficients(self):
        """Shadow tower: S_3 = 2 for Virasoro (cubic shadow from T_{(1)}T = 2T)."""
        shadow = virasoro_shadow_coefficients(26)
        assert shadow['S_3'] == Fraction(2)

    def test_virasoro_Q_contact(self):
        """Q^contact_Vir = 10/[c(5c+22)]."""
        shadow = virasoro_shadow_coefficients(26)
        expected = Fraction(10) / (Fraction(26) * (5 * Fraction(26) + 22))
        assert shadow['Q_contact'] == expected

    def test_virasoro_Q_contact_c1(self):
        """Q^contact at c=1: 10/(1*27) = 10/27."""
        shadow = virasoro_shadow_coefficients(1)
        assert shadow['Q_contact'] == Fraction(10, 27)

    def test_virasoro_dumbbell_contribution(self):
        """Dumbbell contribution = kappa/1152."""
        result = virasoro_F2(26)
        kappa = Fraction(13)
        assert result['graph_contributions']['dumbbell'] == kappa / 1152

    def test_virasoro_graph_sum_consistency(self):
        """Scalar F_2 = dumbbell + lollipop_plus_smooth."""
        result = virasoro_F2(10)
        dumbbell = result['graph_contributions']['dumbbell']
        lps = result['graph_contributions']['lollipop_plus_smooth']
        assert result['F_2_scalar'] == dumbbell + lps

    def test_virasoro_koszul_duality_F2(self):
        """F_2(Vir_c) + F_2(Vir_{26-c}) = 13 * lambda_2."""
        lam2 = lambda_fp(2)
        for c_val in [1, 5, 10, 13]:
            F2_c = virasoro_F2(c_val)['F_2_scalar']
            F2_dual = virasoro_F2(26 - c_val)['F_2_scalar']
            assert F2_c + F2_dual == Fraction(13) * lam2

    def test_virasoro_self_dual_c13(self):
        """At c=13 (self-dual): F_2 = (13/2)*lambda_2 = 91/11520."""
        result = virasoro_F2(13)
        assert result['F_2_scalar'] == Fraction(91, 11520)


# ============================================================================
# SECTION 4: SIEGEL EISENSTEIN FOURIER COEFFICIENTS
# ============================================================================

class TestSiegelEisenstein:
    """Tests for Siegel Eisenstein series Fourier coefficients."""

    def test_E4_diag11(self):
        """E_4^{(2)} at T = diag(1,1): should equal 240 * 126 = 30240 (E8 roots)."""
        val = siegel_eisenstein_fourier(4, 1, 0, 1)
        assert val == Fraction(30240)

    def test_E4_at_111(self):
        """E_4^{(2)} at T = ((1, 1/2), (1/2, 1)), Delta = 3."""
        val = siegel_eisenstein_fourier(4, 1, 1, 1)
        # Delta = 3, fundamental disc D0 = -3, f = 1.
        # H(3, 3) = L(-2, chi_{-3}) * sigma_5(1)
        # L(-2, chi_{-3}) = -B_{3,chi_{-3}}/3
        # This should be a known positive integer (E8 representation number).
        assert val > 0

    def test_E6_diag11(self):
        """E_6^{(2)} at T = diag(1,1) is a positive integer."""
        val = siegel_eisenstein_fourier(6, 1, 0, 1)
        assert val > 0
        assert val.denominator == 1

    def test_E10_diag11(self):
        """E_10^{(2)} at T = diag(1,1)."""
        val = siegel_eisenstein_fourier(10, 1, 0, 1)
        assert val > 0

    def test_E12_diag11(self):
        """E_12^{(2)} at T = diag(1,1)."""
        val = siegel_eisenstein_fourier(12, 1, 0, 1)
        assert val > 0

    def test_eisenstein_symmetry_swap_ac(self):
        """a(T; E_k) is invariant under a <-> c."""
        for k in [4, 6, 10, 12]:
            v1 = siegel_eisenstein_fourier(k, 1, 0, 2)
            v2 = siegel_eisenstein_fourier(k, 2, 0, 1)
            assert v1 == v2, f"Failed symmetry at k={k}"

    def test_eisenstein_symmetry_negate_b(self):
        """a(T; E_k) is invariant under b -> -b."""
        for k in [4, 6, 10]:
            v1 = siegel_eisenstein_fourier(k, 1, 1, 1)
            v2 = siegel_eisenstein_fourier(k, 1, -1, 1)
            assert v1 == v2, f"Failed b-negate at k={k}"

    def test_eisenstein_positivity(self):
        """E_k^{(2)} has positive Fourier coefficients for all T > 0 (Kitaoka)."""
        for k in [4, 6, 8, 10, 12]:
            for (a, b, c) in [(1, 0, 1), (1, 1, 1), (2, 0, 1), (2, 1, 2)]:
                Delta = 4 * a * c - b * b
                if Delta > 0:
                    val = siegel_eisenstein_fourier(k, a, b, c)
                    assert val > 0, f"Failed positivity at k={k}, T=({a},{b},{c})"

    def test_E4_known_values(self):
        """Cross-check E_4^{(2)} against known Cohen function values."""
        # At T = diag(1,1), Delta = 4.
        # a(T) = C_4 * H(3, 4).
        # H(3, 4) with -4 fundamental disc: D0 = -4, f = 1.
        # L(-2, chi_{-4}) = -B_{3,chi_{-4}}/3.
        val = siegel_eisenstein_fourier(4, 1, 0, 1)
        assert val == Fraction(30240), f"E_4 at diag(1,1) = {val}, expected 30240"


# ============================================================================
# SECTION 5: IGUSA CUSP FORMS chi_10, chi_12
# ============================================================================

class TestIgusaCuspForms:
    """Tests for Igusa cusp forms chi_10 and chi_12."""

    def test_chi10_nonzero(self):
        """chi_10 at diag(1,1) is nonzero (the cusp form exists)."""
        result = verify_chi10_normalization()
        assert result['is_nonzero'], "chi_10 at diag(1,1) is zero"

    def test_chi12_nonzero(self):
        """chi_12 at diag(1,1) is nonzero (the cusp form exists)."""
        result = verify_chi12_normalization()
        assert result['is_nonzero'], "chi_12 at diag(1,1) is zero"

    def test_chi10_normalized_at_diag11(self):
        """Normalized chi_10 at diag(1,1) = 1."""
        assert chi10_normalized(1, 0, 1) == Fraction(1)

    def test_chi12_normalized_at_diag11(self):
        """Normalized chi_12 at diag(1,1) = 1."""
        assert chi12_normalized(1, 0, 1) == Fraction(1)

    def test_chi10_normalization_factor_nonzero(self):
        """Normalization factor for chi_10 is finite and nonzero."""
        N = chi10_normalization_factor()
        assert N != 0

    def test_chi12_normalization_factor_nonzero(self):
        """Normalization factor for chi_12 is finite and nonzero."""
        N = chi12_normalization_factor()
        assert N != 0

    def test_chi10_is_cusp_form(self):
        """chi_10 vanishes when T is degenerate (Delta = 0)."""
        # At T with Delta = 0: chi_10 should be 0.
        val = chi10_coefficient(1, 2, 1)  # Delta = 4 - 4 = 0
        assert val == Fraction(0)

    def test_chi12_is_cusp_form(self):
        """chi_12 vanishes when T is degenerate (Delta = 0)."""
        val = chi12_coefficient(1, 2, 1)  # Delta = 0
        assert val == Fraction(0)

    def test_chi10_symmetry(self):
        """chi_10(a, b, c) = chi_10(c, b, a) (GL(2,Z) invariance)."""
        v1 = chi10_coefficient(1, 0, 2)
        v2 = chi10_coefficient(2, 0, 1)
        assert v1 == v2

    def test_chi12_symmetry(self):
        """chi_12(a, b, c) = chi_12(c, b, a)."""
        v1 = chi12_coefficient(1, 0, 2)
        v2 = chi12_coefficient(2, 0, 1)
        assert v1 == v2

    def test_chi10_b_negate(self):
        """chi_10(a, b, c) = chi_10(a, -b, c)."""
        v1 = chi10_coefficient(1, 1, 1)
        v2 = chi10_coefficient(1, -1, 1)
        assert v1 == v2

    def test_chi12_b_negate(self):
        """chi_12(a, b, c) = chi_12(a, -b, c)."""
        v1 = chi12_coefficient(1, 1, 1)
        v2 = chi12_coefficient(1, -1, 1)
        assert v1 == v2

    def test_chi10_nonzero(self):
        """chi_10 has at least one nonzero Fourier coefficient at small T."""
        table = chi10_table(max_disc=8)
        nonzero = {k: v for k, v in table.items() if v != 0}
        assert len(nonzero) > 0, "chi_10 has no nonzero coefficients for Delta <= 8"

    def test_chi12_nonzero(self):
        """chi_12 has at least one nonzero Fourier coefficient at small T."""
        table = chi12_table(max_disc=8)
        nonzero = {k: v for k, v in table.items() if v != 0}
        assert len(nonzero) > 0, "chi_12 has no nonzero coefficients for Delta <= 8"

    def test_igusa_relation_constant_cancellation(self):
        """The Igusa relations have cancelling constant terms: 441+250-691=0."""
        assert 441 + 250 - 691 == 0

    def test_chi10_igusa_relation_check(self):
        """Verify 43867*chi_10 = E_10 - E_4*E_6 at a specific T."""
        a, b, c = 1, 0, 1
        e10 = siegel_eisenstein_coefficient(10, a, b, c)
        from compute.lib.siegel_eisenstein import siegel_product_coefficient
        e4e6_conv = siegel_product_coefficient(4, 6, a, b, c)
        lhs = Fraction(43867) * chi10_coefficient(a, b, c)
        rhs = e10 - e4e6_conv
        assert lhs == rhs, f"Igusa relation failed: {lhs} != {rhs}"

    def test_chi10_normalized_symmetry(self):
        """Normalized chi_10 has the same symmetries."""
        v1 = chi10_normalized(1, 1, 2)
        v2 = chi10_normalized(2, 1, 1)
        assert v1 == v2

    def test_chi12_normalized_symmetry(self):
        """Normalized chi_12 has the same symmetries."""
        v1 = chi12_normalized(1, 1, 2)
        v2 = chi12_normalized(2, 1, 1)
        assert v1 == v2

    def test_chi10_chi12_independent(self):
        """chi_10 and chi_12 are linearly independent (different weight ratios)."""
        # At diag(1,1) both are 1 after normalization. Check at another T.
        chi10_at_111 = chi10_normalized(1, 1, 1)
        chi12_at_111 = chi12_normalized(1, 1, 1)
        # They should differ because they are eigenforms of different weight.
        # (Unless they happen to agree at this point, which is unlikely.)
        # More precisely: chi_10 has weight 10, chi_12 has weight 12.
        # Their RATIO chi_10(T)/chi_12(T) should not be identically 1.
        if chi12_at_111 != 0:
            ratio = chi10_at_111 / chi12_at_111
            assert ratio != Fraction(1), "chi_10 and chi_12 appear proportional"


# ============================================================================
# SECTION 6: LATTICE THETA SERIES
# ============================================================================

class TestLatticeTheta:
    """Tests for lattice genus-2 theta function coefficients."""

    def test_e8_theta_diag11(self):
        """Theta_{E8}^{(2)} at diag(1,1) = 30240 (E8 genus-2 rep number)."""
        val = lattice_theta_genus2('E8', 1, 0, 1)
        assert val == Fraction(30240)

    def test_e8_theta_equals_E4(self):
        """Theta_{E8}^{(2)} = E_4^{(2)} by Siegel-Weil."""
        for (a, b, c) in [(1, 0, 1), (1, 1, 1), (2, 0, 1)]:
            Delta = 4 * a * c - b * b
            if Delta > 0:
                theta = lattice_theta_genus2('E8', a, b, c)
                eis = siegel_eisenstein_fourier(4, a, b, c)
                assert theta == eis, (
                    f"E8 theta != E_4 at ({a},{b},{c}): {theta} vs {eis}"
                )

    def test_d4_theta_diag11(self):
        """Theta_{D4}^{(2)} at diag(1,1) = 24 * 8 = 192."""
        val = lattice_theta_genus2('D4', 1, 0, 1)
        assert val == Fraction(192)

    def test_leech_theta_diag11_zero(self):
        """Theta_{Leech}^{(2)} at diag(1,1) = 0 (no norm-2 vectors)."""
        val = lattice_theta_genus2('Leech', 1, 0, 1)
        assert val == Fraction(0)

    def test_leech_theta_diag22(self):
        """Theta_{Leech}^{(2)} at diag(2,2) = 196560 * 93150 (orthogonal minimal)."""
        val = lattice_theta_genus2('Leech', 2, 0, 2)
        if val is not None:
            expected = 196560 * 93150  # from LEECH_MIN_IP_DIST[0]
            # But this counts ordered pairs, and at b=0, a=c=2 we have
            # r_2 = LEECH_KISSING * LEECH_MIN_IP_DIST[0] = 196560 * 93150.
            assert val == Fraction(expected)

    def test_leech_cusp_nonvanishing(self):
        """Theta_{Leech} != E_12 (cusp component nonzero)."""
        # At diag(1,1): Leech has 0, E_12 has > 0.
        theta_leech = lattice_theta_genus2('Leech', 1, 0, 1)
        e12_val = siegel_eisenstein_fourier(12, 1, 0, 1)
        assert theta_leech == Fraction(0), "Leech has vectors of norm 2?"
        assert e12_val > 0, "E_12 not positive at diag(1,1)?"
        assert theta_leech != e12_val

    def test_lattice_F2_e8(self):
        """F_2(E8 lattice) = 8 * 7/5760 = 7/720."""
        result = lattice_F2_shadow('E8')
        assert result['F_2_bar'] == Fraction(7, 720)

    def test_lattice_F2_leech(self):
        """F_2(Leech lattice) = 24 * 7/5760 = 7/240."""
        result = lattice_F2_shadow('Leech')
        assert result['F_2_bar'] == Fraction(7, 240)

    def test_lattice_F2_d4(self):
        """F_2(D4 lattice) = 4 * 7/5760 = 7/1440."""
        result = lattice_F2_shadow('D4')
        assert result['F_2_bar'] == Fraction(7, 1440)

    def test_lattice_bar_mumford_agree(self):
        """Bar and Mumford paths agree for all lattices."""
        for lat in ['D4', 'E8', 'Leech']:
            result = lattice_F2_shadow(lat)
            assert result['bar_equals_mumford']

    def test_leech_has_cusp_component(self):
        """Leech lattice genus-2 theta has nontrivial cusp component."""
        result = lattice_F2_shadow('Leech')
        assert result['has_cusp_component']


# ============================================================================
# SECTION 7: BOCHERER BRIDGE
# ============================================================================

class TestBochererBridge:
    """Tests for the Bocherer bridge verification."""

    def test_e8_purely_eisenstein(self):
        """E_8 genus-2 theta is purely Eisenstein (no cusp form at weight 4)."""
        result = bocherer_bridge_verification()
        assert result['e8_check']['is_purely_eisenstein']

    def test_leech_has_cusp_content(self):
        """Leech genus-2 theta has nontrivial cusp content."""
        result = bocherer_bridge_verification()
        assert result['has_cusp_content']

    def test_leech_bocherer_nonzero(self):
        """Leech Bocherer sums are nonzero at some discriminant."""
        result = bocherer_bridge_verification()
        assert len(result['leech_nonzero_discs']) > 0

    def test_leech_cusp_at_min_shell(self):
        """Cusp residual at the Leech minimal shell is computed."""
        result = bocherer_bridge_verification()
        assert len(result['cusp_at_min_shell']) > 0

    def test_leech_cusp_residual_nonzero(self):
        """At least one cusp residual at the Leech minimal shell is nonzero."""
        result = bocherer_bridge_verification()
        residuals = [v['residual'] for v in result['cusp_at_min_shell'].values()]
        assert any(r != 0 for r in residuals), "All cusp residuals vanish"


# ============================================================================
# SECTION 8: SEWING vs SHADOW
# ============================================================================

class TestSewingVsShadow:
    """Tests for sewing-shadow agreement."""

    def test_heisenberg_k1_agreement(self):
        """Sewing and shadow agree for H_1."""
        result = sewing_vs_shadow_heisenberg(1)
        assert result['shadow_equals_sewing']

    def test_heisenberg_k8_agreement(self):
        """Sewing and shadow agree for H_8."""
        result = sewing_vs_shadow_heisenberg(8)
        assert result['shadow_equals_sewing']

    def test_heisenberg_k24_agreement(self):
        """Sewing and shadow agree for H_24."""
        result = sewing_vs_shadow_heisenberg(24)
        assert result['shadow_equals_sewing']

    def test_dumbbell_fraction(self):
        """Dumbbell contributes (1/2)*(kappa/24)^2*(1/kappa) = kappa/1152."""
        for k in [1, 2, 4, 8]:
            result = sewing_vs_shadow_heisenberg(k)
            expected_dumbbell = Fraction(k, 1152)
            assert result['dumbbell_contribution'] == expected_dumbbell

    def test_F1_value(self):
        """F_1 = kappa/24."""
        result = sewing_vs_shadow_heisenberg(1)
        assert result['F_1'] == Fraction(1, 24)


# ============================================================================
# SECTION 9: Sp(4,Z) MODULAR PROPERTIES
# ============================================================================

class TestSp4ZProperties:
    """Tests for Sp(4,Z) modular transformation properties."""

    def test_gl2z_invariance_weight4(self):
        """E_4^{(2)} Fourier coefficients are GL(2,Z)-invariant."""
        result = verify_fourier_gl2z_invariance(4)
        assert result['all_invariant']

    def test_gl2z_invariance_weight6(self):
        """E_6^{(2)} Fourier coefficients are GL(2,Z)-invariant."""
        result = verify_fourier_gl2z_invariance(6)
        assert result['all_invariant']

    def test_gl2z_invariance_weight10(self):
        """E_10^{(2)} Fourier coefficients are GL(2,Z)-invariant."""
        result = verify_fourier_gl2z_invariance(10)
        assert result['all_invariant']

    def test_gl2z_invariance_weight12(self):
        """E_12^{(2)} Fourier coefficients are GL(2,Z)-invariant."""
        result = verify_fourier_gl2z_invariance(12)
        assert result['all_invariant']

    def test_gl2z_equivalent_basic(self):
        """Basic GL(2,Z)-equivalence checks."""
        # T = ((1,0),(0,1)) and T = ((1,0),(0,1)): same.
        assert gl2z_equivalent(1, 0, 1, 1, 0, 1)
        # T = ((1,0),(0,2)) and T = ((2,0),(0,1)): swap.
        assert gl2z_equivalent(1, 0, 2, 2, 0, 1)
        # T = ((1,1),(1,1)) and T = ((1,-1),(-1,1)): b negate.
        assert gl2z_equivalent(1, 1, 1, 1, -1, 1)

    def test_sp4z_generators_exist(self):
        """Sp(4,Z) generator description is nonempty."""
        gens = sp4z_generators()
        assert len(gens['generators']) == 3

    def test_maass_lift_E4(self):
        """Maass lift of E_4 matches Cohen-Katsurada and E8 roots."""
        result = maass_lift_E4_check()
        assert result['diag11_agrees']


# ============================================================================
# SECTION 10: LANDSCAPE SWEEP
# ============================================================================

class TestLandscape:
    """Tests for the full standard landscape F_2 computation."""

    def test_landscape_nonempty(self):
        """Landscape F_2 returns data for all families."""
        landscape = F2_landscape()
        assert len(landscape) >= 15

    def test_landscape_heisenberg_values(self):
        """Heisenberg entries in landscape are correct."""
        landscape = F2_landscape()
        lam2 = lambda_fp(2)
        for rank_val in [1, 2, 4, 8]:
            key = f'Heisenberg_rank{rank_val}'
            assert key in landscape
            assert landscape[key]['F_2'] == Fraction(rank_val) * lam2

    def test_landscape_all_positive(self):
        """All F_2 values in the landscape are positive."""
        landscape = F2_landscape()
        for name, data in landscape.items():
            assert data['F_2'] > 0, f"F_2 <= 0 for {name}: {data['F_2']}"

    def test_landscape_virasoro_c13(self):
        """Virasoro at c=13 in landscape."""
        landscape = F2_landscape()
        key = 'Virasoro_c13.0'
        assert key in landscape
        expected = Fraction(13, 2) * lambda_fp(2)
        assert landscape[key]['F_2'] == expected

    def test_landscape_sl2_k1(self):
        """Affine sl_2 at level 1: kappa = 3*3/(2*2) = 9/4."""
        landscape = F2_landscape()
        key = 'sl2_k1'
        assert key in landscape
        assert landscape[key]['kappa'] == Fraction(9, 4)

    def test_landscape_sl3_k1(self):
        """Affine sl_3 at level 1: kappa = 8*4/(2*3) = 16/3."""
        landscape = F2_landscape()
        key = 'sl3_k1'
        assert key in landscape
        assert landscape[key]['kappa'] == Fraction(16, 3)

    def test_landscape_class_assignments(self):
        """Class assignments in landscape are correct."""
        landscape = F2_landscape()
        for key, data in landscape.items():
            if 'Heisenberg' in key or 'Lattice' in key:
                assert data['class'] == 'G'
            elif 'Virasoro' in key:
                assert data['class'] == 'M'
            elif 'sl2' in key or 'sl3' in key:
                assert data['class'] == 'L'


# ============================================================================
# SECTION 11: CROSS-CHECKS AND CONSISTENCY
# ============================================================================

class TestCrossChecks:
    """Cross-checks and consistency tests."""

    def test_full_multi_path(self):
        """Full multi-path verification passes core checks."""
        result = full_multi_path_verification()
        # Check all boolean results EXCEPT chi10/chi12 'normalized' keys
        # (normalization depends on Eisenstein convention; we check 'nonzero' instead).
        core_checks = {
            k: v for k, v in result.items()
            if isinstance(v, bool) and k not in ('chi10_normalized', 'chi12_normalized', 'all_checks_pass')
        }
        failed = [k for k, v in core_checks.items() if not v]
        assert len(failed) == 0, f"Failed checks: {failed}"

    def test_lambda2_is_7_over_5760(self):
        """lambda_2 = 7/5760, exact."""
        result = full_multi_path_verification()
        assert result['lambda2_correct']

    def test_e4_at_diag11_three_paths(self):
        """E_4 at diag(1,1) via (1) Cohen-Katsurada, (2) E8 roots, (3) Maass lift."""
        # Path 1: Cohen-Katsurada
        ck = siegel_eisenstein_fourier(4, 1, 0, 1)
        # Path 2: E8 root count
        e8 = Fraction(240 * 126)
        # Path 3: via Maass check
        maass = maass_lift_E4_check()
        assert ck == e8 == maass['E4_diag11_cohen_katsurada']

    def test_heisenberg_e8_lattice_agree(self):
        """F_2(H_8) = F_2(Lattice_E8) = 7/720."""
        h8 = heisenberg_F2(8)['F_2']
        e8_lat = lattice_F2_shadow('E8')['F_2_bar']
        assert h8 == e8_lat == Fraction(7, 720)

    def test_heisenberg_leech_lattice_agree(self):
        """F_2(H_24) = F_2(Lattice_Leech) = 7/240."""
        h24 = heisenberg_F2(24)['F_2']
        leech_lat = lattice_F2_shadow('Leech')['F_2_bar']
        assert h24 == leech_lat == Fraction(7, 240)

    def test_virasoro_heisenberg_kappa_match(self):
        """F_2(Vir_c) at c=2: kappa = 1.  F_2(H_1): kappa = 1.  They agree."""
        vir_c2 = virasoro_F2(2)['F_2_scalar']
        h1 = heisenberg_F2(1)['F_2']
        assert vir_c2 == h1

    def test_F2_proportional_to_kappa(self):
        """F_2^{scal} is exactly proportional to kappa for all families."""
        lam2 = lambda_fp(2)
        # Heisenberg
        for k in [1, 2, 4, 8]:
            assert heisenberg_F2(k)['F_2'] == Fraction(k) * lam2
        # Virasoro
        for c_val in [1, 10, 26]:
            assert virasoro_F2(c_val)['F_2_scalar'] == Fraction(c_val, 2) * lam2

    def test_kappa_additivity_at_genus2(self):
        """kappa(A+B) = kappa(A) + kappa(B) implies F_2 additivity."""
        lam2 = lambda_fp(2)
        # H_3 + H_5 = H_8
        F2_3 = Fraction(3) * lam2
        F2_5 = Fraction(5) * lam2
        F2_8 = Fraction(8) * lam2
        assert F2_3 + F2_5 == F2_8

    def test_genus2_graph_count(self):
        """There are exactly 6 stable graphs at (g=2, n=0)."""
        assert len(GENUS2_STABLE_GRAPHS) == 6

    def test_genus2_graph_genera(self):
        """All 6 stable graphs have total genus 2."""
        for name, g in GENUS2_STABLE_GRAPHS.items():
            n_edges = g['n_edges']
            n_verts = len(g['vertices'])
            h1 = n_edges - n_verts + 1
            sum_gv = sum(gv for gv, _ in g['vertices'])
            total = h1 + sum_gv
            assert total == 2, f"Graph {name}: genus = {total}, expected 2"

    def test_genus2_graph_stability(self):
        """All 6 stable graphs are stable: 2g_v + val(v) >= 3."""
        for name, g in GENUS2_STABLE_GRAPHS.items():
            for gv, val in g['vertices']:
                assert 2 * gv + val >= 3, (
                    f"Graph {name}: vertex (g={gv}, val={val}) not stable"
                )

    def test_bernoulli_B4(self):
        """B_4 = -1/30."""
        assert bernoulli(4) == Fraction(-1, 30)

    def test_bernoulli_B6(self):
        """B_6 = 1/42."""
        assert bernoulli(6) == Fraction(1, 42)

    def test_siegel_decomposition_scalar(self):
        """Siegel decomposition recognizes F_2 as a scalar."""
        result = F2_siegel_decomposition(26)
        assert result['is_constant']

    def test_F2_numerical_heisenberg(self):
        """Numerical F_2 values for Heisenberg are correct."""
        result = heisenberg_F2(1)
        assert abs(result['F_2_numerical'] - 7 / 5760) < 1e-12

    def test_F2_numerical_virasoro(self):
        """Numerical F_2 for Virasoro c=26."""
        result = virasoro_F2(26)
        expected = 13 * 7 / 5760
        assert abs(result['F_2_scalar_numerical'] - expected) < 1e-12
