#!/usr/bin/env python3
r"""
Tests for critical_line_atlas.py -- Critical line atlas for the standard landscape.

Verifies:
1. Cusp form dimensions (standard number theory)
2. Lattice critical line positions and counts
3. Depth-critical line formula d = 1 + #{lines} for lattice VOAs
4. Lattice critical line spacing
5. Self-dual factorization at c = 13
6. Anomaly cancellation analysis at c = 26
7. Davenport-Heilbronn classification for minimal models
8. Class number computation for fundamental discriminants
9. Betagamma gap of 2
10. Rank-depth table consistency
11. Cross-checks against manuscript claims
"""

import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from critical_line_atlas import (
    cusp_form_dim_sl2z,
    modular_form_dim_sl2z,
    lattice_critical_lines,
    lattice_depth,
    lattice_critical_line_count,
    verify_depth_critical_line_formula,
    lattice_line_spacing,
    LATTICE_DATA,
    affine_km_critical_lines,
    virasoro_shadow_data,
    virasoro_binary_form,
    virasoro_critical_lines_generic,
    virasoro_self_dual_factorization,
    virasoro_c26_analysis,
    minimal_model_c,
    class_number,
    virasoro_dh_discriminant,
    minimal_model_dh_classification,
    betagamma_critical_lines,
    depth_critical_line_verification,
    rank_depth_table,
)


# =========================================================================
# 1. Cusp form dimensions (standard number theory)
# =========================================================================

class TestCuspFormDimensions:

    def test_dim_S_k_below_12(self):
        """dim S_k(SL_2(Z)) = 0 for k < 12."""
        for k in range(0, 12, 2):
            assert cusp_form_dim_sl2z(k) == 0, f"dim S_{k} should be 0"

    def test_dim_S_12(self):
        """dim S_12 = 1 (Ramanujan Delta)."""
        assert cusp_form_dim_sl2z(12) == 1

    def test_dim_S_16(self):
        """dim S_16 = 1."""
        assert cusp_form_dim_sl2z(16) == 1

    def test_dim_S_20(self):
        """dim S_20 = 1."""
        assert cusp_form_dim_sl2z(20) == 1

    def test_dim_S_24(self):
        """dim S_24 = 2."""
        assert cusp_form_dim_sl2z(24) == 2

    def test_dim_S_26(self):
        """dim S_26 = 2 (26 = 2 mod 12, so floor(26/12) - 1 = 1...
        Wait: 26/12 = 2.16, floor = 2, and 26 mod 12 = 2, so dim = 2-1 = 1."""
        assert cusp_form_dim_sl2z(26) == 1

    def test_dim_S_36(self):
        """dim S_36 = 3."""
        assert cusp_form_dim_sl2z(36) == 3

    def test_dim_S_48(self):
        """dim S_48 = 4."""
        assert cusp_form_dim_sl2z(48) == 4

    def test_odd_weight_zero(self):
        """dim S_k = 0 for odd k (no forms for SL_2(Z))."""
        for k in [1, 3, 5, 7, 11, 13]:
            assert cusp_form_dim_sl2z(k) == 0

    def test_dim_M_k_formula(self):
        """dim M_k = dim S_k + 1 for k >= 4."""
        for k in range(4, 50, 2):
            assert modular_form_dim_sl2z(k) == cusp_form_dim_sl2z(k) + 1

    def test_dim_M_0(self):
        """dim M_0 = 1 (constants)."""
        assert modular_form_dim_sl2z(0) == 1

    def test_dim_M_2(self):
        """dim M_2 = 0 (no modular forms of weight 2 for SL_2(Z))."""
        assert modular_form_dim_sl2z(2) == 0


# =========================================================================
# 2. Lattice critical line positions
# =========================================================================

