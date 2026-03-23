r"""Tests for polyakov_effective_action: Polyakov effective action decomposition,
ghost central charges, Koszul duality, anomaly cancellation, Liouville
parametrization, shadow tower depth, and discriminant complementarity.

Ground truth:
  theorem_c_complementarity.py (kappa formulas, FF duality)
  shadow_metric_census.py (G/L/C/M classification)
  shadow_connection.py (discriminant, complementarity)
  concordance.tex (MC5, BRST, Polyakov)

GRADING: Cohomological, |d| = +1.
"""

import pytest
from sympy import Rational

from compute.lib.polyakov_effective_action import (
    anomaly_polynomial,
    brst_anomaly,
    depth_from_anomaly_polynomial,
    discriminant_complementarity,
    discriminant_complementarity_numerator,
    effective_action_components,
    ghost_central_charge,
    kappa,
    kappa_complementarity_sum,
    kappa_functional_equation,
    koszul_dual_central_charge,
    liouville_data,
    non_critical_curvature,
    quartic_contact,
    shadow_class,
    shadow_gf_functional_equation,
    total_anomaly_cancellation,
    virasoro_discriminant,
)


# ======================================================================
# 1. Ghost central charges
# ======================================================================

class TestGhostCentralCharge:
    """c_bc = -26, c_{betagamma} = 11."""

    def test_bc_ghost(self):
        assert ghost_central_charge("bc") == Rational(-26)

    def test_betagamma_ghost(self):
        assert ghost_central_charge("betagamma") == Rational(11)

    def test_bg_alias(self):
        assert ghost_central_charge("bg") == Rational(11)

    def test_unknown_raises(self):
        with pytest.raises(ValueError):
            ghost_central_charge("unknown")


# ======================================================================
# 2. Kappa (modular characteristic) for standard families
# ======================================================================

class TestKappa:
    """S_eff^{(2)} = kappa for all families."""

    def test_heisenberg_k1(self):
        assert kappa("heisenberg", k=1) == Rational(1)

    def test_heisenberg_k3(self):
        assert kappa("heisenberg", k=3) == Rational(3)

    def test_virasoro_c1(self):
        assert kappa("virasoro", c=1) == Rational(1, 2)

    def test_virasoro_c26(self):
        assert kappa("virasoro", c=26) == Rational(13)

    def test_virasoro_c13_selfdual(self):
        assert kappa("virasoro", c=13) == Rational(13, 2)

    def test_affine_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        assert kappa("affine", N=2, k=1) == Rational(9, 4)

    def test_affine_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        assert kappa("affine", N=3, k=1) == Rational(16, 3)

    def test_w3_c2(self):
        assert kappa("w3", c=2) == Rational(5, 3)

    def test_w3_c50_selfdual(self):
        """W_3 self-dual at c = 50."""
        assert kappa("w3", c=50) == Rational(125, 3)

    def test_lattice_rank1(self):
        assert kappa("lattice", rank=1) == Rational(1)

    def test_lattice_rank24(self):
        """Leech lattice: rank 24."""
        assert kappa("lattice", rank=24) == Rational(24)

    def test_betagamma_lam1(self):
        """Standard betagamma (lam=1): c=2, kappa=1."""
        assert kappa("betagamma", lam=1) == Rational(1)

    def test_betagamma_c2(self):
        assert kappa("betagamma", c=2) == Rational(1)


# ======================================================================
# 3. Koszul dual central charge
# ======================================================================

class TestKoszulDualCentralCharge:
    """Koszul duality: c + c' = 26 for Virasoro, 100 for W_3."""

    def test_virasoro_c1(self):
        c_dual = koszul_dual_central_charge("virasoro", c=1)
        assert c_dual == Rational(25)

    def test_virasoro_c26(self):
        c_dual = koszul_dual_central_charge("virasoro", c=26)
        assert c_dual == Rational(0)

    def test_virasoro_c13_selfdual(self):
        c_dual = koszul_dual_central_charge("virasoro", c=13)
        assert c_dual == Rational(13)

    def test_virasoro_sum_26(self):
        """c + c' = 26 for all c."""
        for c_val in [1, 2, Rational(1, 2), 13, 25, 26]:
            c_dual = koszul_dual_central_charge("virasoro", c=c_val)
            assert Rational(c_val) + c_dual == Rational(26)

    def test_w3_c2(self):
        c_dual = koszul_dual_central_charge("w3", c=2)
        assert c_dual == Rational(98)

    def test_w3_sum_100(self):
        """c + c' = 100 for W_3."""
        for c_val in [2, 50, 98, Rational(4, 5)]:
            c_dual = koszul_dual_central_charge("w3", c=c_val)
            assert Rational(c_val) + c_dual == Rational(100)

    def test_heisenberg_dual_sign(self):
        """Heis_k^! = Heis_{-k}."""
        c_dual = koszul_dual_central_charge("heisenberg", k=3)
        assert c_dual == Rational(-3)


