"""Tests for twisted_holography_engine: Costello-Li programme via modular Koszul duality.

Organization:
  1. GL(1) Chern-Simons: full holographic datum
  2. GL(N) Chern-Simons: Gaberdiel-Gopakumar at N=2,3,4,5
  3. Anomaly cancellation (c=26, all affine families)
  4. Holographic shadow connection properties
  5. Entanglement entropy leading order
  6. GZ commuting differentials from MC
  7. Multi-path boundary-bulk map (annulus, Hochschild, shadow)
  8. Koszul pair verification for each holographic pair
  9. M2 brane (ABJM) holographic data
  10. Twisted M-theory on CY5
  11. Collision residue and CYBE
  12. Comprehensive sweeps
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.twisted_holography_engine import (
    # Constructors
    make_heisenberg,
    make_affine_gl_N,
    make_affine_sl_N,
    make_virasoro,
    make_w_N,
    make_bc_ghosts,
    make_abjm,
    make_cy5_m5,
    # Koszul dual
    koszul_dual,
    feigin_frenkel_dual_level,
    # Holographic datum
    extract_holographic_datum,
    gl1_holographic_datum,
    gl1_boundary_bulk_map,
    gl1_complementarity,
    gl_N_holographic_datum,
    # Gaberdiel-Gopakumar
    gaberdiel_gopakumar_data,
    gaberdiel_gopakumar_boundary_bulk,
    thooft_coupling_sl_N,
    kappa_sl_N,
    kappa_anti_symmetry_sl_N,
    # ABJM
    abjm_holographic_datum,
    abjm_shadow_data,
    # CY5
    cy5_holographic_datum,
    cy5_m5_genus_expansion,
    # Shadow connection
    holographic_shadow_connection,
    shadow_connection_flatness_check,
    # Anomaly cancellation
    anomaly_cancellation_bosonic_string,
    anomaly_cancellation_affine,
    anomaly_cancellation_general,
    # Entanglement
    holographic_entanglement,
    entanglement_leading_order,
    entanglement_quantum_correction_depth,
    # GZ differentials
    gz_differentials,
    gz_from_mc_equation,
    # Multi-path
    three_path_F1_verification,
    F_g_value,
    genus_expansion,
    complementarity_at_genus,
    # Koszul pair
    verify_koszul_pair,
    collision_residue,
    # Sweeps
    full_holographic_sweep,
    anomaly_cancellation_sweep,
    koszul_pair_sweep,
    # Internals
    _lambda_fp_exact,
    _bernoulli_exact,
)


# ===========================================================================
# 1. GL(1) Chern-Simons: full holographic datum
# ===========================================================================

class TestGL1ChernSimons:
    """GL(1) CS at level k: the simplest twisted holography example."""

    def test_heisenberg_construction(self):
        H = make_heisenberg(Fraction(1))
        assert H.family == "heisenberg"
        assert H.rank == 1
        assert H.kappa == Fraction(1)
        assert H.central_charge == Fraction(1)
        assert H.shadow_depth == 2

    def test_heisenberg_kappa_equals_level(self):
        """AP39/AP48: kappa(H_k) = k, NOT c/2 = 1/2."""
        for k in [1, 2, 3, 5, 10]:
            H = make_heisenberg(Fraction(k))
            assert H.kappa == Fraction(k), f"kappa(H_{k}) should be {k}, got {H.kappa}"

    def test_gl1_datum_extraction(self):
        datum = gl1_holographic_datum(Fraction(1))
        assert datum.A.name == "H_1"
        assert datum.A.kappa == Fraction(1)
        assert datum.A_dual.kappa == Fraction(-1)
        assert datum.kappa_sum == Fraction(0)
        assert datum.complementarity_type == "anti-symmetric"
        assert datum.connection_is_flat is True

    def test_gl1_datum_at_level_k(self):
        for k in [1, 2, 5]:
            datum = gl1_holographic_datum(Fraction(k))
            assert datum.kappa_sum == Fraction(0)
            assert datum.theta_kappa == Fraction(k)

    def test_gl1_koszul_dual_is_not_h_minus_k(self):
        """AP33: H_k^! = Sym^ch(V*), NOT H_{-k} as algebra.
        But kappa(H_k^!) = -k = kappa(H_{-k})."""
        H = make_heisenberg(Fraction(3))
        H_dual = koszul_dual(H)
        assert H_dual.kappa == Fraction(-3)
        # The name reflects that this is Sym^ch(V*), not H_{-3}
        assert "Sym" in H_dual.name or "!" in H_dual.name
        assert H_dual.family == "heisenberg_dual"

    def test_gl1_boundary_bulk_map(self):
        bbm = gl1_boundary_bulk_map(Fraction(1))
        assert bbm.kappa == Fraction(1)
        assert bbm.F_1_annulus == Fraction(1, 24)
        assert bbm.F_1_hochschild == Fraction(1, 24)
        assert bbm.F_1_shadow == Fraction(1, 24)
        assert bbm.three_paths_agree is True

    def test_gl1_complementarity(self):
        comp = gl1_complementarity(Fraction(1))
        assert comp["sum"] == Fraction(0)
        assert comp["complementarity_holds"] is True

    def test_gl1_complementarity_all_levels(self):
        for k in [1, 2, 3, 5, 7, 10]:
            comp = gl1_complementarity(Fraction(k))
            assert comp["sum"] == Fraction(0), f"Failed at k={k}"

    def test_gl1_collision_residue(self):
        H = make_heisenberg(Fraction(1))
        r = collision_residue(H)
        assert r["residue_type"] == "scalar/z"
        assert r["max_pole_order"] == 1
        assert r["satisfies_cybe"] is True

    def test_gl1_shadow_depth(self):
        H = make_heisenberg(Fraction(1))
        assert H.shadow_depth == 2  # Gaussian class G


# ===========================================================================
# 2. GL(N) Chern-Simons: Gaberdiel-Gopakumar at N=2,3,4,5
# ===========================================================================

class TestGLNChernSimons:
    """GL(N) CS and the Gaberdiel-Gopakumar duality."""

    def test_affine_sl2_construction(self):
        A = make_affine_sl_N(2, Fraction(1))
        assert A.rank == 2
        assert A.dim_lie == 3
        assert A.dual_coxeter == 2
        # c = 1*3/(1+2) = 1
        assert A.central_charge == Fraction(1)
        # kappa = 3*3/(2*2) = 9/4
        assert A.kappa == Fraction(3) * Fraction(3) / (2 * 2)

    def test_affine_sl3_construction(self):
        A = make_affine_sl_N(3, Fraction(2))
        assert A.dim_lie == 8
        assert A.dual_coxeter == 3
        # c = 2*8/(2+3) = 16/5
        assert A.central_charge == Fraction(16, 5)

    def test_kappa_anti_symmetry_sl2(self):
        result = kappa_anti_symmetry_sl_N(2, Fraction(1))
        assert result["anti_symmetric"] is True
        assert result["sum"] == Fraction(0)

    def test_kappa_anti_symmetry_sl3(self):
        result = kappa_anti_symmetry_sl_N(3, Fraction(2))
        assert result["anti_symmetric"] is True
        assert result["sum"] == Fraction(0)

    def test_kappa_anti_symmetry_sl4(self):
        result = kappa_anti_symmetry_sl_N(4, Fraction(3))
        assert result["anti_symmetric"] is True

    def test_kappa_anti_symmetry_sl5(self):
        result = kappa_anti_symmetry_sl_N(5, Fraction(4))
        assert result["anti_symmetric"] is True

    @pytest.mark.parametrize("N,k", [(2, 1), (3, 2), (4, 3), (5, 4), (3, 5), (4, 1)])
    def test_kappa_anti_symmetry_parametric(self, N, k):
        """Kappa anti-symmetry for sl(N) at various levels."""
        result = kappa_anti_symmetry_sl_N(N, Fraction(k))
        assert result["anti_symmetric"] is True, f"Failed for sl({N})_{k}"

    def test_gaberdiel_gopakumar_N2(self):
        gg = gaberdiel_gopakumar_data(2, Fraction(3))
        assert gg.N == 2
        assert gg.boundary_bulk_match is True
        assert gg.c_boundary == gg.c_bulk

    def test_gaberdiel_gopakumar_N3(self):
        gg = gaberdiel_gopakumar_data(3, Fraction(4))
        assert gg.boundary_bulk_match is True

    def test_gaberdiel_gopakumar_N4(self):
        gg = gaberdiel_gopakumar_data(4, Fraction(5))
        assert gg.boundary_bulk_match is True

    def test_gaberdiel_gopakumar_N5(self):
        gg = gaberdiel_gopakumar_data(5, Fraction(6))
        assert gg.boundary_bulk_match is True

    def test_gaberdiel_gopakumar_boundary_bulk_map(self):
        bbm = gaberdiel_gopakumar_boundary_bulk(3, Fraction(4))
        assert bbm.three_paths_agree is True
        assert bbm.F_1_annulus == bbm.F_1_shadow

    def test_thooft_coupling(self):
        # lambda = N/(k+N) = 2/(1+2) = 2/3
        lam = thooft_coupling_sl_N(2, Fraction(1))
        assert lam == Fraction(2, 3)

    def test_thooft_coupling_sl3(self):
        lam = thooft_coupling_sl_N(3, Fraction(2))
        assert lam == Fraction(3, 5)

    def test_feigin_frenkel_dual_level(self):
        """k' = -k - 2h^v. For sl(2): k' = -k - 4."""
        k_dual = feigin_frenkel_dual_level(Fraction(1), 2)
        assert k_dual == Fraction(-5)

    def test_feigin_frenkel_dual_level_sl3(self):
        k_dual = feigin_frenkel_dual_level(Fraction(2), 3)
        assert k_dual == Fraction(-8)

    def test_gl_N_holographic_datum(self):
        datum = gl_N_holographic_datum(2, Fraction(1))
        assert datum.connection_is_flat is True
        assert datum.collision_residue_type == "Casimir/z"

    def test_collision_residue_affine(self):
        A = make_affine_sl_N(3, Fraction(2))
        r = collision_residue(A)
        assert r["residue_type"] == "Casimir/z"
        assert r["max_pole_order"] == 1  # AP19: only z^{-1}
        assert r["satisfies_cybe"] is True
        # Casimir eigenvalue on adj = 2h^v = 6
        assert r["leading_coefficient"] == Fraction(6)


# ===========================================================================
# 3. Anomaly cancellation
# ===========================================================================

class TestAnomalyCancellation:
    """Anomaly cancellation at critical dimension and for affine families."""

    def test_bosonic_string_c26(self):
        """kappa(Vir_26) + kappa(bc) = 26/2 + (-13) = 0."""
        ac = anomaly_cancellation_bosonic_string(Fraction(26))
        assert ac.boundary_kappa == Fraction(13)
        assert ac.ghost_kappa == Fraction(-13)
        assert ac.total == Fraction(0)
        assert ac.cancels is True
        assert ac.critical_value == Fraction(26)

    def test_bosonic_string_c25_no_cancel(self):
        ac = anomaly_cancellation_bosonic_string(Fraction(25))
        assert ac.total == Fraction(-1, 2)
        assert ac.cancels is False

    def test_bosonic_string_c1_no_cancel(self):
        ac = anomaly_cancellation_bosonic_string(Fraction(1))
        assert ac.cancels is False

    @pytest.mark.parametrize("N,k", [(2, 1), (3, 2), (4, 3), (5, 4)])
    def test_affine_anomaly_cancellation(self, N, k):
        """For affine sl(N): kappa + kappa' = 0 at all levels."""
        ac = anomaly_cancellation_affine(N, Fraction(k))
        assert ac.cancels is True, f"Failed for sl({N})_{k}"

    def test_heisenberg_anomaly_cancellation(self):
        A = make_heisenberg(Fraction(1))
        ac = anomaly_cancellation_general(A)
        assert ac.cancels is True

    def test_virasoro_no_koszul_cancellation(self):
        """Virasoro: kappa + kappa' = 13, NOT 0 (AP24)."""
        A = make_virasoro(Fraction(10))
        ac = anomaly_cancellation_general(A)
        # kappa = 5, kappa' = (26-10)/2 = 8. Sum = 13.
        assert ac.total == Fraction(13)
        assert ac.cancels is False

    def test_virasoro_self_dual_c13(self):
        """At c=13: kappa = kappa' = 13/2, sum = 13."""
        A = make_virasoro(Fraction(13))
        ac = anomaly_cancellation_general(A)
        assert ac.boundary_kappa == Fraction(13, 2)
        assert ac.ghost_kappa == Fraction(13, 2)
        assert ac.total == Fraction(13)

    def test_anomaly_cancellation_sweep(self):
        results = anomaly_cancellation_sweep()
        # All affine should cancel
        for key, val in results.items():
            if "sl(" in key or "H_" in key or "c26" in key:
                assert val is True, f"Expected cancellation for {key}"
        # c=25 should NOT cancel
        assert results["bosonic_string_c25_NOT_cancel"] is True


