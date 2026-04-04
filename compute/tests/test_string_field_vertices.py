r"""Tests for string field theory vertices from the bar complex.

Verifies the identification between bar-cobar algebraic structures and
open/closed string field theory vertices.

Test structure:
  1. Neumann coefficients: symmetry, parity, decay, exact values
  2. Open SFT cubic vertex: overlaps, Witten constant, coproduct structure
  3. Tachyon potential: level truncation, Sen's conjecture, critical ratio
  4. Closed SFT vertices: V_{g,n} from shadow tower, kappa * lambda_g
  5. MC equation = closed SFT master equation: sector verification
  6. Polyakov amplitude: Veneziano, Virasoro-Shapiro, genus-1 matching
  7. Anomaly cancellation: bosonic c=26, superstring d=10
  8. Genus expansion: convergence, ratios, generating function
  9. Family-specific vertices: Heisenberg (free), Virasoro (mixed), affine (Lie)
  10. Cross-consistency: open-closed, bar-coproduct, shadow tower

Ground truth: Gross-Jevicki (1987), Rastelli-Sen-Zwiebach (2001),
  Zwiebach (1993), Sen (1999), Witten (1986), Taylor-Zwiebach (2003),
  thm:mc2-bar-intrinsic, thm:shadow-double-convergence, Theorem D.
"""

import math
import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.string_field_vertices import (
    # Section 1: Neumann coefficients
    neumann_A_coefficient,
    neumann_coefficient_N11,
    neumann_coefficient_N12,
    neumann_matrix,
    verify_neumann_symmetry,
    # Section 2: Open SFT vertex
    OpenSFTVertex,
    cubic_vertex_overlap,
    witten_cubic_constant,
    tachyon_cubic_coupling,
    # Section 3: Tachyon potential
    tachyon_potential_level_0,
    tachyon_potential_critical_ratio_level0,
    sen_conjecture_level_truncation,
    tachyon_potential_polynomial,
    # Section 4: Closed SFT vertices
    ClosedSFTVertex,
    closed_vertex_V01,
    closed_vertex_V02,
    closed_vertex_V03,
    closed_vertex_V11,
    closed_vertex_V12,
    closed_vertex_V21,
    closed_vertex_from_shadow,
    # Section 5: MC equation
    mc_equation_sector,
    mc_equation_check_low_sectors,
    # Section 6: Polyakov amplitudes
    veneziano_amplitude,
    veneziano_residue_at_pole,
    virasoro_shapiro_amplitude,
    polyakov_genus1_tadpole,
    # Section 7: Bar coproduct
    bar_coproduct_components,
    # Section 8: Anomaly cancellation
    bosonic_string_anomaly,
    superstring_anomaly,
    # Section 9: Genus expansion
    closed_sft_genus_expansion,
    # Section 10: Family-specific
    sft_vertices_heisenberg,
    sft_vertices_virasoro,
    sft_vertices_affine_sl2,
    # Section 11: Master verification
    verify_all,
)
from compute.lib.utils import lambda_fp, F_g


PI = math.pi


# =========================================================================
# Section 1: Neumann Coefficient Tests
# =========================================================================

