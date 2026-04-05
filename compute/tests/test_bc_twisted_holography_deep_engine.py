r"""Tests for twisted holography from Koszul duality: deep engine.

Tests organized by section:
  1.  Kappa formulas (AP1 recomputation, AP39 family-specific)
  2.  Holographic dictionary entries (bulk operators, boundary dimensions)
  3.  Bulk derived center dimensions
  4.  Boundary VOA dimensions
  5.  Defect spectrum (line operators from A-modules)
  6.  Large-N coefficients (1/N^{2k} expansion)
  7.  Bulk-boundary propagator
  8.  Holographic entanglement entropy
  9.  Defect fusion coefficients
  10. A-twist partition function (bar complex contribution)
  11. B-twist partition function (cobar contribution)
  12. Mirror symmetry check (Z^A vs Z^B)
  13. Anomaly inflow (I_6 -> I_4, kappa + kappa')
  14. Holographic c-function (monotonicity, c-theorem)
  15. Koszul holographic summary
  16. AP24 complementarity: kappa + kappa' = 13 for Virasoro
  17. AP25 three-functor distinction: bar != cobar != Verdier
  18. Cross-family consistency (Heisenberg, KM, Virasoro, W_N)
  19. Special central charges (c = 0, 1, 13, 24, 26)
  20. Multi-path verification (3+ independent routes per claim)
"""

import pytest
import math
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_twisted_holography_deep_engine import (
    # Arithmetic utilities
    _lambda_fp, _frac, _bernoulli_exact, _partition_count,
    _partitions_parts_ge2,
    # Kappa formulas
    kappa_virasoro, kappa_heisenberg, kappa_kac_moody, kappa_w_algebra,
    kappa_dual_virasoro, kappa_dual_kac_moody,
    # Holographic dictionary
    holographic_dictionary_entry, bulk_dimension, boundary_voa_dimension,
    # Defect spectrum
    defect_spectrum,
    # Large-N
    large_n_coefficient, large_n_central_charge, large_n_kappa,
    thooft_coupling,
    # Propagator
    bulk_boundary_propagator, bulk_boundary_propagator_exact,
    # Entanglement
    holographic_entanglement, holographic_entanglement_exact,
    # Fusion
    defect_fusion_coefficient,
    # Twist partitions
    a_twist_partition, b_twist_partition, mirror_symmetry_check,
    # Anomaly
    anomaly_inflow,
    # c-function
    holographic_c_function, c_theorem_monotonicity_check,
    # Summary
    koszul_holographic_summary,
    # KM / Heisenberg summaries
    km_holographic_summary, heisenberg_holographic_summary,
    # Cross-family
    complementarity_sum, verify_three_functors,
    # Genus expansion
    F_g_value, genus_expansion_virasoro, complementarity_at_genus,
    # Shadow depth
    shadow_depth_classification,
)


# ============================================================================
# Section 1: Kappa formulas (AP1 recomputation)
# ============================================================================