# ===========================================================================
# 4. Holographic shadow connection properties
# ===========================================================================

class TestShadowConnection:
    """Properties of nabla^hol = d - Sh_{g,n}(Theta_A)."""

    def test_heisenberg_flat(self):
        """Heisenberg: shadow connection has no singularity (depth 2)."""
        H = make_heisenberg(Fraction(1))
        conn = holographic_shadow_connection(H, 0, 2)
        assert conn.singularity_type == "none"
        assert conn.is_flat is True

    def test_affine_logarithmic(self):
        """Affine: shadow connection has logarithmic singularities (depth 3)."""
        A = make_affine_sl_N(2, Fraction(1))
        conn = holographic_shadow_connection(A, 0, 2)
        assert conn.singularity_type == "logarithmic"
        assert conn.is_flat is True
        assert conn.is_kz_type is True  # KZ at (0,2)

    def test_virasoro_essential(self):
        """Virasoro: shadow connection has essential singularity (depth inf)."""
        V = make_virasoro(Fraction(10))
        conn = holographic_shadow_connection(V, 0, 2)
        assert conn.singularity_type == "essential"
        assert conn.is_flat is True

    def test_affine_kz_at_genus0(self):
        """Affine at genus 0 specializes to KZ connection."""
        A = make_affine_sl_N(3, Fraction(2))
        conn = holographic_shadow_connection(A, 0, 3)
        assert conn.is_kz_type is True

    def test_affine_not_kz_at_genus1(self):
        """At genus >= 1, connection is not of KZ type."""
        A = make_affine_sl_N(2, Fraction(1))
        conn = holographic_shadow_connection(A, 1, 1)
        assert conn.is_kz_type is False

    def test_flatness_sweep(self):
        """Flatness at all (g, n) with 2g-2+n > 0."""
        A = make_affine_sl_N(2, Fraction(1))
        results = shadow_connection_flatness_check(A, max_arity=4)
        for (g, n), is_flat in results.items():
            assert is_flat is True, f"nabla not flat at (g={g}, n={n})"

    def test_flatness_heisenberg(self):
        H = make_heisenberg(Fraction(1))
        results = shadow_connection_flatness_check(H, max_arity=4)
        for (g, n), is_flat in results.items():
            assert is_flat is True


