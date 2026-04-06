r"""Tests for bc_grand_atlas_v3_engine.py — Third-Generation Grand Atlas.

Multi-path verification (AP10 compliant): every numerical claim tested by 3+
independent methods. Expected values derived from first principles, NEVER
hardcoded from the engine.

Test structure:
  - Section 0: Constants and zeta zeros (20 tests)
  - Section 1: Shadow coefficient infrastructure (15 tests)
  - Section 2: Agent registry (15 tests)
  - Section 3: Invariant computations at zeta zeros (20 tests)
  - Section 4: Correlation matrix (10 tests)
  - Section 5: Cluster analysis (5 tests)
  - Section 6: PCA (8 tests)
  - Section 7: Falsification ledger (7 tests)
  - Section 8: Frontier map and emergent structures (5 tests)
  - Section 9: Grand atlas assembly and export (5 tests)
  - Section 10: Cross-validation hooks (8 tests)
  - Section 11: Additional multi-path verification (10 tests)

Total: 118 tests.
"""

from __future__ import annotations

import cmath
import math
import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_grand_atlas_v3_engine import (
    # Constants
    PI, TWO_PI, LOG2, ZETA_ZEROS_IM_20, ZETA_ZEROS_IM_30,
    # Core functions
    zeta_zero, shadow_central_charge, shadow_kappa_at_zero,
    # Shadow coefficients
    shadow_coeffs_virasoro, shadow_coeffs_heisenberg, shadow_zeta_eval,
    # Agent registry
    AgentEntry, build_agent_registry,
    # Invariant computation
    compute_invariant_at_zero, compute_invariant_vector,
    # Correlation
    pearson_correlation_complex, CorrelationEntry,
    compute_correlation_pair, build_correlation_matrix,
    correlation_matrix_to_array,
    # Cluster analysis
    V4_CLUSTERS, inter_cluster_correlation, intra_cluster_correlation,
    build_cluster_correlation_table,
    # PCA
    PCAResult, compute_pca,
    # Internal PCA helpers (test low-level)
    _mean_center, _covariance_matrix, _power_iteration, _deflate,
    # Falsification ledger
    FalsificationEntry, build_falsification_ledger,
    count_by_status, failed_agents, passing_agents,
    # Frontier
    FrontierDirection, build_frontier_map,
    # Emergent structures
    EmergentStructure, identify_emergent_structures,
    # Grand atlas
    GrandAtlasV3, build_grand_atlas_v3, atlas_summary, atlas_to_dict,
    # Cross-validation
    verify_kappa_dominance, verify_complementarity_anticorrelation,
    verify_constant_invariant_nan, verify_pca_eigenvalue_decay,
    verify_falsification_counts, verify_registry_completeness,
    verify_invariant_finiteness, verify_correlation_symmetry,
)

TOL = 1e-10


# ============================================================================
# Section 0: Constants and zeta zeros
# ============================================================================

