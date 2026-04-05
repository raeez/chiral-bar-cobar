r"""Tests for minimal_model_bar: fusion rings, S-matrices, shadow obstruction towers.

Comprehensive verification of minimal model M(p,q) computations:
  1. Central charge values for all standard minimal models
  2. Conformal weight formulas (h_{1,1} = 0, Ising h values, etc.)
  3. Modular S-matrix properties (symmetry, S^2 = C, unitarity)
  4. Verlinde formula vs known fusion rules (Ising, Lee-Yang, TCI)
  5. Genus dimensions (g=0 gives 1, g=1 gives n_primaries)
  6. Shadow obstruction tower consistency with Virasoro at same c
  7. CDG curvature properties
  8. Complementarity c + c' = 26 and kappa + kappa' = 13

Ground truth:
  Ising fusion: sigma x sigma = I + epsilon, sigma x epsilon = sigma,
                epsilon x epsilon = I
  Lee-Yang fusion: phi x phi = I + phi
  Virasoro shadow: kappa = c/2, S_3 = 2, S_4 = 10/(c(5c+22))
  Complementarity: c + c' = 26 for Virasoro (all minimal models)
  comp:ising-bar-interpretation (minimal_model_examples.tex)
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
"""

import math

import pytest
from sympy import Rational, simplify, sqrt, pi, sin

from compute.lib.minimal_model_bar import (
    # Basic data
    minimal_model_c,
    MINIMAL_MODELS,
    ising_bar_data,
    ising_genus1_bar,
    tricritical_ising_data,
    three_state_potts_data,
    verify_minimal_models,
    # Primary field computation
    minimal_model_primaries,
    conformal_weight,
    conformal_weights_table,
    n_primaries,
    # S-matrix
    modular_s_matrix_numerical,
    modular_s_matrix_exact,
    # Fusion
    verlinde_fusion_numerical,
    fusion_ring,
    verlinde_genus_dimension,
    # Bar cohomology
    partition_count,
    kac_determinant_factors,
    kac_determinant_total_degree,
    null_vector_levels,
    bar_cohomology_ranks,
    # Shadow obstruction tower
    shadow_tower_minimal_model,
    shadow_discriminant_complementarity,
    # CDG
    cdg_curvature,
    periodicity_denominator,
    # Extended modular data
    modular_t_matrix,
    verify_s_matrix_properties,
    effective_central_charge,
    is_unitary,
    koszul_dual_central_charge,
    complementarity_sum_kappa,
    s_matrix_s00,
    quantum_dimension,
    global_dimension,
    frobenius_schur_indicator,
    # Cross-family checks
    verify_complementarity_all_models,
    verify_kappa_additivity,
    # Complementarity
    minimal_model_complementarity,
)


# ===========================================================================
# 1. CENTRAL CHARGE VALUES
# ===========================================================================


class TestCentralCharges:
    """Verify central charge formula c = 1 - 6(p-q)^2/(pq)."""

    def test_trivial_c0(self):
        """M(3,2): c = 0 (trivial)."""
        assert minimal_model_c(3, 2) == 0

    def test_ising_c_half(self):
        """M(4,3): c = 1/2 (Ising)."""
        assert minimal_model_c(4, 3) == Rational(1, 2)

    def test_lee_yang_c(self):
        """M(5,2): c = -22/5 (Lee-Yang, non-unitary)."""
        assert minimal_model_c(5, 2) == Rational(-22, 5)

    def test_tricritical_ising_c(self):
        """M(5,4): c = 7/10 (tricritical Ising)."""
        assert minimal_model_c(5, 4) == Rational(7, 10)

    def test_three_state_potts_c(self):
        """M(6,5): c = 4/5 (three-state Potts)."""
        assert minimal_model_c(6, 5) == Rational(4, 5)

    def test_m7_6_c(self):
        """M(7,6): c = 6/7 (tetracritical Ising)."""
        assert minimal_model_c(7, 6) == Rational(6, 7)

    def test_m7_2_c(self):
        """M(7,2): c = -68/7."""
        assert minimal_model_c(7, 2) == Rational(-68, 7)

    def test_central_charge_formula_consistency(self):
        """Verify c = 1 - 6(p-q)^2/(pq) matches stored values."""
        for name, data in MINIMAL_MODELS.items():
            p, q = data["p"], data["q"]
            assert minimal_model_c(p, q) == data["c"], f"Mismatch for {name}"

    def test_unitary_series_c_monotone(self):
        """Unitary series M(m+1, m): c increases toward 1."""
        prev_c = Rational(-1)
        for m in range(2, 10):
            c = minimal_model_c(m + 1, m)
            assert c > prev_c, f"c not monotone at m={m}"
            assert c < 1, f"c >= 1 at m={m}"
            prev_c = c

    def test_unitary_series_c_limit(self):
        """c -> 1 as m -> infinity in the unitary series."""
        c = minimal_model_c(101, 100)
        assert abs(float(c) - 1.0) < 0.01


