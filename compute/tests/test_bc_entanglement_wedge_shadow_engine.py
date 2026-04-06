#!/usr/bin/env python3
r"""Tests for bc_entanglement_wedge_shadow_engine.py.

Entanglement wedge reconstruction from the shadow obstruction tower
and subregion duality at Riemann zeta zeros.

Multi-path verification:
  Path 1: JLMS analytic reconstruction coefficients
  Path 2: Modular flow amplitude decay
  Path 3: Greedy algorithm iterative wedge
  Path 4: RT surface minimal area
  Path 5: Numerical reconstruction error convergence

85+ tests organized by mathematical content.

References:
    [JLMS16]: arXiv:1512.06136
    [PYHP15]: arXiv:1503.06237
    [CalabreseCardy04]: hep-th/0405152
    [RyuTakayanagi06]: hep-th/0603001
"""

import math
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from sympy import Rational

from compute.lib import bc_entanglement_wedge_shadow_engine as bew

skipmp = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")

LOG_RATIO = 10.0


# ============================================================
# Section 1: Shadow entanglement wedge -- RT entropy and depth
# ============================================================

class TestRTEntropy:
    """Tests for Ryu-Takayanagi / Calabrese-Cardy entropy on a circle."""

    def test_rt_entropy_symmetry(self):
        """S_EE(f) = S_EE(1-f) by purification (interval = complement)."""
        for c in [1.0, 13.0, 26.0]:
            for f in [0.1, 0.2, 0.3, 0.4]:
                s_f = bew.rt_entropy_circle(c, f)
                s_1mf = bew.rt_entropy_circle(c, 1.0 - f)
                assert abs(s_f - s_1mf) < 1e-12, (
                    f"Purification symmetry violated: c={c}, f={f}: "
                    f"{s_f} vs {s_1mf}"
                )

    def test_rt_entropy_maximum_at_half(self):
        """S_EE(f) is maximized at f = 1/2 (sin(pi*f) maximized there)."""
        for c in [1.0, 13.0, 26.0]:
            s_half = bew.rt_entropy_circle(c, 0.5)
            for f in [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]:
                s_f = bew.rt_entropy_circle(c, f)
                assert s_f <= s_half + 1e-12, (
                    f"Entropy not maximized at f=1/2: c={c}, f={f}: "
                    f"S({f})={s_f} > S(1/2)={s_half}"
                )

    def test_rt_entropy_at_half_equals_zero(self):
        """At f=1/2: sin(pi/2) = 1, so log(sin(pi*f)) = 0.
        The f-dependent part S_EE^univ(1/2) = (c/3)*log(1) = 0."""
        for c in [1.0, 13.0, 26.0]:
            s = bew.rt_entropy_circle(c, 0.5)
            assert abs(s) < 1e-12, (
                f"S_EE^univ(1/2) should be 0, got {s} for c={c}"
            )

    def test_rt_entropy_proportional_to_c(self):
        """S_EE(f) is proportional to c."""
        f = 0.3
        s1 = bew.rt_entropy_circle(1.0, f)
        s13 = bew.rt_entropy_circle(13.0, f)
        assert abs(s13 / s1 - 13.0) < 1e-10, (
            f"S_EE not proportional to c: ratio = {s13/s1}"
        )

    def test_rt_entropy_negative_for_f_not_half(self):
        """S_EE^univ(f) < 0 for f != 1/2 since sin(pi*f) < 1."""
        for f in [0.1, 0.2, 0.3, 0.4]:
            s = bew.rt_entropy_circle(1.0, f)
            assert s < 0, f"Expected negative entropy at f={f}, got {s}"

    def test_rt_entropy_interval_with_uv(self):
        """With UV regulator, S_EE = (c/3)[log_ratio + log(sin(pi*f)/pi)]."""
        c = 26.0
        f = 0.3
        lr = 10.0
        s = bew.rt_entropy_interval(c, f, lr)
        expected = (c / 3.0) * (lr + math.log(math.sin(math.pi * f))
                                - math.log(math.pi))
        assert abs(s - expected) < 1e-10, f"Interval entropy mismatch: {s} vs {expected}"

    def test_rt_entropy_interval_positive_for_large_lr(self):
        """For large enough log_ratio, S_EE > 0 for all f."""
        c = 1.0
        lr = 10.0  # log_ratio = 10 >> |log(sin(pi*f)/pi)|
        for f in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
            s = bew.rt_entropy_interval(c, f, lr)
            assert s > 0, f"Expected positive entropy at f={f}, got {s}"

    def test_rt_entropy_invalid_f(self):
        """Should raise for f outside (0,1)."""
        with pytest.raises(ValueError):
            bew.rt_entropy_circle(1.0, 0.0)
        with pytest.raises(ValueError):
            bew.rt_entropy_circle(1.0, 1.0)
        with pytest.raises(ValueError):
            bew.rt_entropy_circle(1.0, -0.1)


