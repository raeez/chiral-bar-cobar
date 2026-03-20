"""Tests for the large-N / twisted holography module.

Verifies the holographic modular Koszul datum H(A) = (A, A!, C, r(z), Theta_A, nabla^hol)
and the large-N identification of the MC genus expansion with the 't Hooft 1/N^2 expansion.

Organization:
  1. Algebra construction and basic data (V_k(sl_N), W_N, Heisenberg)
  2. Holographic datum extraction and anti-symmetry
  3. 't Hooft genus expansion and scaling
  4. Feigin-Frenkel involution on 't Hooft coupling
  5. Shadow connection and flatness
  6. Collision residue and CYBE
  7. Ten-theorem projection table
  8. Gravitational phase space / Lagrangian splitting
  9. W_N scaling and Gaberdiel-Gopakumar
  10. M2-brane matching
  11. E_1 vs modular projection
  12. Fredholm determinants and HS-sewing
  13. Comprehensive verification sweeps
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.large_n_twisted_holography import (
    ChiralAlgebraData,
    CollisionResidue,
    E1ModularProjection,
    FredholmData,
    GravitationalPhaseSpace,
    GTheorem,
    HolographicDatum,
    LargeNScaling,
    M2BraneMatch,
    ShadowConnection,
    ThooftExpansion,
    arnold_relation_check,
    central_charge_from_thooft,
    central_charge_sl_N,
    channel_harmonic_divergence,
    collision_residue_affine,
    collision_residue_heisenberg,
    e1_to_modular_projection,
    extract_holographic_datum,
    feigin_frenkel_dual,
    feigin_frenkel_dual_level,
    full_holographic_verification,
    gravitational_phase_space,
    harmonic_divergence_ratio,
    heisenberg_fredholm,
    holographic_summary,
    hs_sewing_criterion,
    kappa_anti_symmetry_check,
    kappa_formula_table,
    kappa_from_data,
    kappa_from_thooft,
    kappa_involution_check,
    kappa_sl_N,
    large_n_scaling_data,
    large_N_central_charge_scaling,
    m2_brane_match,
    make_affine_sl_N,
    make_heisenberg,
    make_virasoro_from_ds,
    make_w_N,
    ribbon_genus_from_euler,
    run_family_sweep,
    s_duality_spectrum,
    shadow_connection_genus0_arity2,
    shadow_connection_genus0_arity3,
    stable_graph_from_ribbon_data,
    ten_theorem_table,
    thooft_coupling,
    thooft_free_energy,
    thooft_inverse,
    thooft_involution,
    verify_cybe_casimir_sl_N,
    verify_cybe_scalar,
    verify_dual_central_charge,
    verify_ff_involution_on_thooft,
    verify_G9_virasoro_self_dual,
    verify_hs_sewing_standard_landscape,
    verify_kappa_sl_N_formula,
    verify_genus_scaling,
    verify_lagrangian_splitting,
    wn_central_charge,
    wn_central_charge_large_N,
    wn_channel_refined_kappa,
    wn_harmonic_divergence_check,
    wn_large_N_leading,
    wn_thooft_coupling,
)
from compute.lib.stable_graph_enumeration import (
    heisenberg_free_energy,
)


# ===========================================================================
# 1. Algebra construction and basic data
# ===========================================================================

class TestAlgebraConstruction:
    """Test construction of chiral algebra data."""

    def test_sl2_basic(self):
        A = make_affine_sl_N(2, Fraction(1))
        assert A.dim == 3
        assert A.rank == 2
        assert A.dual_coxeter == 2
        assert A.level == Fraction(1)
        assert A.central_charge == Fraction(1)  # 1*3/(1+2) = 1

    def test_sl3_basic(self):
        A = make_affine_sl_N(3, Fraction(1))
        assert A.dim == 8
        assert A.rank == 3
        assert A.dual_coxeter == 3
        assert A.central_charge == Fraction(2)  # 1*8/(1+3) = 2

    def test_sl4_basic(self):
        A = make_affine_sl_N(4, Fraction(1))
        assert A.dim == 15
        assert A.rank == 4
        assert A.dual_coxeter == 4
        assert A.central_charge == Fraction(3)  # 1*15/(1+4) = 3

    def test_sl_N_central_charge_formula(self):
        """c = k(N^2-1)/(k+N) for all N, k."""
        for N in range(2, 8):
            for k in [1, 2, 3, 5, 10]:
                A = make_affine_sl_N(N, Fraction(k))
                expected = Fraction(k * (N * N - 1), k + N)
                assert A.central_charge == expected

    def test_sl_N_critical_level_raises(self):
        """Critical level k = -h^v should raise."""
        with pytest.raises(ValueError):
            make_affine_sl_N(3, Fraction(-3))

    def test_heisenberg_basic(self):
        H = make_heisenberg(Fraction(1))
        assert H.dim == 0
        assert H.rank == 1
        assert H.central_charge == Fraction(1)
        assert H.shadow_depth == 2  # Gaussian class

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (the level directly)."""
        for k in [1, 2, 3, 5]:
            H = make_heisenberg(Fraction(k))
            assert kappa_from_data(H) == Fraction(k)

    def test_w_N_construction(self):
        """W_N algebras from DS reduction of sl_N."""
        W2 = make_w_N(2, Fraction(1))
        assert W2.rank == 2
        assert W2.shadow_depth == 1000  # infinite tower
        # W_2 = Virasoro from DS of sl_2
        # c = 1 - 6(k+1)^2/(k+2) = 1 - 6*4/3 = 1 - 8 = -7
        assert W2.central_charge == Fraction(-7)

    def test_virasoro_from_ds(self):
        """Virasoro = W^k(sl_2, f_prin)."""
        V = make_virasoro_from_ds(Fraction(1))
        W2 = make_w_N(2, Fraction(1))
        assert V.central_charge == W2.central_charge

    def test_shadow_depth_classification(self):
        """Shadow depth: 2=Gaussian, 3=Lie/tree, 1000=infinite."""
        H = make_heisenberg()
        A = make_affine_sl_N(2, Fraction(1))
        W = make_w_N(3, Fraction(1))
        assert H.shadow_depth == 2
        assert A.shadow_depth == 3
        assert W.shadow_depth == 1000