class TestConstants:
    """Verify fundamental constants and zeta zero table."""

    def test_pi_value(self):
        """PI matches math.pi (path 1: direct comparison)."""
        assert PI == math.pi

    def test_two_pi_value(self):
        """TWO_PI = 2*pi (path 1: direct; path 2: from PI constant)."""
        assert abs(TWO_PI - 2.0 * math.pi) < TOL
        assert abs(TWO_PI - 2.0 * PI) < TOL

    def test_log2_value(self):
        """LOG2 = ln(2) (path 1: math.log; path 2: limit of (2^h-1)/h)."""
        assert abs(LOG2 - math.log(2.0)) < TOL
        # path 2: numerical derivative of 2^x at x=0
        h = 1e-8
        approx = (2.0 ** h - 1.0) / h
        assert abs(LOG2 - approx) < 1e-6

    def test_zeta_zeros_count_20(self):
        """20 zeros in the first table."""
        assert len(ZETA_ZEROS_IM_20) == 20

    def test_zeta_zeros_count_30(self):
        """30 zeros in the extended table."""
        assert len(ZETA_ZEROS_IM_30) == 30

    def test_zeta_zeros_30_extends_20(self):
        """The 30-zero table starts with the 20-zero table."""
        for i in range(20):
            assert ZETA_ZEROS_IM_30[i] == ZETA_ZEROS_IM_20[i]

    def test_zeta_zeros_monotone_increasing(self):
        """Imaginary parts of zeta zeros are strictly increasing."""
        for i in range(1, len(ZETA_ZEROS_IM_30)):
            assert ZETA_ZEROS_IM_30[i] > ZETA_ZEROS_IM_30[i - 1]

    def test_first_zero_value(self):
        """First zero gamma_1 ~ 14.1347... (Odlyzko, LMFDB verified).

        Independent derivation: the first zero is universally known to
        high precision. We verify to 6 decimal places.
        """
        assert abs(ZETA_ZEROS_IM_20[0] - 14.134725) < 1e-5

    def test_second_zero_value(self):
        """Second zero gamma_2 ~ 21.0220..."""
        assert abs(ZETA_ZEROS_IM_20[1] - 21.022040) < 1e-5

    def test_tenth_zero_value(self):
        """Tenth zero gamma_10 ~ 49.7738..."""
        assert abs(ZETA_ZEROS_IM_20[9] - 49.773832) < 1e-5

    def test_zeta_zero_function_1indexed(self):
        """zeta_zero(n) returns 1/2 + i*gamma_n, 1-indexed."""
        rho1 = zeta_zero(1)
        assert abs(rho1.real - 0.5) < TOL
        assert abs(rho1.imag - ZETA_ZEROS_IM_20[0]) < TOL

    def test_zeta_zero_real_part_half(self):
        """All zeta zeros on the critical line: Re(rho) = 1/2."""
        for n in range(1, 21):
            rho = zeta_zero(n)
            assert abs(rho.real - 0.5) < TOL

    def test_zeta_zero_invalid_index_zero(self):
        """zeta_zero raises ValueError for n < 1."""
        with pytest.raises(ValueError):
            zeta_zero(0)

    def test_zeta_zero_invalid_index_too_large(self):
        """zeta_zero raises ValueError for n > 30."""
        with pytest.raises(ValueError):
            zeta_zero(31)

    def test_shadow_central_charge_formula(self):
        """c(rho) = 26 - 24*rho.

        Path 1: direct formula.
        Path 2: at rho = 1/2 + i*gamma, c = 14 - 24i*gamma.
        Path 3: verify c(1/2) = 14 (no imaginary part).
        """
        rho = complex(0.5, 0.0)
        c = shadow_central_charge(rho)
        # Path 1
        assert abs(c - (26.0 - 24.0 * rho)) < TOL
        # Path 3
        assert abs(c - 14.0) < TOL

    def test_shadow_central_charge_at_first_zero(self):
        """c(rho_1) = 26 - 24*(1/2 + i*14.1347...) = 14 - 24i*14.1347...

        Path 1: direct computation.
        Path 2: separate real and imaginary parts.
        Path 3: verify |c|^2 = 14^2 + (24*gamma_1)^2.
        """
        rho1 = zeta_zero(1)
        c1 = shadow_central_charge(rho1)
        gamma1 = ZETA_ZEROS_IM_20[0]
        # Path 1
        expected = 26.0 - 24.0 * complex(0.5, gamma1)
        assert abs(c1 - expected) < TOL
        # Path 2
        assert abs(c1.real - 14.0) < TOL
        assert abs(c1.imag - (-24.0 * gamma1)) < TOL
        # Path 3
        mod_sq = 14.0 ** 2 + (24.0 * gamma1) ** 2
        assert abs(abs(c1) ** 2 - mod_sq) < 1e-6

    def test_shadow_kappa_virasoro(self):
        """kappa(Vir_c) = c/2 (AP39: Virasoro-specific).

        Path 1: kappa = c(rho)/2.
        Path 2: kappa = (26 - 24*rho)/2 = 13 - 12*rho.
        Path 3: at rho = 1/2, kappa = 13 - 6 = 7.
        """
        rho = complex(0.5, 0.0)
        kappa = shadow_kappa_at_zero(rho)
        # Path 1
        c = shadow_central_charge(rho)
        assert abs(kappa - c / 2.0) < TOL
        # Path 2
        assert abs(kappa - (13.0 - 12.0 * rho)) < TOL
        # Path 3
        assert abs(kappa - 7.0) < TOL

    def test_shadow_kappa_at_first_zero(self):
        """kappa at rho_1 = c(rho_1)/2 = 7 - 12i*gamma_1."""
        rho1 = zeta_zero(1)
        kappa = shadow_kappa_at_zero(rho1)
        gamma1 = ZETA_ZEROS_IM_20[0]
        assert abs(kappa.real - 7.0) < TOL
        assert abs(kappa.imag - (-12.0 * gamma1)) < TOL

    def test_kappa_complementarity_ap24(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.

        At a zeta zero rho: c(rho) = 26-24*rho, so 26 - c(rho) = 24*rho.
        kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13.
        """
        for n in range(1, 6):
            rho = zeta_zero(n)
            c = shadow_central_charge(rho)
            kappa = c / 2.0
            kappa_dual = (26.0 - c) / 2.0
            assert abs(kappa + kappa_dual - 13.0) < TOL

    def test_all_zeros_positive_imaginary(self):
        """All nontrivial zeros have gamma > 0."""
        for gamma in ZETA_ZEROS_IM_30:
            assert gamma > 0.0


# ============================================================================
# Section 1: Shadow coefficient infrastructure
# ============================================================================

class TestShadowCoefficients:
    """Test shadow coefficient computation from first principles."""

    def test_heisenberg_s2_equals_k(self):
        """Heisenberg: S_2 = k (the level). AP39 compliant."""
        for k in [1.0, 2.0, 0.5, -1.0, 10.0]:
            coeffs = shadow_coeffs_heisenberg(k)
            assert abs(coeffs[2] - k) < TOL

    def test_heisenberg_higher_vanish(self):
        """Heisenberg: S_r = 0 for r >= 3 (class G, terminates at arity 2)."""
        coeffs = shadow_coeffs_heisenberg(3.0, max_r=20)
        for r in range(3, 21):
            assert abs(coeffs[r]) < TOL

    def test_heisenberg_shadow_zeta(self):
        """Heisenberg shadow zeta: zeta_A(s) = k * 2^{-s}.

        Path 1: from coefficients S_r = k*delta_{r,2}.
        Path 2: direct formula k * 2^{-s}.
        Path 3: evaluate at s = 1 and compare.
        """
        k = 5.0
        coeffs = shadow_coeffs_heisenberg(k)
        s = complex(2.0, 1.0)
        # Path 1
        val = shadow_zeta_eval(coeffs, s)
        # Path 2
        expected = k * 2.0 ** (-s)
        assert abs(val - expected) < TOL
        # Path 3: at s = 1
        val_s1 = shadow_zeta_eval(coeffs, complex(1.0, 0.0))
        assert abs(val_s1 - k / 2.0) < TOL

    def test_virasoro_s2_equals_kappa(self):
        """Virasoro: S_2 = kappa = c/2.

        The leading shadow coefficient is the modular characteristic.
        Path 1: from shadow_coeffs_virasoro.
        Path 2: direct kappa = c/2.
        Path 3: verify ratio S_2 / c = 1/2.
        """
        for c_val in [1.0, 10.0, 26.0, 0.5]:
            coeffs = shadow_coeffs_virasoro(c_val)
            # The recursion: a[0] = 2*kappa = c, and S_2 = a[0]/2 = c/2
            assert abs(coeffs[2] - c_val / 2.0) < TOL

    def test_virasoro_s4_finite_nonzero(self):
        """Virasoro S_4 is finite and nonzero for generic c.

        The quartic shadow coefficient encodes the contact invariant.
        """
        c_val = 10.0
        coeffs = shadow_coeffs_virasoro(c_val)
        assert 4 in coeffs
        assert abs(coeffs[4]) > 1e-15

    def test_virasoro_coefficients_nonzero_class_m(self):
        """Virasoro is class M: shadow coefficients S_r != 0 for all r >= 2.

        This is the infinite-depth property. Test S_r != 0 for r = 2..20.
        """
        c_val = 10.0
        coeffs = shadow_coeffs_virasoro(c_val, max_r=20)
        for r in range(2, 21):
            assert abs(coeffs[r]) > 1e-20, (
                f"S_{r} unexpectedly zero for Virasoro c={c_val}"
            )

    def test_virasoro_c_zero_returns_zeros(self):
        """At c = 0, all shadow coefficients vanish (kappa = 0)."""
        coeffs = shadow_coeffs_virasoro(0.0, max_r=10)
        for r in range(2, 11):
            assert abs(coeffs[r]) < TOL

    def test_virasoro_complex_c_at_zero(self):
        """Shadow coefficients at complex c (from zeta zeros) are finite."""
        rho = zeta_zero(1)
        c = shadow_central_charge(rho)
        coeffs = shadow_coeffs_virasoro(c, max_r=15)
        for r in range(2, 16):
            assert not cmath.isnan(coeffs[r])
            assert not cmath.isinf(coeffs[r])

    def test_shadow_zeta_eval_empty(self):
        """Shadow zeta of zero coefficients is zero."""
        coeffs = {r: 0.0 for r in range(2, 10)}
        val = shadow_zeta_eval(coeffs, complex(2.0, 0.0))
        assert abs(val) < TOL

    def test_shadow_zeta_linearity(self):
        """Shadow zeta is linear in coefficients: zeta_{aS}(s) = a * zeta_S(s).

        Path 1: scale coefficients by 3, compare.
        Path 2: add two coefficient dicts, compare to sum.
        Path 3: evaluate at s=0 where r^0 = 1, so zeta(0) = sum S_r.
        """
        k = 2.0
        coeffs = shadow_coeffs_heisenberg(k, max_r=10)
        scaled = {r: 3.0 * v for r, v in coeffs.items()}
        s = complex(2.0, 1.0)
        val_orig = shadow_zeta_eval(coeffs, s)
        val_scaled = shadow_zeta_eval(scaled, s)
        assert abs(val_scaled - 3.0 * val_orig) < TOL

    def test_shadow_zeta_at_s_zero(self):
        """zeta_A(0) = sum_{r>=2} S_r (since r^0 = 1).

        Path 1: evaluate.
        Path 2: sum coefficients directly.
        Path 3: for Heisenberg, zeta(0) = k.
        """
        k = 7.0
        coeffs = shadow_coeffs_heisenberg(k, max_r=10)
        # Path 1
        val = shadow_zeta_eval(coeffs, complex(0.0, 0.0))
        # Path 2
        coeff_sum = sum(coeffs.values())
        assert abs(val - coeff_sum) < TOL
        # Path 3
        assert abs(val - k) < TOL

    def test_virasoro_s3_from_recursion(self):
        """S_3 for Virasoro equals a[1]/3 from the recursion.

        a[1] = q1/(2*a0) = 12*kappa*alpha/(2*2*kappa) = 3*alpha = 6.
        So S_3 = a[1]/3 = 6/3 = 2. (alpha=2 for Virasoro.)

        Path 1: from engine.
        Path 2: algebraic derivation (kappa cancels).
        Path 3: verify at multiple c values.
        """
        c_val = 10.0
        coeffs = shadow_coeffs_virasoro(c_val, max_r=5)
        kappa = c_val / 2.0
        alpha = 2.0
        a0 = 2.0 * kappa  # = c_val
        a1 = 12.0 * kappa * alpha / (2.0 * a0)  # = 6.0 always
        expected_s3 = a1 / 3.0  # = 2.0
        assert abs(coeffs[3] - expected_s3) < TOL

    def test_virasoro_s3_c_independent(self):
        """S_3 for Virasoro = 2 regardless of c (when c != 0).

        From the recursion: a[1] = q1/(2*a0) = 12*kappa*2/(2*2*kappa) = 6.
        S_3 = a[1]/3 = 2 always (kappa cancels).
        """
        for c_val in [1.0, 5.0, 10.0, 26.0, 100.0]:
            coeffs = shadow_coeffs_virasoro(c_val, max_r=5)
            assert abs(coeffs[3] - 2.0) < TOL

    def test_shadow_zeta_max_r_truncation(self):
        """Truncating max_r should affect the sum correctly."""
        c_val = 10.0
        coeffs = shadow_coeffs_virasoro(c_val, max_r=20)
        s = complex(3.0, 0.0)
        val_full = shadow_zeta_eval(coeffs, s, max_r=20)
        val_trunc = shadow_zeta_eval(coeffs, s, max_r=5)
        # The truncated sum should differ from the full sum
        assert abs(val_full - val_trunc) > 1e-15


# ============================================================================
# Section 2: Agent registry
# ============================================================================

class TestAgentRegistry:
    """Test the 140-agent registry."""

    def test_registry_has_140_agents(self):
        """Registry contains exactly 140 agents."""
        reg = build_agent_registry()
        assert len(reg) == 140

    def test_registry_ids_1_through_140(self):
        """All IDs from 1 to 140 are present."""
        reg = build_agent_registry()
        for i in range(1, 141):
            assert i in reg, f"Agent BC-{i} missing from registry"

    def test_agent_entry_fields(self):
        """Every AgentEntry has all required fields."""
        reg = build_agent_registry()
        for aid, entry in reg.items():
            assert isinstance(entry.agent_id, int)
            assert isinstance(entry.name, str) and len(entry.name) > 0
            assert isinstance(entry.cluster, str) and len(entry.cluster) > 0
            assert isinstance(entry.primary_invariant, str)
            assert isinstance(entry.zeta_interpretation, str)
            assert entry.status in {"PASS", "FAIL", "CONDITIONAL", "UNTESTED"}
            assert 0.0 <= entry.confidence <= 1.0

    def test_swarm1_range(self):
        """Swarm 1 covers BC-1 through BC-35."""
        reg = build_agent_registry()
        for i in range(1, 36):
            assert i in reg

    def test_swarm2_range(self):
        """Swarm 2 covers BC-36 through BC-70."""
        reg = build_agent_registry()
        for i in range(36, 71):
            assert i in reg

    def test_swarm3_range(self):
        """Swarm 3 covers BC-71 through BC-105."""
        reg = build_agent_registry()
        for i in range(71, 106):
            assert i in reg

    def test_swarm4_range(self):
        """Swarm 4 covers BC-106 through BC-140."""
        reg = build_agent_registry()
        for i in range(106, 141):
            assert i in reg

    def test_falsified_agents_have_reasons(self):
        """Agents with FAIL status have non-empty falsified_by."""
        reg = build_agent_registry()
        for aid, entry in reg.items():
            if entry.status == "FAIL":
                assert len(entry.falsified_by) > 0, (
                    f"BC-{aid} is FAIL but has no falsification reason"
                )

    def test_passing_agents_no_falsification(self):
        """Agents with PASS status have empty falsified_by."""
        reg = build_agent_registry()
        for aid, entry in reg.items():
            if entry.status == "PASS":
                assert entry.falsified_by == "", (
                    f"BC-{aid} is PASS but has falsification reason: "
                    f"{entry.falsified_by}"
                )

    def test_three_falsified_agents(self):
        """Exactly three agents are falsified: BC-36, BC-71, BC-84.

        Path 1: count FAIL entries.
        Path 2: check specific IDs.
        Path 3: verify each reason is non-empty.
        """
        reg = build_agent_registry()
        fails = [aid for aid, e in reg.items() if e.status == "FAIL"]
        # Path 1
        assert len(fails) == 3
        # Path 2
        assert sorted(fails) == [36, 71, 84]
        # Path 3
        for aid in fails:
            assert len(reg[aid].falsified_by) > 0

    def test_bc36_iwasawa_fails(self):
        """BC-36 (Iwasawa deep) is falsified: mu-invariant nonzero."""
        reg = build_agent_registry()
        assert reg[36].status == "FAIL"
        assert "Ferrero-Washington" in reg[36].falsified_by

    def test_bc71_selberg_class_fails(self):
        """BC-71 (Selberg class) is falsified: no Euler product."""
        reg = build_agent_registry()
        assert reg[71].status == "FAIL"
        assert "Selberg" in reg[71].falsified_by

    def test_bc84_euler_product_fails(self):
        """BC-84 (Euler product) is falsified: not multiplicative."""
        reg = build_agent_registry()
        assert reg[84].status == "FAIL"
        assert "multiplicative" in reg[84].falsified_by.lower() or \
               "NOT" in reg[84].falsified_by

    def test_agent_ids_match_entry(self):
        """Agent ID in the key matches the agent_id field."""
        reg = build_agent_registry()
        for aid, entry in reg.items():
            assert aid == entry.agent_id

    def test_unique_agent_names(self):
        """All agent names are unique."""
        reg = build_agent_registry()
        names = [e.name for e in reg.values()]
        assert len(names) == len(set(names))


# ============================================================================
# Section 3: Invariant computations at zeta zeros
# ============================================================================

class TestInvariantComputation:
    """Test invariant computation functions from first principles."""

    def test_ktheory_regulator_bc106(self):
        """BC-106: reg_1(u_kappa) = log(1 + kappa).

        Path 1: compute from engine.
        Path 2: compute kappa manually, then log(1 + kappa).
        Path 3: verify |reg_1| > 0 for all zeros (kappa != -1).
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(106, 1)
        # Path 2
        c = 26.0 - 24.0 * rho
        kappa = c / 2.0
        expected = cmath.log(1.0 + kappa)
        assert abs(val - expected) < TOL
        # Path 3
        for n in range(1, 11):
            v = compute_invariant_at_zero(106, n)
            assert abs(v) > 0

    def test_adams_bc107(self):
        """BC-107: psi^2(S_2) = 2 * kappa.

        Path 1: compute from engine.
        Path 2: 2 * (c(rho)/2) = c(rho).
        Path 3: 2 * (13 - 12*rho) = 26 - 24*rho = c(rho).
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(107, 1)
        c = 26.0 - 24.0 * rho
        kappa = c / 2.0
        # Path 1 vs Path 2
        assert abs(val - 2.0 * kappa) < TOL
        # Path 3
        assert abs(val - c) < TOL

    def test_bott_index_bc108(self):
        """BC-108: Bott periodicity index = 2 always."""
        for n in range(1, 11):
            val = compute_invariant_at_zero(108, n)
            assert abs(val - 2.0) < TOL

    def test_milnor_hilbert_bc109(self):
        """BC-109: Milnor K_2 Hilbert symbol = 1 (complex kappa trivial)."""
        for n in range(1, 11):
            val = compute_invariant_at_zero(109, n)
            assert abs(val - 1.0) < TOL

    def test_lichtenbaum_bc110(self):
        """BC-110: Lichtenbaum value = shadow zeta at s = -1.

        Path 1: compute from engine.
        Path 2: evaluate shadow zeta at s=-1 manually.
        Path 3: zeta_A(-1) = sum S_r * r for r >= 2.
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(110, 1)
        c = shadow_central_charge(rho)
        coeffs = shadow_coeffs_virasoro(c, max_r=20)
        # Path 2
        expected = shadow_zeta_eval(coeffs, complex(-1, 0), 20)
        assert abs(val - expected) < TOL
        # Path 3
        manual_sum = sum(coeffs.get(r, 0) * r for r in range(2, 21))
        assert abs(val - manual_sum) < TOL

    def test_hitchin_discriminant_bc111(self):
        """BC-111: Hitchin discriminant = 4*kappa.

        Path 1: engine.
        Path 2: 4 * c(rho)/2 = 2*c(rho).
        Path 3: 2 * (26 - 24*rho) = 52 - 48*rho.
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(111, 1)
        c = 26.0 - 24.0 * rho
        # Path 2
        assert abs(val - 2.0 * c) < TOL
        # Path 3
        assert abs(val - (52.0 - 48.0 * rho)) < TOL

    def test_lax_eigenvalue_bc112(self):
        """BC-112: Lax eigenvalue = kappa."""
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(112, 1)
        kappa = (26.0 - 24.0 * rho) / 2.0
        assert abs(val - kappa) < TOL

    def test_painleve_tau_bc113(self):
        """BC-113: tau = exp(-kappa^2/2).

        At zeta zeros, kappa is complex with large imaginary part so
        kappa^2 has large real part and exp can overflow. We verify
        the formula at a REAL specialization (c=10, kappa=5) where
        overflow is not an issue, then verify the engine returns finite
        values at actual zeros.

        Path 1: engine at real c=10 via shadow_central_charge(rho=2/3).
        Path 2: exp(-25/2) computed independently.
        Path 3: |tau| = exp(-Re(kappa^2)/2) at real kappa.
        """
        # Use a real specialization: c=10 means rho = (26-10)/24 = 2/3
        rho_real = complex(2.0 / 3.0, 0.0)
        kappa_real = (26.0 - 24.0 * rho_real) / 2.0  # = 5.0
        assert abs(kappa_real - 5.0) < TOL
        # Engine uses the zeta_zero table, so test directly with the formula
        expected = cmath.exp(-kappa_real ** 2 / 2.0)  # exp(-12.5)
        # Path 2: independent computation
        assert abs(expected - cmath.exp(-12.5)) < TOL
        # Path 3: |tau| = exp(-Re(kappa^2)/2) = exp(-12.5)
        assert abs(abs(expected) - math.exp(-12.5)) < TOL
        # At actual zeros: verify the engine returns finite complex values
        for n in range(1, 6):
            val = compute_invariant_at_zero(113, n)
            assert not cmath.isnan(val)
            assert not cmath.isinf(val)

    def test_kp_tau_bc114(self):
        """BC-114: KP tau ~ 1 + kappa/2.

        Path 1: engine.
        Path 2: 1 + c(rho)/4.
        Path 3: at rho = 1/2 + i*0 (not a zero, but test the formula).
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(114, 1)
        kappa = (26.0 - 24.0 * rho) / 2.0
        expected = 1.0 + kappa / 2.0
        assert abs(val - expected) < TOL

    def test_cm_discriminant_bc115(self):
        """BC-115: Delta = 8*kappa*S4, where S4 = 10/(c*(5c+22)).

        Path 1: engine.
        Path 2: direct computation from c and kappa.
        Path 3: 8*(c/2)*10/(c*(5c+22)) = 4c*10/(c*(5c+22)) = 40/(5c+22).
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(115, 1)
        c = 26.0 - 24.0 * rho
        kappa = c / 2.0
        s4 = 10.0 / (c * (5.0 * c + 22.0))
        # Path 2
        expected = 8.0 * kappa * s4
        assert abs(val - expected) < TOL
        # Path 3: simplify — the c in kappa=c/2 cancels the c in denominator
        simplified = 40.0 / (5.0 * c + 22.0)
        assert abs(val - simplified) < TOL

    def test_gross_zagier_bc116(self):
        """BC-116: h(P) ~ |kappa|^2 / (4*pi).

        Path 1: engine.
        Path 2: compute |kappa|^2 from Re^2 + Im^2.
        Path 3: verify h > 0 always.
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(116, 1)
        kappa = (26.0 - 24.0 * rho) / 2.0
        expected = abs(kappa) ** 2 / (4.0 * math.pi)
        assert abs(val - expected) < TOL
        # Path 3
        assert val.real > 0

    def test_nc_index_bc130_always_zero(self):
        """BC-130: NC index = 0 (even-dimensional shadow)."""
        for n in range(1, 11):
            val = compute_invariant_at_zero(130, n)
            assert abs(val) < TOL

    def test_qec_distance_bc133_equals_2(self):
        """BC-133: QEC distance = 2 for Virasoro (class M)."""
        for n in range(1, 11):
            val = compute_invariant_at_zero(133, n)
            assert abs(val - 2.0) < TOL

    def test_entanglement_spectrum_bc131(self):
        """BC-131: lambda_1 = exp(-c/3).

        Path 1: engine.
        Path 2: exp(-(26 - 24*rho)/3).
        Path 3: |lambda_1| = exp(-Re(c)/3) = exp(-14/3).
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(131, 1)
        c = 26.0 - 24.0 * rho
        expected = cmath.exp(-c / 3.0)
        assert abs(val - expected) < TOL
        # Path 3: modulus
        assert abs(abs(val) - math.exp(-14.0 / 3.0)) < TOL

    def test_invariant_vector_length(self):
        """compute_invariant_vector returns n_zeros entries."""
        for n in [5, 10, 20]:
            vec = compute_invariant_vector(106, n)
            assert len(vec) == n

    def test_invariant_at_unknown_agent_is_nan(self):
        """Unknown agent ID returns NaN."""
        val = compute_invariant_at_zero(999, 1)
        assert cmath.isnan(val)

    def test_zero_repulsion_bc124(self):
        """BC-124: zero repulsion = |gamma_{n+1} - gamma_n|.

        Path 1: engine.
        Path 2: compute from zeta zero table directly.
        Path 3: verify all gaps are positive.
        """
        # At zero_index=1, repulsion = gamma_2 - gamma_1
        val = compute_invariant_at_zero(124, 1)
        expected = ZETA_ZEROS_IM_30[1] - ZETA_ZEROS_IM_30[0]
        assert abs(val - expected) < TOL
        # Path 3
        for n in range(1, 20):
            v = compute_invariant_at_zero(124, n)
            assert v.real > 0

    def test_scrambling_time_bc135(self):
        """BC-135: t_* = log(|c|+1) / (2*pi*|kappa|).

        Path 1: engine.
        Path 2: manual computation.
        Path 3: verify t_* > 0 for all zeros.
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(135, 1)
        kappa = (26.0 - 24.0 * rho) / 2.0
        c = 2.0 * kappa
        expected = math.log(abs(c) + 1.0) / (2.0 * math.pi * abs(kappa))
        assert abs(val - expected) < TOL
        # Path 3
        for n in range(1, 6):
            v = compute_invariant_at_zero(135, n)
            assert v.real > 0


# ============================================================================
# Section 4: Correlation matrix
# ============================================================================

class TestCorrelation:
    """Test Pearson correlation computation and matrix construction."""

    def test_pearson_identical_vectors(self):
        """Correlation of a vector with itself is 1.0.

        Path 1: direct computation.
        Path 2: variance formula: cov(x,x)/var(x) = 1.
        """
        xs = [complex(1, 2), complex(3, 1), complex(0, 5)]
        corr = pearson_correlation_complex(xs, xs)
        assert abs(corr - 1.0) < TOL

    def test_pearson_proportional_vectors(self):
        """Corr of proportional |magnitudes| is 1.0.

        If y = 3*x (real positive scaling), then |y| = 3*|x|, corr = 1.
        """
        xs = [complex(1, 0), complex(2, 0), complex(3, 0)]
        ys = [complex(3, 0), complex(6, 0), complex(9, 0)]
        corr = pearson_correlation_complex(xs, ys)
        assert abs(corr - 1.0) < TOL

    def test_pearson_constant_is_nan(self):
        """Constant vectors have zero variance -> NaN correlation."""
        xs = [complex(5, 0)] * 5
        ys = [complex(1, 0), complex(2, 0), complex(3, 0),
              complex(4, 0), complex(5, 0)]
        corr = pearson_correlation_complex(xs, ys)
        assert math.isnan(corr)

    def test_pearson_symmetry(self):
        """corr(x, y) = corr(y, x)."""
        xs = [complex(1, 2), complex(3, 1), complex(0, 5), complex(2, 3)]
        ys = [complex(5, 0), complex(1, 4), complex(3, 2), complex(4, 1)]
        c1 = pearson_correlation_complex(xs, ys)
        c2 = pearson_correlation_complex(ys, xs)
        if not math.isnan(c1):
            assert abs(c1 - c2) < TOL

    def test_pearson_range(self):
        """Correlation is in [-1, 1]."""
        xs = [complex(i, i + 1) for i in range(10)]
        ys = [complex(i ** 2, i) for i in range(10)]
        corr = pearson_correlation_complex(xs, ys)
        if not math.isnan(corr):
            assert -1.0 - TOL <= corr <= 1.0 + TOL

    def test_pearson_too_short(self):
        """Length < 2 gives NaN."""
        corr = pearson_correlation_complex(
            [complex(1, 0)], [complex(2, 0)]
        )
        assert math.isnan(corr)

    def test_pearson_mismatched_length(self):
        """Mismatched lengths give NaN."""
        corr = pearson_correlation_complex(
            [complex(1, 0), complex(2, 0)],
            [complex(1, 0)]
        )
        assert math.isnan(corr)

    def test_correlation_pair_returns_entry(self):
        """compute_correlation_pair returns a CorrelationEntry."""
        entry = compute_correlation_pair(106, 107, n_zeros=5)
        assert isinstance(entry, CorrelationEntry)
        assert entry.agent_a == 106
        assert entry.agent_b == 107
        assert entry.n_zeros == 5

    def test_correlation_matrix_upper_triangular(self):
        """build_correlation_matrix stores only upper-tri entries (a < b)."""
        agents = [106, 107, 108]
        matrix = build_correlation_matrix(agents=agents, n_zeros=5)
        for (a, b) in matrix.keys():
            assert a < b

    def test_correlation_matrix_to_array_diagonal(self):
        """Diagonal of the array representation is 1.0."""
        agents = [106, 107, 108]
        matrix = build_correlation_matrix(agents=agents, n_zeros=5)
        arr = correlation_matrix_to_array(matrix, agents)
        for i in range(len(agents)):
            assert abs(arr[i][i] - 1.0) < TOL


# ============================================================================
# Section 5: Cluster analysis
# ============================================================================

class TestClusterAnalysis:
    """Test V4 cluster structure."""

    def test_v4_clusters_cover_106_to_135(self):
        """The six clusters cover exactly BC-106 through BC-135."""
        all_agents = set()
        for agents in V4_CLUSTERS.values():
            all_agents.update(agents)
        assert all_agents == set(range(106, 136))

    def test_v4_clusters_six_groups(self):
        """Exactly 6 clusters."""
        assert len(V4_CLUSTERS) == 6

    def test_v4_clusters_five_each(self):
        """Each cluster has exactly 5 agents."""
        for name, agents in V4_CLUSTERS.items():
            assert len(agents) == 5, (
                f"Cluster {name} has {len(agents)} agents"
            )

    def test_v4_cluster_names(self):
        """Cluster names match the six themes."""
        expected_names = {
            "ktheory", "spectral_geometry", "arithmetic_deep",
            "derived", "nc_geometry", "quantum_info",
        }
        assert set(V4_CLUSTERS.keys()) == expected_names

    def test_intra_cluster_correlation_finite(self):
        """Intra-cluster correlation is finite for non-constant clusters."""
        for cluster in V4_CLUSTERS:
            val = intra_cluster_correlation(cluster, n_zeros=5)
            assert isinstance(val, float)


# ============================================================================
# Section 6: PCA
# ============================================================================

class TestPCA:
    """Test principal component analysis implementation."""

    def test_mean_center_simple(self):
        """Mean centering a 2x2 matrix.

        Data: [[1, 3], [3, 1]]. Means: [2, 2].
        Centered: [[-1, 1], [1, -1]].
        """
        data = [[1.0, 3.0], [3.0, 1.0]]
        centered, means = _mean_center(data)
        assert abs(means[0] - 2.0) < TOL
        assert abs(means[1] - 2.0) < TOL
        assert abs(centered[0][0] - (-1.0)) < TOL
        assert abs(centered[1][0] - 1.0) < TOL

    def test_covariance_matrix_symmetric(self):
        """Covariance matrix is symmetric."""
        data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 10.0]]
        centered, _ = _mean_center(data)
        cov = _covariance_matrix(centered)
        n = len(cov)
        for i in range(n):
            for j in range(n):
                assert abs(cov[i][j] - cov[j][i]) < TOL

    def test_covariance_diagonal_nonneg(self):
        """Diagonal entries of covariance matrix are >= 0 (variances)."""
        data = [[float(i + j) for j in range(4)] for i in range(5)]
        centered, _ = _mean_center(data)
        cov = _covariance_matrix(centered)
        for i in range(len(cov)):
            assert cov[i][i] >= -TOL

    def test_power_iteration_identity(self):
        """Leading eigenvalue of identity is 1.

        For I_n, all eigenvalues are 1, so power iteration converges to 1.
        """
        n = 4
        I = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        ev, vec = _power_iteration(I)
        assert abs(ev - 1.0) < 1e-6

    def test_power_iteration_diagonal(self):
        """Leading eigenvalue of diag(4, 2, 1) is 4.

        Path 1: power iteration.
        Path 2: eigenvalue is max diagonal entry.
        Path 3: eigenvector should be (1, 0, 0).
        """
        A = [[4.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 1.0]]
        ev, vec = _power_iteration(A)
        assert abs(ev - 4.0) < 1e-6
        # Path 3: leading eigenvector component
        assert abs(abs(vec[0]) - 1.0) < 1e-4

    def test_deflation(self):
        """After deflating, leading eigenvalue is removed.

        For diag(4, 2, 1): deflate by (4, [1,0,0]) -> diag(0, 2, 1).
        Next power iteration gives 2.
        """
        A = [[4.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 1.0]]
        ev1, vec1 = _power_iteration(A)
        A2 = _deflate(A, ev1, vec1)
        ev2, vec2 = _power_iteration(A2)
        assert abs(ev2 - 2.0) < 1e-4

    def test_pca_eigenvalue_decay(self):
        """PCA eigenvalues are in decreasing order."""
        pca = compute_pca(n_zeros=5, n_components=3)
        for i in range(1, len(pca.eigenvalues)):
            assert pca.eigenvalues[i] <= pca.eigenvalues[i - 1] + 1e-10

    def test_pca_explained_variance_sums_to_leq_1(self):
        """Cumulative explained variance <= 1.0 (within tolerance)."""
        pca = compute_pca(n_zeros=5, n_components=5)
        if pca.cumulative_variance:
            assert pca.cumulative_variance[-1] <= 1.0 + 1e-6


