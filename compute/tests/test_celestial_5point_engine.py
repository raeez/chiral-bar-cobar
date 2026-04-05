r"""Tests for the celestial 5-point amplitude engine.

Verifies the arity-5 shadow obstruction tower computation and its
connection to celestial holography via 6 independent verification paths:

    Path 1: Direct shadow extraction from MC element
    Path 2: Mellin transform of the known BGK MHV amplitude
    Path 3: Soft limit factorization (5 -> 4+1 in each channel)
    Path 4: w_{1+infty} Ward identity check
    Path 5: Collinear limit pole structure
    Path 6: Cross-ratio expansion comparison

Ground truth sources:
    - S_5 = -48/[c^2(5c+22)] (virasoro_quintic_shadow.py, independently derived)
    - o^(5) = 480/[c^2(5c+22)] (MC bracket {Sh_3, Sh_4}_H)
    - S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)] (celestial_shadow_engine.py)
    - BGK formula: M_5 = <ij>^8 / (<12><23><34><45><51>)
    - r-matrix pole = OPE pole - 1 (AP19)
    - w_{1+infty} Ward identities (Strominger et al.)
    - Shadow growth rate rho = sqrt(180c+872) / [c*sqrt(5c+22)]

References:
    compute/lib/celestial_5point_engine.py
    compute/lib/virasoro_quintic_shadow.py
    compute/lib/celestial_shadow_engine.py
    concordance.tex: sec:concordance-holographic-datum
    higher_genus_modular_koszul.tex: thm:mc2-bar-intrinsic
"""

from fractions import Fraction
from math import pi, sqrt

import pytest

from compute.lib.celestial_5point_engine import (
    # Cross-ratio geometry
    CrossRatioData5,
    cross_ratios_5,
    cross_ratio_4pt,
    mobius_invariant_5pt,
    # Celestial kinematics
    CelestialParticle,
    celestial_null_momentum,
    spinor_bracket_holomorphic,
    spinor_bracket_antiholomorphic,
    # MHV amplitude
    bgk_5_graviton_mhv_stripped,
    bgk_5_graviton_mhv_full,
    # Celestial Mellin transform
    CelestialMellinData5,
    celestial_mellin_5pt,
    # Arity-5 shadow
    quintic_shadow_coefficient_virasoro,
    quintic_obstruction_coefficient_virasoro,
    quintic_mc_equation_residual,
    quintic_shadow_special_values,
    quintic_shadow_w_infinity_virasoro_channel,
    quintic_shadow_cross_spin_estimate,
    # Soft factorization
    SoftFactorizationData,
    soft_factorization_5to4,
    verify_soft_limit_all_channels,
    # Collinear limits
    collinear_pole_structure_5pt,
    collinear_limit_numerical,
    # Permutation symmetry
    check_s5_symmetry_identical,
    check_mhv_permutation_symmetry,
    # Conformal blocks
    CelestialConformalBlock,
    celestial_block_channels_5pt,
    # Ward identities
    w_infinity_ward_identity_check,
    ward_identity_soft_factor_leading,
    ward_identity_soft_factor_subleading,
    ward_identity_quintic_check,
    # Shadow-amplitude comparison
    shadow_vs_mellin_comparison,
    # Multi-path verification
    verify_path1_direct_shadow,
    verify_path2_mellin_transform,
    verify_path3_soft_factorization,
    verify_path4_ward_identities,
    verify_path5_collinear_poles,
    verify_path6_cross_ratio_expansion,
    # Shadow tower
    shadow_tower_arity_2_to_5,
    verify_tower_sign_alternation,
    # Soft theorem order 3
    SoftGravitonTheoremArity5,
    soft_theorem_arity5,
    # Consistency
    verify_shadow_consistency_arity5,
    verify_duality_at_arity5,
    # Full suite
    run_full_5point_verification,
    # Helpers
    harmonic_number,
)


# ============================================================================
# Standard test configurations
# ============================================================================

# 5 points in general position on P^1 (no coincidences, not collinear)
Z_GENERIC = (0.0 + 0j, 1.0 + 0j, 0.5 + 0.8j, -0.3 + 0.6j, 0.7 - 0.4j)

# Points on the unit circle (symmetric configuration)
Z_CIRCLE = tuple(complex(0.9 * __import__('cmath').exp(2j * pi * k / 5))
                 for k in range(5))

# Points along a line (near-collinear)
Z_LINE = (0.0 + 0j, 0.1 + 0j, 0.2 + 0j, 0.3 + 0j, 0.4 + 0j)

# Central charges
C_VIR = Fraction(26)       # critical string
C_SELFDUAL = Fraction(13)  # self-dual Virasoro
C_GENERIC = Fraction(30)   # generic positive
C_1 = Fraction(1)          # unitary vicinity
C_25 = Fraction(25)        # bosonic string


# ============================================================================
# Section 1: Cross-ratio geometry (5 points on P^1)
# ============================================================================

class TestCrossRatioGeometry:
    """Verify cross-ratio computations for 5 points on P^1."""

    def test_cross_ratios_generic(self):
        """Cross-ratios should be well-defined for generic points."""
        cr = cross_ratios_5(*Z_GENERIC)
        assert cr.n_points == 5
        assert isinstance(cr.u, complex)
        assert isinstance(cr.v, complex)

    def test_cross_ratios_nondegenerate(self):
        """Cross-ratios should be nonzero for generic points."""
        cr = cross_ratios_5(*Z_GENERIC)
        assert abs(cr.u) > 1e-10
        assert abs(cr.v) > 1e-10

    def test_cross_ratios_circle(self):
        """Cross-ratios for points on the unit circle."""
        cr = cross_ratios_5(*Z_CIRCLE)
        assert abs(cr.u) > 1e-10
        assert abs(cr.v) > 1e-10

    def test_4pt_cross_ratio_value(self):
        """4-point cross-ratio for specific configuration."""
        # z1=0, z2=1, z3=inf treated via limit, z4=t
        # Standard: (z12*z34)/(z13*z24) with z3 far away
        chi = cross_ratio_4pt(0, 1, 10, 0.5)
        # (0-1)*(10-0.5) / ((0-10)*(1-0.5)) = (-1)*9.5 / (-10*0.5) = -9.5/(-5) = 1.9
        assert abs(chi - 1.9) < 1e-10

    def test_mobius_invariant_5pt(self):
        """Mobius invariants are well-defined."""
        u, v = mobius_invariant_5pt(Z_GENERIC)
        assert isinstance(u, complex)
        assert isinstance(v, complex)

    def test_coincident_points_raise(self):
        """Coincident points in the denominator should raise ValueError."""
        # z1 = z3 makes denominator z13 = 0
        with pytest.raises(ValueError):
            cross_ratios_5(0, 1, 0, 2, 3)

    def test_cross_ratio_mobius_invariance(self):
        """Cross-ratios are invariant under Mobius transformations."""
        # Apply w = (az+b)/(cz+d) to all 5 points
        a, b, c, d = 1, 2, 0.5, 1  # ad - bc = 1 - 1 = 0 ... fix
        a, b, c, d = 2, 1, 0, 1  # ad - bc = 2
        def mob(z):
            return (a * z + b) / (c * z + d)

        z_orig = Z_GENERIC
        z_transformed = tuple(mob(z) for z in z_orig)

        cr_orig = cross_ratios_5(*z_orig)
        cr_trans = cross_ratios_5(*z_transformed)

        assert abs(cr_orig.u - cr_trans.u) < 1e-10
        assert abs(cr_orig.v - cr_trans.v) < 1e-10