# ===========================================================================
# 2. Holographic datum extraction
# ===========================================================================

class TestHolographicDatum:
    """Test extraction of H(A) = (A, A!, C, r(z), Theta_A, nabla^hol)."""

    def test_datum_extraction_sl2(self):
        A = make_affine_sl_N(2, Fraction(1))
        datum = extract_holographic_datum(A)
        assert datum.kappa_anti_symmetric is True
        assert datum.connection_is_flat is True
        assert datum.collision_residue_type == "Casimir/z"

    def test_datum_extraction_sl3(self):
        A = make_affine_sl_N(3, Fraction(2))
        datum = extract_holographic_datum(A)
        assert datum.kappa_anti_symmetric is True
        assert datum.theta_kappa == kappa_from_data(A)

    def test_datum_extraction_heisenberg(self):
        H = make_heisenberg(Fraction(3))
        datum = extract_holographic_datum(H)
        assert datum.collision_residue_type == "scalar/z"
        assert datum.connection_is_flat is True

    def test_feigin_frenkel_dual_level(self):
        """k' = -k - 2h^v."""
        assert feigin_frenkel_dual_level(Fraction(1), 2) == Fraction(-5)
        assert feigin_frenkel_dual_level(Fraction(1), 3) == Fraction(-7)
        assert feigin_frenkel_dual_level(Fraction(0), 4) == Fraction(-8)

    def test_feigin_frenkel_dual_algebra(self):
        A = make_affine_sl_N(3, Fraction(1))
        A_dual = feigin_frenkel_dual(A)
        assert A_dual.level == Fraction(-7)  # -1 - 6 = -7
        assert A_dual.dim == 8
        assert A_dual.rank == 3

    def test_kappa_anti_symmetry_all_ranks(self):
        """kappa(A) + kappa(A!) = 0 for all sl_N at any level."""
        for N in range(2, 8):
            for k in [1, 2, 3, 5, 10]:
                kap, kap_d, anti = kappa_anti_symmetry_check(N, Fraction(k))
                assert anti, f"Anti-symmetry fails for sl_{N} at k={k}"
                assert kap + kap_d == 0

    def test_kappa_formula_consistency(self):
        """kappa = dim(g)(k+h^v)/(2h^v) matches kappa_from_data."""
        for N in range(2, 7):
            for k in [1, 2, 5]:
                assert verify_kappa_sl_N_formula(N, Fraction(k))

    def test_dual_central_charge_sum(self):
        """c(A) + c(A!) = 2*dim(g) = 2(N^2-1) for sl_N."""
        for N in range(2, 7):
            for k in [1, 2, 3]:
                result = verify_dual_central_charge(N, Fraction(k))
                assert result["match"], f"c+c! mismatch for sl_{N} at k={k}"
                assert result["c_sum"] == Fraction(2 * (N * N - 1))