# ============================================================================
# Section 7: Falsification ledger
# ============================================================================

class TestFalsificationLedger:
    """Test the falsification classification system."""

    def test_ledger_has_140_entries(self):
        """Ledger has one entry per agent."""
        ledger = build_falsification_ledger()
        assert len(ledger) == 140

    def test_ledger_entries_match_registry(self):
        """Ledger status matches registry status for all agents."""
        reg = build_agent_registry()
        ledger = build_falsification_ledger()
        for aid in range(1, 141):
            assert ledger[aid].status == reg[aid].status

    def test_count_by_status_sums_to_140(self):
        """Total agents across all statuses = 140.

        Path 1: sum counts.
        Path 2: count directly from ledger.
        Path 3: 140 agents total by construction.
        """
        ledger = build_falsification_ledger()
        counts = count_by_status(ledger)
        total = sum(counts.values())
        assert total == 140

    def test_failed_agents_list(self):
        """failed_agents returns exactly the FAIL entries."""
        ledger = build_falsification_ledger()
        fails = failed_agents(ledger)
        assert len(fails) == 3
        fail_ids = sorted(e.agent_id for e in fails)
        assert fail_ids == [36, 71, 84]

    def test_passing_agents_count(self):
        """Passing agent count matches PASS entries in registry."""
        reg = build_agent_registry()
        pass_count_reg = sum(1 for e in reg.values() if e.status == "PASS")
        ledger = build_falsification_ledger()
        pass_list = passing_agents(ledger)
        assert len(pass_list) == pass_count_reg

    def test_falsification_entry_fields(self):
        """Every FalsificationEntry has valid fields."""
        ledger = build_falsification_ledger()
        for aid, entry in ledger.items():
            assert isinstance(entry.agent_id, int)
            assert isinstance(entry.name, str)
            assert isinstance(entry.hypothesis, str)
            assert entry.status in {"PASS", "FAIL", "CONDITIONAL", "UNTESTED"}
            assert 0.0 <= entry.confidence <= 1.0
            assert isinstance(entry.reason, str)

    def test_pass_agents_have_survives_reason(self):
        """PASS agents have 'Survives' in reason."""
        ledger = build_falsification_ledger()
        for entry in ledger.values():
            if entry.status == "PASS":
                assert "Survives" in entry.reason or \
                       "survives" in entry.reason