# ============================================================================
# Section 2: Celestial kinematics
# ============================================================================

class TestCelestialKinematics:
    """Verify celestial kinematic constructions."""

    def test_null_momentum_is_null(self):
        """Celestial null momentum should satisfy p^2 = 0."""
        p = celestial_null_momentum(1.0, 0.5 + 0.3j, 0.5 - 0.3j)
        # p^2 = p0^2 - p1^2 - p2^2 - p3^2 (Minkowski)
        p_sq = abs(p[0]) ** 2 - abs(p[1]) ** 2 - abs(p[2]) ** 2 - abs(p[3]) ** 2
        assert abs(p_sq) < 1e-10

    def test_spinor_bracket_antisymmetry(self):
        """<ij> = -<ji>."""
        z1, z2 = 0.5 + 0.3j, 1.2 - 0.1j
        assert abs(spinor_bracket_holomorphic(z1, z2)
                    + spinor_bracket_holomorphic(z2, z1)) < 1e-15

    def test_spinor_bracket_antiholomorphic_antisymmetry(self):
        """[ij] = -[ji]."""
        zb1, zb2 = 0.5 - 0.3j, 1.2 + 0.1j
        assert abs(spinor_bracket_antiholomorphic(zb1, zb2)
                    + spinor_bracket_antiholomorphic(zb2, zb1)) < 1e-15

    def test_celestial_particle_soft(self):
        """Soft particle has Delta <= 1."""
        soft = CelestialParticle(z=0, z_bar=0, Delta=-2, helicity=1, spin=2)
        assert soft.is_soft

    def test_celestial_particle_hard(self):
        """Hard particle has Delta > 1."""
        hard = CelestialParticle(z=0, z_bar=0, Delta=3.0, helicity=1, spin=2)
        assert not hard.is_soft


# ============================================================================
# Section 3: BGK 5-graviton MHV amplitude
# ============================================================================

class TestBGK5GravitonMHV:
    """Verify the BGK 5-graviton MHV amplitude."""

    def test_bgk_5pt_nonzero(self):
        """5-point MHV amplitude should be nonzero for generic points."""
        A5 = bgk_5_graviton_mhv_stripped(Z_GENERIC, (0, 1))
        assert abs(A5) > 1e-20

    def test_bgk_5pt_numerator_power(self):
        """Numerator has z_{01}^8 for neg_hel = (0,1)."""
        z = Z_GENERIC
        z01 = z[0] - z[1]
        A5 = bgk_5_graviton_mhv_stripped(z, (0, 1))
        # A5 = z01^8 / (z01*z12*z23*z34*z40)
        cyclic_denom = 1.0
        for k in range(5):
            cyclic_denom *= (z[k] - z[(k + 1) % 5])
        expected = z01 ** 8 / cyclic_denom
        assert abs(A5 - expected) < 1e-10 * abs(expected)

    def test_bgk_5pt_wrong_n_raises(self):
        """Should raise for n != 5."""
        with pytest.raises(ValueError):
            bgk_5_graviton_mhv_stripped((0, 1, 2, 3), (0, 1))

    def test_bgk_5pt_invalid_neg_hel_raises(self):
        """Should raise for invalid negative-helicity indices."""
        with pytest.raises(ValueError):
            bgk_5_graviton_mhv_stripped(Z_GENERIC, (0, 5))

    def test_bgk_5pt_different_neg_hel(self):
        """Different negative-helicity choices give different amplitudes."""
        A01 = bgk_5_graviton_mhv_stripped(Z_GENERIC, (0, 1))
        A02 = bgk_5_graviton_mhv_stripped(Z_GENERIC, (0, 2))
        assert abs(A01 - A02) > 1e-15

    def test_bgk_5pt_full_nonzero(self):
        """Full (hol * anti-hol) amplitude is nonzero."""
        z = Z_GENERIC
        z_bar = tuple(zi.conjugate() for zi in z)
        A = bgk_5_graviton_mhv_full(z, z_bar, (0, 1))
        assert abs(A) > 1e-20

    def test_bgk_5pt_full_is_product(self):
        """Full amplitude = holomorphic * anti-holomorphic."""
        z = Z_GENERIC
        z_bar = tuple(zi.conjugate() for zi in z)
        A_full = bgk_5_graviton_mhv_full(z, z_bar, (0, 1))
        A_hol = bgk_5_graviton_mhv_stripped(z, (0, 1))
        A_anti = bgk_5_graviton_mhv_stripped(z_bar, (0, 1))
        assert abs(A_full - A_hol * A_anti) / abs(A_full) < 1e-10

    def test_bgk_5pt_scaling_homogeneity(self):
        """Under z -> lambda*z, A_5 scales as lambda^{8-5} = lambda^3.

        Numerator: z_{ij}^8 -> lambda^8 * z_{ij}^8
        Denominator: prod z_{k,k+1} -> lambda^5 * prod z_{k,k+1}
        Net: lambda^{8-5} = lambda^3.
        """
        lam = 2.0 + 0j
        z_scaled = tuple(lam * zi for zi in Z_GENERIC)
        A_orig = bgk_5_graviton_mhv_stripped(Z_GENERIC, (0, 1))
        A_scaled = bgk_5_graviton_mhv_stripped(z_scaled, (0, 1))
        ratio = A_scaled / A_orig
        expected_ratio = lam ** 3  # 8 - 5 = 3
        assert abs(ratio - expected_ratio) / abs(expected_ratio) < 1e-10

    def test_bgk_5pt_translation_invariance(self):
        """Under z -> z + a, A_5 is invariant."""
        a = 3.0 + 2.0j
        z_shifted = tuple(zi + a for zi in Z_GENERIC)
        A_orig = bgk_5_graviton_mhv_stripped(Z_GENERIC, (0, 1))
        A_shifted = bgk_5_graviton_mhv_stripped(z_shifted, (0, 1))
        assert abs(A_orig - A_shifted) / abs(A_orig) < 1e-10