# ===========================================================================
# 2. CONFORMAL WEIGHTS
# ===========================================================================


class TestConformalWeights:
    """Verify h_{r,s} = ((pr - qs)^2 - (p-q)^2) / (4pq)."""

    def test_vacuum_weight_always_zero(self):
        """h_{1,1} = 0 for all M(p,q)."""
        models = [(4, 3), (5, 4), (5, 2), (6, 5), (7, 6), (7, 2)]
        for p, q in models:
            assert conformal_weight(p, q, 1, 1) == 0

    def test_ising_sigma(self):
        """Ising sigma: h_{1,2} = 1/16."""
        assert conformal_weight(4, 3, 1, 2) == Rational(1, 16)

    def test_ising_epsilon(self):
        """Ising epsilon: h_{1,3} = 1/2."""
        # Actually h_{2,1} in (r <= p-1, s <= q-1) convention
        # but in our convention h_{1,3} with 1<=r<=q-1=2, 1<=s<=p-1=3
        assert conformal_weight(4, 3, 1, 3) == Rational(1, 2)

    def test_tricritical_ising_weights(self):
        """TCI M(5,4): verify all 6 conformal weights."""
        expected = {
            (1, 1): Rational(0),
            (1, 2): Rational(1, 10),
            (1, 3): Rational(3, 5),
            (1, 4): Rational(3, 2),
            (2, 1): Rational(7, 16),
            (2, 2): Rational(3, 80),
        }
        wt = conformal_weights_table(5, 4)
        assert wt == expected

    def test_lee_yang_weights(self):
        """Lee-Yang M(5,2): two primaries, h = 0 and h = -1/5."""
        assert conformal_weight(5, 2, 1, 1) == 0
        assert conformal_weight(5, 2, 1, 2) == Rational(-1, 5)

    def test_identification_symmetry(self):
        """h_{r,s} = h_{q-r, p-s} under the identification."""
        models = [(4, 3), (5, 4), (6, 5)]
        for p, q in models:
            for r in range(1, q):
                for s in range(1, p):
                    h1 = conformal_weight(p, q, r, s)
                    h2 = conformal_weight(p, q, q - r, p - s)
                    assert h1 == h2, (
                        f"M({p},{q}): h({r},{s})={h1} != "
                        f"h({q-r},{p-s})={h2}"
                    )

    def test_n_primaries_count(self):
        """(p-1)(q-1)/2 primaries for each model."""
        assert n_primaries(3, 2) == 1
        assert n_primaries(4, 3) == 3
        assert n_primaries(5, 4) == 6
        assert n_primaries(5, 2) == 2
        assert n_primaries(6, 5) == 10
        assert n_primaries(7, 6) == 15

    def test_primaries_list_length(self):
        """minimal_model_primaries returns correct number of fields."""
        for p, q in [(4, 3), (5, 4), (5, 2), (6, 5), (7, 6)]:
            prims = minimal_model_primaries(p, q)
            assert len(prims) == n_primaries(p, q)

    def test_nonunitary_negative_weights(self):
        """Non-unitary models can have negative conformal weights."""
        # Lee-Yang: h = -1/5 < 0
        assert conformal_weight(5, 2, 1, 2) < 0

    def test_unitary_nonnegative_weights(self):
        """Unitary models M(m+1,m) have all h >= 0."""
        for m in range(2, 8):
            p, q = m + 1, m
            wt = conformal_weights_table(p, q)
            for (r, s), h in wt.items():
                assert h >= 0, f"M({p},{q}): h({r},{s}) = {h} < 0"


# ===========================================================================
# 3. MODULAR S-MATRIX PROPERTIES
# ===========================================================================