# ======================================================================
# 4. Total anomaly cancellation
# ======================================================================

class TestAnomalyCancellation:
    """c_matter + c_Liouville + c_ghost = 0 for all c."""

    def test_cancellation_c1(self):
        assert total_anomaly_cancellation(1) == Rational(0)

    def test_cancellation_c26(self):
        assert total_anomaly_cancellation(26) == Rational(0)

    def test_cancellation_c_half(self):
        assert total_anomaly_cancellation(Rational(1, 2)) == Rational(0)

    def test_cancellation_c_negative(self):
        assert total_anomaly_cancellation(-10) == Rational(0)

    def test_cancellation_c_large(self):
        assert total_anomaly_cancellation(1000) == Rational(0)


# ======================================================================
# 5. BRST anomaly
# ======================================================================

class TestBRSTAnomaly:
    """Q^2_BRST = 0 iff c = 26."""

    def test_brst_zero_at_26(self):
        assert brst_anomaly(26) == Rational(0)

    def test_brst_nonzero_at_1(self):
        assert brst_anomaly(1) == Rational(-25)

    def test_brst_nonzero_at_25(self):
        assert brst_anomaly(25) == Rational(-1)

    def test_brst_nonzero_at_0(self):
        assert brst_anomaly(0) == Rational(-26)

    def test_brst_positive_at_27(self):
        assert brst_anomaly(27) == Rational(1)


# ======================================================================
# 6. Liouville data
# ======================================================================

class TestLiouvilleData:
    """Liouville parametrization: c = 1 + 6Q^2, Q = b + 1/b."""

    def test_anomaly_sum_zero(self):
        """c + c_L + c_ghost = 0 for all c."""
        for c_val in [1, 6, 13, 25, 26, Rational(1, 2)]:
            data = liouville_data(c_val)
            assert data["anomaly_sum"] == Rational(0)

    def test_c_L_equals_26_minus_c(self):
        for c_val in [1, 13, 25]:
            data = liouville_data(c_val)
            assert data["c_L"] == Rational(26) - Rational(c_val)

    def test_Q_squared_at_c1(self):
        """c = 1 => Q^2 = 0 => Q = 0 => b = i."""
        data = liouville_data(1)
        assert data["Q_squared"] == Rational(0)

    def test_Q_squared_at_c25(self):
        """c = 25 => Q^2 = 24/6 = 4."""
        data = liouville_data(25)
        assert data["Q_squared"] == Rational(4)

    def test_Q_squared_at_c13(self):
        """c = 13 => Q^2 = 12/6 = 2."""
        data = liouville_data(13)
        assert data["Q_squared"] == Rational(2)

    def test_kappa_matter(self):
        data = liouville_data(10)
        assert data["kappa_matter"] == Rational(5)

    def test_kappa_liouville(self):
        data = liouville_data(10)
        assert data["kappa_Liouville"] == Rational(8)

    def test_ghost_charge(self):
        data = liouville_data(10)
        assert data["c_ghost"] == Rational(-26)


# ======================================================================
# 7. Quartic contact invariant
# ======================================================================