class TestLatticeCriticalLines:

    def test_E8_two_lines(self):
        """E_8 (rank 8): 2 critical lines at Re(s) = 1/2 and 7/2."""
        lines = lattice_critical_lines(8)
        assert len(lines) == 2
        positions = sorted([l['position'] for l in lines])
        assert positions == [Fraction(1, 2), Fraction(7, 2)]

    def test_E8_squared_two_lines(self):
        """E_8^2 (rank 16): 2 lines at Re(s) = 1/2 and 15/2."""
        lines = lattice_critical_lines(16)
        assert len(lines) == 2
        positions = sorted([l['position'] for l in lines])
        assert positions == [Fraction(1, 2), Fraction(15, 2)]

    def test_Leech_three_lines(self):
        """Leech (rank 24): 3 lines at 1/2, 23/2, 6."""
        data = LATTICE_DATA['Leech']
        lines = data['critical_lines']
        positions = sorted([l['position'] for l in lines])
        assert positions == [Fraction(1, 2), Fraction(6, 1), Fraction(23, 2)]

    def test_rank_48_four_lines(self):
        """Rank 48: 4 lines (2 from cusp forms of S_24, dim=2)."""
        data = LATTICE_DATA['rank_48']
        lines = data['critical_lines']
        assert len(lines) == 4
        # Two cusp form lines both at Re(s) = 12
        cusp_lines = [l for l in lines if 'f_' in l['source']]
        assert len(cusp_lines) == 2
        for cl in cusp_lines:
            assert cl['position'] == Fraction(12, 1)

    def test_Z2_one_line(self):
        """Z^2 (rank 2): 1 line at Re(s) = 1/2."""
        data = LATTICE_DATA['Z2']
        assert len(data['critical_lines']) == 1
        assert data['critical_lines'][0]['position'] == Fraction(1, 2)

    def test_Z_rank1_line(self):
        """Z (rank 1): 1 line at Re(s) = 1/4 (from zeta(2s))."""
        data = LATTICE_DATA['Z']
        assert len(data['critical_lines']) == 1
        assert data['critical_lines'][0]['position'] == Fraction(1, 4)

    def test_E8_Eisenstein_product(self):
        """E_8 Epstein = 240*2^{-s}*zeta(s)*zeta(s-3) (manuscript eq)."""
        data = LATTICE_DATA['E8']
        assert 'zeta(s)' in data['epstein_formula']
        assert 'zeta(s-3)' in data['epstein_formula']

    def test_Leech_Ramanujan_L_function(self):
        """Leech Epstein includes L(s, Delta_12) from Ramanujan cusp form."""
        data = LATTICE_DATA['Leech']
        cusp_lines = [l for l in data['critical_lines'] if 'Delta_12' in l['source']]
        assert len(cusp_lines) == 1
        assert cusp_lines[0]['position'] == Fraction(6, 1)


# =========================================================================
# 3. Depth-critical line formula
# =========================================================================

class TestDepthFormula:

    def test_lattice_depth_formula_rank_8(self):
        """d(V_{E_8}) = 3 = 1 + 2 critical lines."""
        assert lattice_depth(8) == 3
        assert lattice_critical_line_count(8) == 2
        assert lattice_depth(8) == 1 + lattice_critical_line_count(8)

    def test_lattice_depth_formula_rank_16(self):
        """d(V_{E_8^2}) = 3 = 1 + 2."""
        assert lattice_depth(16) == 3
        assert lattice_critical_line_count(16) == 2

    def test_lattice_depth_formula_rank_24(self):
        """d(V_Leech) = 4 = 1 + 3."""
        assert lattice_depth(24) == 4
        assert lattice_critical_line_count(24) == 3

    def test_lattice_depth_formula_rank_48(self):
        """d(rank 48) = 5 = 1 + 4."""
        assert lattice_depth(48) == 5
        assert lattice_critical_line_count(48) == 4

    def test_depth_equals_1_plus_lines_all_ranks(self):
        """d = 1 + #{lines} for all even unimodular lattice ranks up to 120."""
        for rank in range(8, 121, 8):
            d = lattice_depth(rank)
            n = lattice_critical_line_count(rank)
            assert d == 1 + n, f"rank {rank}: d={d}, 1+n={1+n}"

    def test_depth_formula_d_3_plus_gk(self):
        """d = 3 + dim S_{r/2} for rank >= 8."""
        for rank in range(8, 121, 8):
            k = rank // 2
            g_k = cusp_form_dim_sl2z(k)
            d = lattice_depth(rank)
            assert d == 3 + g_k, f"rank {rank}: d={d}, 3+g={3+g_k}"

    def test_low_rank_depth_2(self):
        """d = 2 for rank < 8."""
        for rank in [1, 2, 4]:
            assert lattice_depth(rank) == 2

    def test_betagamma_gap_2(self):
        """Betagamma: depth=4, lines=1, gap=2."""
        bg = betagamma_critical_lines()
        assert bg['shadow_depth'] == 4
        assert bg['critical_line_count'] == 1
        assert bg['gap'] == 2
        # Verify: depth = 1 + lines + gap
        assert bg['shadow_depth'] == 1 + bg['critical_line_count'] + bg['gap']

    def test_verify_depth_all_lattices(self):
        """Systematic verification of depth-critical line formula."""
        results = depth_critical_line_verification()
        for r in results:
            if isinstance(r['rank'], int):
                if r['rank'] >= 8:
                    assert r['formula_holds'], \
                        f"Depth formula fails at rank {r['rank']}"
                    assert r['gap'] == 0, \
                        f"Nonzero gap at rank {r['rank']}"