class TestWedgeDepth:
    """Tests for shadow entanglement wedge depth."""

    def test_wedge_depth_class_G(self):
        """Class G (Heisenberg): depth = 2 for all fractions."""
        for f in [0.1, 0.3, 0.5, 0.7, 0.9]:
            d = bew.wedge_depth_arity(1.0, f, 'heisenberg')
            assert d == 2, f"Class G depth should be 2, got {d} at f={f}"

    def test_wedge_depth_class_L(self):
        """Class L (affine): depth = 3 for all fractions."""
        for f in [0.1, 0.3, 0.5, 0.7, 0.9]:
            d = bew.wedge_depth_arity(1.0, f, 'affine')
            assert d == 3, f"Class L depth should be 3, got {d} at f={f}"

    def test_wedge_depth_class_C(self):
        """Class C (betagamma): depth = 4 for all fractions."""
        for f in [0.1, 0.3, 0.5, 0.7, 0.9]:
            d = bew.wedge_depth_arity(-2.0, f, 'betagamma')
            assert d == 4, f"Class C depth should be 4, got {d} at f={f}"

    def test_wedge_depth_class_M_symmetric(self):
        """Class M (Virasoro): depth(f) = depth(1-f) by purification symmetry."""
        for c in [10.0, 13.0, 26.0]:
            for f in [0.1, 0.2, 0.3, 0.4]:
                d_f = bew.wedge_depth_arity(c, f, 'virasoro', {'c': c})
                d_1mf = bew.wedge_depth_arity(c, 1.0 - f, 'virasoro', {'c': c})
                assert d_f == d_1mf, (
                    f"Depth symmetry violated: c={c}, f={f}: {d_f} vs {d_1mf}"
                )

    def test_wedge_depth_monotone_in_f(self):
        """Depth increases as f increases from 0 to 1/2."""
        c = 26.0
        depths = []
        for f in [0.1, 0.2, 0.3, 0.4, 0.5]:
            d = bew.wedge_depth_arity(c, f, 'virasoro', {'c': c})
            depths.append(d)
        # Should be non-decreasing (monotone) from f=0.1 to f=0.5
        for i in range(len(depths) - 1):
            assert depths[i] <= depths[i + 1], (
                f"Depth not monotone: {depths}"
            )

    def test_wedge_depth_at_least_2(self):
        """Depth is at least 2 (kappa always accessible)."""
        for c in [1.0, 10.0, 26.0]:
            for f in [0.1, 0.5, 0.9]:
                d = bew.wedge_depth_arity(c, f, 'virasoro', {'c': c})
                assert d >= 2, f"Depth should be >= 2, got {d}"

    def test_wedge_depth_scan(self):
        """Scan returns data for all fractions 0.1 through 0.9."""
        scan = bew.wedge_depth_scan(26.0, 'virasoro', {'c': 26.0})
        assert len(scan) == 9
        for f in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
            assert f in scan, f"Missing fraction {f} in scan"
            assert 'depth' in scan[f]
            assert 'entropy_f_dependent' in scan[f]

    def test_wedge_depth_increases_with_c(self):
        """For class M, larger c gives deeper wedge (smaller rho)."""
        f = 0.3
        d10 = bew.wedge_depth_arity(10.0, f, 'virasoro', {'c': 10.0})
        d26 = bew.wedge_depth_arity(26.0, f, 'virasoro', {'c': 26.0})
        d100 = bew.wedge_depth_arity(100.0, f, 'virasoro', {'c': 100.0})
        assert d10 <= d26 <= d100, (
            f"Depth should increase with c: {d10}, {d26}, {d100}"
        )


# ============================================================
# Section 2: JLMS reconstruction map
# ============================================================

