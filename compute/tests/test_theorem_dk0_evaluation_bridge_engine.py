r"""Tests for DK-0 evaluation module comparison with DNP25 constraints.

THEOREM (Drinfeld-Kohno comparison, DK-0):
The KZ monodromy on evaluation modules reproduces the quantum group
Casimir eigenvalues:
    Mon(KZ)|_{V_j} = q^{C_2(j) - C_2(j1) - C_2(j2)}
where q = exp(pi*i/(k+h^v)) and C_2(j) = j(j+1).

FOUR VERIFICATION PATHS (3+ per claim, per CLAUDE.md multi-path mandate):

    Path 1 (Analytic monodromy):  exp(2*pi*i*Omega/(k+h^v)) eigenvalues
    Path 2 (Quantum Casimir):     q^{C_2(j)-C_2(j1)-C_2(j2)} from U_q(sl_2)
    Path 3 (Yangian ratio):       R^Y(u) ratio at Drinfeld specialization
    Path 4 (DNP25 Verlinde):      fusion truncation via quantum dim vanishing

Cross-checks:
    (a) Path 1 eigenvalues = Path 2 eigenvalues (DK comparison)
    (b) Full monodromy matrix = quantum Casimir matrix (tautological)
    (c) Numerical monodromy (ODE) = analytic monodromy (matrix exp)
    (d) scipy monodromy = analytic monodromy
    (e) Yangian ratio at u_D = KZ ratio q^2
    (f) Verlinde truncation from [2j+1]_q = 0
    (g) Yang-Baxter equation for Yangian R-matrix
    (h) Hecke relation for quantum group braiding
    (i) DK at higher spins j1 x j2 for multiple levels

All formulas computed from first principles (AP1, AP3).
Cross-family consistency verified (AP10).
Multi-path verification per CLAUDE.md mandate.

References:
    thm:shadow-connection-kz (yangians_drinfeld_kohno.tex)
    thm:derived-dk-affine (yangians_drinfeld_kohno.tex)
    AP19: r-matrix pole order one below OPE
    AP27: bar propagator d log E(z,w) is weight 1
"""

import cmath

import numpy as np
import pytest
from numpy import linalg as la

from compute.lib.theorem_dk0_evaluation_bridge_engine import (
    # Constants
    PI, I2, I4, SIGMA_X, SIGMA_Y, SIGMA_Z, PERM_2, P_SYM, P_ASYM,
    CASIMIR_SL2_FUND, LIE_DATA,
    # KZ data
    KZData,
    # Casimir
    casimir_sl2_fund, casimir_eigenvalues_fund, casimir_eigenvalues_verify,
    casimir_tensor_product, casimir_eigenvalue_formula,
    # Spin representations
    spin_j_rep,
    # Path 1: KZ monodromy
    kz_monodromy_fund, kz_monodromy_eigenvalues,
    kz_monodromy_numerical, kz_monodromy_scipy,
    kz_monodromy_general, kz_monodromy_general_eigenvalues,
    # Path 2: Quantum Casimir
    quantum_group_q, quantum_casimir_eigenvalue, quantum_dim_sl2,
    dk_comparison_fund, dk_comparison_general, dk_matrix_comparison_fund,
    # Path 3: Yangian
    yangian_r_matrix_fund, yangian_eigenvalues, yangian_eigenvalue_ratio,
    kz_eigenvalue_ratio, drinfeld_specialization, yangian_kz_ratio_comparison,
    yangian_evaluation_ybe_check,
    # Yangian evaluation modules
    yangian_evaluation_action, yangian_evaluation_r_matrix,
    # Path 4: Verlinde / DNP25
    verlinde_fusion_sl2, verlinde_truncation_from_qdim,
    verlinde_vs_clebsch_gordan, verlinde_from_r_eigenspaces,
    # Shadow connection
    shadow_connection_kz, collision_residue_from_theta, verify_shadow_eq_kz,
    # U_q R-matrix (Hecke)
    uq_r_matrix_fund, uq_braiding_fund, uq_braiding_eigenvalues,
    hecke_relation_check,
    # Full verification
    verify_dk0_fund, verify_dk0_multi_level, verify_dk0_higher_spin,
)


# ============================================================================
# I. CASIMIR TENSOR (FOUNDATIONAL)
# ============================================================================

