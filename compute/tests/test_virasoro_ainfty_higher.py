r"""Tests for higher A-infinity transferred structure maps m_5, m_6, m_7
for the Virasoro algebra.

Verifies:
1. Exact symbolic formulas for S_5, S_6, S_7 (independent derivation)
2. Convolution recursion consistency (f^2 = Q_L)
3. A-infinity / Maurer-Cartan relations at arities 5, 6, 7
4. Shadow-formality cross-check against quintic_shadow_engine.py
5. Four-class depth classification at higher arities
6. Complementarity (AP24-safe: kappa + kappa' = 13, NOT 0)
7. Sign pattern and growth rate
8. Specific central charge evaluations (Ising, free boson, Liouville, critical)
9. Formality obstruction nontriviality (class M: infinite depth)
10. Structure constant tables

Ground truth:
    quintic_shadow_engine.py (independent computation)
    prop:shadow-formality-low-arity (nonlinear_modular_shadows.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    landscape_census.tex (authoritative formula source)
"""

import pytest
from fractions import Fraction as FR


from compute.lib.virasoro_ainfty_higher import (
    HigherVirasoroAInfinity,
    S5_exact,
    S6_exact,
    S7_exact,
    alternating_sign_pattern,
    bc_ghosts_higher,
    affine_sl2_higher,
    complementarity_sum,
    convolution_coefficients,
    cross_family_table,
    evaluate_at_special_charges,
    heisenberg_higher,
    mk_coefficient_table,
    shadow_growth_rate,
    virasoro_shadow_metric,
    virasoro_shadow_tower,
)


# ============================================================================
# 1. Exact symbolic formulas: S_5, S_6, S_7
# ============================================================================

class TestExactFormulas:
    """Verify exact rational formulas for S_5, S_6, S_7 against the recursion."""

    def test_S5_formula_c25(self):
        """S_5(25) = -48 / (625 * 147) = -48/91875."""
        c = FR(25)
        expected = FR(-48) / (c ** 2 * (FR(5) * c + FR(22)))
        assert S5_exact(c) == expected

    def test_S5_formula_c1(self):
        """S_5(1) = -48 / (1 * 27) = -16/9."""
        c = FR(1)
        expected = FR(-48) / (FR(1) * FR(27))
        assert S5_exact(c) == expected

    def test_S5_matches_recursion_c25(self):
        """S_5 from exact formula matches convolution recursion at c=25."""
        c = FR(25)
        tower = virasoro_shadow_tower(c, 7)
        assert tower[5] == S5_exact(c)

    def test_S5_matches_recursion_c1(self):
        c = FR(1)
        tower = virasoro_shadow_tower(c, 7)
        assert tower[5] == S5_exact(c)

    def test_S5_matches_recursion_c13(self):
        c = FR(13)
        tower = virasoro_shadow_tower(c, 7)
        assert tower[5] == S5_exact(c)

    def test_S6_formula_c25(self):
        """S_6(25) = 80*(45*25+193) / (3*25^3*(5*25+22)^2)
        = 80*1318 / (3*15625*21609) = 105440 / 1012921875."""
        c = FR(25)
        expected = S6_exact(c)
        tower = virasoro_shadow_tower(c, 7)
        assert tower[6] == expected

    def test_S6_matches_recursion_c1(self):
        c = FR(1)
        tower = virasoro_shadow_tower(c, 7)
        assert tower[6] == S6_exact(c)

    def test_S6_matches_recursion_c13(self):
        c = FR(13)
        tower = virasoro_shadow_tower(c, 7)
        assert tower[6] == S6_exact(c)

    def test_S7_formula_c25(self):
        c = FR(25)
        expected = S7_exact(c)
        tower = virasoro_shadow_tower(c, 8)
        assert tower[7] == expected

    def test_S7_matches_recursion_c1(self):
        c = FR(1)
        tower = virasoro_shadow_tower(c, 8)
        assert tower[7] == S7_exact(c)

    def test_S7_matches_recursion_c13(self):
        c = FR(13)
        tower = virasoro_shadow_tower(c, 8)
        assert tower[7] == S7_exact(c)

    def test_S5_independent_derivation_c25(self):
        """Verify S_5 from first principles:
        a_0=c, a_1=6, a_2=40/(c(5c+22)), a_3=-a_1*a_2/a_0, S_5=a_3/5."""
        c = FR(25)
        a0 = c
        a1 = FR(6)
        a2 = FR(40) / (c * (FR(5) * c + FR(22)))
        a3 = -a1 * a2 / a0
        S5_derived = a3 / FR(5)
        assert S5_derived == S5_exact(c)

    def test_S6_independent_derivation_c25(self):
        """Verify S_6 from first principles: a_4=-(2*a_1*a_3+a_2^2)/(2*a_0)."""
        c = FR(25)
        a0 = c
        a1 = FR(6)
        a2 = FR(40) / (c * (FR(5) * c + FR(22)))
        a3 = -a1 * a2 / a0
        a4 = -(FR(2) * a1 * a3 + a2 ** 2) / (FR(2) * a0)
        S6_derived = a4 / FR(6)
        assert S6_derived == S6_exact(c)

    def test_S7_independent_derivation_c25(self):
        """Verify S_7 from first principles: a_5=-(2*a_1*a_4+2*a_2*a_3)/(2*a_0)."""
        c = FR(25)
        a0 = c
        a1 = FR(6)
        a2 = FR(40) / (c * (FR(5) * c + FR(22)))
        a3 = -a1 * a2 / a0
        a4 = -(FR(2) * a1 * a3 + a2 ** 2) / (FR(2) * a0)
        a5 = -(FR(2) * a1 * a4 + FR(2) * a2 * a3) / (FR(2) * a0)
        S7_derived = a5 / FR(7)
        assert S7_derived == S7_exact(c)