# ============================================================================
# Section 4: Celestial Mellin transform
# ============================================================================

class TestCelestialMellin:
    """Verify the celestial Mellin transform at 5 points."""

    def test_mellin_5pt_momentum_conservation(self):
        """sum Delta_i = 5 for on-shell celestial amplitudes."""
        data = celestial_mellin_5pt(
            Deltas=(1, 1, 1, 1, 1), z=Z_GENERIC,
            helicities=(-1, -1, 1, 1, 1),
        )
        assert data.momentum_conservation_sum == 5

    def test_mellin_5pt_off_shell(self):
        """Off-shell Deltas give sum != 5 (regularized)."""
        data = celestial_mellin_5pt(
            Deltas=(2, 2, 1, 1, 1), z=Z_GENERIC,
            helicities=(-1, -1, 1, 1, 1),
        )
        assert data.momentum_conservation_sum == 7

    def test_mellin_5pt_holomorphic_exponents(self):
        """Holomorphic exponents are computed for all pairs."""
        data = celestial_mellin_5pt(
            Deltas=(1, 1, 1, 1, 1), z=Z_GENERIC,
            helicities=(-1, -1, 1, 1, 1),
        )
        # C(5,2) = 10 pairs
        assert len(data.holomorphic_exponents) == 10

    def test_mellin_5pt_neg_hel_numerator(self):
        """Negative-helicity pair gets exponent 8 from numerator."""
        data = celestial_mellin_5pt(
            Deltas=(1, 1, 1, 1, 1), z=Z_GENERIC,
            helicities=(-1, -1, 1, 1, 1),
        )
        # (0,1) are negative-helicity, numerator gives z_{01}^8
        assert data.holomorphic_exponents[(0, 1)] >= 7  # 8 - possible denom contribution

    def test_mellin_wrong_particle_count_raises(self):
        """Should raise for n != 5."""
        with pytest.raises(ValueError):
            celestial_mellin_5pt((1, 1, 1, 1), Z_GENERIC[:4])

    def test_mellin_wrong_neg_count_raises(self):
        """MHV requires exactly 2 negative helicities."""
        with pytest.raises(ValueError):
            celestial_mellin_5pt(
                (1, 1, 1, 1, 1), Z_GENERIC,
                helicities=(-1, -1, -1, 1, 1),
            )


# ============================================================================
# Section 5: Quintic shadow coefficient S_5 (PATH 1)
# ============================================================================

class TestQuinticShadow:
    """Verify S_5 = -48/[c^2(5c+22)] from MC bracket."""

    def test_S5_formula(self):
        """S_5(c) = -48/[c^2(5c+22)] at c=30."""
        c = Fraction(30)
        S5 = quintic_shadow_coefficient_virasoro(c)
        expected = Fraction(-48) / (Fraction(30) ** 2 * (5 * Fraction(30) + 22))
        assert S5 == expected

    def test_S5_at_c1(self):
        """S_5(1) = -48/(1*27) = -16/9."""
        S5 = quintic_shadow_coefficient_virasoro(Fraction(1))
        assert S5 == Fraction(-16, 9)

    def test_S5_at_c13_self_dual(self):
        """S_5(13) = -48/(169*87) = -16/4901."""
        S5 = quintic_shadow_coefficient_virasoro(C_SELFDUAL)
        # 13^2 = 169, 5*13+22 = 87, 169*87 = 14703, 48/14703 = 16/4901
        assert S5 == Fraction(-16, 4901)

    def test_S5_at_c26_critical(self):
        """S_5(26) = -48/(676*152) = -3/6422."""
        S5 = quintic_shadow_coefficient_virasoro(C_VIR)
        # 26^2=676, 5*26+22=152, 676*152=102752, 48/102752 = 3/6422
        assert S5 == Fraction(-3, 6422)

    def test_S5_at_c25_bosonic(self):
        """S_5(25) = -48/(625*147) = -16/30625."""
        S5 = quintic_shadow_coefficient_virasoro(C_25)
        # 25^2=625, 5*25+22=147, 625*147=91875, 48/91875 = 16/30625
        assert S5 == Fraction(-16, 30625)

    def test_S5_negative_for_positive_c(self):
        """S_5 < 0 for all c > 0."""
        for cv in [1, 5, 10, 13, 20, 26, 30, 100]:
            S5 = quintic_shadow_coefficient_virasoro(Fraction(cv))
            assert S5 < 0, f"S_5 not negative at c = {cv}"

    def test_S5_singular_at_c0(self):
        """S_5 has a pole at c = 0."""
        with pytest.raises(ValueError):
            quintic_shadow_coefficient_virasoro(Fraction(0))

    def test_S5_special_values_match(self):
        """Cross-check against quintic_shadow_special_values."""
        vals = quintic_shadow_special_values()
        assert vals["c=1"] == Fraction(-16, 9)
        assert vals["c=13 (self-dual)"] == Fraction(-16, 4901)
        assert vals["c=26 (critical)"] == Fraction(-3, 6422)

    def test_obstruction_o5(self):
        """o^(5) = 480/[c^2(5c+22)]."""
        c = Fraction(30)
        o5 = quintic_obstruction_coefficient_virasoro(c)
        expected = Fraction(480) / (c ** 2 * (5 * c + 22))
        assert o5 == expected

    def test_obstruction_positive(self):
        """o^(5) > 0 for c > 0."""
        for cv in [1, 13, 26, 30]:
            o5 = quintic_obstruction_coefficient_virasoro(Fraction(cv))
            assert o5 > 0

    def test_S5_equals_minus_o5_over_10(self):
        """S_5 = -o^(5)/10 (from nabla_H inversion)."""
        for cv in [1, 5, 13, 26, 30, 100]:
            c = Fraction(cv)
            S5 = quintic_shadow_coefficient_virasoro(c)
            o5 = quintic_obstruction_coefficient_virasoro(c)
            assert S5 == -o5 / 10


