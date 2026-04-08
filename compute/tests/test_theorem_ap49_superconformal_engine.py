"""Tests for AP49 cross-volume superconformal family verification.

30+ tests covering:
  - N=0 Virasoro baseline
  - N=1 SVir: kappa, complementarity, decomposition, multi-path
  - N=2 SCA: cross-volume fix verification, coset decomposition
  - N=4 small SCA: cross-volume fix verification, two dualities
  - BP W(sl_3, f_min): kappa, anomaly ratio, Koszul conductor,
    intra-file contradiction detection, collapsing level
  - Superconformal hierarchy: decreasing comp sums, AP48 checks
"""

from fractions import Fraction
import pytest

from compute.lib.theorem_ap49_superconformal_engine import (
    # N=0
    kappa_vir, vir_koszul_dual_c, vir_comp_sum,
    # N=1
    kappa_svir, svir_koszul_dual_c, svir_comp_sum,
    svir_kappa_decomposition, multipath_svir,
    # N=2
    n2_central_charge, n2_level_from_c, kappa_n2_from_c, kappa_n2_from_level,
    n2_koszul_dual_c, n2_comp_sum, n2_coset_decomposition,
    # N=4
    n4_central_charge, kappa_n4_from_level, kappa_n4_from_c,
    n4_koszul_dual_c, n4_comp_sum_ff, n4_comp_sum_cy,
    # BP
    bp_central_charge, bp_varrho, bp_varrho_unsigned, kappa_bp,
    kappa_bp_t_line, bp_ff_dual_level, bp_koszul_conductor,
    bp_comp_sum, bp_comp_sum_t_line,
    bp_wrong_central_charge, bp_wrong_koszul_conductor,
    # Hierarchy
    superconformal_hierarchy, hierarchy_comp_sums_decreasing,
    # Cross-volume
    check_n2_cross_volume, check_n4_cross_volume,
    check_bp_intra_file_contradiction, check_bp_collapsing_level,
    check_bp_anomaly_ratio, ap48_kappa_not_c_over_2,
    multipath_bp,
)

F = Fraction


# =====================================================================
# N=0 Virasoro (baseline)
# =====================================================================

class TestVirasoro:
    def test_kappa_vir_basic(self):
        assert kappa_vir(F(0)) == 0
        assert kappa_vir(F(26)) == 13
        assert kappa_vir(F(13)) == F(13, 2)

    def test_vir_koszul_involution(self):
        assert vir_koszul_dual_c(F(0)) == 26
        assert vir_koszul_dual_c(F(13)) == 13  # self-dual

    def test_vir_comp_sum(self):
        for c_val in [0, 1, 5, 13, 24]:
            assert vir_comp_sum(F(c_val)) == 13


# =====================================================================
# N=1 SVir
# =====================================================================

class TestSVir:
    def test_kappa_svir_formula(self):
        """kappa(SVir_c) = (3c-2)/4."""
        assert kappa_svir(F(0)) == F(-1, 2)
        assert kappa_svir(F(15)) == F(43, 4)
        assert kappa_svir(F(15, 2)) == F(41, 8)
        # Vanishes at c = 2/3
        assert kappa_svir(F(2, 3)) == 0

    def test_svir_koszul_involution(self):
        """c -> 15 - c, self-dual at c = 15/2."""
        assert svir_koszul_dual_c(F(0)) == 15
        assert svir_koszul_dual_c(F(15, 2)) == F(15, 2)
        assert svir_koszul_dual_c(F(15)) == 0

    def test_svir_comp_sum_constant(self):
        """kappa(c) + kappa(15-c) = 41/4 for all c."""
        for c_val in [0, 1, F(2, 3), F(15, 2), 7, F(43, 7)]:
            assert svir_comp_sum(c_val) == F(41, 4)

    def test_svir_decomposition(self):
        """kappa = kappa_bos + kappa_ferm = c/2 + (c-2)/4."""
        for c_val in [0, 1, F(15, 2), 15]:
            d = svir_kappa_decomposition(F(c_val))
            assert d['matches_formula']
            assert d['kappa_bos'] == F(c_val) / 2
            assert d['kappa_ferm'] == (F(c_val) - 2) / 4

    def test_svir_multipath(self):
        """Multi-path verification at several central charges."""
        for c_val in [0, 1, F(2, 3), 5, F(15, 2)]:
            mp = multipath_svir(F(c_val))
            assert mp['paths_agree']
            assert mp['comp_is_41_4']

    def test_svir_not_c_over_2(self):
        """kappa(SVir) != c/2 generically (AP48)."""
        c = F(15, 2)
        assert kappa_svir(c) != c / 2
        # kappa = 41/8, c/2 = 15/4. These differ.
        assert kappa_svir(c) == F(41, 8)
        assert c / 2 == F(15, 4)