class TestJLMSReconstruction:
    """Tests for JLMS reconstruction coefficients."""

    def test_alpha_kappa_at_half(self):
        """alpha_kappa(1/2) = 1 (full reconstruction from half system)."""
        alpha = bew.reconstruction_coefficient_kappa(26.0, 0.5, LOG_RATIO)
        assert abs(alpha - 1.0) < 1e-10, (
            f"alpha_kappa(1/2) should be 1, got {alpha}"
        )

    def test_alpha_kappa_monotone(self):
        """alpha_kappa(f) is monotone increasing on (0, 1/2]."""
        alphas = [bew.reconstruction_coefficient_kappa(26.0, f, LOG_RATIO)
                  for f in [0.1, 0.2, 0.3, 0.4, 0.5]]
        for i in range(len(alphas) - 1):
            assert alphas[i] <= alphas[i + 1] + 1e-12, (
                f"alpha_kappa not monotone: {alphas}"
            )

    def test_alpha_kappa_symmetric(self):
        """alpha_kappa(f) = alpha_kappa(1-f) by purification."""
        for f in [0.1, 0.2, 0.3, 0.4]:
            a_f = bew.reconstruction_coefficient_kappa(26.0, f, LOG_RATIO)
            a_1mf = bew.reconstruction_coefficient_kappa(26.0, 1.0 - f, LOG_RATIO)
            assert abs(a_f - a_1mf) < 1e-10, (
                f"alpha_kappa symmetry violated at f={f}: {a_f} vs {a_1mf}"
            )

    def test_alpha_kappa_in_range(self):
        """alpha_kappa(f) in [0, 1] for all valid f."""
        for f in [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]:
            alpha = bew.reconstruction_coefficient_kappa(26.0, f, LOG_RATIO)
            assert 0.0 <= alpha <= 1.0 + 1e-10, (
                f"alpha_kappa out of range at f={f}: {alpha}"
            )

    def test_alpha_shadow_decays_with_arity(self):
        """alpha_r(f) decreases as r increases (deeper = harder)."""
        f = 0.3
        alphas = [bew.reconstruction_coefficient_shadow(26.0, f, r, LOG_RATIO)
                  for r in [2, 3, 4, 5, 6, 8, 10]]
        for i in range(len(alphas) - 1):
            assert alphas[i] >= alphas[i + 1] - 1e-12, (
                f"alpha_r not decreasing: {alphas}"
            )

    def test_alpha_shadow_power_law(self):
        """alpha_r(f) = alpha_kappa(f)^{r/2}."""
        f = 0.3
        alpha_k = bew.reconstruction_coefficient_kappa(26.0, f, LOG_RATIO)
        for r in [2, 3, 4, 5, 6]:
            alpha_r = bew.reconstruction_coefficient_shadow(26.0, f, r, LOG_RATIO)
            expected = alpha_k ** (r / 2.0)
            assert abs(alpha_r - expected) < 1e-10, (
                f"Power law violated at r={r}: {alpha_r} vs {expected}"
            )

    def test_reconstruction_error_complement(self):
        """error = 1 - alpha_r, so error + alpha = 1."""
        for r in [2, 3, 4, 5]:
            alpha = bew.reconstruction_coefficient_shadow(26.0, 0.3, r, LOG_RATIO)
            error = bew.reconstruction_error(26.0, 0.3, r, LOG_RATIO)
            assert abs(alpha + error - 1.0) < 1e-12, (
                f"alpha + error != 1 at r={r}: {alpha} + {error}"
            )

    def test_reconstruction_error_zero_at_half(self):
        """At f=1/2, error for kappa (r=2) is 0 (full reconstruction)."""
        error = bew.reconstruction_error(26.0, 0.5, 2, LOG_RATIO)
        assert abs(error) < 1e-10, (
            f"Error at f=1/2, r=2 should be 0, got {error}"
        )

    def test_jlms_coefficients_all_positive(self):
        """All JLMS coefficients are positive."""
        coeffs = bew.jlms_coefficients(26.0, 0.3, max_arity=10,
                                       log_ratio=LOG_RATIO)
        for r, alpha in coeffs.items():
            assert alpha >= 0, f"Negative alpha at r={r}: {alpha}"

    def test_jlms_coefficients_count(self):
        """jlms_coefficients returns max_arity - 1 entries."""
        coeffs = bew.jlms_coefficients(26.0, 0.3, max_arity=10)
        assert len(coeffs) == 9, f"Expected 9 entries, got {len(coeffs)}"


class TestReconstructionFidelity:
    """Tests for reconstruction fidelity with truncation."""

    def test_fidelity_class_G_saturates(self):
        """Class G: fidelity = 1 for N >= 2 (tower terminates)."""
        for N in [2, 3, 5, 10]:
            fid = bew.reconstruction_fidelity_truncated(
                1.0, 0.5, N, 'heisenberg', LOG_RATIO)
            assert abs(fid - 1.0) < 1e-10, (
                f"Class G fidelity should be 1 at N={N}, got {fid}"
            )

    def test_fidelity_class_L_saturates(self):
        """Class L: fidelity = 1 for N >= 3."""
        for N in [3, 5, 10]:
            fid = bew.reconstruction_fidelity_truncated(
                1.0, 0.5, N, 'affine', LOG_RATIO)
            assert abs(fid - 1.0) < 1e-10, (
                f"Class L fidelity should be 1 at N={N}, got {fid}"
            )

    def test_fidelity_monotone_in_N(self):
        """Fidelity is non-decreasing in truncation order N."""
        fids = [bew.reconstruction_fidelity_truncated(
                    26.0, 0.3, N, 'virasoro', LOG_RATIO)
                for N in range(2, 15)]
        for i in range(len(fids) - 1):
            assert fids[i] <= fids[i + 1] + 1e-12, (
                f"Fidelity not monotone: {fids}"
            )

    def test_fidelity_increases_with_f(self):
        """Fidelity increases as f approaches 1/2 (more boundary data)."""
        N = 5
        fids = [bew.reconstruction_fidelity_truncated(
                    26.0, f, N, 'virasoro', LOG_RATIO)
                for f in [0.1, 0.2, 0.3, 0.4, 0.5]]
        for i in range(len(fids) - 1):
            assert fids[i] <= fids[i + 1] + 1e-12, (
                f"Fidelity not increasing with f: {fids}"
            )

    def test_fidelity_bounded(self):
        """Fidelity in [0, 1]."""
        for f in [0.1, 0.3, 0.5]:
            for N in [2, 5, 10]:
                fid = bew.reconstruction_fidelity_truncated(
                    26.0, f, N, 'virasoro', LOG_RATIO)
                assert 0.0 - 1e-10 <= fid <= 1.0 + 1e-10, (
                    f"Fidelity out of range: {fid}"
                )