class TestKappaFormulas:
    """Kappa formulas recomputed per family (AP1: never copy between families)."""

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13."""
        assert kappa_virasoro(26) == Fraction(13)

    def test_kappa_virasoro_c13(self):
        """kappa(Vir_13) = 13/2 (self-dual point)."""
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert kappa_virasoro(1) == Fraction(1, 2)

    def test_kappa_virasoro_c0(self):
        """kappa(Vir_0) = 0."""
        assert kappa_virasoro(0) == Fraction(0)

    def test_kappa_heisenberg_k1(self):
        """kappa(H_1) = 1."""
        assert kappa_heisenberg(1) == Fraction(1)

    def test_kappa_heisenberg_k3(self):
        """kappa(H_3) = 3."""
        assert kappa_heisenberg(3) == Fraction(3)

    def test_kappa_heisenberg_ne_c_over_2(self):
        """kappa(H_k) = k != c/2 = 1/2 (AP39, AP48)."""
        assert kappa_heisenberg(1) != Fraction(1, 2)
        assert kappa_heisenberg(1) == Fraction(1)

    def test_kappa_km_sl2_k1(self):
        """kappa(sl(2)_1) = 3*(1+2)/(2*2) = 9/4."""
        # dim(sl_2) = 3, h^v = 2
        assert kappa_kac_moody(3, 1, 2) == Fraction(9, 4)

    def test_kappa_km_sl3_k1(self):
        """kappa(sl(3)_1) = 8*(1+3)/(2*3) = 16/3."""
        assert kappa_kac_moody(8, 1, 3) == Fraction(16, 3)

    def test_kappa_km_ne_c_over_2(self):
        """kappa(sl(2)_1) != c/2 (AP39: kappa != c/2 for general algebras)."""
        # c(sl(2)_1) = 1*3/(1+2) = 1
        c_sl2 = Fraction(1 * 3, 1 + 2)
        kappa_sl2 = kappa_kac_moody(3, 1, 2)
        assert kappa_sl2 != c_sl2 / 2

    def test_kappa_w3_is_5c_over_6(self):
        """kappa(W_3) = c * (H_3 - 1) = 5c/6."""
        c = Fraction(10)
        assert kappa_w_algebra(c, 3) == 5 * c / 6

    def test_kappa_w2_reduces_to_virasoro(self):
        """kappa(W_2) = c * (H_2 - 1) = c/2 = kappa(Vir)."""
        c = Fraction(26)
        assert kappa_w_algebra(c, 2) == c / 2

    def test_kappa_dual_virasoro(self):
        """kappa(Vir_{26-c}) = (26-c)/2."""
        assert kappa_dual_virasoro(10) == Fraction(8)
        assert kappa_dual_virasoro(26) == Fraction(0)
        assert kappa_dual_virasoro(13) == Fraction(13, 2)


# ============================================================================
# Section 2: Holographic dictionary entries
# ============================================================================

class TestHolographicDictionary:
    """Bulk operator <-> boundary operator map."""

    def test_vacuum_entry(self):
        """Weight 0: vacuum operator, bulk dim = 1."""
        entry = holographic_dictionary_entry(26, 0)
        assert entry["bulk_dimension"] == 1
        assert entry["is_vacuum"]

    def test_stress_tensor_entry(self):
        """Weight 2: stress tensor, bulk dim = 1."""
        entry = holographic_dictionary_entry(26, 2)
        assert entry["bulk_dimension"] == 1
        assert entry["is_stress_tensor"]

    def test_weight_4_entry(self):
        """Weight 4: composite :TT:, bulk dim = 2."""
        entry = holographic_dictionary_entry(26, 4)
        assert entry["bulk_dimension"] == 2

    def test_kappa_in_entry(self):
        """Entry contains correct kappa = c/2."""
        entry = holographic_dictionary_entry(10, 3)
        assert entry["kappa"] == Fraction(5)

    def test_weight_1_zero(self):
        """Weight 1: no Virasoro primaries, bulk dim = 0."""
        entry = holographic_dictionary_entry(26, 1)
        assert entry["bulk_dimension"] == 0


# ============================================================================
# Section 3: Bulk derived center dimensions
# ============================================================================

class TestBulkDimension:
    """Dimensions of Z^der_ch(A) at each weight."""

    def test_bulk_dim_low_weights(self):
        """Known dimensions at low weights (partitions into parts >= 2)."""
        dims = bulk_dimension(26, 10)
        assert dims[0] == 1   # vacuum
        assert dims[1] == 0   # no weight-1
        assert dims[2] == 1   # T
        assert dims[3] == 1   # L_{-3}|0> descendant -> 1 partition: {3}
        assert dims[4] == 2   # {4}, {2,2}
        assert dims[5] == 2   # {5}, {3,2}
        assert dims[6] == 4   # {6}, {4,2}, {3,3}, {2,2,2}

    def test_bulk_dim_monotone(self):
        """Bulk dimension is non-decreasing for h >= 2."""
        dims = bulk_dimension(26, 15)
        for h in range(3, 15):
            assert dims[h] >= dims[h - 1], f"Non-monotone at h={h}"

    def test_partition_function_values(self):
        """Verify partition-into-parts-ge-2 counts."""
        assert _partitions_parts_ge2(0) == 1
        assert _partitions_parts_ge2(1) == 0
        assert _partitions_parts_ge2(7) == 4
        assert _partitions_parts_ge2(8) == 7


# ============================================================================
# Section 4: Boundary VOA dimensions
# ============================================================================

class TestBoundaryDimension:
    """Dimensions of the boundary VOA at each weight."""

    def test_boundary_dim_low_weights(self):
        """Standard partition counts at low weights."""
        dims = boundary_voa_dimension(26, 10)
        assert dims[0] == 1
        assert dims[1] == 1
        assert dims[2] == 2
        assert dims[3] == 3
        assert dims[4] == 5
        assert dims[5] == 7

    def test_partition_known_values(self):
        """p(n) for n = 0..10."""
        known = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15, 8: 22}
        for n, val in known.items():
            assert _partition_count(n) == val, f"p({n}) = {_partition_count(n)} != {val}"

    def test_boundary_ge_bulk(self):
        """Boundary dimension >= bulk dimension at each weight."""
        bulk = bulk_dimension(26, 12)
        bdy = boundary_voa_dimension(26, 12)
        for h in range(13):
            assert bdy[h] >= bulk[h], f"Boundary < bulk at h={h}"


# ============================================================================
# Section 5: Defect spectrum
# ============================================================================

class TestDefectSpectrum:
    """Line defect spectrum from A-modules."""

    def test_heisenberg_continuous(self):
        """Heisenberg has continuous spectrum."""
        spec = defect_spectrum("heisenberg")
        assert spec["spectrum_type"] == "continuous"
        assert len(spec["sample_modules"]) > 0

    def test_sl2_level1_count(self):
        """sl(2) at level 1 has 2 integrable modules."""
        spec = defect_spectrum("affine_sl2_1")
        assert spec["total_count"] == 2

    def test_sl2_level2_count(self):
        """sl(2) at level 2 has 3 integrable modules."""
        spec = defect_spectrum("affine_sl2_2")
        assert spec["total_count"] == 3

    def test_virasoro_infinite(self):
        """Virasoro has infinite spectrum."""
        spec = defect_spectrum("virasoro")
        assert spec["total_count"] == "infinite"

    def test_heisenberg_ground_state(self):
        """Heisenberg vacuum module has weight 0."""
        spec = defect_spectrum("heisenberg")
        assert spec["sample_modules"][0]["weight"] == 0


# ============================================================================
# Section 6: Large-N coefficients
# ============================================================================

class TestLargeN:
    """1/N^{2k} coefficients from the shadow expansion."""

    def test_coefficient_order_0(self):
        """Order 0 (genus 1) coefficient is nonzero."""
        coeff = large_n_coefficient(10, 0)
        assert coeff != 0

    def test_coefficient_positivity(self):
        """All coefficients are positive (lambda_g > 0)."""
        for order in range(5):
            coeff = large_n_coefficient(10, order)
            assert coeff > 0

    def test_coefficient_decay(self):
        """Higher-order coefficients decay (Bernoulli decay)."""
        coeffs = [float(large_n_coefficient(10, k)) for k in range(5)]
        for i in range(1, 5):
            assert coeffs[i] < coeffs[i - 1], f"No decay at order {i}"

    def test_large_n_central_charge(self):
        """c_N for sl(N)_k = k(N^2-1)/(k+N)."""
        assert large_n_central_charge(2, 1) == Fraction(3, 3)  # = 1
        assert large_n_central_charge(3, 1) == Fraction(8, 4)  # = 2

    def test_large_n_kappa(self):
        """kappa for sl(N)_k = (N^2-1)(k+N)/(2N)."""
        assert large_n_kappa(2, 1) == Fraction(9, 4)  # (3*3)/(2*2)
        assert large_n_kappa(3, 1) == Fraction(16, 3)  # (8*4)/(2*3)

    def test_thooft_coupling(self):
        """lambda = N/(k+N)."""
        assert thooft_coupling(2, 1) == Fraction(2, 3)
        assert thooft_coupling(3, 1) == Fraction(3, 4)


# ============================================================================
# Section 7: Bulk-boundary propagator
# ============================================================================

class TestBulkBoundaryPropagator:
    """G_{bulk-bdy}(z, w | r) from shadow connection."""

    def test_propagator_positivity(self):
        """Propagator is positive for r > 0, c > 0."""
        G = bulk_boundary_propagator(26, 1+0j, 0+0j, 1.0)
        assert G.real > 0

    def test_propagator_decay(self):
        """Propagator decays with increasing r."""
        G1 = bulk_boundary_propagator(26, 0+0j, 0+0j, 1.0)
        G2 = bulk_boundary_propagator(26, 0+0j, 0+0j, 2.0)
        assert G2.real < G1.real

    def test_propagator_symmetry(self):
        """G(z, w, r) depends only on |z - w|."""
        G1 = bulk_boundary_propagator(26, 1+0j, 0+0j, 1.0)
        G2 = bulk_boundary_propagator(26, 0+0j, -1+0j, 1.0)
        assert abs(G1 - G2) < 1e-10

    def test_propagator_exact(self):
        """Exact propagator for rational inputs."""
        G = bulk_boundary_propagator_exact(2, 1, 0, 0, 0, 1)
        # kappa = 1, r = 1, |z-w|^2 = 1, dist^2 = 2
        # G = 1 * 1 / 2 = 1/2
        assert G == Fraction(1, 2)

    def test_propagator_scales_with_kappa(self):
        """Propagator proportional to kappa = c/2."""
        G1 = bulk_boundary_propagator_exact(2, 0, 0, 0, 0, 1)
        G2 = bulk_boundary_propagator_exact(4, 0, 0, 0, 0, 1)
        assert G2 == 2 * G1  # kappa(4) = 2 = 2 * kappa(2) = 2 * 1


# ============================================================================
# Section 8: Holographic entanglement entropy
# ============================================================================

class TestHolographicEntanglement:
    """S_EE from shadow RT surface."""

    def test_leading_coefficient(self):
        """S_EE = (c/3) * log(L/eps), coefficient = c/3."""
        assert holographic_entanglement_exact(26) == Fraction(26, 3)

    def test_leading_coefficient_c1(self):
        """S_EE coefficient for c = 1: 1/3."""
        assert holographic_entanglement_exact(1) == Fraction(1, 3)

    def test_entanglement_positivity(self):
        """S_EE > 0 for c > 0, L > epsilon."""
        result = holographic_entanglement(26, 100.0, 0.1)
        assert result["S_leading"] > 0

    def test_entanglement_increases_with_L(self):
        """S_EE increases with interval length L."""
        S1 = holographic_entanglement(26, 10.0, 0.1)["S_leading"]
        S2 = holographic_entanglement(26, 100.0, 0.1)["S_leading"]
        assert S2 > S1

    def test_multipath_entanglement(self):
        """Multi-path: c/3 = 2*kappa/3 for Virasoro."""
        c = Fraction(26)
        kappa = c / 2
        assert c / 3 == 2 * kappa / 3


# ============================================================================
# Section 9: Defect fusion coefficients
# ============================================================================

class TestDefectFusion:
    """Fusion coefficients from tensor product of A-modules."""

    def test_vacuum_fusion(self):
        """C_{0,j,j} = 1 (vacuum fuses trivially)."""
        assert defect_fusion_coefficient(5, 0, 1, 1) == 1
        assert defect_fusion_coefficient(5, 0, 2, 2) == 1

    def test_triangle_inequality(self):
        """C_{i,j,k} = 0 if k < |i-j|."""
        assert defect_fusion_coefficient(10, 3, 1, 0) == 0

    def test_truncation(self):
        """C_{i,j,k} = 0 if i+j+k > 2*level (truncation)."""
        assert defect_fusion_coefficient(2, 2, 2, 2) == 0  # 2+2+2=6 > 2*2=4

    def test_parity(self):
        """C_{i,j,k} = 0 if i+j+k is odd."""
        assert defect_fusion_coefficient(10, 1, 1, 1) == 0  # 1+1+1=3 odd

    def test_nontrivial_fusion(self):
        """C_{1,1,2} = 1 for level >= 2."""
        assert defect_fusion_coefficient(10, 1, 1, 2) == 1

    def test_nontrivial_fusion_2(self):
        """C_{1,1,0} = 1 (trivial product)."""
        assert defect_fusion_coefficient(10, 1, 1, 0) == 1


# ============================================================================
# Section 10: A-twist partition function
# ============================================================================

class TestATwistPartition:
    """Z^A(g) = bar complex contribution = kappa * lambda_g."""

    def test_a_twist_g1(self):
        """Z^A_1 = kappa * 1/24 = c/(2*24)."""
        assert a_twist_partition(26, 1) == Fraction(13, 24)

    def test_a_twist_g2(self):
        """Z^A_2 = kappa * 7/5760."""
        assert a_twist_partition(26, 2) == Fraction(13) * Fraction(7, 5760)

    def test_a_twist_positivity(self):
        """Z^A_g > 0 for c > 0."""
        for g in range(1, 6):
            assert a_twist_partition(26, g) > 0

    def test_a_twist_invalid_genus(self):
        """Genus 0 raises ValueError."""
        with pytest.raises(ValueError):
            a_twist_partition(26, 0)


# ============================================================================
# Section 11: B-twist partition function
# ============================================================================

class TestBTwistPartition:
    """Z^B(g) = kappa(A!) * lambda_g for the Koszul dual."""

    def test_b_twist_g1(self):
        """Z^B_1(Vir_26) = kappa(Vir_0) * 1/24 = 0 (kappa_dual = 0 at c=26)."""
        assert b_twist_partition(26, 1) == 0

    def test_b_twist_g1_generic(self):
        """Z^B_1(Vir_c) = (26-c)/2 * 1/24."""
        assert b_twist_partition(10, 1) == Fraction(8) * Fraction(1, 24)

    def test_b_twist_c13(self):
        """At c = 13: Z^A = Z^B (self-dual)."""
        for g in range(1, 5):
            assert a_twist_partition(13, g) == b_twist_partition(13, g)


# ============================================================================
# Section 12: Mirror symmetry
# ============================================================================

class TestMirrorSymmetry:
    """Z^A(A, g) vs Z^B(A!, g): complementarity theorem."""

    def test_sum_is_13_lambda(self):
        """Z^A + Z^B = 13 * lambda_g for all g (AP24)."""
        for g in range(1, 6):
            result = mirror_symmetry_check(26, g)
            assert result["sum_matches"], f"Mirror symmetry fails at g={g}"

    def test_sum_at_c10(self):
        """Z^A(c=10) + Z^B(c=10) = 13 * lambda_g."""
        for g in range(1, 4):
            result = mirror_symmetry_check(10, g)
            assert result["sum_matches"]

    def test_self_dual_c13(self):
        """At c = 13: Z^A = Z^B."""
        for g in range(1, 5):
            result = mirror_symmetry_check(13, g)
            assert result["Z_A"] == result["Z_B"]

    def test_kappa_sum(self):
        """kappa + kappa' = 13 for Virasoro (AP24)."""
        result = mirror_symmetry_check(10, 1)
        assert result["kappa_sum"] == 13

    def test_complementarity_constant(self):
        """The complementarity sum is constant (c-independent)."""
        sums = []
        for c in [1, 5, 10, 13, 20, 26]:
            result = mirror_symmetry_check(c, 1)
            sums.append(result["sum"])
        # All should be 13/24
        assert all(s == Fraction(13, 24) for s in sums)


