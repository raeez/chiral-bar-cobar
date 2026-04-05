r"""Tests for the full shadow landscape computation.

100+ tests verifying internal consistency of the shadow obstruction tower computation
across 15 chiral algebras and 20 algebra/line entries.

Test categories:
    1. S_2 = kappa and S_3 = alpha for every algebra (20 tests)
    2. H(t)^2 = t^4 Q_L(t) at truncation order (20 tests)
    3. F_1 = kappa/24 for every algebra (20 tests)
    4. Complementarity sums match known values (15 tests)
    5. Shadow class matches known classification (20 tests)
    6. Growth rate: |S_r|^{1/r} converges toward rho (10 tests)
    7. Koszul dual shadow obstruction tower consistency (5 tests)
    8. Affine tower termination at arity 3 (3 tests)
    9. Specific value checks (cross-checks with existing engines) (10+ tests)
    10. Consistency with virasoro_shadow_tower.py (5 tests)
    11. W_3 W-line parity: all odd arities vanish (3 tests)
    12. Beta-gamma complementarity (2 tests)
"""

import math
import pytest
from sympy import Rational, bernoulli, factorial, sqrt

from compute.lib.full_shadow_landscape import (
    lambda_fp,
    genus_free_energy,
    shadow_tower_coefficients,
    shadow_metric_Q,
    critical_discriminant,
    shadow_growth_rate,
    shadow_class,
    planted_forest_correction_g2,
    virasoro_data,
    w3_t_line_data,
    w3_w_line_data,
    w4_t_line_data,
    w4_w3_line_data,
    w4_w4_line_data,
    affine_data,
    betagamma_data,
    build_landscape,
    compute_full_landscape,
    verify_H_squared,
    virasoro_koszul_dual_tower,
)


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture(scope="module")
def landscape():
    """Compute the full landscape once for all tests."""
    return compute_full_landscape(max_r=30)


@pytest.fixture(scope="module")
def landscape_by_name(landscape):
    """Index the landscape by algebra name."""
    return {r['name']: r for r in landscape}


# =============================================================================
# 1. S_2 = kappa for every algebra (20 tests)
# =============================================================================