# =====================================================================
# N=2 SCA (fix verification)
# =====================================================================

class TestN2SCA:
    def test_n2_central_charge(self):
        assert n2_central_charge(F(1)) == 1
        assert n2_central_charge(F(2)) == F(3, 2)

    def test_kappa_n2_two_forms(self):
        """(6-c)/(2(3-c)) = (k+4)/4 for c = 3k/(k+2)."""
        for k_val in [1, 2, 3, 5, 10]:
            k = F(k_val)
            c = n2_central_charge(k)
            assert kappa_n2_from_c(c) == kappa_n2_from_level(k)

    def test_n2_coset_decomposition(self):
        """Kazama-Suzuki coset gives (k+4)/4."""
        for k_val in [1, 2, 5]:
            d = n2_coset_decomposition(F(k_val))
            assert d['matches_formula']

    def test_n2_comp_sum_is_one(self):
        """kappa(c) + kappa(6-c) = 1 for all c != 3."""
        for c_val in [0, 1, 2, F(1, 2), F(5, 2)]:
            assert n2_comp_sum(F(c_val)) == 1

    def test_n2_cross_volume_fix(self):
        """Verify the N=2 AP49 fix: kappa != c/2."""
        result = check_n2_cross_volume()
        assert result['all_agree']
        assert result['correctly_differs_from_virasoro']
        # At c=1: kappa = 5/4, NOT 1/2
        assert result['kappa_from_c'] == F(5, 4)

    def test_n2_self_dual_is_pole(self):
        """Self-dual point c=3 is the free-field limit (pole of kappa)."""
        with pytest.raises(ValueError):
            kappa_n2_from_c(F(3))


# =====================================================================
# N=4 small SCA (fix verification)
# =====================================================================

class TestN4Small:
    def test_kappa_n4_basic(self):
        """kappa = 2k = c/3."""
        assert kappa_n4_from_level(F(1)) == 2
        assert kappa_n4_from_c(F(6)) == 2
        assert kappa_n4_from_level(F(1)) == kappa_n4_from_c(n4_central_charge(F(1)))

    def test_n4_not_c_over_2(self):
        """kappa = c/3, NOT c/2 (AP48)."""
        c = F(6)
        assert kappa_n4_from_c(c) == 2
        assert c / 2 == 3
        assert kappa_n4_from_c(c) != c / 2

    def test_n4_ff_duality(self):
        """FF involution: c -> -c-24, comp sum = -8."""
        assert n4_koszul_dual_c(F(6)) == -30
        assert n4_koszul_dual_c(F(-12)) == -12  # self-dual
        for c_val in [6, 12, -6, 24]:
            assert n4_comp_sum_ff(F(c_val)) == -8

    def test_n4_cy_duality(self):
        """CY sigma-model duality: k -> -k, comp sum = 0."""
        for k_val in [1, 2, 3]:
            assert n4_comp_sum_cy(F(k_val)) == 0

    def test_n4_cross_volume_fix(self):
        """Verify the N=4 AP49 fix: kappa = c/3, duality c -> -c-24."""
        result = check_n4_cross_volume()
        assert result['agree']
        assert result['correctly_differs']
        assert result['kappa_from_k'] == 2
        assert result['correct_dual_c'] == -30
        assert result['correct_dual_c'] != result['wrong_dual_c']

    def test_n4_two_dualities_differ(self):
        """FF duality and CY duality give DIFFERENT comp sums."""
        assert n4_comp_sum_ff(F(6)) == -8
        assert n4_comp_sum_cy(F(1)) == 0
        # These are different dualities, not a contradiction


# =====================================================================
# Bershadsky-Polyakov
# =====================================================================