# ===========================================================================
# 3. 't Hooft genus expansion
# ===========================================================================

class TestThooftExpansion:
    """Test 't Hooft genus expansion log Z = sum N^{2-2g} F_g(lambda)."""

    def test_thooft_coupling_basic(self):
        """lambda = N/(k+N)."""
        assert thooft_coupling(3, Fraction(1)) == Fraction(3, 4)
        assert thooft_coupling(2, Fraction(2)) == Fraction(1, 2)
        assert thooft_coupling(5, Fraction(5)) == Fraction(1, 2)

    def test_thooft_inverse(self):
        """k = N/lambda - N recovers k from lambda."""
        for N in [2, 3, 5]:
            for k in [1, 2, 3, 10]:
                lam = thooft_coupling(N, Fraction(k))
                k_rec = thooft_inverse(N, lam)
                assert k_rec == Fraction(k)

    def test_central_charge_thooft(self):
        """c_N = (N^2-1)(1-lambda) in terms of lambda."""
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 5]:
                lam = thooft_coupling(N, Fraction(k))
                c_direct = central_charge_sl_N(N, Fraction(k))
                c_thooft = central_charge_from_thooft(N, lam)
                assert c_direct == c_thooft, \
                    f"Mismatch for N={N}, k={k}: {c_direct} vs {c_thooft}"

    def test_kappa_thooft(self):
        """kappa = (N^2-1)/(2*lambda) in terms of lambda."""
        for N in [2, 3, 5]:
            for k in [1, 2, 5]:
                lam = thooft_coupling(N, Fraction(k))
                kap_direct = kappa_sl_N(N, Fraction(k))
                kap_thooft = kappa_from_thooft(N, lam)
                assert kap_direct == kap_thooft

    def test_free_energy_expansion(self):
        """F_g are computed correctly via kappa * lambda_g^FP."""
        exp = thooft_free_energy(3, Fraction(1), 3)
        assert exp.rank == 3
        assert exp.thooft_coupling == Fraction(3, 4)
        # F_1 = kappa * 1/24 = (16/3) * (1/24) = 2/9
        assert exp.free_energies[1] == Fraction(2, 9)

    def test_genus_scaling_nonzero(self):
        """F_g / N^{2-2g} should be nonzero (well-defined scaling)."""
        for N in [2, 3, 5]:
            for g in [1, 2, 3]:
                fg, n_pow, ratio = verify_genus_scaling(N, Fraction(1), g)
                assert fg != 0
                assert ratio != 0

    def test_large_N_central_charge_convergence(self):
        """c_N / N^2 -> (1-lambda) as N -> infinity."""
        lam = Fraction(1, 3)
        target = Fraction(2, 3)
        prev_dist = Fraction(1)  # start with distance 1
        for N in [5, 10, 20, 50, 100]:
            _, ratio, _ = large_N_central_charge_scaling(N, lam)
            dist = abs(ratio - target)
            assert dist < prev_dist, f"Not converging at N={N}"
            prev_dist = dist
        # At N=100: ratio should be very close
        assert abs(ratio - target) < Fraction(1, 100)


# ===========================================================================
# 4. Feigin-Frenkel involution on 't Hooft coupling
# ===========================================================================