# ===========================================================================
# 5. Entanglement entropy leading order
# ===========================================================================

class TestEntanglement:
    """Holographic entanglement entropy from the shadow CohFT."""

    def test_leading_order_virasoro(self):
        """S_EE = (c/3) log(L/eps)."""
        V = make_virasoro(Fraction(26))
        ee = holographic_entanglement(V)
        assert ee.leading_coefficient == Fraction(26, 3)
        assert ee.has_quantum_corrections is True  # depth infinity

    def test_leading_order_heisenberg(self):
        H = make_heisenberg(Fraction(1))
        ee = holographic_entanglement(H)
        assert ee.leading_coefficient == Fraction(1, 3)
        assert ee.has_quantum_corrections is False  # depth 2, Gaussian

    def test_leading_order_affine(self):
        A = make_affine_sl_N(2, Fraction(1))
        ee = holographic_entanglement(A)
        # c = 1 for sl(2)_1
        assert ee.leading_coefficient == Fraction(1, 3)
        assert ee.has_quantum_corrections is True  # depth 3

    def test_entanglement_coefficient(self):
        assert entanglement_leading_order(Fraction(12)) == Fraction(4)
        assert entanglement_leading_order(Fraction(1)) == Fraction(1, 3)

    def test_quantum_correction_depth_gaussian(self):
        H = make_heisenberg(Fraction(1))
        assert entanglement_quantum_correction_depth(H) == 0

    def test_quantum_correction_depth_lie(self):
        A = make_affine_sl_N(2, Fraction(1))
        assert entanglement_quantum_correction_depth(A) == 1

    def test_quantum_correction_depth_contact(self):
        A = make_abjm(1, 1)
        assert entanglement_quantum_correction_depth(A) == 2

    def test_quantum_correction_depth_mixed(self):
        V = make_virasoro(Fraction(10))
        assert entanglement_quantum_correction_depth(V) == -1  # infinite