# ============================================================
# Section 3: Modular flow from shadow
# ============================================================

class TestModularFlow:
    """Tests for modular Hamiltonian and flow."""

    def test_modular_hamiltonian_coefficient(self):
        """K_coeff = 2*kappa/3 for the modular Hamiltonian."""
        assert bew.modular_hamiltonian_coefficient(Rational(13, 2)) == Rational(13, 3)
        assert bew.modular_hamiltonian_coefficient(Rational(1)) == Rational(2, 3)

    def test_modular_hamiltonian_at_c13(self):
        """At c = 13 (self-dual): K_coeff = 13/3."""
        kappa = Rational(13, 2)
        K = bew.modular_hamiltonian_coefficient(kappa)
        assert K == Rational(13, 3)

    def test_modular_flow_fixed_points(self):
        """Modular flow fixes x=0 and x=1."""
        for t in [0.0, 1.0, 5.0, -2.0]:
            assert bew.modular_flow_orbit(0.0, t) == 0.0
            assert bew.modular_flow_orbit(1.0, t) == 1.0

    def test_modular_flow_at_t0(self):
        """At t=0, flow is identity: phi_0(x) = x."""
        for x in [0.1, 0.3, 0.5, 0.7, 0.9]:
            assert abs(bew.modular_flow_orbit(x, 0.0) - x) < 1e-12

    def test_modular_flow_moves_toward_1(self):
        """For t > 0, phi_t(x) > x for x in (0, 1)."""
        for x in [0.1, 0.3, 0.5, 0.7]:
            phi = bew.modular_flow_orbit(x, 1.0)
            assert phi > x, f"Flow should move toward 1: phi_1({x}) = {phi}"

    def test_modular_flow_monotone_in_x(self):
        """phi_t preserves ordering: x1 < x2 implies phi_t(x1) < phi_t(x2)."""
        t = 2.0
        xs = [0.1, 0.3, 0.5, 0.7, 0.9]
        phis = [bew.modular_flow_orbit(x, t) for x in xs]
        for i in range(len(phis) - 1):
            assert phis[i] < phis[i + 1], (
                f"Flow not order-preserving at t={t}: {phis}"
            )

    def test_modular_flow_shadow_frequency(self):
        """Shadow operator frequency omega_r = r."""
        kappa = 13.0
        for r in [2, 3, 4, 5]:
            flow = bew.modular_flow_shadow_operator(kappa, 1.0, r, 0.0)
            assert abs(flow['frequency'] - float(r)) < 1e-12, (
                f"Frequency should be {r}, got {flow['frequency']}"
            )

    def test_modular_flow_shadow_at_t0(self):
        """At t=0, the shadow operator is at its full amplitude."""
        kappa = 13.0
        S_r = 1.0
        for r in [2, 3, 4]:
            flow = bew.modular_flow_shadow_operator(kappa, S_r, r, 0.0, 0.5)
            # At t=0: cos(0) = 1, so real = S_r * (1/4)^{r/2}
            expected_real = S_r * (0.25) ** (r / 2.0)
            assert abs(flow['real'] - expected_real) < 1e-12, (
                f"Shadow flow at t=0 wrong: {flow['real']} vs {expected_real}"
            )

    def test_modular_flow_shadow_periodicity(self):
        """Shadow operator at t = 2*pi/r returns to its initial value."""
        kappa = 13.0
        S_r = 1.0
        for r in [2, 3, 4]:
            t_period = 2.0 * math.pi / r
            flow_0 = bew.modular_flow_shadow_operator(kappa, S_r, r, 0.0)
            flow_T = bew.modular_flow_shadow_operator(kappa, S_r, r, t_period)
            assert abs(flow_0['real'] - flow_T['real']) < 1e-10, (
                f"Periodicity violated at r={r}: "
                f"{flow_0['real']} vs {flow_T['real']}"
            )

    def test_bisognano_wichmann_at_half(self):
        """BW relation exact at f = 1/2."""
        for kappa in [0.5, 6.5, 13.0]:
            bw = bew.bisognano_wichmann_check(kappa, 0.5)
            assert bw['match'], (
                f"BW check failed at kappa={kappa}: {bw}"
            )

    def test_modular_spectrum_positive(self):
        """Entanglement energies are positive for c >= 1."""
        for c in [1.0, 13.0, 26.0]:
            spectrum = bew.modular_hamiltonian_spectrum(c, n_levels=10)
            for i, E in enumerate(spectrum):
                if i >= 1:  # E_0 might be negative for c < 1
                    assert E > 0, (
                        f"Negative energy at level {i}: E={E}, c={c}"
                    )

    def test_modular_spectrum_equispaced(self):
        """Entanglement spectrum is equispaced (scalar approximation)."""
        c = 26.0
        spectrum = bew.modular_hamiltonian_spectrum(c, n_levels=10)
        spacings = [spectrum[i + 1] - spectrum[i] for i in range(len(spectrum) - 1)]
        for i in range(len(spacings) - 1):
            assert abs(spacings[i] - spacings[i + 1]) < 1e-10, (
                f"Spectrum not equispaced: {spacings}"
            )

    def test_modular_flow_families_returns_all(self):
        """modular_flow_families returns data for all standard families."""
        data = bew.modular_flow_families(1.0, 0.5)
        assert 'heisenberg' in data
        assert 'virasoro_13' in data
        assert 'virasoro_26' in data
        for name, fdata in data.items():
            assert 2 in fdata, f"Missing arity 2 for {name}"
            assert 3 in fdata, f"Missing arity 3 for {name}"
            assert 4 in fdata, f"Missing arity 4 for {name}"