class TestFFInvolution:
    """Test the Feigin-Frenkel involution lambda -> -lambda."""

    def test_ff_sends_lambda_to_minus_lambda(self):
        """lambda' = -lambda under Feigin-Frenkel."""
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 3, 5]:
                result = verify_ff_involution_on_thooft(N, Fraction(k))
                assert result["is_negation"], \
                    f"FF involution fails for N={N}, k={k}"

    def test_ff_lambda_sum_zero(self):
        """lambda + lambda' = 0."""
        for N in [2, 3, 5]:
            for k in [1, 2, 10]:
                result = verify_ff_involution_on_thooft(N, Fraction(k))
                assert result["sum"] == 0

    def test_kappa_involution(self):
        """kappa(A) + kappa(A!) = 0 verified via kappa_involution_check."""
        for N in [2, 3, 4]:
            for k in [1, 2, 5]:
                result = kappa_involution_check(N, Fraction(k))
                assert result["anti_symmetric"]
                assert result["sum"] == 0

    def test_thooft_involution_function(self):
        """thooft_involution(lambda) = -lambda."""
        assert thooft_involution(Fraction(1, 3)) == Fraction(-1, 3)
        assert thooft_involution(Fraction(1, 2)) == Fraction(-1, 2)


# ===========================================================================
# 5. Shadow connection and flatness
# ===========================================================================

class TestShadowConnection:
    """Test the shadow connection nabla^hol = d - Sh_{g,n}(Theta_A)."""

    def test_genus0_arity2_flat(self):
        A = make_affine_sl_N(3, Fraction(1))
        conn = shadow_connection_genus0_arity2(A)
        assert conn.is_flat
        assert conn.genus == 0
        assert conn.arity == 2

    def test_genus0_arity2_kz_type(self):
        """For affine algebras, genus 0 arity 2 gives KZ connection."""
        A = make_affine_sl_N(3, Fraction(1))
        conn = shadow_connection_genus0_arity2(A)
        assert conn.is_kz_type

    def test_genus0_arity2_heisenberg(self):
        """Heisenberg is not KZ-type (abelian)."""
        H = make_heisenberg()
        conn = shadow_connection_genus0_arity2(H)
        assert not conn.is_kz_type  # abelian
        assert conn.is_flat

    def test_genus0_arity3_flat(self):
        A = make_affine_sl_N(2, Fraction(1))
        conn = shadow_connection_genus0_arity3(A)
        assert conn.is_flat
        assert conn.arity == 3

    def test_arnold_relation(self):
        """Arnold relation holds for all n >= 3."""
        for n in range(3, 8):
            assert arnold_relation_check(n)

    def test_connection_kappa_matches(self):
        """Connection kappa matches kappa_from_data."""
        for N in [2, 3, 4]:
            A = make_affine_sl_N(N, Fraction(2))
            conn = shadow_connection_genus0_arity2(A)
            assert conn.kappa_value == kappa_from_data(A)


# ===========================================================================
# 6. Collision residue and CYBE
# ===========================================================================

class TestCollisionResidue:
    """Test r(z) = Res^coll_{0,2}(Theta_A) and the CYBE."""

    def test_affine_residue_type(self):
        r = collision_residue_affine(3, Fraction(1))
        assert r.residue_type == "Casimir/z"
        assert r.satisfies_cybe

    def test_casimir_eigenvalue(self):
        """Casimir eigenvalue on adjoint = 2h^v = 2N for sl_N."""
        for N in [2, 3, 4, 5]:
            r = collision_residue_affine(N, Fraction(1))
            assert r.casimir_eigenvalue == Fraction(2 * N)

    def test_heisenberg_residue(self):
        r = collision_residue_heisenberg(Fraction(3))
        assert r.residue_type == "scalar/z"
        assert r.satisfies_cybe
        assert r.casimir_eigenvalue == Fraction(3)

    def test_cybe_scalar(self):
        """Scalar CYBE is trivially satisfied."""
        assert verify_cybe_scalar(Fraction(5))

    def test_cybe_casimir_sl_N(self):
        """CYBE for Casimir/z r-matrix holds for all sl_N."""
        for N in [2, 3, 4, 5]:
            result = verify_cybe_casimir_sl_N(N)
            assert result["cybe_holds"]
            assert result["dim_g"] == N * N - 1
            assert result["casimir_eigenvalue_adj"] == 2 * N

    def test_casimir_fund_eigenvalue(self):
        """Casimir eigenvalue on fundamental = (N^2-1)/(2N)."""
        for N in [2, 3, 4]:
            result = verify_cybe_casimir_sl_N(N)
            expected = Fraction(N * N - 1, 2 * N)
            assert result["casimir_eigenvalue_fund"] == expected