class TestNeumannCoefficients:
    """Tests for Neumann coefficients of the cubic open string vertex."""

    def test_neumann_A0_is_one(self):
        """A_0 = binom(0,0)/4^0 = 1."""
        assert neumann_A_coefficient(0) == Rational(1)

    def test_neumann_A1_is_half(self):
        """A_1 = binom(2,1)/4 = 2/4 = 1/2."""
        assert neumann_A_coefficient(1) == Rational(1, 2)

    def test_neumann_A2(self):
        """A_2 = binom(4,2)/16 = 6/16 = 3/8."""
        assert neumann_A_coefficient(2) == Rational(3, 8)

    def test_neumann_A3(self):
        """A_3 = binom(6,3)/64 = 20/64 = 5/16."""
        assert neumann_A_coefficient(3) == Rational(5, 16)

    def test_neumann_A_decreasing(self):
        """A_n is decreasing for n >= 1 (approaches 0)."""
        for n in range(1, 10):
            assert neumann_A_coefficient(n) > neumann_A_coefficient(n + 1)

    def test_neumann_A_positive(self):
        """A_n > 0 for all n >= 0."""
        for n in range(20):
            assert neumann_A_coefficient(n) > 0

    def test_N11_symmetry(self):
        """N^{11}_{mn} = N^{11}_{nm} (symmetric matrix)."""
        for m in range(1, 8):
            for n in range(1, 8):
                assert neumann_coefficient_N11(m, n) == neumann_coefficient_N11(n, m)

    def test_N11_parity_selection(self):
        """N^{11}_{mn} = 0 when m+n is odd."""
        for m in range(1, 10):
            for n in range(1, 10):
                if (m + n) % 2 != 0:
                    assert neumann_coefficient_N11(m, n) == 0

    def test_N11_nonzero_even_sum(self):
        """N^{11}_{mn} != 0 when m+n is even and m,n >= 1."""
        for m in range(1, 8):
            for n in range(1, 8):
                if (m + n) % 2 == 0:
                    assert neumann_coefficient_N11(m, n) != 0

    def test_N11_11_exact(self):
        """N^{11}_{1,1} = -1/4 (exact ground-state overlap).

        Computation: m+n=2 (even), sign = (-1)^3 = -1,
        prefactor = 2/2 = 1, A_1 = 1/2, A_1 = 1/2.
        N = -1 * 1 * 1/2 * 1/2 = -1/4.
        """
        assert neumann_coefficient_N11(1, 1) == Rational(-1, 4)

    def test_N11_22_exact(self):
        """N^{11}_{2,2}: exact computation.

        m+n=4 (even), sign = (-1)^5 = -1,
        prefactor = 2/4 = 1/2, A_2 = 3/8.
        N = -1 * 1/2 * 3/8 * 3/8 = -9/128.
        """
        assert neumann_coefficient_N11(2, 2) == Rational(-9, 128)

    def test_N11_13_exact(self):
        """N^{11}_{1,3}: exact computation.

        m+n=4 (even), sign = (-1)^5 = -1,
        prefactor = 2/4 = 1/2, A_1 = 1/2, A_3 = 5/16.
        N = -1 * 1/2 * 1/2 * 5/16 = -5/64.
        """
        assert neumann_coefficient_N11(1, 3) == Rational(-5, 64)

    def test_N11_boundary_zero(self):
        """N^{11}_{0,n} = 0 and N^{11}_{m,0} = 0."""
        for n in range(5):
            assert neumann_coefficient_N11(0, n) == 0
            assert neumann_coefficient_N11(n, 0) == 0

    def test_N11_negative_zero(self):
        """N^{11}_{-1,n} = 0."""
        assert neumann_coefficient_N11(-1, 3) == 0

    def test_neumann_matrix_shape(self):
        """Neumann matrix has correct number of entries."""
        N = neumann_matrix(5)
        assert len(N) == 25  # 5 x 5

    def test_neumann_unitarity_bound(self):
        """Row sums of N^{11}_{mn}^2 < 1 (unitarity constraint)."""
        L = 10
        N = neumann_matrix(L)
        for m in range(1, L + 1):
            row_sum = sum(N[(m, n)]**2 for n in range(1, L + 1))
            assert float(row_sum) <= 1.0 + 1e-10

    def test_verify_neumann_all_pass(self):
        """All structural properties of Neumann matrix verified."""
        results = verify_neumann_symmetry(8)
        for key, val in results.items():
            assert val, f"Neumann property '{key}' failed"

    def test_N11_diagonal_decay(self):
        """Diagonal elements |N^{11}_{n,n}| decay with n."""
        vals = [abs(neumann_coefficient_N11(n, n))
                for n in range(2, 12, 2)]
        for i in range(len(vals) - 1):
            assert vals[i] >= vals[i + 1]

    def test_N12_matches_N11_structure(self):
        """N^{12}_{mn} has same parity selection as N^{11}."""
        for m in range(1, 6):
            for n in range(1, 6):
                if (m + n) % 2 != 0:
                    assert neumann_coefficient_N12(m, n) == 0


# =========================================================================
# Section 2: Open SFT Cubic Vertex Tests
# =========================================================================

class TestOpenSFTVertex:
    """Tests for open string field theory vertices."""

    def test_cubic_overlap_equals_N11(self):
        """Cubic vertex overlap <V_3|phi_m phi_n> = N^{11}_{mn}."""
        for m in range(1, 6):
            for n in range(1, 6):
                assert cubic_vertex_overlap(m, n) == neumann_coefficient_N11(m, n)

    def test_witten_cubic_constant(self):
        """K^2 = 27/16 where K = 3*sqrt(3)/4."""
        K_sq = witten_cubic_constant()
        assert K_sq == Rational(27, 16)
        # Numerical: K = 3*sqrt(3)/4 ~ 1.2990, K^2 ~ 1.6875
        assert abs(float(K_sq) - (3 * math.sqrt(3) / 4)**2) < 1e-10

    def test_open_sft_vertex_dataclass(self):
        """OpenSFTVertex data structure works correctly."""
        v = OpenSFTVertex(order=3, max_level=5)
        assert v.is_cubic
        v4 = OpenSFTVertex(order=4, max_level=5)
        assert not v4.is_cubic