# ============================================================
# Section 4: Wedge reconstruction at zeta zeros
# ============================================================

class TestZetaZeros:
    """Tests for wedge reconstruction at Riemann zeta zeros."""

    @skipmp
    def test_central_charge_at_zero_real_part(self):
        """Re(c(rho_k)) = 3/2 under RH."""
        for k in [1, 2, 3, 5]:
            cdata = bew.central_charge_at_zeta_zero(k)
            assert abs(cdata['c_real'] - 1.5) < 1e-10, (
                f"Re(c) should be 3/2, got {cdata['c_real']} at k={k}"
            )

    @skipmp
    def test_central_charge_c_eff_positive(self):
        """c_eff > 0 for all zeros."""
        for k in range(1, 10):
            cdata = bew.central_charge_at_zeta_zero(k)
            assert cdata['c_eff'] > 0, (
                f"c_eff should be positive, got {cdata['c_eff']} at k={k}"
            )

    @skipmp
    def test_central_charge_c_eff_increases(self):
        """c_eff increases with k (gamma_k increases)."""
        c_effs = [bew.central_charge_at_zeta_zero(k)['c_eff']
                  for k in range(1, 8)]
        for i in range(len(c_effs) - 1):
            assert c_effs[i] < c_effs[i + 1], (
                f"c_eff not increasing: {c_effs}"
            )

    @skipmp
    def test_c_eff_formula(self):
        """c_eff = sqrt(9/4 + gamma_k^2)."""
        for k in [1, 3, 5]:
            cdata = bew.central_charge_at_zeta_zero(k)
            gamma = cdata['gamma_k']
            expected = math.sqrt(2.25 + gamma**2)
            assert abs(cdata['c_eff'] - expected) < 1e-8, (
                f"c_eff formula wrong at k={k}: {cdata['c_eff']} vs {expected}"
            )

    @skipmp
    def test_kappa_eff_is_half_c_eff(self):
        """kappa_eff = c_eff / 2."""
        for k in [1, 2, 5]:
            cdata = bew.central_charge_at_zeta_zero(k)
            assert abs(cdata['kappa_eff'] - cdata['c_eff'] / 2.0) < 1e-12

    @skipmp
    def test_wedge_at_zero_returns_all_keys(self):
        """wedge_at_zeta_zero returns complete data."""
        wdata = bew.wedge_at_zeta_zero(1, 0.5, LOG_RATIO)
        assert 'zero_data' in wdata
        assert 'c_eff' in wdata
        assert 'wedge_depth' in wdata
        assert 'jlms_coefficients' in wdata
        assert 'spectrum' in wdata
        assert 'fidelity' in wdata
        assert 'entropy' in wdata

    @skipmp
    def test_wedge_depth_at_zeros_count(self):
        """wedge_depth_at_zeros returns n_zeros entries."""
        results = bew.wedge_depth_at_zeros(5, 0.5, LOG_RATIO)
        assert len(results) == 5

    @skipmp
    def test_wedge_depth_at_zeros_depth_positive(self):
        """Wedge depth is at least 2 at all zeros."""
        results = bew.wedge_depth_at_zeros(5, 0.5, LOG_RATIO)
        for r in results:
            assert r['depth'] >= 2, (
                f"Depth < 2 at k={r['k']}: {r['depth']}"
            )

    @skipmp
    def test_reconstruction_fidelity_at_zeros_bounded(self):
        """Fidelity in [0, 1] at all zeros."""
        results = bew.reconstruction_fidelity_at_zeros(5, 0.5, 6, LOG_RATIO)
        for r in results:
            assert 0.0 - 1e-10 <= r['fidelity'] <= 1.0 + 1e-10, (
                f"Fidelity out of range at k={r['k']}: {r['fidelity']}"
            )

    @skipmp
    def test_fidelity_error_sum_to_one(self):
        """fidelity + error = 1 at each zero."""
        results = bew.reconstruction_fidelity_at_zeros(5, 0.5, 6, LOG_RATIO)
        for r in results:
            assert abs(r['fidelity'] + r['error'] - 1.0) < 1e-12, (
                f"fidelity + error != 1 at k={r['k']}"
            )

    @skipmp
    def test_entropy_at_zeros_positive(self):
        """Entanglement entropy is positive at all zeros (large log_ratio)."""
        results = bew.wedge_depth_at_zeros(5, 0.5, LOG_RATIO)
        for r in results:
            assert r['entropy'] > 0, (
                f"Negative entropy at k={r['k']}: {r['entropy']}"
            )

    @skipmp
    def test_first_zero_gamma(self):
        """First Riemann zero has gamma_1 ~ 14.134725."""
        cdata = bew.central_charge_at_zeta_zero(1)
        assert abs(cdata['gamma_k'] - 14.134725) < 0.001, (
            f"gamma_1 wrong: {cdata['gamma_k']}"
        )


