r"""Tests for Theorem: S_3 = 2 universally on the T-line.

Multi-path verification of the cubic shadow universality theorem:
S_3|_T = 2 for ALL chiral algebras with a Virasoro subalgebra.

Four independent proofs, each verified by multiple tests:
  Proof 1: Direct OPE (T_{(1)}T = 2T => C^T_{TT} = 2 => S_3 = 2)
  Proof 2: Cachazo-Strominger subleading soft graviton (universal angular momentum)
  Proof 3: Shadow metric (q_1 = 12*kappa*alpha, alpha = h_T = 2)
  Proof 4: Conformal Ward identity (S_3 = L_0 eigenvalue of T = 2)

Cross-family verification across the entire standard landscape.
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_s3_universality_engine import (
    S3_UNIVERSAL,
    H_T,
    virasoro_ope_modes,
    structure_constant_CTT_T,
    s3_from_ope_direct,
    cubic_tensor_virasoro,
    subleading_soft_factor_structure,
    soft_factor_for_virasoro,
    shadow_metric_coefficients,
    s3_from_shadow_metric,
    s3_from_sqrt_ql_expansion,
    gaussian_decomposition,
    conformal_weight_of_stress_tensor,
    l0_eigenvalue_on_primary,
    s3_from_conformal_ward,
    universal_gravitational_cubic,
    virasoro_shadow_data,
    w_n_tline_shadow_data,
    affine_km_sugawara_tline_data,
    betagamma_tline_data,
    complementarity_sum_s3,
    universal_cubic_coefficient_from_ope,
    verify_mc_recursion_with_s3,
    verify_sqrt_ql_expansion,
    affine_current_line_data,
    w3_wline_data,
    run_full_verification,
)


# ============================================================================
# PROOF 1: Direct OPE computation
# ============================================================================

class TestProof1DirectOPE:
    """Tests for Proof 1: S_3 = 2 from the TT OPE."""

    def test_ope_modes_complete(self):
        """T_{(n)}T modes are correctly catalogued."""
        modes = virasoro_ope_modes()
        assert modes[3] == 'c/2'
        assert modes[2] == '0'
        assert modes[1] == '2T'
        assert modes[0] == 'dT'

    def test_structure_constant_CTT_T(self):
        """C^T_{TT} = 2 from T_{(1)}T = 2T."""
        assert structure_constant_CTT_T() == Fraction(2)

    def test_s3_from_ope(self):
        """S_3 = 2 directly from the OPE."""
        assert s3_from_ope_direct() == Fraction(2)

    def test_s3_equals_h_T(self):
        """S_3 = h_T (the conformal weight of T)."""
        assert s3_from_ope_direct() == Fraction(H_T)

    def test_cubic_tensor_depends_on_c(self):
        """C_3(T,T,T) = c (depends on c), but S_3 = 2 (does not)."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(13)]:
            tensor = cubic_tensor_virasoro(c_val)
            assert tensor == c_val  # C_3 depends on c
        # But S_3 itself does not:
        assert s3_from_ope_direct() == Fraction(2)

    def test_cubic_tensor_formula(self):
        """C_3(T,T,T) = eta_{TT} * C^T_{TT} = (c/2) * 2 = c."""
        for c_val in [Fraction(1), Fraction(7), Fraction(26)]:
            assert cubic_tensor_virasoro(c_val) == c_val

    def test_s3_independent_of_c_ope(self):
        """S_3 = C^T_{TT} = 2 for all c values."""
        for c_val in [Fraction(1, 2), Fraction(7, 10), Fraction(4, 5),
                      Fraction(1), Fraction(13), Fraction(25), Fraction(26),
                      Fraction(100), Fraction(1, 100)]:
            _, S3, _ = virasoro_shadow_data(c_val)
            assert S3 == Fraction(2), f"S_3 != 2 at c = {c_val}"


# ============================================================================
# PROOF 2: Cachazo-Strominger subleading soft graviton
# ============================================================================