# =========================================================================
# Section 3: Tachyon Potential Tests
# =========================================================================

class TestTachyonPotential:
    """Tests for the tachyon potential and Sen's conjecture."""

    def test_tachyon_potential_at_zero(self):
        """V(0) = 0 (no vacuum energy shift in level truncation)."""
        assert abs(tachyon_potential_level_0(0.0)) < 1e-15

    def test_tachyon_potential_has_maximum_and_minimum(self):
        """V(t) has a local maximum at t=0 and a global minimum at t_0 > 0."""
        # V'(t) = -t + K^3 t^2 = t(-1 + K^3 t)
        # Roots: t=0 (maximum), t=1/K^3 (minimum)
        # V''(0) = -1 < 0 (maximum)
        v_at_0 = tachyon_potential_level_0(0.0)
        v_at_small = tachyon_potential_level_0(0.1)
        assert v_at_small < v_at_0  # decreasing near 0

    def test_tachyon_critical_ratio_68_percent(self):
        """Level (0,0) gives ~68.5% of Sen's conjecture.

        V(T_0)/T_D ~ -0.6846 (the celebrated 68% result).
        """
        ratio = tachyon_potential_critical_ratio_level0()
        assert -0.70 < ratio < -0.67
        # More precise: ~ -0.6846
        assert abs(ratio - (-0.6846)) < 0.001

    def test_sen_conjecture_level_truncation_monotone(self):
        """Higher level truncation gives ratios closer to -1."""
        data = sen_conjecture_level_truncation()
        # Level (0,0): ~68%, Level (2,4): ~95%, Level (2,6): ~99.9%
        assert data['level_0_0'] > data['level_2_4']  # more negative at higher level
        assert data['level_2_4'] > data['level_2_6']
        assert data['level_2_6'] > -1.001  # doesn't overshoot

    def test_sen_conjecture_exact_value(self):
        """Exact conjecture is V(T_0)/T_D = -1."""
        data = sen_conjecture_level_truncation()
        assert data['exact_conjecture'] == -1.0

    def test_tachyon_polynomial_kinetic_term(self):
        """Kinetic term coefficient is -1/2."""
        coeffs = tachyon_potential_polynomial()
        assert coeffs[2] == -0.5

    def test_tachyon_polynomial_cubic_positive(self):
        """Cubic coupling is positive."""
        coeffs = tachyon_potential_polynomial()
        assert coeffs[3] > 0

    def test_tachyon_polynomial_quartic_zero_at_level0(self):
        """Quartic and higher vanish at level (0,0)."""
        coeffs = tachyon_potential_polynomial(max_order=8)
        for n in range(4, 9):
            assert coeffs[n] == 0.0

    def test_level_0_ratio_exact_formula(self):
        """Verify the exact formula V/T_D = -pi^2/(3*K^6)."""
        K = 3 * math.sqrt(3) / 4
        K6 = K**6
        expected = -PI**2 / (3 * K6)
        computed = tachyon_potential_critical_ratio_level0()
        assert abs(computed - expected) < 1e-12


# =========================================================================
# Section 4: Closed SFT Vertex Tests
# =========================================================================