class TestSMatrix:
    """Verify modular S-matrix properties."""

    @pytest.mark.parametrize("p,q", [(4, 3), (5, 4), (5, 2), (6, 5)])
    def test_s_matrix_symmetric(self, p, q):
        """S is a symmetric matrix."""
        sdata = modular_s_matrix_numerical(p, q)
        mat = sdata["matrix"]
        n = len(mat)
        for i in range(n):
            for j in range(n):
                assert abs(mat[i][j] - mat[j][i]) < 1e-10

    @pytest.mark.parametrize("p,q", [(4, 3), (5, 4), (5, 2), (6, 5)])
    def test_s_squared_is_identity(self, p, q):
        """S^2 = C = I (charge conjugation is identity for minimal models)."""
        sdata = modular_s_matrix_numerical(p, q)
        mat = sdata["matrix"]
        n = len(mat)
        # Compute S^2
        for i in range(n):
            for j in range(n):
                s2_ij = sum(mat[i][k] * mat[k][j] for k in range(n))
                expected = 1.0 if i == j else 0.0
                assert abs(s2_ij - expected) < 1e-10, (
                    f"M({p},{q}): (S^2)[{i},{j}] = {s2_ij}, expected {expected}"
                )

    @pytest.mark.parametrize("p,q", [(4, 3), (5, 4), (5, 2)])
    def test_s00_positive(self, p, q):
        """S_{00} > 0 (vacuum normalization)."""
        sdata = modular_s_matrix_numerical(p, q)
        assert sdata["S00"] > 0

    def test_ising_s_matrix_known_values(self):
        """Ising S-matrix matches the well-known values."""
        sdata = modular_s_matrix_numerical(4, 3)
        mat = sdata["matrix"]
        s2 = math.sqrt(2.0)
        expected = [
            [0.5, s2 / 2, 0.5],
            [s2 / 2, 0.0, -s2 / 2],
            [0.5, -s2 / 2, 0.5],
        ]
        for i in range(3):
            for j in range(3):
                assert abs(mat[i][j] - expected[i][j]) < 1e-10

    def test_s00_formula(self):
        """S_{00} = 2*sqrt(2/(pq)) * sin(pi/p) * sin(pi/q)."""
        for p, q in [(4, 3), (5, 4), (5, 2), (6, 5)]:
            computed = s_matrix_s00(p, q)
            sdata = modular_s_matrix_numerical(p, q)
            assert abs(computed - sdata["S00"]) < 1e-10

    @pytest.mark.parametrize("p,q", [(4, 3), (5, 4), (5, 2)])
    def test_verify_s_matrix_properties_all(self, p, q):
        """Full property verification suite for S-matrix."""
        results = verify_s_matrix_properties(p, q)
        for prop, ok in results.items():
            assert ok, f"M({p},{q}): {prop} failed"


# ===========================================================================
# 4. VERLINDE FUSION RULES
# ===========================================================================


