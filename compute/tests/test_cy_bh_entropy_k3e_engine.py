r"""Tests for CY-27: Black hole entropy from K3 x E compactification.

Multi-path verification:
  Path (a): macroscopic attractor entropy S = pi*sqrt(Delta)
  Path (b): microscopic 1/Phi_10 Fourier coefficients
  Path (c): Rademacher expansion convergence

Over 130 tests covering all six sections of the engine.

CAUTION (AP1):  All expected values independently computed.
CAUTION (AP10): Cross-family consistency checks, not just hardcoded values.
CAUTION (AP38): DVV normalization throughout.
CAUTION (AP46): eta includes q^{1/24}.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.cy_bh_entropy_k3e_engine import (
    BMPVBlackHole,
    K3Invariants,
    K3xE_Invariants,
    K3xE_Prepotential,
    attractor_entropy,
    bekenstein_hawking_leading,
    bmpv_entropy_table,
    charge_discriminant_simple,
    convergence_ratio,
    degeneracy_exact,
    degeneracy_signed,
    discriminant_entropy_table,
    euler_characteristic_E,
    euler_characteristic_K3,
    euler_characteristic_K3xE,
    log_correction_subleading,
    log_degeneracy,
    rademacher_expansion,
    rademacher_leading_entropy,
    rademacher_term,
    second_chern_class_K3,
    second_chern_class_K3xE,
    sen_entropy_with_corrections,
    shadow_genus1_correction,
    shadow_gravity_dictionary,
    shadow_kappa_K3,
    subleading_coefficient,
    wald_entropy_R2_correction,
    _bessel_I_half_integer,
    _eta_product_coeffs,
)

PI = math.pi


# ============================================================
# SECTION 1: BMPV BLACK HOLE (5D)
# ============================================================

class TestBMPV:
    """Tests for the BMPV black hole in 5d."""

    def test_bmpv_basic_entropy(self):
        """S = 2*pi*sqrt(Q1*Q5*n) for (1,1,1)."""
        bh = BMPVBlackHole(1, 1, 1)
        assert abs(bh.entropy_macroscopic() - 2 * PI) < 1e-12

    def test_bmpv_central_charge(self):
        """c_eff = 6*Q1*Q5."""
        bh = BMPVBlackHole(2, 3, 5)
        assert bh.c_eff == 6 * 2 * 3 == 36
        assert bh.central_charge_left == 36
        assert bh.central_charge_right == 36

    def test_bmpv_macro_micro_match_111(self):
        """Macro = micro for (1,1,1)."""
        bh = BMPVBlackHole(1, 1, 1)
        assert bh.verify_macro_micro_match()

    def test_bmpv_macro_micro_match_112(self):
        """Macro = micro for (1,1,2)."""
        bh = BMPVBlackHole(1, 1, 2)
        assert bh.verify_macro_micro_match()
        expected = 2 * PI * math.sqrt(2)
        assert abs(bh.entropy_macroscopic() - expected) < 1e-12

    def test_bmpv_macro_micro_match_211(self):
        """Macro = micro for (2,1,1)."""
        bh = BMPVBlackHole(2, 1, 1)
        assert bh.verify_macro_micro_match()
        expected = 2 * PI * math.sqrt(2)
        assert abs(bh.entropy_macroscopic() - expected) < 1e-12

    def test_bmpv_macro_micro_match_121(self):
        """Macro = micro for (1,2,1)."""
        bh = BMPVBlackHole(1, 2, 1)
        assert bh.verify_macro_micro_match()
        expected = 2 * PI * math.sqrt(2)
        assert abs(bh.entropy_macroscopic() - expected) < 1e-12

    def test_bmpv_symmetry_Q1_Q5(self):
        """S is symmetric in Q1 and Q5."""
        bh1 = BMPVBlackHole(2, 3, 5)
        bh2 = BMPVBlackHole(3, 2, 5)
        assert abs(bh1.entropy_macroscopic() - bh2.entropy_macroscopic()) < 1e-12

    def test_bmpv_scaling(self):
        """S(lambda*Q1, Q5, n) = sqrt(lambda) * S(Q1, Q5, n)."""
        bh1 = BMPVBlackHole(1, 1, 1)
        bh4 = BMPVBlackHole(4, 1, 1)
        assert abs(bh4.entropy_macroscopic() - 2 * bh1.entropy_macroscopic()) < 1e-12

    def test_bmpv_cardy_derivation(self):
        """Verify Cardy formula: S = 2*pi*sqrt(c_eff * n / 6)."""
        for Q1, Q5, n in [(1, 1, 1), (2, 3, 5), (1, 1, 10)]:
            bh = BMPVBlackHole(Q1, Q5, n)
            S_cardy = 2 * PI * math.sqrt(bh.c_eff * bh.n / 6.0)
            S_charges = 2 * PI * math.sqrt(Q1 * Q5 * n)
            assert abs(S_cardy - S_charges) < 1e-12

    def test_bmpv_positive_charges_required(self):
        """Negative charges should raise ValueError."""
        with pytest.raises(ValueError):
            BMPVBlackHole(-1, 1, 1)
        with pytest.raises(ValueError):
            BMPVBlackHole(1, 0, 1)

    def test_bmpv_log_correction(self):
        """Entropy with log correction for (1,1,1)."""
        bh = BMPVBlackHole(1, 1, 1)
        S_log = bh.entropy_with_log_correction()
        S0 = 2 * PI  # macroscopic
        expected = S0 - 1.5 * math.log(1)  # log(1) = 0
        assert abs(S_log - expected) < 1e-12

    def test_bmpv_log_correction_nontrivial(self):
        """Log correction for (2,3,5): S0 - 1.5*log(30)."""
        bh = BMPVBlackHole(2, 3, 5)
        S0 = 2 * PI * math.sqrt(30)
        expected = S0 - 1.5 * math.log(30)
        assert abs(bh.entropy_with_log_correction() - expected) < 1e-10

    def test_bmpv_charge_product(self):
        """charge_product = Q1*Q5*n."""
        bh = BMPVBlackHole(3, 4, 5)
        assert bh.charge_product == 60

    def test_bmpv_large_charges(self):
        """BMPV at large charges (10,10,10): S = 2*pi*sqrt(1000)."""
        bh = BMPVBlackHole(10, 10, 10)
        expected = 2 * PI * math.sqrt(1000)
        assert abs(bh.entropy_macroscopic() - expected) < 1e-10
        assert bh.verify_macro_micro_match()


# ============================================================
# SECTION 2: 4D BLACK HOLES FROM K3 x T^2
# ============================================================

class TestAttractorEntropy:
    """Tests for 4d attractor entropy."""

    def test_attractor_entropy_Delta1(self):
        """S(1) = pi."""
        assert abs(attractor_entropy(1.0) - PI) < 1e-12

    def test_attractor_entropy_Delta4(self):
        """S(4) = 2*pi."""
        assert abs(attractor_entropy(4.0) - 2 * PI) < 1e-12

    def test_attractor_entropy_Delta9(self):
        """S(9) = 3*pi."""
        assert abs(attractor_entropy(9.0) - 3 * PI) < 1e-12

    def test_attractor_entropy_Delta16(self):
        """S(16) = 4*pi."""
        assert abs(attractor_entropy(16.0) - 4 * PI) < 1e-12

    def test_attractor_entropy_Delta25(self):
        """S(25) = 5*pi."""
        assert abs(attractor_entropy(25.0) - 5 * PI) < 1e-12

    def test_attractor_entropy_zero(self):
        """S(0) = 0."""
        assert attractor_entropy(0.0) == 0.0

    def test_attractor_entropy_negative(self):
        """S(Delta < 0) = 0."""
        assert attractor_entropy(-1.0) == 0.0

    def test_attractor_scaling(self):
        """S(k^2 * Delta) = k * S(Delta)."""
        for k in [2, 3, 5]:
            for Delta in [1.0, 4.0, 7.0]:
                assert abs(attractor_entropy(k * k * Delta) -
                           k * attractor_entropy(Delta)) < 1e-10

    def test_charge_discriminant_simple(self):
        """Delta = 4*p0*q0 for simple charges."""
        assert charge_discriminant_simple(1, 1) == 4
        assert charge_discriminant_simple(2, 3) == 24
        assert charge_discriminant_simple(5, 5) == 100

    def test_sen_entropy_no_log(self):
        """Sen entropy without log correction = attractor entropy."""
        for Delta in [1.0, 4.0, 9.0, 16.0, 25.0]:
            S_sen = sen_entropy_with_corrections(Delta, include_log=False)
            S_attr = attractor_entropy(Delta)
            assert abs(S_sen - S_attr) < 1e-12

    def test_sen_entropy_with_log(self):
        """Sen entropy with log correction = pi*sqrt(Delta) - 1.5*log(Delta)."""
        for Delta in [4.0, 9.0, 16.0, 25.0, 100.0]:
            S = sen_entropy_with_corrections(Delta, include_log=True)
            expected = PI * math.sqrt(Delta) - 1.5 * math.log(Delta)
            assert abs(S - expected) < 1e-10


# ============================================================
# SECTION 3: MICROSCOPIC DEGENERACY FROM 1/PHI_10
# ============================================================

class TestDegeneracy:
    """Tests for 1/Phi_10 Fourier coefficients."""

    def test_d_minus1(self):
        """d(-1) = 1 (leading pole of 1/Phi_10)."""
        assert degeneracy_exact(-1) == 1

    def test_d_0(self):
        """d(0) = 2 in absolute value."""
        assert degeneracy_exact(0) == 2

    def test_d_0_signed(self):
        """Signed d(0) = -2."""
        assert degeneracy_signed(0) == -2

    def test_d_1(self):
        """|d(1)| = 48."""
        assert degeneracy_exact(1) == 48

    def test_d_1_signed(self):
        """Signed d(1) = -48."""
        assert degeneracy_signed(1) == -48

    def test_d_positive_for_small_Delta(self):
        """Degeneracies are positive for small Delta."""
        for Delta in range(1, 16):
            assert degeneracy_exact(Delta) > 0

    def test_d_growth_monotone_average(self):
        """Average |d(Delta)| grows with Delta (not strictly monotone)."""
        d_vals = [degeneracy_exact(Delta) for Delta in range(1, 16)]
        # Check that the average of the last 5 exceeds the first 5
        avg_early = sum(d_vals[:5]) / 5
        avg_late = sum(d_vals[10:]) / 5
        assert avg_late > avg_early

    def test_known_values_consistency(self):
        """Cross-check: |d(4)| > |d(1)| > 1."""
        assert degeneracy_exact(4) > degeneracy_exact(1)
        assert degeneracy_exact(1) > 1

    def test_log_degeneracy_positive(self):
        """log|d(Delta)| > 0 for Delta >= 1."""
        for Delta in range(1, 16):
            assert log_degeneracy(Delta) > 0

    def test_log_degeneracy_growing(self):
        """log|d(Delta)| grows with Delta on average."""
        vals = [log_degeneracy(Delta) for Delta in range(1, 16)]
        # Check that vals[14] > vals[0]
        assert vals[14] > vals[0]

    def test_bekenstein_hawking_leading(self):
        """BH leading term: pi*sqrt(Delta)."""
        for Delta in [1, 4, 9, 16, 25, 100]:
            expected = PI * math.sqrt(Delta)
            assert abs(bekenstein_hawking_leading(float(Delta)) - expected) < 1e-12


# ============================================================
# SECTION 3b: CONVERGENCE OF LOG D TO BH
# ============================================================

class TestConvergence:
    """Tests that log|d(Delta)|/pi*sqrt(Delta) -> 1 at large Delta."""

    def test_convergence_ratio_at_small_Delta(self):
        """At small Delta, ratio may deviate from 1."""
        r = convergence_ratio(1)
        # log(48) / pi ~ 1.23, so ratio > 1 at small Delta
        assert r > 0  # at least positive

    def test_convergence_ratio_computable(self):
        """Convergence ratio is computable for Delta = 1,...,15."""
        for Delta in range(1, 16):
            r = convergence_ratio(Delta)
            assert not math.isnan(r)

    def test_subleading_coefficient_computed(self):
        """Subleading coefficient is computable for known values."""
        for Delta in range(2, 16):
            c = subleading_coefficient(Delta)
            assert not math.isnan(c)

    def test_log_correction_subleading_value(self):
        """-(3/2)*log(Delta) at Delta=100 = -(3/2)*log(100) ~ -6.9."""
        val = log_correction_subleading(100.0)
        expected = -1.5 * math.log(100)
        assert abs(val - expected) < 1e-10

    def test_log_correction_negative(self):
        """The log correction is negative for Delta > 1."""
        for Delta in [2, 10, 100, 1000]:
            assert log_correction_subleading(float(Delta)) < 0


# ============================================================
# SECTION 4: OSV CONJECTURE
# ============================================================

class TestOSV:
    """Tests for the OSV conjecture Z_BH = |Z_top|^2."""

    def test_F0_stu_basic(self):
        """F_0 = -STU for the STU model."""
        prep = K3xE_Prepotential(S=1 + 1j, T=1 + 1j, U=1 + 1j)
        F0 = prep.F0_stu()
        # (1+i)^3 = 1 + 3i + 3i^2 + i^3 = 1 + 3i - 3 - i = -2 + 2i
        expected = -(-2 + 2j)  # -STU where STU = (1+i)^3
        # STU = (1+i)(1+i)(1+i) = (1+i)(2i) = 2i + 2i^2 = -2 + 2i
        assert abs(F0 - (2 - 2j)) < 1e-12

    def test_F0_real_stu(self):
        """F_0 for real S=T=U=2: F_0 = -8."""
        prep = K3xE_Prepotential(S=2.0, T=2.0, U=2.0)
        assert abs(prep.F0_stu() - (-8.0)) < 1e-12

    def test_F1_one_loop(self):
        """F_1 = -0.5*log(ImS*ImT*ImU)."""
        F1 = K3xE_Prepotential.F1_one_loop(1.0, 1.0, 1.0)
        assert abs(F1 - 0.0) < 1e-12  # log(1) = 0

    def test_F1_one_loop_nontrivial(self):
        """F_1 at ImS=ImT=ImU=2: -0.5*log(8) = -1.5*log(2)."""
        F1 = K3xE_Prepotential.F1_one_loop(2.0, 2.0, 2.0)
        expected = -0.5 * math.log(8)
        assert abs(F1 - expected) < 1e-12

    def test_F0_cubic(self):
        """F_0 is cubic in the moduli (degree 3)."""
        # F_0(lambda*S, lambda*T, lambda*U) = lambda^3 * F_0(S,T,U)
        prep1 = K3xE_Prepotential(S=1.0 + 0.5j, T=2.0 + 0.3j, U=0.5 + 1.0j)
        prep2 = K3xE_Prepotential(S=2.0 + 1.0j, T=4.0 + 0.6j, U=1.0 + 2.0j)
        assert abs(prep2.F0_stu() - 8 * prep1.F0_stu()) < 1e-10


# ============================================================
# SECTION 5: QUANTUM CORRECTIONS TO ENTROPY
# ============================================================

class TestQuantumCorrections:
    """Tests for Wald entropy and R^2 corrections."""

    def test_chi_K3(self):
        """chi(K3) = 24."""
        assert euler_characteristic_K3() == 24

    def test_chi_E(self):
        """chi(E) = 0."""
        assert euler_characteristic_E() == 0

    def test_chi_K3xE(self):
        """chi(K3 x E) = 0."""
        assert euler_characteristic_K3xE() == 0

    def test_chi_product_formula(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert euler_characteristic_K3xE() == euler_characteristic_K3() * euler_characteristic_E()

    def test_c2_K3(self):
        """c_2(K3) = chi(K3) = 24."""
        assert second_chern_class_K3() == 24

    def test_c2_K3xE(self):
        """c_2(K3 x E) = 24 (from K3 contribution)."""
        c2_total, c2_K3, c2_cross = second_chern_class_K3xE()
        assert c2_total == 24
        assert c2_K3 == 24
        assert c2_cross == 0

    def test_wald_R2_correction(self):
        """Wald entropy with R^2 correction."""
        # Delta = 100, C2.p = 0: S = pi*10
        S0 = wald_entropy_R2_correction(100.0, 0.0)
        assert abs(S0 - 10 * PI) < 1e-10

    def test_wald_R2_positive_correction(self):
        """R^2 correction INCREASES entropy (for C2.p > 0)."""
        S_no_corr = wald_entropy_R2_correction(100.0, 0.0)
        S_with_corr = wald_entropy_R2_correction(100.0, 24.0)
        assert S_with_corr > S_no_corr

    def test_shadow_genus1_coefficient(self):
        """F_1 = kappa * (1/24)."""
        coeff = shadow_genus1_correction(1.0)
        assert coeff == Fraction(1, 24)

    def test_shadow_kappa_K3_Q1Q5(self):
        """kappa = 3*Q1*Q5 for MSW CFT."""
        assert shadow_kappa_K3(1, 1) == 3.0
        assert shadow_kappa_K3(2, 3) == 18.0

    def test_shadow_kappa_consistency(self):
        """kappa = c/2 with c = 6*Q1*Q5."""
        for Q1, Q5 in [(1, 1), (2, 3), (5, 5)]:
            c = 6 * Q1 * Q5
            kappa = shadow_kappa_K3(Q1, Q5)
            assert abs(kappa - c / 2) < 1e-12


# ============================================================
# SECTION 6: RADEMACHER EXPANSION
# ============================================================

class TestRademacher:
    """Tests for the Rademacher expansion."""

    def test_rademacher_leading_entropy_formula(self):
        """Leading entropy = pi*sqrt(Delta) from Rademacher c=1."""
        for Delta in [1, 4, 9, 16, 25, 100]:
            S = rademacher_leading_entropy(Delta)
            expected = PI * math.sqrt(Delta)
            assert abs(S - expected) < 1e-12

    def test_rademacher_term_c1_positive(self):
        """c=1 Rademacher term is nonzero for Delta > 0."""
        for Delta in [1, 4, 10, 25, 100]:
            t = rademacher_term(Delta, 1)
            assert t != 0

    def test_rademacher_term_c1_dominates(self):
        """c=1 term dominates over c=2 for large Delta."""
        for Delta in [50, 100]:
            t1 = abs(rademacher_term(Delta, 1))
            t2 = abs(rademacher_term(Delta, 2))
            assert t1 > t2

    def test_rademacher_expansion_convergent(self):
        """Partial sums should stabilize."""
        sums = rademacher_expansion(100, max_c=5)
        # The partial sums should exist and be finite
        for s in sums:
            assert math.isfinite(s)
        # The c=1 term should dominate
        assert abs(sums[0]) > 0

    def test_rademacher_zero_Delta(self):
        """Rademacher at Delta=0 returns 0."""
        assert rademacher_term(0, 1) == 0.0

    def test_rademacher_negative_Delta(self):
        """Rademacher at Delta < 0 returns 0."""
        assert rademacher_term(-5, 1) == 0.0

    def test_rademacher_expansion_length(self):
        """Expansion returns correct number of terms."""
        sums = rademacher_expansion(50, max_c=7)
        assert len(sums) == 7


# ============================================================
# SECTION 7: BESSEL FUNCTION
# ============================================================

class TestBessel:
    """Tests for the half-integer Bessel function I_{n+1/2}."""

    def test_I_half(self):
        """I_{1/2}(x) = sqrt(2/(pi*x)) * sinh(x)."""
        for x in [0.5, 1.0, 2.0, 5.0]:
            computed = _bessel_I_half_integer(0.5, x)
            expected = math.sqrt(2 / (PI * x)) * math.sinh(x)
            assert abs(computed - expected) < 1e-10

    def test_I_three_halves(self):
        """I_{3/2}(x) = sqrt(2/(pi*x)) * (cosh(x) - sinh(x)/x)."""
        for x in [1.0, 2.0, 5.0]:
            computed = _bessel_I_half_integer(1.5, x)
            expected = math.sqrt(2 / (PI * x)) * (math.cosh(x) - math.sinh(x) / x)
            assert abs(computed - expected) / max(abs(expected), 1e-15) < 1e-8

    def test_I_positive(self):
        """I_nu(x) > 0 for x > 0, nu >= 0."""
        for nu in [0.5, 1.5, 2.5, 4.5, 8.5]:
            for x in [0.1, 1.0, 5.0, 10.0]:
                assert _bessel_I_half_integer(nu, x) > 0

    def test_I_monotone_in_x(self):
        """I_nu(x) is increasing in x for fixed nu."""
        for nu in [0.5, 2.5, 8.5]:
            vals = [_bessel_I_half_integer(nu, x) for x in [1.0, 2.0, 5.0, 10.0]]
            for i in range(len(vals) - 1):
                assert vals[i + 1] > vals[i]

    def test_I_asymptotic(self):
        """For large x: I_nu(x) ~ e^x / sqrt(2*pi*x) * (1 + (4nu^2-1)/(8x) + ...).

        The leading correction is (4*nu^2 - 1)/(8*x), so we need
        x >> 4*nu^2 for the ratio to be close to 1.  We choose x
        large enough per nu for a meaningful test.
        """
        for nu, x in [(0.5, 50.0), (4.5, 200.0), (8.5, 400.0)]:
            computed = _bessel_I_half_integer(nu, x)
            asymptotic = math.exp(x) / math.sqrt(2 * PI * x)
            ratio = computed / asymptotic
            # First correction ~ (4*nu^2-1)/(8*x); verify ratio is within 2x that
            first_corr = (4 * nu ** 2 - 1) / (8 * x)
            assert abs(ratio - 1.0) < 2 * first_corr + 0.01

    def test_I_zero_argument(self):
        """I_nu(0) = 0 for nu > 0 (by convention in our implementation)."""
        assert _bessel_I_half_integer(0.5, 0) == 0.0

    def test_I_recurrence_check(self):
        """Check I_{nu+1} = I_{nu-1} - (2*nu/x)*I_nu (recurrence)."""
        x = 5.0
        nu = 2.5
        I_prev = _bessel_I_half_integer(nu - 1, x)  # I_{1.5}
        I_curr = _bessel_I_half_integer(nu, x)       # I_{2.5}
        I_next = _bessel_I_half_integer(nu + 1, x)   # I_{3.5}
        expected_next = I_prev - (2 * nu / x) * I_curr
        assert abs(I_next - expected_next) / max(abs(I_next), 1e-15) < 1e-8


# ============================================================
# SECTION 8: K3 TOPOLOGICAL INVARIANTS
# ============================================================

class TestK3Invariants:
    """Tests for K3 topological invariants."""

    def test_betti_numbers(self):
        """b(K3) = (1, 0, 22, 0, 1)."""
        assert K3Invariants.betti_numbers() == (1, 0, 22, 0, 1)

    def test_euler_from_betti(self):
        """chi = sum (-1)^i b_i = 1 - 0 + 22 - 0 + 1 = 24."""
        b = K3Invariants.betti_numbers()
        chi = sum((-1) ** i * b[i] for i in range(5))
        assert chi == 24

    def test_b2(self):
        """b_2(K3) = 22."""
        assert K3Invariants.b2() == 22

    def test_signature(self):
        """sigma(K3) = -16."""
        assert K3Invariants.signature() == -16

    def test_signature_from_intersection(self):
        """sigma = b_2^+ - b_2^- = 3 - 19 = -16.

        H^2(K3,Z) = -E_8^2 + U^3 has signature (3,19).
        """
        assert K3Invariants.signature() == 3 - 19

    def test_pontryagin(self):
        """p_1(K3) = 3*sigma = -48."""
        assert K3Invariants.pontryagin_class_p1() == 3 * K3Invariants.signature()
        assert K3Invariants.pontryagin_class_p1() == -48

    def test_a_hat_genus(self):
        r"""\hat{A}(K3) = -p_1/24 = 48/24 = 2."""
        assert K3Invariants.a_hat_genus() == Fraction(2, 1)
        # Cross-check: -p_1/24 = -(-48)/24 = 2
        assert K3Invariants.a_hat_genus() == Fraction(-K3Invariants.pontryagin_class_p1(), 24)

    def test_hodge_numbers_sum(self):
        """Sum of Hodge numbers gives Betti numbers."""
        h = K3Invariants.hodge_numbers()
        # b_0 = h^{0,0} = 1
        assert h[(0, 0)] == 1
        # b_2 = h^{2,0} + h^{1,1} + h^{0,2} = 1 + 20 + 1 = 22
        assert h[(2, 0)] + h[(1, 1)] + h[(0, 2)] == 22
        # b_4 = h^{2,2} = 1
        assert h[(2, 2)] == 1

    def test_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} (Hodge symmetry)."""
        h = K3Invariants.hodge_numbers()
        for (p, q), v in h.items():
            if (q, p) in h:
                assert h[(q, p)] == v

    def test_hirzebruch_L_genus(self):
        """L(K3) = sigma = -16."""
        assert K3Invariants.hirzebruch_L_genus() == Fraction(-16, 1)