# ===========================================================================
# 6. GZ commuting differentials from MC
# ===========================================================================

class TestGZDifferentials:
    """Gaiotto-Zhang differentials as arity-2 MC projection."""

    def test_gz_from_heisenberg(self):
        H = make_heisenberg(Fraction(1))
        gz = gz_differentials(H)
        assert gz.d1_squared_vanishes is True
        assert gz.d2_squared_vanishes is True
        assert gz.anticommutator_vanishes is True
        assert gz.is_mc_projection is True

    def test_gz_from_affine(self):
        A = make_affine_sl_N(2, Fraction(1))
        gz = gz_differentials(A)
        assert gz.d1_squared_vanishes is True
        assert gz.d2_squared_vanishes is True
        assert gz.anticommutator_vanishes is True

    def test_gz_from_virasoro(self):
        V = make_virasoro(Fraction(26))
        gz = gz_differentials(V)
        assert gz.d1_squared_vanishes is True
        assert gz.d2_squared_vanishes is True
        assert gz.anticommutator_vanishes is True

    def test_gz_mc_equation_components(self):
        result = gz_from_mc_equation(Fraction(13, 2))
        assert result["d1_squared"] == Fraction(0)
        assert result["d2_squared"] == Fraction(0)
        assert result["anticommutator"] == Fraction(0)
        assert result["bar_complex_d_squared_zero"] is True
        assert result["sewing_d_squared_zero"] is True
        assert result["leibniz_compatibility"] is True

    def test_gz_kappa_dependence(self):
        """GZ differentials depend on kappa."""
        for kappa in [Fraction(1), Fraction(13, 2), Fraction(0)]:
            result = gz_from_mc_equation(kappa)
            assert result["kappa"] == kappa
            assert result["structure_from_mc"] is True