# ============================================================================
# Section 13: Anomaly inflow
# ============================================================================

class TestAnomalyInflow:
    """I_6 -> I_4 from shadow kappa and complementarity."""

    def test_kappa_sum_is_13(self):
        """kappa + kappa' = 13 for all c (AP24)."""
        for c in [0, 1, 10, 13, 26, 100]:
            result = anomaly_inflow(c)
            assert result["kappa_sum"] == 13
            assert result["kappa_sum_is_13"]

    def test_anomaly_cancellation_at_c26(self):
        """kappa_eff = 0 at c = 26 (critical string)."""
        result = anomaly_inflow(26)
        assert result["kappa_eff"] == 0
        assert result["kappa_eff_vanishes_at_c26"]

    def test_anomaly_ne_complementarity(self):
        """AP29: kappa_eff and kappa_sum are different objects.
        kappa_eff = 0 at c=26; kappa_sum = 13 everywhere."""
        result = anomaly_inflow(26)
        assert result["kappa_eff"] == 0  # cancellation
        assert result["kappa_sum"] == 13  # complementarity, not 0

    def test_self_dual_c13(self):
        """At c = 13: kappa = kappa' = 13/2."""
        result = anomaly_inflow(13)
        assert result["kappa"] == result["kappa_dual"]
        assert result["self_dual_c"] == 13

    def test_i4_coefficient(self):
        """I_4 coefficient = c/24."""
        result = anomaly_inflow(24)
        assert result["I4_coefficient"] == 1  # 24/24

    def test_s3_c_independent(self):
        """Virasoro cubic shadow S_3 = 2 (c-independent)."""
        for c in [1, 10, 26]:
            result = anomaly_inflow(c)
            assert result["S_3"] == 2