class TestQuarticContact:
    """Q^contact for standard families."""

    def test_heisenberg_zero(self):
        """Gaussian class: Q^contact = 0."""
        assert quartic_contact("heisenberg", k=1) == Rational(0)

    def test_virasoro_c1(self):
        """Q^contact_Vir(c=1) = 10/(1*27) = 10/27."""
        assert quartic_contact("virasoro", c=1) == Rational(10, 27)

    def test_virasoro_c_half(self):
        """Q^contact_Vir(c=1/2) = 10/((1/2)*(5/2+22)) = 10/(1/2*49/2) = 10*4/49 = 40/49."""
        c_val = Rational(1, 2)
        expected = Rational(10) / (c_val * (5 * c_val + 22))
        assert quartic_contact("virasoro", c=Rational(1, 2)) == expected

    def test_virasoro_c25(self):
        """Q^contact_Vir(c=25) = 10/(25*147) = 10/3675 = 2/735."""
        expected = Rational(10) / (25 * 147)
        assert quartic_contact("virasoro", c=25) == expected

    def test_virasoro_c26(self):
        """Q^contact_Vir(c=26) = 10/(26*152) = 10/3952 = 5/1976."""
        expected = Rational(10) / (26 * 152)
        assert quartic_contact("virasoro", c=26) == expected

    def test_affine_quartic_zero(self):
        """Lie class: quartic contact = 0."""
        assert quartic_contact("affine", N=2, k=1) == Rational(0)

    def test_lattice_quartic_zero(self):
        """Lattice (Gaussian class): quartic = 0."""
        assert quartic_contact("lattice", rank=1) == Rational(0)

    def test_betagamma_nonzero(self):
        """Contact class: quartic is nonzero."""
        q = quartic_contact("betagamma", lam=1)
        assert q != Rational(0)


# ======================================================================
# 8. Discriminant complementarity
# ======================================================================

class TestDiscriminantComplementarity:
    """Delta(c) + Delta(26-c) has constant numerator 6960."""

    def test_numerator_6960(self):
        assert discriminant_complementarity_numerator(1) == Rational(6960)

    def test_virasoro_discriminant_c1(self):
        """Delta(1) = 40/(5+22) = 40/27."""
        assert virasoro_discriminant(1) == Rational(40, 27)

    def test_virasoro_discriminant_c13(self):
        """Delta(13) = 40/(65+22) = 40/87."""
        assert virasoro_discriminant(13) == Rational(40, 87)

    def test_complementarity_c1(self):
        """Delta(1) + Delta(25) = 6960/(27*147)."""
        result = discriminant_complementarity(1)
        expected = Rational(6960) / (27 * 147)
        assert result == expected

    def test_complementarity_c5(self):
        """Delta(5) + Delta(21) = 6960/(47*127)."""
        result = discriminant_complementarity(5)
        expected = Rational(6960) / (47 * 127)
        assert result == expected

    def test_complementarity_c13_selfdual(self):
        """At c = 13: Delta(13) + Delta(13) = 2*40/87 = 80/87."""
        result = discriminant_complementarity(13)
        assert result == Rational(80, 87)

    def test_complementarity_c25(self):
        """Delta(25) + Delta(1)."""
        result = discriminant_complementarity(25)
        expected = Rational(6960) / (147 * 27)
        assert result == expected

    def test_complementarity_symmetry(self):
        """Delta(c) + Delta(26-c) = Delta(26-c) + Delta(c)."""
        for c_val in [1, 5, 13, 25]:
            assert discriminant_complementarity(c_val) == discriminant_complementarity(26 - c_val)


# ======================================================================
# 9. Effective action components
# ======================================================================

class TestEffectiveActionComponents:
    """S_eff^{(r)} decomposition for standard families."""

    def test_heisenberg_arity2(self):
        """S_eff^{(2)} = kappa = k for Heisenberg."""
        components = effective_action_components("heisenberg", k=1)
        assert components[2] == Rational(1)

    def test_heisenberg_arity3_zero(self):
        """S_eff^{(3)} = 0 for Heisenberg (Gaussian class, terminates at r=2)."""
        components = effective_action_components("heisenberg", k=1)
        assert components[3] == Rational(0)

    def test_heisenberg_arity4_zero(self):
        """S_eff^{(4)} = 0 for Heisenberg (Gaussian class)."""
        components = effective_action_components("heisenberg", k=1)
        assert components[4] == Rational(0)

    def test_affine_arity2(self):
        """S_eff^{(2)} = kappa for affine sl_2."""
        components = effective_action_components("affine", N=2, k=1)
        assert components[2] == Rational(9, 4)

    def test_affine_arity3_nonzero(self):
        """S_eff^{(3)} != 0 for affine (Lie class)."""
        components = effective_action_components("affine", N=2, k=1)
        assert components[3] != Rational(0)

    def test_affine_arity4_zero(self):
        """S_eff^{(4)} = 0 for affine (Lie class, terminates at r=3)."""
        components = effective_action_components("affine", N=2, k=1)
        assert components[4] == Rational(0)

    def test_virasoro_arity2(self):
        """S_eff^{(2)} = c/2 for Virasoro."""
        components = effective_action_components("virasoro", c=26)
        assert components[2] == Rational(13)

    def test_virasoro_arity3_nonzero(self):
        """S_eff^{(3)} != 0 for Virasoro (Mixed class)."""
        components = effective_action_components("virasoro", c=1)
        assert components[3] != Rational(0)

    def test_virasoro_arity4_nonzero(self):
        """S_eff^{(4)} != 0 for Virasoro (Mixed class)."""
        components = effective_action_components("virasoro", c=1)
        assert components[4] != Rational(0)