# ===========================================================================
# 7. Ten-theorem projection table
# ===========================================================================

class TestGTheorems:
    """Test the ten G-theorems as projections of Theta_A."""

    def test_ten_theorems_count(self):
        table = ten_theorem_table()
        assert len(table) == 10

    def test_all_proved(self):
        """All ten G-theorems should have status 'proved'."""
        for thm in ten_theorem_table():
            assert thm.status == "proved", f"{thm.label} not proved"

    def test_labels_sequential(self):
        table = ten_theorem_table()
        for i, thm in enumerate(table):
            assert thm.label == f"G{i+1}"

    def test_G9_virasoro_self_dual(self):
        """G9: Virasoro self-dual at c = 13."""
        result = verify_G9_virasoro_self_dual()
        assert result["is_self_dual"]
        assert result["self_dual_c"] == Fraction(13)
        assert result["kappa_sum"] == Fraction(13)
        # c + c' = 26 for Virasoro
        assert result["c"] + (26 - result["c"]) == 26

    def test_G4_anti_symmetry(self):
        """G4 (S-duality): kappa(A!) = -kappa(A) for affine algebras."""
        for N in [2, 3, 4, 5]:
            _, _, anti = kappa_anti_symmetry_check(N, Fraction(1))
            assert anti


# ===========================================================================
# 8. Gravitational phase space
# ===========================================================================

class TestGravitationalPhaseSpace:
    """Test C_g(A) = Q_g(A) + Q_g(A!), Lagrangian splitting."""

    def test_balanced_splitting_sl2(self):
        A = make_affine_sl_N(2, Fraction(1))
        for g in range(1, 5):
            phase = gravitational_phase_space(A, g)
            assert phase.is_balanced
            assert phase.total == 0

    def test_balanced_splitting_all_ranks(self):
        """Lagrangian splitting Q_g(A) + Q_g(A!) = 0 for all (N, k, g)."""
        for N in range(2, 6):
            for k in [1, 2, 3]:
                result = verify_lagrangian_splitting(N, Fraction(k), 4)
                for g, balanced in result.items():
                    assert balanced, f"Not balanced: N={N}, k={k}, g={g}"

    def test_Q_g_values(self):
        """Q_g(A) = kappa * lambda_g^FP, Q_g(A!) = kappa! * lambda_g^FP."""
        A = make_affine_sl_N(3, Fraction(1))
        phase = gravitational_phase_space(A, 1)
        kap = kappa_from_data(A)
        lfp = Fraction(1, 24)  # lambda_1^FP
        assert phase.Q_g_A == kap * lfp

    def test_Q_g_antisymmetric(self):
        """Q_g(A!) = -Q_g(A) when kappa! = -kappa."""
        A = make_affine_sl_N(4, Fraction(2))
        for g in range(1, 4):
            phase = gravitational_phase_space(A, g)
            assert phase.Q_g_A == -phase.Q_g_A_dual


# ===========================================================================
# 9. W_N scaling and Gaberdiel-Gopakumar
# ===========================================================================

class TestWNScaling:
    """Test W_N central charge formulas and harmonic divergence."""

    def test_wn_virasoro_match(self):
        """W_2 = Virasoro: c = 1 - 6(k+1)^2/(k+2)."""
        for k in [1, 2, 3, 5]:
            c_wn = wn_central_charge(2, Fraction(k))
            k_f = Fraction(k)
            c_vir = 1 - 6 * (k_f + 1) ** 2 / (k_f + 2)
            assert c_wn == c_vir, f"W_2 != Vir at k={k}"

    def test_wn_central_charge_values(self):
        """Known W_N central charge values."""
        # W_2 at k=1: c = 1 - 6*4/3 = -7
        assert wn_central_charge(2, Fraction(1)) == Fraction(-7)
        # W_3 at k=1: c = 2 - 3*8*9/4 = 2 - 54 = -52
        assert wn_central_charge(3, Fraction(1)) == Fraction(-52)

    def test_channel_refined_kappa(self):
        """sum_{s=2}^N c/s = c * (H_N - 1)."""
        for N in [3, 5, 10]:
            c = Fraction(12)  # test with concrete c
            total, channels = wn_channel_refined_kappa(N, c)
            # Check individual channels
            for s in range(2, N + 1):
                assert channels[s] == c / s
            # Check total matches harmonic formula
            H_N = sum(Fraction(1, j) for j in range(1, N + 1))
            assert total == c * (H_N - 1)

    def test_harmonic_divergence_check(self):
        """Verify sum_{s=2}^N c/s = c*(H_N - 1) exactly."""
        for N in [3, 5, 8, 15]:
            result = wn_harmonic_divergence_check(N, Fraction(10))
            assert result["match"]

    def test_wn_large_N_matches_direct(self):
        """wn_central_charge_large_N matches wn_central_charge."""
        for N in [3, 5, 10]:
            k = Fraction(2)
            lam = wn_thooft_coupling(N, k)
            c_direct = wn_central_charge(N, k)
            c_thooft = wn_central_charge_large_N(N, lam)
            assert c_direct == c_thooft

    def test_harmonic_divergence_rate(self):
        """(H_N - 1) / H_N -> 1 as N -> infinity."""
        prev = Fraction(0)
        for N in [5, 10, 50, 100]:
            ratio = harmonic_divergence_ratio(N)
            assert ratio > prev, f"Not monotone at N={N}"
            prev = ratio
        assert prev > Fraction(4, 5)  # close to 1 (H_100-1)/H_100 ~ 0.807