# ============================================================================
# 2. Convolution recursion consistency (f^2 = Q_L)
# ============================================================================

class TestConvolutionRecursion:
    """Verify f(t)^2 = Q_L(t) at all orders."""

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25), FR(26)])
    def test_f_squared_order0(self, c_val):
        """[t^0]: a_0^2 = q0 = c^2."""
        q0, q1, q2 = virasoro_shadow_metric(c_val)
        coeffs = convolution_coefficients(q0, q1, q2, 0)
        assert coeffs[0] ** 2 == q0

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25), FR(26)])
    def test_f_squared_order1(self, c_val):
        """[t^1]: 2*a_0*a_1 = q1 = 12c."""
        q0, q1, q2 = virasoro_shadow_metric(c_val)
        coeffs = convolution_coefficients(q0, q1, q2, 1)
        assert FR(2) * coeffs[0] * coeffs[1] == q1

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25), FR(26)])
    def test_f_squared_order2(self, c_val):
        """[t^2]: 2*a_0*a_2 + a_1^2 = q2."""
        q0, q1, q2 = virasoro_shadow_metric(c_val)
        coeffs = convolution_coefficients(q0, q1, q2, 2)
        assert FR(2) * coeffs[0] * coeffs[2] + coeffs[1] ** 2 == q2

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25), FR(26)])
    @pytest.mark.parametrize("order", [3, 4, 5, 6, 7])
    def test_f_squared_higher_vanishes(self, c_val, order):
        """[t^n] for n >= 3 must vanish (Q_L is degree 2)."""
        q0, q1, q2 = virasoro_shadow_metric(c_val)
        coeffs = convolution_coefficients(q0, q1, q2, order)
        conv = sum(coeffs[j] * coeffs[order - j] for j in range(order + 1))
        assert conv == FR(0), f"[t^{order}] residual = {conv} at c={c_val}"

    def test_shadow_metric_identity_full(self):
        """Full f^2=Q_L check via HigherVirasoroAInfinity."""
        vir = HigherVirasoroAInfinity(FR(25))
        residuals = vir.verify_shadow_metric_identity(7)
        for order, res in residuals.items():
            assert res == FR(0), f"f^2=Q_L fails at t^{order}: residual={res}"


# ============================================================================
# 3. A-infinity / Maurer-Cartan relations
# ============================================================================

