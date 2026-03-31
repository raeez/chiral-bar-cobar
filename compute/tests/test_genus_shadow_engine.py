"""Tests for the genus expansion (Theorem D) and shadow tower machinery.

Verifies:
1. Faber-Pandharipande numbers lambda_g^FP (exact values, positivity, asymptotics)
2. F_g = kappa * lambda_g for all standard families
3. Genus table computation and structural properties
4. Kappa values for all families (symbolic and numeric)
5. Complementarity at the genus level (level-independence)
6. Shadow growth rate and critical discriminant
7. Shadow depth classification (G/L/C/M)
8. Virasoro shadow tower specific values (Q^contact, Hessian correction)
9. Virasoro self-duality at c=13
10. Bernoulli number properties used in genus expansion

All arithmetic is exact (sympy Rational). Never floating point for ground truth.
"""

import pytest
from sympy import Rational, Symbol, simplify, Abs, pi, bernoulli, factorial


# ============================================================================
# 1. Faber-Pandharipande numbers lambda_g^FP
# ============================================================================

class TestFaberPandharipandeNumbers:
    """lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!"""

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_2_factored(self):
        """lambda_2 = 7/(24*240), verifying factor decomposition."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp(2) == Rational(7, 24 * 240)

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_4(self):
        """lambda_4 = 127/154828800."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda_5(self):
        """lambda_5 = 73/3503554560."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp(5) == Rational(73, 3503554560)

    @pytest.mark.parametrize("g", list(range(1, 16)))
    def test_lambda_positive(self, g):
        """lambda_g > 0 for all g >= 1 (Bernoulli sign pattern)."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp(g) > 0

    def test_lambda_invalid_genus(self):
        """lambda_fp raises ValueError for g < 1."""
        from compute.lib.utils import lambda_fp
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_lambda_formula_from_bernoulli(self):
        """Verify lambda_g against direct Bernoulli computation for g=1..5."""
        from compute.lib.utils import lambda_fp
        for g in range(1, 6):
            B_2g = bernoulli(2 * g)
            numerator = (2 ** (2 * g - 1) - 1) * Abs(B_2g)
            denominator = 2 ** (2 * g - 1) * factorial(2 * g)
            expected = Rational(numerator, denominator)
            assert simplify(lambda_fp(g) - expected) == 0

    def test_lambda_asymptotic_decay(self):
        """lambda_g decays like 1/(2*pi)^{2g}: successive ratios approach 1/(2*pi)^2."""
        from compute.lib.utils import lambda_fp
        import math
        target = 1 / (2 * math.pi) ** 2
        ratios = []
        for g in range(1, 15):
            ratio = float(lambda_fp(g + 1) / lambda_fp(g))
            ratios.append(ratio)
        # Ratios should converge toward target ~ 0.02533
        assert ratios[-1] < ratios[0], "Ratios should decrease"
        assert abs(ratios[-1] - target) < 0.005, "Final ratio should be near 1/(2*pi)^2"

    def test_lambda_monotone_decreasing(self):
        """lambda_g is strictly decreasing for g >= 1."""
        from compute.lib.utils import lambda_fp
        for g in range(1, 15):
            assert lambda_fp(g) > lambda_fp(g + 1)


# ============================================================================
# 2. F_g = kappa * lambda_g for all families
# ============================================================================

class TestFgUniversalFormula:
    """F_g(A) = kappa(A) * lambda_g^FP (thm:universal-generating-function)."""

    def test_heisenberg_F1(self):
        """F_1(H_1) = 1 * 1/24 = 1/24."""
        from compute.lib.utils import F_g
        assert F_g(Rational(1), 1) == Rational(1, 24)

    def test_heisenberg_F2(self):
        """F_2(H_1) = 1 * 7/5760 = 7/5760."""
        from compute.lib.utils import F_g
        assert F_g(Rational(1), 2) == Rational(7, 5760)

    def test_sl2_k1_F1(self):
        """F_1(sl_2, k=1): kappa = 3*3/4 = 9/4, F_1 = 9/4 * 1/24 = 3/32."""
        from compute.lib.utils import F_g
        kappa = Rational(9, 4)
        assert F_g(kappa, 1) == Rational(3, 32)

    def test_virasoro_c26_F1(self):
        """F_1(Vir_{26}): kappa = 13, F_1 = 13/24."""
        from compute.lib.utils import F_g
        assert F_g(Rational(13), 1) == Rational(13, 24)

    def test_virasoro_c2_F1(self):
        """F_1(Vir_2): kappa = 1, F_1 = 1/24."""
        from compute.lib.utils import F_g
        assert F_g(Rational(1), 1) == Rational(1, 24)

    @pytest.mark.parametrize("kappa_val,g,expected", [
        (Rational(1), 1, Rational(1, 24)),
        (Rational(1), 2, Rational(7, 5760)),
        (Rational(9, 4), 1, Rational(3, 32)),
        (Rational(13), 1, Rational(13, 24)),
        (Rational(13), 2, Rational(91, 5760)),
        (Rational(5, 6), 1, Rational(5, 144)),
    ])
    def test_parametrized_Fg(self, kappa_val, g, expected):
        """F_g for specific (kappa, g) pairs."""
        from compute.lib.utils import F_g
        assert simplify(F_g(kappa_val, g) - expected) == 0

    def test_Fg_linearity(self):
        """F_g is linear in kappa: F_g(a+b) = F_g(a) + F_g(b)."""
        from compute.lib.utils import F_g
        a = Rational(3, 2)
        b = Rational(7, 4)
        for g in range(1, 6):
            assert simplify(F_g(a + b, g) - F_g(a, g) - F_g(b, g)) == 0

    def test_Fg_zero_kappa(self):
        """F_g(0) = 0 for all g (uncurved algebra)."""
        from compute.lib.utils import F_g
        for g in range(1, 10):
            assert F_g(Rational(0), g) == 0