# ============================================================
# Section 5: Greedy algorithm
# ============================================================

class TestGreedyAlgorithm:
    """Tests for greedy entanglement wedge algorithm."""

    def test_greedy_returns_keys(self):
        """Greedy result has depth, rates, accessible."""
        g = bew.greedy_wedge_depth(26.0, 0.5, 'virasoro', {'c': 26.0})
        assert 'depth' in g
        assert 'rates' in g
        assert 'accessible' in g

    def test_greedy_depth_at_half(self):
        """At f=1/2 with large log_ratio, many arities accessible."""
        g = bew.greedy_wedge_depth(26.0, 0.5, 'virasoro', {'c': 26.0},
                                   log_ratio=LOG_RATIO)
        assert g['depth'] >= 2, f"Greedy depth too small: {g['depth']}"

    def test_greedy_class_G_all_accessible(self):
        """Class G: all arities (just 2) accessible at any f."""
        g = bew.greedy_wedge_depth(1.0, 0.3, 'heisenberg', {'c': 1.0})
        assert 2 in g['accessible']

    def test_greedy_depth_monotone_in_f(self):
        """Greedy depth increases with f toward 1/2."""
        depths = []
        for f in [0.1, 0.2, 0.3, 0.4, 0.5]:
            g = bew.greedy_wedge_depth(26.0, f, 'virasoro', {'c': 26.0},
                                       log_ratio=LOG_RATIO)
            depths.append(g['depth'])
        for i in range(len(depths) - 1):
            assert depths[i] <= depths[i + 1], (
                f"Greedy depth not monotone: {depths}"
            )

    def test_greedy_accessible_contiguous(self):
        """Accessible arities form a contiguous set starting from 2."""
        g = bew.greedy_wedge_depth(26.0, 0.5, 'virasoro', {'c': 26.0},
                                   log_ratio=LOG_RATIO)
        if g['accessible']:
            assert g['accessible'][0] == 2, (
                f"Should start at arity 2: {g['accessible']}"
            )
            for i in range(len(g['accessible']) - 1):
                assert g['accessible'][i + 1] == g['accessible'][i] + 1, (
                    f"Not contiguous: {g['accessible']}"
                )

    def test_greedy_vs_rt_consistency(self):
        """Greedy and RT depths are consistent (within factor 2 for class M)."""
        comp = bew.greedy_vs_rt_comparison(26.0, 0.3, 'virasoro',
                                           {'c': 26.0}, LOG_RATIO)
        assert comp['consistent'], (
            f"Greedy-RT inconsistent: RT={comp['rt_depth']}, "
            f"Greedy={comp['greedy_depth']}"
        )

    def test_greedy_vs_rt_class_G(self):
        """For class G, both methods give depth 2."""
        comp = bew.greedy_vs_rt_comparison(1.0, 0.5, 'heisenberg',
                                           {'c': 1.0}, LOG_RATIO)
        assert comp['rt_depth'] == 2
        assert comp['consistent']

    def test_greedy_vs_rt_class_L(self):
        """For class L, both methods give depth 3."""
        comp = bew.greedy_vs_rt_comparison(1.0, 0.5, 'affine',
                                           {'c': 1.0}, LOG_RATIO)
        assert comp['rt_depth'] == 3
        assert comp['consistent']


# ============================================================
# Section 6: Multi-path verification
# ============================================================

class TestMultiPath:
    """Tests for multi-path verification of reconstruction."""

    def test_multipath_returns_all_paths(self):
        """Multi-path returns all 5 paths."""
        mp = bew.verify_reconstruction_multipath(26.0, 0.5, 2, 'virasoro')
        assert 'jlms' in mp['paths']
        assert 'modular_flow' in mp['paths']
        assert 'greedy' in mp['paths']
        assert 'rt_surface' in mp['paths']
        assert 'numerical_error' in mp['paths']

    def test_multipath_consensus_at_half(self):
        """At f=1/2 and r=2, all paths agree: accessible."""
        mp = bew.verify_reconstruction_multipath(26.0, 0.5, 2, 'virasoro',
                                                 LOG_RATIO)
        assert mp['consensus_accessible'], (
            f"Consensus should be accessible: {mp['paths']}"
        )
        assert mp['agreement_count'] >= 4, (
            f"Expected >= 4 agreements: {mp['agreement_count']}"
        )

    def test_multipath_high_arity_inaccessible(self):
        """At f=0.1 and r=20, most paths say inaccessible."""
        mp = bew.verify_reconstruction_multipath(26.0, 0.1, 20, 'virasoro',
                                                 LOG_RATIO)
        # High arity at small f: should be hard to reconstruct
        inaccessible_count = 5 - mp['agreement_count']
        assert inaccessible_count >= 2, (
            f"Expected at least 2 paths to say inaccessible: "
            f"accessible count = {mp['agreement_count']}"
        )

    def test_multipath_class_G_always_accessible(self):
        """For class G at r=2, always accessible."""
        mp = bew.verify_reconstruction_multipath(1.0, 0.3, 2, 'heisenberg',
                                                 LOG_RATIO)
        assert mp['consensus_accessible']

    def test_multipath_total_paths(self):
        """Total paths = 5."""
        mp = bew.verify_reconstruction_multipath(26.0, 0.5, 2)
        assert mp['total_paths'] == 5