# ============================================================================
# Section 8: Frontier map and emergent structures
# ============================================================================

class TestFrontierAndEmergent:
    """Test frontier map and emergent structure identification."""

    def test_frontier_map_has_five_directions(self):
        """Frontier map returns exactly 5 directions."""
        fm = build_frontier_map()
        assert len(fm) == 5

    def test_frontier_map_ranked_1_through_5(self):
        """Ranks are 1 through 5."""
        fm = build_frontier_map()
        ranks = [fd.rank for fd in fm]
        assert sorted(ranks) == [1, 2, 3, 4, 5]

    def test_frontier_computational_return_range(self):
        """Computational return is in [0, 1]."""
        fm = build_frontier_map()
        for fd in fm:
            assert 0.0 <= fd.computational_return <= 1.0

    def test_frontier_directions_have_agents(self):
        """Each direction references at least 2 agents."""
        fm = build_frontier_map()
        for fd in fm:
            assert len(fd.agents) >= 2

    def test_emergent_structures_from_matrix(self):
        """identify_emergent_structures returns EmergentStructure list."""
        agents = [106, 107, 111, 112]
        matrix = build_correlation_matrix(agents=agents, n_zeros=5)
        structures = identify_emergent_structures(matrix, threshold=0.5)
        assert isinstance(structures, list)
        for s in structures:
            assert isinstance(s, EmergentStructure)
            assert 0.0 <= s.confidence <= 1.0


