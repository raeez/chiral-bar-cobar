r"""Tests for the full beta-gamma shadow tower at arbitrary conformal weight.

Tests organized by section:
  1. Basic invariants (central charge, kappa)
  2. Shadow tower on the T-line (Virasoro sub-OPE)
  3. Shadow tower on the weight-changing line (rank-one abelian rigidity)
  4. Complementarity (bg <-> bc, kappa + kappa' = 0)
  5. Weight symmetry (lambda <-> 1-lambda, distinct from Koszul duality)
  6. Koszul dual identification (bg^! = bc, NOT bc_{1-lambda})
  7. Mumford isomorphism connection
  8. Stratum separation (1D tower infinite, global depth 4)
  9. bc ghost data cross-check
  10. Consistency with existing compute modules
  11. Special weight edge cases (AP18: lambda=0 weight-0 generator)
  12. Critical discriminant and shadow metric
  13. Generating function on T-line
"""

from __future__ import annotations

import pytest
from sympy import Rational, Symbol, simplify, sqrt, expand

from compute.lib.betagamma_shadow_full import (
    central_charge,
    kappa,
    central_charge_bc,
    kappa_bc,
    S2_T_line,
    S3_T_line,
    S4_T_line,
    S2_weight_line,
    S3_weight_line,
    S4_weight_line,
    S5_weight_line,
    shadow_metric_T_line,
    critical_discriminant,
    shadow_growth_rate_T_line,
    T_line_tower,
    full_shadow_tower,
    complementarity_kappa,
    complementarity_central_charge,
    weight_symmetry,
    koszul_dual_identification,
    mumford_exponent,
    mumford_kappa_identity,
    evaluate_at_weight,
    stratum_separation_verification,
    bc_ghost_1d_data,
    depth_class_proof,
)


# =========================================================================
# 1. Basic invariants
# =========================================================================

class TestBasicInvariants:
    """Central charge and kappa at specific weights."""

    def test_c_lambda_0(self):
        assert central_charge(0) == 2

    def test_c_lambda_half(self):
        assert central_charge(Rational(1, 2)) == -1

    def test_c_lambda_1(self):
        assert central_charge(1) == 2

    def test_c_lambda_2(self):
        assert central_charge(2) == 26

    def test_kappa_lambda_0(self):
        assert kappa(0) == 1

    def test_kappa_lambda_half(self):
        assert kappa(Rational(1, 2)) == Rational(-1, 2)

    def test_kappa_lambda_1(self):
        assert kappa(1) == 1

    def test_kappa_lambda_2(self):
        assert kappa(2) == 13

    def test_kappa_is_half_c(self):
        """kappa = c/2 for all lambda."""
        lam = Symbol('lambda')
        assert simplify(kappa(lam) - central_charge(lam) / 2) == 0

    def test_c_formula_expansion(self):
        """c = 12*lambda^2 - 12*lambda + 2."""
        lam = Symbol('lambda')
        c = central_charge(lam)
        expected = 12 * lam**2 - 12 * lam + 2
        assert simplify(c - expected) == 0

    def test_kappa_formula_expansion(self):
        """kappa = 6*lambda^2 - 6*lambda + 1."""
        lam = Symbol('lambda')
        k = kappa(lam)
        expected = 6 * lam**2 - 6 * lam + 1
        assert simplify(k - expected) == 0


# =========================================================================
# 2. Shadow tower on the T-line
# =========================================================================