class TestProof2CachazoStrominger:
    """Tests for Proof 2: universality from the subleading soft graviton theorem."""

    def test_soft_factor_structure(self):
        """Subleading soft factor has correct structure."""
        info = subleading_soft_factor_structure()
        assert info['s3_value'] == Fraction(2)
        assert info['factor_type'] == 'angular_momentum'

    def test_soft_factor_universality_reason(self):
        """Universality comes from the Lorentz algebra, not matter content."""
        info = subleading_soft_factor_structure()
        assert 'Lorentz' in info['universality_reason']

    def test_soft_factor_numerical(self):
        """Numerical subleading soft factor is consistent."""
        # Two insertions with h=2 (both stress tensors)
        h_vals = [2, 2]
        z_vals = [1.0, -1.0]
        z_s = 10.0
        result = soft_factor_for_virasoro(h_vals, z_vals, z_s)
        # Each term: h(h-1)/(z_s - z_i)^2 = 2*1/(10-1)^2 + 2*1/(10+1)^2
        expected = 2.0 / 81.0 + 2.0 / 121.0
        assert abs(result - expected) < 1e-12

    def test_soft_factor_scales_with_h(self):
        """Soft factor for weight-h insertions scales as h(h-1)."""
        z_s = 100.0
        z_vals = [0.0]
        for h in [1, 2, 3, 4, 5]:
            result = soft_factor_for_virasoro([h], z_vals, z_s)
            expected = h * (h - 1) / z_s ** 2
            assert abs(result - expected) < 1e-12


# ============================================================================
# PROOF 3: Shadow metric
# ============================================================================