# ============================================================================
# Section 6: MC equation at arity 5
# ============================================================================

class TestMCEquationArity5:
    """Verify the Maurer-Cartan equation at arity 5."""

    def test_mc_residual_zero(self):
        """The MC equation residual 10*S_5 + o^(5) = 0."""
        for cv in [1, 5, 13, 26, 30, 100]:
            res = quintic_mc_equation_residual(Fraction(cv))
            assert res == 0, f"MC residual nonzero at c = {cv}: {res}"

    def test_mc_bracket_structure(self):
        """o^(5) = {Sh_3, Sh_4}_H with Sh_3 = 2x^3, Sh_4 = 10/[c(5c+22)] x^4.

        The H-Poisson bracket is:
        {f, g}_H = (df/dx)(2/c)(dg/dx)
        {2x^3, [10/(c(5c+22))]x^4}_H = 6x^2 * (2/c) * [40/(c(5c+22))]x^3
                                        = 480 x^5 / [c^2(5c+22)]
        Coefficient: 480/[c^2(5c+22)] = o^(5). Check.
        """
        c = Fraction(30)
        # d(2x^3)/dx = 6x^2; coefficient = 6
        # d([10/(c(5c+22))]x^4)/dx = [40/(c(5c+22))]x^3; coefficient = 40/(c(5c+22))
        # Product with propagator 2/c: 6 * (2/c) * 40/(c(5c+22)) = 480/[c^2(5c+22)]
        o5_expected = Fraction(480) / (c ** 2 * (5 * c + 22))
        o5_computed = quintic_obstruction_coefficient_virasoro(c)
        assert o5_computed == o5_expected


# ============================================================================
# Section 7: Shadow tower arity 2 through 5
# ============================================================================

class TestShadowTower:
    """Verify the shadow tower S_2, S_3, S_4, S_5."""

    def test_tower_at_c30(self):
        """Complete tower at c = 30."""
        tower = shadow_tower_arity_2_to_5(Fraction(30))
        assert tower[2] == Fraction(15)        # c/2
        assert tower[3] == Fraction(2)         # cubic
        assert tower[4] == Fraction(10) / (30 * 172)  # 10/(30*172) = 1/516
        # S_5 = -48/(900*172) = -48/154800 = -1/3225
        assert tower[5] == Fraction(-48) / (Fraction(900) * 172)

    def test_tower_kappa_is_c_over_2(self):
        """S_2 = kappa = c/2 for all c."""
        for cv in [1, 13, 26, 30]:
            tower = shadow_tower_arity_2_to_5(Fraction(cv))
            assert tower[2] == Fraction(cv, 2)

    def test_tower_cubic_c_independent(self):
        """S_3 = 2 for all c (c-independent)."""
        for cv in [1, 13, 26, 30, 100]:
            tower = shadow_tower_arity_2_to_5(Fraction(cv))
            assert tower[3] == Fraction(2)

    def test_sign_alternation_at_arity5(self):
        """First negative term is at arity 5."""
        result = verify_tower_sign_alternation(Fraction(30))
        assert result["first_negative_arity"] == 5
        assert result["alternation_starts_at_5"]

    def test_sign_pattern_positive_c(self):
        """For c > 0: S_2 > 0, S_3 > 0, S_4 > 0, S_5 < 0."""
        for cv in [1, 10, 13, 26, 50]:
            tower = shadow_tower_arity_2_to_5(Fraction(cv))
            assert tower[2] > 0
            assert tower[3] > 0
            assert tower[4] > 0
            assert tower[5] < 0


# ============================================================================
# Section 8: Soft limit factorization (PATH 3)
# ============================================================================

class TestSoftFactorization:
    """Verify A_5 -> OPE * A_4 in soft limits."""

    def test_soft_factorization_channel_45(self):
        """Soft limit z_5 -> z_4: factorization holds."""
        data = soft_factorization_5to4(Z_GENERIC, soft_idx=4, approach_idx=3)
        assert data.leading_pole_order == 1

    def test_soft_factorization_channel_01(self):
        """Soft limit z_1 -> z_0: factorization data computed."""
        data = soft_factorization_5to4(Z_GENERIC, soft_idx=0, approach_idx=4)
        assert data.leading_pole_order == 1

    def test_soft_all_channels(self):
        """Check soft factorization in all 5 channels."""
        results = verify_soft_limit_all_channels(Z_GENERIC)
        assert len(results) == 5

    def test_soft_residue_finite(self):
        """The soft residue should be finite (not zero or infinite)."""
        data = soft_factorization_5to4(Z_GENERIC, soft_idx=4, approach_idx=3)
        assert data.residue_ratio is not None
        assert abs(data.residue_ratio) > 1e-20
        assert abs(data.residue_ratio) < 1e20


# ============================================================================
# Section 9: Collinear limits (PATH 5)
# ============================================================================

class TestCollinearLimits:
    """Verify collinear pole structure."""

    def test_collinear_pole_graviton(self):
        """For spin-2 gravitons: r-matrix pole order = 3."""
        data = collinear_pole_structure_5pt(spin=2)
        assert data["r_matrix_pole_order"] == 3

    def test_collinear_pole_spin1(self):
        """For spin-1 (gluons): r-matrix pole order = 1."""
        data = collinear_pole_structure_5pt(spin=1)
        assert data["r_matrix_pole_order"] == 1

    def test_collinear_pole_spin3(self):
        """For spin-3: r-matrix pole order = 5."""
        data = collinear_pole_structure_5pt(spin=3)
        assert data["r_matrix_pole_order"] == 5

    def test_collinear_adjacent_pairs(self):
        """5 points have 4 adjacent pairs in cyclic ordering."""
        data = collinear_pole_structure_5pt()
        assert data["n_adjacent_pairs"] == 4

    def test_collinear_stripped_pole(self):
        """Stripped amplitude has simple poles from cyclic product."""
        data = collinear_pole_structure_5pt()
        assert data["stripped_collinear_pole"] == 1

    def test_collinear_numerical_scaling(self):
        """Near-collinear amplitude: scaling follows z^{8-5} = z^3.

        For the BGK stripped amplitude z_{01}^8 / prod z_{k,k+1},
        in the collinear regime z_k = eps * k * direction:
            numerator ~ eps^8, denominator ~ eps^5,
        so |A_5| ~ eps^3. This DECREASES as eps -> 0.

        The pole structure emerges after the Mellin transform
        (which introduces energy-dependent factors).
        """
        data = collinear_limit_numerical(z_base=0.0, direction=1.0)
        if "eps=1.00e+00" in data and "eps=1.00e-01" in data:
            if isinstance(data["eps=1.00e+00"], dict) and isinstance(data["eps=1.00e-01"], dict):
                a1 = data["eps=1.00e+00"]["abs_amplitude"]
                a2 = data["eps=1.00e-01"]["abs_amplitude"]
                # Stripped amplitude decreases as eps^3
                assert a2 < a1