# ===========================================================================
# 7. Multi-path boundary-bulk map
# ===========================================================================

class TestMultiPathVerification:
    """Three-path verification of F_1: annulus, Hochschild, shadow."""

    def test_three_paths_heisenberg(self):
        H = make_heisenberg(Fraction(1))
        bbm = three_path_F1_verification(H)
        assert bbm.three_paths_agree is True
        assert bbm.F_1_annulus == Fraction(1, 24)

    def test_three_paths_affine(self):
        A = make_affine_sl_N(2, Fraction(1))
        bbm = three_path_F1_verification(A)
        assert bbm.three_paths_agree is True
        # kappa(sl(2)_1) = 3*3/(2*2) = 9/4
        expected_F1 = Fraction(9, 4) / 24
        assert bbm.F_1_annulus == expected_F1

    def test_three_paths_virasoro(self):
        V = make_virasoro(Fraction(26))
        bbm = three_path_F1_verification(V)
        assert bbm.three_paths_agree is True
        # kappa(Vir_26) = 13
        assert bbm.F_1_annulus == Fraction(13, 24)

    def test_three_paths_w3(self):
        W = make_w_N(3, Fraction(4))
        bbm = three_path_F1_verification(W)
        assert bbm.three_paths_agree is True

    def test_three_paths_abjm(self):
        A = make_abjm(2, 1)
        bbm = three_path_F1_verification(A)
        assert bbm.three_paths_agree is True
        # kappa(ABJM(2,1)) = -4
        assert bbm.F_1_annulus == Fraction(-4, 24)

    @pytest.mark.parametrize("k", [1, 2, 3, 5, 10])
    def test_three_paths_heisenberg_all_levels(self, k):
        H = make_heisenberg(Fraction(k))
        bbm = three_path_F1_verification(H)
        assert bbm.three_paths_agree is True
        assert bbm.F_1_annulus == Fraction(k, 24)

    def test_F1_equals_kappa_over_24(self):
        """Universal genus-1 formula: F_1 = kappa/24."""
        algebras = [
            make_heisenberg(Fraction(1)),
            make_affine_sl_N(2, Fraction(1)),
            make_virasoro(Fraction(10)),
            make_w_N(3, Fraction(4)),
            make_abjm(1, 1),
        ]
        for A in algebras:
            F1 = F_g_value(A.kappa, 1)
            assert F1 == A.kappa / 24, f"F_1 != kappa/24 for {A.name}"