class TestBP:
    def test_bp_central_charge_collapsing(self):
        """At k=-1 (collapsing level), c = 2 = dim(g_0^f)."""
        assert bp_central_charge(F(-1)) == 2

    def test_bp_central_charge_pole(self):
        """Pole at k=-3 (critical level)."""
        with pytest.raises(ValueError):
            bp_central_charge(F(-3))

    def test_bp_varrho_signed(self):
        """Signed anomaly ratio = 1/6."""
        assert bp_varrho() == F(1, 6)

    def test_bp_varrho_unsigned_wrong(self):
        """The unsigned formula gives 17/12, which is WRONG."""
        assert bp_varrho_unsigned() == F(17, 12)
        assert bp_varrho() != bp_varrho_unsigned()

    def test_bp_anomaly_ratio_computation(self):
        """Verify the signed anomaly ratio from generators."""
        result = check_bp_anomaly_ratio()
        assert result['signed_is_1_6']
        assert result['unsigned_is_17_12']
        assert result['they_differ']

    def test_kappa_bp_is_c_over_6(self):
        """kappa(BP) = c/6, NOT c/2."""
        for k_val in [0, 1, 2, -1, -2]:
            k = F(k_val)
            if k == -3:
                continue
            c = bp_central_charge(k)
            assert kappa_bp(k) == c / 6

    def test_kappa_bp_differs_from_t_line(self):
        """kappa(BP) != kappa_T(BP) = c/2 for the full algebra."""
        k = F(1)
        assert kappa_bp(k) != kappa_bp_t_line(k)
        assert kappa_bp(k) == bp_central_charge(k) / 6
        assert kappa_bp_t_line(k) == bp_central_charge(k) / 2

    def test_bp_koszul_conductor_196(self):
        """K_BP = 196 at ALL levels (FKR convention)."""
        for k_val in [0, 1, 2, 5, -1, -2, 10, -5]:
            k = F(k_val)
            assert bp_koszul_conductor(k) == 196

    def test_bp_comp_sum_full(self):
        """Full algebra: kappa + kappa' = varrho * K = 98/3."""
        for k_val in [0, 1, 2, 5]:
            assert bp_comp_sum(F(k_val)) == F(98, 3)

    def test_bp_comp_sum_t_line(self):
        """T-line: kappa_T + kappa_T' = K/2 = 98."""
        for k_val in [0, 1, 2, 5]:
            assert bp_comp_sum_t_line(F(k_val)) == 98

    def test_bp_wrong_formula_gives_76(self):
        """The WRONG formula gives K=76 (detecting the error)."""
        for k_val in [0, 1, 2, 5, -1]:
            assert bp_wrong_koszul_conductor(F(k_val)) == 76

    def test_bp_wrong_formula_wrong_at_collapsing(self):
        """The wrong formula gives c=1/2 at k=-1 instead of 2."""
        result = check_bp_collapsing_level()
        assert result['correct_is_2']
        assert result['wrong_is_half']

    def test_bp_intra_file_contradiction(self):
        """Detect the K=196 vs K=76 contradiction in the same file."""
        results = check_bp_intra_file_contradiction()
        for key, data in results.items():
            assert data['correct_is_196'], f"K != 196 at {key}"
            assert data['wrong_is_76'], f"Wrong K != 76 at {key}"

    def test_bp_multipath(self):
        """Multi-path verification of BP kappa."""
        for k_val in [0, 1, 2, 5]:
            mp = multipath_bp(F(k_val))
            assert mp['kappa_equals_c_6']
            assert mp['K_is_196']
            assert mp['comp_is_98_3']


# =====================================================================
# Superconformal hierarchy
# =====================================================================

class TestHierarchy:
    def test_comp_sums_decreasing(self):
        """13 > 41/4 > 1 > -8."""
        assert hierarchy_comp_sums_decreasing()

    def test_all_w_type(self):
        """All superconformal families have nonzero comp sum (W-type)."""
        h = superconformal_hierarchy()
        for name, data in h.items():
            assert data['comp_sum'] != 0, f"{name} has zero comp sum"

    def test_self_dual_points(self):
        """Verify self-dual central charges."""
        h = superconformal_hierarchy()
        assert h['N0_Vir']['self_dual_c'] == 13
        assert h['N1_SVir']['self_dual_c'] == F(15, 2)
        assert h['N2_SCA']['self_dual_c'] == 3
        assert h['N4_small']['self_dual_c'] == -12

    def test_kappa_at_self_dual(self):
        """kappa at self-dual point."""
        assert kappa_vir(F(13)) == F(13, 2)
        assert kappa_svir(F(15, 2)) == F(41, 8)
        # N=2 at c=3 is a pole
        assert kappa_n4_from_c(F(-12)) == -4

    def test_ap48_systematic(self):
        """kappa != c/2 for ALL non-Virasoro superconformal families."""
        results = ap48_kappa_not_c_over_2()
        for name, data in results.items():
            assert data['differs'], f"AP48 violation: {name} has kappa = c/2"