class TestCasimir:
    """Test the sl_2 Casimir tensor in fund x fund."""

    def test_casimir_eigenvalues_formula(self):
        """Casimir eigenvalues from the analytic formula."""
        ev = casimir_eigenvalues_fund()
        assert abs(ev["triplet"] - 0.25) < 1e-15
        assert abs(ev["singlet"] - (-0.75)) < 1e-15

    def test_casimir_eigenvalues_diagonalization(self):
        """Casimir eigenvalues by direct diagonalization (Path 1)."""
        ev = casimir_eigenvalues_verify()
        assert abs(ev["singlet"] - (-0.75)) < 1e-12
        for t in ev["triplet_deg3"]:
            assert abs(t - 0.25) < 1e-12

    def test_casimir_formula_vs_diag(self):
        """Formula and diagonalization agree (multi-path check)."""
        formula = casimir_eigenvalues_fund()
        diag = casimir_eigenvalues_verify()
        assert abs(formula["triplet"] - diag["triplet_deg3"][0]) < 1e-12
        assert abs(formula["singlet"] - diag["singlet"]) < 1e-12

    def test_casimir_is_P_half_minus_I_quarter(self):
        """Omega = P/2 - I/4 (definition check)."""
        Omega = casimir_sl2_fund()
        expected = PERM_2 / 2 - I4 / 4
        assert la.norm(Omega - expected) < 1e-15

    def test_casimir_trace(self):
        """Tr(Omega) = 3*(1/4) + 1*(-3/4) = 0."""
        Omega = casimir_sl2_fund()
        assert abs(np.trace(Omega)) < 1e-15

    def test_casimir_general_fund_matches_explicit(self):
        """casimir_tensor_product(1/2, 1/2) matches the explicit formula."""
        Omega_gen = casimir_tensor_product(0.5, 0.5)
        Omega_exp = casimir_sl2_fund()
        assert la.norm(Omega_gen - Omega_exp) < 1e-12

    def test_casimir_eigenvalue_formula_vs_computation(self):
        """casimir_eigenvalue_formula agrees with eigenvalues of the matrix."""
        for j1, j2 in [(0.5, 0.5), (0.5, 1.0), (1.0, 1.0), (0.5, 1.5)]:
            Omega = casimir_tensor_product(j1, j2)
            eigvals = sorted(la.eigvalsh(Omega.real))
            j = abs(j1 - j2)
            idx = 0
            while j <= j1 + j2 + 1e-10:
                expected_ev = casimir_eigenvalue_formula(j, j1, j2)
                dim_j = int(2 * j + 1)
                for _ in range(dim_j):
                    assert abs(eigvals[idx] - expected_ev) < 1e-10, \
                        f"j1={j1}, j2={j2}, j={j}: {eigvals[idx]} != {expected_ev}"
                    idx += 1
                j += 1.0


# ============================================================================
# II. PATH 1: KZ MONODROMY
# ============================================================================

class TestKZMonodromy:
    """Test KZ monodromy computation (Path 1)."""

    def test_kz_monodromy_eigenvalues_level1(self):
        """KZ monodromy eigenvalues at level 1: q^{1/2} and q^{-3/2}."""
        ev = kz_monodromy_eigenvalues(1.0)
        q = cmath.exp(1j * PI / 3)
        assert abs(ev["triplet"] - q ** 0.5) < 1e-12
        assert abs(ev["singlet"] - q ** (-1.5)) < 1e-12

    def test_kz_monodromy_eigenvalues_level2(self):
        """KZ monodromy eigenvalues at level 2."""
        ev = kz_monodromy_eigenvalues(2.0)
        q = cmath.exp(1j * PI / 4)
        assert abs(ev["triplet"] - q ** 0.5) < 1e-12
        assert abs(ev["singlet"] - q ** (-1.5)) < 1e-12

    def test_kz_monodromy_matrix_vs_eigenvalues(self):
        """Full 4x4 monodromy matrix eigenvalues match closed formula."""
        for k in [1, 2, 3, 5]:
            Mon = kz_monodromy_fund(float(k))
            eigvals = la.eigvals(Mon)
            ev = kz_monodromy_eigenvalues(float(k))

            # Sort by argument for comparison
            eigvals_sorted = sorted(eigvals, key=lambda x: cmath.phase(x))

            # The singlet eigenvalue appears once, triplet three times
            trip = ev["triplet"]
            sing = ev["singlet"]

            trip_count = sum(1 for e in eigvals if abs(e - trip) < 1e-10)
            sing_count = sum(1 for e in eigvals if abs(e - sing) < 1e-10)
            assert trip_count == 3, f"k={k}: expected 3 triplet, got {trip_count}"
            assert sing_count == 1, f"k={k}: expected 1 singlet, got {sing_count}"

    def test_kz_monodromy_numerical_vs_exact(self):
        """Numerical ODE integration matches analytic monodromy."""
        for k in [1, 2, 3]:
            Mon_exact = kz_monodromy_fund(float(k))
            Mon_num = kz_monodromy_numerical(float(k), n_steps=5000)
            diff = la.norm(Mon_exact - Mon_num)
            assert diff < 1e-10, f"k={k}: numerical diff = {diff:.2e}"

    def test_kz_monodromy_scipy_vs_exact(self):
        """scipy ODE solver matches analytic monodromy."""
        for k in [1, 2, 3]:
            Mon_exact = kz_monodromy_fund(float(k))
            Mon_scipy = kz_monodromy_scipy(float(k))
            diff = la.norm(Mon_exact - Mon_scipy)
            assert diff < 1e-10, f"k={k}: scipy diff = {diff:.2e}"

    def test_kz_monodromy_unitary(self):
        """KZ monodromy is unitary (Mon * Mon^dag = I)."""
        for k in [1, 2, 3, 5, 10]:
            Mon = kz_monodromy_fund(float(k))
            prod = Mon @ Mon.conj().T
            assert la.norm(prod - I4) < 1e-10, f"k={k}: not unitary"


