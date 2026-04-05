"""Tests for non-simply-laced shadow obstruction tower data: B_2, C_2, G_2, F_4.

Verifies all shadow obstruction tower formulas from first principles (AP1).
Every expected value is independently computed in the test, NOT imported
from the library under test (AP10).

Test categories:
    1. Kappa formulas (primary definition, verified against dim(g)*(k+h^v)/(2*h^v))
    2. Shadow class L assignment (S_3 != 0, S_4 = 0, Delta = 0, r_max = 3)
    3. r-matrix structure (simple pole)
    4. Complementarity (kappa + kappa' = 0 for all KM)
    5. Feigin-Frenkel involution properties
    6. Central charge formulas
    7. Cross-family consistency (B2=C2 isomorphism, additivity)
    8. Numerical spot-checks at specific levels
    9. h vs h^vee distinction
"""

import pytest
from sympy import Rational, Symbol, simplify, cancel, S

from compute.lib.non_simply_laced_shadows import (
    kappa_affine,
    central_charge_affine,
    ff_dual_level,
    lacing_number,
    shadow_data,
    b2_shadow,
    c2_shadow,
    g2_shadow,
    f4_shadow,
    all_nsl_shadows,
    verify_kappa_formula,
    verify_ff_involution,
    verify_complementarity,
    verify_shadow_class,
    verify_h_distinction,
    verify_all,
    cross_family_kappa_additivity,
    cross_family_b2_c2_coincidence,
    cross_family_simply_laced_comparison,
    kappa_table,
    central_charge_table,
    shadow_census,
)
from compute.lib.lie_algebra import cartan_data

k = Symbol('k')


# =========================================================================
# Independent ground truth (AP10: recomputed, not imported)
# =========================================================================

def _kappa_from_first_principles(dim_g, h_dual, level):
    """kappa = dim(g) * (k + h^vee) / (2 * h^vee), computed independently."""
    return Rational(dim_g) * (level + h_dual) / (2 * h_dual)


def _cc_from_first_principles(dim_g, h_dual, level):
    """c = dim(g) * k / (k + h^vee), computed independently."""
    return Rational(dim_g) * level / (level + h_dual)


def _ff_dual_from_first_principles(h_dual, level):
    """k' = -k - 2*h^vee, computed independently."""
    return -level - 2 * h_dual


# Ground truth table: independently verified against Kac, Table Aff 1-3
# Format: (type, rank, dim, h, h_dual, lacing, exponents)
GROUND_TRUTH = {
    'B2': ('B', 2, 10, 4, 3, 2, [1, 3]),
    'C2': ('C', 2, 10, 4, 3, 2, [1, 3]),
    'G2': ('G', 2, 14, 6, 4, 3, [1, 5]),
    'F4': ('F', 4, 52, 12, 9, 2, [1, 5, 7, 11]),
}


# =========================================================================
# 1. Lie algebra data verification
# =========================================================================

class TestLieAlgebraData:
    """Verify that cartan_data returns correct values for all NSL types."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_dim(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        data = cartan_data(type_, rank)
        assert data.dim == dim, f"{label}: dim should be {dim}, got {data.dim}"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_h(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        data = cartan_data(type_, rank)
        assert data.h == h, f"{label}: h should be {h}, got {data.h}"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_h_dual(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        data = cartan_data(type_, rank)
        assert data.h_dual == h_dual, f"{label}: h_dual should be {h_dual}, got {data.h_dual}"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_h_neq_h_dual(self, label, gt):
        """Non-simply-laced types must have h != h^vee."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        assert h != h_dual, f"{label}: h should differ from h_dual for NSL type"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_exponents(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        data = cartan_data(type_, rank)
        assert data.exponents == exponents, (
            f"{label}: exponents should be {exponents}, got {data.exponents}"
        )

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_lacing(self, label, gt):
        type_, rank, dim, h, h_dual, lacing_expected, exponents = gt
        assert lacing_number(type_, rank) == lacing_expected


# =========================================================================
# 2. Kappa formula tests
# =========================================================================