# =====================================================================
# Consistency across hierarchy
# =====================================================================

class TestConsistency:
    def test_comp_sum_values(self):
        """Verify exact complementarity sum values."""
        h = superconformal_hierarchy()
        for name, data in h.items():
            kfn = data['kappa_fn']
            dfn = data['dual_c_fn']
            sd = data['self_dual_c']
            expected = data['comp_sum']
            # Check at self-dual point (if not a pole)
            if name == 'N2_SCA':
                # c=3 is a pole; check at c=1 instead
                actual = kfn(F(1)) + kfn(dfn(F(1)))
            else:
                actual = kfn(sd) + kfn(dfn(sd))
            assert actual == expected, (
                f"{name}: comp sum {actual} != expected {expected}"
            )

    def test_koszul_involution_is_involution(self):
        """c'' = c for all families (involution property)."""
        assert vir_koszul_dual_c(vir_koszul_dual_c(F(5))) == 5
        assert svir_koszul_dual_c(svir_koszul_dual_c(F(3))) == 3
        assert n2_koszul_dual_c(n2_koszul_dual_c(F(1))) == 1
        assert n4_koszul_dual_c(n4_koszul_dual_c(F(6))) == 6

    def test_bp_ff_involution(self):
        """k'' = k for BP (FF involution is involution)."""
        assert bp_ff_dual_level(bp_ff_dual_level(F(1))) == 1
        assert bp_ff_dual_level(bp_ff_dual_level(F(0))) == 0
        assert bp_ff_dual_level(bp_ff_dual_level(F(-2))) == -2


# =====================================================================
# Cross-family and cross-method verification (AP10 cross-checks)
# =====================================================================