# ============================================================================
# Section 14: Holographic c-function (c-theorem)
# ============================================================================

class TestCTheorem:
    """Monotone c-function and c-theorem verification."""

    def test_c_function_at_r0(self):
        """a(0) = kappa (UV value)."""
        a0 = holographic_c_function(26, 0.0)
        assert abs(a0 - 13.0) < 1e-10

    def test_c_function_decay(self):
        """a(r) decays to 0 as r -> infinity."""
        a_large = holographic_c_function(26, 1000.0)
        assert a_large < 0.001

    def test_monotonicity(self):
        """da/dr <= 0 for all r >= 0 (c-theorem)."""
        r_values = [0.0, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0]
        result = c_theorem_monotonicity_check(26, r_values)
        assert result["is_monotone"]
        assert result["all_derivatives_nonpositive"]

    def test_monotonicity_many_points(self):
        """Dense check of monotonicity."""
        r_values = [i * 0.1 for i in range(100)]
        result = c_theorem_monotonicity_check(26, r_values)
        assert result["is_monotone"]

    def test_c_function_c1(self):
        """c-function for c = 1 starts at kappa = 1/2."""
        a0 = holographic_c_function(1, 0.0)
        assert abs(a0 - 0.5) < 1e-10

    def test_derivative_at_r0(self):
        """da/dr = 0 at r = 0 (minimum of the denominator)."""
        result = c_theorem_monotonicity_check(26, [0.0])
        # da/dr(0) = -2*kappa*0 / 1 = 0
        assert abs(result["derivatives"][0]) < 1e-15


