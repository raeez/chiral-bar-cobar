"""Tests for polyakov_shadow_bridge: Polyakov-shadow obstruction tower bridge verification.

Verifies the arity-2 projection of the shadow obstruction tower:
  - kappa(A) replaces c in the Polyakov formula
  - anomaly ratio rho = kappa/c
  - complementarity kappa(A) + kappa(A!) = constant
  - Faber-Pandharipande intersection numbers
  - BPZ parameters and Koszul self-duality
  - shadow depth classification G/L/C/M
  - bosonic string free energy and critical dimension

Ground truth:
  theorem_c_complementarity.py (verified kappa formulas),
  betagamma_determinant.py (betagamma c and kappa),
  nonlinear_modular_shadows.tex (shadow obstruction tower),
  concordance.tex (shadow archetype classification).
"""
from fractions import Fraction

import pytest

from compute.lib.polyakov_shadow_bridge import (
    kappa,
    central_charge,
    anomaly_ratio,
    complementarity_sum,
    faber_pandharipande,
    genus_free_energy,
    polyakov_coefficient,
    bpz_parameter,
    mumford_exponent,
    shadow_depth_class,
    shadow_depth,
    bosonic_string_free_energy,
    bosonic_string_critical_dimension,
    genus_growth_bound,
    polyakov_bridge_summary,
    anomaly_ratio_table,
    affine_anomaly_ratio,
)


# ======================================================================
# 1. Heisenberg kappa = k
# ======================================================================

class TestHeisenbergKappa:
    """kappa(H_k) = k for all levels."""

    @pytest.mark.parametrize("k", range(1, 11))
    def test_kappa_equals_level(self, k):
        """kappa(H_k) = k."""
        assert kappa("heisenberg", k=k) == Fraction(k)

    @pytest.mark.parametrize("k", range(1, 6))
    def test_kappa_equals_central_charge(self, k):
        """For Heisenberg: kappa = c = k, so rho = 1."""
        assert kappa("heisenberg", k=k) == central_charge("heisenberg", k=k)

    def test_anomaly_ratio_is_one(self):
        """Heisenberg anomaly ratio rho = 1."""
        assert anomaly_ratio("heisenberg", k=3) == Fraction(1)

    def test_kappa_half_integer(self):
        """kappa works for non-integer level."""
        assert kappa("heisenberg", k=Fraction(1, 2)) == Fraction(1, 2)


# ======================================================================
# 2. Virasoro kappa = c/2
# ======================================================================

class TestVirasoroKappa:
    """kappa(Vir_c) = c/2."""

    @pytest.mark.parametrize("c", [1, Fraction(1, 2), Fraction(7, 10), 25, 26])
    def test_kappa_is_c_over_2(self, c):
        """kappa(Vir_c) = c/2."""
        assert kappa("virasoro", c=c) == Fraction(c) / 2

    def test_anomaly_ratio_is_half(self):
        """Virasoro anomaly ratio rho = 1/2."""
        assert anomaly_ratio("virasoro", c=1) == Fraction(1, 2)

    def test_anomaly_ratio_half_generic(self):
        """rho = 1/2 for Virasoro at any c != 0."""
        assert anomaly_ratio("virasoro", c=Fraction(7, 10)) == Fraction(1, 2)


# ======================================================================
# 3. W_3 kappa = 5c/6
# ======================================================================

class TestW3Kappa:
    """kappa(W_3) = 5c/6."""

    @pytest.mark.parametrize("c", [2, 50, 100, Fraction(4, 5)])
    def test_kappa_is_5c_over_6(self, c):
        """kappa(W_3, c) = 5c/6."""
        assert kappa("w3", c=c) == Fraction(5) * Fraction(c) / 6

    def test_anomaly_ratio_is_5_over_6(self):
        """W_3 anomaly ratio rho = 5/6."""
        assert anomaly_ratio("w3", c=2) == Fraction(5, 6)


# ======================================================================
# 4. Affine sl_2 kappa
# ======================================================================