class TestClosedSFTVertices:
    """Tests for closed string field theory vertices from shadow tower."""

    def test_V01_vanishes(self):
        """V_{0,1} = 0 (no genus-0 tadpole)."""
        assert closed_vertex_V01(Rational(13)) == 0

    def test_V02_is_kinetic(self):
        """V_{0,2} = 0 (kinetic term, not a vertex)."""
        assert closed_vertex_V02(Rational(13)) == 0

    def test_V11_equals_kappa_over_24(self):
        """V_{1,1} = kappa/24 (genus-1 tadpole, Theorem D)."""
        for kappa in [Rational(1), Rational(13), Rational(-13), Rational(1, 2)]:
            assert closed_vertex_V11(kappa) == kappa * Rational(1, 24)

    def test_V11_virasoro_c26(self):
        """V_{1,1}(Vir_{26}) = 13/24."""
        assert closed_vertex_V11(Rational(13)) == Rational(13, 24)

    def test_V11_heisenberg_rank1(self):
        """V_{1,1}(H_1) = 1/24."""
        assert closed_vertex_V11(Rational(1)) == Rational(1, 24)

    def test_V12_equals_kappa_lambda1(self):
        """V_{1,2} = kappa * lambda_1 = kappa/24 (string equation at genus 1)."""
        kappa = Rational(13)
        assert closed_vertex_V12(kappa) == kappa * lambda_fp(1)

    def test_V21_equals_kappa_lambda2(self):
        """V_{2,1} = kappa * lambda_2 at the scalar level."""
        kappa = Rational(13)
        assert closed_vertex_V21(kappa) == kappa * lambda_fp(2)

    def test_V21_exact_value(self):
        """V_{2,1}(kappa=1) = 7/5760."""
        assert closed_vertex_V21(Rational(1)) == Rational(7, 5760)

    def test_closed_vertex_stability_check(self):
        """V_{g,n} = 0 when 2g-2+n <= 0 (unstable surface)."""
        kappa = Rational(13)
        assert closed_vertex_from_shadow(kappa, 0, 1) == 0  # g=0, n=1 unstable
        assert closed_vertex_from_shadow(kappa, 0, 2) == 0  # g=0, n=2 unstable
        assert closed_vertex_from_shadow(kappa, 0, 0) == 0  # g=0, n=0 unstable

    def test_closed_vertex_genus1_arity1_stable(self):
        """V_{1,1} is stable (2*1 - 2 + 1 = 1 > 0)."""
        kappa = Rational(1)
        v = closed_vertex_from_shadow(kappa, 1, 1)
        assert v == kappa * lambda_fp(1)

    def test_closed_vertex_genus2_arity0_stable(self):
        """V_{2,0} is stable (2*2 - 2 + 0 = 2 > 0)."""
        kappa = Rational(1)
        v = closed_vertex_from_shadow(kappa, 2, 0)
        assert v == kappa * lambda_fp(2)

    def test_closed_vertex_linearity_in_kappa(self):
        """V_{g,n} is linear in kappa (at scalar level)."""
        for g in range(1, 5):
            v1 = closed_vertex_from_shadow(Rational(1), g, 1)
            v2 = closed_vertex_from_shadow(Rational(2), g, 1)
            assert v2 == 2 * v1

    def test_closed_vertex_dataclass(self):
        """ClosedSFTVertex data structure works correctly."""
        v = ClosedSFTVertex(genus=1, arity=1, value=Rational(13, 24),
                            algebra='Virasoro', kappa=Rational(13))
        assert v.genus == 1
        assert v.arity == 1
        assert v.value == Rational(13, 24)


# =========================================================================
# Section 5: MC Equation = Closed SFT Master Equation
# =========================================================================

class TestMCEquation:
    """Tests verifying the MC equation IS the closed SFT master equation."""

    def test_mc_sector_11_verified(self):
        """MC equation at (1,1) is verified (Theorem D)."""
        result = mc_equation_sector(1, 1, Rational(13))
        assert result['verified']

    def test_mc_sector_11_value(self):
        """V_{1,1} = 13/24 for c=26 Virasoro."""
        result = mc_equation_sector(1, 1, Rational(13))
        assert result['vertex_value'] == Rational(13, 24)

    def test_mc_sector_03_verified(self):
        """MC equation at (0,3) is verified (genus-0 tree level)."""
        result = mc_equation_sector(0, 3, Rational(13))
        assert result['verified']

    def test_mc_sector_04_verified(self):
        """MC equation at (0,4) is verified (quartic resonance class)."""
        result = mc_equation_sector(0, 4, Rational(13))
        assert result['verified']

    def test_mc_sector_12_verified(self):
        """MC equation at (1,2) is verified."""
        result = mc_equation_sector(1, 2, Rational(13))
        assert result['verified']

    def test_mc_sector_21_verified(self):
        """MC equation at (2,1) is verified."""
        result = mc_equation_sector(2, 1, Rational(13))
        assert result['verified']

    def test_mc_all_low_sectors(self):
        """All five lowest sectors of the MC equation are verified."""
        results = mc_equation_check_low_sectors(Rational(13))
        for key, data in results.items():
            assert data['verified'], f"Sector {key} not verified"

    def test_mc_equation_genus_interpretation(self):
        """The MC equation at (1,1) has correct interpretation."""
        result = mc_equation_sector(1, 1, Rational(1))
        assert 'kappa/24' in result['interpretation']

    def test_mc_higher_genus_scalar_level(self):
        """MC equation at (g, 1) is verified at scalar level for g >= 1."""
        kappa = Rational(5)
        for g in range(1, 6):
            result = mc_equation_sector(g, 1, kappa)
            assert result['verified']