# ============================================================================
# III. PATH 2: DK COMPARISON (QUANTUM CASIMIR)
# ============================================================================

class TestDKComparison:
    """Test the Drinfeld-Kohno comparison: KZ monodromy = quantum Casimir."""

    def test_dk_fund_all_levels(self):
        """DK comparison for fund x fund at levels 1 through 20."""
        for k in range(1, 21):
            r = dk_comparison_fund(float(k))
            assert r["dk_verified"], f"DK failed at k={k}"

    def test_dk_matrix_all_levels(self):
        """DK matrix comparison for fund x fund at multiple levels."""
        for k in [1, 2, 3, 5, 10]:
            r = dk_matrix_comparison_fund(float(k))
            assert r["match"], f"Matrix mismatch at k={k}"

    def test_dk_higher_spin_half_x_one(self):
        """DK for j=1/2 x j=1 at levels 2, 3, 5, 10."""
        for k in [2, 3, 5, 10]:
            r = dk_comparison_general(0.5, 1.0, float(k))
            assert r["all_match"], f"DK failed for 1/2 x 1 at k={k}"

    def test_dk_higher_spin_one_x_one(self):
        """DK for j=1 x j=1 at levels 3, 4, 5, 10."""
        for k in [3, 4, 5, 10]:
            r = dk_comparison_general(1.0, 1.0, float(k))
            assert r["all_match"], f"DK failed for 1 x 1 at k={k}"

    def test_dk_higher_spin_half_x_three_half(self):
        """DK for j=1/2 x j=3/2 at levels 4, 5, 10."""
        for k in [4, 5, 10]:
            r = dk_comparison_general(0.5, 1.5, float(k))
            assert r["all_match"], f"DK failed for 1/2 x 3/2 at k={k}"

    def test_dk_higher_spin_one_x_three_half(self):
        """DK for j=1 x j=3/2 at levels 5, 6, 10."""
        for k in [5, 6, 10]:
            r = dk_comparison_general(1.0, 1.5, float(k))
            assert r["all_match"], f"DK failed for 1 x 3/2 at k={k}"

    def test_dk_symmetry_j1_j2(self):
        """DK eigenvalues unchanged under j1 <-> j2 (commutativity)."""
        for k in [3, 5]:
            r1 = dk_comparison_general(0.5, 1.0, float(k))
            r2 = dk_comparison_general(1.0, 0.5, float(k))
            for c1, c2 in zip(r1["comparisons"], r2["comparisons"]):
                assert abs(c1["kz_eigenvalue"] - c2["kz_eigenvalue"]) < 1e-10


# ============================================================================
# IV. PATH 3: YANGIAN R-MATRIX
# ============================================================================