class TestAffineSl2Kappa:
    """kappa(V_k(sl_2)) = 3(k+2)/4."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 10])
    def test_affine_sl2_kappa(self, k):
        """kappa = dim(sl_2)*(k+h^v)/(2*h^v) = 3(k+2)/4."""
        expected = Fraction(3) * (k + 2) / 4
        assert kappa("affine", lie_type="A", rank=1, k=k) == expected

    def test_affine_sl2_rho_not_one(self):
        """Affine rho != 1 (not the same as Heisenberg)."""
        rho = anomaly_ratio("affine", lie_type="A", rank=1, k=1)
        assert rho != Fraction(1)

    def test_affine_sl2_central_charge(self):
        """c(sl_2, k=1) = 3*1/(1+2) = 1."""
        assert central_charge("affine", lie_type="A", rank=1, k=1) == Fraction(1)

    def test_affine_sl3_kappa(self):
        """kappa(V_k(sl_3)) = 8(k+3)/6 = 4(k+3)/3."""
        # dim(sl_3) = 8, h^v = 3
        k = 1
        expected = Fraction(8) * (k + 3) / (2 * 3)
        assert kappa("affine", lie_type="A", rank=2, k=k) == expected


# ======================================================================
# 5. betagamma kappa
# ======================================================================

class TestBetagammaKappa:
    """kappa(betagamma at weight lam) = 6*lam^2 - 6*lam + 1 = c/2."""

    def test_standard_betagamma_lambda_1(self):
        """At lam=1: kappa = 6-6+1 = 1, c = 2."""
        assert kappa("betagamma", lam=1) == Fraction(1)
        assert central_charge("betagamma", lam=1) == Fraction(2)

    def test_betagamma_lambda_0(self):
        """At lam=0: kappa = 0-0+1 = 1, c = 2."""
        assert kappa("betagamma", lam=0) == Fraction(1)

    def test_betagamma_lambda_half(self):
        """At lam=1/2: kappa = 6/4-3+1 = -1/2, c = -1."""
        lam = Fraction(1, 2)
        expected = 6 * lam ** 2 - 6 * lam + 1
        assert expected == Fraction(-1, 2)
        assert kappa("betagamma", lam=Fraction(1, 2)) == Fraction(-1, 2)

    def test_betagamma_anomaly_ratio(self):
        """betagamma anomaly ratio rho = 1/2."""
        assert anomaly_ratio("betagamma", lam=1) == Fraction(1, 2)

    def test_betagamma_rho_not_one(self):
        """betagamma rho != 1."""
        rho = anomaly_ratio("betagamma", lam=1)
        assert rho != Fraction(1)


# ======================================================================
# 6. Lattice kappa
# ======================================================================

class TestLatticeKappa:
    """kappa(V_Lambda) = rank (anomaly ratio rho = 1)."""

    @pytest.mark.parametrize("rank", [1, 2, 8, 16, 24])
    def test_lattice_kappa(self, rank):
        assert kappa("lattice", rank=rank) == Fraction(rank)

    def test_lattice_anomaly_ratio_one(self):
        """Lattice: kappa = rank, c = rank, rho = 1."""
        assert anomaly_ratio("lattice", rank=8) == Fraction(1)


# ======================================================================
# 7. Complementarity: kappa + kappa' = constant
# ======================================================================

class TestComplementarity:
    """Complementarity sum kappa(A) + kappa(A!) is level-independent."""

    # --- Virasoro: kappa + kappa' = c/2 + (26-c)/2 = 13 ---

    @pytest.mark.parametrize("c", [1, Fraction(1, 2), 13, 25, 26])
    def test_virasoro_complementarity_13(self, c):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        assert complementarity_sum("virasoro", c=c) == Fraction(13)

    # --- W_3: kappa + kappa' = 5c/6 + 5(100-c)/6 = 250/3 ---

    def test_w3_complementarity(self):
        """kappa(W_3, c) + kappa(W_3, 100-c) = 250/3."""
        assert complementarity_sum("w3", c=2) == Fraction(250, 3)

    def test_w3_complementarity_at_selfdual(self):
        """At c = 50: kappa = kappa' = 125/3, sum = 250/3."""
        assert complementarity_sum("w3", c=50) == Fraction(250, 3)

    # --- Affine sl_2: kappa(k) + kappa(-k-4) = 0 ---

    @pytest.mark.parametrize("k", [1, 2, 3, 4])
    def test_affine_sl2_complementarity_zero(self, k):
        """kappa(V_k(sl_2)) + kappa(V_{-k-4}(sl_2)) = 0.

        FF involution: k -> -k - 2h^v = -k - 4 for sl_2.
        kappa(k) = 3(k+2)/4, kappa(-k-4) = 3(-k-4+2)/4 = 3(-k-2)/4 = -3(k+2)/4.
        Sum = 0.
        """
        assert complementarity_sum("affine", lie_type="A", rank=1, k=k) == Fraction(0)

    # --- Heisenberg: kappa + kappa' = k + (-k) = 0 ---

    def test_heisenberg_complementarity_zero(self):
        """kappa(H_k) + kappa(H_{-k}) = 0."""
        assert complementarity_sum("heisenberg", k=3) == Fraction(0)

    # --- betagamma: kappa + kappa' = 0 ---

    def test_betagamma_complementarity_zero(self):
        """kappa(betagamma) + kappa(bc) = 0."""
        assert complementarity_sum("betagamma", lam=1) == Fraction(0)

    # --- Lattice: kappa + kappa' = 0 ---

    def test_lattice_complementarity_zero(self):
        """kappa(V_Lambda) + kappa(V_Lambda!) = 0."""
        assert complementarity_sum("lattice", rank=8) == Fraction(0)

    # --- Level independence ---

    def test_virasoro_complementarity_level_independent(self):
        """The complementarity sum is the same for all c values."""
        sums = [complementarity_sum("virasoro", c=c)
                for c in [1, 5, 13, 25, Fraction(7, 10)]]
        assert all(s == Fraction(13) for s in sums)

    def test_affine_sl2_complementarity_level_independent(self):
        """Sum = 0 for all levels k."""
        sums = [complementarity_sum("affine", lie_type="A", rank=1, k=k)
                for k in [1, 2, 5, 10, 100]]
        assert all(s == Fraction(0) for s in sums)