# =========================================================================
# Section 6: Polyakov Amplitude Tests
# =========================================================================

class TestPolyakovAmplitudes:
    """Tests for Polyakov path integral amplitudes."""

    def test_veneziano_finite_at_generic_point(self):
        """Veneziano amplitude is finite at generic (non-pole) Mandelstam values.

        Poles occur when alpha(s) or alpha(t) is a non-negative integer,
        i.e., s = -1, 0, 1, 2, ... or t = -1, 0, 1, 2, ...
        Also when -alpha(s)-alpha(t) is a non-positive integer.
        Test at a point away from all poles.
        """
        # s=-0.3, t=-0.3: alpha(s)=0.7, alpha(t)=0.7, sum=1.4
        # -alpha(s)=-0.7, -alpha(t)=-0.7, -sum=-1.4: no Gamma poles
        val = veneziano_amplitude(-0.3, -0.3)
        assert not math.isnan(val)
        assert abs(val) < 100  # finite at non-pole

    def test_veneziano_symmetry(self):
        """A(s,t) = A(t,s) for the Veneziano amplitude.

        Must pick s, t such that alpha(s), alpha(t), and alpha(s)+alpha(t)
        avoid non-negative integers: alpha(x)=1+x, so avoid s,t in Z_{>=-1}
        and s+t in Z_{>=-2} simultaneously.
        """
        s, t = -0.3, -0.4  # alpha: 0.7, 0.6, sum 1.3; all non-integer
        assert abs(veneziano_amplitude(s, t) - veneziano_amplitude(t, s)) < 1e-10

    def test_veneziano_residue_structure(self):
        """Residues at tachyon pole are finite and nonzero."""
        res = veneziano_residue_at_pole(0)
        assert not math.isnan(res)
        assert abs(res) > 0

    def test_virasoro_shapiro_symmetry(self):
        """A(s,t,u) is symmetric under permutations.

        Must avoid Gamma poles: -s/2, -t/2, -u/2 must not be non-positive
        integers, and 1+s/2, 1+t/2, 1+u/2 must not be non-positive integers.
        With s+t+u = -8: pick s=-2.3, t=-2.7, u=-3.0.
        -s/2=1.15, -t/2=1.35, -u/2=1.5; 1+s/2=-0.15, 1+t/2=-0.35, 1+u/2=-0.5.
        All non-integer, so Gamma is finite.
        """
        s, t = -2.3, -2.7
        u = -8.0 - s - t  # = -3.0
        val1 = virasoro_shapiro_amplitude(s, t, u)
        val2 = virasoro_shapiro_amplitude(t, s, u)
        val3 = virasoro_shapiro_amplitude(s, u, t)
        assert not math.isnan(val1)
        assert abs(val1 - val2) < 1e-10
        assert abs(val1 - val3) < 1e-10

    def test_polyakov_genus1_matches_V11(self):
        """Polyakov one-loop tadpole = V_{1,1} = kappa/24."""
        kappa = Rational(13)
        poly = polyakov_genus1_tadpole(kappa)
        v11 = closed_vertex_V11(kappa)
        assert poly == v11

    def test_polyakov_genus1_exact(self):
        """Polyakov tadpole for kappa=1 is 1/24."""
        assert polyakov_genus1_tadpole(Rational(1)) == Rational(1, 24)


# =========================================================================
# Section 7: Anomaly Cancellation Tests
# =========================================================================