# ===========================================================================
# 8. Koszul pair verification
# ===========================================================================

class TestKoszulPairs:
    """Verify Koszul pairs for each holographic example."""

    def test_koszul_pair_heisenberg(self):
        H = make_heisenberg(Fraction(1))
        pair = verify_koszul_pair(H)
        assert pair["kappa_sum"] == Fraction(0)
        assert pair["shadow_class"] == "G"
        assert pair["datum_complete"] is True

    def test_koszul_pair_affine_sl2(self):
        A = make_affine_sl_N(2, Fraction(1))
        pair = verify_koszul_pair(A)
        assert pair["kappa_sum"] == Fraction(0)
        assert pair["shadow_class"] == "L"

    def test_koszul_pair_affine_sl3(self):
        A = make_affine_sl_N(3, Fraction(2))
        pair = verify_koszul_pair(A)
        assert pair["kappa_sum"] == Fraction(0)
        assert pair["shadow_class"] == "L"

    def test_koszul_pair_virasoro(self):
        V = make_virasoro(Fraction(10))
        pair = verify_koszul_pair(V)
        # kappa(10) + kappa(16) = 5 + 8 = 13
        assert pair["kappa_sum"] == Fraction(13)
        assert pair["shadow_class"] == "M"

    def test_koszul_pair_virasoro_self_dual(self):
        V = make_virasoro(Fraction(13))
        pair = verify_koszul_pair(V)
        assert pair["kappa_A"] == pair["kappa_A_dual"]
        assert pair["kappa_sum"] == Fraction(13)

    def test_koszul_pair_abjm(self):
        A = make_abjm(2, 1)
        pair = verify_koszul_pair(A)
        assert pair["kappa_sum"] == Fraction(0)

    def test_koszul_pair_sweep(self):
        results = koszul_pair_sweep()
        for name, complete in results.items():
            assert complete is True, f"Koszul pair incomplete for {name}"

    def test_virasoro_dual_is_virasoro(self):
        """Vir_c! = Vir_{26-c}."""
        V = make_virasoro(Fraction(10))
        V_dual = koszul_dual(V)
        assert V_dual.central_charge == Fraction(16)
        assert V_dual.kappa == Fraction(8)

    def test_affine_dual_level(self):
        """sl(N)_k dual at k' = -k - 2N."""
        A = make_affine_sl_N(3, Fraction(2))
        A_dual = koszul_dual(A)
        assert A_dual.level == Fraction(-8)  # -2 - 6

    def test_genus_expansion_heisenberg(self):
        H = make_heisenberg(Fraction(1))
        fe = genus_expansion(H, max_genus=3)
        assert fe[1] == Fraction(1, 24)
        assert fe[2] == Fraction(7, 5760)
        assert fe[3] == Fraction(31, 967680)

    def test_complementarity_at_genus_affine(self):
        """Q_g(A) + Q_g(A!) = 0 at all genera for affine."""
        A = make_affine_sl_N(2, Fraction(1))
        for g in range(1, 5):
            comp = complementarity_at_genus(A, g)
            assert comp["balanced"] is True, f"Not balanced at g={g}"

    def test_complementarity_at_genus_virasoro(self):
        """Q_g(A) + Q_g(A!) = 13 * lambda_g for Virasoro."""
        V = make_virasoro(Fraction(10))
        for g in range(1, 4):
            comp = complementarity_at_genus(V, g)
            expected = Fraction(13) * _lambda_fp_exact(g)
            assert comp["total"] == expected, f"Wrong at g={g}"


# ===========================================================================
# 9. M2 brane (ABJM)
# ===========================================================================