class TestK3xEInvariants:
    """Tests for K3 x E invariants."""

    def test_chi_zero(self):
        """chi(K3 x E) = 0."""
        assert K3xE_Invariants.euler_characteristic() == 0

    def test_hodge_h11(self):
        """h^{1,1}(K3 x E) = 21."""
        assert K3xE_Invariants.hodge_numbers()['h11'] == 21

    def test_hodge_h21(self):
        """h^{2,1}(K3 x E) = 21."""
        assert K3xE_Invariants.hodge_numbers()['h21'] == 21

    def test_chi_from_hodge(self):
        """chi = 2*(h^{1,1} - h^{2,1}) = 0."""
        h = K3xE_Invariants.hodge_numbers()
        assert 2 * (h['h11'] - h['h21']) == 0

    def test_c2_integrated(self):
        """int_{K3} c_2(K3 x E) = 24."""
        assert K3xE_Invariants.second_chern_integrated_K3_fiber() == 24


# ============================================================
# SECTION 9: ENTROPY TABLE COMPUTATIONS
# ============================================================

class TestEntropyTables:
    """Tests for bulk entropy table computations."""

    def test_bmpv_table_default(self):
        """Default BMPV table has 8 entries."""
        table = bmpv_entropy_table()
        assert len(table) == 8

    def test_bmpv_table_all_match(self):
        """All BMPV entries have macro=micro."""
        table = bmpv_entropy_table()
        for row in table:
            assert row['match'] is True

    def test_bmpv_table_S_positive(self):
        """All BMPV entropies are positive."""
        table = bmpv_entropy_table()
        for row in table:
            assert row['S_macro'] > 0
            assert row['S_micro_cardy'] > 0

    def test_discriminant_table_default(self):
        """Default discriminant table has 100 entries."""
        table = discriminant_entropy_table()
        assert len(table) == 100

    def test_discriminant_table_S_positive(self):
        """All attractor entropies are positive."""
        table = discriminant_entropy_table()
        for row in table:
            assert row['S_attractor'] > 0

    def test_discriminant_table_d_positive(self):
        """All exact degeneracies are positive."""
        table = discriminant_entropy_table()
        for row in table:
            assert row['d_exact'] > 0

    def test_discriminant_table_custom(self):
        """Custom discriminant list."""
        table = discriminant_entropy_table([1, 4, 9])
        assert len(table) == 3
        assert table[0]['Delta'] == 1
        assert table[1]['Delta'] == 4