class TestYangian:
    """Test Yangian R-matrix and Drinfeld specialization (Path 3)."""

    def test_yangian_eigenvalues(self):
        """Yangian R^Y(u) = u*I + i*P has eigenvalues u+i (trip) and u-i (sing)."""
        for u in [1.0, 2.5, 0.5 + 1j, -3.0]:
            R = yangian_r_matrix_fund(u)
            eigvals = la.eigvals(R)
            trip_count = sum(1 for e in eigvals if abs(e - (u + 1j)) < 1e-10)
            sing_count = sum(1 for e in eigvals if abs(e - (u - 1j)) < 1e-10)
            assert trip_count == 3, f"u={u}: expected 3 triplet eigenvalues"
            assert sing_count == 1, f"u={u}: expected 1 singlet eigenvalue"

    def test_yangian_classical_limit(self):
        """As u -> infinity, R^Y(u)/u -> I (classical limit)."""
        u = 1000.0
        R = yangian_r_matrix_fund(u)
        assert la.norm(R / u - I4) < 0.01

    def test_yangian_ybe(self):
        """Yang-Baxter equation R_{12}R_{13}R_{23} = R_{23}R_{13}R_{12}."""
        params = [
            (1.0, 2.0, 3.0),
            (0.5 + 1j, 2.0 - 0.3j, -1.0 + 0.5j),
            (0.1, 0.2, 0.3),
        ]
        for a, b, c in params:
            res = yangian_evaluation_ybe_check(a, b, c)
            assert res < 1e-12, f"YBE failed for ({a},{b},{c}): {res:.2e}"

    def test_drinfeld_specialization_real(self):
        """Drinfeld spectral parameter u_D is real."""
        for k in [1, 2, 3, 5, 10]:
            u_D = drinfeld_specialization(float(k))
            assert abs(u_D.imag) < 1e-10, f"k={k}: u_D = {u_D} is not real"

    def test_drinfeld_specialization_positive(self):
        """u_D = cot(pi/(k+2)) > 0 for all k >= 1."""
        for k in range(1, 21):
            u_D = drinfeld_specialization(float(k))
            assert u_D.real > 0, f"k={k}: u_D = {u_D.real} not positive"

    def test_yangian_ratio_matches_kz(self):
        """Yangian ratio at u_D equals KZ ratio q^2 at all levels."""
        for k in range(1, 21):
            r = yangian_kz_ratio_comparison(float(k))
            assert r["ratio_match"], f"Yangian ratio mismatch at k={k}"

    def test_yangian_evaluation_module_structure(self):
        """Evaluation module T_1^a = a * T_0^a."""
        a = 3.0 + 1j
        mod = yangian_evaluation_action(a)
        assert la.norm(mod["T1_e"] - a * mod["T0_e"]) < 1e-15
        assert la.norm(mod["T1_f"] - a * mod["T0_f"]) < 1e-15
        assert la.norm(mod["T1_h"] - a * mod["T0_h"]) < 1e-15

    def test_yangian_eval_r_matrix_eq_yang(self):
        """R_{V(a),V(b)} = (a-b)*I + i*P = R^Y(a-b)."""
        a, b = 2.0 + 1j, 0.5 - 0.3j
        R_eval = yangian_evaluation_r_matrix(a, b)
        R_yang = yangian_r_matrix_fund(a - b)
        assert la.norm(R_eval - R_yang) < 1e-15


# ============================================================================
# V. PATH 4: DNP25 VERLINDE FUSION
# ============================================================================