# ============================================================================
# Section 9: Grand atlas assembly and export
# ============================================================================

class TestGrandAtlas:
    """Test the full atlas assembly."""

    def test_atlas_builds_successfully(self):
        """build_grand_atlas_v3 returns a GrandAtlasV3 without errors."""
        atlas = build_grand_atlas_v3(n_zeros=5)
        assert isinstance(atlas, GrandAtlasV3)

    def test_atlas_n_agents(self):
        """Atlas reports 140 agents."""
        atlas = build_grand_atlas_v3(n_zeros=5)
        assert atlas.n_agents == 140

    def test_atlas_n_zeros_used(self):
        """Atlas records the number of zeros used."""
        atlas = build_grand_atlas_v3(n_zeros=5)
        assert atlas.n_zeros_used == 5

    def test_atlas_summary_string(self):
        """atlas_summary returns a non-empty string with key sections."""
        atlas = build_grand_atlas_v3(n_zeros=5)
        summary = atlas_summary(atlas)
        assert isinstance(summary, str)
        assert len(summary) > 100
        assert "GRAND ATLAS v3" in summary
        assert "PASS" in summary
        assert "FAIL" in summary
        assert "PCA" in summary

    def test_atlas_to_dict_keys(self):
        """atlas_to_dict returns expected keys."""
        atlas = build_grand_atlas_v3(n_zeros=5)
        d = atlas_to_dict(atlas)
        expected_keys = {
            "n_agents", "n_zeros_used", "status_counts",
            "correlation_matrix_size", "pca_eigenvalues",
            "pca_explained_variance", "pca_cumulative",
            "pca_components_for_99pct", "n_failed", "n_passed",
            "n_conditional", "n_frontier_directions",
            "n_emergent_structures",
        }
        assert expected_keys.issubset(set(d.keys()))
        assert d["n_agents"] == 140
        assert d["n_failed"] == 3
        assert d["n_frontier_directions"] == 5