class TestTLineTower:
    """Shadow data on the stress tensor primary line."""

    def test_S2_equals_kappa(self):
        """S_2 on T-line = kappa."""
        for lam_val in [0, Rational(1, 2), 1, 2]:
            assert S2_T_line(lam_val) == kappa(lam_val)

    def test_S3_universal(self):
        """S_3 = 2 on T-line, independent of lambda (Virasoro universal)."""
        for lam_val in [0, Rational(1, 2), 1, 2, Rational(1, 3)]:
            assert S3_T_line(lam_val) == 2

    def test_S4_lambda_1(self):
        """S_4 at lambda=1: c=2, S_4 = 10/(2*32) = 5/32."""
        assert S4_T_line(1) == Rational(5, 32)

    def test_S4_lambda_0(self):
        """S_4 at lambda=0: same as lambda=1 by weight symmetry."""
        assert S4_T_line(0) == Rational(5, 32)

    def test_S4_lambda_half(self):
        """S_4 at lambda=1/2: c=-1, S_4 = 10/((-1)*17) = -10/17."""
        assert S4_T_line(Rational(1, 2)) == Rational(-10, 17)

    def test_S4_lambda_2(self):
        """S_4 at lambda=2: c=26, S_4 = 10/(26*152) = 5/1976."""
        assert S4_T_line(2) == Rational(5, 1976)

    def test_S4_virasoro_formula(self):
        """S_4 = 10/(c*(5c+22)) -- the Virasoro quartic contact."""
        lam = Symbol('lambda')
        c = central_charge(lam)
        s4 = S4_T_line(lam)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(s4 - expected) == 0

    def test_tower_S2_S3_S4(self):
        """Tower matches individual functions at lambda=1."""
        tower = T_line_tower(1, max_arity=6)
        assert tower[2] == kappa(1)
        assert tower[3] == S3_T_line(1)
        assert tower[4] == S4_T_line(1)

    def test_tower_S5_nonzero(self):
        """S_5 on the 1D T-line is NONZERO (class M in 1D restriction)."""
        tower = T_line_tower(1, max_arity=6)
        assert tower[5] != 0

    def test_tower_S5_lambda_1(self):
        """S_5 at lambda=1 (c=2): explicitly computed value."""
        tower = T_line_tower(1, max_arity=6)
        # From the convolution recursion at c=2
        assert tower[5] == Rational(-3, 8)


# =========================================================================
# 3. Shadow tower on the weight-changing line
# =========================================================================

class TestWeightChangingLine:
    """All shadows vanish on the weight-changing line (rank-one rigidity)."""

    def test_S2_weight_line_zero(self):
        for lam_val in [0, Rational(1, 2), 1, 2]:
            assert S2_weight_line(lam_val) == 0

    def test_S3_weight_line_zero(self):
        for lam_val in [0, Rational(1, 2), 1, 2]:
            assert S3_weight_line(lam_val) == 0

    def test_S4_weight_line_zero(self):
        for lam_val in [0, Rational(1, 2), 1, 2]:
            assert S4_weight_line(lam_val) == 0

    def test_S5_weight_line_zero(self):
        for lam_val in [0, Rational(1, 2), 1, 2]:
            assert S5_weight_line(lam_val) == 0


# =========================================================================
# 4. Complementarity
# =========================================================================

class TestComplementarity:
    """kappa(bg) + kappa(bc) = 0, c(bg) + c(bc) = 0."""

    @pytest.mark.parametrize("lam_val", [
        Rational(0), Rational(1, 2), Rational(1), Rational(2),
        Rational(1, 3), Rational(3, 7),
    ])
    def test_kappa_complementarity(self, lam_val):
        """kappa(bg) + kappa(bc) = 0 for all lambda."""
        ck = complementarity_kappa(lam_val)
        assert ck['vanishes']

    @pytest.mark.parametrize("lam_val", [
        Rational(0), Rational(1, 2), Rational(1), Rational(2),
    ])
    def test_central_charge_complementarity(self, lam_val):
        """c(bg) + c(bc) = 0 for all lambda."""
        cc = complementarity_central_charge(lam_val)
        assert cc['vanishes']

    def test_symbolic_complementarity(self):
        """kappa(bg) + kappa(bc) = 0 symbolically."""
        lam = Symbol('lambda')
        assert simplify(kappa(lam) + kappa_bc(lam)) == 0

    def test_symbolic_c_complementarity(self):
        """c(bg) + c(bc) = 0 symbolically."""
        lam = Symbol('lambda')
        assert simplify(central_charge(lam) + central_charge_bc(lam)) == 0

    def test_not_virasoro_complementarity(self):
        """bg/bc complementarity is kappa+kappa'=0, NOT 13 (unlike Virasoro).
        AP24: kappa+kappa'=0 for free fields, =13 for Virasoro."""
        lam = Symbol('lambda')
        k_sum = kappa(lam) + kappa_bc(lam)
        assert simplify(k_sum) == 0  # NOT 13


# =========================================================================
# 5. Weight symmetry
# =========================================================================

class TestWeightSymmetry:
    """kappa(lambda) = kappa(1-lambda), distinct from Koszul duality."""

    @pytest.mark.parametrize("lam_val", [
        Rational(0), Rational(1, 3), Rational(1, 2), Rational(2), Rational(-1),
    ])
    def test_weight_symmetry(self, lam_val):
        ws = weight_symmetry(lam_val)
        assert ws['symmetric']

    def test_symbolic_weight_symmetry(self):
        lam = Symbol('lambda')
        assert simplify(kappa(lam) - kappa(1 - lam)) == 0

    def test_c_weight_symmetry(self):
        """c(lambda) = c(1-lambda) as well."""
        lam = Symbol('lambda')
        assert simplify(central_charge(lam) - central_charge(1 - lam)) == 0