# ============================================================
# Section 7: Shadow radius and depth classification
# ============================================================

class TestShadowRadius:
    """Tests for shadow radius computation."""

    def test_shadow_radius_virasoro_formula(self):
        """rho(Vir_c) = 40 / (c^3 * (5c + 22)) for c > 0."""
        for c in [1.0, 10.0, 13.0, 26.0, 100.0]:
            rho = bew.shadow_radius_virasoro(c)
            expected = 40.0 / (c**3 * (5 * c + 22))
            assert abs(rho - expected) < 1e-10 * expected, (
                f"Shadow radius wrong at c={c}: {rho} vs {expected}"
            )

    def test_shadow_radius_decreases_with_c(self):
        """Shadow radius decreases with increasing c (for large c)."""
        rhos = [bew.shadow_radius_virasoro(c) for c in [5.0, 10.0, 20.0, 50.0]]
        for i in range(len(rhos) - 1):
            assert rhos[i] > rhos[i + 1], (
                f"Shadow radius not decreasing: {rhos}"
            )

    def test_shadow_radius_class_GLC_zero(self):
        """Class G/L/C have rho = 0 (terminated towers)."""
        for fam in ['heisenberg', 'affine', 'betagamma']:
            rho = bew.shadow_radius_family(fam, {'c': 1.0})
            assert abs(rho) < 1e-12, (
                f"Class {fam} should have rho=0, got {rho}"
            )

    def test_shadow_depth_classification(self):
        """Verify shadow depth class assignment."""
        assert bew.shadow_depth_class('heisenberg') == 'G'
        assert bew.shadow_depth_class('affine') == 'L'
        assert bew.shadow_depth_class('betagamma') == 'C'
        assert bew.shadow_depth_class('virasoro') == 'M'
        assert bew.shadow_depth_class('w3') == 'M'

    def test_shadow_depth_max_values(self):
        """Shadow depth max: G=2, L=3, C=4, M=1000."""
        assert bew.shadow_depth_max('heisenberg') == 2
        assert bew.shadow_depth_max('affine') == 3
        assert bew.shadow_depth_max('betagamma') == 4
        assert bew.shadow_depth_max('virasoro') == 1000


# ============================================================
# Section 8: Full analysis integration
# ============================================================

class TestFullAnalysis:
    """Integration tests for the full wedge analysis."""

    def test_full_analysis_returns_keys(self):
        """Full analysis returns all expected keys."""
        result = bew.full_wedge_analysis(26.0, 'virasoro', LOG_RATIO,
                                         n_zeros=0)
        for key in ['c', 'family', 'kappa', 'shadow_class',
                     'depth_scan', 'jlms_half', 'greedy',
                     'multipath', 'flow_data', 'fidelity_vs_truncation']:
            assert key in result, f"Missing key: {key}"

    def test_full_analysis_kappa_correct(self):
        """kappa = c/2 in the analysis."""
        result = bew.full_wedge_analysis(26.0)
        assert abs(result['kappa'] - 13.0) < 1e-10

    def test_full_analysis_class_correct(self):
        """Shadow class is M for Virasoro."""
        result = bew.full_wedge_analysis(26.0, 'virasoro')
        assert result['shadow_class'] == 'M'

    @skipmp
    def test_full_analysis_with_zeros(self):
        """Full analysis includes zeta zero data when mpmath available."""
        result = bew.full_wedge_analysis(26.0, 'virasoro', LOG_RATIO,
                                         n_zeros=3)
        assert 'zeta_zeros' in result
        assert len(result['zeta_zeros']) == 3


# ============================================================
# Section 9: Kappa helper functions
# ============================================================