class TestCrossChecks:
    """Cross-checks that verify consistency ACROSS families and methods,
    not just hardcoded values.  These catch AP10-type errors where both
    the formula and the expected value could be independently wrong."""

    def test_comp_sum_level_independence(self):
        """For each family, the comp sum is the SAME at 5+ values of c/k.

        If both formula and test hardcode the same wrong constant, this
        test catches it by verifying the sum is constant across many points.
        """
        # N=0: comp sum at 5 different c values must all agree
        vir_sums = {vir_comp_sum(F(c)) for c in [0, 1, 5, 13, 25]}
        assert len(vir_sums) == 1, f"Vir comp sum not constant: {vir_sums}"

        # N=1: comp sum at 5 different c values
        svir_sums = {svir_comp_sum(F(c)) for c in [0, 1, F(2, 3), 7, F(15, 2)]}
        assert len(svir_sums) == 1, f"SVir comp sum not constant: {svir_sums}"

        # N=2: comp sum at 4 different c values (avoiding c=3 pole)
        n2_sums = {n2_comp_sum(F(c)) for c in [0, 1, 2, F(1, 2)]}
        assert len(n2_sums) == 1, f"N=2 comp sum not constant: {n2_sums}"

        # N=4: comp sum at 4 different c values
        n4_sums = {n4_comp_sum_ff(F(c)) for c in [6, 12, -6, 24]}
        assert len(n4_sums) == 1, f"N=4 comp sum not constant: {n4_sums}"

        # BP: Koszul conductor at 6 different levels
        bp_Ks = {bp_koszul_conductor(F(k)) for k in [0, 1, 2, 5, -1, -2]}
        assert len(bp_Ks) == 1, f"BP K not constant: {bp_Ks}"

    def test_hierarchy_strict_ordering(self):
        """The comp sums 13 > 41/4 > 1 > -8 are verified by computing
        each from its own formula, not from a shared table."""
        s0 = vir_comp_sum(F(1))       # computed from kappa_vir
        s1 = svir_comp_sum(F(1))      # computed from kappa_svir
        s2 = n2_comp_sum(F(1))        # computed from kappa_n2_from_c
        s4 = n4_comp_sum_ff(F(6))     # computed from kappa_n4_from_c
        assert s0 > s1 > s2 > s4

    def test_n2_three_path_agreement(self):
        """N=2 kappa via three independent routes at 4 levels."""
        for k_val in [1, 2, 5, 10]:
            k = F(k_val)
            c = n2_central_charge(k)
            path_c = kappa_n2_from_c(c)
            path_k = kappa_n2_from_level(k)
            path_coset = n2_coset_decomposition(k)['total']
            assert path_c == path_k == path_coset, (
                f"N=2 paths disagree at k={k}: {path_c}, {path_k}, {path_coset}"
            )

    def test_bp_kappa_vs_t_line_ratio(self):
        """kappa(BP)/kappa_T(BP) = varrho/(1/2) = (1/6)/(1/2) = 1/3.

        Cross-check: the ratio of the full kappa to the T-line kappa
        must equal the anomaly ratio divided by the Virasoro anomaly ratio.
        """
        for k_val in [0, 1, 2, 5]:
            k = F(k_val)
            ratio = kappa_bp(k) / kappa_bp_t_line(k)
            expected = bp_varrho() / F(1, 2)
            assert ratio == expected == F(1, 3), (
                f"BP kappa ratio wrong at k={k}: {ratio}"
            )

    def test_n4_two_dualities_consistency(self):
        """At k=1, the FF and CY dualities give different kappa' values.

        FF: kappa' = 2(-k-4) = -10.
        CY: kappa' = 2(-k) = -2.
        These are different objects; the test verifies they are both
        computed correctly and differ as expected.
        """
        k = F(1)
        kappa_ff_dual = kappa_n4_from_level(bp_ff_dual_level(k))
        # N=4 FF dual: k' = -k-4 (h^v(su2)=2), so k'=-5, kappa'=2*(-5)=-10
        kappa_ff = kappa_n4_from_level(-k - 4)
        kappa_cy = kappa_n4_from_level(-k)
        assert kappa_ff == -10
        assert kappa_cy == -2
        assert kappa_ff != kappa_cy

    def test_svir_kappa_zero_vs_vir_kappa_zero(self):
        """SVir kappa vanishes at c=2/3; Vir kappa vanishes at c=0.

        These are DIFFERENT zero points.  Cross-checks that the formulas
        are genuinely different, not off by a constant.
        """
        assert kappa_svir(F(2, 3)) == 0
        assert kappa_vir(F(0)) == 0
        # SVir at c=0 is nonzero
        assert kappa_svir(F(0)) == F(-1, 2)
        # Vir at c=2/3 is nonzero
        assert kappa_vir(F(2, 3)) == F(1, 3)

    def test_comp_sum_signs(self):
        """The comp sums have definite signs: +, +, +, -.

        N=0: 13 > 0, N=1: 41/4 > 0, N=2: 1 > 0, N=4: -8 < 0.
        The sign change occurs between N=2 and N=4.
        """
        assert vir_comp_sum(F(1)) > 0
        assert svir_comp_sum(F(1)) > 0
        assert n2_comp_sum(F(1)) > 0
        assert n4_comp_sum_ff(F(6)) < 0

    def test_bp_wrong_vs_correct_diverge(self):
        """The wrong and correct BP central charges diverge at ALL levels.

        Cross-check: they agree at k=-1 is NOT true (correct gives 2,
        wrong gives 1/2), so they disagree everywhere.
        """
        for k_val in [-2, -1, 0, 1, 2, 5]:
            k = F(k_val)
            c_good = bp_central_charge(k)
            c_bad = bp_wrong_central_charge(k)
            assert c_good != c_bad, f"Formulas agree at k={k}: {c_good}"

    def test_all_involutions_are_involutions(self):
        """Every Koszul involution satisfies f(f(x)) = x.

        Cross-check across all 5 families at 3+ points each.
        """
        for c_val in [0, 1, 5, 13]:
            c = F(c_val)
            assert vir_koszul_dual_c(vir_koszul_dual_c(c)) == c
            assert svir_koszul_dual_c(svir_koszul_dual_c(c)) == c
            assert n4_koszul_dual_c(n4_koszul_dual_c(c)) == c
        for c_val in [0, 1, 2]:
            c = F(c_val)
            assert n2_koszul_dual_c(n2_koszul_dual_c(c)) == c
        for k_val in [0, 1, 2, -2]:
            k = F(k_val)
            assert bp_ff_dual_level(bp_ff_dual_level(k)) == k