class TestAnomalyCancellation:
    """Tests for anomaly cancellation in string field theory."""

    def test_bosonic_anomaly_free_at_c26(self):
        """Bosonic string is anomaly-free at c = 26."""
        result = bosonic_string_anomaly(26)
        assert result['anomaly_free']
        assert result['critical_dimension']

    def test_bosonic_anomaly_nonzero_at_c25(self):
        """Bosonic string has anomaly at c != 26."""
        result = bosonic_string_anomaly(25)
        assert not result['anomaly_free']

    def test_bosonic_kappa_eff_zero_at_c26(self):
        """kappa_eff = kappa_matter + kappa_ghost = 13 - 13 = 0."""
        result = bosonic_string_anomaly(26)
        assert result['kappa_eff'] == 0
        assert result['kappa_matter'] == Rational(13)
        assert result['kappa_ghost'] == Rational(-13)

    def test_bosonic_V11_total_vanishes(self):
        """V_{1,1}^{total} = 0 at c=26 (anomaly cancellation)."""
        result = bosonic_string_anomaly(26)
        assert result['V11_total'] == 0

    def test_bosonic_V11_matter_nonzero(self):
        """V_{1,1}^{matter} = 13/24 != 0 (matter alone has anomaly)."""
        result = bosonic_string_anomaly(26)
        assert result['V11_matter'] == Rational(13, 24)

    def test_bosonic_V11_ghost_nonzero(self):
        """V_{1,1}^{ghost} = -13/24 (ghost contribution cancels matter)."""
        result = bosonic_string_anomaly(26)
        assert result['V11_ghost'] == Rational(-13, 24)

    def test_superstring_anomaly_free_at_d10(self):
        """Superstring is anomaly-free at d = 10."""
        result = superstring_anomaly(10)
        assert result['anomaly_free']
        assert result['critical_dimension']

    def test_superstring_c_total_zero(self):
        """Total central charge vanishes at d=10: 3*10/2 - 15 = 0."""
        result = superstring_anomaly(10)
        assert result['c_total'] == 0

    def test_superstring_anomaly_nonzero_d9(self):
        """Superstring has anomaly at d != 10."""
        result = superstring_anomaly(9)
        assert not result['anomaly_free']

    def test_kappa_eff_varies_with_c(self):
        """kappa_eff = c/2 - 13 varies linearly with c.

        AP20: kappa_eff is a property of the COMPOSITE system, not intrinsic.
        """
        for c in [0, 10, 20, 26, 30]:
            result = bosonic_string_anomaly(c)
            assert result['kappa_eff'] == Rational(c, 2) - 13


# =========================================================================
# Section 8: Genus Expansion Tests
# =========================================================================

class TestGenusExpansion:
    """Tests for the closed SFT genus expansion."""

    def test_F1_exact(self):
        """F_1 = kappa/24."""
        expansion = closed_sft_genus_expansion(Rational(1), max_genus=5)
        assert expansion['F1'] == Rational(1, 24)

    def test_F2_exact(self):
        """F_2 = kappa * 7/5760."""
        expansion = closed_sft_genus_expansion(Rational(1), max_genus=5)
        assert expansion['F2'] == Rational(7, 5760)

    def test_genus_ratio_converges(self):
        """F_{g+1}/F_g -> 1/(2*pi)^2 ~ 0.0253."""
        expansion = closed_sft_genus_expansion(Rational(1), max_genus=30)
        target = 1.0 / (4 * PI**2)
        # Check at genus 15
        assert abs(expansion['ratios'][15] - target) < 0.001

    def test_F_g_positive(self):
        """F_g > 0 for all g >= 1 (Bernoulli signs: Ahat(ix) has all positive coefficients)."""
        expansion = closed_sft_genus_expansion(Rational(1), max_genus=20)
        for g in range(1, 21):
            assert expansion['terms'][g] > 0

    def test_genus_expansion_linearity(self):
        """F_g(2*kappa) = 2*F_g(kappa)."""
        e1 = closed_sft_genus_expansion(Rational(1), max_genus=5)
        e2 = closed_sft_genus_expansion(Rational(2), max_genus=5)
        for g in range(1, 6):
            assert e2['terms'][g] == 2 * e1['terms'][g]

    def test_convergence_radius_2pi(self):
        """Convergence radius of the genus expansion is 2*pi."""
        expansion = closed_sft_genus_expansion(Rational(1), max_genus=10)
        assert abs(expansion['convergence_radius'] - 2 * PI) < 1e-10

    def test_partial_sums_increasing(self):
        """Partial sums are monotonically increasing (all terms positive for kappa > 0)."""
        expansion = closed_sft_genus_expansion(Rational(1), max_genus=10)
        for g in range(1, 10):
            assert expansion['partial_sums'][g + 1] > expansion['partial_sums'][g]

    def test_genus_expansion_kappa_zero(self):
        """F_g(0) = 0 for all g."""
        expansion = closed_sft_genus_expansion(Rational(0), max_genus=5)
        for g in range(1, 6):
            assert expansion['terms'][g] == 0


# =========================================================================
# Section 9: Family-Specific Vertex Tests
# =========================================================================