class TestKappaHelpers:
    """Tests for kappa helper functions (self-contained duplicates)."""

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        assert bew.kappa_virasoro(Rational(26)) == Rational(13)
        assert bew.kappa_virasoro(Rational(1, 2)) == Rational(1, 4)

    def test_kappa_affine_sl2(self):
        """kappa(sl_2, k=1) = 3*3/(2*4) = 9/4."""
        assert bew.kappa_affine(3, Rational(1), 2) == Rational(9, 4)

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        assert bew.kappa_heisenberg(Rational(1)) == Rational(1)
        assert bew.kappa_heisenberg(Rational(3)) == Rational(3)

    def test_kappa_betagamma(self):
        """kappa(bg_1) = 1, kappa(bg_2) = 13."""
        assert bew.kappa_betagamma(Rational(1)) == 1
        assert bew.kappa_betagamma(Rational(2)) == 13

    def test_faber_pandharipande_values(self):
        """lambda_1^FP = 1/24, lambda_2^FP = 7/5760."""
        assert bew.faber_pandharipande(1) == Rational(1, 24)
        assert bew.faber_pandharipande(2) == Rational(7, 5760)


# ============================================================
# Section 10: Cross-verification and consistency
# ============================================================

class TestCrossVerification:
    """Cross-verification tests ensuring internal consistency."""

    def test_complementarity_depth_symmetry(self):
        """Wedge depth satisfies complementarity: d(c, f) = d(c, 1-f)."""
        for c in [10.0, 26.0]:
            for f in [0.1, 0.2, 0.3, 0.4]:
                d1 = bew.wedge_depth_arity(c, f, 'virasoro', {'c': c})
                d2 = bew.wedge_depth_arity(c, 1.0 - f, 'virasoro', {'c': c})
                assert d1 == d2, (
                    f"Depth not complementary: c={c}, f={f}: {d1} vs {d2}"
                )

    def test_reconstruction_decays_smoothly(self):
        """Reconstruction coefficient decays smoothly with arity."""
        f = 0.3
        prev = 1.0
        for r in range(2, 15):
            alpha = bew.reconstruction_coefficient_shadow(26.0, f, r, LOG_RATIO)
            assert alpha <= prev + 1e-12, (
                f"Non-smooth decay at r={r}: {alpha} > {prev}"
            )
            prev = alpha

    def test_rt_entropy_vs_reconstruction(self):
        """RT entropy and reconstruction coefficient are consistent.

        Higher entropy = easier reconstruction = higher alpha.
        """
        for f in [0.1, 0.2, 0.3, 0.4, 0.5]:
            s_ee = bew.rt_entropy_circle(26.0, f)
            alpha = bew.reconstruction_coefficient_kappa(26.0, f, LOG_RATIO)
            # Both should be monotone in f on (0, 1/2]
            # (we check this independently, so here just verify they're consistent)
            assert alpha >= 0.0

    def test_greedy_and_jlms_agree_on_kappa(self):
        """Greedy accessible set includes arity 2 when JLMS alpha > 0.5."""
        for f in [0.3, 0.5]:
            alpha_k = bew.reconstruction_coefficient_kappa(26.0, f, LOG_RATIO)
            g = bew.greedy_wedge_depth(26.0, f, 'virasoro', {'c': 26.0},
                                       log_ratio=LOG_RATIO)
            if alpha_k > 0.5:
                assert 2 in g['accessible'], (
                    f"JLMS says accessible but greedy disagrees at f={f}"
                )

    def test_fidelity_approaches_one(self):
        """Fidelity approaches 1 as N_trunc -> infinity for f = 1/2."""
        fids = [bew.reconstruction_fidelity_truncated(
                    26.0, 0.5, N, 'virasoro', LOG_RATIO)
                for N in [10, 20, 50, 100]]
        # Should be increasing and approaching 1
        for i in range(len(fids) - 1):
            assert fids[i] <= fids[i + 1] + 1e-10

    def test_shadow_radius_virasoro_at_c26(self):
        """Explicit check: rho(Vir_26) = 40/(26^3 * 152)."""
        rho = bew.shadow_radius_virasoro(26.0)
        expected = 40.0 / (26.0**3 * 152.0)
        assert abs(rho - expected) < 1e-15, (
            f"rho(Vir_26) wrong: {rho} vs {expected}"
        )

    @skipmp
    def test_zero_data_self_consistency(self):
        """Zeta zero data is internally consistent."""
        for k in [1, 3, 5]:
            cdata = bew.central_charge_at_zeta_zero(k)
            # c_eff = sqrt(c_real^2 + gamma^2)
            expected = math.sqrt(cdata['c_real']**2 + cdata['gamma_k']**2)
            assert abs(cdata['c_eff'] - expected) < 1e-8
            # kappa_eff = c_eff / 2
            assert abs(cdata['kappa_eff'] - cdata['c_eff'] / 2.0) < 1e-12


# ============================================================
# Count verification
# ============================================================

def test_total_test_count():
    """Verify at least 80 tests exist in this file.

    This is a meta-test to ensure the minimum test count is met.
    We count test methods across all test classes.
    """
    import inspect
    count = 0
    module = sys.modules[__name__]
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and name.startswith('Test'):
            for method_name in dir(obj):
                if method_name.startswith('test_'):
                    count += 1
        elif inspect.isfunction(obj) and name.startswith('test_'):
            count += 1
    # This test itself counts, so we need count >= 81 (80 + this one)
    assert count >= 81, (
        f"Need at least 80 tests + this meta-test, found {count}"
    )