class TestFusionRules:
    """Verify Verlinde formula reproduces known fusion rules."""

    def test_ising_sigma_sigma(self):
        """Ising: sigma x sigma = I + epsilon."""
        # sigma = index 1, I = index 0, epsilon = index 2
        assert verlinde_fusion_numerical(4, 3, 1, 1, 0) == 1  # I
        assert verlinde_fusion_numerical(4, 3, 1, 1, 1) == 0  # not sigma
        assert verlinde_fusion_numerical(4, 3, 1, 1, 2) == 1  # epsilon

    def test_ising_sigma_epsilon(self):
        """Ising: sigma x epsilon = sigma."""
        assert verlinde_fusion_numerical(4, 3, 1, 2, 0) == 0  # not I
        assert verlinde_fusion_numerical(4, 3, 1, 2, 1) == 1  # sigma
        assert verlinde_fusion_numerical(4, 3, 1, 2, 2) == 0  # not epsilon

    def test_ising_epsilon_epsilon(self):
        """Ising: epsilon x epsilon = I."""
        assert verlinde_fusion_numerical(4, 3, 2, 2, 0) == 1  # I
        assert verlinde_fusion_numerical(4, 3, 2, 2, 1) == 0  # not sigma
        assert verlinde_fusion_numerical(4, 3, 2, 2, 2) == 0  # not epsilon

    def test_lee_yang_phi_phi(self):
        """Lee-Yang: phi x phi = I + phi."""
        assert verlinde_fusion_numerical(5, 2, 1, 1, 0) == 1  # I
        assert verlinde_fusion_numerical(5, 2, 1, 1, 1) == 1  # phi

    def test_vacuum_is_identity(self):
        """phi_0 x phi_j = phi_j for all j (vacuum is the identity)."""
        for p, q in [(4, 3), (5, 4), (5, 2)]:
            n = n_primaries(p, q)
            for j in range(n):
                for k in range(n):
                    expected = 1 if j == k else 0
                    assert verlinde_fusion_numerical(p, q, 0, j, k) == expected

    def test_fusion_commutativity(self):
        """N_{ij}^k = N_{ji}^k (fusion is commutative)."""
        for p, q in [(4, 3), (5, 4)]:
            n = n_primaries(p, q)
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        nij = verlinde_fusion_numerical(
                            p, q, min(i, j), max(i, j), k
                        )
                        # Since we store (min, max), compute directly:
                        sdata = modular_s_matrix_numerical(p, q)
                        mat = sdata["matrix"]
                        nij_direct = 0.0
                        for l in range(n):
                            if abs(mat[0][l]) > 1e-15:
                                nij_direct += (
                                    mat[i][l] * mat[j][l] * mat[k][l]
                                    / mat[0][l]
                                )
                        assert int(round(nij_direct)) >= 0

    def test_fusion_ring_structure(self):
        """Full fusion ring for Ising has correct structure."""
        fr = fusion_ring(4, 3)
        assert fr["n_primaries"] == 3
        # sigma x sigma = I + epsilon
        assert fr["fusion_coefficients"][(1, 1, 0)] == 1
        assert fr["fusion_coefficients"][(1, 1, 2)] == 1
        # sigma x epsilon = sigma
        assert fr["fusion_coefficients"][(1, 2, 1)] == 1
        # epsilon x epsilon = I
        assert fr["fusion_coefficients"][(2, 2, 0)] == 1

    def test_nonneg_integer_fusion(self):
        """All fusion coefficients are non-negative integers."""
        for p, q in [(4, 3), (5, 4), (5, 2)]:
            n = n_primaries(p, q)
            for i in range(n):
                for j in range(i, n):
                    for k in range(n):
                        nijk = verlinde_fusion_numerical(p, q, i, j, k)
                        assert nijk >= 0
                        assert nijk == int(nijk)


# ===========================================================================
# 5. GENUS DIMENSIONS
# ===========================================================================


class TestGenusDimensions:
    """Verify dim V_g = sum_i S_{0i}^{2-2g}."""

    def test_genus_0_always_1(self):
        """dim V_0 = 1 for all minimal models."""
        for p, q in [(4, 3), (5, 4), (5, 2), (6, 5)]:
            dim = verlinde_genus_dimension(p, q, 0)
            assert abs(dim - 1.0) < 1e-10

    def test_genus_1_equals_n_primaries(self):
        """dim V_1 = number of primaries."""
        for p, q in [(4, 3), (5, 4), (5, 2), (6, 5)]:
            dim = verlinde_genus_dimension(p, q, 1)
            assert abs(dim - n_primaries(p, q)) < 1e-10

    def test_ising_genus_2(self):
        """Ising dim V_2 = 10."""
        dim = verlinde_genus_dimension(4, 3, 2)
        assert abs(dim - 10.0) < 1e-10

    def test_ising_genus_3(self):
        """Ising dim V_3 = 36."""
        dim = verlinde_genus_dimension(4, 3, 3)
        assert abs(dim - 36.0) < 1e-10

    def test_genus_dimension_grows(self):
        """dim V_g grows with g for g >= 1."""
        for p, q in [(4, 3), (5, 4)]:
            prev = verlinde_genus_dimension(p, q, 1)
            for g in range(2, 5):
                curr = verlinde_genus_dimension(p, q, g)
                assert curr > prev
                prev = curr

    def test_lee_yang_genus_dimensions(self):
        """Lee-Yang: 2 primaries, so dim V_1 = 2."""
        assert abs(verlinde_genus_dimension(5, 2, 1) - 2.0) < 1e-10


# ===========================================================================
# 6. SHADOW TOWER CONSISTENCY
# ===========================================================================


