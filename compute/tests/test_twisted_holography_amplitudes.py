"""Tests for twisted holography amplitudes from Koszul duality (Costello-Li programme).

Verifies:
  1. D3 brane (twisted N=4 SYM): kappa, genus expansion, R-matrix, anomaly matching
  2. M2 brane (ABJM): shadow invariants, genus expansion, R-matrix, anomaly matching
  3. Bulk-boundary propagator: genus 0 and genus 1
  4. Witten diagrams from shadow obstruction tower: 3-point, 4-point, vacuum, tadpole
  5. Sphere reconstruction (GZ 2026): Sh_{0,n} for n = 2,3,4,5
  6. Holographic R-matrix: D3 and M2, CYBE verification
  7. Anomaly matching: kappa_eff = 0 for both examples
  8. Koszul complementarity: kappa(A) + kappa(A!) = 0
  9. Cross-checks: consistency of all components

55+ tests covering all seven computational sections.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.twisted_holography_amplitudes import (
    ABJMShadowData,
    AnomalyMatching,
    BulkBoundaryPropagator,
    HolographicRMatrix,
    TwistedN4Data,
    WittenDiagram,
    _bernoulli_exact,
    _lambda_fp_exact,
    abjm_shadow_invariants,
    anomaly_matching_d3,
    anomaly_matching_m2,
    bulk_boundary_genus0_glN,
    bulk_boundary_genus1_glN,
    cross_check_d3_genus_expansion,
    full_twisted_holography_datum_d3,
    full_twisted_holography_datum_m2,
    gz_commuting_differentials,
    holographic_r_matrix_d3,
    holographic_r_matrix_m2,
    koszul_complementarity_d3,
    koszul_complementarity_m2,
    sphere_shadow_amplitude,
    twisted_n4_F1,
    twisted_n4_F2,
    twisted_n4_F3,
    twisted_n4_genus_expansion,
    twisted_n4_kappa,
    verify_cybe_rational,
    witten_3pt_tree,
    witten_4pt_tree,
    witten_tadpole_oneloop,
    witten_vacuum_oneloop,
)


# ========================================================================
# Exact arithmetic helpers
# ========================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers used in lambda_g^FP computation."""

    def test_B0(self):
        assert _bernoulli_exact(0) == Fraction(1)

    def test_B1(self):
        assert _bernoulli_exact(1) == Fraction(-1, 2)

    def test_B2(self):
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            assert _bernoulli_exact(n) == Fraction(0)