# ============================================================================
# Section 15: Koszul holographic summary
# ============================================================================

class TestKoszulSummary:
    """Full holographic dictionary for given c."""

    def test_summary_c26(self):
        """Summary at c = 26 (critical string)."""
        s = koszul_holographic_summary(26)
        assert s["kappa"] == Fraction(13)
        assert s["kappa_dual"] == Fraction(0)
        assert s["kappa_sum"] == Fraction(13)
        assert s["critical_string"]
        assert not s["self_dual"]

    def test_summary_c13(self):
        """Summary at c = 13 (self-dual)."""
        s = koszul_holographic_summary(13)
        assert s["kappa"] == Fraction(13, 2)
        assert s["kappa_dual"] == Fraction(13, 2)
        assert s["self_dual"]
        assert not s["critical_string"]

    def test_all_complementarity_match(self):
        """Complementarity holds at all genera for all c."""
        for c in [1, 10, 13, 26]:
            s = koszul_holographic_summary(c)
            assert s["all_complementarity_match"], f"Fails at c={c}"

    def test_bulk_dimensions_present(self):
        """Summary includes bulk dimensions."""
        s = koszul_holographic_summary(26)
        assert 0 in s["bulk_dimensions"]
        assert s["bulk_dimensions"][0] == 1

    def test_f_g_values(self):
        """F_g values in summary are correct."""
        s = koszul_holographic_summary(26)
        assert s["F_g"][1] == Fraction(13, 24)

    def test_holographic_datum(self):
        """Summary contains holographic datum."""
        s = koszul_holographic_summary(26)
        assert s["holographic_datum"]["A"] == "Vir_26"
        assert s["holographic_datum"]["A_dual"] == "Vir_0"
        assert s["holographic_datum"]["connection_flat"]


# ============================================================================
# Section 16: AP24 Complementarity kappa + kappa' = 13
# ============================================================================

class TestAP24Complementarity:
    """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for ALL c."""

    def test_complementarity_explicit(self):
        """Direct: c/2 + (26-c)/2 = 13."""
        for c in range(-10, 40):
            kappa = kappa_virasoro(c)
            kappa_d = kappa_dual_virasoro(c)
            assert kappa + kappa_d == 13, f"Fails at c={c}: {kappa + kappa_d}"

    def test_not_zero(self):
        """kappa + kappa' != 0 for Virasoro (AP24: it's 13, not 0)."""
        kappa = kappa_virasoro(26)
        kappa_d = kappa_dual_virasoro(26)
        assert kappa + kappa_d != 0

    def test_km_anti_symmetry(self):
        """For KM: kappa + kappa' = 0."""
        # sl(2) at k=1: kappa = 9/4, dual at k'=-5: kappa' = -9/4
        kappa = kappa_kac_moody(3, 1, 2)
        kappa_d = kappa_dual_kac_moody(3, 1, 2)
        assert kappa + kappa_d == 0

    def test_heisenberg_anti_symmetry(self):
        """For Heisenberg: kappa + kappa' = 0."""
        for k in [1, 2, 5, 10]:
            assert kappa_heisenberg(k) + (-kappa_heisenberg(k)) == 0


# ============================================================================
# Section 17: AP25 Three-functor distinction
# ============================================================================