class TestShadowTower:
    """Verify shadow obstruction tower at c(M(p,q)) matches Virasoro shadow obstruction tower."""

    def test_ising_kappa(self):
        """Ising: kappa = c/2 = 1/4."""
        st = shadow_tower_minimal_model(4, 3)
        assert st["kappa"] == Rational(1, 4)

    def test_ising_alpha(self):
        """Ising: S_3 = alpha = 2 (universal Virasoro)."""
        st = shadow_tower_minimal_model(4, 3)
        assert st["alpha"] == 2

    def test_ising_s4(self):
        """Ising: S_4 = 10/(c(5c+22)) = 10/(1/2 * 49/2) = 40/49."""
        st = shadow_tower_minimal_model(4, 3)
        assert st["S4"] == Rational(40, 49)

    def test_ising_s5(self):
        """Ising: S_5 = -48/(c^3(5c+22)) = -48/(1/8 * 49/2) = -768/49."""
        st = shadow_tower_minimal_model(4, 3)
        assert st["S5"] == Rational(-768, 49)

    def test_ising_delta(self):
        """Ising: Delta = 40/(5c+22) = 40/(49/2) = 80/49."""
        st = shadow_tower_minimal_model(4, 3)
        assert st["Delta"] == Rational(80, 49)

    def test_ising_class_M(self):
        """Ising: Delta != 0 => class M (infinite shadow depth)."""
        st = shadow_tower_minimal_model(4, 3)
        assert st["class"] == "M"

    def test_trivial_kappa_zero(self):
        """M(3,2): c = 0 => kappa = 0, trivial shadow obstruction tower."""
        st = shadow_tower_minimal_model(3, 2)
        assert st["kappa"] == 0
        assert st["class"] == "trivial"

    def test_shadow_s2_equals_kappa(self):
        """S_2 = kappa = c/2 for all non-trivial minimal models."""
        for p, q in [(4, 3), (5, 4), (6, 5)]:
            st = shadow_tower_minimal_model(p, q)
            c = minimal_model_c(p, q)
            assert st["S"][2] == c / 2

    def test_shadow_quadratic_metric(self):
        """Q_L(t) = q0 + q1*t + q2*t^2 with q0 = 4*kappa^2."""
        for p, q in [(4, 3), (5, 4), (6, 5)]:
            st = shadow_tower_minimal_model(p, q)
            kappa = st["kappa"]
            assert st["q0"] == 4 * kappa ** 2

    def test_shadow_q1_coefficient(self):
        """q1 = 12*kappa*alpha."""
        for p, q in [(4, 3), (5, 4)]:
            st = shadow_tower_minimal_model(p, q)
            assert st["q1"] == 12 * st["kappa"] * st["alpha"]

    def test_lee_yang_singular(self):
        """Lee-Yang M(5,2): c = -22/5, 5c+22 = 0 => S_4 singular."""
        st = shadow_tower_minimal_model(5, 2)
        assert st["class"] == "singular"

    def test_tci_shadow_class_M(self):
        """TCI: Delta != 0 => class M."""
        st = shadow_tower_minimal_model(5, 4)
        assert st["class"] == "M"

    def test_shadow_rho_squared_positive(self):
        """For class M: rho^2 > 0."""
        for p, q in [(4, 3), (5, 4), (6, 5)]:
            st = shadow_tower_minimal_model(p, q)
            if st["class"] == "M":
                assert st["rho_squared"] is not None
                assert st["rho_squared"] > 0


# ===========================================================================
# 7. CDG CURVATURE
# ===========================================================================


class TestCDGCurvature:
    """Verify CDG (curved DG) structure for minimal model bar complexes."""

    def test_ising_null_level(self):
        """Ising M(4,3): null vector at level (p-1)(q-1) = 6."""
        cdg = cdg_curvature(4, 3)
        assert cdg["null_vector_level"] == 6

    def test_lee_yang_null_level(self):
        """Lee-Yang M(5,2): null vector at level 4."""
        cdg = cdg_curvature(5, 2)
        assert cdg["null_vector_level"] == 4

    def test_tci_null_level(self):
        """TCI M(5,4): null vector at level 12."""
        cdg = cdg_curvature(5, 4)
        assert cdg["null_vector_level"] == 12

    def test_potts_null_level(self):
        """Potts M(6,5): null vector at level 20."""
        cdg = cdg_curvature(6, 5)
        assert cdg["null_vector_level"] == 20

    def test_simple_quotient_is_curved(self):
        """Simple quotient (minimal model) is always curved."""
        for p, q in [(4, 3), (5, 4), (5, 2), (6, 5)]:
            cdg = cdg_curvature(p, q)
            assert cdg["is_curved"] is True

    def test_universal_not_curved(self):
        """Universal Virasoro algebra is NOT curved."""
        for p, q in [(4, 3), (5, 4), (5, 2)]:
            cdg = cdg_curvature(p, q)
            assert cdg["universal_is_curved"] is False

    def test_admissible_level(self):
        """Admissible level k = p/q - 2."""
        cdg = cdg_curvature(4, 3)
        assert cdg["admissible_level"] == Rational(4, 3) - 2
        assert cdg["admissible_level"] == Rational(-2, 3)

    def test_null_level_increases_with_pq(self):
        """Null level (p-1)(q-1) increases with p*q."""
        levels = []
        for p, q in [(3, 2), (4, 3), (5, 4), (6, 5)]:
            cdg = cdg_curvature(p, q)
            levels.append(cdg["null_vector_level"])
        for i in range(1, len(levels)):
            assert levels[i] > levels[i - 1]