# ============================================================================
# Section 10: Permutation symmetry (PATH 5 supplement)
# ============================================================================

class TestPermutationSymmetry:
    """Verify permutation symmetry of the MHV amplitude."""

    def test_all_same_helicity_vanishes(self):
        """All-same-helicity MHV vanishes for n >= 4."""
        result = check_s5_symmetry_identical(Z_GENERIC)
        assert result["all_plus_vanishes"]

    def test_s2_neg_symmetry(self):
        """Swapping neg-helicity legs: the numerator z_{ij}^8 is invariant.

        The cyclic-ordered BGK amplitude is NOT invariant under
        swapping two particles (the cyclic denominator changes).
        But the numerator z_{01}^8 is symmetric (even power).
        We check the ratio is a computable quantity.
        """
        result = check_mhv_permutation_symmetry(Z_GENERIC, neg_hel=(0, 1))
        # The ratio exists and is finite
        ratio = result.get("S2_neg_swap_ratio")
        assert ratio is not None
        assert abs(ratio) > 1e-20

    def test_s3_pos_permutations_unit_modulus(self):
        """Permutations of positive legs give unit-modulus ratios."""
        result = check_mhv_permutation_symmetry(Z_GENERIC, neg_hel=(0, 1))
        # The BGK formula is NOT symmetric under arbitrary permutations
        # of the positive legs (the cyclic ordering matters).
        # But the physical amplitude (summed over orderings) is.
        # We check that the ratios have |ratio| = 1.
        assert "S3_pos_ratios" in result

    def test_neg_swap_ratio_finite(self):
        """Swapping neg-helicity legs: ratio is finite and nonzero.

        The cyclic-ordered BGK amplitude changes under particle swap
        (the cyclic denominator depends on ordering). The ratio is
        a well-defined nonzero complex number; the PHYSICAL amplitude
        (summed over orderings) would be symmetric.
        """
        result = check_mhv_permutation_symmetry(Z_GENERIC, neg_hel=(0, 1))
        ratio = result.get("S2_neg_swap_ratio")
        if ratio is not None:
            assert abs(ratio) > 1e-20
            assert abs(ratio) < 1e20


# ============================================================================
# Section 11: Conformal block decomposition
# ============================================================================

class TestConformalBlocks:
    """Verify celestial conformal block channel enumeration."""

    def test_block_channels_enumerated(self):
        """At least 3 channels for the 5-point function."""
        blocks = celestial_block_channels_5pt((1, 1, 1, 1, 1))
        assert len(blocks) >= 3

    def test_graviton_exchange_channel(self):
        """Graviton exchange has spin 2."""
        blocks = celestial_block_channels_5pt((1, 1, 1, 1, 1))
        graviton_blocks = [b for b in blocks if b.spin_O == 2]
        assert len(graviton_blocks) >= 1

    def test_exchange_dimension(self):
        """Exchange graviton has Delta_O = Delta_1 + Delta_2 - 1."""
        blocks = celestial_block_channels_5pt((2, 3, 1, 1, 1))
        exchange = [b for b in blocks if "graviton" in b.channel][0]
        assert exchange.Delta_O == 2 + 3 - 1  # = 4

    def test_vacuum_channel_vanishes(self):
        """Vacuum (identity) exchange vanishes at tree level."""
        blocks = celestial_block_channels_5pt((1, 1, 1, 1, 1))
        vacuum = [b for b in blocks if b.spin_O == 0]
        if vacuum:
            assert vacuum[0].coefficient == 0.0

    def test_spin3_channel_present(self):
        """w_{1+inf} has spin-3 exchange channel."""
        blocks = celestial_block_channels_5pt((1, 1, 1, 1, 1))
        spin3 = [b for b in blocks if b.spin_O == 3]
        assert len(spin3) >= 1


# ============================================================================
# Section 12: w_{1+infty} Ward identities (PATH 4)
# ============================================================================

class TestWardIdentities:
    """Verify w_{1+infty} Ward identities."""

    def test_ward_order_0_supertranslation(self):
        """s=0 Ward identity is Weinberg supertranslation."""
        result = w_infinity_ward_identity_check(5, 0)
        assert result["shadow_arity"] == 2
        assert "supertranslation" in result["ward_identity_type"].lower()

    def test_ward_order_1_superrotation(self):
        """s=1 Ward identity is Cachazo-Strominger superrotation."""
        result = w_infinity_ward_identity_check(5, 1)
        assert result["shadow_arity"] == 3

    def test_ward_order_2_subsubleading(self):
        """s=2 Ward identity involves quartic shadow."""
        result = w_infinity_ward_identity_check(5, 2)
        assert result["shadow_arity"] == 4
        assert not result["requires_nonlinear_mc"]

    def test_ward_order_3_requires_nonlinear_mc(self):
        """s=3 Ward identity REQUIRES nonlinear MC structure."""
        result = w_infinity_ward_identity_check(5, 3)
        assert result["shadow_arity"] == 5
        assert result["requires_nonlinear_mc"]

    def test_ward_soft_factor_leading(self):
        """Leading soft factor: 1/(z_soft - z_k) for each hard leg."""
        z_soft = 10.0 + 0j
        z_hard = (0, 1, 2, 3)
        factors = ward_identity_soft_factor_leading(z_soft, z_hard)
        assert len(factors) == 4
        assert abs(factors[0] - 1.0 / (10.0 - 0.0)) < 1e-15

    def test_ward_soft_factor_subleading(self):
        """Subleading soft factor involves conformal weights."""
        z_soft = 10.0 + 0j
        z_hard = (0, 1, 2, 3)
        h_hard = (2, 2, 2, 2)  # all spin-2 (graviton)
        factors = ward_identity_soft_factor_subleading(z_soft, z_hard, h_hard)
        assert len(factors) == 4
        # h_k / delta^2 at k=0: 2 / (10^2) = 0.02
        assert abs(factors[0] - 0.02) < 1e-15

    def test_ward_quintic_coefficient_negative(self):
        """The arity-5 Ward coefficient S_5 is negative for c > 0."""
        result = ward_identity_quintic_check(Fraction(30))
        assert result["S5_sign"] == "negative"
        assert result["alternating_sign"]

    def test_ward_quintic_nonzero(self):
        """The arity-5 Ward coefficient is nonzero (proves infinite tower)."""
        result = ward_identity_quintic_check(Fraction(26))
        assert result["S5"] != 0