# =========================================================================
# 4. Lattice critical line spacing
# =========================================================================

class TestLineSpacing:

    def test_E8_spacing(self):
        """E_8: spacing between lines 1 and 2 is k-1 = 3."""
        sp = lattice_line_spacing(8)
        assert sp['spacing_1_2'] == Fraction(3, 1)

    def test_E8_sq_spacing(self):
        """E_8^2: spacing = k-1 = 7."""
        sp = lattice_line_spacing(16)
        assert sp['spacing_1_2'] == Fraction(7, 1)

    def test_Leech_spacing(self):
        """Leech: spacing = k-1 = 11."""
        sp = lattice_line_spacing(24)
        assert sp['spacing_1_2'] == Fraction(11, 1)

    def test_cusp_line_between(self):
        """Cusp form line Re(s) = k/2 is between 1/2 and k-1/2 for k >= 12."""
        for rank in [24, 48, 72, 96]:
            sp = lattice_line_spacing(rank)
            if sp['cusp_form_dim'] > 0:
                assert sp['cusp_between'] is True, \
                    f"rank {rank}: cusp line not between Eisenstein lines"

    def test_spacing_grows_with_rank(self):
        """Spacing between lines 1 and 2 grows as r/2 - 1."""
        for rank in range(8, 97, 8):
            sp = lattice_line_spacing(rank)
            k = rank // 2
            expected = Fraction(k - 1)
            assert sp['spacing_1_2'] == expected, \
                f"rank {rank}: spacing {sp['spacing_1_2']} != {expected}"


# =========================================================================
# 5. Self-dual factorization at c = 13
# =========================================================================

class TestSelfDualFactorization:

    def test_c13_is_self_dual(self):
        """Vir_13 is Koszul self-dual: Vir_13^! = Vir_{26-13} = Vir_13."""
        sd = virasoro_self_dual_factorization()
        assert sd['self_dual'] is True
        assert sd['kappa'] == sd['kappa_dual']

    def test_c13_kappa(self):
        """kappa(Vir_13) = 13/2."""
        sd = virasoro_self_dual_factorization()
        assert sd['kappa'] == Fraction(13, 2)

    def test_c13_discriminant(self):
        """disc(Q_L) at c=13 = -320*169/87."""
        sd = virasoro_self_dual_factorization()
        expected = Fraction(-320) * Fraction(169) / Fraction(87)
        assert sd['discriminant'] == expected

    def test_c13_Delta(self):
        """Delta = 40/(5*13+22) = 40/87."""
        sd = virasoro_self_dual_factorization()
        assert sd['Delta'] == Fraction(40, 87)

    def test_c13_S4(self):
        """S4 = 10/(13*87) = 10/1131."""
        sd = virasoro_self_dual_factorization()
        expected = Fraction(10, 13 * 87)
        assert sd['S4'] == expected

    def test_c13_references_theorem(self):
        """Self-dual factorization references thm:self-dual-factorization."""
        sd = virasoro_self_dual_factorization()
        assert sd['theorem'] == 'thm:self-dual-factorization'

    def test_c13_critical_line_at_half(self):
        """Self-dual Virasoro has critical line at Re(s) = 1/2."""
        sd = virasoro_self_dual_factorization()
        assert len(sd['critical_lines']) == 1
        assert sd['critical_lines'][0]['position'] == Fraction(1, 2)


# =========================================================================
# 6. c = 26 analysis
# =========================================================================