# ======================================================================
# 10. Kappa functional equation
# ======================================================================

class TestKappaFunctionalEquation:
    """kappa(c) + kappa(26-c) = 13 for Virasoro."""

    def test_functional_eq_c1(self):
        assert kappa_functional_equation(1) == Rational(13)

    def test_functional_eq_c13(self):
        assert kappa_functional_equation(13) == Rational(13)

    def test_functional_eq_c25(self):
        assert kappa_functional_equation(25) == Rational(13)

    def test_functional_eq_c_half(self):
        assert kappa_functional_equation(Rational(1, 2)) == Rational(13)

    def test_shadow_gf_at_t0(self):
        """At t=0, H(c) + H(26-c) = 13 for Virasoro."""
        H_c, H_dual = shadow_gf_functional_equation(1)
        assert H_c + H_dual == Rational(13)


# ======================================================================
# 11. Kappa complementarity sum
# ======================================================================

class TestKappaComplementaritySum:
    """kappa(A) + kappa(A!) for standard families."""

    def test_virasoro_sum_13(self):
        assert kappa_complementarity_sum("virasoro", c=1) == Rational(13)

    def test_virasoro_sum_13_at_c26(self):
        assert kappa_complementarity_sum("virasoro", c=26) == Rational(13)

    def test_heisenberg_sum_0(self):
        assert kappa_complementarity_sum("heisenberg", k=1) == Rational(0)

    def test_heisenberg_sum_0_k5(self):
        assert kappa_complementarity_sum("heisenberg", k=5) == Rational(0)

    def test_w3_sum_250_over_3(self):
        """kappa(W_3, c) + kappa(W_3, 100-c) = 5*100/6 = 250/3."""
        assert kappa_complementarity_sum("w3", c=2) == Rational(250, 3)

    def test_betagamma_sum_0(self):
        assert kappa_complementarity_sum("betagamma", c=2) == Rational(0)

    def test_lattice_sum_0(self):
        assert kappa_complementarity_sum("lattice", rank=24) == Rational(0)


# ======================================================================
# 12. Non-critical curvature
# ======================================================================

class TestNonCriticalCurvature:
    """d^2 coefficient = kappa * omega_g."""

    def test_genus1_c26(self):
        """At c=26: kappa = 13, omega_1 = 1. Curvature = 13."""
        assert non_critical_curvature(26, genus=1) == Rational(13)

    def test_genus1_c1(self):
        """At c=1: kappa = 1/2."""
        assert non_critical_curvature(1, genus=1) == Rational(1, 2)

    def test_genus1_c0(self):
        """At c=0: kappa = 0."""
        assert non_critical_curvature(0, genus=1) == Rational(0)


# ======================================================================
# 13. Anomaly polynomial and depth
# ======================================================================

class TestAnomalyPolynomial:
    """Anomaly polynomial length determines shadow depth."""

    def test_heisenberg_length_1(self):
        """Heisenberg: depth 2, polynomial has 1 entry [kappa]."""
        poly = anomaly_polynomial("heisenberg", k=1)
        assert len(poly) == 1  # only kappa, depth = 2
        assert poly[0] == Rational(1)

    def test_affine_length_2(self):
        """Affine: depth 3, polynomial has 2 entries [kappa, C]."""
        poly = anomaly_polynomial("affine", N=2, k=1)
        assert len(poly) == 2
        assert poly[0] == Rational(9, 4)  # kappa
        assert poly[1] != Rational(0)     # cubic nonzero

    def test_betagamma_length_3(self):
        """Betagamma: depth 4, polynomial has 3 entries [kappa, C, Q]."""
        poly = anomaly_polynomial("betagamma", lam=1)
        assert len(poly) == 3
        assert poly[0] == Rational(1)     # kappa
        assert poly[2] != Rational(0)     # quartic nonzero

    def test_virasoro_mixed_class(self):
        """Virasoro: infinite depth (M class), returns 5 entries."""
        poly = anomaly_polynomial("virasoro", c=1)
        assert len(poly) == 5  # returns through arity 6

    def test_depth_from_poly_heisenberg(self):
        poly = anomaly_polynomial("heisenberg", k=1)
        assert depth_from_anomaly_polynomial(poly) == 2

    def test_depth_from_poly_affine(self):
        poly = anomaly_polynomial("affine", N=2, k=1)
        assert depth_from_anomaly_polynomial(poly) == 3

    def test_depth_from_poly_betagamma(self):
        poly = anomaly_polynomial("betagamma", lam=1)
        assert depth_from_anomaly_polynomial(poly) == 4