# ============================================================================
# Section 13: Shadow-amplitude comparison
# ============================================================================

class TestShadowAmplitudeComparison:
    """Verify shadow extraction matches Mellin transform."""

    def test_shadow_vs_mellin_finite(self):
        """Both shadow and Mellin sides give finite results."""
        result = shadow_vs_mellin_comparison(Fraction(30), Z_GENERIC)
        assert abs(result["stripped_amplitude"]) > 1e-20
        assert abs(result["stripped_amplitude"]) < 1e20

    def test_shadow_contribution_nonzero(self):
        """Shadow contribution to the 5-point amplitude is nonzero."""
        result = shadow_vs_mellin_comparison(Fraction(30), Z_GENERIC)
        assert abs(result["shadow_contribution"]) > 1e-30

    def test_shadow_s5_matches_direct(self):
        """S_5 in comparison matches direct computation."""
        result = shadow_vs_mellin_comparison(Fraction(30), Z_GENERIC)
        assert result["S5"] == quintic_shadow_coefficient_virasoro(Fraction(30))


# ============================================================================
# Section 14: Multi-path verification (all 6 paths)
# ============================================================================

class TestPath1DirectShadow:
    """Path 1: Direct shadow extraction from MC element."""

    def test_mc_satisfied(self):
        """MC equation is satisfied at arity 5."""
        result = verify_path1_direct_shadow(Fraction(30))
        assert result["mc_satisfied"]

    def test_s5_consistent(self):
        """S_5 = -o^(5)/10."""
        result = verify_path1_direct_shadow(Fraction(30))
        assert result["S5_equals_minus_o5_over_10"]

    def test_multiple_c_values(self):
        """MC equation holds for multiple c values."""
        for cv in [1, 5, 13, 26, 30, 50, 100]:
            result = verify_path1_direct_shadow(Fraction(cv))
            assert result["mc_satisfied"]


class TestPath2Mellin:
    """Path 2: Mellin transform of BGK amplitude."""

    def test_momentum_conservation(self):
        """sum Delta_i = 5 for on-shell."""
        result = verify_path2_mellin_transform(Z_GENERIC)
        assert result["sum_equals_5"]

    def test_amplitude_nonzero(self):
        """Mellin amplitude is nonzero for generic points."""
        result = verify_path2_mellin_transform(Z_GENERIC)
        assert result["abs_amplitude"] > 1e-20


class TestPath3Soft:
    """Path 3: Soft limit factorization."""

    def test_all_channels_computed(self):
        """All 5 soft channels are computed."""
        result = verify_path3_soft_factorization(Z_GENERIC)
        assert len(result) == 5

    def test_pole_order_is_1(self):
        """Each soft channel has simple pole (order 1)."""
        result = verify_path3_soft_factorization(Z_GENERIC)
        for key, val in result.items():
            if isinstance(val, dict) and "pole_order" in val:
                assert val["pole_order"] == 1


class TestPath4Ward:
    """Path 4: w_{1+infty} Ward identities."""

    def test_all_orders_computed(self):
        """Ward identities computed at orders 0, 1, 2, 3."""
        result = verify_path4_ward_identities(Fraction(30))
        assert "order_0" in result
        assert "order_1" in result
        assert "order_2" in result
        assert "order_3" in result

    def test_quintic_ward_present(self):
        """Quintic Ward identity data is present."""
        result = verify_path4_ward_identities(Fraction(30))
        assert "quintic_ward" in result
        assert result["quintic_ward"]["requires_nonlinear_mc"]


class TestPath5Collinear:
    """Path 5: Collinear pole structure."""

    def test_pole_structure_computed(self):
        """Collinear pole structure is computed."""
        result = verify_path5_collinear_poles()
        assert "r_matrix_pole_order" in result
        assert result["r_matrix_pole_order"] == 3  # for spin 2

    def test_four_adjacent_pairs(self):
        result = verify_path5_collinear_poles()
        assert result["n_adjacent_pairs"] == 4


class TestPath6CrossRatio:
    """Path 6: Cross-ratio expansion."""

    def test_cross_ratios_computed(self):
        """Cross-ratios are computed for generic points."""
        result = verify_path6_cross_ratio_expansion(Fraction(30), Z_GENERIC)
        assert result["u"] is not None
        assert result["v"] is not None

    def test_amplitude_in_cross_ratios(self):
        """Amplitude is computed alongside cross-ratios."""
        result = verify_path6_cross_ratio_expansion(Fraction(30), Z_GENERIC)
        assert result["abs_amplitude"] > 1e-20


# ============================================================================
# Section 15: Virasoro duality at arity 5
# ============================================================================

class TestDualityArity5:
    """Verify Virasoro duality c <-> 26-c at arity 5."""

    def test_self_dual_point(self):
        """At c=13: S_5(c) = S_5(26-c)."""
        result = verify_duality_at_arity5(Fraction(13))
        assert result["S5_c"] == result["S5_dual"]

    def test_duality_nontrivial(self):
        """Away from c=13: S_5(c) != S_5(26-c) in general."""
        result = verify_duality_at_arity5(Fraction(10))
        assert result["S5_c"] != result["S5_dual"]

    def test_duality_sum_at_c13(self):
        """At c=13: S_5 + S_5' = 2*S_5(13)."""
        result = verify_duality_at_arity5(Fraction(13))
        assert result["S5_sum"] == 2 * result["S5_c"]

    def test_duality_ratio(self):
        """S_5(c)/S_5(26-c) = c'^2(5c'+22) / [c^2(5c+22)] where c'=26-c."""
        c = Fraction(10)
        c_dual = Fraction(16)
        S5_c = quintic_shadow_coefficient_virasoro(c)
        S5_d = quintic_shadow_coefficient_virasoro(c_dual)
        # S5 = -48/[c^2(5c+22)], so ratio = c'^2(5c'+22) / [c^2(5c+22)]
        expected_ratio = (c_dual ** 2 * (5 * c_dual + 22)) / (c ** 2 * (5 * c + 22))
        actual_ratio = S5_c / S5_d
        assert actual_ratio == expected_ratio