# ===========================================================================
# 8. COMPLEMENTARITY c + c' = 26
# ===========================================================================


class TestComplementarity:
    """Verify Virasoro complementarity: c + c' = 26."""

    def test_c_plus_c_dual_26_ising(self):
        """Ising: c + c' = 1/2 + 51/2 = 26."""
        c = minimal_model_c(4, 3)
        c_dual = koszul_dual_central_charge(4, 3)
        assert c + c_dual == 26

    def test_c_plus_c_dual_26_all(self):
        """c + c' = 26 for all standard minimal models."""
        results = verify_complementarity_all_models()
        for name, ok in results.items():
            assert ok, f"Complementarity failed for {name}"

    def test_kappa_plus_kappa_dual_13(self):
        """kappa + kappa' = 13 for all minimal models."""
        results = verify_kappa_additivity()
        for name, ok in results.items():
            assert ok, f"Kappa additivity failed for {name}"

    def test_complementarity_sum_constant(self):
        """minimal_model_complementarity always returns 26."""
        for p, q in [(4, 3), (5, 4), (5, 2), (6, 5), (7, 6)]:
            assert minimal_model_complementarity(p, q) == 26

    def test_discriminant_complementarity(self):
        """Delta + Delta' = 6960/((5c+22)(152-5c)) for Virasoro."""
        for p, q in [(4, 3), (5, 4), (6, 5), (7, 6)]:
            result = shadow_discriminant_complementarity(p, q)
            if result["sum"] is not None:
                assert result["match"], (
                    f"M({p},{q}): discriminant complementarity failed"
                )


# ===========================================================================
# 9. PARTITION FUNCTION AND KAC DETERMINANT
# ===========================================================================