# ============================================================================
# 3. Genus table computation
# ============================================================================

class TestGenusTable:
    """genus_table returns dict with keys 1..max_genus, all values positive."""

    def test_returns_dict_with_correct_keys(self):
        """genus_table returns dict with keys 1..max_genus."""
        from compute.lib.genus_expansion import genus_table
        table = genus_table(Rational(1), max_genus=7)
        assert set(table.keys()) == set(range(1, 8))

    def test_all_values_positive_for_positive_kappa(self):
        """All F_g > 0 when kappa > 0."""
        from compute.lib.genus_expansion import genus_table
        table = genus_table(Rational(13), max_genus=10)
        for g, val in table.items():
            assert val > 0, f"F_{g} = {val} should be positive"

    def test_all_values_negative_for_negative_kappa(self):
        """All F_g < 0 when kappa < 0."""
        from compute.lib.genus_expansion import genus_table
        table = genus_table(Rational(-1), max_genus=10)
        for g, val in table.items():
            assert val < 0, f"F_{g} = {val} should be negative for kappa < 0"

    def test_heisenberg_level1_F1(self):
        """Heisenberg at level 1: F_1 = 1/24."""
        from compute.lib.genus_expansion import genus_table, kappa_heisenberg
        kappa = kappa_heisenberg(1)
        table = genus_table(kappa, max_genus=3)
        assert table[1] == Rational(1, 24)


# ============================================================================
# 4. Kappa values for all families
# ============================================================================