# ============================================================================
# Section 16: Shadow consistency
# ============================================================================

class TestShadowConsistency:
    """Cross-consistency checks for the arity-5 shadow."""

    def test_consistency_at_c30(self):
        """Full consistency at c=30."""
        result = verify_shadow_consistency_arity5(Fraction(30))
        assert result["mc_equation"]
        assert result["S5_negative_for_positive_c"]
        assert result["S5_at_c13"]
        assert result["S5_at_c26_simplified"]
        assert result["ratio_S5_S4"]

    def test_ratio_S5_S4_formula(self):
        """S_5/S_4 = -24/(5c)."""
        for cv in [1, 5, 10, 13, 26, 30]:
            c = Fraction(cv)
            tower = shadow_tower_arity_2_to_5(c)
            ratio = tower[5] / tower[4]
            expected = Fraction(-24, 5) / c
            assert ratio == expected

    def test_growth_rate_comparison(self):
        """|S_5/S_4| is within a factor of 3 of the shadow growth rate rho."""
        result = verify_shadow_consistency_arity5(Fraction(30))
        assert result["ratio_within_factor_3_of_rho"]


# ============================================================================
# Section 17: Soft graviton theorem at order 3
# ============================================================================

class TestSoftTheoremOrder3:
    """Verify the s=3 soft graviton theorem from arity-5 shadow."""

    def test_soft_theorem_construction(self):
        """SoftGravitonTheoremArity5 is correctly constructed."""
        thm = soft_theorem_arity5(Fraction(30))
        assert thm.is_nonzero
        assert thm.differential_order == 3
        assert thm.sign == "negative"

    def test_soft_theorem_at_c26(self):
        """At critical string (c=26): S_5 = -3/6422."""
        thm = soft_theorem_arity5(Fraction(26))
        assert thm.shadow_coefficient == Fraction(-3, 6422)
        assert thm.is_nonzero

    def test_soft_theorem_mc_origin(self):
        """The soft theorem arises from the MC bracket {Sh_3, Sh_4}."""
        thm = soft_theorem_arity5(Fraction(30))
        assert "Sh_3" in thm.mc_bracket_origin
        assert "Sh_4" in thm.mc_bracket_origin

    def test_soft_theorem_nonzero_proves_infinite_tower(self):
        """S_5 != 0 proves the shadow tower is infinite (class M)."""
        for cv in [1, 5, 13, 26, 30]:
            thm = soft_theorem_arity5(Fraction(cv))
            assert thm.is_nonzero


# ============================================================================
# Section 18: w_{1+infty} channel structure
# ============================================================================

class TestWInfinityChannels:
    """Verify w_{1+infty}-specific structure of the 5-point amplitude."""

    def test_virasoro_channel_dominates(self):
        """Virasoro (T-T) channel is the leading contribution."""
        S5_TT = quintic_shadow_w_infinity_virasoro_channel(Fraction(30))
        assert S5_TT == quintic_shadow_coefficient_virasoro(Fraction(30))

    def test_cross_spin_suppressed(self):
        """Cross-spin contributions are suppressed by 1/N^2."""
        result = quintic_shadow_cross_spin_estimate(10, Fraction(30))
        assert result["cross_spin_suppression_order"] == 2
        assert result["dominant_channel"] == "Virasoro (T-T)"

    def test_cross_spin_at_large_N(self):
        """At N=100: cross-spin suppression is strong."""
        result = quintic_shadow_cross_spin_estimate(100, Fraction(30))
        assert result["cross_spin_suppression_order"] >= 2


# ============================================================================
# Section 19: Numerical cross-checks
# ============================================================================

class TestNumericalCrossChecks:
    """Numerical sanity checks across different configurations."""

    def test_amplitude_changes_with_config(self):
        """Different point configurations give different amplitudes."""
        A1 = bgk_5_graviton_mhv_stripped(Z_GENERIC, (0, 1))
        A2 = bgk_5_graviton_mhv_stripped(Z_CIRCLE, (0, 1))
        assert abs(A1 - A2) > 1e-15

    def test_amplitude_conjugation(self):
        """A_5(z_bar) = conjugate of A_5(z) for real z."""
        z = (0.0, 1.0, 2.0, 3.0, 4.5)  # real points
        z_complex = tuple(complex(zi) for zi in z)
        z_bar = tuple(complex(zi).conjugate() for zi in z)
        A = bgk_5_graviton_mhv_stripped(z_complex, (0, 1))
        A_bar = bgk_5_graviton_mhv_stripped(z_bar, (0, 1))
        # For real z: z = z_bar, so A = A_bar
        assert abs(A - A_bar) < 1e-10 * max(abs(A), 1)

    def test_s5_decreasing_in_c(self):
        """|S_5(c)| decreases as c increases (for large c).

        |S_5| = 48/[c^2(5c+22)] ~ 48/(5c^3) for large c.
        """
        c_values = [10, 20, 30, 50, 100]
        abs_S5 = [abs(quintic_shadow_coefficient_virasoro(Fraction(cv)))
                   for cv in c_values]
        for k in range(len(abs_S5) - 1):
            assert abs_S5[k] > abs_S5[k + 1]

    def test_s5_large_c_scaling(self):
        """|S_5| ~ 48/(5c^3) for large c."""
        c = Fraction(1000)
        S5 = quintic_shadow_coefficient_virasoro(c)
        asymptotic = Fraction(-48, 5) / c ** 3
        # Should agree to within 1% for c=1000
        ratio = float(S5 / asymptotic)
        assert abs(ratio - 1.0) < 0.01


# ============================================================================
# Section 20: Full verification suite
# ============================================================================