class TestC26Analysis:

    def test_c26_kappa(self):
        """kappa(Vir_26) = 13."""
        c26 = virasoro_c26_analysis()
        assert c26['kappa'] == Fraction(13)

    def test_c26_kappa_dual(self):
        """kappa(Vir_0) = 0 (Koszul dual at c=26)."""
        c26 = virasoro_c26_analysis()
        assert c26['kappa_dual'] == Fraction(0)

    def test_c26_kappa_eff(self):
        """kappa_eff = 0 at c=26 (anomaly cancellation)."""
        c26 = virasoro_c26_analysis()
        assert c26['kappa_eff'] == Fraction(0)

    def test_c26_complementarity_AP24(self):
        """kappa + kappa' = 13 (NOT 0, per AP24)."""
        c26 = virasoro_c26_analysis()
        # kappa(Vir_26) + kappa(Vir_0) = 13 + 0 = 13
        assert c26['complementarity_sum'] == Fraction(13)
        # This is NOT zero, confirming AP24

    def test_c26_shadow_infinite(self):
        """Shadow depth is infinite at c=26 (class M)."""
        c26 = virasoro_c26_analysis()
        assert c26['shadow_class'] == 'M'
        assert c26['shadow_depth'] == float('inf')

    def test_c26_discriminant_nonzero(self):
        """Discriminant at c=26 is nonzero (nondegenerate form)."""
        c26 = virasoro_c26_analysis()
        assert c26['discriminant'] != 0

    def test_c26_Delta(self):
        """Delta at c=26: 40/(5*26+22) = 40/152 = 5/19."""
        c26 = virasoro_c26_analysis()
        expected = Fraction(40, 152)
        assert c26['Delta'] == expected

    def test_c26_dual_uncurved(self):
        """Koszul dual Vir_0 is uncurved (kappa = 0)."""
        c26 = virasoro_c26_analysis()
        assert c26['dual_analysis']['kappa_dual'] == Fraction(0)

    def test_c26_has_pole(self):
        """Epstein zeta has standard pole at s = 1."""
        c26 = virasoro_c26_analysis()
        assert c26['scattering']['pole_at_s_1'] is True


# =========================================================================
# 7. Class number computation
# =========================================================================

class TestClassNumber:

    def test_heegner_discriminants(self):
        """The 9 Heegner discriminants have h = 1."""
        heegner = [-3, -4, -7, -8, -11, -19, -43, -67, -163]
        for D in heegner:
            h = class_number(D)
            assert h == 1, f"h({D}) = {h}, expected 1"

    def test_class_number_2(self):
        """Known class number 2 discriminants."""
        for D in [-15, -20, -24]:
            h = class_number(D)
            assert h == 2, f"h({D}) = {h}, expected 2"

    def test_class_number_3(self):
        """h(-23) = 3."""
        assert class_number(-23) == 3

    def test_class_number_40(self):
        """h(-40) = 2 (appears for Ising model)."""
        assert class_number(-40) == 2

    def test_class_number_520(self):
        """h(-520) = 4 (appears for m=5 minimal model)."""
        assert class_number(-520) == 4

    def test_invalid_discriminant(self):
        """Non-discriminant values return None."""
        # D = 2 mod 4 with D odd: not valid
        assert class_number(-5) is None  # -5 mod 4 = 3, but -5 IS valid
        # Actually -5 mod 4 = 3 (in the sense that -5 = -2*4 + 3),
        # so -5 is not a valid discriminant since D must be 0 or 1 mod 4.
        # Wait: -5 mod 4 = -1 mod 4 = 3. And 3 mod 4 = 3.
        # Valid discriminant requires D = 0 or 1 mod 4.
        # -5 mod 4: -5 = -2*4 + 3, so -5 mod 4 = 3. Not in {0,1}. So invalid.
        assert class_number(-5) is None

    def test_positive_returns_none(self):
        """Positive D returns None."""
        assert class_number(5) is None


# =========================================================================
# 8. Davenport-Heilbronn classification
# =========================================================================