class TestKappaFormulas:
    """Verify kappa = dim(g) * (k + h^vee) / (2 * h^vee) for each type."""

    def test_kappa_b2(self):
        """B_2: kappa = 10(k+3)/6 = 5(k+3)/3."""
        kap = kappa_affine('B', 2, k)
        expected = _kappa_from_first_principles(10, 3, k)
        assert simplify(kap - expected) == 0
        # Check simplified form
        assert simplify(kap - Rational(5) * (k + 3) / 3) == 0

    def test_kappa_c2(self):
        """C_2: kappa = 10(k+3)/6 = 5(k+3)/3.

        NOTE: C_2 has h^vee = 3, NOT 2.  (C_n: h^vee = n+1.)
        The user's original claim h^vee = 2 was WRONG (AP1 violation).
        """
        kap = kappa_affine('C', 2, k)
        expected = _kappa_from_first_principles(10, 3, k)
        assert simplify(kap - expected) == 0
        # The WRONG formula would be 5(k+2)/2 -- verify it does NOT match
        wrong = Rational(5) * (k + 2) / 2
        assert simplify(kap - wrong) != 0

    def test_kappa_g2(self):
        """G_2: kappa = 14(k+4)/8 = 7(k+4)/4."""
        kap = kappa_affine('G', 2, k)
        expected = _kappa_from_first_principles(14, 4, k)
        assert simplify(kap - expected) == 0
        assert simplify(kap - Rational(7) * (k + 4) / 4) == 0

    def test_kappa_f4(self):
        """F_4: kappa = 52(k+9)/18 = 26(k+9)/9."""
        kap = kappa_affine('F', 4, k)
        expected = _kappa_from_first_principles(52, 9, k)
        assert simplify(kap - expected) == 0
        assert simplify(kap - Rational(26) * (k + 9) / 9) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_kappa_vanishes_at_critical(self, label, gt):
        """kappa(-h^vee) = 0 for all types."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        kap = kappa_affine(type_, rank, k)
        assert simplify(kap.subs(k, -h_dual)) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_kappa_at_level_zero(self, label, gt):
        """kappa(0) = dim(g)/2 for all types."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        kap = kappa_affine(type_, rank, k)
        assert simplify(kap.subs(k, 0) - Rational(dim, 2)) == 0


class TestKappaNumerical:
    """Numerical spot-checks for kappa at specific levels."""

    def test_b2_k1(self):
        """B_2 at k=1: kappa = 5*4/3 = 20/3."""
        assert kappa_affine('B', 2, 1) == Rational(20, 3)

    def test_c2_k1(self):
        """C_2 at k=1: kappa = 5*4/3 = 20/3 (same as B_2)."""
        assert kappa_affine('C', 2, 1) == Rational(20, 3)

    def test_g2_k1(self):
        """G_2 at k=1: kappa = 7*5/4 = 35/4."""
        assert kappa_affine('G', 2, 1) == Rational(35, 4)

    def test_f4_k1(self):
        """F_4 at k=1: kappa = 26*10/9 = 260/9."""
        assert kappa_affine('F', 4, 1) == Rational(260, 9)

    def test_b2_k2(self):
        """B_2 at k=2: kappa = 5*5/3 = 25/3."""
        assert kappa_affine('B', 2, 2) == Rational(25, 3)

    def test_g2_k3(self):
        """G_2 at k=3: kappa = 7*7/4 = 49/4."""
        assert kappa_affine('G', 2, 3) == Rational(49, 4)

    def test_f4_k2(self):
        """F_4 at k=2: kappa = 26*11/9 = 286/9."""
        assert kappa_affine('F', 4, 2) == Rational(286, 9)


# =========================================================================
# 3. Shadow class L tests
# =========================================================================