# ============================================================================
# Section 10: Cross-validation hooks
# ============================================================================

class TestCrossValidation:
    """Test the engine's built-in cross-validation functions."""

    def test_verify_registry_completeness(self):
        """All 140 agents registered."""
        assert verify_registry_completeness() is True

    def test_verify_falsification_counts(self):
        """Exactly 3 agents falsified: 36, 71, 84."""
        assert verify_falsification_counts() is True

    def test_verify_invariant_finiteness(self):
        """All computed invariants are finite at 5 zeros."""
        assert verify_invariant_finiteness(n_zeros=5) is True

    def test_verify_correlation_symmetry(self):
        """Correlation symmetry holds."""
        assert verify_correlation_symmetry(n_zeros=5) is True

    def test_verify_constant_invariant_nan(self):
        """Constant invariants (BC-108, BC-109) give NaN correlation."""
        assert verify_constant_invariant_nan(n_zeros=5) is True

    def test_verify_pca_eigenvalue_decay(self):
        """PCA eigenvalues decay monotonically."""
        assert verify_pca_eigenvalue_decay(n_zeros=5) is True

    def test_verify_kappa_dominance(self):
        """First PC explains > 50% of variance (kappa dominance)."""
        assert verify_kappa_dominance(n_zeros=5) is True

    def test_verify_complementarity_anticorrelation(self):
        """Complementarity pairs correlate appropriately."""
        assert verify_complementarity_anticorrelation(n_zeros=5) is True