class TestDavenportHeilbronn:

    def test_ising_dh_active(self):
        """Ising (m=3, c=1/2): h(-40) = 2, DH active."""
        disc, d_0, h = virasoro_dh_discriminant(Fraction(1, 2))
        assert d_0 == -40
        assert h == 2

    def test_m9_dh_absent(self):
        """M(9,10) at c=14/15: h(-3) = 1, DH absent."""
        disc, d_0, h = virasoro_dh_discriminant(Fraction(14, 15))
        assert d_0 == -3
        assert h == 1

    def test_m5_dh_active(self):
        """M(5,6) at c=4/5: h(-520) = 4, DH active."""
        disc, d_0, h = virasoro_dh_discriminant(Fraction(4, 5))
        assert d_0 == -520
        assert h == 4

    def test_m9_unique_class_1(self):
        """m=9 is the UNIQUE minimal model with h(d_0) = 1 in range 3..20."""
        dh = minimal_model_dh_classification(20)
        class_1_models = [r for r in dh if r['class_number'] == 1]
        assert len(class_1_models) == 1
        assert class_1_models[0]['m'] == 9
        assert class_1_models[0]['c'] == Fraction(14, 15)

    def test_all_models_have_data(self):
        """All 18 minimal models (m=3..20) have discriminant data."""
        dh = minimal_model_dh_classification(20)
        assert len(dh) == 18
        for r in dh:
            assert r['discriminant'] is not None
            assert r['fundamental_disc'] != 0

    def test_discriminant_negative(self):
        """All Virasoro shadow metric discriminants are negative (definite forms)."""
        for m in range(3, 21):
            c = minimal_model_c(m)
            disc, d_0, h = virasoro_dh_discriminant(c)
            assert float(disc) < 0, f"m={m}: disc = {disc} not negative"

    def test_discriminant_grows_magnitude(self):
        """Discriminant magnitude increases with m (approaches -320/5 = -64)."""
        dh = minimal_model_dh_classification(20)
        for i in range(len(dh) - 1):
            # The absolute value of disc grows with m
            assert abs(float(dh[i]['discriminant'])) < abs(float(dh[i+1]['discriminant'])), \
                f"|disc(m={dh[i]['m']})| >= |disc(m={dh[i+1]['m']})|"


# =========================================================================
# 9. Virasoro shadow data consistency
# =========================================================================