class TestAInfinityRelations:
    """Verify A-infinity relations at arities 5, 6, 7."""

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25), FR(26)])
    def test_mc_relation_arity5(self, c_val):
        vir = HigherVirasoroAInfinity(c_val)
        assert vir.verify_ainfty_relation(5) == FR(0)

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25), FR(26)])
    def test_mc_relation_arity6(self, c_val):
        vir = HigherVirasoroAInfinity(c_val)
        assert vir.verify_ainfty_relation(6) == FR(0)

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25), FR(26)])
    def test_mc_relation_arity7(self, c_val):
        vir = HigherVirasoroAInfinity(c_val)
        assert vir.verify_ainfty_relation(7) == FR(0)

    def test_all_relations_c25(self):
        """All MC relations at arities 3-7 vanish at c=25."""
        vir = HigherVirasoroAInfinity(FR(25))
        for n, res in vir.verify_all_ainfty_relations(7).items():
            assert res == FR(0), f"MC relation fails at arity {n}"

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25)])
    def test_all_relations_sweep(self, c_val):
        """Sweep all MC relations at multiple central charges."""
        vir = HigherVirasoroAInfinity(c_val)
        for n, res in vir.verify_all_ainfty_relations(7).items():
            assert res == FR(0), f"MC at arity {n}, c={c_val}: {res}"


# ============================================================================
# 4. Cross-check with quintic_shadow_engine.py
# ============================================================================

class TestQuinticCrossCheck:
    """Verify S_5, S_6, S_7 match quintic_shadow_engine.py."""

    def test_S5_matches_quintic_engine_c25(self):
        """Cross-check against quintic_shadow_engine.virasoro_quintic_exact."""
        from compute.lib.quintic_shadow_engine import virasoro_quintic_exact
        from sympy import Rational, Symbol, simplify
        c_sym = Symbol('c', positive=True)

        qe = virasoro_quintic_exact()
        S5_qe = qe['S5']
        # Evaluate at c = 25
        S5_qe_val = S5_qe.subs(c_sym, 25)
        S5_here = S5_exact(FR(25))
        assert float(S5_qe_val) == pytest.approx(float(S5_here), rel=1e-12)

    def test_S5_matches_quintic_engine_c1(self):
        from compute.lib.quintic_shadow_engine import virasoro_quintic_exact
        from sympy import Symbol
        c_sym = Symbol('c', positive=True)

        qe = virasoro_quintic_exact()
        S5_qe_val = float(qe['S5'].subs(c_sym, 1))
        S5_here = float(S5_exact(FR(1)))
        assert S5_qe_val == pytest.approx(S5_here, rel=1e-12)

    def test_S6_matches_quintic_engine(self):
        from compute.lib.quintic_shadow_engine import virasoro_sextic_exact
        from sympy import Symbol
        c_sym = Symbol('c', positive=True)

        se = virasoro_sextic_exact()
        S6_qe_val = float(se['S6'].subs(c_sym, 25))
        S6_here = float(S6_exact(FR(25)))
        assert S6_qe_val == pytest.approx(S6_here, rel=1e-12)

    def test_S7_matches_quintic_engine(self):
        from compute.lib.quintic_shadow_engine import virasoro_sextic_exact
        from sympy import Symbol
        c_sym = Symbol('c', positive=True)

        se = virasoro_sextic_exact()
        S7_qe_val = float(se['S7'].subs(c_sym, 25))
        S7_here = float(S7_exact(FR(25)))
        assert S7_qe_val == pytest.approx(S7_here, rel=1e-12)

    def test_shadow_tower_matches_quintic_engine_full(self):
        """Full tower cross-check at c=25 against quintic_shadow_engine."""
        from compute.lib.quintic_shadow_engine import virasoro_shadow_tower_exact
        from sympy import Symbol
        c_sym = Symbol('c', positive=True)

        tower_qe = virasoro_shadow_tower_exact(max_r=8)
        tower_here = virasoro_shadow_tower(FR(25), max_arity=8)

        for r in range(2, 9):
            qe_val = float(tower_qe[r].subs(c_sym, 25))
            here_val = float(tower_here[r])
            assert qe_val == pytest.approx(here_val, rel=1e-12), \
                f"S_{r}: quintic_engine={qe_val}, here={here_val}"


# ============================================================================
# 5. Four-class depth classification at higher arities
# ============================================================================