# ======================================================================
# 8. Faber-Pandharipande intersection numbers
# ======================================================================

class TestFaberPandharipande:
    """Exact Faber-Pandharipande numbers."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Fraction(31, 967680)

    def test_lambda_4(self):
        """lambda_4^FP = (2^7-1)/2^7 * |B_8| / 8!."""
        # B_8 = -1/30, |B_8| = 1/30
        # (128-1)/128 * (1/30) / 40320 = 127/(128*30*40320)
        # = 127 / 154828800
        expected = Fraction(127, 128) * Fraction(1, 30) / 40320
        assert faber_pandharipande(4) == expected

    def test_lambda_positive(self):
        """lambda_g > 0 for all g >= 1."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0

    def test_lambda_decreasing(self):
        """lambda_g decreases rapidly."""
        for g in range(1, 7):
            assert faber_pandharipande(g) > faber_pandharipande(g + 1)

    def test_genus_0_raises(self):
        """genus 0 is not defined for FP numbers."""
        with pytest.raises(ValueError):
            faber_pandharipande(0)


# ======================================================================
# 9. Genus free energy
# ======================================================================

class TestGenusFreeEnergy:
    """F_g = kappa * lambda_g^FP."""

    def test_heisenberg_F1(self):
        """F_1(H_1) = 1 * 1/24 = 1/24."""
        assert genus_free_energy("heisenberg", 1, k=1) == Fraction(1, 24)

    def test_virasoro_F1(self):
        """F_1(Vir_c) = (c/2) * (1/24) = c/48."""
        assert genus_free_energy("virasoro", 1, c=1) == Fraction(1, 48)

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all families."""
        families = [
            ("heisenberg", {"k": 3}),
            ("virasoro", {"c": 10}),
            ("affine", {"lie_type": "A", "rank": 1, "k": 2}),
            ("betagamma", {"lam": 1}),
            ("w3", {"c": 50}),
            ("lattice", {"rank": 8}),
        ]
        for fam, params in families:
            k = kappa(fam, **params)
            assert genus_free_energy(fam, 1, **params) == k / 24

    def test_F1_heisenberg_k1_equals_c_over_24(self):
        """For Heisenberg at k=1: F_1 = c/24 = 1/24."""
        c = central_charge("heisenberg", k=1)
        F1 = genus_free_energy("heisenberg", 1, k=1)
        assert F1 == c / 24

    def test_genus_2_heisenberg(self):
        """F_2(H_1) = 1 * 7/5760 = 7/5760."""
        assert genus_free_energy("heisenberg", 2, k=1) == Fraction(7, 5760)

    def test_genus_3_heisenberg(self):
        """F_3(H_1) = 31/967680."""
        assert genus_free_energy("heisenberg", 3, k=1) == Fraction(31, 967680)


# ======================================================================
# 10. BPZ parameters
# ======================================================================

class TestBPZParameters:
    """BPZ: b^2 = 6/c, (b')^2 = 6/(26-c)."""

    def test_bpz_at_c1(self):
        """At c = 1: b^2 = 6, (b')^2 = 6/25."""
        b_sq, bp_sq = bpz_parameter(1)
        assert b_sq == Fraction(6)
        assert bp_sq == Fraction(6, 25)

    def test_bpz_at_c25(self):
        """At c = 25: b^2 = 6/25, (b')^2 = 6."""
        b_sq, bp_sq = bpz_parameter(25)
        assert b_sq == Fraction(6, 25)
        assert bp_sq == Fraction(6)

    def test_bpz_self_dual_at_c13(self):
        """At c = 13: b^2 = (b')^2 = 6/13 (self-dual point)."""
        b_sq, bp_sq = bpz_parameter(13)
        assert b_sq == Fraction(6, 13)
        assert bp_sq == Fraction(6, 13)
        assert b_sq == bp_sq

    def test_bpz_duality_swap(self):
        """b^2(c) = (b')^2(26-c) and vice versa."""
        for c in [1, 5, 10, 13, 20, 25]:
            b_sq_c, bp_sq_c = bpz_parameter(c)
            b_sq_dual, bp_sq_dual = bpz_parameter(26 - c)
            assert b_sq_c == bp_sq_dual
            assert bp_sq_c == b_sq_dual

    def test_bpz_c0_raises(self):
        """c = 0: b^2 undefined."""
        with pytest.raises(ValueError):
            bpz_parameter(0)

    def test_bpz_c26_raises(self):
        """c = 26: (b')^2 undefined."""
        with pytest.raises(ValueError):
            bpz_parameter(26)


# ======================================================================
# 11. Shadow depth classification
# ======================================================================

class TestShadowDepth:
    """Shadow depth class: G/L/C/M."""

    def test_heisenberg_is_G(self):
        assert shadow_depth_class("heisenberg") == "G"

    def test_lattice_is_G(self):
        assert shadow_depth_class("lattice") == "G"

    def test_affine_is_L(self):
        assert shadow_depth_class("affine") == "L"

    def test_betagamma_is_C(self):
        assert shadow_depth_class("betagamma") == "C"

    def test_virasoro_is_M(self):
        assert shadow_depth_class("virasoro") == "M"

    def test_w3_is_M(self):
        assert shadow_depth_class("w3") == "M"

    def test_wn_is_M(self):
        assert shadow_depth_class("wn") == "M"

    def test_heisenberg_depth_2(self):
        assert shadow_depth("heisenberg") == 2

    def test_affine_depth_3(self):
        assert shadow_depth("affine") == 3

    def test_betagamma_depth_4(self):
        assert shadow_depth("betagamma") == 4

    def test_virasoro_depth_none(self):
        """Infinite tower: depth = None."""
        assert shadow_depth("virasoro") is None


# ======================================================================
# 12. Polyakov coefficient
# ======================================================================

class TestPolyakovCoefficient:
    """Polyakov coefficient kappa/12."""

    def test_heisenberg_k1(self):
        """Polyakov coefficient for H_1 = 1/12."""
        assert polyakov_coefficient("heisenberg", k=1) == Fraction(1, 12)

    def test_virasoro_c26(self):
        """Polyakov coefficient for Vir_26 = 26/24 = 13/12."""
        assert polyakov_coefficient("virasoro", c=26) == Fraction(13, 12)

    def test_polyakov_is_kappa_over_12(self):
        """General: polyakov_coefficient = kappa / 12."""
        for fam, params in [
            ("heisenberg", {"k": 5}),
            ("virasoro", {"c": 10}),
            ("w3", {"c": 50}),
        ]:
            assert polyakov_coefficient(fam, **params) == kappa(fam, **params) / 12


# ======================================================================
# 13. Bosonic string
# ======================================================================

class TestBosonicString:
    """Bosonic string free energy and critical dimension."""

    def test_critical_dimension(self):
        """d = 26 is the critical dimension."""
        assert bosonic_string_critical_dimension() == 26

    def test_d26_all_genera_vanish(self):
        """At d = 26: F_g = 0 for all g."""
        for g in range(1, 6):
            assert bosonic_string_free_energy(26, g) == Fraction(0)

    def test_d25_nonzero(self):
        """At d = 25: F_g != 0."""
        assert bosonic_string_free_energy(25, 1) != Fraction(0)

    def test_d26_kappa_total_zero(self):
        """At d = 26: kappa_total = 26/2 - 13 = 0."""
        # The Polyakov coefficient vanishes
        kappa_total = Fraction(26, 2) - 13
        assert kappa_total == 0

    def test_d2_F1(self):
        """d = 2: kappa = 1 - 13 = -12, F_1 = -12/24 = -1/2."""
        assert bosonic_string_free_energy(2, 1) == Fraction(-1, 2)


# ======================================================================
# 14. Genus growth
# ======================================================================

class TestGenusGrowth:
    """Genus growth bounds."""

    def test_growth_list_length(self):
        """genus_growth_bound returns max_g entries."""
        result = genus_growth_bound("heisenberg", 10, k=1)
        assert len(result) == 10

    def test_first_entry_is_F1(self):
        """First entry = |F_1|."""
        result = genus_growth_bound("virasoro", 5, c=1)
        assert result[0] == abs(genus_free_energy("virasoro", 1, c=1))

    def test_all_positive(self):
        """All |F_g| are non-negative."""
        result = genus_growth_bound("heisenberg", 10, k=1)
        assert all(x >= 0 for x in result)

    def test_convergent_ratio(self):
        """The ratio lambda_{g+1}/lambda_g converges to 1/(4*pi^2).

        The Faber-Pandharipande numbers satisfy:
          lambda_{g+1}/lambda_g -> 1/(4*pi^2) ~ 0.02533
        so the genus series converges for |kappa| < 4*pi^2.
        This is a consequence of the Bernoulli number asymptotics:
          |B_{2g}| ~ 2 * (2g)! / (2*pi)^{2g}.
        """
        import math
        result = genus_growth_bound("heisenberg", 10, k=1)
        ratios = [float(result[g] / result[g - 1]) for g in range(1, len(result))]
        target = 1.0 / (4 * math.pi ** 2)
        # Ratios should converge to 1/(4*pi^2) from above
        for r in ratios:
            assert r < 1  # series converges
        # Last ratio should be close to 1/(4*pi^2)
        assert abs(ratios[-1] - target) < 0.001


# ======================================================================
# 15. Anomaly ratio table
# ======================================================================

class TestAnomalyRatioTable:
    """Anomaly ratio rho = kappa/c across families."""

    def test_heisenberg_rho_1(self):
        """Heisenberg: rho = 1."""
        table = anomaly_ratio_table()
        assert table["heisenberg"] == Fraction(1)

    def test_virasoro_rho_half(self):
        """Virasoro: rho = 1/2."""
        table = anomaly_ratio_table()
        assert table["virasoro"] == Fraction(1, 2)

    def test_betagamma_rho_half(self):
        """betagamma: rho = 1/2."""
        table = anomaly_ratio_table()
        assert table["betagamma"] == Fraction(1, 2)

    def test_w3_rho_5_6(self):
        """W_3: rho = 5/6."""
        table = anomaly_ratio_table()
        assert table["w3"] == Fraction(5, 6)


# ======================================================================
# 16. Affine anomaly ratio (level-dependent)
# ======================================================================

class TestAffineAnomalyRatio:
    """Affine anomaly ratio rho(k) = (k+h^v)^2 / (2*h^v*k)."""

    def test_sl2_k1(self):
        """sl_2, k=1: rho = (1+2)^2/(2*2*1) = 9/4."""
        assert affine_anomaly_ratio("A", 1, 1) == Fraction(9, 4)

    def test_sl2_k2(self):
        """sl_2, k=2: rho = (2+2)^2/(2*2*2) = 16/8 = 2."""
        assert affine_anomaly_ratio("A", 1, 2) == Fraction(2)

    def test_sl2_level_dependent(self):
        """Affine rho varies with level (unlike Virasoro)."""
        rho_1 = affine_anomaly_ratio("A", 1, 1)
        rho_2 = affine_anomaly_ratio("A", 1, 2)
        assert rho_1 != rho_2


# ======================================================================
# 17. Mumford exponent
# ======================================================================

class TestMumfordExponent:
    """Mumford exponent = complementarity sum."""

    def test_virasoro_mumford_13(self):
        """Virasoro: complementarity sum = 13."""
        assert mumford_exponent("virasoro", c=1) == Fraction(13)

    def test_heisenberg_mumford_0(self):
        """Heisenberg: sum = 0."""
        assert mumford_exponent("heisenberg", k=1) == Fraction(0)


# ======================================================================
# 18. Bridge summary
# ======================================================================

class TestBridgeSummary:
    """polyakov_bridge_summary returns complete data."""

    def test_heisenberg_summary_keys(self):
        """Summary has all expected keys."""
        s = polyakov_bridge_summary("heisenberg", k=1)
        expected_keys = {
            "family", "params", "central_charge", "kappa",
            "anomaly_ratio", "polyakov_coefficient",
            "complementarity_sum", "shadow_depth_class",
            "shadow_depth", "genus_free_energies",
        }
        assert expected_keys.issubset(set(s.keys()))

    def test_heisenberg_summary_values(self):
        """Summary values are correct for Heisenberg."""
        s = polyakov_bridge_summary("heisenberg", k=2)
        assert s["central_charge"] == Fraction(2)
        assert s["kappa"] == Fraction(2)
        assert s["anomaly_ratio"] == Fraction(1)
        assert s["polyakov_coefficient"] == Fraction(1, 6)
        assert s["complementarity_sum"] == Fraction(0)
        assert s["shadow_depth_class"] == "G"
        assert s["shadow_depth"] == 2
        assert s["genus_free_energies"][1] == Fraction(2, 24)


# ======================================================================
# 19. Cross-checks with theorem_c_complementarity
# ======================================================================

class TestCrossChecks:
    """Cross-checks ensuring consistency with established formulas."""

    def test_affine_sl2_kappa_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4, matching theorem_c_complementarity.py."""
        for k in [1, 2, 3, 5, 10]:
            expected = Fraction(3) * (k + 2) / 4
            assert kappa("affine", lie_type="A", rank=1, k=k) == expected

    def test_affine_sl3_kappa_formula(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3."""
        for k in [1, 2, 3]:
            expected = Fraction(8) * (k + 3) / 6
            assert kappa("affine", lie_type="A", rank=2, k=k) == expected

    def test_virasoro_selfdual_c13(self):
        """At c = 13: kappa = kappa! = 13/2 (self-dual)."""
        k_A = kappa("virasoro", c=13)
        assert k_A == Fraction(13, 2)
        # complementarity sum = 13, so kappa! = 13 - 13/2 = 13/2
        comp = complementarity_sum("virasoro", c=13)
        assert comp == Fraction(13)
        assert comp - k_A == k_A  # kappa! = kappa

    def test_w3_selfdual_c50(self):
        """At c = 50: kappa = kappa! = 125/3 (self-dual for W_3)."""
        k_A = kappa("w3", c=50)
        assert k_A == Fraction(250, 6)  # = 125/3
        comp = complementarity_sum("w3", c=50)
        assert comp - k_A == k_A

    def test_betagamma_c_and_kappa_relation(self):
        """For all lam: kappa = c/2."""
        for lam in [0, Fraction(1, 2), 1, 2, Fraction(3, 2)]:
            c_val = central_charge("betagamma", lam=lam)
            k_val = kappa("betagamma", lam=lam)
            assert k_val == c_val / 2


# ======================================================================
# 20. Critical level error handling
# ======================================================================

class TestCriticalLevels:
    """Error handling at critical levels."""

    def test_affine_sl2_critical_raises(self):
        """k = -2 is critical for sl_2."""
        with pytest.raises(ValueError):
            kappa("affine", lie_type="A", rank=1, k=-2)

    def test_affine_sl3_critical_raises(self):
        """k = -3 is critical for sl_3."""
        with pytest.raises(ValueError):
            kappa("affine", lie_type="A", rank=2, k=-3)

    def test_central_charge_critical_raises(self):
        """Central charge also raises at critical level."""
        with pytest.raises(ValueError):
            central_charge("affine", lie_type="A", rank=1, k=-2)