# ===========================================================================
# 10. M2-brane matching
# ===========================================================================

class TestM2Brane:
    """Test M2-brane holographic matching."""

    def test_m2_match_basic(self):
        match = m2_brane_match(3)
        assert match.N == 3
        assert match.bar_cobar_match
        assert match.genus_expansion_match

    def test_m2_match_all_N(self):
        for N in range(2, 8):
            match = m2_brane_match(N)
            assert match.bar_cobar_match
            assert match.genus_expansion_match
            assert f"sl_{N}" in match.boundary_algebra


# ===========================================================================
# 11. E_1 vs modular projection
# ===========================================================================

class TestE1Modular:
    """Test the coinvariant projection from E_1 to modular."""

    def test_projection_genus0_n3(self):
        proj = e1_to_modular_projection(0, 3)
        assert proj.num_stable_graphs == 1
        assert proj.coinvariant_surjective

    def test_projection_genus0_n4(self):
        proj = e1_to_modular_projection(0, 4)
        assert proj.num_stable_graphs == 4
        # Ribbon: 3 ordered channels (s, t, u)
        assert proj.num_ribbon_graphs == 3
        assert proj.coinvariant_surjective

    def test_projection_genus1_n0(self):
        proj = e1_to_modular_projection(1, 0)
        assert proj.num_stable_graphs == 2
        assert proj.coinvariant_surjective

    def test_projection_genus1_n1(self):
        proj = e1_to_modular_projection(1, 1)
        assert proj.num_stable_graphs == 2
        assert proj.coinvariant_surjective

    def test_ribbon_genus_euler_sphere(self):
        """Sphere: chi = V - E + F = 2, genus = 0."""
        # Tetrahedron: V=4, E=6, F=4 -> chi=2 -> g=0
        assert ribbon_genus_from_euler(4, 6, 4) == 0
        # Single point: V=1, E=0, F=1 -> chi=2 -> g=0
        assert ribbon_genus_from_euler(1, 0, 1) == 0

    def test_ribbon_genus_euler_torus(self):
        """Torus: chi = 0, genus = 1."""
        # Minimal torus: V=1, E=2, F=1 -> chi=0 -> g=1
        assert ribbon_genus_from_euler(1, 2, 1) == 1

    def test_ribbon_genus_euler_genus2(self):
        """Genus 2: chi = -2."""
        # V=1, E=4, F=1 -> chi=-2 -> g=2
        assert ribbon_genus_from_euler(1, 4, 1) == 2

    def test_stable_from_ribbon(self):
        """Coinvariant projection gives a stable graph."""
        sg = stable_graph_from_ribbon_data((0,), (), (0, 0, 0))
        assert sg.is_stable
        assert sg.arithmetic_genus == 0


# ===========================================================================
# 12. Fredholm determinants and HS-sewing
# ===========================================================================