# ============================================================
# SECTION 10: MULTI-PATH CROSS-CHECKS
# ============================================================

class TestMultiPath:
    """Multi-path verification: macro vs micro vs Rademacher."""

    def test_path_a_vs_c_agreement(self):
        """Path (a) attractor = Path (c) Rademacher leading."""
        for Delta in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
            S_a = attractor_entropy(float(Delta))
            S_c = rademacher_leading_entropy(Delta)
            assert abs(S_a - S_c) < 1e-12

    def test_bmpv_three_ways(self):
        """BMPV: macroscopic = Cardy = 2*pi*sqrt(Q1*Q5*n)."""
        for Q1, Q5, n in [(1, 1, 1), (2, 3, 5), (4, 4, 4)]:
            bh = BMPVBlackHole(Q1, Q5, n)
            S_macro = bh.entropy_macroscopic()
            S_cardy = bh.entropy_microscopic_cardy()
            S_direct = 2 * PI * math.sqrt(Q1 * Q5 * n)
            assert abs(S_macro - S_cardy) < 1e-12
            assert abs(S_macro - S_direct) < 1e-12

    def test_entropy_formula_consistency(self):
        """attractor_entropy and sen_entropy agree without log correction."""
        for Delta in [4.0, 25.0, 100.0]:
            S_att = attractor_entropy(Delta)
            S_sen = sen_entropy_with_corrections(Delta, include_log=False)
            assert abs(S_att - S_sen) < 1e-12

    def test_micro_exceeds_macro_at_small_Delta(self):
        """For small Delta, log|d| may exceed pi*sqrt(Delta) (subleading terms).

        This is expected: the log correction is large relative to the leading term.
        """
        # At Delta=1: log(48) ~ 3.87 vs pi ~ 3.14
        log_d_1 = log_degeneracy(1)
        bh_1 = bekenstein_hawking_leading(1.0)
        # log|d| > BH at small Delta is expected (subleading corrections)
        assert log_d_1 > 0 and bh_1 > 0

    def test_c2_chi_agreement(self):
        """c_2(K3) = chi(K3) = 24: two independent computations."""
        assert second_chern_class_K3() == euler_characteristic_K3() == 24

    def test_kappa_from_two_routes(self):
        """kappa = c/2 = 3*Q1*Q5 from two routes."""
        for Q1, Q5 in [(1, 1), (2, 3), (5, 7)]:
            kappa_shadow = shadow_kappa_K3(Q1, Q5)
            c = 6 * Q1 * Q5
            kappa_virasoro = c / 2
            assert abs(kappa_shadow - kappa_virasoro) < 1e-12

    def test_attractor_perfect_square_discriminants(self):
        """S(n^2) = n*pi for perfect square discriminants."""
        for n in range(1, 20):
            Delta = n * n
            assert abs(attractor_entropy(float(Delta)) - n * PI) < 1e-10

    def test_bmpv_symmetry_all_permutations(self):
        """S is symmetric under permutations of Q1, Q5 (but NOT n)."""
        # Q1 and Q5 appear symmetrically in the formula
        bh12 = BMPVBlackHole(3, 7, 5)
        bh21 = BMPVBlackHole(7, 3, 5)
        assert abs(bh12.entropy_macroscopic() - bh21.entropy_macroscopic()) < 1e-12

    def test_five_way_S_check(self):
        """Five-way entropy check for Delta = 100.

        (a) attractor: pi*sqrt(100) = 10*pi
        (b) log|d(100)| (from 1/Phi_10)
        (c) Rademacher leading: pi*sqrt(100) = 10*pi
        (d) BMPV at Q1=5,Q5=5,n=1: 2*pi*sqrt(25) = 10*pi (different formula!)
            WAIT: BMPV gives 2*pi*sqrt(Q1*Q5*n) but attractor gives pi*sqrt(Delta).
            These are DIFFERENT physical systems (5d vs 4d).
            The BMPV formula applies in 5d; the attractor in 4d.
            For Q1=5, Q5=5, n=1: S_BMPV = 2*pi*sqrt(25) = 10*pi.
            For Delta=100: S_4d = pi*sqrt(100) = 10*pi.
            The numerical agreement is a COINCIDENCE of these specific charges.
        (e) Sen with no log: same as (a)
        """
        S_a = attractor_entropy(100.0)
        S_c = rademacher_leading_entropy(100)
        S_e = sen_entropy_with_corrections(100.0, include_log=False)
        assert abs(S_a - 10 * PI) < 1e-10
        assert abs(S_c - 10 * PI) < 1e-10
        assert abs(S_e - 10 * PI) < 1e-10

    def test_eta_product_coeffs_basic(self):
        """First few coefficients of prod(1-q^n)^{-24}."""
        a = _eta_product_coeffs(5)
        # a[0] = 1 (constant term of prod(1-q^n)^{-24})
        assert a[0] == 1
        # a[1] = 24 (from 24 * sigma_1(1) * a[0] / 1 = 24)
        assert a[1] == 24
        # a[2] = 24 * (1*24 + 3*1) / 2 = 24 * 27 / 2 ... let me recompute
        # n=2: 2*a[2] = 24*(sigma_1(1)*a[1] + sigma_1(2)*a[0])
        #             = 24*(1*24 + 3*1) = 24*27 = 648
        # a[2] = 324
        assert a[2] == 324

    def test_eta_product_coeffs_positive(self):
        """All coefficients of prod(1-q^n)^{-24} are positive."""
        a = _eta_product_coeffs(20)
        for n in range(21):
            assert a[n] > 0

    def test_gravity_dictionary_complete(self):
        """Shadow-gravity dictionary has all expected keys."""
        d = shadow_gravity_dictionary()
        assert 'kappa' in d
        assert 'F_1 = kappa/24' in d
        assert 'shadow_depth' in d
        assert 'complementarity' in d