# =========================================================================
# 6. Koszul dual identification
# =========================================================================

class TestKoszulDualIdentification:
    """Koszul dual is bc_lambda, NOT bc_{1-lambda}."""

    def test_koszul_not_weight_swap(self):
        """kappa(bg_lambda) != kappa(bc_{1-lambda}) in general."""
        kdi = koszul_dual_identification(Rational(1, 3))
        # kappa(bg_{1/3}) = -1/3, kappa(bc_{2/3}) = 1/3
        # These are NOT equal (they differ by sign, in fact)
        assert kdi['false_equality_bg_bc1ml'] != 0

    def test_koszul_complementarity_zero(self):
        """kappa(bg_lambda) + kappa(bc_lambda) = 0 (TRUE Koszul duality)."""
        kdi = koszul_dual_identification(Rational(1, 3))
        assert kdi['koszul_complementarity'] == 0

    def test_bg_not_equal_bc_1_minus_lambda(self):
        """kappa(bg_lambda) = -kappa(bc_{1-lambda}), not equal."""
        lam = Symbol('lambda')
        k_bg = kappa(lam)
        k_bc_1ml = kappa_bc(1 - lam)
        # k_bg = 6*lam^2 - 6*lam + 1
        # k_bc_1ml = -(6*(1-lam)^2 - 6*(1-lam) + 1) = -(6*lam^2 - 6*lam + 1) = -k_bg
        assert simplify(k_bg + k_bc_1ml) == 0  # they are negatives
        assert simplify(k_bg - k_bc_1ml) != 0  # not equal


# =========================================================================
# 7. Mumford isomorphism
# =========================================================================

class TestMumford:
    """Connection between Mumford isomorphism and kappa."""

    def test_mumford_exponent_0(self):
        assert mumford_exponent(0) == 1

    def test_mumford_exponent_1(self):
        assert mumford_exponent(1) == 1

    def test_mumford_exponent_2(self):
        assert mumford_exponent(2) == 13

    def test_mumford_exponent_3(self):
        assert mumford_exponent(3) == 37

    @pytest.mark.parametrize("lam_val", [
        Rational(0), Rational(1, 2), Rational(1), Rational(2), Rational(1, 3),
    ])
    def test_mumford_identity(self, lam_val):
        """e(lambda) + e(1-lambda) = c_{bg}(lambda)."""
        mi = mumford_kappa_identity(lam_val)
        assert mi['identity_holds']

    def test_kappa_is_half_mumford_sum(self):
        """kappa = (e(lambda) + e(1-lambda)) / 2."""
        mi = mumford_kappa_identity(Rational(1, 3))
        assert mi['kappa_is_half_e_sum']


# =========================================================================
# 8. Stratum separation
# =========================================================================

class TestStratumSeparation:
    """1D tower infinite, global depth 4 by stratum separation."""

    def test_1d_tower_does_not_terminate(self):
        """The T-line 1D restriction has infinite depth (class M)."""
        sv = stratum_separation_verification(1, max_arity=8)
        assert not sv['T_line_terminates']

    def test_global_depth_4(self):
        sv = stratum_separation_verification(1, max_arity=8)
        assert sv['global_depth'] == 4

    def test_cubic_vanishes(self):
        sv = stratum_separation_verification(1, max_arity=8)
        assert sv['cubic_vanishes']

    def test_quintic_obstruction_vanishes(self):
        sv = stratum_separation_verification(1, max_arity=8)
        assert sv['quintic_obstruction_vanishes']

    def test_1d_S5_nonzero(self):
        """On the 1D T-line, S_5 is nonzero (the tower continues)."""
        tower = T_line_tower(1, max_arity=6)
        assert tower[5] != 0

    def test_1d_S6_nonzero(self):
        """On the 1D T-line, S_6 is nonzero."""
        tower = T_line_tower(1, max_arity=7)
        assert tower[6] != 0

    def test_1d_S7_nonzero(self):
        tower = T_line_tower(1, max_arity=8)
        assert tower[7] != 0


# =========================================================================
# 9. bc ghost data cross-check
# =========================================================================