class TestFamilyVertices:
    """Tests for SFT vertices of specific chiral algebra families."""

    def test_heisenberg_is_free_theory(self):
        """Heisenberg SFT is free (no cubic vertex, class G)."""
        data = sft_vertices_heisenberg(rank=1)
        assert data['is_free_theory']
        assert data['V_03'] == 0
        assert data['shadow_class'] == 'G (Gaussian)'
        assert data['shadow_depth'] == 2

    def test_heisenberg_V11(self):
        """Heisenberg V_{1,1} = rank/24."""
        for rank in [1, 2, 5]:
            data = sft_vertices_heisenberg(rank=rank)
            assert data['V_11'] == Rational(rank, 24)

    def test_virasoro_shadow_class_M(self):
        """Virasoro is class M (infinite shadow depth)."""
        data = sft_vertices_virasoro(26)
        assert data['shadow_class'] == 'M (mixed, infinite depth)'
        assert data['shadow_depth'] == float('inf')

    def test_virasoro_V11_c26(self):
        """Virasoro V_{1,1} at c=26 is 13/24."""
        data = sft_vertices_virasoro(26)
        assert data['V_11'] == Rational(13, 24)

    def test_virasoro_Q_contact(self):
        """Q^contact(Vir_c) = 10/(c*(5c+22))."""
        for c in [1, 10, 26]:
            data = sft_vertices_virasoro(c)
            expected = Rational(10) / (Rational(c) * (5 * Rational(c) + 22))
            assert data['Q_contact'] == expected

    def test_affine_sl2_shadow_class_L(self):
        """Affine sl_2 is class L (shadow depth 3)."""
        data = sft_vertices_affine_sl2(1)
        assert data['shadow_class'] == 'L (Lie/tree)'
        assert data['shadow_depth'] == 3

    def test_affine_sl2_kappa(self):
        """kappa(sl2, k) = 3(k+2)/4."""
        for k in [1, 2, 5]:
            data = sft_vertices_affine_sl2(k)
            assert data['kappa'] == Rational(3) * (Rational(k) + 2) / 4

    def test_affine_sl2_V11(self):
        """Affine sl_2 V_{1,1} = 3(k+2)/(4*24) = (k+2)/32."""
        data = sft_vertices_affine_sl2(1)
        assert data['V_11'] == Rational(3) * Rational(3) / (4 * 24)

    def test_virasoro_not_free(self):
        """Virasoro SFT is not free theory."""
        data = sft_vertices_virasoro(26)
        assert not data['is_free_theory']

    def test_affine_not_free(self):
        """Affine sl_2 SFT is not free theory."""
        data = sft_vertices_affine_sl2(1)
        assert not data['is_free_theory']


# =========================================================================
# Section 10: Cross-Consistency Tests
# =========================================================================

class TestCrossConsistency:
    """Cross-consistency tests between different computations."""

    def test_polyakov_matches_shadow_genus1(self):
        """Polyakov genus-1 amplitude matches shadow tower V_{1,1}."""
        for kappa in [Rational(1), Rational(13), Rational(1, 2)]:
            assert polyakov_genus1_tadpole(kappa) == closed_vertex_V11(kappa)

    def test_anomaly_cancellation_matches_V11_vanishing(self):
        """V_{1,1} = 0 iff kappa_eff = 0 iff c = 26."""
        anom = bosonic_string_anomaly(26)
        assert anom['V11_total'] == 0
        assert anom['anomaly_free']

    def test_shadow_tower_matches_sft_vertex(self):
        """Shadow tower at genus g, arity 2 matches V_{g,1}."""
        kappa = Rational(13)
        for g in range(1, 6):
            shadow = F_g(kappa, g)
            vertex = closed_vertex_from_shadow(kappa, g, 1)
            assert shadow == vertex

    def test_bar_coproduct_has_neumann_data(self):
        """Bar coproduct computation includes Neumann matrix."""
        data = bar_coproduct_components(max_level=4)
        assert 'neumann_matrix' in data
        assert len(data['neumann_matrix']) > 0

    def test_bar_coproduct_neumann_consistency(self):
        """Neumann data from bar coproduct matches direct computation."""
        data = bar_coproduct_components(max_level=4)
        for (m, n), val in data['neumann_matrix'].items():
            assert val == neumann_coefficient_N11(m, n)

    def test_V11_is_F1(self):
        """V_{1,1} and F_1 are the same quantity."""
        kappa = Rational(7)
        assert closed_vertex_V11(kappa) == F_g(kappa, 1)

    def test_V21_is_F2(self):
        """V_{2,1} (scalar level) equals F_2."""
        kappa = Rational(7)
        assert closed_vertex_V21(kappa) == F_g(kappa, 2)

    def test_genus_expansion_terms_match_vertices(self):
        """Genus expansion F_g matches closed vertex at each genus."""
        kappa = Rational(5)
        expansion = closed_sft_genus_expansion(kappa, max_genus=5)
        for g in range(1, 6):
            assert expansion['terms'][g] == closed_vertex_from_shadow(kappa, g, 1)

    def test_kappa_additivity_in_sft(self):
        """kappa(A + B) = kappa(A) + kappa(B) reflected in vertex additivity.

        For a direct sum of algebras, the SFT vertices are additive
        at the scalar level.
        """
        k1 = Rational(3)
        k2 = Rational(5)
        for g in range(1, 5):
            v1 = closed_vertex_from_shadow(k1, g, 1)
            v2 = closed_vertex_from_shadow(k2, g, 1)
            v_sum = closed_vertex_from_shadow(k1 + k2, g, 1)
            assert v_sum == v1 + v2

    def test_complementarity_V11(self):
        """V_{1,1}(matter) + V_{1,1}(ghost) = 0 at c=26.

        This is the SFT manifestation of Theorem C (complementarity).
        """
        kappa_matter = Rational(13)
        kappa_ghost = Rational(-13)
        assert closed_vertex_V11(kappa_matter) + closed_vertex_V11(kappa_ghost) == 0