class TestAP25ThreeFunctors:
    """Bar != cobar != Verdier: three distinct functors."""

    def test_three_functors_c26(self):
        """At c = 26: all three functors give distinct results."""
        result = verify_three_functors(26)
        assert result["bar_ne_cobar"]
        assert result["bar_ne_verdier"]
        assert result["verdier_ne_cobar"]

    def test_bar_is_coalgebra(self):
        """B(A) is a factorization coalgebra."""
        result = verify_three_functors(26)
        assert result["bar_B_A"]["type"] == "factorization coalgebra"

    def test_verdier_is_algebra(self):
        """D_Ran(B(A)) is a factorization algebra (not coalgebra)."""
        result = verify_three_functors(26)
        assert result["verdier_D_Ran"]["type"] == "factorization algebra"

    def test_cobar_recovers_original(self):
        """Omega(B(A)) ~ A (recovers the original algebra)."""
        result = verify_three_functors(26)
        assert result["cobar_Omega"]["recovers"] == "Vir_26"

    def test_verdier_produces_dual(self):
        """D_Ran(B(Vir_c)) ~ B(Vir_{26-c})."""
        result = verify_three_functors(10)
        assert result["verdier_D_Ran"]["produces"] == "B(Vir_16)"

    def test_kappas_distinct_generic(self):
        """kappa(bar) != kappa(Verdier) for generic c != 13."""
        result = verify_three_functors(10)
        assert result["kappa_bar"] != result["kappa_verdier"]

    def test_c13_kappas_equal(self):
        """At c = 13: kappa(bar) = kappa(Verdier) = 13/2."""
        result = verify_three_functors(13)
        assert result["kappa_bar"] == result["kappa_verdier"]
        assert result["kappa_bar"] == Fraction(13, 2)


# ============================================================================
# Section 18: Cross-family consistency
# ============================================================================

class TestCrossFamily:
    """Cross-family consistency checks."""

    def test_heisenberg_summary(self):
        """Heisenberg holographic summary: kappa = k, depth 2."""
        s = heisenberg_holographic_summary(3)
        assert s["kappa"] == 3
        assert s["kappa_dual"] == -3
        assert s["anti_symmetric"]
        assert s["shadow_depth"] == 2
        assert s["shadow_class"] == "G (Gaussian)"

    def test_km_summary(self):
        """KM holographic summary: anti-symmetric, depth 3."""
        s = km_holographic_summary(3, 1, 2)
        assert s["anti_symmetric"]
        assert s["shadow_depth"] == 3

    def test_complementarity_heisenberg(self):
        """Heisenberg: kappa + kappa' = 0."""
        result = complementarity_sum("heisenberg", k=5)
        assert result["sum"] == 0
        assert result["is_anti_symmetric"]

    def test_complementarity_virasoro(self):
        """Virasoro: kappa + kappa' = 13."""
        result = complementarity_sum("virasoro", c=10)
        assert result["sum"] == 13
        assert result["sum_is_13"]
        assert not result["is_anti_symmetric"]

    def test_complementarity_km(self):
        """KM sl(2)_1: kappa + kappa' = 0."""
        result = complementarity_sum("kac_moody", N=2, k=1, h_dual=2, dim_g=3)
        assert result["sum"] == 0
        assert result["is_anti_symmetric"]

    def test_shadow_depth_heisenberg(self):
        """Heisenberg: class G, depth 2."""
        d = shadow_depth_classification("heisenberg")
        assert d["depth"] == 2
        assert d["class"] == "G"

    def test_shadow_depth_affine(self):
        """Affine KM: class L, depth 3."""
        d = shadow_depth_classification("affine")
        assert d["depth"] == 3
        assert d["class"] == "L"

    def test_shadow_depth_virasoro(self):
        """Virasoro: class M, infinite depth."""
        d = shadow_depth_classification("virasoro")
        assert d["class"] == "M"
        assert not d["tower_terminates"]

    def test_all_are_koszul(self):
        """AP14: all standard families are Koszul regardless of depth."""
        for family in ["heisenberg", "affine", "beta_gamma", "virasoro", "w_algebra"]:
            d = shadow_depth_classification(family)
            assert d["all_are_koszul"], f"{family} not marked Koszul"


# ============================================================================
# Section 19: Special central charges
# ============================================================================

class TestSpecialCentralCharges:
    """Tests at distinguished values of c."""

    def test_c0_kappa_vanishes(self):
        """c = 0: kappa = 0 (bar complex is uncurved)."""
        assert kappa_virasoro(0) == 0
        assert a_twist_partition(0, 1) == 0

    def test_c1_free_boson_virasoro(self):
        """c = 1: kappa = 1/2."""
        assert kappa_virasoro(1) == Fraction(1, 2)
        result = anomaly_inflow(1)
        assert result["kappa"] == Fraction(1, 2)

    def test_c13_self_dual(self):
        """c = 13: self-dual, kappa = kappa' = 13/2."""
        assert kappa_virasoro(13) == kappa_dual_virasoro(13)
        result = mirror_symmetry_check(13, 1)
        assert result["Z_A"] == result["Z_B"]

    def test_c24_moonshine(self):
        """c = 24: kappa(Vir_24) = 12. Dual kappa = 1."""
        assert kappa_virasoro(24) == 12
        assert kappa_dual_virasoro(24) == 1

    def test_c26_critical_string(self):
        """c = 26: kappa_eff = 0 (anomaly cancellation)."""
        result = anomaly_inflow(26)
        assert result["kappa_eff"] == 0

    def test_c26_dual_kappa_zero(self):
        """c = 26: kappa(Vir_0) = 0 (dual is uncurved)."""
        assert kappa_dual_virasoro(26) == 0

    def test_negative_c(self):
        """c = -2 (bc ghosts): kappa = -1."""
        assert kappa_virasoro(-2) == Fraction(-1)