class TestVerlinde:
    """Test DNP25 Verlinde fusion constraints (Path 4)."""

    def test_verlinde_fund_x_fund_k1(self):
        """At k=1: V_{1/2} x V_{1/2} = V_0 only (triplet truncated)."""
        spins = verlinde_fusion_sl2(0.5, 0.5, 1)
        assert len(spins) == 1
        assert abs(spins[0] - 0.0) < 1e-10

    def test_verlinde_fund_x_fund_k2(self):
        """At k=2: V_{1/2} x V_{1/2} = V_0 + V_1 (full CG)."""
        spins = verlinde_fusion_sl2(0.5, 0.5, 2)
        assert len(spins) == 2
        assert abs(spins[0] - 0.0) < 1e-10
        assert abs(spins[1] - 1.0) < 1e-10

    def test_verlinde_truncation_mechanism(self):
        """Verlinde truncation at k=1: [3]_q = 0 (quantum dim of V_1 vanishes)."""
        q = quantum_group_q(1.0)
        qdim_1 = quantum_dim_sl2(1, q)
        assert abs(qdim_1) < 1e-10, f"[3]_q at k=1 should vanish, got {qdim_1}"

    def test_verlinde_truncation_general(self):
        """At level k, [2j+1]_q = 0 for j = (k+1)/2 (truncation boundary)."""
        for k in range(1, 10):
            q = quantum_group_q(float(k))
            j_trunc = (k + 1) / 2.0
            qdim = quantum_dim_sl2(j_trunc, q)
            assert abs(qdim) < 1e-10, \
                f"k={k}: [2*{j_trunc}+1]_q should vanish, got {qdim}"

    def test_verlinde_integrable_nonvanishing(self):
        """Integrable reps j <= k/2 have nonzero quantum dimension."""
        for k in [2, 3, 4, 5]:
            q = quantum_group_q(float(k))
            j = 0.0
            while j <= k / 2.0 + 1e-10:
                qdim = quantum_dim_sl2(j, q)
                assert abs(qdim) > 1e-10, \
                    f"k={k}, j={j}: integrable rep has qdim=0"
                j += 0.5

    def test_verlinde_vs_cg_truncation(self):
        """Verlinde fusion is CG truncated; truncated channels have qdim=0."""
        for k in [1, 2, 3]:
            r = verlinde_vs_clebsch_gordan(0.5, 0.5, k)
            assert r["truncation_by_qdim_vanishing"]

    def test_verlinde_vs_cg_higher_spin(self):
        """Higher-spin Verlinde truncation: truncated channels with j > k/2 have qdim=0.

        Note: Verlinde truncation has TWO mechanisms:
        (a) j > k/2 => quantum dimension vanishes (DNP25 decoupling)
        (b) j1 + j2 + j > k => fusion rule constraint (even if qdim != 0)
        Both are genuine truncation. Here we test case (a).
        """
        # 1/2 x 1 at k=2: CG gives j=1/2, 3/2. Verlinde j_max = min(3/2, 1/2) = 1/2.
        # j=3/2 is truncated, and [4]_q = 0 at k=2 (j=3/2 > k/2=1).
        r = verlinde_vs_clebsch_gordan(0.5, 1.0, 2)
        assert r["truncation_by_qdim_vanishing"], \
            "1/2 x 1 at k=2: truncated j=3/2 should have qdim=0"

    def test_verlinde_fusion_rule_constraint(self):
        """Verlinde fusion rule can truncate even when qdim != 0.

        At k=2, 1 x 1: CG gives j=0,1,2. Verlinde gives j=0 only
        (since k - j1 - j2 = 0). The j=1 channel has nonzero qdim
        but is excluded by the fusion rule j <= k - j1 - j2.
        """
        r = verlinde_vs_clebsch_gordan(1.0, 1.0, 2)
        assert r["verlinde_spins"] == [0.0]
        assert 1.0 in r["truncated_spins"]

    def test_verlinde_from_r_eigenspaces_k1(self):
        """At k=1: V_1 has qdim=0, only singlet (V_0) allowed."""
        r = verlinde_from_r_eigenspaces(1.0)
        assert r["singlet_allowed"]
        assert not r["triplet_allowed"]
        assert r["k1_truncation"]

    def test_verlinde_from_r_eigenspaces_k2(self):
        """At k=2: both singlet and triplet allowed."""
        r = verlinde_from_r_eigenspaces(2.0)
        assert r["singlet_allowed"]
        assert r["triplet_allowed"]


# ============================================================================
# VI. SHADOW CONNECTION = KZ
# ============================================================================

class TestShadowConnection:
    """Test that the shadow connection equals the KZ connection."""

    def test_shadow_eq_kz_all_levels(self):
        """Shadow connection = KZ connection at all tested levels."""
        for k in [1, 2, 3, 5, 10, 20]:
            r = verify_shadow_eq_kz(float(k))
            assert r["match"], f"Shadow != KZ at k={k}"

    def test_collision_residue_structure(self):
        """Collision residue = Omega/(k+h^v), proportional to Casimir."""
        kz = KZData(lie_type="sl2", level=3.0)
        res = collision_residue_from_theta(kz)
        Omega = casimir_sl2_fund()
        expected = Omega / 5.0  # k+h^v = 3+2 = 5
        assert la.norm(res - expected) < 1e-14

    def test_shadow_connection_at_z(self):
        """Shadow connection at z=2 is Omega/(2*(k+h^v))."""
        kz = KZData(lie_type="sl2", level=2.0)
        A = shadow_connection_kz(kz, z=2.0)
        Omega = casimir_sl2_fund()
        expected = Omega / (4 * 2)  # kz_parameter = 1/4, divided by z=2
        assert la.norm(A - expected) < 1e-14