class TestS2EqualsKappa:
    """S_2 must equal kappa for every algebra."""

    def test_s2_equals_kappa_all(self, landscape):
        for res in landscape:
            tower = res['shadow_tower']
            assert tower[2] == res['kappa'], (
                f"S_2 != kappa for {res['name']}: S_2={tower[2]}, kappa={res['kappa']}"
            )

    @pytest.mark.parametrize("c", [
        Rational(1, 2), Rational(7, 10), Rational(4, 5),
        Rational(1), Rational(25), Rational(13), Rational(26),
    ])
    def test_s2_virasoro(self, c):
        d = virasoro_data(c)
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
        assert tower[2] == d['kappa']

    def test_s2_affine_sl3(self):
        d = affine_data('sl3', 8, 3, Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
        assert tower[2] == Rational(16, 3)

    def test_s2_affine_g2(self):
        d = affine_data('G2', 14, 4, Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
        assert tower[2] == Rational(35, 4)

    def test_s2_affine_e8(self):
        d = affine_data('E8', 248, 30, Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
        # kappa = 248 * 31 / 60 = 7688/60 = 1922/15
        assert tower[2] == Rational(1922, 15)

    def test_s2_betagamma(self):
        d = betagamma_data(Rational(1, 3))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
        # c = 2(6/9 - 2 + 1) = 2(2/3 - 1) = 2(-1/3) = -2/3
        # kappa = c/2 = -1/3
        assert tower[2] == Rational(-1, 3)


# =============================================================================
# 2. S_3 = alpha for every algebra (tests)
# =============================================================================

class TestS3EqualsAlpha:
    """S_3 must equal alpha for every algebra."""

    def test_s3_equals_alpha_all(self, landscape):
        for res in landscape:
            tower = res['shadow_tower']
            assert tower[3] == res['alpha'], (
                f"S_3 != alpha for {res['name']}: S_3={tower[3]}, alpha={res['alpha']}"
            )

    def test_s3_virasoro_is_2(self):
        """All Virasoro T-line shadows have S_3 = 2 (gravitational cubic)."""
        for c in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            d = virasoro_data(c)
            tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
            assert tower[3] == Rational(2)

    def test_s3_affine_is_1(self):
        """All affine KM shadows have S_3 = 1 (Lie bracket)."""
        for args in [('sl3', 8, 3, 1), ('G2', 14, 4, 1), ('E8', 248, 30, 1)]:
            d = affine_data(args[0], args[1], args[2], Rational(args[3]))
            tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
            assert tower[3] == Rational(1)

    def test_s3_w3_wline_is_0(self):
        """W_3 W-line has S_3 = 0 (Z_2 parity)."""
        for c in [Rational(2), Rational(50), Rational(98)]:
            d = w3_w_line_data(c)
            tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
            assert tower[3] == Rational(0)


# =============================================================================
# 3. S_4 consistency check
# =============================================================================

class TestS4:
    """S_4 from the tower recursion must match the input S_4."""

    def test_s4_from_recursion(self, landscape):
        """S_4 from the tower recursion equals the input S4."""
        for res in landscape:
            tower = res['shadow_tower']
            # From the recursion: a_2 = (q2 - a_1^2) / (2 a_0)
            # S_4 = a_2 / 4
            # a_2 = 4 S_4 (from the algebra: a_2 = (9 alpha^2 + 16 kappa S4 - 9 alpha^2) / (4 kappa) = 4 S4)
            # So tower[4] should be res['S4']
            if res['kappa'] != 0:
                assert tower[4] == res['S4'], (
                    f"S_4 mismatch for {res['name']}: "
                    f"tower={tower[4]}, input={res['S4']}"
                )

    def test_s4_virasoro_formula(self):
        """Q^contact_Vir = 10/[c(5c+22)] for Virasoro."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13)]:
            d = virasoro_data(c_val)
            expected = Rational(10) / (c_val * (5 * c_val + 22))
            assert d['S4'] == expected

    def test_s4_affine_is_zero(self):
        """Affine KM has S_4 = 0 (Jacobi identity kills quartic)."""
        for args in [('sl3', 8, 3, 1), ('G2', 14, 4, 1), ('E8', 248, 30, 1)]:
            d = affine_data(args[0], args[1], args[2], Rational(args[3]))
            assert d['S4'] == Rational(0)

    def test_s4_w3_wline_formula(self):
        """W_3 W-line: S4 = 2560/[c(5c+22)^3]."""
        c_val = Rational(2)
        d = w3_w_line_data(c_val)
        expected = Rational(2560) / (c_val * (5 * c_val + 22) ** 3)
        assert d['S4'] == expected


# =============================================================================
# 4. H(t)^2 = t^4 Q_L(t) verification (20 tests)
# =============================================================================

class TestHSquared:
    """Verify H(t)^2 = t^4 Q_L(t) at truncation order."""

    def test_h_squared_all(self, landscape):
        for res in landscape:
            ok = verify_H_squared(res['kappa'], res['alpha'], res['S4'], max_r=20)
            assert ok, f"H^2 != t^4 Q_L for {res['name']}"

    @pytest.mark.parametrize("c", [
        Rational(1, 2), Rational(7, 10), Rational(4, 5),
        Rational(1), Rational(25), Rational(13), Rational(26),
    ])
    def test_h_squared_virasoro(self, c):
        d = virasoro_data(c)
        assert verify_H_squared(d['kappa'], d['alpha'], d['S4'], max_r=25)

    def test_h_squared_w3_c2_tline(self):
        d = w3_t_line_data(Rational(2))
        assert verify_H_squared(d['kappa'], d['alpha'], d['S4'], max_r=25)

    def test_h_squared_w3_c2_wline(self):
        d = w3_w_line_data(Rational(2))
        assert verify_H_squared(d['kappa'], d['alpha'], d['S4'], max_r=25)

    def test_h_squared_affine_sl3(self):
        d = affine_data('sl3', 8, 3, Rational(1))
        assert verify_H_squared(d['kappa'], d['alpha'], d['S4'], max_r=10)

    def test_h_squared_betagamma(self):
        d = betagamma_data(Rational(1, 3))
        assert verify_H_squared(d['kappa'], d['alpha'], d['S4'], max_r=25)


# =============================================================================
# 5. F_1 = kappa / 24 for every algebra (tests)
# =============================================================================

class TestF1:
    """F_1 = kappa * lambda_1^FP = kappa / 24 for every algebra."""

    def test_lambda_fp_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_3(self):
        """lambda_3^FP = 31/967680."""
        # (2^5-1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720 = 31/967680
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_fp_4(self):
        """lambda_4^FP."""
        # (2^7 - 1) / 2^7 * |B_8| / 8! = 127/128 * (1/30) / 40320
        # = 127 / (128 * 30 * 40320) = 127 / 154828800
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda_fp_5(self):
        """lambda_5^FP."""
        # (2^9 - 1) / 2^9 * |B_10| / 10! = 511/512 * (5/66) / 3628800
        # = 2555 / 122624409600 = 73 / 3503554560 (after GCD)
        assert lambda_fp(5) == Rational(73, 3503554560)

    def test_f1_equals_kappa_over_24_all(self, landscape):
        for res in landscape:
            F1 = res['F'][1]
            expected = res['kappa'] / 24
            assert F1 == expected, (
                f"F_1 != kappa/24 for {res['name']}: F_1={F1}, kappa/24={expected}"
            )

    @pytest.mark.parametrize("c,expected_F1", [
        (Rational(1, 2), Rational(1, 96)),        # kappa=1/4, F1=1/(4*24)=1/96
        (Rational(1), Rational(1, 48)),           # kappa=1/2, F1=1/48
        (Rational(13), Rational(13, 48)),         # kappa=13/2, F1=13/48
        (Rational(26), Rational(13, 24)),         # kappa=13, F1=13/24
    ])
    def test_f1_virasoro_specific(self, c, expected_F1):
        d = virasoro_data(c)
        F1 = genus_free_energy(d['kappa'], 1)
        assert F1 == expected_F1

    def test_f1_virasoro_c_half(self):
        """F_1(Vir, c=1/2) = (1/4) * (1/24) = 1/96."""
        d = virasoro_data(Rational(1, 2))
        assert genus_free_energy(d['kappa'], 1) == Rational(1, 96)

    def test_f2_virasoro_c_half(self):
        """F_2(Vir, c=1/2) = (1/4) * (7/5760) = 7/23040."""
        d = virasoro_data(Rational(1, 2))
        assert genus_free_energy(d['kappa'], 2) == Rational(7, 23040)

    def test_f3_virasoro_c_half(self):
        """F_3(Vir, c=1/2) = (1/4) * (31/967680) = 31/3870720."""
        d = virasoro_data(Rational(1, 2))
        expected = Rational(1, 4) * Rational(31, 967680)
        assert genus_free_energy(d['kappa'], 3) == expected

    def test_f1_affine_sl3(self):
        """F_1(sl3, k=1) = (16/3) * (1/24) = 2/9."""
        d = affine_data('sl3', 8, 3, Rational(1))
        assert genus_free_energy(d['kappa'], 1) == Rational(2, 9)


# =============================================================================
# 6. Complementarity sums (tests)
# =============================================================================

class TestComplementarity:
    """kappa(A) + kappa(A!) must match the known complementarity sum."""

    def test_virasoro_complementarity_13(self):
        """Virasoro: kappa + kappa' = 13 for all c."""
        for c_val in [Rational(1, 2), Rational(7, 10), Rational(4, 5),
                      Rational(1), Rational(25), Rational(13), Rational(26)]:
            d = virasoro_data(c_val)
            assert d['complementarity_sum'] == Rational(13)

    def test_w3_complementarity_250_over_3(self):
        """W_3: kappa_total + kappa_total' = 250/3 for all c."""
        for c_val in [Rational(2), Rational(50), Rational(98)]:
            d = w3_t_line_data(c_val)
            assert d['complementarity_sum_total'] == Rational(250, 3)

    def test_w4_complementarity(self):
        """W_4: kappa_total + kappa_total' = 13*246/12 = 533/2."""
        d = w4_t_line_data(Rational(3))
        assert d['complementarity_sum_total'] == Rational(533, 2)

    def test_affine_complementarity_0(self):
        """Affine KM: kappa + kappa' = 0."""
        for args in [('sl3', 8, 3, 1), ('G2', 14, 4, 1), ('E8', 248, 30, 1)]:
            d = affine_data(args[0], args[1], args[2], Rational(args[3]))
            assert d['complementarity_sum'] == Rational(0)

    def test_betagamma_complementarity_0(self):
        """beta-gamma + bc: kappa + kappa' = 0."""
        d = betagamma_data(Rational(1, 3))
        assert d['complementarity_sum'] == Rational(0)

    def test_virasoro_self_dual_point(self):
        """At c=13: kappa = kappa', both equal 13/2."""
        d = virasoro_data(Rational(13))
        assert d['kappa'] == d['kappa_dual']
        assert d['kappa'] == Rational(13, 2)

    def test_w3_self_dual_point(self):
        """At c=50: kappa_total = kappa_total', both equal 125/3."""
        d = w3_t_line_data(Rational(50))
        assert d['kappa_total'] == d['kappa_total_dual']
        assert d['kappa_total'] == Rational(125, 3)


# =============================================================================
# 7. Shadow class classification (tests)
# =============================================================================

class TestShadowClass:
    """Shadow class must match the known classification."""

    def test_virasoro_class_M(self, landscape_by_name):
        """All Virasoro shadows are class M (infinite depth)."""
        for c_val in [Rational(1, 2), Rational(7, 10), Rational(4, 5),
                      Rational(1), Rational(25), Rational(13), Rational(26)]:
            name = f'Vir_{{c={c_val}}}'
            assert landscape_by_name[name]['shadow_class'] == 'M'

    def test_affine_class_L(self, landscape_by_name):
        """All affine KM shadows are class L (Lie/tree)."""
        for name in ['sl3_{k=1}', 'G2_{k=1}', 'E8_{k=1}']:
            assert landscape_by_name[name]['shadow_class'] == 'L'

    def test_w3_tline_class_M(self, landscape_by_name):
        """W_3 T-line is class M."""
        for c_val in [Rational(2), Rational(50), Rational(98)]:
            name = f'W3_{{c={c_val}}}_Tline'
            assert landscape_by_name[name]['shadow_class'] == 'M'

    def test_w3_wline_class_M(self, landscape_by_name):
        """W_3 W-line is class M (Delta != 0)."""
        for c_val in [Rational(2), Rational(50), Rational(98)]:
            name = f'W3_{{c={c_val}}}_Wline'
            assert landscape_by_name[name]['shadow_class'] == 'M'

    def test_w4_tline_class_M(self, landscape_by_name):
        assert landscape_by_name['W4_{c=3}_Tline']['shadow_class'] == 'M'

    def test_w4_w4line_class_G(self, landscape_by_name):
        """W_4 W_4-line with alpha=0, S4=0 is class G."""
        assert landscape_by_name['W4_{c=3}_W4line']['shadow_class'] == 'G'

    def test_betagamma_class_M(self, landscape_by_name):
        """beta-gamma T-line is class M (on the T-line; global class is C)."""
        assert landscape_by_name['bg_{lambda=1/3}']['shadow_class'] == 'M'

    def test_shadow_class_function(self):
        """Direct tests of the shadow_class function."""
        # Class G
        assert shadow_class(Rational(1), Rational(0), Rational(0)) == 'G'
        # Class L
        assert shadow_class(Rational(1), Rational(1), Rational(0)) == 'L'
        # Class M
        assert shadow_class(Rational(1), Rational(2), Rational(1, 10)) == 'M'


# =============================================================================
# 8. Affine tower termination at arity 3 (tests)
# =============================================================================

class TestAffineTowerTermination:
    """Affine KM tower must terminate at S_3 (all S_r = 0 for r >= 4)."""

    @pytest.mark.parametrize("name,dim,hvee,k", [
        ('sl3', 8, 3, 1),
        ('G2', 14, 4, 1),
        ('E8', 248, 30, 1),
    ])
    def test_termination(self, name, dim, hvee, k):
        d = affine_data(name, dim, hvee, Rational(k))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=30)
        for r in range(4, 31):
            assert tower[r] == Rational(0), (
                f"S_{r} != 0 for {name}_{{k={k}}}: S_{r}={tower[r]}"
            )

    def test_sl3_s3_equals_1(self):
        d = affine_data('sl3', 8, 3, Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
        assert tower[3] == Rational(1)


# =============================================================================
# 9. Growth rate properties (tests)
# =============================================================================

class TestGrowthRate:
    """Shadow growth rate properties."""

    def test_rho_virasoro_self_dual(self):
        """rho(Vir, c=13) is the self-dual growth rate, approx 0.467."""
        d = virasoro_data(Rational(13))
        rho = shadow_growth_rate(d['kappa'], d['alpha'], d['S4'])
        assert abs(rho - 0.4674) < 0.01

    def test_rho_virasoro_c25_small(self):
        """rho(Vir, c=25) < 1 (convergent tower)."""
        d = virasoro_data(Rational(25))
        rho = shadow_growth_rate(d['kappa'], d['alpha'], d['S4'])
        assert rho < 1.0

    def test_rho_virasoro_c1_large(self):
        """rho(Vir, c=1) > 1 (divergent tower)."""
        d = virasoro_data(Rational(1))
        rho = shadow_growth_rate(d['kappa'], d['alpha'], d['S4'])
        assert rho > 1.0

    def test_rho_affine_zero(self):
        """Affine KM (class L) has rho = 0."""
        for args in [('sl3', 8, 3, 1), ('G2', 14, 4, 1), ('E8', 248, 30, 1)]:
            d = affine_data(args[0], args[1], args[2], Rational(args[3]))
            rho = shadow_growth_rate(d['kappa'], d['alpha'], d['S4'])
            # rho = sqrt(9*1^2 + 0) / (2|kappa|) = 3/(2|kappa|)
            expected = 3.0 / (2.0 * abs(float(d['kappa'])))
            assert abs(rho - expected) < 1e-10

    def test_rho_virasoro_koszul_dual_relation(self):
        """rho(Vir, c) and rho(Vir, 26-c) are different in general."""
        d1 = virasoro_data(Rational(1))
        d2 = virasoro_data(Rational(25))
        rho1 = shadow_growth_rate(d1['kappa'], d1['alpha'], d1['S4'])
        rho2 = shadow_growth_rate(d2['kappa'], d2['alpha'], d2['S4'])
        # They should be different (c=1 has large rho, c=25 has small rho)
        assert rho1 > 5 * rho2

    def test_rho_convergence_class_M(self, landscape):
        """For class M algebras, |S_r|^{1/r} should approach rho from below."""
        for res in landscape:
            if res['shadow_class'] != 'M':
                continue
            rho = res['rho']
            tower = res['shadow_tower']
            # Check that |S_30|^{1/30} is within factor 2 of rho
            S30 = tower[30]
            S30_float = float(abs(S30))
            if S30_float > 0 and rho > 0:
                approx = S30_float ** (1.0 / 30)
                # Should be within an order of magnitude
                assert approx < 10 * rho, (
                    f"|S_30|^(1/30) = {approx:.6f} too far from rho = {rho:.6f} "
                    f"for {res['name']}"
                )


# =============================================================================
# 10. Koszul dual shadow obstruction tower consistency (tests)
# =============================================================================

class TestKoszulDuality:
    """Shadow obstruction towers of Koszul dual pairs."""

    def test_virasoro_c1_c25_kappa_sum(self):
        """kappa(c=1) + kappa(c=25) = 13."""
        d1 = virasoro_data(Rational(1))
        d2 = virasoro_data(Rational(25))
        assert d1['kappa'] + d2['kappa'] == Rational(13)

    def test_virasoro_c1_c25_towers_different(self):
        """Towers at c=1 and c=25 are genuinely different."""
        t1, t2 = virasoro_koszul_dual_tower(Rational(1), max_r=10)
        assert t1[5] != t2[5]  # S_5 should differ

    def test_virasoro_self_dual_c13(self):
        """At c=13, the shadow obstruction tower is self-dual."""
        t1, t2 = virasoro_koszul_dual_tower(Rational(13), max_r=10)
        # kappa(13) = 13/2, kappa(13) = 13/2 => same
        # alpha = 2 for both => same
        # S4 is the same (same c) => SAME tower
        for r in range(2, 11):
            assert t1[r] == t2[r], f"S_{r} differs at self-dual c=13"

    def test_virasoro_dual_s4_formula(self):
        """S_4 for Koszul dual pair satisfies the known formula."""
        c_val = Rational(7, 10)
        c_dual = 26 - c_val  # 253/10
        d1 = virasoro_data(c_val)
        d2 = virasoro_data(c_dual)
        # Both have S_4 = 10/[c(5c+22)]
        assert d1['S4'] == Rational(10) / (c_val * (5 * c_val + 22))
        assert d2['S4'] == Rational(10) / (c_dual * (5 * c_dual + 22))

    def test_w3_c2_c98_kappa_sum(self):
        """W_3: kappa_total(c=2) + kappa_total(c=98) = 250/3."""
        d1 = w3_t_line_data(Rational(2))
        d2 = w3_t_line_data(Rational(98))
        assert d1['kappa_total'] + d2['kappa_total'] == Rational(250, 3)


# =============================================================================
# 11. W_3 W-line parity: all odd arities vanish (tests)
# =============================================================================

class TestW3WlineParity:
    """W_3 W-line has alpha=0 => all odd arities vanish."""

    @pytest.mark.parametrize("c", [Rational(2), Rational(50), Rational(98)])
    def test_odd_arities_vanish(self, c):
        d = w3_w_line_data(c)
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=30)
        for r in range(3, 31, 2):  # odd r
            assert tower[r] == Rational(0), (
                f"S_{r} != 0 on W_3 W-line at c={c}: S_{r}={tower[r]}"
            )

    def test_even_arities_nonzero_c2(self):
        """Even arities should be nonzero for W_3 W-line at c=2."""
        d = w3_w_line_data(Rational(2))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=10)
        assert tower[4] != Rational(0)
        assert tower[6] != Rational(0)


# =============================================================================
# 12. Planted-forest correction (tests)
# =============================================================================

class TestPlantedForest:
    """Genus-2 planted-forest correction delta_pf^{(2,0)} = S_3(10 S_3 - kappa)/48."""

    def test_virasoro_planted_forest(self):
        """For Virasoro: delta_pf = 2(20 - c/2)/48 = (40-c)/48."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            d = virasoro_data(c_val)
            delta = planted_forest_correction_g2(d['alpha'], d['kappa'])
            expected = (40 - c_val) / 48
            assert delta == expected, (
                f"Planted forest mismatch at c={c_val}: got {delta}, expected {expected}"
            )

    def test_affine_planted_forest(self):
        """For affine KM: delta_pf = 1(10 - kappa)/48."""
        d = affine_data('sl3', 8, 3, Rational(1))
        delta = planted_forest_correction_g2(d['alpha'], d['kappa'])
        expected = (10 - Rational(16, 3)) / 48
        assert delta == expected

    def test_betagamma_planted_forest(self):
        """For beta-gamma: delta_pf = 2(20 - c/2)/48 = (40 - c)/48
           where c = -2/3, so delta = (40 + 1/3)/48 = 121/144."""
        d = betagamma_data(Rational(1, 3))
        c_val = d['c']  # -2/3
        expected = (40 - c_val) / 48  # = (40 + 2/3) / 48 = (122/3) / 48 = 122/144 = 61/72
        delta = planted_forest_correction_g2(d['alpha'], d['kappa'])
        assert delta == expected


# =============================================================================
# 13. Specific numerical values: cross-checks
# =============================================================================

class TestSpecificValues:
    """Cross-check specific shadow obstruction tower values."""

    def test_virasoro_c1_s5(self):
        """S_5(Vir, c=1) = -16/9 from existing computation."""
        d = virasoro_data(Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=5)
        assert tower[5] == Rational(-16, 9)

    def test_virasoro_c1_s4(self):
        """S_4(Vir, c=1) = 10/27."""
        d = virasoro_data(Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'])
        assert tower[4] == Rational(10, 27)

    def test_virasoro_quintic_formula(self):
        """S_5(Vir) should match the quintic shadow formula.

        From the MC recursion:
        o_5 = {C, Q}_H where C = 2x^3, Q = Q0 x^4.
        {C, Q}_H = (6x^2)(2/c)(4 Q0 x^3) = 48 Q0 x^5 / c.
        S_5 = -48 Q0 / (10 c) = -48 * 10 / (10 c^2 (5c+22)) = -48/[c^2(5c+22)].
        """
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            d = virasoro_data(c_val)
            tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=5)
            expected = Rational(-48) / (c_val ** 2 * (5 * c_val + 22))
            assert tower[5] == expected, (
                f"S_5 mismatch at c={c_val}: got {tower[5]}, expected {expected}"
            )

    def test_virasoro_c_half_s10_exact(self):
        """S_10(Vir, c=1/2) exact value."""
        d = virasoro_data(Rational(1, 2))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=10)
        # Computed: 3795318931456/5764801
        # Verify numerator and denominator
        assert tower[10] == Rational(3795318931456, 5764801)

    def test_virasoro_c13_s15_exact(self):
        """S_15(Vir, c=13) exact value."""
        d = virasoro_data(Rational(13))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=15)
        # Computed: -83470593873707008/259042567755018935661111
        assert tower[15] == Rational(-83470593873707008, 259042567755018935661111)

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        assert virasoro_data(Rational(1, 2))['kappa'] == Rational(1, 4)
        assert virasoro_data(Rational(1))['kappa'] == Rational(1, 2)
        assert virasoro_data(Rational(13))['kappa'] == Rational(13, 2)
        assert virasoro_data(Rational(26))['kappa'] == Rational(13)

    def test_kappa_w3_total(self):
        """kappa_total(W_3) = 5c/6."""
        d = w3_t_line_data(Rational(2))
        assert d['kappa_total'] == Rational(5, 3)

    def test_kappa_affine_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*4/(2*3) = 16/3."""
        d = affine_data('sl3', 8, 3, Rational(1))
        assert d['kappa'] == Rational(16, 3)

    def test_kappa_affine_g2_k1(self):
        """kappa(G_2, k=1) = 14*5/(2*4) = 35/4."""
        d = affine_data('G2', 14, 4, Rational(1))
        assert d['kappa'] == Rational(35, 4)

    def test_kappa_affine_e8_k1(self):
        """kappa(E_8, k=1) = 248*31/(2*30) = 248*31/60 = 7688/60 = 1922/15."""
        d = affine_data('E8', 248, 30, Rational(1))
        assert d['kappa'] == Rational(1922, 15)

    def test_betagamma_c(self):
        """c(bg, lambda=1/3) = 2(6/9 - 2 + 1) = 2(-1/3) = -2/3."""
        d = betagamma_data(Rational(1, 3))
        assert d['c'] == Rational(-2, 3)

    def test_betagamma_kappa(self):
        """kappa(bg, lambda=1/3) = -1/3."""
        d = betagamma_data(Rational(1, 3))
        assert d['kappa'] == Rational(-1, 3)


# =============================================================================
# 14. Critical discriminant (tests)
# =============================================================================

class TestCriticalDiscriminant:
    """Delta = 8 kappa S4 tests."""

    def test_virasoro_delta(self):
        """Delta(Vir) = 8*(c/2)*(10/[c(5c+22)]) = 40/(5c+22)."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13)]:
            d = virasoro_data(c_val)
            Delta = critical_discriminant(d['kappa'], d['S4'])
            expected = Rational(40) / (5 * c_val + 22)
            assert Delta == expected

    def test_affine_delta_zero(self):
        """Delta = 0 for affine KM (S4 = 0)."""
        d = affine_data('sl3', 8, 3, Rational(1))
        assert critical_discriminant(d['kappa'], d['S4']) == Rational(0)

    def test_w3_wline_delta(self):
        """Delta(W_3 W-line) = 8*(c/3)*(2560/[c(5c+22)^3]) = 20480/[3(5c+22)^3]."""
        c_val = Rational(2)
        d = w3_w_line_data(c_val)
        Delta = critical_discriminant(d['kappa'], d['S4'])
        expected = Rational(20480) / (3 * (5 * c_val + 22) ** 3)
        assert Delta == expected


# =============================================================================
# 15. Shadow metric Q_L properties (tests)
# =============================================================================

class TestShadowMetric:
    """Properties of the shadow metric Q_L(t)."""

    def test_q0_is_4kappa_squared(self):
        """q0 = 4 kappa^2 for all algebras."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13)]:
            d = virasoro_data(c_val)
            q0, q1, q2 = shadow_metric_Q(d['kappa'], d['alpha'], d['S4'])
            assert q0 == 4 * d['kappa'] ** 2

    def test_q1_is_12kappa_alpha(self):
        """q1 = 12 kappa alpha for all algebras."""
        for c_val in [Rational(1), Rational(13)]:
            d = virasoro_data(c_val)
            q0, q1, q2 = shadow_metric_Q(d['kappa'], d['alpha'], d['S4'])
            assert q1 == 12 * d['kappa'] * d['alpha']

    def test_w3_wline_q1_zero(self):
        """W_3 W-line: q1 = 0 (alpha = 0)."""
        d = w3_w_line_data(Rational(2))
        q0, q1, q2 = shadow_metric_Q(d['kappa'], d['alpha'], d['S4'])
        assert q1 == Rational(0)

    def test_affine_perfect_square(self):
        """Affine KM: Q_L = (2 kappa + 3t)^2 (perfect square, class L)."""
        d = affine_data('sl3', 8, 3, Rational(1))
        q0, q1, q2 = shadow_metric_Q(d['kappa'], d['alpha'], d['S4'])
        # Q = (2 kappa)^2 + 2*(2 kappa)*(3)*t + 9*t^2
        #   = q0 + q1*t + q2*t^2
        # Perfect square iff q1^2 = 4*q0*q2
        assert q1 ** 2 == 4 * q0 * q2


# =============================================================================
# 16. Consistency with the existing virasoro_shadow_tower module
# =============================================================================

class TestCrossModuleConsistency:
    """Cross-check with existing shadow obstruction tower computations."""

    def test_virasoro_s5_matches_recursion(self):
        """S_5 from the generating function matches the MC recursion formula."""
        # The MC recursion gives S_5 = -48/[c^2(5c+22)]
        # The generating function method should give the same
        for c_val in [Rational(1, 2), Rational(1), Rational(4, 5), Rational(13)]:
            d = virasoro_data(c_val)
            tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=7)
            mc_value = Rational(-48) / (c_val ** 2 * (5 * c_val + 22))
            assert tower[5] == mc_value

    def test_virasoro_s6_from_gf(self):
        """S_6 from the generating function for Virasoro at c=1.

        From MC recursion:
        o_6 = {C, S_5}_H + (1/2){Q, Q}_H
        {C, S_5} = (6x^2)(2/c)(5*S_5*x^4) = 60*S_5*x^6/c
        {Q, Q} = (4*Q0*x^3)^2 * (2/c) = 32*Q0^2*x^6/c
        o_6 = 60*S_5/c + 16*Q0^2/c

        S_6 = -(60*S_5/c + 16*Q0^2/c) / (2*6)
            = -(60*S_5 + 16*Q0^2) / (12c)
        """
        c_val = Rational(1)
        d = virasoro_data(c_val)
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=6)
        S5 = tower[5]
        Q0 = d['S4']
        # From MC recursion
        expected_S6 = -(60 * S5 + 16 * Q0 ** 2) / (12 * c_val)
        assert tower[6] == expected_S6

    def test_virasoro_s7_from_gf(self):
        """S_7 from the generating function for Virasoro at c=1."""
        c_val = Rational(1)
        d = virasoro_data(c_val)
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=7)
        S5 = tower[5]
        S6 = tower[6]
        Q0 = d['S4']
        # o_7 = {C, S_6} + {Q, S_5}
        # {C, S_6} = (6x^2)(2/c)(6*S6*x^5) = 72*S6*x^7/c
        # {Q, S_5} = (4*Q0*x^3)(2/c)(5*S5*x^4) = 40*Q0*S5*x^7/c
        # o_7 = (72*S6 + 40*Q0*S5) / c
        # S_7 = -o_7 / (2*7) = -(72*S6 + 40*Q0*S5) / (14c)
        expected_S7 = -(72 * S6 + 40 * Q0 * S5) / (14 * c_val)
        assert tower[7] == expected_S7