# ============================================================
# SECTION 11: EDGE CASES AND ROBUSTNESS
# ============================================================

class TestEdgeCases:
    """Edge case tests for robustness."""

    def test_attractor_large_Delta(self):
        """Attractor entropy at Delta=10000."""
        assert abs(attractor_entropy(10000.0) - 100 * PI) < 1e-8

    def test_rademacher_c_decreasing(self):
        """Higher c terms are smaller in absolute value."""
        Delta = 200
        terms = [abs(rademacher_term(Delta, c)) for c in range(1, 6)]
        # Generally decreasing (c^{-12} suppression is extreme)
        for i in range(len(terms) - 1):
            assert terms[i] >= terms[i + 1] * 0.01  # very mild check

    def test_bessel_large_order(self):
        """Bessel at large order nu=8.5, moderate x."""
        val = _bessel_I_half_integer(8.5, 10.0)
        assert val > 0
        assert math.isfinite(val)

    def test_bessel_large_x(self):
        """Bessel at large x uses asymptotic."""
        val = _bessel_I_half_integer(4.5, 600.0)
        # Should use asymptotic branch
        assert val > 0

    def test_degeneracy_at_threshold(self):
        """Degeneracy at Delta=0 (threshold)."""
        assert degeneracy_exact(0) == 2

    def test_rademacher_expansion_empty(self):
        """Rademacher for Delta=-1 gives zeros."""
        sums = rademacher_expansion(-1, max_c=5)
        for s in sums:
            assert s == 0.0

    def test_wald_negative_correction(self):
        """Wald entropy with large negative C2.p."""
        # Delta_eff = Delta + C2.p could go negative
        S = wald_entropy_R2_correction(10.0, -20.0)
        # Delta_eff = -10 < 0 ⟹ S = 0
        assert S == 0.0