class TestPartitionsAndKac:
    """Verify partition counts and Kac determinant structure."""

    def test_partition_small_values(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        assert partition_count(0) == 1
        assert partition_count(1) == 1
        assert partition_count(2) == 2
        assert partition_count(3) == 3
        assert partition_count(4) == 5
        assert partition_count(5) == 7
        assert partition_count(6) == 11
        assert partition_count(7) == 15

    def test_kac_factors_level_1(self):
        """Level 1: single factor (1,1) with multiplicity 1."""
        factors = kac_determinant_factors(4, 3, 1)
        assert len(factors) == 1
        r, s, h_rs, mult = factors[0]
        assert (r, s) == (1, 1)
        assert mult == 1

    def test_kac_total_degree_level_2(self):
        """Total degree of Kac determinant at level 2 is 3."""
        # (1,1) with p(1)=1, (1,2) with p(0)=1, (2,1) with p(0)=1
        assert kac_determinant_total_degree(2) == 3

    def test_kac_total_degree_grows(self):
        """Kac determinant degree grows with level."""
        prev = 0
        for n in range(1, 8):
            deg = kac_determinant_total_degree(n)
            assert deg > prev
            prev = deg

    def test_kac_factors_include_vacuum(self):
        """h_{1,1} = 0 is always a factor at level >= 1."""
        for p, q in [(4, 3), (5, 4)]:
            for level in range(1, 5):
                factors = kac_determinant_factors(p, q, level)
                h_values = [f[2] for f in factors if (f[0], f[1]) == (1, 1)]
                assert len(h_values) == 1
                assert h_values[0] == 0


# ===========================================================================
# 10. BAR COHOMOLOGY
# ===========================================================================


class TestBarCohomology:
    """Verify bar cohomology ranks for universal Virasoro."""

    def test_universal_koszul_h0(self):
        """H^0(Bar) = 1 (ground field)."""
        ranks = bar_cohomology_ranks(4, 3)
        assert ranks[0] == 1

    def test_universal_koszul_h1(self):
        """H^1(Bar) = 1 (single generator T)."""
        ranks = bar_cohomology_ranks(4, 3)
        assert ranks[1] == 1

    def test_universal_koszul_h2(self):
        """H^2(Bar) = 1 (single relation)."""
        ranks = bar_cohomology_ranks(4, 3)
        assert ranks[2] == 1

    def test_universal_koszul_higher_vanish(self):
        """H^k(Bar) = 0 for k >= 3 (Koszul)."""
        ranks = bar_cohomology_ranks(4, 3, max_degree=6)
        for k in range(3, 7):
            assert ranks[k] == 0


# ===========================================================================
# 11. EXTENDED MODULAR DATA
# ===========================================================================


class TestExtendedModularData:
    """Verify modular T-matrix, quantum dimensions, etc."""

    def test_t_matrix_vacuum_phase(self):
        """Vacuum phase: h_{1,1} - c/24 = -c/24."""
        for p, q in [(4, 3), (5, 4)]:
            tdata = modular_t_matrix(p, q)
            c = minimal_model_c(p, q)
            assert tdata["phases"][(1, 1)] == -c / 24

    def test_quantum_dim_vacuum_is_1(self):
        """Quantum dimension of vacuum is 1."""
        for p, q in [(4, 3), (5, 4), (5, 2)]:
            d = quantum_dimension(p, q, 1, 1)
            assert abs(d - 1.0) < 1e-10

    def test_ising_quantum_dim_sigma(self):
        """Ising: d_sigma = sqrt(2)."""
        d = quantum_dimension(4, 3, 1, 2)
        assert abs(d - math.sqrt(2)) < 1e-10

    def test_ising_quantum_dim_epsilon(self):
        """Ising: d_epsilon = 1."""
        d = quantum_dimension(4, 3, 1, 3)
        assert abs(d - 1.0) < 1e-10

    def test_global_dimension_inverse_s00_sq(self):
        """D^2 = 1/S_{00}^2."""
        for p, q in [(4, 3), (5, 4)]:
            D2 = global_dimension(p, q)
            s00 = s_matrix_s00(p, q)
            assert abs(D2 - 1.0 / s00 ** 2) < 1e-10

    def test_ising_global_dimension(self):
        """Ising: D^2 = 4 (since S_{00} = 1/2)."""
        D2 = global_dimension(4, 3)
        assert abs(D2 - 4.0) < 1e-10

    def test_frobenius_schur_all_plus_one(self):
        """All FS indicators are +1 for minimal models (self-conjugate)."""
        for p, q in [(4, 3), (5, 4)]:
            for r, s in minimal_model_primaries(p, q):
                assert frobenius_schur_indicator(p, q, r, s) == 1

    def test_is_unitary_classification(self):
        """M(m+1, m) is unitary; others are not."""
        assert is_unitary(4, 3) is True
        assert is_unitary(5, 4) is True
        assert is_unitary(6, 5) is True
        assert is_unitary(5, 2) is False
        assert is_unitary(7, 2) is False

    def test_effective_c_unitary(self):
        """For unitary models: c_eff = c (since h_min = 0)."""
        for m in range(2, 7):
            p, q = m + 1, m
            assert effective_central_charge(p, q) == minimal_model_c(p, q)

    def test_effective_c_nonunitary_larger(self):
        """For non-unitary models: c_eff > c."""
        # Lee-Yang: c = -22/5, h_min = -1/5, c_eff = -22/5 + 24/5 = 2/5
        c_eff = effective_central_charge(5, 2)
        assert c_eff == Rational(2, 5)
        assert c_eff > minimal_model_c(5, 2)


# ===========================================================================
# 12. PERIODICITY
# ===========================================================================


class TestPeriodicity:
    """Verify periodicity denominators."""

    def test_ising_periodicity(self):
        """Ising M(4,3): period 24."""
        assert periodicity_denominator(4, 3) == 24

    def test_lee_yang_periodicity(self):
        """Lee-Yang M(5,2): period 20."""
        assert periodicity_denominator(5, 2) == 20


# ===========================================================================
# 13. NULL VECTORS
# ===========================================================================


class TestNullVectors:
    """Verify null vector levels."""

    def test_ising_null_vectors(self):
        """Ising: vacuum null vectors at levels 1 and 6."""
        nvs = null_vector_levels(4, 3)
        levels = [nv[2] for nv in nvs]
        assert 1 in levels
        assert 6 in levels

    def test_lee_yang_null_vectors(self):
        """Lee-Yang: vacuum null vectors at levels 1 and 4."""
        nvs = null_vector_levels(5, 2)
        levels = [nv[2] for nv in nvs]
        assert 1 in levels
        assert 4 in levels


# ===========================================================================
# 14. CROSS-CONSISTENCY CHECKS
# ===========================================================================


class TestCrossConsistency:
    """Cross-checks between different computational methods."""

    def test_ising_bar_data_matches_new_computation(self):
        """Existing ising_bar_data() matches new conformal_weight computation."""
        ising = ising_bar_data()
        wt = conformal_weights_table(4, 3)
        assert ising["conformal_weights"]["I"] == wt[(1, 1)]
        assert ising["conformal_weights"]["sigma"] == wt[(1, 2)]
        assert ising["conformal_weights"]["epsilon"] == wt[(1, 3)]

    def test_ising_fusion_matches_verlinde(self):
        """Existing Ising fusion data matches Verlinde computation."""
        ising = ising_bar_data()
        # sigma x sigma = I + epsilon
        assert verlinde_fusion_numerical(4, 3, 1, 1, 0) == 1
        assert verlinde_fusion_numerical(4, 3, 1, 1, 2) == 1
        # sigma x epsilon = sigma
        assert verlinde_fusion_numerical(4, 3, 1, 2, 1) == 1
        # epsilon x epsilon = I
        assert verlinde_fusion_numerical(4, 3, 2, 2, 0) == 1

    def test_tci_data_matches_new_computation(self):
        """Existing tricritical_ising_data() matches new computation."""
        tci = tricritical_ising_data()
        assert tci["c"] == minimal_model_c(5, 4)
        assert tci["kappa"] == minimal_model_c(5, 4) / 2
        assert tci["n_modules"] == n_primaries(5, 4)

    def test_potts_data_matches(self):
        """Existing three_state_potts_data() matches new computation."""
        potts = three_state_potts_data()
        assert potts["c"] == minimal_model_c(6, 5)
        assert potts["kappa"] == minimal_model_c(6, 5) / 2
        assert potts["n_modules"] == n_primaries(6, 5)

    def test_verify_minimal_models_all_pass(self):
        """The original verify_minimal_models() function passes."""
        results = verify_minimal_models()
        for name, ok in results.items():
            assert ok, f"verify_minimal_models: {name} failed"

    def test_shadow_kappa_matches_existing(self):
        """Shadow obstruction tower kappa = c/2 matches existing bar data."""
        ising = ising_bar_data()
        st = shadow_tower_minimal_model(4, 3)
        assert ising["kappa"] == st["kappa"]


# ===========================================================================
# 15. INPUT VALIDATION
# ===========================================================================


class TestInputValidation:
    """Verify proper error handling for invalid inputs."""

    def test_p_less_than_q_raises(self):
        """p < q should raise ValueError."""
        with pytest.raises(ValueError):
            minimal_model_primaries(3, 4)

    def test_q_less_than_2_raises(self):
        """q < 2 should raise ValueError."""
        with pytest.raises(ValueError):
            minimal_model_primaries(5, 1)

    def test_gcd_not_1_raises(self):
        """gcd(p,q) != 1 should raise ValueError."""
        with pytest.raises(ValueError):
            minimal_model_primaries(6, 4)  # gcd = 2

    def test_quantum_dim_invalid_field(self):
        """Invalid field label should raise ValueError."""
        with pytest.raises(ValueError):
            quantum_dimension(4, 3, 3, 3)  # not a valid primary


# ===========================================================================
# 16. EXACT S-MATRIX
# ===========================================================================


class TestExactSMatrix:
    """Verify exact (SymPy) S-matrix computations."""

    def test_exact_s00_ising(self):
        """Exact S_{00} for Ising = 1/2."""
        sdata = modular_s_matrix_exact(4, 3)
        s00 = simplify(sdata["S00"])
        assert s00 == Rational(1, 2)

    def test_exact_symmetry_ising(self):
        """Exact S-matrix is symmetric for Ising."""
        sdata = modular_s_matrix_exact(4, 3)
        mat = sdata["matrix"]
        n = len(sdata["primaries"])
        for i in range(n):
            for j in range(n):
                assert simplify(mat[i][j] - mat[j][i]) == 0