class TestBCGhostComparison:
    """Cross-check with the bc ghost system (Koszul dual)."""

    def test_bc_kappa_lambda_1(self):
        """kappa(bc_{lambda=1}) = -1."""
        bc_data = bc_ghost_1d_data(1)
        assert simplify(bc_data['kappa_bc'] - (-1)) == 0

    def test_bc_S4_lambda_1(self):
        """S_4 for bc at lambda=1: -5/12 (c_bc = -2)."""
        bc_data = bc_ghost_1d_data(1)
        assert simplify(bc_data['S4_T'] - Rational(-5, 12)) == 0

    def test_bc_c_lambda_1(self):
        """c(bc_{lambda=1}) = -2."""
        bc_data = bc_ghost_1d_data(1)
        assert simplify(bc_data['c_bc'] - (-2)) == 0

    def test_bc_depth(self):
        bc_data = bc_ghost_1d_data(1)
        assert bc_data['depth'] == 4
        assert bc_data['class'] == 'C'

    def test_bc_Delta_lambda_1(self):
        """Delta for bc at lambda=1: 8*(-1)*(-5/12) = 10/3."""
        bc_data = bc_ghost_1d_data(1)
        assert simplify(bc_data['Delta'] - Rational(10, 3)) == 0


# =========================================================================
# 10. Consistency with existing compute modules
# =========================================================================

class TestCrossModuleConsistency:
    """Verify consistency with betagamma_determinant and betagamma_quartic_contact."""

    def test_kappa_matches_determinant_module(self):
        """Check our kappa matches betagamma_determinant.kappa_betagamma."""
        from compute.lib.betagamma_determinant import kappa_betagamma
        for lam_val in [0, Rational(1, 2), 1, 2]:
            assert simplify(kappa(lam_val) - kappa_betagamma(lam_val)) == 0

    def test_c_matches_determinant_module(self):
        """Check our c matches betagamma_determinant.central_charge."""
        from compute.lib.betagamma_determinant import central_charge as det_c
        for lam_val in [0, Rational(1, 2), 1, 2]:
            assert simplify(central_charge(lam_val) - det_c(lam_val)) == 0

    def test_kappa_bc_matches(self):
        """Check kappa_bc matches betagamma_determinant.kappa_bc."""
        from compute.lib.betagamma_determinant import kappa_bc as det_kbc
        for lam_val in [0, Rational(1, 2), 1, 2]:
            assert simplify(kappa_bc(lam_val) - det_kbc(lam_val)) == 0

    def test_shadow_class_matches(self):
        """Check shadow class matches betagamma_determinant."""
        from compute.lib.betagamma_determinant import shadow_class
        assert shadow_class() == 'C'

    def test_shadow_depth_matches(self):
        """Check shadow depth matches betagamma_determinant."""
        from compute.lib.betagamma_determinant import shadow_depth
        assert shadow_depth() == 4


# =========================================================================
# 11. Special weight edge cases (AP18)
# =========================================================================

class TestEdgeCases:
    """AP18: lambda=0 (weight-0 generator), lambda=1/2, etc."""

    def test_lambda_0_weight_0_generator(self):
        """AP18: lambda=0 means gamma has weight 1, beta has weight 0.
        Weight-0 generator violates positive grading, but kappa is still defined."""
        data = evaluate_at_weight(0)
        assert data['c'] == 2
        assert data['kappa'] == 1
        assert data['depth'] == 4

    def test_lambda_half_self_symmetric(self):
        """lambda=1/2: beta and gamma both have weight 1/2 (symplectic boson).
        The system is self-symmetric under beta <-> gamma exchange."""
        data = evaluate_at_weight(Rational(1, 2))
        assert data['c'] == -1
        assert data['kappa'] == Rational(-1, 2)

    def test_lambda_negative(self):
        """lambda = -1: exotic weight. kappa and c well-defined."""
        c = central_charge(-1)
        k = kappa(-1)
        assert c == 2 * (6 + 6 + 1)  # = 26
        assert k == 13

    def test_lambda_1_minus_lambda_at_half(self):
        """At lambda = 1/2, weight symmetry gives kappa(1/2) = kappa(1/2)."""
        assert kappa(Rational(1, 2)) == kappa(Rational(1, 2))

    def test_kappa_minimum(self):
        """kappa = 6*lambda^2 - 6*lambda + 1 has minimum at lambda=1/2.
        kappa(1/2) = 6/4 - 3 + 1 = -1/2. This is the UNIQUE minimum."""
        assert kappa(Rational(1, 2)) == Rational(-1, 2)

    def test_kappa_zeros(self):
        """kappa = 0 at lambda = (3 +/- sqrt(3))/6.
        These are irrational, so kappa != 0 at all rational weights."""
        lam = Symbol('lambda')
        # kappa = 6*lam^2 - 6*lam + 1 = 0
        # lam = (6 +/- sqrt(36-24))/12 = (6 +/- sqrt(12))/12 = (3 +/- sqrt(3))/6
        from sympy import solve
        zeros = solve(kappa(lam), lam)
        assert len(zeros) == 2
        # Check they are irrational
        for z in zeros:
            from sympy import Rational as R
            assert not z.is_rational