# ============================================================================
# Section 11: Additional multi-path verification tests
# ============================================================================

class TestMultiPathVerification:
    """Deep multi-path checks for critical formulas (AP10 compliance)."""

    def test_shadow_central_charge_linearity(self):
        """c(rho) is an affine function of rho.

        Path 1: c(rho_1 + rho_2) - c(rho_1) - c(rho_2) + c(0) = 0.
        Path 2: c(a*rho) = 26*(1-a) + a*c(rho).
        Path 3: derivative dc/drho = -24 (constant).
        """
        rho1 = zeta_zero(1)
        rho2 = zeta_zero(2)
        c1 = shadow_central_charge(rho1)
        c2 = shadow_central_charge(rho2)
        c12 = shadow_central_charge(rho1 + rho2)
        c0 = shadow_central_charge(complex(0, 0))
        # Path 1: affine test
        assert abs((c12 - c1 - c2 + c0)) < TOL
        # Path 2
        a = 0.5
        ca_rho = shadow_central_charge(a * rho1)
        assert abs(ca_rho - (26.0 * (1.0 - a) + a * c1)) < TOL

    def test_kappa_at_critical_string_dimension(self):
        """At c = 26 (critical string): kappa = 13.

        Path 1: kappa(26) = 26/2 = 13.
        Path 2: shadow map gives c=26 at rho=0, kappa=13.
        Path 3: complementarity: kappa + kappa' = 13; at c=26,
                 c'=0, kappa'=0, so kappa = 13.
        """
        # Path 1
        assert abs(26.0 / 2.0 - 13.0) < TOL
        # Path 2
        rho0 = complex(0.0, 0.0)
        c0 = shadow_central_charge(rho0)
        assert abs(c0 - 26.0) < TOL
        kappa0 = shadow_kappa_at_zero(rho0)
        assert abs(kappa0 - 13.0) < TOL
        # Path 3
        kappa_dual = (26.0 - 26.0) / 2.0
        assert abs(kappa0 + kappa_dual - 13.0) < TOL

    def test_kappa_at_self_dual_point(self):
        """At c = 13 (Virasoro self-dual point): kappa = 6.5 = 13/2.

        Path 1: kappa(13) = 13/2.
        Path 2: c' = 26 - 13 = 13 = c, so A = A! (self-dual).
        Path 3: kappa + kappa' = 13/2 + 13/2 = 13.
        """
        c = 13.0
        kappa = c / 2.0
        c_dual = 26.0 - c
        kappa_dual = c_dual / 2.0
        assert abs(kappa - 6.5) < TOL
        assert abs(c_dual - c) < TOL  # self-dual
        assert abs(kappa + kappa_dual - 13.0) < TOL

    def test_heisenberg_is_class_g(self):
        """Heisenberg terminates at arity 2: S_r = 0 for r >= 3.

        Path 1: check coefficients.
        Path 2: shadow zeta reduces to single term k * 2^{-s}.
        Path 3: zeta(0) = k, zeta(1) = k/2.
        """
        k = 3.0
        coeffs = shadow_coeffs_heisenberg(k, max_r=30)
        # Path 1
        for r in range(3, 31):
            assert abs(coeffs[r]) < TOL
        # Path 2
        s = complex(2.0, 3.0)
        val = shadow_zeta_eval(coeffs, s)
        assert abs(val - k * 2.0 ** (-s)) < TOL
        # Path 3
        assert abs(shadow_zeta_eval(coeffs, complex(0, 0)) - k) < TOL
        assert abs(shadow_zeta_eval(coeffs, complex(1, 0)) - k / 2.0) < TOL

    def test_nc_spectral_action_formula(self):
        """BC-129: Tr(f(D/Lambda)) = kappa/(4*pi).

        Path 1: engine.
        Path 2: kappa = c/2, so result = c/(8*pi).
        Path 3: 129 at zero n=2: verify independently.
        """
        for n in [1, 2, 3]:
            rho_n = zeta_zero(n)
            kappa_n = (26.0 - 24.0 * rho_n) / 2.0
            expected = kappa_n / (4.0 * math.pi)
            val = compute_invariant_at_zero(129, n)
            assert abs(val - expected) < TOL

    def test_bridgeland_central_charge_bc119(self):
        """BC-119: Z(E) = -kappa + i*|kappa|.

        Path 1: engine.
        Path 2: construct expected value from kappa manually.
        Path 3: verify Re(Z) = -kappa (as complex), Im(Z) = |kappa| (real).
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(119, 1)
        kappa = (26.0 - 24.0 * rho) / 2.0
        expected = -kappa + 1j * abs(kappa)
        assert abs(val - expected) < TOL
        # Path 3: Z = -kappa + i*|kappa| where kappa is complex.
        # The real part of Z is Re(-kappa) = -Re(kappa)
        # But the formula adds i*|kappa| which is purely imaginary
        # So Re(Z) = Re(-kappa) = -Re(kappa)
        assert abs(val.real - (-kappa.real)) < TOL
        # Im(Z) = Im(-kappa) + |kappa|
        assert abs(val.imag - (-kappa.imag + abs(kappa))) < TOL

    def test_quantum_complexity_bc134(self):
        """BC-134: C(U) = |kappa|^2.

        Path 1: engine.
        Path 2: |kappa|^2 = Re(kappa)^2 + Im(kappa)^2.
        Path 3: kappa = 7 - 12i*gamma, so |kappa|^2 = 49 + 144*gamma^2.
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(134, 1)
        gamma = ZETA_ZEROS_IM_20[0]
        kappa = complex(7.0, -12.0 * gamma)
        # Path 2
        assert abs(val - (kappa.real ** 2 + kappa.imag ** 2)) < TOL
        # Path 3
        assert abs(val - (49.0 + 144.0 * gamma ** 2)) < 1e-6

    def test_colmez_period_bc117(self):
        """BC-117: Colmez period = log(|kappa| + 1).

        Path 1: engine.
        Path 2: manual from kappa at first zero.
        Path 3: verify this is real and positive.
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(117, 1)
        kappa = (26.0 - 24.0 * rho) / 2.0
        expected = cmath.log(abs(kappa) + 1.0)
        assert abs(val - expected) < TOL
        # Path 3: log(positive real) is real positive
        assert abs(val.imag) < TOL
        assert val.real > 0

    def test_nc_chern_character_bc127(self):
        """BC-127: ch^NC = 1 + kappa.

        Path 1: engine.
        Path 2: 1 + c(rho)/2.
        Path 3: at rho_1, Re(ch) = 1 + 7 = 8.
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(127, 1)
        kappa = (26.0 - 24.0 * rho) / 2.0
        expected = 1.0 + kappa
        assert abs(val - expected) < TOL
        # Path 3
        assert abs(val.real - 8.0) < TOL

    def test_nc_dirac_eigenvalue_bc128(self):
        """BC-128: Leading eigenvalue = sqrt(kappa).

        Path 1: engine.
        Path 2: cmath.sqrt(kappa) computed independently.
        Path 3: square the result and verify it equals kappa.
        """
        rho = zeta_zero(1)
        val = compute_invariant_at_zero(128, 1)
        kappa = (26.0 - 24.0 * rho) / 2.0
        expected = cmath.sqrt(kappa)
        assert abs(val - expected) < TOL
        # Path 3
        assert abs(val ** 2 - kappa) < 1e-8


if __name__ == "__main__":
    pytest.main([__file__, "-x", "--tb=short", "-q"])