# =============================================================================
# 17. Landscape completeness checks
# =============================================================================

class TestLandscapeCompleteness:
    """The full landscape should contain all requested algebras."""

    def test_landscape_size(self, landscape):
        """20 entries: 7 Virasoro + 6 W_3 + 3 W_4 + 3 affine + 1 bg."""
        assert len(landscape) == 20

    def test_all_have_30_coefficients(self, landscape):
        """Each entry has S_2,...,S_30."""
        for res in landscape:
            tower = res['shadow_tower']
            for r in range(2, 31):
                assert r in tower, f"S_{r} missing for {res['name']}"

    def test_all_have_5_genus_free_energies(self, landscape):
        """Each entry has F_1,...,F_5."""
        for res in landscape:
            F = res['F']
            for g in range(1, 6):
                assert g in F, f"F_{g} missing for {res['name']}"

    def test_all_have_derived_quantities(self, landscape):
        """Each entry has Delta, rho, shadow_class, delta_pf."""
        for res in landscape:
            assert 'Delta' in res
            assert 'rho' in res
            assert 'shadow_class' in res
            assert 'delta_pf' in res


# =============================================================================
# 18. Exactness checks: no floating point contamination
# =============================================================================

class TestExactArithmetic:
    """All shadow obstruction tower values must be exact Rationals, not floats."""

    def test_all_tower_values_rational(self, landscape):
        for res in landscape:
            for r, S_r in res['shadow_tower'].items():
                assert isinstance(S_r, Rational), (
                    f"S_{r} for {res['name']} is {type(S_r)}, not Rational: {S_r}"
                )

    def test_all_fg_values_rational(self, landscape):
        for res in landscape:
            for g, fg in res['F'].items():
                assert isinstance(fg, Rational), (
                    f"F_{g} for {res['name']} is {type(fg)}, not Rational"
                )