class TestDepthClassification:
    """Verify G/L/C/M classification at arities 5-7."""

    def test_heisenberg_all_zero_higher(self):
        """Class G: S_r = 0 for all r >= 3."""
        h = heisenberg_higher(FR(1), 7)
        for r in range(3, 8):
            assert h[r] == FR(0), f"Heisenberg S_{r} = {h[r]} != 0"

    def test_affine_all_zero_arity4plus(self):
        """Class L: S_r = 0 for all r >= 4."""
        a = affine_sl2_higher(FR(1), 7)
        assert a[3] != FR(0), "Affine S_3 should be nonzero"
        for r in range(4, 8):
            assert a[r] == FR(0), f"Affine S_{r} = {a[r]} != 0"

    def test_bc_ghosts_all_zero_arity5plus(self):
        """Class C: S_r = 0 for all r >= 5 (stratum separation)."""
        bg = bc_ghosts_higher(7)
        assert bg[3] != FR(0), "bc S_3 should be nonzero"
        assert bg[4] != FR(0), "bc S_4 should be nonzero"
        for r in range(5, 8):
            assert bg[r] == FR(0), f"bc S_{r} = {bg[r]} != 0"

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(25)])
    def test_virasoro_all_nonzero(self, c_val):
        """Class M: S_r != 0 for ALL r >= 2."""
        tower = virasoro_shadow_tower(c_val, 7)
        for r in range(2, 8):
            assert tower[r] != FR(0), f"Virasoro S_{r} = 0 at c={c_val}"

    def test_cross_family_table_structure(self):
        """Cross-family table has correct structure."""
        table = cross_family_table(7)
        assert 'Heisenberg' in table
        assert 'Affine_sl2' in table
        assert 'bc_ghosts' in table
        assert 'Virasoro_c25' in table
        for name, tower in table.items():
            for r in range(2, 8):
                assert r in tower, f"{name} missing S_{r}"


# ============================================================================
# 6. Complementarity (AP24-safe)
# ============================================================================

class TestComplementarity:
    """Verify Koszul duality constraints at higher arities."""

    def test_kappa_sum_is_13_not_0(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        c = FR(25)
        sums = complementarity_sum(c, 7)
        assert sums[2] == FR(13)

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(5), FR(13), FR(25)])
    def test_kappa_sum_parametric(self, c_val):
        sums = complementarity_sum(c_val, 7)
        assert sums[2] == FR(13)

    def test_S3_sum(self):
        """S_3(c) + S_3(26-c) = 2 + 2 = 4 (both are alpha=2)."""
        c = FR(25)
        sums = complementarity_sum(c, 7)
        assert sums[3] == FR(4)

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25)])
    def test_S3_sum_parametric(self, c_val):
        sums = complementarity_sum(c_val, 7)
        assert sums[3] == FR(4)

    def test_self_dual_c13_higher(self):
        """At self-dual c=13: S_r(13) + S_r(13) = 2*S_r(13)."""
        sums = complementarity_sum(FR(13), 7)
        tower = virasoro_shadow_tower(FR(13), 7)
        for r in range(2, 8):
            assert sums[r] == FR(2) * tower[r]

    def test_complementarity_sum_rational(self):
        """The sum S_r(c) + S_r(26-c) is a well-defined rational function."""
        for c_val in [FR(1), FR(5), FR(10), FR(25)]:
            sums = complementarity_sum(c_val, 7)
            for r in range(2, 8):
                assert isinstance(sums[r], FR), \
                    f"S_{r}(c)+S_{r}(26-c) not Fraction at c={c_val}"


# ============================================================================
# 7. Sign pattern and growth rate
# ============================================================================

class TestSignsAndGrowth:
    """Verify alternating sign pattern and growth rate convergence."""

    def test_sign_pattern_c25(self):
        """Virasoro at c=25: S_2,S_3,S_4 > 0; S_5 < 0; S_6 > 0; S_7 < 0."""
        signs = alternating_sign_pattern(FR(25), 7)
        assert signs[2] == 1   # kappa > 0
        assert signs[3] == 1   # alpha = 2 > 0
        assert signs[4] == 1   # S_4 > 0
        assert signs[5] == -1  # S_5 < 0
        assert signs[6] == 1   # S_6 > 0
        assert signs[7] == -1  # S_7 < 0

    def test_sign_pattern_c1(self):
        """Same alternating pattern at c=1."""
        signs = alternating_sign_pattern(FR(1), 7)
        assert signs[2] == 1
        assert signs[3] == 1
        assert signs[4] == 1
        assert signs[5] == -1

    def test_growth_rate_c25_convergent(self):
        """At c=25, growth rate rho < 1 (convergent tower)."""
        rho_sq = shadow_growth_rate(FR(25))
        assert float(rho_sq) < 1.0

    def test_growth_rate_c13_convergent(self):
        """At c=13 (self-dual), rho < 1."""
        rho_sq = shadow_growth_rate(FR(13))
        assert float(rho_sq) < 1.0

    def test_growth_rate_positive(self):
        """rho^2 > 0 for all positive c (class M: infinite depth)."""
        for c_val in [FR(1, 2), FR(1), FR(5), FR(13), FR(25), FR(26)]:
            rho_sq = shadow_growth_rate(c_val)
            assert rho_sq > 0, f"rho^2 = {rho_sq} not positive at c={c_val}"

    def test_growth_rate_formula(self):
        """rho^2 = (180c + 872) / (c^2*(5c+22))."""
        c = FR(25)
        expected = (FR(180) * c + FR(872)) / (c ** 2 * (FR(5) * c + FR(22)))
        assert shadow_growth_rate(c) == expected