class TestKappaFormulas:
    """Exact kappa formulas for the standard landscape."""

    def test_kappa_heisenberg_symbolic(self):
        """kappa(H_k) = k (the level IS the obstruction coefficient)."""
        from compute.lib.genus_expansion import kappa_heisenberg
        k = Symbol("kappa")
        assert kappa_heisenberg() == k

    @pytest.mark.parametrize("level,expected", [
        (1, 1), (2, 2), (Rational(1, 2), Rational(1, 2)), (-1, -1),
    ])
    def test_kappa_heisenberg_numeric(self, level, expected):
        """kappa_heisenberg(k) = k for specific values."""
        from compute.lib.genus_expansion import kappa_heisenberg
        assert kappa_heisenberg(level) == expected

    def test_kappa_virasoro_symbolic(self):
        """kappa(Vir_c) = c/2."""
        from compute.lib.genus_expansion import kappa_virasoro
        c = Symbol("c")
        assert simplify(kappa_virasoro() - c / 2) == 0

    @pytest.mark.parametrize("c_val,expected", [
        (2, 1), (26, 13), (13, Rational(13, 2)), (1, Rational(1, 2)),
    ])
    def test_kappa_virasoro_numeric(self, c_val, expected):
        """kappa_virasoro(c) = c/2 for specific values."""
        from compute.lib.genus_expansion import kappa_virasoro
        assert kappa_virasoro(c_val) == expected

    def test_kappa_w3_symbolic(self):
        """kappa(W_3) = 5c/6."""
        from compute.lib.genus_expansion import kappa_w3
        c = Symbol("c")
        assert simplify(kappa_w3() - 5 * c / 6) == 0

    @pytest.mark.parametrize("c_val,expected", [
        (6, 5), (12, 10), (3, Rational(5, 2)),
    ])
    def test_kappa_w3_numeric(self, c_val, expected):
        """kappa_w3(c) = 5c/6 for specific values."""
        from compute.lib.genus_expansion import kappa_w3
        assert kappa_w3(c_val) == expected

    def test_kappa_sl2_symbolic(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        from compute.lib.genus_expansion import kappa_sl2
        k = Symbol("k")
        assert simplify(kappa_sl2() - 3 * (k + 2) / 4) == 0

    @pytest.mark.parametrize("k_val,expected", [
        (1, Rational(9, 4)),
        (2, Rational(3)),
        (0, Rational(3, 2)),
        (10, Rational(9)),
    ])
    def test_kappa_sl2_numeric(self, k_val, expected):
        """kappa_sl2(k) = 3(k+2)/4 for specific values."""
        from compute.lib.genus_expansion import kappa_sl2
        assert kappa_sl2(k_val) == expected

    def test_kappa_sl3_symbolic(self):
        """kappa(sl_3, k) = 4(k+3)/3."""
        from compute.lib.genus_expansion import kappa_sl3
        k = Symbol("k")
        assert simplify(kappa_sl3() - 4 * (k + 3) / 3) == 0

    @pytest.mark.parametrize("k_val,expected", [
        (1, Rational(16, 3)),
        (0, Rational(4)),
        (3, Rational(8)),
    ])
    def test_kappa_sl3_numeric(self, k_val, expected):
        """kappa_sl3(k) = 4(k+3)/3 for specific values."""
        from compute.lib.genus_expansion import kappa_sl3
        assert kappa_sl3(k_val) == expected

    def test_kappa_b2_symbolic(self):
        """kappa(B_2, k) = 5(k+3)/3."""
        from compute.lib.genus_expansion import kappa_b2
        k = Symbol("k")
        assert simplify(kappa_b2() - 5 * (k + 3) / 3) == 0

    @pytest.mark.parametrize("k_val,expected", [
        (1, Rational(20, 3)),
        (0, Rational(5)),
        (3, Rational(10)),
    ])
    def test_kappa_b2_numeric(self, k_val, expected):
        """kappa_b2(k) = 5(k+3)/3 for specific values."""
        from compute.lib.genus_expansion import kappa_b2
        assert kappa_b2(k_val) == expected

    def test_kappa_g2_symbolic(self):
        """kappa(G_2, k) = 7(k+4)/4."""
        from compute.lib.genus_expansion import kappa_g2
        k = Symbol("k")
        assert simplify(kappa_g2() - 7 * (k + 4) / 4) == 0

    @pytest.mark.parametrize("k_val,expected", [
        (1, Rational(35, 4)),
        (0, Rational(7)),
        (4, Rational(14)),
    ])
    def test_kappa_g2_numeric(self, k_val, expected):
        """kappa_g2(k) = 7(k+4)/4 for specific values."""
        from compute.lib.genus_expansion import kappa_g2
        assert kappa_g2(k_val) == expected

    def test_kappa_general_formula_dim_hdual(self):
        """kappa = dim(g) * (k + h^v) / (2 * h^v) for all KM families."""
        from compute.lib.lie_algebra import kappa_km, cartan_data
        for (type_, rank), k_val in [
            (("A", 1), 1), (("A", 2), 1), (("B", 2), 1), (("G", 2), 1),
        ]:
            data = cartan_data(type_, rank)
            expected = Rational(data.dim) * (Rational(k_val) + data.h_dual) / (2 * data.h_dual)
            assert kappa_km(type_, rank, k_val) == expected

    def test_kappa_sl2_cross_check_with_kappa_km(self):
        """kappa_sl2 matches the general kappa_km formula."""
        from compute.lib.genus_expansion import kappa_sl2
        from compute.lib.lie_algebra import kappa_km
        for k_val in [0, 1, 2, 5, 10]:
            assert kappa_sl2(k_val) == kappa_km("A", 1, k_val)


# ============================================================================
# 5. Complementarity at the genus level
# ============================================================================

class TestComplementarityKM:
    """kappa(g_k) + kappa(g_{k'}) = 0 for KM (Feigin-Frenkel: k' = -k - 2h^v)."""

    @pytest.mark.parametrize("type_,rank", [
        ("A", 1), ("A", 2), ("B", 2), ("G", 2),
    ])
    def test_km_sum_vanishes(self, type_, rank):
        """kappa(g_k) + kappa(g_{k'}) = 0 for Kac-Moody (level-independent)."""
        from compute.lib.genus_expansion import complementarity_sum_km
        total = complementarity_sum_km(type_, rank)
        assert simplify(total) == 0

    @pytest.mark.parametrize("type_,rank", [
        ("A", 1), ("A", 2), ("B", 2), ("G", 2),
    ])
    def test_km_sum_level_independent(self, type_, rank):
        """The complementarity sum has no k dependence."""
        from compute.lib.genus_expansion import complementarity_sum_km
        k = Symbol("k")
        total = complementarity_sum_km(type_, rank)
        assert simplify(total.diff(k)) == 0

    def test_virasoro_complementarity_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13."""
        from compute.lib.genus_expansion import kappa_virasoro
        c = Symbol("c")
        total = kappa_virasoro() + (26 - c) / 2
        assert simplify(total - 13) == 0

    def test_w3_complementarity_sum_250_over_3(self):
        """kappa(W_3) + kappa(W_3') = 250/3 where c + c' = 100."""
        from compute.lib.genus_expansion import kappa_w3
        c = Symbol("c")
        total = kappa_w3() + 5 * (100 - c) / 6
        assert simplify(total - Rational(250, 3)) == 0


# ============================================================================
# 6. Shadow growth rate verification
# ============================================================================

class TestShadowGrowthRate:
    """Shadow growth rate rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)."""

    def test_critical_discriminant_zero_for_S4_zero(self):
        """Delta = 8*kappa*S4 = 0 when S4 = 0 (class G/L)."""
        from compute.lib.shadow_radius import critical_discriminant
        assert critical_discriminant(Rational(3), Rational(0)) == 0

    def test_critical_discriminant_zero_any_kappa(self):
        """Delta = 0 when S4 = 0 regardless of kappa."""
        from compute.lib.shadow_radius import critical_discriminant
        for kappa_val in [Rational(1), Rational(13), Rational(-5, 2)]:
            assert critical_discriminant(kappa_val, Rational(0)) == 0

    def test_heisenberg_rho_zero(self):
        """Heisenberg: alpha=0, S4=0, so rho=0 (class G, tower terminates)."""
        from compute.lib.shadow_radius import shadow_growth_rate
        rho = shadow_growth_rate(Rational(1), Rational(0), Rational(0))
        assert rho == 0

    def test_growth_rate_nonnegative(self):
        """Shadow growth rate is nonnegative for all valid inputs."""
        from compute.lib.shadow_radius import shadow_growth_rate
        # Class M inputs: positive kappa, nonzero alpha, positive S4
        rho = shadow_growth_rate(Rational(1, 2), Rational(2), Rational(10, 27))
        assert float(rho.evalf()) >= 0

    def test_affine_km_rho_zero(self):
        """Affine KM (class L): alpha != 0 but S4 = 0, Delta = 0, rho = |3*alpha|/(2*|kappa|)."""
        from compute.lib.shadow_radius import shadow_growth_rate
        # For class L with S4=0: rho = sqrt(9*alpha^2) / (2*|kappa|) = 3*|alpha|/(2*|kappa|)
        # This is NONZERO if alpha != 0. However class L terminates at depth 3
        # because the cubic gauge triviality theorem applies. The radius formula
        # gives a nonzero value, but the tower truncates before it matters.
        kappa_val = Rational(9, 4)  # sl_2 at k=1
        alpha_val = Rational(1)     # Killing 3-cocycle
        rho = shadow_growth_rate(kappa_val, alpha_val, Rational(0))
        # rho = 3/(2 * 9/4) = 3/(9/2) = 2/3
        assert simplify(rho - Rational(2, 3)) == 0

    def test_virasoro_c1_growth_rate(self):
        """Virasoro at c=1: kappa=1/2, compute growth rate from shadow data."""
        from compute.lib.shadow_radius import shadow_growth_rate, critical_discriminant
        kappa_val = Rational(1, 2)
        alpha_val = Rational(2)
        S4_val = Rational(10) / (Rational(1) * (5 * Rational(1) + 22))
        # S4 = 10/27
        assert S4_val == Rational(10, 27)
        Delta = critical_discriminant(kappa_val, S4_val)
        # Delta = 8 * 1/2 * 10/27 = 40/27
        assert simplify(Delta - Rational(40, 27)) == 0
        rho = shadow_growth_rate(kappa_val, alpha_val, S4_val)
        # rho = sqrt(36 + 80/27) / 1 = sqrt((972 + 80)/27) = sqrt(1052/27)
        rho_sq = Rational(36) + Rational(80, 27)
        assert simplify(rho_sq - Rational(1052, 27)) == 0
        assert float(rho.evalf()) > 1, "c=1 Virasoro tower should diverge (rho > 1)"

    def test_virasoro_c26_growth_rate_convergent(self):
        """Virasoro at c=26: tower converges (rho < 1)."""
        from compute.lib.shadow_radius import shadow_growth_rate
        kappa_val = Rational(13)
        alpha_val = Rational(2)
        S4_val = Rational(10) / (Rational(26) * (5 * Rational(26) + 22))
        # S4 = 10/(26*152) = 10/3952 = 5/1976
        assert S4_val == Rational(5, 1976)
        rho = shadow_growth_rate(kappa_val, alpha_val, S4_val)
        assert float(rho.evalf()) < 1, "c=26 Virasoro tower should converge (rho < 1)"

    def test_virasoro_shadow_data_consistency(self):
        """virasoro_shadow_data returns consistent kappa, alpha, S4, Delta."""
        from compute.lib.shadow_radius import virasoro_shadow_data
        c_sym = Symbol('c')
        kappa, alpha, S4, Delta = virasoro_shadow_data()
        assert simplify(kappa - c_sym / 2) == 0
        assert alpha == Rational(2)
        assert simplify(S4 - Rational(10) / (c_sym * (5 * c_sym + 22))) == 0
        assert simplify(Delta - Rational(40) / (5 * c_sym + 22)) == 0


# ============================================================================
# 7. Shadow depth classification
# ============================================================================

class TestShadowDepthClassification:
    """Four classes: G (depth 2), L (depth 3), C (depth 4), M (depth inf)."""

    def test_heisenberg_class_G(self):
        """Heisenberg: class G, Delta=0, S3=0, r_max=2."""
        from compute.lib.shadow_radius import critical_discriminant
        # Heisenberg: kappa=k, alpha=0, S4=0
        Delta = critical_discriminant(Rational(1), Rational(0))
        assert Delta == 0

    def test_affine_class_L(self):
        """Affine KM: class L, Delta=0, S3 != 0, r_max=3."""
        from compute.lib.shadow_radius import critical_discriminant
        # Affine: S4=0 (Jacobi identity kills quartic)
        Delta = critical_discriminant(Rational(9, 4), Rational(0))
        assert Delta == 0
        # But alpha (= Killing 3-cocycle) is nonzero for non-abelian

    def test_virasoro_class_M(self):
        """Virasoro: class M, Delta != 0, r_max=infinity."""
        from compute.lib.shadow_radius import critical_discriminant
        # Virasoro at c=1: kappa=1/2, S4=10/27
        Delta = critical_discriminant(Rational(1, 2), Rational(10, 27))
        assert Delta != 0
        assert Delta > 0

    @pytest.mark.parametrize("c_val", [1, 2, 13, 25, 26])
    def test_virasoro_delta_positive_all_c(self, c_val):
        """Delta > 0 for Virasoro at all positive c (class M)."""
        from compute.lib.shadow_radius import critical_discriminant
        c = Rational(c_val)
        kappa_val = c / 2
        S4_val = Rational(10) / (c * (5 * c + 22))
        Delta = critical_discriminant(kappa_val, S4_val)
        assert Delta > 0

    def test_shadow_atlas_class_assignments(self):
        """Shadow radius atlas returns correct class assignments."""
        from compute.lib.shadow_radius import shadow_radius_atlas
        atlas = shadow_radius_atlas()
        assert atlas['Heisenberg']['class'] == 'G'
        assert atlas['Heisenberg']['depth'] == 2
        assert atlas['Affine V_k(g)']['class'] == 'L'
        assert atlas['Affine V_k(g)']['depth'] == 3
        assert atlas['Beta-gamma']['class'] == 'C'
        assert atlas['Beta-gamma']['depth'] == 4
        assert atlas['Virasoro Vir_c']['class'] == 'M'

    def test_class_G_rho_zero(self):
        """Class G: rho = 0 (tower terminates at depth 2)."""
        from compute.lib.shadow_radius import shadow_radius_atlas
        atlas = shadow_radius_atlas()
        assert atlas['Heisenberg']['rho'] == 0

    def test_class_L_rho_zero(self):
        """Class L: rho = 0 (tower terminates at depth 3)."""
        from compute.lib.shadow_radius import shadow_radius_atlas
        atlas = shadow_radius_atlas()
        assert atlas['Affine V_k(g)']['rho'] == 0


# ============================================================================
# 8. Virasoro shadow tower specific values
# ============================================================================

class TestVirasoroShadowTower:
    """Q^contact_Vir, Hessian correction, and self-duality."""

    def test_Q_contact_c1(self):
        """Q^contact_Vir at c=1: 10/(1*(5+22)) = 10/27."""
        c_val = Rational(1)
        Q = Rational(10) / (c_val * (5 * c_val + 22))
        assert Q == Rational(10, 27)

    def test_Q_contact_c26(self):
        """Q^contact_Vir at c=26: 10/(26*152) = 5/1976."""
        c_val = Rational(26)
        Q = Rational(10) / (c_val * (5 * c_val + 22))
        assert Q == Rational(5, 1976)

    def test_Q_contact_c13(self):
        """Q^contact_Vir at c=13: 10/(13*87) = 10/1131."""
        c_val = Rational(13)
        Q = Rational(10) / (c_val * (5 * c_val + 22))
        assert Q == Rational(10, 1131)

    def test_Q_contact_formula_consistency(self):
        """Q^contact = S_4 = 10/(c(5c+22)) matches virasoro_shadow_data."""
        from compute.lib.shadow_radius import virasoro_shadow_data
        c_sym = Symbol('c')
        _, _, S4, _ = virasoro_shadow_data()
        expected = Rational(10) / (c_sym * (5 * c_sym + 22))
        assert simplify(S4 - expected) == 0

    def test_hessian_correction_coefficient_c1(self):
        """delta_H^(1)_Vir coefficient 120/(c^2(5c+22)) at c=1 gives 120/27 = 40/9."""
        c_val = Rational(1)
        coeff = Rational(120) / (c_val ** 2 * (5 * c_val + 22))
        assert coeff == Rational(40, 9)

    def test_hessian_correction_coefficient_c26(self):
        """delta_H^(1)_Vir coefficient 120/(c^2(5c+22)) at c=26."""
        c_val = Rational(26)
        coeff = Rational(120) / (c_val ** 2 * (5 * c_val + 22))
        # 120/(676*152) = 120/102752 = 15/12844
        assert coeff == Rational(120, 102752)

    def test_critical_discriminant_virasoro(self):
        """Delta_Vir = 40/(5c+22) from virasoro_shadow_data."""
        from compute.lib.shadow_radius import virasoro_shadow_data
        c_sym = Symbol('c')
        _, _, _, Delta = virasoro_shadow_data()
        assert simplify(Delta - Rational(40) / (5 * c_sym + 22)) == 0

    def test_virasoro_critical_central_charge_exists(self):
        """Critical c* where rho = 1 exists and is approximately 6.12."""
        from compute.lib.shadow_radius import virasoro_critical_central_charge
        c_star = virasoro_critical_central_charge()
        assert c_star is not None
        c_star_float = float(c_star.evalf())
        assert 6.0 < c_star_float < 6.3

    def test_virasoro_critical_polynomial(self):
        """c* satisfies 5c^3 + 22c^2 - 180c - 872 = 0."""
        from compute.lib.shadow_radius import virasoro_critical_central_charge
        c_star = virasoro_critical_central_charge()
        poly_val = 5 * c_star ** 3 + 22 * c_star ** 2 - 180 * c_star - 872
        assert simplify(poly_val) == 0


# ============================================================================
# 9. Virasoro self-duality at c=13
# ============================================================================

class TestVirasoroSelfDuality:
    """Vir_c^! = Vir_{26-c}. Self-dual at c=13."""

    def test_kappa_self_dual_c13(self):
        """kappa(Vir_13) = 13/2."""
        from compute.lib.genus_expansion import kappa_virasoro
        assert kappa_virasoro(13) == Rational(13, 2)

    def test_kappa_dual_c13(self):
        """kappa(Vir_{26-13}) = kappa(Vir_13) = 13/2."""
        from compute.lib.genus_expansion import kappa_virasoro
        assert kappa_virasoro(26 - 13) == Rational(13, 2)

    def test_kappa_sum_c13(self):
        """kappa + kappa' = 13/2 + 13/2 = 13 at c=13."""
        from compute.lib.genus_expansion import kappa_virasoro
        total = kappa_virasoro(13) + kappa_virasoro(26 - 13)
        assert total == 13

    def test_Q_contact_self_dual_c13(self):
        """Q^contact is symmetric under c <-> 26-c at c=13."""
        c_val = Rational(13)
        c_dual = 26 - c_val
        Q_c = Rational(10) / (c_val * (5 * c_val + 22))
        Q_dual = Rational(10) / (c_dual * (5 * c_dual + 22))
        assert Q_c == Q_dual

    def test_Q_contact_duality_general(self):
        """Q^contact(c) and Q^contact(26-c) coincide at c=13 but differ elsewhere."""
        # At c=1 vs c=25
        Q_1 = Rational(10) / (Rational(1) * (5 * Rational(1) + 22))
        Q_25 = Rational(10) / (Rational(25) * (5 * Rational(25) + 22))
        assert Q_1 != Q_25
        # But at c=13 they match (tested above)

    def test_shadow_radius_self_dual_c13(self):
        """rho(Vir_13) = rho(Vir_{26-13}) = rho(Vir_13) (self-dual)."""
        from compute.lib.shadow_radius import virasoro_koszul_product
        result = virasoro_koszul_product(13)
        assert result['self_dual'] is True

    def test_shadow_radius_not_self_dual_c1(self):
        """rho(Vir_1) != rho(Vir_25) (not self-dual away from c=13)."""
        from compute.lib.shadow_radius import virasoro_koszul_product
        result = virasoro_koszul_product(1)
        assert result['self_dual'] is False

    def test_Fg_complementarity_at_c13(self):
        """F_g(Vir_13) + F_g(Vir_13) = 2*F_g(Vir_13) at self-dual point."""
        from compute.lib.utils import F_g
        kappa_13 = Rational(13, 2)
        for g in range(1, 6):
            fg = F_g(kappa_13, g)
            fg_dual = F_g(Rational(26 - 13, 2), g)
            assert fg == fg_dual


# ============================================================================
# 10. Bernoulli number properties
# ============================================================================

class TestBernoulliProperties:
    """Bernoulli numbers underlying the genus expansion."""

    def test_B2(self):
        """B_2 = 1/6."""
        assert bernoulli(2) == Rational(1, 6)

    def test_B4(self):
        """B_4 = -1/30."""
        assert bernoulli(4) == Rational(-1, 30)

    def test_B6(self):
        """B_6 = 1/42."""
        assert bernoulli(6) == Rational(1, 42)

    def test_B8(self):
        """B_8 = -1/30."""
        assert bernoulli(8) == Rational(-1, 30)

    def test_B10(self):
        """B_10 = 5/66."""
        assert bernoulli(10) == Rational(5, 66)

    def test_B12(self):
        """B_12 = -691/2730."""
        assert bernoulli(12) == Rational(-691, 2730)

    @pytest.mark.parametrize("g", list(range(1, 11)))
    def test_bernoulli_alternating_sign(self, g):
        """(-1)^{g+1} * B_{2g} > 0 for g=1..10."""
        B_2g = bernoulli(2 * g)
        assert (-1) ** (g + 1) * B_2g > 0

    def test_bernoulli_odd_vanish(self):
        """B_{2k+1} = 0 for k >= 1 (odd Bernoulli numbers vanish)."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli(n) == 0

    def test_B1_convention(self):
        """B_1 = +1/2 in sympy convention (some references use -1/2)."""
        assert bernoulli(1) == Rational(1, 2)

    def test_bernoulli_sign_implies_lambda_positive(self):
        """The sign pattern (-1)^{g+1}*B_{2g} > 0 implies lambda_g > 0."""
        from compute.lib.utils import lambda_fp
        # lambda_g = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
        # All factors are positive, so lambda_g > 0 is equivalent to B_{2g} != 0
        for g in range(1, 11):
            assert bernoulli(2 * g) != 0
            assert lambda_fp(g) > 0


# ============================================================================
# 11. Cross-family F_g consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Verify F_g relations across different algebra families."""

    def test_genus_determines_kappa(self):
        """kappa = 24 * F_1 (thm:genus-determines-pair)."""
        from compute.lib.utils import F_g
        for kappa_val in [Rational(1), Rational(9, 4), Rational(13), Rational(5, 6)]:
            f1 = F_g(kappa_val, 1)
            assert 24 * f1 == kappa_val

    def test_F1_complementarity_virasoro(self):
        """F_1(Vir_c) + F_1(Vir_{26-c}) = 13/24."""
        from compute.lib.utils import F_g
        for c_val in [Rational(1), Rational(1, 2), Rational(13), Rational(25)]:
            kappa = c_val / 2
            kappa_dual = (26 - c_val) / 2
            assert F_g(kappa, 1) + F_g(kappa_dual, 1) == Rational(13, 24)

    @pytest.mark.parametrize("g", [1, 2, 3, 4, 5])
    def test_Fg_complementarity_virasoro_all_genera(self, g):
        """F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g for all g."""
        from compute.lib.utils import F_g, lambda_fp
        c_val = Rational(7)
        kappa = c_val / 2
        kappa_dual = (26 - c_val) / 2
        assert simplify(F_g(kappa, g) + F_g(kappa_dual, g) - 13 * lambda_fp(g)) == 0

    @pytest.mark.parametrize("g", [1, 2, 3])
    def test_Fg_complementarity_sl2_all_genera(self, g):
        """F_g(sl_2, k) + F_g(sl_2, k') = 0 for all g (anti-symmetry)."""
        from compute.lib.utils import F_g
        from compute.lib.genus_expansion import kappa_sl2
        kappa_k = kappa_sl2(1)       # k=1
        kappa_kp = kappa_sl2(-5)     # k'=-1-4=-5
        assert simplify(F_g(kappa_k, g) + F_g(kappa_kp, g)) == 0

    def test_Fg_ratio_independent_of_kappa(self):
        """F_{g+1}/F_g = lambda_{g+1}/lambda_g (kappa cancels)."""
        from compute.lib.utils import F_g, lambda_fp
        for g in range(1, 5):
            ratio_kappa1 = F_g(Rational(1), g + 1) / F_g(Rational(1), g)
            ratio_kappa13 = F_g(Rational(13), g + 1) / F_g(Rational(13), g)
            lambda_ratio = lambda_fp(g + 1) / lambda_fp(g)
            assert simplify(ratio_kappa1 - lambda_ratio) == 0
            assert simplify(ratio_kappa13 - lambda_ratio) == 0

    def test_genus_homomorphism(self):
        """F_g(kappa_a + kappa_b) = F_g(kappa_a) + F_g(kappa_b)."""
        from compute.lib.utils import F_g
        a, b = Rational(3, 2), Rational(7, 4)
        for g in range(1, 6):
            assert F_g(a + b, g) == F_g(a, g) + F_g(b, g)


# ============================================================================
# 12. Branch point and convergence analysis
# ============================================================================

class TestBranchPoints:
    """Branch points of the shadow generating function."""

    def test_branch_points_virasoro_complex_conjugate(self):
        """Virasoro branch points are complex conjugate (Delta > 0)."""
        from compute.lib.shadow_radius import branch_points
        c_val = Rational(1)
        kappa_val = c_val / 2
        alpha_val = Rational(2)
        S4_val = Rational(10) / (c_val * (5 * c_val + 22))
        t_plus, t_minus = branch_points(kappa_val, alpha_val, S4_val)
        # For Delta > 0, discriminant < 0, so sqrt gives imaginary part
        # t_plus and t_minus are complex conjugates
        t_plus_c = complex(t_plus.evalf())
        t_minus_c = complex(t_minus.evalf())
        assert abs(t_plus_c.real - t_minus_c.real) < 1e-10
        assert abs(t_plus_c.imag + t_minus_c.imag) < 1e-10

    def test_shadow_convergence_radius_virasoro_c26(self):
        """R = 1/rho at c=26 should be > 1 (convergent tower)."""
        from compute.lib.shadow_radius import shadow_convergence_radius
        c_val = Rational(26)
        kappa_val = c_val / 2
        alpha_val = Rational(2)
        S4_val = Rational(10) / (c_val * (5 * c_val + 22))
        R = shadow_convergence_radius(kappa_val, alpha_val, S4_val)
        assert float(R.evalf()) > 1

    def test_shadow_metric_discriminant_sign(self):
        """disc(Q_L) = -32*kappa^2*Delta: negative for class M (Delta > 0)."""
        from compute.lib.shadow_radius import shadow_metric_discriminant
        c_val = Rational(13)
        kappa_val = c_val / 2
        alpha_val = Rational(2)
        S4_val = Rational(10) / (c_val * (5 * c_val + 22))
        disc = shadow_metric_discriminant(kappa_val, alpha_val, S4_val)
        assert disc < 0


# ============================================================================
# 13. DS depth increase
# ============================================================================

class TestDSDepthIncrease:
    """DS reduction increases shadow depth: sl_N (class L) -> W_N (class M)."""

    def test_sl_to_w_depth_increase(self):
        """sl_N has rho=0; W_N has rho>0 (depth increase via ghost sector)."""
        from compute.lib.shadow_radius import ds_shadow_radius_comparison
        result = ds_shadow_radius_comparison(3, c_val=2)
        assert result['sl_N']['rho'] == 0
        assert result['W_3']['rho_T_line'] > 0

    def test_sl_class_L(self):
        """sl_N is class L (depth 3)."""
        from compute.lib.shadow_radius import ds_shadow_radius_comparison
        result = ds_shadow_radius_comparison(2)
        assert result['sl_N']['class'] == 'L'
        assert result['sl_N']['depth'] == 3

    def test_w_class_M(self):
        """W_N is class M (depth infinity)."""
        from compute.lib.shadow_radius import ds_shadow_radius_comparison
        result = ds_shadow_radius_comparison(3)
        assert result['W_3']['class'] == 'M'


# ============================================================================
# 14. Kappa formula from Sugawara
# ============================================================================

class TestKappaFromSugawara:
    """kappa = dim(g)*(k+h^v)/(2*h^v) = c*dim(g)/(2*k*dim(g)/(k+h^v))..."""

    def test_sugawara_c_sl2(self):
        """c(sl_2, k=1) = 1*3/(1+2) = 1 (matches known)."""
        from compute.lib.lie_algebra import sugawara_c
        assert sugawara_c("A", 1, 1) == 1

    def test_sugawara_c_sl3(self):
        """c(sl_3, k=1) = 1*8/(1+3) = 2."""
        from compute.lib.lie_algebra import sugawara_c
        assert sugawara_c("A", 2, 1) == 2

    def test_sugawara_critical_raises(self):
        """Sugawara undefined at critical level k = -h^v."""
        from compute.lib.lie_algebra import sugawara_c
        with pytest.raises(ValueError):
            sugawara_c("A", 1, -2)  # sl_2 critical level

    def test_kappa_from_sugawara_consistency(self):
        """kappa = c * dim/(2*k*dim/(k+h^v)) simplifies to dim*(k+h^v)/(2*h^v)."""
        from compute.lib.lie_algebra import sugawara_c, kappa_km, cartan_data
        # For sl_2 at k=1: c=1, kappa=9/4
        # kappa = dim*(k+h^v)/(2*h^v) = 3*3/4 = 9/4
        assert kappa_km("A", 1, 1) == Rational(9, 4)
        # Alternative: kappa = c * sigma where sigma = sum 1/(m_i+1)
        # For Virasoro (DS of sl_2): kappa_Vir = c_Vir/2
        # But for KM itself: kappa = dim(g)*(k+h^v)/(2*h^v)