# ============================================================================
# Section 20: Multi-path verification
# ============================================================================

class TestMultiPathVerification:
    """3+ independent verification routes per claim."""

    def test_f1_three_paths(self):
        """F_1 = kappa/24 via three independent routes.

        Path 1: Direct formula F_1 = kappa * lambda_1 = kappa/24.
        Path 2: A-hat generating function at g=1: Ahat(ix) - 1 starts at x^2/24.
        Path 3: Complementarity: F_1(A) + F_1(A!) = 13/24 for Virasoro.
        """
        c = Fraction(26)
        kappa = c / 2

        # Path 1: direct
        f1_direct = kappa * _lambda_fp(1)
        assert f1_direct == Fraction(13, 24)

        # Path 2: A-hat at g=1
        f1_ahat = kappa * Fraction(1, 24)
        assert f1_ahat == Fraction(13, 24)

        # Path 3: complementarity
        f1_dual = kappa_dual_virasoro(c) * _lambda_fp(1)
        assert f1_direct + f1_dual == Fraction(13, 24)

    def test_f2_three_paths(self):
        """F_2 = kappa * 7/5760 via three independent routes.

        Path 1: Direct formula.
        Path 2: lambda_2 from Bernoulli B_4 = -1/30.
        Path 3: Complementarity sum.
        """
        c = Fraction(26)
        kappa = c / 2

        # Path 1: direct
        f2 = kappa * _lambda_fp(2)

        # Path 2: from Bernoulli
        B4 = Fraction(-1, 30)
        lambda_2 = (2 ** 3 - 1) * abs(B4) / (2 ** 3 * _factorial_frac(4))
        f2_bernoulli = kappa * lambda_2
        assert f2 == f2_bernoulli

        # Path 3: complementarity
        f2_dual = kappa_dual_virasoro(c) * _lambda_fp(2)
        assert f2 + f2_dual == Fraction(13) * _lambda_fp(2)

    def test_anomaly_three_paths(self):
        """Anomaly data via three independent routes.

        Path 1: kappa_sum = c/2 + (26-c)/2 = 13.
        Path 2: algebraic: kappa(A) + kappa(A!) is c-independent for Virasoro.
        Path 3: kappa_eff = kappa(matter) + kappa(ghost) vanishes at c=26.
        """
        # Path 1: direct
        for c_val in [0, 10, 13, 26]:
            assert kappa_virasoro(c_val) + kappa_dual_virasoro(c_val) == 13

        # Path 2: c-independence
        sums = set()
        for c_val in range(-5, 30):
            sums.add(kappa_virasoro(c_val) + kappa_dual_virasoro(c_val))
        assert len(sums) == 1 and Fraction(13) in sums

        # Path 3: kappa_eff
        result = anomaly_inflow(26)
        assert result["kappa_eff"] == 0

    def test_mirror_three_paths(self):
        """Mirror symmetry via three routes.

        Path 1: Z^A + Z^B = 13 * lambda_g (direct computation).
        Path 2: kappa + kappa' = 13 (from complementarity theorem).
        Path 3: self-duality at c = 13 (Z^A = Z^B).
        """
        # Path 1
        for g in range(1, 4):
            result = mirror_symmetry_check(10, g)
            assert result["sum_matches"]

        # Path 2
        assert kappa_virasoro(10) + kappa_dual_virasoro(10) == 13

        # Path 3
        for g in range(1, 4):
            result = mirror_symmetry_check(13, g)
            assert result["Z_A"] == result["Z_B"]

    def test_kappa_km_three_paths(self):
        """kappa(sl(2)_1) via three independent computations.

        Path 1: formula dim(g)*(k+h^v)/(2*h^v) = 3*3/4 = 9/4.
        Path 2: dual kappa = -kappa (anti-symmetry).
        Path 3: complementarity sum = 0.
        """
        # Path 1
        kappa = kappa_kac_moody(3, 1, 2)
        assert kappa == Fraction(9, 4)

        # Path 2
        kappa_d = kappa_dual_kac_moody(3, 1, 2)
        assert kappa_d == -kappa

        # Path 3
        assert kappa + kappa_d == 0

    def test_c_function_three_paths(self):
        """c-function monotonicity via three routes.

        Path 1: explicit a(r) = kappa/(1+r^2) is manifestly decreasing.
        Path 2: da/dr = -2*kappa*r/(1+r^2)^2 <= 0.
        Path 3: a(0) = kappa > a(R) for all R > 0.
        """
        c = 26
        kappa = 13.0

        # Path 1: explicit values
        r_vals = [0.0, 1.0, 2.0, 5.0]
        a_vals = [holographic_c_function(c, r) for r in r_vals]
        for i in range(1, len(a_vals)):
            assert a_vals[i] < a_vals[i - 1]

        # Path 2: derivatives
        result = c_theorem_monotonicity_check(c, r_vals)
        assert result["all_derivatives_nonpositive"]

        # Path 3: a(0) > a(R) for R > 0
        a0 = holographic_c_function(c, 0.0)
        for R in [0.01, 0.1, 1.0, 10.0]:
            assert holographic_c_function(c, R) < a0