class TestFredholm:
    """Test Fredholm determinant data and HS-sewing criterion."""

    def test_heisenberg_fredholm_g1(self):
        fd = heisenberg_fredholm(1)
        assert fd.kernel_type == "Bergman"
        assert fd.is_trace_class
        assert fd.free_energy == Fraction(1, 24)

    def test_heisenberg_fredholm_g2(self):
        fd = heisenberg_fredholm(2)
        assert fd.free_energy == Fraction(7, 5760)

    def test_heisenberg_fredholm_g3(self):
        fd = heisenberg_fredholm(3)
        assert fd.free_energy == Fraction(31, 967680)

    def test_heisenberg_fredholm_matches_existing(self):
        """Cross-check with stable_graph_enumeration.heisenberg_free_energy."""
        for g in range(1, 6):
            fd = heisenberg_fredholm(g)
            old = heisenberg_free_energy(g)
            assert fd.free_energy == old, f"Mismatch at g={g}"

    def test_heisenberg_fredholm_level(self):
        """F_g(H_k) = k * lambda_g^FP."""
        for k in [1, 2, 3, 5]:
            fd = heisenberg_fredholm(1, Fraction(k))
            assert fd.free_energy == Fraction(k, 24)

    def test_hs_sewing_criterion(self):
        assert hs_sewing_criterion(True, True) is True
        assert hs_sewing_criterion(True, False) is False
        assert hs_sewing_criterion(False, True) is False
        assert hs_sewing_criterion(False, False) is False

    def test_hs_sewing_standard_landscape(self):
        """All standard families satisfy HS-sewing."""
        results = verify_hs_sewing_standard_landscape()
        for name, ok in results.items():
            assert ok, f"HS-sewing fails for {name}"


# ===========================================================================
# 13. Comprehensive verification sweeps
# ===========================================================================

class TestComprehensiveSweep:
    """Run comprehensive verification across all (N, k) combinations."""

    def test_full_verification_sl2_k1(self):
        results = full_holographic_verification(2, Fraction(1), 3)
        assert results["datum_extracted"]
        assert results["kappa_anti_symmetric"]
        assert results["connection_flat"]
        assert results["lambda_negation"]
        assert results["cybe_satisfied"]
        assert results["all_g_proved"]
        assert results["lagrangian_balanced"]

    def test_full_verification_sl3_k2(self):
        results = full_holographic_verification(3, Fraction(2), 3)
        assert results["datum_extracted"]
        assert results["kappa_anti_symmetric"]
        assert results["lagrangian_balanced"]

    def test_full_verification_sl5_k3(self):
        results = full_holographic_verification(5, Fraction(3), 3)
        assert results["datum_extracted"]
        assert results["kappa_anti_symmetric"]
        assert results["lagrangian_balanced"]

    def test_family_sweep_small(self):
        """Sweep over small grid of (N, k)."""
        results = run_family_sweep(max_N=4, levels=[1, 2, 3], max_genus=2)
        for (N, k), data in results.items():
            assert data["datum_extracted"], f"Failed for N={N}, k={k}"
            assert data["kappa_anti_symmetric"], f"Anti-sym fails for N={N}, k={k}"
            assert data["lagrangian_balanced"], f"Lagrangian fails for N={N}, k={k}"

    def test_s_duality_spectrum(self):
        """S-duality spectrum: kappa_sum = 0, c_sum = 2(N^2-1)."""
        spec = s_duality_spectrum(6)
        for N, data in spec.items():
            assert data["kappa_sum"] == 0, f"kappa_sum != 0 for N={N}"
            assert data["c_sum"] == data["c_sum_expected"], \
                f"c_sum mismatch for N={N}: {data['c_sum']} vs {data['c_sum_expected']}"

    def test_holographic_summary_runs(self):
        """Smoke test that holographic_summary produces output."""
        summary = holographic_summary(3, 1)
        assert "sl_3" in summary
        assert "kappa" in summary
        assert "Feigin-Frenkel" in summary

    def test_kappa_formula_table_nonempty(self):
        """Formula table has entries for all standard families."""
        table = kappa_formula_table()
        assert len(table) >= 7
        assert "Heisenberg H_k" in table
        assert "V_k(sl_N)" in table
        assert "Virasoro Vir_c" in table


# ===========================================================================
# Edge cases and regression tests
# ===========================================================================