class TestABJM:
    """M2 brane holographic data."""

    def test_abjm_construction(self):
        A = make_abjm(1, 1)
        assert A.central_charge == Fraction(-2)
        assert A.kappa == Fraction(-1)
        assert A.shadow_depth == 4  # contact class

    def test_abjm_construction_N2(self):
        A = make_abjm(2, 1)
        assert A.central_charge == Fraction(-8)
        assert A.kappa == Fraction(-4)
        assert A.shadow_depth == 1000  # mixed class

    def test_abjm_kappa_scaling(self):
        """kappa(ABJM(N,k)) = -N^2 for all k."""
        for N in [1, 2, 3, 4, 5]:
            A = make_abjm(N, 1)
            assert A.kappa == Fraction(-N * N)

    def test_abjm_complementarity(self):
        """kappa + kappa' = 0 for ABJM."""
        datum = abjm_holographic_datum(2, 1)
        assert datum.kappa_sum == Fraction(0)

    def test_abjm_shadow_data(self):
        sd = abjm_shadow_data(2, 1)
        assert sd["kappa"] == Fraction(-4)
        assert sd["F_1"] == Fraction(-4, 24)
        assert sd["shadow_class"] == "M"

    def test_abjm_shadow_data_N1(self):
        sd = abjm_shadow_data(1, 1)
        assert sd["shadow_class"] == "C"  # contact at N=1

    def test_abjm_F1_formula(self):
        """F_1 = kappa/24 = -N^2/24."""
        for N in [1, 2, 3]:
            sd = abjm_shadow_data(N, 1)
            assert sd["F_1"] == Fraction(-N * N, 24)

    def test_abjm_genus_expansion(self):
        sd = abjm_shadow_data(2, 1)
        # F_1 = -4/24 = -1/6
        assert sd["F_g"][1] == Fraction(-1, 6)
        # F_2 = -4 * 7/5760 = -28/5760 = -7/1440
        assert sd["F_g"][2] == Fraction(-4) * Fraction(7, 5760)


# ===========================================================================
# 10. Twisted M-theory on CY5
# ===========================================================================

class TestCY5:
    """Twisted M-theory: M5 wrapping divisor in CY5."""

    def test_cy5_construction(self):
        A = make_cy5_m5(Fraction(12), Fraction(6))
        assert A.family == "cy5"
        assert A.central_charge == Fraction(12)
        assert A.kappa == Fraction(6)

    def test_cy5_datum(self):
        datum = cy5_holographic_datum(Fraction(12), Fraction(6))
        assert datum.A.kappa == Fraction(6)
        assert datum.A_dual.kappa == Fraction(-6)
        assert datum.kappa_sum == Fraction(0)

    def test_cy5_genus_expansion(self):
        fe = cy5_m5_genus_expansion(Fraction(12), Fraction(6), max_genus=3)
        assert fe[1] == Fraction(6, 24)
        assert fe[1] == Fraction(1, 4)


# ===========================================================================
# 11. Collision residue and CYBE
# ===========================================================================

class TestCollisionResidue:
    """r(z) = Res^{coll}_{0,2}(Theta_A) and CYBE."""

    def test_heisenberg_residue(self):
        H = make_heisenberg(Fraction(3))
        r = collision_residue(H)
        assert r["residue_type"] == "scalar/z"
        assert r["max_pole_order"] == 1
        assert r["leading_coefficient"] == Fraction(3)

    def test_affine_residue(self):
        A = make_affine_sl_N(3, Fraction(2))
        r = collision_residue(A)
        assert r["residue_type"] == "Casimir/z"
        assert r["max_pole_order"] == 1
        # Casimir on adj = 2*h^v = 6
        assert r["leading_coefficient"] == Fraction(6)

    def test_virasoro_residue(self):
        """Virasoro r-matrix: pole at z^{-3} and z^{-1} (AP19)."""
        V = make_virasoro(Fraction(10))
        r = collision_residue(V)
        assert r["max_pole_order"] == 3
        assert r["satisfies_cybe"] is True

    def test_w3_residue(self):
        """W_3 r-matrix: pole up to z^{-5} (OPE pole 6, minus 1 from d log)."""
        W = make_w_N(3, Fraction(4))
        r = collision_residue(W)
        assert r["max_pole_order"] == 5  # 2*3 - 1

    def test_cybe_all_families(self):
        """CYBE satisfied for all families (by MC + Arnold)."""
        algebras = [
            make_heisenberg(Fraction(1)),
            make_affine_sl_N(2, Fraction(1)),
            make_affine_sl_N(3, Fraction(2)),
            make_virasoro(Fraction(10)),
            make_w_N(3, Fraction(4)),
            make_abjm(2, 1),
        ]
        for A in algebras:
            r = collision_residue(A)
            assert r["satisfies_cybe"] is True, f"CYBE failed for {A.name}"


# ===========================================================================
# 12. Comprehensive sweeps
# ===========================================================================