class TestVirasoroShadowData:

    def test_kappa_formula(self):
        """kappa = c/2 for Virasoro."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(13), Fraction(26)]:
            data = virasoro_shadow_data(c_val)
            assert data['kappa'] == c_val / 2

    def test_alpha_is_2(self):
        """alpha = 2 for Virasoro (universal)."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(7, 10), Fraction(26)]:
            data = virasoro_shadow_data(c_val)
            assert data['alpha'] == Fraction(2)

    def test_S4_formula(self):
        """S4 = 10/(c(5c+22)) for Virasoro."""
        c = Fraction(1)
        data = virasoro_shadow_data(c)
        expected = Fraction(10, 27)
        assert data['S4'] == expected

    def test_Delta_formula(self):
        """Delta = 40/(5c+22) for Virasoro."""
        c = Fraction(1)
        data = virasoro_shadow_data(c)
        expected = Fraction(40, 27)
        assert data['Delta'] == expected

    def test_discriminant_formula(self):
        """disc = -320c^2/(5c+22) for Virasoro."""
        c = Fraction(1)
        data = virasoro_shadow_data(c)
        expected = Fraction(-320, 27)
        assert data['discriminant'] == expected

    def test_binary_form_discriminant_matches(self):
        """Binary form disc matches direct formula."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(13), Fraction(26)]:
            a, b, c_coeff, disc = virasoro_binary_form(c_val)
            expected = Fraction(-320) * c_val ** 2 / (5 * c_val + 22)
            assert disc == expected, \
                f"c={c_val}: form disc {disc} != formula {expected}"


# =========================================================================
# 10. Affine KM
# =========================================================================

class TestAffineKM:

    def test_sl2_level1_lattice_type(self):
        """sl_2 level 1 is lattice-type (= V_{A_1})."""
        data = affine_km_critical_lines('A', 1, 1)
        assert data['note'] == 'Lattice-type: V_1(sl_2) = V_{A_1}'

    def test_sl2_level1_depth(self):
        """sl_2 level 1: shadow depth 3 (class L)."""
        data = affine_km_critical_lines('A', 1, 1)
        assert data['shadow_depth'] == 3
        assert data['shadow_class'] == 'L'

    def test_sl2_level1_central_charge(self):
        """sl_2 level 1: c = 1."""
        data = affine_km_critical_lines('A', 1, 1)
        assert data['central_charge'] == Fraction(1)

    def test_sl2_level1_kappa(self):
        """sl_2 level 1: kappa = 1/2."""
        data = affine_km_critical_lines('A', 1, 1)
        assert data['kappa'] == Fraction(1, 2)


# =========================================================================
# 11. Rank-depth table
# =========================================================================

class TestRankDepthTable:

    def test_table_structure(self):
        """Table has correct structure."""
        table = rank_depth_table(96)
        assert len(table) == 12  # ranks 8, 16, ..., 96
        for row in table:
            assert 'rank' in row
            assert 'theta_weight' in row
            assert 'dim_M_k' in row
            assert 'dim_S_k' in row

    def test_table_depth_formula(self):
        """max_depth = 3 + dim_S_k for all rows."""
        for row in rank_depth_table(96):
            assert row['max_depth'] == 3 + row['dim_S_k']

    def test_table_line_formula(self):
        """max_lines = 2 + dim_S_k for all rows."""
        for row in rank_depth_table(96):
            assert row['max_lines'] == 2 + row['dim_S_k']

    def test_table_depth_eq_1_plus_lines(self):
        """depth = 1 + lines for all rows."""
        for row in rank_depth_table(96):
            assert row['max_depth'] == 1 + row['max_lines']


# =========================================================================
# 12. Cross-checks against manuscript claims
# =========================================================================

class TestManuscriptClaims:

    def test_Z_depth_2_one_line(self):
        """comp:period-shadow-vz: depth 2, one critical line at Re(s)=1/4."""
        data = LATTICE_DATA['Z']
        assert data['depth'] == 2
        assert len(data['critical_lines']) == 1
        assert data['critical_lines'][0]['position'] == Fraction(1, 4)

    def test_E8_depth_3_two_lines(self):
        """comp:period-shadow-ve8: depth 3, two lines at 1/2 and 7/2."""
        data = LATTICE_DATA['E8']
        assert data['depth'] == 3
        positions = sorted([l['position'] for l in data['critical_lines']])
        assert positions == [Fraction(1, 2), Fraction(7, 2)]

    def test_Leech_depth_4_three_lines(self):
        """comp:period-shadow-leech: depth 4, three lines at 1/2, 23/2, 6."""
        data = LATTICE_DATA['Leech']
        assert data['depth'] == 4
        positions = sorted([l['position'] for l in data['critical_lines']])
        assert positions == [Fraction(1, 2), Fraction(6, 1), Fraction(23, 2)]

    def test_Leech_Ramanujan_at_arity_4(self):
        """Leech: arity-4 shadow detects L(s, Delta_12) at Re(s) = 6."""
        data = LATTICE_DATA['Leech']
        arity_4 = [l for l in data['critical_lines'] if 'Delta_12' in l['source']]
        assert len(arity_4) == 1
        assert arity_4[0]['position'] == Fraction(6, 1)

    def test_Z2_depth_2_dedekind(self):
        """comp:period-shadow-rank2: Z^2 depth 2, Dedekind zeta."""
        data = LATTICE_DATA['Z2']
        assert data['depth'] == 2
        assert 'zeta_{Q(i)}' in data['critical_lines'][0]['source']

    def test_depth_from_rank_formula(self):
        """eq:depth-from-rank: d <= 1 + 2 + dim S_{r/2}."""
        for rank in range(8, 97, 8):
            k = rank // 2
            d = lattice_depth(rank)
            g_k = cusp_form_dim_sl2z(k)
            assert d <= 1 + 2 + g_k

    def test_spectral_decomposition_d_3_plus_gk(self):
        """eq:depth-L-count: d(V_Lambda) = 3 + dim S_{r/2}."""
        for rank in range(8, 97, 8):
            k = rank // 2
            d = lattice_depth(rank)
            g_k = cusp_form_dim_sl2z(k)
            assert d == 3 + g_k

    def test_refined_inequality(self):
        """thm:refined-shadow-spectral: d >= 1 + #{critical lines}."""
        # Lattice: equality
        for rank in [8, 16, 24, 48]:
            d = lattice_depth(rank)
            n = lattice_critical_line_count(rank)
            assert d >= 1 + n
        # Betagamma: gap of 2
        bg = betagamma_critical_lines()
        assert bg['shadow_depth'] >= 1 + bg['critical_line_count']

    def test_rank_table_matches_manuscript(self):
        """Table in sec:higher-depths matches our computation."""
        manuscript_data = [
            (8, 4, 1, 0, 2, 3),
            (16, 8, 1, 0, 2, 3),
            (24, 12, 2, 1, 3, 4),
            (32, 16, 2, 1, 3, 4),
            (48, 24, 3, 2, 4, 5),
            (72, 36, 4, 3, 5, 6),
            (96, 48, 5, 4, 6, 7),
        ]
        for rank, k, dim_M, dim_S, max_lines, max_depth in manuscript_data:
            assert modular_form_dim_sl2z(k) == dim_M, \
                f"rank {rank}: dim M_{k} = {modular_form_dim_sl2z(k)} != {dim_M}"
            assert cusp_form_dim_sl2z(k) == dim_S, \
                f"rank {rank}: dim S_{k} = {cusp_form_dim_sl2z(k)} != {dim_S}"
            assert lattice_critical_line_count(rank) == max_lines
            assert lattice_depth(rank) == max_depth