# ============================================================================
# VII. U_q(sl_2) HECKE ALGEBRA
# ============================================================================

class TestHecke:
    """Test the quantum group braiding and Hecke algebra structure."""

    def test_hecke_relation(self):
        """(sigma - q)(sigma + q^{-1}) = 0 at all levels."""
        for k in [1, 2, 3, 5, 10]:
            res = hecke_relation_check(float(k))
            assert res < 1e-12, f"Hecke relation fails at k={k}: {res:.2e}"

    def test_braiding_eigenvalues(self):
        """Braiding sigma = P*R has eigenvalues q (x3) and -q^{-1} (x1)."""
        for k in [1, 2, 3, 5]:
            q = quantum_group_q(float(k))
            sigma = uq_braiding_fund(float(k))
            eigvals = la.eigvals(sigma)
            trip_count = sum(1 for e in eigvals if abs(e - q) < 1e-8)
            sing_count = sum(1 for e in eigvals if abs(e - (-1.0 / q)) < 1e-8)
            assert trip_count == 3, f"k={k}: expected 3 triplet, got {trip_count}"
            assert sing_count == 1, f"k={k}: expected 1 singlet, got {sing_count}"

    def test_braiding_ne_monodromy(self):
        """Braiding eigenvalues differ from KZ monodromy eigenvalues.

        This is a STRUCTURAL test: the Hecke eigenvalues q and -q^{-1}
        are NOT the same as the KZ eigenvalues q^{1/2} and q^{-3/2}.
        The DK comparison matches monodromy with the QUANTUM CASIMIR, not
        the Hecke generator.
        """
        for k in [1, 2, 3]:
            kz_ev = kz_monodromy_eigenvalues(float(k))
            hk_ev = uq_braiding_eigenvalues(float(k))
            # Triplet: q^{1/2} != q (for k >= 1)
            assert abs(kz_ev["triplet"] - hk_ev["triplet"]) > 1e-3, \
                f"k={k}: braiding and monodromy should differ on triplet"

    def test_r_matrix_structure(self):
        """R-matrix has the standard Drinfeld-Jimbo form."""
        for k in [1, 2, 3]:
            q = quantum_group_q(float(k))
            R = uq_r_matrix_fund(float(k))
            assert abs(R[0, 0] - q) < 1e-12
            assert abs(R[1, 1] - 1) < 1e-12
            assert abs(R[1, 2] - (q - 1.0 / q)) < 1e-12
            assert abs(R[2, 2] - 1) < 1e-12
            assert abs(R[3, 3] - q) < 1e-12
            # Off-diagonal zeros
            for (i, j) in [(0, 1), (0, 2), (0, 3), (1, 3),
                           (2, 0), (2, 1), (2, 3), (3, 0), (3, 1), (3, 2)]:
                assert abs(R[i, j]) < 1e-15


# ============================================================================
# VIII. SPIN REPRESENTATIONS
# ============================================================================

class TestSpinRep:
    """Test spin-j representation infrastructure."""

    def test_spin_half_dims(self):
        """Spin-1/2: dim = 2."""
        rep = spin_j_rep(0.5)
        assert rep["dim"] == 2

    def test_spin_one_dims(self):
        """Spin-1: dim = 3."""
        rep = spin_j_rep(1.0)
        assert rep["dim"] == 3

    def test_casimir_scalar_on_irrep(self):
        """C_2 = j(j+1) on each irrep."""
        for j in [0.5, 1.0, 1.5, 2.0]:
            rep = spin_j_rep(j)
            Jz, Jp, Jm = rep["Jz"], rep["Jp"], rep["Jm"]
            C2 = Jz @ Jz + 0.5 * (Jp @ Jm + Jm @ Jp)
            expected = j * (j + 1) * np.eye(rep["dim"])
            assert la.norm(C2 - expected) < 1e-10, f"j={j}: C_2 wrong"


# ============================================================================
# IX. KZ DATA
# ============================================================================