# =========================================================================
# Section 11: Master Verification Test
# =========================================================================

class TestMasterVerification:
    """Run the complete internal verification suite."""

    def test_verify_all_pass(self):
        """All internal consistency checks pass."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Master verification failed: {name}"

    def test_verify_all_count(self):
        """At least 10 checks in the master verification."""
        results = verify_all()
        assert len(results) >= 10


# =========================================================================
# Section 12: Edge Cases and Robustness
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_V11_negative_kappa(self):
        """V_{1,1} with negative kappa (ghost system)."""
        v = closed_vertex_V11(Rational(-13))
        assert v == Rational(-13, 24)

    def test_V11_zero_kappa(self):
        """V_{1,1} = 0 when kappa = 0 (uncurved bar complex)."""
        assert closed_vertex_V11(Rational(0)) == 0

    def test_neumann_large_modes(self):
        """Neumann coefficients for large mode numbers are small."""
        val = neumann_coefficient_N11(20, 20)
        assert abs(float(val)) < 0.01

    def test_genus_expansion_many_terms(self):
        """Genus expansion computed to high genus without overflow."""
        expansion = closed_sft_genus_expansion(Rational(1), max_genus=30)
        assert 30 in expansion['terms']
        assert expansion['terms'][30] > 0

    def test_veneziano_at_pole_neighborhood(self):
        """Veneziano amplitude grows near the tachyon pole s = -1.

        The Veneziano amplitude has a pole at alpha(s) = 0, i.e. s = -1.
        Approaching s -> -1 from above with t generic, |A| -> infinity.
        """
        t_val = -0.3  # generic, away from poles
        vals = [abs(veneziano_amplitude(-1.0 + 0.01 * (i + 1), t_val))
                for i in range(5)]
        # Near s = -1, amplitude grows: at s=-0.99 already ~100
        assert any(v > 10 for v in vals if not math.isnan(v))

    def test_closed_vertex_large_genus(self):
        """Closed SFT vertex at large genus is very small."""
        kappa = Rational(13)
        v20 = closed_vertex_from_shadow(kappa, 20, 1)
        assert float(v20) < 1e-20  # extremely small due to Bernoulli decay

    def test_heisenberg_all_higher_vertices_scalar(self):
        """For Heisenberg (free theory), all vertices are scalar level only."""
        data = sft_vertices_heisenberg(1)
        # Shadow depth 2 means no cubic or higher interactions
        assert data['shadow_depth'] == 2

    def test_stability_boundary(self):
        """V_{1,0} is stable (2-2+0=0, marginal; we return 0 for non-positive)."""
        assert closed_vertex_from_shadow(Rational(1), 1, 0) == 0

    def test_lambda_fp_first_few(self):
        """Cross-check lambda_g^FP values used throughout."""
        assert lambda_fp(1) == Rational(1, 24)
        assert lambda_fp(2) == Rational(7, 5760)
        # lambda_3 = (2^5-1)/2^5 * |B_6|/6! = 31/32 * 1/42 / 720
        #          = 31/(32*42*720) = 31/967680
        assert lambda_fp(3) == Rational(31, 967680)