# =========================================================================
# 13. Virasoro class M infinite depth
# =========================================================================

class TestVirasoroClassM:

    def test_generic_virasoro_class_M(self):
        """Generic Virasoro is class M with infinite depth."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(25)]:
            data = virasoro_critical_lines_generic(c_val)
            assert data['shadow_class'] == 'M'
            assert data['shadow_depth'] == float('inf')

    def test_generic_virasoro_1_critical_line(self):
        """Binary form -> 1 critical line position."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(13), Fraction(26)]:
            data = virasoro_critical_lines_generic(c_val)
            assert data['d_arith'] == 1
            assert len(data['critical_lines']) == 1
            assert data['critical_lines'][0]['position'] == Fraction(1, 2)


# =========================================================================
# 14. Complementarity and duality checks
# =========================================================================

class TestComplementarity:

    def test_kappa_complementarity_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(7, 10), Fraction(13)]:
            c_dual = 26 - c_val
            kappa = c_val / 2
            kappa_dual = c_dual / 2
            assert kappa + kappa_dual == Fraction(13), \
                f"c={c_val}: kappa+kappa'={kappa+kappa_dual} != 13"

    def test_c13_self_dual_kappa(self):
        """kappa(Vir_13) = kappa(Vir_{26-13}) = 13/2."""
        kappa = Fraction(13, 2)
        kappa_dual = Fraction(26 - 13, 2)
        assert kappa == kappa_dual

    def test_c26_kappa_sum(self):
        """kappa(Vir_26) + kappa(Vir_0) = 13 + 0 = 13."""
        c26 = virasoro_c26_analysis()
        assert c26['complementarity_sum'] == Fraction(13)


# =========================================================================
# 15. Minimal model central charges
# =========================================================================

class TestMinimalModelCharges:

    def test_ising_c(self):
        """M(3,4): c = 1/2."""
        assert minimal_model_c(3) == Fraction(1, 2)

    def test_tricritical_ising_c(self):
        """M(4,5): c = 7/10."""
        assert minimal_model_c(4) == Fraction(7, 10)

    def test_3state_potts_c(self):
        """M(5,6): c = 4/5."""
        assert minimal_model_c(5) == Fraction(4, 5)

    def test_c_approaches_1(self):
        """c(m) -> 1 as m -> infinity."""
        c_100 = minimal_model_c(100)
        assert float(c_100) > 0.999
        assert float(c_100) < 1


# =========================================================================
# 16. Ising model special case
# =========================================================================

class TestIsingModel:

    def test_ising_constrained_epstein(self):
        """Ising constrained Epstein: 2^{-s} + 4^s has zeros on Re(s) = 0.

        This is NOT on Re(s) = 1/2. The constrained Epstein of the partition
        function is a DIFFERENT object from the Koszul-Epstein of the shadow
        metric Q_L.
        """
        # The zeros: 2^{-s} + 4^s = 0 => 2^{-s} = -2^{2s}
        # => 2^{-3s} = -1 => s = -i*pi*(2k+1)/(3*log 2)
        # All on Re(s) = 0.
        import cmath
        for k in range(-5, 6):
            s = -1j * cmath.pi * (2*k + 1) / (3 * cmath.log(2))
            val = 2**(-s) + 4**s
            assert abs(val) < 1e-10, f"k={k}: |val|={abs(val)}"
            assert abs(s.real) < 1e-15, f"k={k}: Re(s) = {s.real}"

    def test_ising_dh_discriminant(self):
        """Ising: fundamental discriminant d_0 = -40, h = 2."""
        disc, d_0, h = virasoro_dh_discriminant(Fraction(1, 2))
        assert d_0 == -40
        assert h == 2


# =========================================================================
# Run tests with pytest
# =========================================================================

if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v', '--tb=short', '-x'])