class TestLambdaFP:
    """Verify Faber-Pandharipande numbers."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert _lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert _lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert _lambda_fp_exact(3) == Fraction(31, 967680)

    def test_genus_0_raises(self):
        with pytest.raises(ValueError):
            _lambda_fp_exact(0)


# ========================================================================
# D3 brane: twisted N=4 SYM
# ========================================================================

class TestTwistedN4Data:
    """Test D3 brane data (gl_N at level 1)."""

    def test_central_charge_N2(self):
        """c(gl_2, k=1) = 1*3/3 + 1 = 1 + 1 = 2."""
        data = TwistedN4Data(N=2)
        assert data.central_charge == Fraction(2)

    def test_central_charge_N3(self):
        """c(gl_3, k=1) = 1*8/4 + 1 = 2 + 1 = 3."""
        data = TwistedN4Data(N=3)
        assert data.central_charge == Fraction(3)

    def test_central_charge_N4(self):
        """c(gl_4, k=1) = 1*15/5 + 1 = 3 + 1 = 4."""
        data = TwistedN4Data(N=4)
        assert data.central_charge == Fraction(4)

    def test_central_charge_equals_N(self):
        """c(gl_N, k=1) = N for all N >= 2."""
        for N in range(2, 10):
            data = TwistedN4Data(N=N)
            assert data.central_charge == Fraction(N), f"Failed for N={N}"

    def test_kappa_sl_N2(self):
        """kappa_sl(sl_2, k=1) = 3*3/4 = 9/4."""
        data = TwistedN4Data(N=2)
        assert data.kappa_sl == Fraction(9, 4)

    def test_kappa_sl_N3(self):
        """kappa_sl(sl_3, k=1) = 8*4/6 = 32/6 = 16/3."""
        data = TwistedN4Data(N=3)
        assert data.kappa_sl == Fraction(16, 3)

    def test_kappa_u1(self):
        """kappa(u(1), k=1) = 1."""
        data = TwistedN4Data(N=2)
        assert data.kappa_u1 == Fraction(1)

    def test_kappa_total_N2(self):
        """kappa(gl_2, k=1) = 9/4 + 1 = 13/4."""
        data = TwistedN4Data(N=2)
        assert data.kappa == Fraction(13, 4)

    def test_kappa_total_N3(self):
        """kappa(gl_3, k=1) = 16/3 + 1 = 19/3."""
        data = TwistedN4Data(N=3)
        assert data.kappa == Fraction(19, 3)

    def test_kappa_total_N4(self):
        """kappa(gl_4, k=1) = 75/8 + 1 = 83/8."""
        data = TwistedN4Data(N=4)
        assert data.kappa == Fraction(83, 8)

    def test_shadow_depth(self):
        """Shadow depth = 3 (class L) for affine KM."""
        data = TwistedN4Data(N=5)
        assert data.shadow_depth == 3


class TestTwistedN4Kappa:
    """Test kappa computation for D3 brane."""

    def test_kappa_function_N2(self):
        assert twisted_n4_kappa(2, 1) == Fraction(13, 4)

    def test_kappa_function_N3(self):
        assert twisted_n4_kappa(3, 1) == Fraction(19, 3)

    def test_kappa_function_N4(self):
        assert twisted_n4_kappa(4, 1) == Fraction(83, 8)

    def test_kappa_positive(self):
        """kappa(gl_N, k=1) > 0 for all N >= 2."""
        for N in range(2, 15):
            assert twisted_n4_kappa(N, 1) > 0


class TestTwistedN4GenusExpansion:
    """Test genus expansion F_g = kappa * lambda_g^FP for D3 brane."""

    def test_F1_N2(self):
        """F_1(gl_2) = 13/4 * 1/24 = 13/96."""
        assert twisted_n4_F1(2) == Fraction(13, 96)

    def test_F1_N3(self):
        """F_1(gl_3) = 19/3 * 1/24 = 19/72."""
        assert twisted_n4_F1(3) == Fraction(19, 72)

    def test_F1_N4(self):
        """F_1(gl_4) = 83/8 * 1/24 = 83/192."""
        assert twisted_n4_F1(4) == Fraction(83, 192)

    def test_F2_N2(self):
        """F_2(gl_2) = 13/4 * 7/5760 = 91/23040."""
        expected = Fraction(13, 4) * Fraction(7, 5760)
        assert twisted_n4_F2(2) == expected

    def test_F2_N3(self):
        expected = Fraction(19, 3) * Fraction(7, 5760)
        assert twisted_n4_F2(3) == expected

    def test_F2_N4(self):
        expected = Fraction(83, 8) * Fraction(7, 5760)
        assert twisted_n4_F2(4) == expected

    def test_F3_N2(self):
        expected = Fraction(13, 4) * Fraction(31, 967680)
        assert twisted_n4_F3(2) == expected

    def test_genus_expansion_all_match(self):
        """Verify F_g = kappa * lambda_g^FP for N=2,3,4 and g=1..5."""
        for N in [2, 3, 4]:
            expansion = twisted_n4_genus_expansion(N, g_max=5)
            kappa = twisted_n4_kappa(N, 1)
            for g, fg in expansion.items():
                assert fg == kappa * _lambda_fp_exact(g), \
                    f"Mismatch at N={N}, g={g}"


# ========================================================================
# M2 brane: ABJM
# ========================================================================

class TestABJMShadowData:
    """Test ABJM shadow data."""

    def test_kappa_N1_k1(self):
        """kappa(ABJM(1,1)) = -1."""
        data = ABJMShadowData(N=1, k=1)
        assert data.kappa == Fraction(-1)

    def test_kappa_N2_k1(self):
        """kappa(ABJM(2,1)) = -4."""
        data = ABJMShadowData(N=2, k=1)
        assert data.kappa == Fraction(-4)

    def test_kappa_N3_k2(self):
        """kappa(ABJM(3,2)) = -9."""
        data = ABJMShadowData(N=3, k=2)
        assert data.kappa == Fraction(-9)

    def test_thooft_coupling(self):
        """lambda = N/k."""
        data = ABJMShadowData(N=3, k=2)
        assert data.thooft_coupling == Fraction(3, 2)

    def test_F1(self):
        """F_1(ABJM(N,k)) = -N^2/24."""
        for N in [1, 2, 3, 5]:
            data = ABJMShadowData(N=N, k=1)
            assert data.F_g(1) == Fraction(-N * N, 24)

    def test_shadow_depth_N1(self):
        """N=1: contact class C (shadow depth 4)."""
        data = ABJMShadowData(N=1, k=1)
        assert data.shadow_depth == 4

    def test_shadow_depth_N_ge_2(self):
        """N >= 2: mixed class M (shadow depth = infinity)."""
        for N in [2, 3, 5]:
            data = ABJMShadowData(N=N, k=1)
            assert data.shadow_depth == 1000


class TestABJMShadowInvariants:
    """Test the first 3 shadow invariants for ABJM."""

    def test_kappa_invariant(self):
        """Shadow 1 = kappa = -N^2."""
        result = abjm_shadow_invariants(3, 1, n_invariants=1)
        assert result["kappa"] == Fraction(-9)

    def test_cubic_shadow_vanishes(self):
        """Cubic shadow at scalar level vanishes for ABJM."""
        result = abjm_shadow_invariants(2, 1, n_invariants=2)
        assert result["cubic_shadow_scalar"] == Fraction(0)

    def test_quartic_contact_N1(self):
        """Q^contact at N=1: 10/[(-2)(12)] = -5/12."""
        result = abjm_shadow_invariants(1, 1, n_invariants=3)
        assert result["quartic_contact_scalar"] == Fraction(-5, 12)

    def test_three_invariants_returned(self):
        """All three invariants returned when requested."""
        result = abjm_shadow_invariants(1, 1, n_invariants=3)
        assert "kappa" in result
        assert "cubic_shadow_scalar" in result
        assert "quartic_contact_scalar" in result


# ========================================================================
# Bulk-boundary propagator
# ========================================================================

class TestBulkBoundaryPropagator:
    """Test bulk-to-boundary propagator construction."""

    def test_genus0_type(self):
        prop = bulk_boundary_genus0_glN(3)
        assert prop.propagator_type == "rational"
        assert prop.genus == 0

    def test_genus0_pole_order(self):
        """AP19: R-matrix pole order = OPE pole order - 1 = 1."""
        prop = bulk_boundary_genus0_glN(3)
        assert prop.leading_pole_order == 1

    def test_genus1_type(self):
        prop = bulk_boundary_genus1_glN(3)
        assert prop.propagator_type == "elliptic"
        assert prop.genus == 1

    def test_genus1_pole_order(self):
        """Genus-1 propagator also has simple pole."""
        prop = bulk_boundary_genus1_glN(3)
        assert prop.leading_pole_order == 1

    def test_casimir_type(self):
        prop = bulk_boundary_genus0_glN(4)
        assert prop.casimir_type == "gl_N"


# ========================================================================
# Witten diagrams from shadow obstruction tower
# ========================================================================

class TestWittenDiagrams:
    """Test Witten diagram amplitudes from shadow Feynman rules."""

    def test_3pt_tree_cubic_trivial(self):
        """3-point tree: cubic shadow trivial for KM at scalar level."""
        kappa = Fraction(13, 4)  # gl_2 at k=1
        wd = witten_3pt_tree(kappa)
        assert wd.genus == 0
        assert wd.n_external == 3
        assert wd.amplitude_scalar == Fraction(0)

    def test_4pt_tree_amplitude(self):
        """4-point tree: O(kappa^2) at scalar level."""
        kappa = Fraction(13, 4)
        wd = witten_4pt_tree(kappa)
        assert wd.genus == 0
        assert wd.n_external == 4
        assert wd.n_internal_edges == 1
        assert wd.amplitude_scalar == kappa * kappa

    def test_vacuum_oneloop(self):
        """Genus-1 vacuum: F_1 = kappa/24."""
        kappa = Fraction(13, 4)
        wd = witten_vacuum_oneloop(kappa)
        assert wd.genus == 1
        assert wd.amplitude_scalar == kappa * Fraction(1, 24)

    def test_tadpole_oneloop(self):
        """Genus-1 tadpole: amplitude = kappa/24."""
        kappa = Fraction(19, 3)
        wd = witten_tadpole_oneloop(kappa)
        assert wd.genus == 1
        assert wd.n_external == 1
        assert wd.amplitude_scalar == kappa * Fraction(1, 24)

    def test_vacuum_matches_F1(self):
        """Vacuum diagram amplitude equals F_1."""
        for N in [2, 3, 4]:
            kappa = twisted_n4_kappa(N, 1)
            wd = witten_vacuum_oneloop(kappa)
            assert wd.amplitude_scalar == twisted_n4_F1(N)


# ========================================================================
# Sphere reconstruction (GZ 2026)
# ========================================================================

class TestSphereReconstruction:
    """Test Gaiotto-Zinenko commuting differentials = scalar shadow."""

    def test_sh_02(self):
        """Sh_{0,2} = kappa."""
        kappa = Fraction(13, 4)
        assert sphere_shadow_amplitude(kappa, 2) == kappa

    def test_sh_03(self):
        """Sh_{0,3} = 0 (cubic shadow trivial for KM at scalar level)."""
        kappa = Fraction(13, 4)
        assert sphere_shadow_amplitude(kappa, 3) == Fraction(0)

    def test_sh_04(self):
        """Sh_{0,4} = 0 at scalar level."""
        kappa = Fraction(13, 4)
        assert sphere_shadow_amplitude(kappa, 4) == Fraction(0)

    def test_sh_05(self):
        """Sh_{0,5} = 0 at scalar level."""
        kappa = Fraction(19, 3)
        assert sphere_shadow_amplitude(kappa, 5) == Fraction(0)

    def test_arity_1_raises(self):
        """Arity < 2 raises ValueError."""
        with pytest.raises(ValueError):
            sphere_shadow_amplitude(Fraction(1), 1)

    def test_gz_commuting_differentials_structure(self):
        """GZ data has correct structure."""
        kappa = Fraction(13, 4)
        gz = gz_commuting_differentials(kappa, 4)
        assert gz["n"] == 4
        assert gz["genus"] == 0
        assert gz["is_flat"] is True
        assert gz["scalar_shadow"] == Fraction(0)
        assert gz["n_commuting_operators"] == 4

    def test_gz_n3_is_kz_type(self):
        """At n=3, the GZ connection is KZ-type."""
        gz = gz_commuting_differentials(Fraction(1), 3)
        assert gz["connection_type"] == "KZ-type"


# ========================================================================
# Holographic R-matrix
# ========================================================================

class TestHolographicRMatrix:
    """Test holographic R-matrix for D3 and M2."""

    def test_d3_residue_type(self):
        r = holographic_r_matrix_d3(3)
        assert r.residue_type == "Casimir/z"

    def test_d3_pole_order(self):
        """AP19: simple pole (1 below double-pole OPE)."""
        r = holographic_r_matrix_d3(3)
        assert r.leading_pole_order == 1

    def test_d3_cybe(self):
        r = holographic_r_matrix_d3(3)
        assert r.satisfies_cybe is True

    def test_d3_casimir_eigenvalue(self):
        """Casimir eigenvalue on adj(gl_N) = N."""
        for N in [2, 3, 4, 5]:
            r = holographic_r_matrix_d3(N)
            assert r.casimir_eigenvalue_adj == Fraction(N)

    def test_d3_scalar_trace_equals_kappa(self):
        """Scalar trace of r-matrix = kappa."""
        for N in [2, 3, 4]:
            r = holographic_r_matrix_d3(N)
            kappa = twisted_n4_kappa(N, 1)
            assert r.scalar_trace == kappa

    def test_m2_residue_type(self):
        r = holographic_r_matrix_m2(3, 1)
        assert r.residue_type == "Casimir/z"

    def test_m2_pole_order(self):
        r = holographic_r_matrix_m2(3, 1)
        assert r.leading_pole_order == 1

    def test_m2_cybe(self):
        r = holographic_r_matrix_m2(3, 1)
        assert r.satisfies_cybe is True

    def test_m2_scalar_trace(self):
        """Scalar trace for ABJM = kappa = -N^2."""
        r = holographic_r_matrix_m2(3, 1)
        assert r.scalar_trace == Fraction(-9)

    def test_cybe_verification_d3(self):
        result = verify_cybe_rational("Casimir/z", 3)
        assert result["satisfies_cybe"] is True

    def test_cybe_verification_m2(self):
        result = verify_cybe_rational("Casimir/z", 5)
        assert result["satisfies_cybe"] is True


# ========================================================================
# Anomaly matching
# ========================================================================

class TestAnomalyMatching:
    """Test kappa_eff = kappa(matter) + kappa(ghost) = 0."""

    def test_d3_anomaly_free(self):
        """D3 brane: kappa_eff = 0."""
        a = anomaly_matching_d3(3)
        assert a.kappa_eff == Fraction(0)
        assert a.is_anomaly_free is True

    def test_d3_matter_plus_ghost(self):
        """kappa(ghost) = -kappa(matter)."""
        for N in [2, 3, 4, 5]:
            a = anomaly_matching_d3(N)
            assert a.kappa_matter + a.kappa_ghost == Fraction(0)

    def test_d3_kappa_matter_positive(self):
        """kappa(matter) > 0 for gl_N at level 1."""
        for N in [2, 3, 4]:
            a = anomaly_matching_d3(N)
            assert a.kappa_matter > 0

    def test_m2_anomaly_free(self):
        """M2 brane: kappa_eff = 0."""
        a = anomaly_matching_m2(3, 1)
        assert a.kappa_eff == Fraction(0)
        assert a.is_anomaly_free is True

    def test_m2_matter_ghost(self):
        """ABJM: kappa(matter) = -2N^2, kappa(ghost) = 2N^2."""
        for N in [1, 2, 3]:
            a = anomaly_matching_m2(N, 1)
            assert a.kappa_matter == Fraction(-2 * N * N)
            assert a.kappa_ghost == Fraction(2 * N * N)

    def test_anomaly_distinguishes_kappa_from_kappa_eff(self):
        """AP29: kappa(A) != kappa_eff in general.

        kappa(gl_N) is the modular characteristic of the BOUNDARY ALGEBRA.
        kappa_eff = kappa(matter) + kappa(ghost) = 0 is anomaly cancellation.
        These are different: kappa(gl_N) != 0 but kappa_eff = 0.
        """
        a = anomaly_matching_d3(3)
        kappa_A = twisted_n4_kappa(3, 1)
        assert kappa_A != Fraction(0)  # kappa(A) is nonzero
        assert a.kappa_eff == Fraction(0)  # kappa_eff is zero
        assert kappa_A != a.kappa_eff  # They are different!


# ========================================================================
# Koszul complementarity
# ========================================================================

class TestKoszulComplementarity:
    """Test kappa(A) + kappa(A!) = 0 for both brane systems."""

    def test_d3_anti_symmetric(self):
        """D3: kappa(gl_N) + kappa(gl_N)^! = 0."""
        for N in [2, 3, 4, 5]:
            result = koszul_complementarity_d3(N)
            assert result["anti_symmetric"] is True, f"Failed for N={N}"
            assert result["sum"] == Fraction(0), f"Failed for N={N}"

    def test_d3_kappa_dual(self):
        """kappa(A!) = -kappa(A) for D3."""
        for N in [2, 3, 4]:
            result = koszul_complementarity_d3(N)
            kappa = twisted_n4_kappa(N, 1)
            assert result["kappa_A_dual"] == -kappa

    def test_m2_anti_symmetric(self):
        """M2: kappa(ABJM) + kappa(ABJM!) = 0."""
        for N in [1, 2, 3]:
            result = koszul_complementarity_m2(N, 1)
            assert result["anti_symmetric"] is True
            assert result["sum"] == Fraction(0)

    def test_m2_kappa_dual(self):
        """kappa(ABJM!) = N^2 = -kappa(ABJM)."""
        result = koszul_complementarity_m2(3, 1)
        assert result["kappa_A_dual"] == Fraction(9)


# ========================================================================
# Comprehensive summary and cross-checks
# ========================================================================

class TestFullDatum:
    """Test complete holographic datum extraction."""

    def test_d3_full_datum_N2(self):
        datum = full_twisted_holography_datum_d3(2)
        assert datum["kappa(A)"] == Fraction(13, 4)
        assert datum["anti_symmetric"] is True
        assert datum["satisfies_cybe"] is True
        assert datum["anomaly_free"] is True
        assert datum["kappa_eff"] == Fraction(0)
        assert datum["connection_flat"] is True

    def test_d3_full_datum_N3(self):
        datum = full_twisted_holography_datum_d3(3)
        assert datum["kappa(A)"] == Fraction(19, 3)
        assert datum["c(A)"] == Fraction(3)

    def test_m2_full_datum(self):
        datum = full_twisted_holography_datum_m2(2, 1)
        assert datum["kappa(A)"] == Fraction(-4)
        assert datum["anti_symmetric"] is True
        assert datum["anomaly_free"] is True
        assert datum["shadow_depth"] == 1000  # class M

    def test_m2_full_datum_N1(self):
        datum = full_twisted_holography_datum_m2(1, 1)
        assert datum["kappa(A)"] == Fraction(-1)
        assert datum["shadow_depth"] == 4  # class C


class TestCrossChecks:
    """Cross-check consistency of all components."""

    def test_cross_check_d3_N2(self):
        result = cross_check_d3_genus_expansion(2, g_max=5)
        assert result["all_match"] is True

    def test_cross_check_d3_N3(self):
        result = cross_check_d3_genus_expansion(3, g_max=5)
        assert result["all_match"] is True

    def test_cross_check_d3_N4(self):
        result = cross_check_d3_genus_expansion(4, g_max=3)
        assert result["all_match"] is True

    def test_F1_positive_d3(self):
        """F_1 > 0 for D3 (kappa > 0)."""
        for N in [2, 3, 4, 5]:
            assert twisted_n4_F1(N) > 0

    def test_F1_negative_m2(self):
        """F_1 < 0 for M2 (kappa < 0)."""
        for N in [1, 2, 3]:
            data = ABJMShadowData(N=N, k=1)
            assert data.F_g(1) < 0

    def test_r_matrix_pole_order_AP19(self):
        """AP19: r-matrix pole order = 1 (one below OPE double pole)."""
        for N in [2, 3, 4]:
            r = holographic_r_matrix_d3(N)
            assert r.leading_pole_order == 1

    def test_complementarity_plus_anomaly_consistency(self):
        """kappa(A) + kappa(A!) = 0 and kappa_eff = 0 are DIFFERENT conditions.

        For D3: kappa(A) != 0, kappa(A!) = -kappa(A), kappa_eff = 0.
        Both hold but for different reasons (AP29).
        """
        for N in [2, 3, 4]:
            comp = koszul_complementarity_d3(N)
            anom = anomaly_matching_d3(N)
            # Both zero, but from different mechanisms
            assert comp["sum"] == Fraction(0)
            assert anom.kappa_eff == Fraction(0)
            # But kappa(A) is the same in both
            assert comp["kappa_A"] == anom.kappa_matter

    def test_witten_vacuum_matches_genus_expansion(self):
        """Witten vacuum amplitude = F_1 from genus expansion."""
        for N in [2, 3, 4]:
            kappa = twisted_n4_kappa(N, 1)
            wd = witten_vacuum_oneloop(kappa)
            f1 = twisted_n4_F1(N)
            assert wd.amplitude_scalar == f1

    def test_sphere_sh02_matches_kappa(self):
        """Sh_{0,2} = kappa for all N."""
        for N in [2, 3, 4]:
            kappa = twisted_n4_kappa(N, 1)
            assert sphere_shadow_amplitude(kappa, 2) == kappa

    def test_shadow_depth_classification(self):
        """D3 (affine KM) = class L (depth 3), M2 (N>=2) = class M (depth inf)."""
        d3 = TwistedN4Data(N=3)
        m2_small = ABJMShadowData(N=1, k=1)
        m2_large = ABJMShadowData(N=3, k=1)
        assert d3.shadow_depth == 3      # class L
        assert m2_small.shadow_depth == 4  # class C
        assert m2_large.shadow_depth == 1000  # class M