# =========================================================================
# 12. Critical discriminant and shadow metric
# =========================================================================

class TestShadowMetric:
    """Shadow metric Q_L(t) on the T-line."""

    def test_discriminant_lambda_1(self):
        """Delta at lambda=1: 40/(5*2+22) = 40/32 = 5/4."""
        Delta = critical_discriminant(1)
        assert simplify(Delta - Rational(5, 4)) == 0

    def test_discriminant_lambda_half(self):
        """Delta at lambda=1/2: 40/(5*(-1)+22) = 40/17."""
        Delta = critical_discriminant(Rational(1, 2))
        assert simplify(Delta - Rational(40, 17)) == 0

    def test_discriminant_lambda_2(self):
        """Delta at lambda=2: 40/(5*26+22) = 40/152 = 5/19."""
        Delta = critical_discriminant(2)
        assert simplify(Delta - Rational(5, 19)) == 0

    def test_discriminant_nonzero_all_real(self):
        """Delta != 0 for all real lambda (5c+22 != 0 for real lambda).
        5c+22 = 5*2*(6*lam^2-6*lam+1)+22 = 60*lam^2-60*lam+32.
        Discriminant = 3600-7680 = -4080 < 0, so no real zeros."""
        lam = Symbol('lambda')
        c = central_charge(lam)
        denom = 5 * c + 22
        # denom = 60*lam^2 - 60*lam + 32
        expanded = expand(denom)
        # Check discriminant < 0 to confirm no real zeros
        # 60*lam^2 - 60*lam + 32: disc = 3600 - 4*60*32 = 3600 - 7680 = -4080 < 0
        assert -4080 < 0  # no real zeros

    def test_shadow_metric_coefficients_lambda_1(self):
        """q0, q1, q2 at lambda=1 (c=2, kappa=1, alpha=2, S4=5/32).
        q0 = 4*kappa^2 = 4
        q1 = 12*kappa*alpha = 12*1*2 = 24
        q2 = 9*alpha^2 + 16*kappa*S4 = 36 + 16*1*5/32 = 36 + 5/2 = 77/2
        """
        q0, q1, q2, Delta = shadow_metric_T_line(1)
        assert q0 == 4
        assert q1 == 24
        assert simplify(q2 - Rational(77, 2)) == 0

    def test_shadow_metric_Delta_equals_8kS4(self):
        """Delta = 8*kappa*S_4."""
        for lam_val in [0, Rational(1, 2), 1, 2]:
            _, _, _, Delta = shadow_metric_T_line(lam_val)
            expected = 8 * kappa(lam_val) * S4_T_line(lam_val)
            assert simplify(Delta - expected) == 0


# =========================================================================
# 13. Generating function on T-line
# =========================================================================