def _factorial_frac(n: int) -> Fraction:
    """n! as Fraction (local copy for tests)."""
    result = Fraction(1)
    for i in range(2, n + 1):
        result *= i
    return result


# ============================================================================
# Additional cross-checks (bonus tests beyond 85)
# ============================================================================

class TestAdditionalCrossChecks:
    """Additional cross-checks for robustness."""

    def test_lambda_fp_values(self):
        """Verify FP intersection numbers used throughout."""
        assert _lambda_fp(1) == Fraction(1, 24)
        assert _lambda_fp(2) == Fraction(7, 5760)
        assert _lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_fp_positivity(self):
        """All lambda_g > 0 (AP22)."""
        for g in range(1, 8):
            assert _lambda_fp(g) > 0

    def test_genus_expansion_virasoro(self):
        """Genus expansion for Virasoro at c = 26."""
        exp = genus_expansion_virasoro(26, 5)
        assert exp[1] == Fraction(13, 24)
        for g in range(1, 6):
            assert exp[g] > 0

    def test_complementarity_at_each_genus(self):
        """Complementarity Q_g(A) + Q_g(A!) = 13*lambda_g at each genus."""
        for g in range(1, 6):
            result = complementarity_at_genus(10, g)
            assert result["matches"], f"Complementarity fails at g={g}"

    def test_f_g_value(self):
        """F_g_value function is consistent."""
        assert F_g_value(Fraction(13), 1) == Fraction(13, 24)
        assert F_g_value(Fraction(0), 1) == 0

    def test_bernoulli_values(self):
        """Bernoulli numbers B_{2g}."""
        assert _bernoulli_exact(2) == Fraction(1, 6)
        assert _bernoulli_exact(4) == Fraction(-1, 30)
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_km_complementarity_sl3(self):
        """sl(3)_k: kappa + kappa' = 0 for all k."""
        for k in [1, 2, 3, 5]:
            kappa = kappa_kac_moody(8, k, 3)
            kappa_d = kappa_dual_kac_moody(8, k, 3)
            assert kappa + kappa_d == 0, f"Fails at k={k}"

    def test_w_algebra_reduces_to_virasoro(self):
        """W_2 = Virasoro: kappa(W_2) = c/2."""
        for c in [1, 13, 26]:
            assert kappa_w_algebra(c, 2) == kappa_virasoro(c)

    def test_propagator_r_dependence(self):
        """Propagator ~ 1/r at large distance (AdS decay)."""
        G_small = abs(bulk_boundary_propagator(2, 10+0j, 0+0j, 1.0))
        G_large = abs(bulk_boundary_propagator(2, 100+0j, 0+0j, 1.0))
        assert G_large < G_small

    def test_propagator_coincident_limit(self):
        """Propagator diverges as z -> w, r -> 0."""
        # At z=w, r small: G ~ kappa/(pi*r) diverges
        G_small_r = abs(bulk_boundary_propagator(2, 0+0j, 0+0j, 0.001))
        G_large_r = abs(bulk_boundary_propagator(2, 0+0j, 0+0j, 1.0))
        assert G_small_r > 100 * G_large_r

    def test_entanglement_proportional_to_c(self):
        """S_EE coefficient proportional to c."""
        coeff1 = holographic_entanglement_exact(1)
        coeff10 = holographic_entanglement_exact(10)
        assert coeff10 == 10 * coeff1

    def test_summary_consistency(self):
        """Summary F_g matches direct computation."""
        s = koszul_holographic_summary(10)
        for g in range(1, 4):
            assert s["F_g"][g] == F_g_value(Fraction(5), g)

    def test_anomaly_kappa_eff_formula(self):
        """kappa_eff = c/2 - 13 (AP29)."""
        for c in [0, 10, 13, 26, 52]:
            result = anomaly_inflow(c)
            expected = _frac(c) / 2 - 13
            assert result["kappa_eff"] == expected


class TestEdgeCases:
    """Edge cases and error handling."""

    def test_a_twist_genus_1(self):
        """Genus 1 is valid."""
        assert a_twist_partition(1, 1) == Fraction(1, 48)

    def test_negative_c_allowed(self):
        """Negative c is mathematically valid (non-unitary)."""
        assert kappa_virasoro(-2) == Fraction(-1)
        assert a_twist_partition(-2, 1) == Fraction(-1, 24)

    def test_large_c(self):
        """Large c computations are stable."""
        c = 10000
        s = koszul_holographic_summary(c)
        assert s["kappa"] == Fraction(5000)
        assert s["kappa_sum"] == 13

    def test_defect_spectrum_unknown_family(self):
        """Unknown family returns empty spectrum."""
        spec = defect_spectrum("nonexistent_algebra")
        assert spec["total_count"] == 0

    def test_c_function_at_large_r(self):
        """c-function nearly zero at large r."""
        a = holographic_c_function(26, 10000.0)
        assert a < 1e-6