# ============================================================================
# 8. Specific central charge evaluations
# ============================================================================

class TestSpecialCharges:
    """Evaluate at physically significant central charges."""

    def test_ising_c_half(self):
        """Ising model c=1/2."""
        tower = virasoro_shadow_tower(FR(1, 2), 7)
        assert tower[2] == FR(1, 4)  # kappa = 1/4
        assert tower[3] == FR(2)     # universal alpha
        for r in range(2, 8):
            assert tower[r] != FR(0), f"S_{r} = 0 at Ising"

    def test_free_boson_c1(self):
        """Free boson c=1."""
        tower = virasoro_shadow_tower(FR(1), 7)
        assert tower[2] == FR(1, 2)  # kappa = 1/2
        assert tower[3] == FR(2)     # alpha
        assert tower[4] == FR(10) / (FR(1) * FR(27))  # S_4 = 10/27

    def test_liouville_c25(self):
        """Liouville theory c=25."""
        tower = virasoro_shadow_tower(FR(25), 7)
        assert tower[2] == FR(25, 2)  # kappa = 25/2
        assert tower[3] == FR(2)

    def test_critical_string_c26(self):
        """Critical string c=26: dual has c'=0 (uncurved)."""
        tower = virasoro_shadow_tower(FR(26), 7)
        assert tower[2] == FR(13)  # kappa = 13
        assert tower[3] == FR(2)
        # S_4 = 10/(26*152) = 10/3952 = 5/1976
        assert tower[4] == FR(10) / (FR(26) * FR(152))

    def test_self_dual_c13(self):
        """Self-dual c=13: Vir_13^! = Vir_13."""
        tower = virasoro_shadow_tower(FR(13), 7)
        assert tower[2] == FR(13, 2)  # kappa = 13/2
        # S_4 = 10/(13*87) = 10/1131
        assert tower[4] == FR(10) / (FR(13) * (FR(5) * FR(13) + FR(22)))

    def test_evaluate_at_special_charges_runs(self):
        """The evaluation function runs without error."""
        results = evaluate_at_special_charges(7)
        assert 'Ising_c=1/2' in results
        assert 'critical_string_c=26' in results
        for name, tower in results.items():
            for r in range(2, 8):
                assert r in tower, f"{name} missing S_{r}"

    def test_dual_pair_c1_c25(self):
        """c=1 and c=25 are Koszul dual: c + c' = 26."""
        tower_1 = virasoro_shadow_tower(FR(1), 7)
        tower_25 = virasoro_shadow_tower(FR(25), 7)
        # kappa sum = 13
        assert tower_1[2] + tower_25[2] == FR(13)
        # S_3 sum = 4
        assert tower_1[3] + tower_25[3] == FR(4)


# ============================================================================
# 9. Formality obstruction nontriviality
# ============================================================================

class TestFormalityObstruction:
    """Verify Virasoro is NOT A-infinity formal (class M, infinite depth)."""

    @pytest.mark.parametrize("k", [3, 4, 5, 6, 7])
    def test_obstruction_nonzero_c25(self, k):
        """o^(k) != 0 for all k >= 3 at c=25."""
        vir = HigherVirasoroAInfinity(FR(25))
        obs = vir.formality_obstruction(k)
        assert obs['nonzero'] is True, f"o^({k}) unexpectedly zero"
        assert obs['is_trivial'] is False

    @pytest.mark.parametrize("k", [3, 4, 5, 6, 7])
    def test_obstruction_nonzero_c1(self, k):
        """o^(k) != 0 for all k >= 3 at c=1."""
        vir = HigherVirasoroAInfinity(FR(1))
        obs = vir.formality_obstruction(k)
        assert obs['nonzero'] is True

    def test_obstruction_data_structure(self):
        vir = HigherVirasoroAInfinity(FR(25))
        obs = vir.formality_obstruction(5)
        assert 'arity' in obs
        assert 'S_k' in obs
        assert 'forcing_sum' in obs
        assert obs['arity'] == 5

    def test_heisenberg_is_formal(self):
        """Heisenberg has S_r = 0 for r >= 3: A-infinity formal."""
        h = heisenberg_higher(FR(1), 7)
        for r in range(3, 8):
            assert h[r] == FR(0)