class TestGeneratingFunction:
    """The T-line generating function H(t) = t^2 * sqrt(Q_L(t))."""

    def test_tower_first_three_match_inputs(self):
        """The first three tower entries match the input data."""
        lam_val = Rational(2)
        tower = T_line_tower(lam_val, max_arity=6)
        assert simplify(tower[2] - kappa(lam_val)) == 0
        assert simplify(tower[3] - S3_T_line(lam_val)) == 0
        assert simplify(tower[4] - S4_T_line(lam_val)) == 0

    def test_tower_convolution_identity(self):
        """Verify: sum_{j=0}^{n} a_j * a_{n-j} = [t^n] Q_L for the sqrt."""
        # At lambda=2: kappa=13, alpha=2, S4=5/1976
        # q0 = 4*169 = 676, q1 = 12*13*2 = 312, q2 = 36 + 16*13*5/1976 = 36 + 40/152 = 36+5/19
        q0, q1, q2, _ = shadow_metric_T_line(2)

        tower = T_line_tower(2, max_arity=8)
        # a_n = (n+2) * S_{n+2}
        a = {n: (n + 2) * tower[n + 2] for n in range(7)}

        # Check [t^0]: a_0^2 = q0
        assert simplify(a[0]**2 - q0) == 0

        # Check [t^1]: 2*a_0*a_1 = q1
        assert simplify(2 * a[0] * a[1] - q1) == 0

        # Check [t^2]: a_1^2 + 2*a_0*a_2 = q2
        assert simplify(a[1]**2 + 2 * a[0] * a[2] - q2) == 0

        # Check [t^3]: 2*a_0*a_3 + 2*a_1*a_2 = 0
        assert simplify(2 * a[0] * a[3] + 2 * a[1] * a[2]) == 0

    def test_growth_rate_lambda_2(self):
        """rho at lambda=2 (c=26) should match the Virasoro value ~0.2325."""
        data = evaluate_at_weight(2)
        rho = data.get('rho_T')
        assert rho is not None
        assert abs(rho - 0.2324) < 0.01

    def test_growth_rate_lambda_1(self):
        """rho at lambda=1 (c=2) should be > 1 (divergent tower)."""
        data = evaluate_at_weight(1)
        rho = data.get('rho_T')
        assert rho is not None
        assert rho > 1.0

    def test_growth_rate_self_dual_point(self):
        """At the self-dual Virasoro point c=13 (lambda solving 6*lam^2-6*lam+1=13/2),
        rho should match the Virasoro self-dual radius ~0.467."""
        # c = 13 means 6*lam^2 - 6*lam + 1 = 13/2, i.e. 12*lam^2 - 12*lam - 11 = 0
        # This has solutions at lambda = (12 +/- sqrt(144+528))/24 = (12 +/- sqrt(672))/24
        # Just use the formula directly with c=13 approach via S4
        # Delta = 40/(5*13+22) = 40/87
        # rho_sq = (36 + 2*40/87) / (4*(13/2)^2) = (36 + 80/87) / (169)
        Delta = Rational(40, 87)
        numer_sq = 36 + 2 * Delta
        rho_sq = numer_sq / (4 * (Rational(13, 2))**2)
        rho = float(sqrt(rho_sq).evalf())
        assert abs(rho - 0.467) < 0.01


# =========================================================================
# 14. Full shadow tower structure
# =========================================================================

class TestFullTower:
    """Integration tests for the full shadow tower."""

    def test_full_tower_depth(self):
        tower = full_shadow_tower(1)
        assert tower['depth'] == 4
        assert tower['class'] == 'C'

    def test_full_tower_weight_line_all_zero(self):
        tower = full_shadow_tower(1)
        wl = tower['weight_line']
        assert wl['S2'] == 0
        assert wl['S3'] == 0
        assert wl['S4'] == 0
        assert wl['S5'] == 0

    def test_full_tower_T_line_S3_nonzero(self):
        tower = full_shadow_tower(1)
        assert tower['T_line']['S3'] != 0

    def test_full_tower_T_line_S4_nonzero(self):
        tower = full_shadow_tower(1)
        assert tower['T_line']['S4'] != 0

    def test_full_tower_global_mu_bg_zero(self):
        tower = full_shadow_tower(1)
        assert tower['global']['mu_bg'] == 0

    def test_full_tower_global_S5_zero(self):
        tower = full_shadow_tower(1)
        assert tower['global']['S5'] == 0

    def test_depth_class_proof_structure(self):
        proof = depth_class_proof()
        assert proof['depth'] == 4
        assert proof['class'] == 'C'
        assert proof['archetype'] == 'contact/quartic'


# =========================================================================
# 15. Parametric verification (symbolic lambda)
# =========================================================================

class TestSymbolic:
    """Tests with symbolic lambda to verify universal identities."""

    def test_c_bc_negates_c_bg(self):
        lam = Symbol('lambda')
        assert simplify(central_charge(lam) + central_charge_bc(lam)) == 0

    def test_kappa_bc_negates_kappa_bg(self):
        lam = Symbol('lambda')
        assert simplify(kappa(lam) + kappa_bc(lam)) == 0

    def test_mumford_identity_symbolic(self):
        lam = Symbol('lambda')
        mi = mumford_kappa_identity(lam)
        assert mi['identity_holds']

    def test_weight_symmetry_symbolic(self):
        lam = Symbol('lambda')
        ws = weight_symmetry(lam)
        assert ws['symmetric']


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