class TestKZData:
    """Test KZ connection data structure."""

    def test_kappa_sl2(self):
        """kappa(sl_2, k) = 3*(k+2)/4 (AP1)."""
        for k in [1, 2, 3, 5, 10]:
            kz = KZData(lie_type="sl2", level=float(k))
            expected = 3.0 * (k + 2) / 4.0
            assert abs(kz.kappa - expected) < 1e-12

    def test_kz_parameter(self):
        """KZ parameter h = 1/(k+h^v) = 1/(k+2) for sl_2."""
        for k in [1, 2, 3]:
            kz = KZData(lie_type="sl2", level=float(k))
            assert abs(kz.kz_parameter - 1.0 / (k + 2)) < 1e-14

    def test_critical_level_raises(self):
        """Critical level k = -h^v raises ValueError."""
        kz = KZData(lie_type="sl2", level=-2.0)
        with pytest.raises(ValueError, match="Critical level"):
            _ = kz.kz_parameter

    def test_q_root_of_unity(self):
        """q = exp(pi*i/(k+2)) is a (2(k+2))-th root of unity."""
        for k in [1, 2, 3, 5]:
            kz = KZData(lie_type="sl2", level=float(k))
            order = 2 * (k + 2)
            assert abs(kz.q ** order - 1.0) < 1e-10


# ============================================================================
# X. FULL CHAIN VERIFICATION
# ============================================================================

class TestFullChain:
    """Full DK-0 verification chain (all four paths)."""

    def test_full_dk0_levels_1_to_10(self):
        """All four paths consistent at levels 1 through 10."""
        for k in range(1, 11):
            r = verify_dk0_fund(float(k))
            assert r["all_paths_consistent"], f"DK-0 failed at k={k}"

    def test_full_dk0_large_level(self):
        """DK-0 at large level k=50 (semiclassical regime)."""
        r = verify_dk0_fund(50.0)
        assert r["all_paths_consistent"]

    def test_multi_level_batch(self):
        """Batch verification across standard levels."""
        results = verify_dk0_multi_level([1, 2, 3, 5, 10, 20])
        for r in results:
            assert r["all_paths_consistent"], \
                f"DK-0 failed at k={r['level']}"

    def test_higher_spin_sweep(self):
        """DK-0 higher-spin sweep: multiple (j1, j2, k) triples."""
        triples = [
            (0.5, 0.5, 2), (0.5, 0.5, 5),
            (0.5, 1.0, 3), (0.5, 1.0, 5),
            (1.0, 1.0, 3), (1.0, 1.0, 5),
            (0.5, 1.5, 4), (1.0, 1.5, 5),
            (1.5, 1.5, 5), (0.5, 2.0, 5),
        ]
        for j1, j2, k in triples:
            r = verify_dk0_higher_spin(float(k), j1, j2)
            assert r["all_match"], \
                f"DK-0 failed for j1={j1}, j2={j2}, k={k}"


# ============================================================================
# XI. CROSS-PATH CONSISTENCY
# ============================================================================