# ============================================================================
# 10. Structure constant tables
# ============================================================================

class TestStructureConstants:
    """Verify structure constant tables."""

    def test_table_c25_has_entries(self):
        table = mk_coefficient_table(FR(25), max_arity=7, max_weight=14)
        assert len(table) >= 6  # arities 2-7
        for entry in table:
            assert 'arity' in entry
            assert 'output_weight' in entry
            assert 'S_k' in entry

    def test_table_output_weight_is_2k(self):
        """Output weight = 2 * arity."""
        table = mk_coefficient_table(FR(25), max_arity=7)
        for entry in table:
            assert entry['output_weight'] == 2 * entry['arity']

    def test_table_all_nonzero_virasoro(self):
        """All structure constants nonzero for Virasoro (class M)."""
        table = mk_coefficient_table(FR(25), max_arity=7)
        for entry in table:
            assert entry['S_k'] != FR(0), \
                f"S_{entry['arity']} = 0 at c=25"

    def test_higher_ainfty_structure_constants(self):
        """Test HigherVirasoroAInfinity.structure_constants_table."""
        vir = HigherVirasoroAInfinity(FR(25))
        table = vir.structure_constants_table(7)
        assert len(table) >= 6
        for entry in table:
            assert entry['coefficient'] != FR(0)

    def test_mk_matches_shadow_tower(self):
        """mk_primary matches shadow_tower directly."""
        vir = HigherVirasoroAInfinity(FR(25))
        tower = vir.shadow_tower(7)
        for k in range(2, 8):
            assert vir.mk_primary(k) == tower[k]

    def test_m1_is_zero(self):
        """m_1 = 0 on cohomology."""
        vir = HigherVirasoroAInfinity(FR(25))
        assert vir.mk_primary(1) == FR(0)

    def test_m0_is_zero(self):
        """mk_primary(0) = 0."""
        vir = HigherVirasoroAInfinity(FR(25))
        assert vir.mk_primary(0) == FR(0)


# ============================================================================
# 11. Shadow metric coefficients
# ============================================================================

class TestShadowMetric:
    """Verify shadow metric Q_L coefficients."""

    def test_q0_is_c_squared(self):
        """q0 = 4*kappa^2 = c^2."""
        c = FR(25)
        q0, _, _ = virasoro_shadow_metric(c)
        assert q0 == c ** 2

    def test_q1_is_12c(self):
        """q1 = 12*kappa*alpha = 12c."""
        c = FR(25)
        _, q1, _ = virasoro_shadow_metric(c)
        assert q1 == FR(12) * c

    def test_q2_formula(self):
        """q2 = 36 + 80/(5c+22)."""
        c = FR(25)
        _, _, q2 = virasoro_shadow_metric(c)
        expected = FR(36) + FR(80) / (FR(5) * c + FR(22))
        assert q2 == expected

    @pytest.mark.parametrize("c_val", [FR(1, 2), FR(1), FR(13), FR(25)])
    def test_metric_coefficients_positive(self, c_val):
        """All metric coefficients positive for c > 0."""
        q0, q1, q2 = virasoro_shadow_metric(c_val)
        assert q0 > 0
        assert q1 > 0
        assert q2 > 0


# ============================================================================
# 12. Convolution coefficient properties
# ============================================================================