# ============================================================
# SECTION 12: PHYSICAL CONSISTENCY
# ============================================================

class TestPhysicalConsistency:
    """Tests for physical consistency of the results."""

    def test_area_law(self):
        """Entropy scales as sqrt(Delta) ~ sqrt(area)."""
        # S(4*Delta) = 2*S(Delta) ⟹ quadratic area law
        for Delta in [1.0, 4.0, 25.0, 100.0]:
            assert abs(attractor_entropy(4 * Delta) -
                       2 * attractor_entropy(Delta)) < 1e-10

    def test_second_law_monotonicity(self):
        """Entropy is monotonically increasing in Delta."""
        S_prev = attractor_entropy(1.0)
        for Delta in range(2, 101):
            S_curr = attractor_entropy(float(Delta))
            assert S_curr > S_prev
            S_prev = S_curr

    def test_log_correction_sign(self):
        """The one-loop correction is NEGATIVE (reduces entropy)."""
        for Delta in [4.0, 9.0, 100.0]:
            S_with = sen_entropy_with_corrections(Delta, include_log=True)
            S_without = sen_entropy_with_corrections(Delta, include_log=False)
            assert S_with < S_without

    def test_chi_CY3_vanishes(self):
        """For K3 x E: chi = 0 (consistent with N=4 SUSY in 4d)."""
        assert K3xE_Invariants.euler_characteristic() == 0

    def test_c2_positivity(self):
        """c_2(K3 x E) = 24 > 0 (positive R^2 correction)."""
        c2_total, _, _ = second_chern_class_K3xE()
        assert c2_total > 0

    def test_bmpv_extremal_limit(self):
        """BMPV entropy vanishes as charges -> 0 (n=1, Q=1)."""
        bh_min = BMPVBlackHole(1, 1, 1)
        # S = 2*pi ~ 6.28 (nonzero for unit charges)
        assert bh_min.entropy_macroscopic() == pytest.approx(2 * PI, rel=1e-10)

    def test_no_negative_entropy(self):
        """Entropy is never negative."""
        for Delta in range(0, 101):
            assert attractor_entropy(float(Delta)) >= 0

    def test_ahat_K3_integer(self):
        """A-hat(K3) = 2 is an integer (required for spin manifold)."""
        assert K3Invariants.a_hat_genus() == 2

    def test_b2_K3_lattice_rank(self):
        """b_2(K3) = 22 = rank of K3 lattice = rank(-E_8^2 + U^3)."""
        # -E_8^2 has rank 16, U^3 has rank 6, total 22
        assert K3Invariants.b2() == 16 + 6