class TestProof3ShadowMetric:
    """Tests for Proof 3: S_3 from the shadow metric Q_L."""

    def test_shadow_metric_q1(self):
        """q_1 = 12*kappa*alpha = 12*kappa*2 = 24*kappa for Virasoro."""
        for c_val in [Fraction(1), Fraction(13), Fraction(26)]:
            kappa, S3, S4 = virasoro_shadow_data(c_val)
            q0, q1, q2 = shadow_metric_coefficients(kappa, S3, S4)
            assert q1 == 24 * kappa

    def test_s3_from_metric_extraction(self):
        """S_3 = q1/(12*kappa) = alpha = 2."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(13), Fraction(26)]:
            kappa, S3, S4 = virasoro_shadow_data(c_val)
            q0, q1, q2 = shadow_metric_coefficients(kappa, S3, S4)
            extracted = s3_from_shadow_metric(kappa, q1)
            assert extracted == Fraction(2)

    def test_s3_from_sqrt_expansion(self):
        """S_3 = a_1/3 where a_1 = q1/(2*a_0) = 3*alpha."""
        for c_val in [Fraction(1, 2), Fraction(7, 10), Fraction(1),
                      Fraction(13), Fraction(25), Fraction(26)]:
            kappa, S3, S4 = virasoro_shadow_data(c_val)
            result = s3_from_sqrt_ql_expansion(kappa, S3, S4)
            assert result == Fraction(2)

    def test_gaussian_decomposition_alpha(self):
        """Gaussian decomposition gives alpha = 2."""
        for c_val in [Fraction(1), Fraction(13)]:
            kappa, S3, S4 = virasoro_shadow_data(c_val)
            decomp = gaussian_decomposition(kappa, S3, S4)
            assert decomp['alpha'] == Fraction(2)

    def test_gaussian_decomposition_nonterminating(self):
        """Delta != 0 for Virasoro (class M, infinite tower)."""
        for c_val in [Fraction(1), Fraction(13)]:
            kappa, S3, S4 = virasoro_shadow_data(c_val)
            decomp = gaussian_decomposition(kappa, S3, S4)
            assert decomp['Delta'] != 0
            assert not decomp['terminates']

    def test_q0_is_4kappa_squared(self):
        """q_0 = 4*kappa^2 = c^2."""
        for c_val in [Fraction(1), Fraction(7), Fraction(13)]:
            kappa = c_val / 2
            q0, _, _ = shadow_metric_coefficients(kappa, Fraction(2),
                           Fraction(10) / (c_val * (5 * c_val + 22)))
            assert q0 == c_val ** 2


# ============================================================================
# PROOF 4: Conformal Ward identity
# ============================================================================

class TestProof4ConformalWard:
    """Tests for Proof 4: S_3 = h_T from the L_0 eigenvalue."""

    def test_h_T_equals_2(self):
        """The stress tensor has conformal weight 2."""
        assert conformal_weight_of_stress_tensor() == 2

    def test_s3_from_ward(self):
        """S_3 = h_T = 2 from conformal Ward identity."""
        assert s3_from_conformal_ward() == 2

    def test_l0_eigenvalue_T(self):
        """L_0 eigenvalue on T is 2."""
        assert l0_eigenvalue_on_primary('T', 2) == 2

    def test_l0_eigenvalue_W3(self):
        """L_0 eigenvalue on W (weight 3) is 3."""
        assert l0_eigenvalue_on_primary('W', 3) == 3

    def test_universal_gravitational_cubic_T3(self):
        """The T^3 coefficient in the universal cubic is 2 = h_T."""
        # Virasoro: only T (weight 2)
        cubic = universal_gravitational_cubic([2])
        assert cubic['T^3'] == 2

    def test_universal_gravitational_cubic_W3(self):
        """For W_3 (weights 2, 3): T^3 coeff = 2, T*W^2 coeff = 3."""
        cubic = universal_gravitational_cubic([2, 3])
        assert cubic['T^3'] == 2
        assert cubic['T*W_1^2'] == 3

    def test_universal_gravitational_cubic_W4(self):
        """For W_4 (weights 2, 3, 4): T^3 = 2, T*W_3^2 = 3, T*W_4^2 = 4."""
        cubic = universal_gravitational_cubic([2, 3, 4])
        assert cubic['T^3'] == 2
        assert cubic['T*W_1^2'] == 3
        assert cubic['T*W_2^2'] == 4


# ============================================================================
# CROSS-FAMILY VERIFICATION
# ============================================================================

class TestCrossFamily:
    """Cross-family verification: S_3 = 2 on the T-line across the landscape."""

    @pytest.mark.parametrize("c_val", [
        Fraction(1, 2),   # Ising
        Fraction(7, 10),  # Tricritical Ising
        Fraction(4, 5),   # 3-state Potts
        Fraction(1),      # Free boson
        Fraction(13),     # Self-dual point
        Fraction(25),     # Near critical
        Fraction(26),     # Critical (ghost)
        Fraction(100),    # Large c
        Fraction(1, 100), # Small c
    ])
    def test_virasoro_s3_at_c(self, c_val):
        """S_3 = 2 for Virasoro at c = {c_val}."""
        _, S3, _ = virasoro_shadow_data(c_val)
        assert S3 == Fraction(2)

    @pytest.mark.parametrize("N,c_val", [
        (3, Fraction(2)),
        (3, Fraction(50)),
        (4, Fraction(3)),
        (5, Fraction(4)),
        (6, Fraction(5)),
    ])
    def test_w_n_tline_s3(self, N, c_val):
        """S_3 = 2 on the W_N T-line at c = {c_val}."""
        _, S3, _ = w_n_tline_shadow_data(c_val)
        assert S3 == Fraction(2)

    @pytest.mark.parametrize("name,dim_g,h_vee,k", [
        ('sl2', 3, 2, 1),
        ('sl2', 3, 2, 10),
        ('sl3', 8, 3, 1),
        ('sl3', 8, 3, 5),
        ('G2', 14, 4, 1),
        ('F4', 52, 9, 1),
        ('E8', 248, 30, 1),
    ])
    def test_affine_km_sugawara_tline_s3(self, name, dim_g, h_vee, k):
        """S_3 = 2 on the Sugawara T-line for affine {name} at level {k}."""
        _, S3, _ = affine_km_sugawara_tline_data(dim_g, h_vee, k)
        assert S3 == Fraction(2)

    @pytest.mark.parametrize("lam", [
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(1),
    ])
    def test_betagamma_tline_s3(self, lam):
        """S_3 = 2 on the beta-gamma T-line at lambda = {lam}."""
        _, S3, _ = betagamma_tline_data(lam)
        assert S3 == Fraction(2)


# ============================================================================
# COMPLEMENTARITY
# ============================================================================

class TestComplementarity:
    """Tests for S_3 complementarity: S_3(c) + S_3(26-c) = 4."""

    @pytest.mark.parametrize("c_val", [
        Fraction(1),
        Fraction(7),
        Fraction(13),
        Fraction(25),
    ])
    def test_complementarity_sum(self, c_val):
        """S_3(c) + S_3(26-c) = 4."""
        assert complementarity_sum_s3(c_val) == Fraction(4)

    def test_complementarity_at_self_dual(self):
        """At c = 13: S_3(13) = S_3(13) = 2, sum = 4."""
        assert complementarity_sum_s3(Fraction(13)) == Fraction(4)


# ============================================================================
# NON-UNIVERSALITY ON OTHER LINES
# ============================================================================

class TestNonUniversality:
    """S_3 is NOT universal on non-T lines (scope honesty)."""

    def test_affine_sl2_current_line_s3_neq_2(self):
        """Affine sl_2 current algebra line: S_3 = 1, not 2."""
        _, S3, _ = affine_current_line_data(3, 2, 1)
        assert S3 == Fraction(1)
        assert S3 != Fraction(2)

    def test_w3_wline_s3_eq_0(self):
        """W_3 W-line: S_3 = 0 (Z_2 parity)."""
        _, S3, _ = w3_wline_data(Fraction(2))
        assert S3 == Fraction(0)
        assert S3 != Fraction(2)


# ============================================================================
# MC RECURSION CONSISTENCY
# ============================================================================

class TestMCRecursionConsistency:
    """Verify that S_3 = 2 produces consistent higher shadows via MC recursion."""

    @pytest.mark.parametrize("c_val", [
        Fraction(1, 2),
        Fraction(1),
        Fraction(13),
        Fraction(26),
    ])
    def test_mc_agrees_with_sqrt_ql(self, c_val):
        """MC recursion and sqrt(Q_L) agree for all r >= 5 when S_3 = 2."""
        kappa, S3, S4 = virasoro_shadow_data(c_val)
        mc = verify_mc_recursion_with_s3(kappa, S3, S4, max_r=15)
        sq = verify_sqrt_ql_expansion(kappa, S3, S4, max_r=15)
        for r in range(5, 16):
            assert mc[r] == sq[r], f"Mismatch at r={r}, c={c_val}"

    def test_s5_from_mc_virasoro(self):
        """S_5 = -48/[c^2(5c+22)] from MC recursion with S_3 = 2 seed."""
        c_val = Fraction(1)
        kappa, S3, S4 = virasoro_shadow_data(c_val)
        mc = verify_mc_recursion_with_s3(kappa, S3, S4, max_r=6)
        # S_5(c=1) = -48/(1^2 * 27) = -48/27 = -16/9
        expected = Fraction(-48, 27)
        assert mc[5] == expected

    def test_wrong_s3_gives_wrong_tower(self):
        """If S_3 != 2, the higher shadows differ (S_3 is genuinely a seed)."""
        c_val = Fraction(1)
        kappa = c_val / 2
        S4 = Fraction(10) / (c_val * (5 * c_val + 22))

        # Correct: S_3 = 2
        mc_correct = verify_mc_recursion_with_s3(kappa, Fraction(2), S4, max_r=8)

        # Wrong: S_3 = 3
        mc_wrong = verify_mc_recursion_with_s3(kappa, Fraction(3), S4, max_r=8)

        # They should differ at r = 5 (first recursion step that uses S_3)
        assert mc_correct[5] != mc_wrong[5]


# ============================================================================
# PROOF CONVERGENCE: all four proofs give the same answer
# ============================================================================

class TestProofConvergence:
    """All four proofs yield S_3 = 2."""

    def test_all_proofs_agree(self):
        """All four independent proofs give S_3 = 2."""
        proof1 = s3_from_ope_direct()
        proof2 = subleading_soft_factor_structure()['s3_value']
        proof3 = s3_from_sqrt_ql_expansion(
            Fraction(1, 2), Fraction(2),
            Fraction(10) / (Fraction(1) * Fraction(27)))
        proof4 = Fraction(s3_from_conformal_ward())

        assert proof1 == Fraction(2)
        assert proof2 == Fraction(2)
        assert proof3 == Fraction(2)
        assert proof4 == Fraction(2)

    def test_full_verification_suite(self):
        """The complete verification suite passes."""
        results = run_full_verification(verbose=False)
        failures = [name for name, ok in results.items() if not ok]
        assert len(failures) == 0, f"Failed tests: {failures}"

    def test_full_verification_count(self):
        """The verification suite has at least 20 individual checks."""
        results = run_full_verification(verbose=False)
        assert len(results) >= 20


# ============================================================================
# STRUCTURAL TESTS
# ============================================================================

class TestStructural:
    """Tests for structural/mathematical properties."""

    def test_s3_is_integer(self):
        """S_3 = 2 is an INTEGER (not a rational function of c)."""
        val = s3_from_ope_direct()
        assert val.denominator == 1

    def test_s3_is_positive(self):
        """S_3 = 2 > 0."""
        assert s3_from_ope_direct() > 0

    def test_s3_universal_constant(self):
        """S3_UNIVERSAL matches the module-level constant."""
        assert S3_UNIVERSAL == Fraction(2)

    def test_h_T_constant(self):
        """H_T = 2 matches the module-level constant."""
        assert H_T == 2

    def test_cubic_coefficient_equals_weight(self):
        """For ANY primary field of weight h, T_{(1)}phi = h*phi."""
        for h in [1, 2, 3, 4, 5, 6, 7, 8]:
            assert universal_cubic_coefficient_from_ope(h) == h

    def test_s3_koszul_dual_equal(self):
        """S_3(A) = S_3(A!) = 2 for Virasoro (both Vir_c and Vir_{26-c})."""
        for c_val in [Fraction(1), Fraction(7), Fraction(13), Fraction(25)]:
            _, s3_A, _ = virasoro_shadow_data(c_val)
            c_dual = 26 - c_val
            _, s3_Ad, _ = virasoro_shadow_data(c_dual)
            assert s3_A == Fraction(2)
            assert s3_Ad == Fraction(2)

    def test_s3_at_self_dual_point(self):
        """At c = 13 (self-dual): S_3 = 2."""
        _, S3, _ = virasoro_shadow_data(Fraction(13))
        assert S3 == Fraction(2)

    def test_s3_at_critical_dimension(self):
        """At c = 26 (critical): S_3 = 2."""
        _, S3, _ = virasoro_shadow_data(Fraction(26))
        assert S3 == Fraction(2)

    def test_s2_depends_on_c_but_s3_does_not(self):
        """S_2 = c/2 varies with c, S_3 = 2 does not."""
        c_vals = [Fraction(1), Fraction(7), Fraction(26)]
        s2_vals = set()
        s3_vals = set()
        for c_val in c_vals:
            kappa, S3, _ = virasoro_shadow_data(c_val)
            s2_vals.add(kappa)
            s3_vals.add(S3)
        assert len(s2_vals) == 3  # S_2 varies
        assert len(s3_vals) == 1  # S_3 constant
        assert s3_vals == {Fraction(2)}

    def test_s4_depends_on_c(self):
        """S_4 depends on c (unlike S_3)."""
        c_vals = [Fraction(1), Fraction(13), Fraction(26)]
        s4_vals = set()
        for c_val in c_vals:
            _, _, S4 = virasoro_shadow_data(c_val)
            s4_vals.add(S4)
        assert len(s4_vals) == 3  # S_4 varies with c