class TestShadowClassL:
    """Verify shadow class L assignment for all NSL affine KM algebras."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_class_is_L(self, label, gt):
        type_, rank = gt[0], gt[1]
        sd = shadow_data(type_, rank)
        assert sd.shadow_class == 'L'

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_depth_is_3(self, label, gt):
        type_, rank = gt[0], gt[1]
        sd = shadow_data(type_, rank)
        assert sd.shadow_depth == 3

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_S3_nonzero(self, label, gt):
        """Cubic shadow is nonzero (from Lie bracket)."""
        type_, rank = gt[0], gt[1]
        sd = shadow_data(type_, rank)
        assert sd.S3_nonzero is True

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_S4_zero(self, label, gt):
        """Quartic shadow vanishes on primary line (Jacobi identity)."""
        type_, rank = gt[0], gt[1]
        sd = shadow_data(type_, rank)
        assert sd.S4_zero is True

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_Delta_zero(self, label, gt):
        """Critical discriminant Delta = 0 (class L: perfect square Q_L)."""
        type_, rank = gt[0], gt[1]
        sd = shadow_data(type_, rank)
        assert simplify(sd.Delta) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_r_matrix_simple_pole(self, label, gt):
        """r-matrix has simple pole at z=0 (AP19)."""
        type_, rank = gt[0], gt[1]
        sd = shadow_data(type_, rank)
        assert sd.r_matrix_pole_order == 1


# =========================================================================
# 4. Complementarity tests (AP24)
# =========================================================================

class TestComplementarity:
    """Verify complementarity relations for KM algebras."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_kappa_anti_symmetry(self, label, gt):
        """kappa(k) + kappa(k') = 0 for all KM (AP24)."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        kap = kappa_affine(type_, rank, k)
        kd = ff_dual_level(type_, rank, k)
        kap_dual = kappa_affine(type_, rank, kd)
        assert simplify(kap + kap_dual) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_central_charge_complementarity(self, label, gt):
        """c(k) + c(k') = 2*dim(g) for all KM."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        cc = central_charge_affine(type_, rank, k)
        kd = ff_dual_level(type_, rank, k)
        cc_dual = central_charge_affine(type_, rank, kd)
        assert simplify(cancel(cc + cc_dual) - 2 * dim) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_shadow_data_complementarity_kappa(self, label, gt):
        """Shadow data stores correct complementarity sum for kappa."""
        type_, rank = gt[0], gt[1]
        sd = shadow_data(type_, rank)
        assert simplify(sd.complementarity_sum_kappa) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_shadow_data_complementarity_c(self, label, gt):
        """Shadow data stores correct complementarity sum for c."""
        type_, rank, dim = gt[0], gt[1], gt[2]
        sd = shadow_data(type_, rank)
        assert simplify(sd.complementarity_sum_c - 2 * dim) == 0

    def test_b2_complementarity_sum_c_is_20(self):
        """B_2: c + c' = 2*10 = 20."""
        sd = b2_shadow()
        assert simplify(sd.complementarity_sum_c - 20) == 0

    def test_g2_complementarity_sum_c_is_28(self):
        """G_2: c + c' = 2*14 = 28."""
        sd = g2_shadow()
        assert simplify(sd.complementarity_sum_c - 28) == 0

    def test_f4_complementarity_sum_c_is_104(self):
        """F_4: c + c' = 2*52 = 104."""
        sd = f4_shadow()
        assert simplify(sd.complementarity_sum_c - 104) == 0


# =========================================================================
# 5. Feigin-Frenkel involution tests
# =========================================================================

class TestFFInvolution:
    """Verify Feigin-Frenkel involution k -> -k - 2*h^vee."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_involution(self, label, gt):
        """(k')' = k for all types."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        kd = ff_dual_level(type_, rank, k)
        kdd = ff_dual_level(type_, rank, kd)
        assert simplify(kdd - k) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_critical_fixed_point(self, label, gt):
        """k = -h^vee is a fixed point of the involution."""
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        kd = ff_dual_level(type_, rank, -h_dual)
        assert simplify(kd + h_dual) == 0

    def test_b2_ff_dual(self):
        """B_2: k' = -k - 6."""
        assert simplify(ff_dual_level('B', 2, k) - (-k - 6)) == 0

    def test_c2_ff_dual(self):
        """C_2: k' = -k - 6 (same as B_2)."""
        assert simplify(ff_dual_level('C', 2, k) - (-k - 6)) == 0

    def test_g2_ff_dual(self):
        """G_2: k' = -k - 8."""
        assert simplify(ff_dual_level('G', 2, k) - (-k - 8)) == 0

    def test_f4_ff_dual(self):
        """F_4: k' = -k - 18."""
        assert simplify(ff_dual_level('F', 4, k) - (-k - 18)) == 0


# =========================================================================
# 6. Central charge tests
# =========================================================================

class TestCentralCharge:
    """Verify central charge c = dim(g) * k / (k + h^vee)."""

    def test_cc_b2(self):
        """B_2: c = 10k/(k+3)."""
        cc = central_charge_affine('B', 2, k)
        expected = Rational(10) * k / (k + 3)
        assert simplify(cc - expected) == 0

    def test_cc_c2(self):
        """C_2: c = 10k/(k+3) (same as B_2)."""
        cc = central_charge_affine('C', 2, k)
        expected = Rational(10) * k / (k + 3)
        assert simplify(cc - expected) == 0

    def test_cc_g2(self):
        """G_2: c = 14k/(k+4)."""
        cc = central_charge_affine('G', 2, k)
        expected = Rational(14) * k / (k + 4)
        assert simplify(cc - expected) == 0

    def test_cc_f4(self):
        """F_4: c = 52k/(k+9)."""
        cc = central_charge_affine('F', 4, k)
        expected = Rational(52) * k / (k + 9)
        assert simplify(cc - expected) == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_cc_at_level_zero(self, label, gt):
        """c(0) = 0 for all types."""
        type_, rank = gt[0], gt[1]
        cc = central_charge_affine(type_, rank, 0)
        assert cc == 0

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_cc_large_k_limit(self, label, gt):
        """As k -> infinity, c -> dim(g)."""
        type_, rank, dim = gt[0], gt[1], gt[2]
        cc = central_charge_affine(type_, rank, k)
        # At very large k, c ~ dim * k / k = dim
        cc_large = cc.subs(k, 10**6)
        assert abs(float(cc_large) - dim) < 0.001


# =========================================================================
# 7. Cross-family consistency tests (AP10)
# =========================================================================

class TestCrossFamily:
    """Cross-family consistency checks."""

    def test_b2_c2_isomorphism_kappa(self):
        """B_2 = C_2 as Lie algebras => same kappa."""
        kap_b2 = kappa_affine('B', 2, k)
        kap_c2 = kappa_affine('C', 2, k)
        assert simplify(kap_b2 - kap_c2) == 0

    def test_b2_c2_isomorphism_cc(self):
        """B_2 = C_2 as Lie algebras => same central charge."""
        cc_b2 = central_charge_affine('B', 2, k)
        cc_c2 = central_charge_affine('C', 2, k)
        assert simplify(cc_b2 - cc_c2) == 0

    def test_b2_c2_isomorphism_ff_dual(self):
        """B_2 = C_2 as Lie algebras => same FF dual level."""
        kd_b2 = ff_dual_level('B', 2, k)
        kd_c2 = ff_dual_level('C', 2, k)
        assert simplify(kd_b2 - kd_c2) == 0

    def test_b2_c2_isomorphism_shadow_data(self):
        """B_2 = C_2: full shadow data matches."""
        results = cross_family_b2_c2_coincidence()
        for name, ok in results.items():
            assert ok, f"B2=C2 check failed: {name}"

    def test_kappa_additivity(self):
        """kappa is additive on direct sums at specific levels."""
        results = cross_family_kappa_additivity()
        for name, ok in results.items():
            assert ok, f"additivity check failed: {name}"

    def test_all_nsl_are_class_L(self):
        """All NSL KM algebras are class L (like all KM)."""
        results = cross_family_simply_laced_comparison()
        for name, ok in results.items():
            assert ok, f"class comparison failed: {name}"


# =========================================================================
# 8. h vs h^vee distinction tests
# =========================================================================

class TestHDistinction:
    """Verify that h != h^vee for non-simply-laced, and formulas use the right one."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_h_neq_h_dual(self, label, gt):
        type_, rank, dim, h, h_dual, lacing, exponents = gt
        assert h != h_dual

    def test_b2_h_values(self):
        """B_2: h = 4, h^vee = 3."""
        sd = b2_shadow()
        assert sd.h == 4
        assert sd.h_dual == 3

    def test_c2_h_values(self):
        """C_2: h = 4, h^vee = 3."""
        sd = c2_shadow()
        assert sd.h == 4
        assert sd.h_dual == 3

    def test_g2_h_values(self):
        """G_2: h = 6, h^vee = 4."""
        sd = g2_shadow()
        assert sd.h == 6
        assert sd.h_dual == 4

    def test_f4_h_values(self):
        """F_4: h = 12, h^vee = 9."""
        sd = f4_shadow()
        assert sd.h == 12
        assert sd.h_dual == 9

    def test_kappa_uses_h_dual_not_h(self):
        """kappa formula uses h^vee, NOT h.

        For G_2: if you wrongly use h=6 instead of h^vee=4,
        you get kappa = 14(k+6)/12 = 7(k+6)/6, which is WRONG.
        The correct formula gives kappa = 7(k+4)/4.
        """
        kap_correct = kappa_affine('G', 2, k)
        kap_wrong = Rational(14) * (k + 6) / (2 * 6)  # using h instead of h^vee
        assert simplify(kap_correct - kap_wrong) != 0


# =========================================================================
# 9. Shadow data accessors
# =========================================================================

class TestShadowDataAccessors:
    """Test individual shadow data accessor functions."""

    def test_b2_shadow_label(self):
        assert b2_shadow().label == 'B2'

    def test_c2_shadow_label(self):
        assert c2_shadow().label == 'C2'

    def test_g2_shadow_label(self):
        assert g2_shadow().label == 'G2'

    def test_f4_shadow_label(self):
        assert f4_shadow().label == 'F4'

    def test_all_nsl_shadows_count(self):
        """There are exactly 4 non-simply-laced types."""
        shadows = all_nsl_shadows()
        assert len(shadows) == 4
        assert set(shadows.keys()) == {'B2', 'C2', 'G2', 'F4'}

    def test_shadow_census_rows(self):
        """Census produces 4 rows."""
        rows = shadow_census()
        assert len(rows) == 4

    def test_kappa_table_entries(self):
        """Kappa table has entries for all types and levels."""
        table = kappa_table([1, 5])
        assert len(table) == 4
        for label in ['B2', 'C2', 'G2', 'F4']:
            assert label in table
            assert 1 in table[label]
            assert 5 in table[label]

    def test_cc_table_entries(self):
        """Central charge table has entries for all types and levels."""
        table = central_charge_table([1])
        assert len(table) == 4


# =========================================================================
# 10. Verification suite tests
# =========================================================================

class TestVerificationSuite:
    """Test that all internal verification checks pass."""

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_kappa_verification(self, label, gt):
        type_, rank = gt[0], gt[1]
        results = verify_kappa_formula(type_, rank)
        for name, ok in results.items():
            assert ok, f"verification failed: {name}"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_ff_verification(self, label, gt):
        type_, rank = gt[0], gt[1]
        results = verify_ff_involution(type_, rank)
        for name, ok in results.items():
            assert ok, f"verification failed: {name}"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_complementarity_verification(self, label, gt):
        type_, rank = gt[0], gt[1]
        results = verify_complementarity(type_, rank)
        for name, ok in results.items():
            assert ok, f"verification failed: {name}"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_shadow_class_verification(self, label, gt):
        type_, rank = gt[0], gt[1]
        results = verify_shadow_class(type_, rank)
        for name, ok in results.items():
            assert ok, f"verification failed: {name}"

    @pytest.mark.parametrize("label,gt", list(GROUND_TRUTH.items()))
    def test_h_distinction_verification(self, label, gt):
        type_, rank = gt[0], gt[1]
        results = verify_h_distinction(type_, rank)
        for name, ok in results.items():
            assert ok, f"verification failed: {name}"

    def test_verify_all(self):
        """Full verification suite passes."""
        results = verify_all()
        failures = {name: ok for name, ok in results.items() if not ok}
        assert len(failures) == 0, f"Verification failures: {failures}"


# =========================================================================
# 11. Lacing number tests
# =========================================================================

class TestLacingNumber:
    """Verify lacing numbers."""

    def test_b2_lacing(self):
        """B_2: lacing number = 2 (double bond)."""
        assert lacing_number('B', 2) == 2

    def test_c2_lacing(self):
        """C_2: lacing number = 2 (double bond)."""
        assert lacing_number('C', 2) == 2

    def test_g2_lacing(self):
        """G_2: lacing number = 3 (triple bond)."""
        assert lacing_number('G', 2) == 3

    def test_f4_lacing(self):
        """F_4: lacing number = 2 (double bond on middle edge)."""
        assert lacing_number('F', 4) == 2


# =========================================================================
# 12. Kappa simplified string tests
# =========================================================================

class TestKappaSimplified:
    """Verify the human-readable kappa string."""

    def test_b2_kappa_str(self):
        assert b2_shadow().kappa_simplified == '5(k+3)/3'

    def test_c2_kappa_str(self):
        assert c2_shadow().kappa_simplified == '5(k+3)/3'

    def test_g2_kappa_str(self):
        assert g2_shadow().kappa_simplified == '7(k+4)/4'

    def test_f4_kappa_str(self):
        assert f4_shadow().kappa_simplified == '26(k+9)/9'


# =========================================================================
# 13. AP-specific regression tests
# =========================================================================

class TestAPRegressions:
    """Tests targeting specific anti-patterns from the manuscript's error history."""

    def test_ap1_no_formula_copy(self):
        """AP1: Each kappa is computed from its own (dim, h^vee), not copied.

        B_2 and C_2 happen to have the same kappa, but this must arise from
        the SAME (dim, h^vee) pair, not from copying B_2's formula to C_2.
        """
        data_b2 = cartan_data('B', 2)
        data_c2 = cartan_data('C', 2)
        # The coincidence arises because dim and h^vee are both the same
        assert data_b2.dim == data_c2.dim == 10
        assert data_b2.h_dual == data_c2.h_dual == 3

    def test_ap9_kappa_vs_c_distinction(self):
        """AP9: kappa(G_2, k) != c(G_2, k) in general.

        kappa = 7(k+4)/4, c = 14k/(k+4). These are different objects.
        """
        kap = kappa_affine('G', 2, k)
        cc = central_charge_affine('G', 2, k)
        assert simplify(kap - cc) != 0

    def test_ap19_r_matrix_pole_order(self):
        """AP19: r-matrix has pole at z^{-1}, not z^{-2}.

        The KM OPE has z^{-2} (central) and z^{-1} (bracket) poles.
        The r-matrix absorbs one power: pole at z^{-1} only.
        """
        for label, (type_, rank) in [('B2', ('B', 2)), ('G2', ('G', 2)),
                                      ('C2', ('C', 2)), ('F4', ('F', 4))]:
            sd = shadow_data(type_, rank)
            assert sd.r_matrix_pole_order == 1, (
                f"{label}: r-matrix should have simple pole (AP19)"
            )

    def test_ap24_km_anti_symmetry(self):
        """AP24: For KM, kappa + kappa' = 0 (not 13 like Virasoro).

        This is the clean anti-symmetric case. Verify at multiple levels.
        """
        for type_, rank in [('B', 2), ('C', 2), ('G', 2), ('F', 4)]:
            for level_val in [1, 2, 5, 10, 100]:
                kap = kappa_affine(type_, rank, level_val)
                kd = ff_dual_level(type_, rank, level_val)
                kap_dual = kappa_affine(type_, rank, kd)
                assert simplify(kap + kap_dual) == 0

    def test_c2_h_dual_is_3_not_2(self):
        """AP1 regression: C_2 has h^vee = 3, not 2.

        The standard table (Kac, Table Aff 1) gives:
            C_n: h = 2n, h^vee = n + 1
        So C_2: h = 4, h^vee = 3.

        The user's original specification claimed h^vee(C_2) = 2.
        This is wrong. C_n has h^vee = n+1 for n >= 2.
        """
        data = cartan_data('C', 2)
        assert data.h_dual == 3, "C_2 h^vee must be 3 (from Kac: C_n has h^vee = n+1)"
        assert data.h_dual != 2, "C_2 h^vee is NOT 2"

    def test_ap27_all_use_weight_1_propagator(self):
        """AP27: The bar propagator is d log E(z,w), weight 1 regardless of algebra.

        This test just confirms the structural claim: the r-matrix
        r(z) = Omega/z has weight 1 in each variable (from d log).
        """
        for label, (type_, rank) in [('B2', ('B', 2)), ('G2', ('G', 2)),
                                      ('C2', ('C', 2)), ('F4', ('F', 4))]:
            sd = shadow_data(type_, rank)
            # r-matrix pole order 1 is consistent with weight-1 propagator
            assert sd.r_matrix_pole_order == 1