class TestComprehensiveSweeps:
    """Full holographic verification sweeps."""

    def test_full_sweep(self):
        results = full_holographic_sweep()
        assert len(results) >= 10
        for name, data in results.items():
            assert data["datum_complete"] is True, f"Incomplete for {name}"

    def test_koszul_pair_sweep_all_complete(self):
        results = koszul_pair_sweep()
        assert len(results) >= 9
        for name, complete in results.items():
            assert complete is True

    def test_anomaly_sweep(self):
        results = anomaly_cancellation_sweep()
        assert results["bosonic_string_c26"] is True

    def test_lambda_fp_values(self):
        """Verify lambda_g^FP values (cross-check with existing modules)."""
        assert _lambda_fp_exact(1) == Fraction(1, 24)
        assert _lambda_fp_exact(2) == Fraction(7, 5760)
        assert _lambda_fp_exact(3) == Fraction(31, 967680)

    def test_bernoulli_values(self):
        """Verify Bernoulli numbers used in lambda_g^FP."""
        assert _bernoulli_exact(0) == Fraction(1)
        assert _bernoulli_exact(1) == Fraction(-1, 2)
        assert _bernoulli_exact(2) == Fraction(1, 6)
        assert _bernoulli_exact(4) == Fraction(-1, 30)
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_F_g_additivity(self):
        """F_g(A + B) = F_g(A) + F_g(B) when kappa is additive."""
        k1, k2 = Fraction(3), Fraction(5)
        for g in range(1, 4):
            F1 = F_g_value(k1, g)
            F2 = F_g_value(k2, g)
            F_sum = F_g_value(k1 + k2, g)
            assert F1 + F2 == F_sum, f"Additivity fails at g={g}"


# ===========================================================================
# 13. Additional cross-checks and edge cases
# ===========================================================================

class TestEdgeCases:
    """Edge cases and cross-checks."""

    def test_critical_level_raises(self):
        """k = -h^v should raise."""
        with pytest.raises(ValueError):
            make_affine_sl_N(2, Fraction(-2))

    def test_kappa_at_level_0(self):
        """sl(N) at k=0: non-critical but degenerate."""
        A = make_affine_sl_N(2, Fraction(0))
        # kappa = 3*2/(2*2) = 3/2
        assert A.kappa == Fraction(3, 2)

    def test_virasoro_c0(self):
        """Vir at c=0: kappa = 0, uncurved bar complex."""
        V = make_virasoro(Fraction(0))
        assert V.kappa == Fraction(0)

    def test_virasoro_c26(self):
        """Vir at c=26: kappa = 13, dual at c=0."""
        V = make_virasoro(Fraction(26))
        V_dual = koszul_dual(V)
        assert V_dual.central_charge == Fraction(0)
        assert V_dual.kappa == Fraction(0)

    def test_bc_ghost_construction(self):
        bc = make_bc_ghosts()
        assert bc.central_charge == Fraction(-26)
        assert bc.kappa == Fraction(-13)

    def test_heisenberg_at_high_level(self):
        H = make_heisenberg(Fraction(100))
        assert H.kappa == Fraction(100)
        datum = extract_holographic_datum(H)
        assert datum.kappa_sum == Fraction(0)

    def test_large_N_affine(self):
        """Large N: kappa grows as N^2."""
        A_10 = make_affine_sl_N(10, Fraction(5))
        A_20 = make_affine_sl_N(20, Fraction(5))
        # kappa(sl_N, k) = (N^2-1)(k+N)/(2N), grows ~ N^2/2 * (k+N)/N ~ N(k+N)/2
        assert A_20.kappa > A_10.kappa

    def test_w_N_virasoro_specialization(self):
        """W^k(sl_2) = Virasoro at c = 1 - 6(k+1)^2/(k+2)."""
        W = make_w_N(2, Fraction(3))
        # c = 1 - 2*3*(3+1)^2/(3+2) = 1 - 6*16/5 = 1 - 96/5 = -91/5
        assert W.central_charge == Fraction(-91, 5)

    def test_holographic_datum_bulk_description(self):
        H = make_heisenberg(Fraction(1))
        datum = extract_holographic_datum(H)
        assert "Fock" in datum.bulk_description

    def test_holographic_datum_affine_bulk(self):
        A = make_affine_sl_N(3, Fraction(2))
        datum = extract_holographic_datum(A)
        assert "Higher-spin" in datum.bulk_description or "W" in datum.bulk_description