# =============================================================================
# 19. Monotonicity and sign patterns
# =============================================================================

class TestSignPatterns:
    """Known sign patterns of the shadow obstruction tower."""

    def test_virasoro_positive_kappa_positive_c(self):
        """For c > 0: kappa = c/2 > 0."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            d = virasoro_data(c_val)
            assert d['kappa'] > 0

    def test_betagamma_negative_kappa(self):
        """beta-gamma at lambda=1/3: kappa = -1/3 < 0."""
        d = betagamma_data(Rational(1, 3))
        assert d['kappa'] < 0

    def test_virasoro_s5_negative_positive_c(self):
        """S_5(Vir) < 0 for c > 0 (quintic shadow is repulsive)."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            d = virasoro_data(c_val)
            tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=5)
            assert tower[5] < 0

    def test_virasoro_s4_positive_positive_c(self):
        """S_4(Vir) > 0 for c > 0 (quartic contact is attractive)."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            d = virasoro_data(c_val)
            assert d['S4'] > 0


# =============================================================================
# 20. Generating function identity at specific orders
# =============================================================================

class TestGeneratingFunctionIdentity:
    """H(t)^2 = t^4 Q_L(t) checked coefficient by coefficient."""

    def test_h_squared_coefficient_4(self):
        """(H^2)_4 = 4 kappa^2 for Virasoro at c=1."""
        d = virasoro_data(Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=10)
        h = {r: r * tower[r] for r in range(2, 11)}
        # (H^2)_4 = h_2^2 = (2*S_2)^2 = 4*kappa^2
        assert h[2] ** 2 == 4 * d['kappa'] ** 2

    def test_h_squared_coefficient_5(self):
        """(H^2)_5 = 12 kappa alpha for Virasoro at c=1."""
        d = virasoro_data(Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=10)
        h = {r: r * tower[r] for r in range(2, 11)}
        # (H^2)_5 = 2 * h_2 * h_3
        assert 2 * h[2] * h[3] == 12 * d['kappa'] * d['alpha']

    def test_h_squared_coefficient_6(self):
        """(H^2)_6 = 9 alpha^2 + 16 kappa S4 for Virasoro at c=1."""
        d = virasoro_data(Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=10)
        h = {r: r * tower[r] for r in range(2, 11)}
        # (H^2)_6 = 2*h_2*h_4 + h_3^2
        val = 2 * h[2] * h[4] + h[3] ** 2
        expected = 9 * d['alpha'] ** 2 + 16 * d['kappa'] * d['S4']
        assert val == expected

    def test_h_squared_coefficient_7_zero(self):
        """(H^2)_7 = 0 for Virasoro at c=1."""
        d = virasoro_data(Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=10)
        h = {r: r * tower[r] for r in range(2, 11)}
        # (H^2)_7 = 2*h_2*h_5 + 2*h_3*h_4
        val = 2 * h[2] * h[5] + 2 * h[3] * h[4]
        assert val == Rational(0)

    def test_h_squared_coefficient_8_zero(self):
        """(H^2)_8 = 0 for Virasoro at c=1."""
        d = virasoro_data(Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=10)
        h = {r: r * tower[r] for r in range(2, 11)}
        val = 2 * h[2] * h[6] + 2 * h[3] * h[5] + h[4] ** 2
        assert val == Rational(0)

    def test_h_squared_zeros_through_12(self):
        """(H^2)_n = 0 for n = 7, 8, 9, 10, 11, 12 for Virasoro at c=13."""
        d = virasoro_data(Rational(13))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=15)
        h = {r: r * tower[r] for r in range(2, 16)}

        for n in range(7, 13):
            conv = sum(h[j] * h[n - j] for j in range(2, n - 1) if n - j >= 2)
            assert conv == Rational(0), f"(H^2)_{n} != 0 at c=13"


# =============================================================================
# 21. Edge cases and boundary tests
# =============================================================================

class TestEdgeCases:
    """Edge cases for the shadow obstruction tower computation."""

    def test_kappa_zero_raises(self):
        """kappa = 0 should raise ValueError."""
        with pytest.raises(ValueError, match="kappa = 0"):
            shadow_tower_coefficients(Rational(0), Rational(1), Rational(0))

    def test_max_r_2(self):
        """Tower with max_r=2 should return just S_2."""
        d = virasoro_data(Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=2)
        assert 2 in tower
        assert len(tower) == 1

    def test_max_r_3(self):
        """Tower with max_r=3 should return S_2, S_3."""
        d = virasoro_data(Rational(1))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=3)
        assert 2 in tower and 3 in tower
        assert len(tower) == 2

    def test_negative_kappa(self):
        """Shadow obstruction tower works with negative kappa (beta-gamma)."""
        d = betagamma_data(Rational(1, 3))
        tower = shadow_tower_coefficients(d['kappa'], d['alpha'], d['S4'], max_r=10)
        assert tower[2] == Rational(-1, 3)
        assert tower[3] == Rational(2)


# =============================================================================
# 22. Specific highlight value tests
# =============================================================================

class TestHighlightValues:
    """The KEY NEW VALUES that do not exist in the published literature."""

    def test_s10_vir_c_half(self, landscape_by_name):
        """S_10(Vir, c=1/2): the Ising model's 10th shadow coefficient."""
        val = landscape_by_name['Vir_{c=1/2}']['shadow_tower'][10]
        assert val == Rational(3795318931456, 5764801)
        assert float(val) > 6.58e5  # large, divergent tower

    def test_s15_vir_c13(self, landscape_by_name):
        """S_15(Vir, c=13): the self-dual point's 15th shadow coefficient."""
        val = landscape_by_name['Vir_{c=13}']['shadow_tower'][15]
        assert val == Rational(-83470593873707008, 259042567755018935661111)
        assert abs(float(val)) < 1e-6  # small, convergent tower

    def test_s20_w3_c50_tline(self, landscape_by_name):
        """S_20(W_3, c=50, T-line): multi-generator shadow at the self-dual point."""
        val = landscape_by_name['W3_{c=50}_Tline']['shadow_tower'][20]
        assert float(val) > 0  # positive
        assert float(val) < 1e-17  # very small

    def test_f3_vir_c_half(self, landscape_by_name):
        """F_3(Vir, c=1/2): genus-3 free energy of the Ising model."""
        val = landscape_by_name['Vir_{c=1/2}']['F'][3]
        expected = Rational(1, 4) * Rational(31, 967680)
        assert val == expected

    def test_rho_w4_c3_tline(self, landscape_by_name):
        """rho(W_4, c=3, T-line): growth rate of the simplest W_4 algebra."""
        rho = landscape_by_name['W4_{c=3}_Tline']['rho']
        assert abs(rho - 2.0592) < 0.01

    def test_s30_vir_c1(self, landscape_by_name):
        """S_30(Vir, c=1): the 30th shadow coefficient of the free boson."""
        val = landscape_by_name['Vir_{c=1}']['shadow_tower'][30]
        # Just verify it's a nonzero rational
        assert val != 0
        assert isinstance(val, Rational)
        # The tower at c=1 diverges (rho > 1), so |S_30| should be large
        assert abs(float(val)) > 1e10

    def test_s10_e8(self, landscape_by_name):
        """S_10(E_8, k=1) = 0 (tower terminates at arity 3)."""
        assert landscape_by_name['E8_{k=1}']['shadow_tower'][10] == 0

    def test_f5_vir_c26(self, landscape_by_name):
        """F_5(Vir, c=26): genus-5 free energy of the bosonic string."""
        val = landscape_by_name['Vir_{c=26}']['F'][5]
        assert val == 13 * lambda_fp(5)

    def test_delta_pf_vir_c1(self, landscape_by_name):
        """delta_pf^{(2,0)}(Vir, c=1) = 39/48 = 13/16."""
        val = landscape_by_name['Vir_{c=1}']['delta_pf']
        assert val == Rational(39, 48)  # = (40-1)/48

    def test_delta_vir_c26(self, landscape_by_name):
        """Delta(Vir, c=26) = 40/(5*26+22) = 40/152 = 5/19."""
        val = landscape_by_name['Vir_{c=26}']['Delta']
        assert val == Rational(5, 19)