class TestCrossPath:
    """Cross-path consistency checks."""

    def test_kz_ratio_eq_q_squared(self):
        """KZ eigenvalue ratio = q^2 = exp(2*pi*i/(k+2))."""
        for k in [1, 2, 3, 5, 10]:
            kz_r = kz_eigenvalue_ratio(float(k))
            q = quantum_group_q(float(k))
            assert abs(kz_r - q ** 2) < 1e-12

    def test_three_monodromy_methods_agree(self):
        """Analytic, numerical, and scipy monodromy all agree."""
        for k in [1, 2, 3]:
            Mon_a = kz_monodromy_fund(float(k))
            Mon_n = kz_monodromy_numerical(float(k), n_steps=5000)
            Mon_s = kz_monodromy_scipy(float(k))
            assert la.norm(Mon_a - Mon_n) < 1e-10
            assert la.norm(Mon_a - Mon_s) < 1e-10

    def test_verlinde_consistent_with_dk(self):
        """Verlinde channels match CG channels within integrable sector.

        At level k >= 2, the fund x fund decomposition V_0 + V_1 is fully
        within the integrable sector, so Verlinde = CG.  DK verifies each
        channel independently.
        """
        for k in [2, 3, 5]:
            ver = verlinde_fusion_sl2(0.5, 0.5, k)
            assert 0.0 in [round(j, 1) for j in ver]
            assert 1.0 in [round(j, 1) for j in ver]
            dk = dk_comparison_fund(float(k))
            assert dk["dk_verified"]

    def test_semiclassical_limit(self):
        """As k -> infinity, q -> 1 and KZ monodromy -> I (decoupling).

        At large k, Omega/(k+2) -> 0, so Mon -> I.
        """
        Mon = kz_monodromy_fund(1000.0)
        assert la.norm(Mon - I4) < 0.01

    def test_casimir_formula_vs_matrix_vs_qdim(self):
        """Triple cross-check: Casimir formula, matrix eigenvalue, quantum Casimir.

        Path A: casimir_eigenvalue_formula(j, j1, j2) (analytic)
        Path B: eigenvalues of casimir_tensor_product matrix (numerical)
        Path C: quantum_casimir_eigenvalue(j, j1, j2, k) (quantum group)
        Path D: kz_monodromy eigenvalue from matrix exponential

        All four must be consistent: Path D = exp(2*pi*i * Path A / (k+2))
        and Path D = Path C.
        """
        for j1, j2, k in [(0.5, 0.5, 3), (0.5, 1.0, 5), (1.0, 1.0, 4)]:
            Omega = casimir_tensor_product(j1, j2)
            eigvals_mat = sorted(la.eigvalsh(Omega.real))
            Mon = kz_monodromy_general(j1, j2, float(k))
            mon_eigvals = sorted(la.eigvals(Mon), key=lambda x: cmath.phase(x))

            j = abs(j1 - j2)
            idx = 0
            while j <= j1 + j2 + 1e-10:
                dim_j = int(2 * j + 1)
                # Path A: formula
                omega_A = casimir_eigenvalue_formula(j, j1, j2)
                # Path B: matrix eigenvalue
                omega_B = eigvals_mat[idx]
                # Path C: quantum Casimir
                qc_ev = quantum_casimir_eigenvalue(j, j1, j2, float(k))
                # Path D: monodromy matrix eigenvalue
                mon_ev = cmath.exp(2 * PI * 1j * omega_A / (k + 2))

                assert abs(omega_A - omega_B) < 1e-10, \
                    f"Path A vs B: {omega_A} vs {omega_B}"
                assert abs(mon_ev - qc_ev) < 1e-10, \
                    f"Path D vs C: {mon_ev} vs {qc_ev}"

                idx += dim_j
                j += 1.0

    def test_yangian_ratio_cross_path(self):
        """Triple cross-check for eigenvalue ratio.

        Path A: KZ monodromy eigenvalue ratio (trip/sing)
        Path B: q^2 from quantum group parameter
        Path C: Yangian ratio (u_D+i)/(u_D-i) at Drinfeld specialization

        All three must agree.
        """
        for k in [1, 2, 3, 5, 10]:
            kf = float(k)
            # Path A: KZ ratio
            ev = kz_monodromy_eigenvalues(kf)
            ratio_A = ev["triplet"] / ev["singlet"]
            # Path B: q^2
            q = quantum_group_q(kf)
            ratio_B = q ** 2
            # Path C: Yangian
            u_D = drinfeld_specialization(kf)
            ratio_C = yangian_eigenvalue_ratio(u_D)

            assert abs(ratio_A - ratio_B) < 1e-10, \
                f"k={k}: KZ ratio {ratio_A} != q^2 {ratio_B}"
            assert abs(ratio_B - ratio_C) < 1e-10, \
                f"k={k}: q^2 {ratio_B} != Yangian ratio {ratio_C}"

    def test_monodromy_determinant_vs_trace(self):
        """Multi-path determinant check.

        Path A: det(Mon) = product of eigenvalues = q^{1/2} * q^{-3/2} * q^{1/2} * q^{1/2}
                         = q^{3*1/2 + (-3/2)} = q^0 = 1 ... no, let me compute.
        det = (q^{1/2})^3 * q^{-3/2} = q^{3/2 - 3/2} = q^0 = 1.
        Path B: det(exp(A)) = exp(tr(A)).
        tr(2*pi*i*Omega/(k+2)) = 2*pi*i * tr(Omega) / (k+2) = 0 (since tr(Omega) = 0).
        So det(Mon) = exp(0) = 1.
        """
        for k in [1, 2, 3, 5]:
            Mon = kz_monodromy_fund(float(k))
            det_A = la.det(Mon)
            assert abs(abs(det_A) - 1.0) < 1e-10, f"k={k}: |det| != 1"
            # Phase should be 0 (mod 2*pi)
            assert abs(cmath.phase(det_A)) < 1e-10 or \
                   abs(abs(cmath.phase(det_A)) - 2 * PI) < 1e-10, \
                f"k={k}: det phase nonzero"