# ======================================================================
# 14. Shadow class (G/L/C/M)
# ======================================================================

class TestShadowClass:
    """G/L/C/M classification of standard families."""

    def test_heisenberg_gaussian(self):
        assert shadow_class("heisenberg") == "G"

    def test_lattice_gaussian(self):
        assert shadow_class("lattice") == "G"

    def test_affine_lie(self):
        assert shadow_class("affine") == "L"

    def test_betagamma_contact(self):
        assert shadow_class("betagamma") == "C"

    def test_virasoro_mixed(self):
        assert shadow_class("virasoro") == "M"

    def test_w3_mixed(self):
        assert shadow_class("w3") == "M"


# ======================================================================
# 15. Cross-checks and consistency
# ======================================================================

class TestCrossChecks:
    """Consistency between different computed quantities."""

    def test_brst_anomaly_equals_c_minus_26(self):
        """BRST anomaly = c - 26."""
        for c_val in [0, 1, 13, 25, 26, 27]:
            assert brst_anomaly(c_val) == Rational(c_val) - 26

    def test_kappa_virasoro_equals_half_c(self):
        for c_val in [0, 1, Rational(1, 2), 13, 25, 26, 100]:
            assert kappa("virasoro", c=c_val) == Rational(c_val) / 2

    def test_effective_action_arity2_equals_kappa(self):
        """S_eff^{(2)} = kappa for all families."""
        families = [
            ("heisenberg", {"k": 3}),
            ("virasoro", {"c": 10}),
            ("affine", {"N": 2, "k": 1}),
            ("w3", {"c": 5}),
            ("betagamma", {"lam": 1}),
            ("lattice", {"rank": 8}),
        ]
        for fam, params in families:
            components = effective_action_components(fam, **params)
            k_val = kappa(fam, **params)
            assert components[2] == k_val, f"Mismatch for {fam}"

    def test_anomaly_cancellation_universal(self):
        """c + (26-c) + (-26) = 0 for a range of values."""
        for c_val in range(-10, 50):
            assert total_anomaly_cancellation(c_val) == Rational(0)

    def test_discriminant_complementarity_constant_numerator(self):
        """The numerator 40*174 = 6960 is independent of c."""
        for c_val in [1, 2, 5, 10, 13, 20, 25]:
            c_r = Rational(c_val)
            D_sum = discriminant_complementarity(c_r)
            # Verify D_sum = 6960 / ((5c+22)(152-5c))
            expected_denom = (5 * c_r + 22) * (152 - 5 * c_r)
            expected = Rational(6960) / expected_denom
            assert D_sum == expected, f"Failed at c = {c_val}"

    def test_liouville_Q_squared_non_negative_for_c_geq_1(self):
        """Q^2 = (c-1)/6 >= 0 for c >= 1."""
        for c_val in [1, 2, 7, 13, 25, 26, 100]:
            data = liouville_data(c_val)
            assert data["Q_squared"] >= 0

    def test_virasoro_selfdual_c13(self):
        """Virasoro self-dual point: c = 13, c' = 13."""
        assert koszul_dual_central_charge("virasoro", c=13) == Rational(13)
        assert kappa_complementarity_sum("virasoro", c=13) == Rational(13)

    def test_w3_selfdual_c50(self):
        """W_3 self-dual point: c = 50, c' = 50."""
        assert koszul_dual_central_charge("w3", c=50) == Rational(50)
        assert kappa_complementarity_sum("w3", c=50) == Rational(250, 3)