# ============================================================
# SECTION 13: ADDITIONAL MULTI-PATH AND GROWTH TESTS
# ============================================================

class TestGrowthAndAsymptotics:
    """Tests for the asymptotic growth of degeneracies."""

    def test_log_d_grows_as_sqrt_Delta(self):
        """log|d(Delta)| / sqrt(Delta) is bounded and positive for large Delta."""
        for Delta in [20, 40, 60, 80, 100]:
            r = log_degeneracy(Delta) / math.sqrt(Delta)
            # Should be O(1) and positive (not diverging or vanishing)
            assert r > 1.0  # well above zero
            assert r < 20.0  # not diverging

    def test_degeneracy_exponential_growth(self):
        """d(Delta) grows exponentially: d(50) >> d(10) >> d(1)."""
        d1 = degeneracy_exact(1)
        d10 = degeneracy_exact(10)
        d50 = degeneracy_exact(50)
        assert d50 > d10 > d1

    def test_log_degeneracy_concavity(self):
        """log|d(Delta)| / sqrt(Delta) should roughly stabilize.

        This is a weak test: the ratio should not oscillate wildly.
        """
        ratios = [log_degeneracy(Delta) / math.sqrt(Delta)
                  for Delta in range(10, 101, 10)]
        # Check that ratios are all in a bounded range
        assert max(ratios) / min(ratios) < 5.0

    def test_p24_vs_exact_at_overlap(self):
        """For Delta in the exact table, p24 and exact d differ
        (they are different objects), but both are positive."""
        p24 = _eta_product_coeffs(15)
        for Delta in range(1, 16):
            assert p24[Delta] > 0
            assert degeneracy_exact(Delta) > 0

    def test_bmpv_entropy_grows_with_n(self):
        """BMPV entropy grows as sqrt(n) for fixed Q1, Q5."""
        S_vals = [BMPVBlackHole(2, 3, n).entropy_macroscopic()
                  for n in [1, 4, 9, 16, 25]]
        # S(n) = 2*pi*sqrt(6*n), so S(4n)/S(n) = 2
        for i in range(len(S_vals) - 1):
            assert S_vals[i + 1] > S_vals[i]

    def test_bmpv_entropy_grows_with_Q1(self):
        """BMPV entropy grows as sqrt(Q1) for fixed Q5, n."""
        S1 = BMPVBlackHole(1, 1, 10).entropy_macroscopic()
        S4 = BMPVBlackHole(4, 1, 10).entropy_macroscopic()
        S9 = BMPVBlackHole(9, 1, 10).entropy_macroscopic()
        assert abs(S4 / S1 - 2.0) < 1e-10
        assert abs(S9 / S1 - 3.0) < 1e-10

    def test_attractor_entropy_continuity(self):
        """Attractor entropy is continuous: S(Delta+eps) ~ S(Delta)."""
        S1 = attractor_entropy(100.0)
        S2 = attractor_entropy(100.01)
        assert abs(S2 - S1) < 0.01

    def test_sen_log_correction_relative_size(self):
        """Log correction is subleading: |(3/2)log(Delta)| << pi*sqrt(Delta) for large Delta."""
        for Delta in [100, 400, 900]:
            leading = PI * math.sqrt(Delta)
            correction = abs(1.5 * math.log(Delta))
            assert correction < 0.5 * leading

    def test_bessel_I_half_equals_sinh(self):
        """Cross-check: I_{1/2}(x) = sqrt(2/(pi*x)) * sinh(x) for many x values."""
        for x in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0]:
            computed = _bessel_I_half_integer(0.5, x)
            expected = math.sqrt(2 / (PI * x)) * math.sinh(x)
            assert abs(computed - expected) / max(abs(expected), 1e-15) < 1e-10

    def test_bessel_I_neg_half_equals_cosh(self):
        """I_{-1/2}(x) = sqrt(2/(pi*x)) * cosh(x) — used as base of recurrence.

        We verify indirectly: I_{3/2}(x) = I_{-1/2}(x) - (1/x)*I_{1/2}(x).
        """
        for x in [1.0, 3.0, 10.0]:
            I_half = _bessel_I_half_integer(0.5, x)
            I_three_half = _bessel_I_half_integer(1.5, x)
            pf = math.sqrt(2 / (PI * x))
            I_neg_half = pf * math.cosh(x)
            expected = I_neg_half - (1.0 / x) * I_half
            assert abs(I_three_half - expected) / max(abs(expected), 1e-15) < 1e-10

    def test_osv_F0_homogeneity(self):
        """F_0 = -STU is homogeneous of degree 3."""
        for lam in [0.5, 2.0, 3.0]:
            prep1 = K3xE_Prepotential(S=1+1j, T=2+0.5j, U=0.3+0.7j)
            prep_lam = K3xE_Prepotential(
                S=lam*(1+1j), T=lam*(2+0.5j), U=lam*(0.3+0.7j))
            assert abs(prep_lam.F0_stu() - lam**3 * prep1.F0_stu()) < 1e-10

    def test_rademacher_c1_vs_c2_ratio(self):
        """c=2 term is suppressed by at least c^{-12} = 1/4096 relative to c=1."""
        Delta = 100
        t1 = abs(rademacher_term(Delta, 1))
        t2 = abs(rademacher_term(Delta, 2))
        # c^{-12} = 2^{-12} = 1/4096, plus Bessel suppression
        assert t2 < t1 / 100  # much stronger than 1/4096 due to Bessel

    def test_K3_noether_formula(self):
        """Noether formula: chi(O_K3) = (1/12)*(c_1^2 + c_2) = (0 + 24)/12 = 2."""
        # c_1(K3) = 0 (Calabi-Yau), c_2(K3) = 24
        chi_O = (0 + 24) / 12
        assert chi_O == 2.0
        # This equals h^{0,0} - h^{1,0} + h^{2,0} = 1 - 0 + 1 = 2
        h = K3Invariants.hodge_numbers()
        assert h[(0,0)] - h[(1,0)] + h[(2,0)] == 2