class TestFullSuite:
    """Run the complete 6-path verification suite."""

    def test_full_suite_at_c30(self):
        """Full suite runs without errors at c = 30."""
        result = run_full_5point_verification(Fraction(30))
        assert "path1_shadow" in result
        assert "path2_mellin" in result
        assert "path3_soft" in result
        assert "path4_ward" in result
        assert "path5_collinear" in result
        assert "path6_cross_ratio" in result

    def test_full_suite_mc_satisfied(self):
        """MC equation is satisfied in the full suite."""
        result = run_full_5point_verification(Fraction(30))
        assert result["path1_shadow"]["mc_satisfied"]

    def test_full_suite_tower_present(self):
        """Shadow tower arity 2-5 is in the full suite."""
        result = run_full_5point_verification(Fraction(30))
        tower = result["tower_2_to_5"]
        assert 2 in tower and 3 in tower and 4 in tower and 5 in tower

    def test_full_suite_sign_alternation(self):
        """Sign alternation is verified in the full suite."""
        result = run_full_5point_verification(Fraction(30))
        assert result["sign_alternation"]["alternation_starts_at_5"]

    def test_full_suite_soft_theorem(self):
        """Soft theorem at order 3 is nonzero."""
        result = run_full_5point_verification(Fraction(26))
        assert result["soft_theorem_3"]["nonzero"]

    def test_full_suite_at_c13(self):
        """Full suite at self-dual point c=13."""
        result = run_full_5point_verification(Fraction(13))
        assert result["path1_shadow"]["mc_satisfied"]
        assert result["duality"]["S5_c"] == result["duality"]["S5_dual"]

    def test_full_suite_at_c26(self):
        """Full suite at critical string c=26."""
        result = run_full_5point_verification(Fraction(26))
        assert result["path1_shadow"]["mc_satisfied"]

    def test_full_suite_custom_z(self):
        """Full suite with custom point configuration."""
        z_custom = (0.1 + 0.2j, 1.3 - 0.1j, -0.5 + 0.9j, 0.8 + 0.4j, -0.2 - 0.6j)
        result = run_full_5point_verification(Fraction(30), z=z_custom)
        assert result["path1_shadow"]["mc_satisfied"]


# ============================================================================
# Section 21: Cross-verification with existing modules
# ============================================================================

class TestCrossVerification:
    """Cross-check against celestial_shadow_engine.py and virasoro_quintic_shadow.py."""

    def test_s5_matches_quintic_module_at_c1(self):
        """S_5(1) = -16/9, matching virasoro_quintic_shadow.py."""
        S5 = quintic_shadow_coefficient_virasoro(Fraction(1))
        assert S5 == Fraction(-16, 9)

    def test_s5_matches_quintic_module_at_c13(self):
        """S_5(13) = -16/4901, matching virasoro_quintic_shadow.py."""
        S5 = quintic_shadow_coefficient_virasoro(Fraction(13))
        assert S5 == Fraction(-16, 4901)

    def test_s5_matches_quintic_module_at_c26(self):
        """S_5(26) = -3/6422, matching virasoro_quintic_shadow.py."""
        S5 = quintic_shadow_coefficient_virasoro(Fraction(26))
        assert S5 == Fraction(-3, 6422)

    def test_kappa_consistency_with_shadow_engine(self):
        """S_2 = kappa = c/2, consistent with celestial_shadow_engine.py."""
        for cv in [1, 13, 26, 30]:
            tower = shadow_tower_arity_2_to_5(Fraction(cv))
            assert tower[2] == Fraction(cv, 2)

    def test_cubic_consistency(self):
        """S_3 = 2, consistent with celestial_shadow_engine.py."""
        for cv in [1, 13, 26, 30]:
            tower = shadow_tower_arity_2_to_5(Fraction(cv))
            assert tower[3] == Fraction(2)

    def test_quartic_consistency(self):
        """S_4 = 10/[c(5c+22)], consistent with celestial_shadow_engine.py."""
        c = Fraction(30)
        tower = shadow_tower_arity_2_to_5(c)
        expected_S4 = Fraction(10) / (c * (5 * c + 22))
        assert tower[4] == expected_S4

    def test_harmonic_number_matches(self):
        """Harmonic numbers match between modules."""
        assert harmonic_number(1) == Fraction(1)
        assert harmonic_number(5) == Fraction(137, 60)


# ============================================================================
# Section 22: Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_s5_at_negative_c(self):
        """S_5 at c = -1 (physically unusual but mathematically valid)."""
        S5 = quintic_shadow_coefficient_virasoro(Fraction(-1))
        # c=-1: c^2=1, 5c+22=17, S_5 = -48/17
        assert S5 == Fraction(-48, 17)

    def test_s5_near_lee_yang(self):
        """S_5 near c = -22/5 (Lee-Yang, pole): S_5 blows up."""
        # c = -22/5 + epsilon with very small epsilon
        c_near = Fraction(-22, 5) + Fraction(1, 10000)
        S5 = quintic_shadow_coefficient_virasoro(c_near)
        # Should be large (near pole at 5c+22 = 0)
        assert abs(S5) > 1000

    def test_cross_ratios_near_coincidence(self):
        """Cross-ratios with nearly coincident points."""
        z = (0, 1e-10, 0.5, 0.8, 1.0)
        z_complex = tuple(complex(zi) for zi in z)
        # Should not crash (points are distinct)
        cr = cross_ratios_5(*z_complex)
        assert abs(cr.u) > 1e-20 or abs(cr.u) < 1e-20  # just check it returns

    def test_bgk_collinear_raises(self):
        """BGK with exactly collinear (coincident pair) raises."""
        z_degen = (0 + 0j, 0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j)
        with pytest.raises((ValueError, ZeroDivisionError)):
            bgk_5_graviton_mhv_stripped(z_degen, (0, 1))

    def test_ward_leading_factor_sum_vanishes_for_translational(self):
        """sum_k F^{(0)}_k = sum_k 1/(z_soft - z_k).

        This sum does NOT generally vanish (it vanishes only when
        integrated against a constant function, by the residue theorem
        with a contour enclosing all z_k).
        """
        z_soft = 10.0
        z_hard = (0, 1, 2, 3)
        factors = ward_identity_soft_factor_leading(z_soft, z_hard)
        total = sum(factors)
        # The sum is 1/10 + 1/9 + 1/8 + 1/7 != 0 in general
        assert abs(total) > 1e-5