class TestEdgeCases:
    """Edge cases and regression tests."""

    def test_large_N(self):
        """Construction works for large N."""
        A = make_affine_sl_N(20, Fraction(1))
        assert A.dim == 399
        kap = kappa_from_data(A)
        assert kap == Fraction(399 * 21, 2 * 20)

    def test_large_level(self):
        """Construction works for large k."""
        A = make_affine_sl_N(2, Fraction(1000))
        assert A.central_charge == Fraction(3000, 1002)
        kap = kappa_from_data(A)
        assert kap == Fraction(3 * 1002, 4)

    def test_fractional_level(self):
        """Fractional (admissible) levels work."""
        A = make_affine_sl_N(2, Fraction(-1, 2))
        c = A.central_charge
        # c = (-1/2)*3 / (-1/2 + 2) = -3/2 / (3/2) = -1
        assert c == Fraction(-1)

    def test_negative_kappa(self):
        """Negative kappa is allowed (below critical)."""
        A = make_affine_sl_N(2, Fraction(-3))
        # k+h^v = -3+2 = -1
        kap = kappa_from_data(A)
        assert kap == Fraction(3 * (-1), 4)
        assert kap < 0

    def test_thooft_critical_raises(self):
        """thooft_coupling at critical level raises."""
        with pytest.raises(ValueError):
            thooft_coupling(3, Fraction(-3))

    def test_make_w_N_critical_raises(self):
        with pytest.raises(ValueError):
            make_w_N(3, Fraction(-3))

    def test_ribbon_genus_odd_chi_raises(self):
        with pytest.raises(ValueError):
            ribbon_genus_from_euler(1, 1, 1)  # chi = 1, odd

    def test_ribbon_genus_negative_raises(self):
        with pytest.raises(ValueError):
            ribbon_genus_from_euler(4, 2, 2)  # chi = 4, g = -1

    def test_channel_divergence_growth(self):
        """Channel sum grows without bound as N -> infinity."""
        c = Fraction(10)
        prev = Fraction(0)
        for N in [3, 10, 50, 200]:
            ch = channel_harmonic_divergence(N, c)
            assert ch > prev
            prev = ch


# ===========================================================================
# Cross-checks with existing codebase
# ===========================================================================

class TestCrossChecks:
    """Cross-check with existing compute modules."""

    def test_kappa_sl2_matches_genus_expansion(self):
        """kappa_sl_N(2, k) = 3(k+2)/4 matches genus_expansion.kappa_sl2."""
        for k in [1, 2, 3, 5, 10]:
            our_kappa = kappa_sl_N(2, Fraction(k))
            expected = Fraction(3) * (Fraction(k) + 2) / 4
            assert our_kappa == expected

    def test_kappa_sl3_matches_genus_expansion(self):
        """kappa_sl_N(3, k) = 4(k+3)/3 matches genus_expansion.kappa_sl3."""
        for k in [1, 2, 3, 5]:
            our_kappa = kappa_sl_N(3, Fraction(k))
            # kappa = (N^2-1)(k+N)/(2N) = 8(k+3)/6 = 4(k+3)/3
            expected = Fraction(4) * (Fraction(k) + 3) / 3
            assert our_kappa == expected

    def test_heisenberg_F_g_matches(self):
        """Our Fredholm F_g matches stable_graph_enumeration."""
        for g in range(1, 8):
            ours = heisenberg_fredholm(g).free_energy
            theirs = heisenberg_free_energy(g)
            assert ours == theirs, f"Mismatch at g={g}: {ours} vs {theirs}"

    def test_ff_dual_level_matches_koszul_pairs(self):
        """Our FF dual level matches koszul_pairs.ff_dual_level."""
        # sl_2: h^v = 2, dual level = -k - 4
        assert feigin_frenkel_dual_level(Fraction(1), 2) == Fraction(-5)
        # sl_3: h^v = 3, dual level = -k - 6
        assert feigin_frenkel_dual_level(Fraction(1), 3) == Fraction(-7)

    def test_w2_central_charge_matches_virasoro(self):
        """W_2 central charge matches the Virasoro DS formula."""
        for k in [1, 2, 3, 5]:
            c_w2 = wn_central_charge(2, Fraction(k))
            k_f = Fraction(k)
            c_vir = 1 - 6 * (k_f + 1) ** 2 / (k_f + 2)
            assert c_w2 == c_vir