class TestConvolutionCoefficients:
    """Verify properties of the convolution coefficients a_n."""

    def test_a0_equals_c(self):
        """a_0 = sqrt(q0) = c for Virasoro."""
        q0, q1, q2 = virasoro_shadow_metric(FR(25))
        coeffs = convolution_coefficients(q0, q1, q2, 0)
        assert coeffs[0] == FR(25)

    def test_a1_equals_6(self):
        """a_1 = q1/(2*a_0) = 12c/(2c) = 6 (universal)."""
        for c_val in [FR(1, 2), FR(1), FR(13), FR(25), FR(26)]:
            q0, q1, q2 = virasoro_shadow_metric(c_val)
            coeffs = convolution_coefficients(q0, q1, q2, 1)
            assert coeffs[1] == FR(6), f"a_1 = {coeffs[1]} != 6 at c={c_val}"

    def test_a2_formula(self):
        """a_2 = 40/(c*(5c+22)) for Virasoro."""
        c = FR(25)
        q0, q1, q2 = virasoro_shadow_metric(c)
        coeffs = convolution_coefficients(q0, q1, q2, 2)
        expected = FR(40) / (c * (FR(5) * c + FR(22)))
        assert coeffs[2] == expected

    def test_sr_equals_a_over_r(self):
        """S_r = a_{r-2} / r."""
        c = FR(25)
        tower = virasoro_shadow_tower(c, 7)
        q0, q1, q2 = virasoro_shadow_metric(c)
        coeffs = convolution_coefficients(q0, q1, q2, 5)
        for n in range(len(coeffs)):
            r = n + 2
            if r in tower:
                assert tower[r] == coeffs[n] / FR(r)


# ============================================================================
# 13. Additional robustness tests
# ============================================================================

class TestRobustness:
    """Edge cases and additional checks."""

    def test_large_arity(self):
        """Compute through arity 15 without error."""
        tower = virasoro_shadow_tower(FR(25), 15)
        assert len(tower) == 14  # S_2 through S_15
        for r in range(2, 16):
            assert r in tower
            assert tower[r] != FR(0)

    def test_tower_alternates_eventually(self):
        """For large enough arity, signs alternate (oscillatory tower)."""
        tower = virasoro_shadow_tower(FR(25), 12)
        # From arity 5 onwards, sign alternates
        for r in range(5, 12):
            if tower[r] != FR(0) and tower[r + 1] != FR(0):
                assert (tower[r] > 0) != (tower[r + 1] > 0), \
                    f"Signs don't alternate at S_{r}, S_{r+1}"

    def test_mc_relations_arity_8_through_10(self):
        """MC relations hold at arities 8-10 too."""
        vir = HigherVirasoroAInfinity(FR(25))
        for n in range(8, 11):
            vir._tower_cache = None  # force recompute
            # Need tower through arity n
            tower = vir.shadow_tower(n)
            res = vir.verify_ainfty_relation(n)
            assert res == FR(0), f"MC fails at arity {n}: {res}"

    def test_small_c_half(self):
        """c=1/2 (Ising): exact computation works."""
        vir = HigherVirasoroAInfinity(FR(1, 2))
        tower = vir.shadow_tower(7)
        assert tower[2] == FR(1, 4)
        assert tower[5] == S5_exact(FR(1, 2))

    def test_c26_dual_uncurved(self):
        """At c=26, the dual has c'=0 (uncurved). But Virasoro at c=26 is curved."""
        tower = virasoro_shadow_tower(FR(26), 7)
        # kappa = 13
        assert tower[2] == FR(13)
        # All S_r nonzero (class M)
        for r in range(2, 8):
            assert tower[r] != FR(0)

    def test_negative_c_raises(self):
        """Negative central charge raises ValueError."""
        with pytest.raises(ValueError):
            virasoro_shadow_tower(FR(-1), 5)

    def test_zero_c_raises(self):
        """c=0 raises ValueError (division by zero in S_4)."""
        with pytest.raises((ValueError, ZeroDivisionError)):
            virasoro_shadow_tower(FR(0), 5)

    def test_higher_ainfty_constructor(self):
        """Constructor works correctly."""
        vir = HigherVirasoroAInfinity(FR(25))
        assert vir.c == FR(25)
        assert vir.kappa == FR(25, 2)

    def test_higher_ainfty_negative_c_raises(self):
        with pytest.raises(ValueError):
            HigherVirasoroAInfinity(FR(-5))

    def test_evaluate_tower_numeric(self):
        """Numeric evaluation gives floats."""
        vir = HigherVirasoroAInfinity(FR(25))
        numeric = vir.evaluate_tower_numeric(7)
        for r, val in numeric.items():
            assert isinstance(val, float)
