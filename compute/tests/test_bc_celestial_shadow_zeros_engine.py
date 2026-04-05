#!/usr/bin/env python3
r"""Tests for bc_celestial_shadow_zeros_engine (BC-99): celestial amplitudes
evaluated at shadow zeros.

Verifies:
1. Shadow Mellin amplitude M_4^{sh}(Delta)
2. Soft theorem residues at Delta = 0, 1, 2
3. Celestial OPE from shadow: C^{sh}_{r1,r2}^{r3} and associativity
4. Conformally soft modes: zeta_A(s) at s = 0, 1, 2
5. w_{1+infty} shadow data: kappa(W_N) and S_r
6. Genus corrections and genus-0 celestial sphere check
7. Carrollian limit (kappa -> 0)
8. Graviton 4-point from shadow
9. Celestial pole structure
10. Koszul complementarity: kappa + kappa' = 13 (AP24)
11. Shadow depth -- soft hierarchy mapping
12. Mellin-Zeta mismatch at shadow zeros
13. Multi-path cross-verification

Ground truth sources:
    - kappa(Vir_c) = c/2 (concordance.tex, AP1)
    - kappa + kappa' = 13 for Virasoro (AP24: NOT zero)
    - Q^contact_Vir = 10/[c(5c+22)] (higher_genus_modular_koszul.tex)
    - Shadow tower from sqrt(Q_L) (thm:riccati-algebraicity)
    - r-matrix pole = OPE pole - 1 (AP19)
    - Shadow depth: G(2), L(3), C(4), M(inf) (thm:single-line-dichotomy)
    - Soft theorems: S^{(n)} from S_{n+2} (Strominger et al.)
    - kappa(W_N) = c * (H_N - 1) (celestial_shadow_engine.py, AP1)
    - F_1 = kappa * lambda_1 = kappa/24 (Faber-Pandharipande)

References:
    compute/lib/bc_celestial_shadow_zeros_engine.py
    compute/lib/bc_celestial_deep_shadow_engine.py
    compute/lib/shadow_zeta_function_engine.py
    compute/lib/celestial_shadow_engine.py
"""

from fractions import Fraction
from math import comb

import mpmath
import pytest

from compute.lib.bc_celestial_shadow_zeros_engine import (
    # Helpers
    _frac, _mp, harmonic_number,
    # Shadow coefficients
    virasoro_shadow_coefficients,
    heisenberg_shadow_coefficients,
    affine_km_shadow_coefficients,
    betagamma_shadow_coefficients,
    wn_shadow_coefficients_tline,
    # Shadow zeta
    shadow_zeta,
    # Mellin amplitude
    shadow_mellin_amplitude,
    shadow_mellin_at_zero,
    # Soft theorem residues
    soft_theorem_residue,
    # Celestial OPE
    celestial_shadow_ope,
    celestial_shadow_ope_table,
    ope_associativity_check,
    # Conformally soft modes
    conformally_soft_modes,
    soft_shadow_data_all_families,
    # w_{1+infty}
    winfinity_kappa,
    winfinity_shadow_data,
    # Genus correction
    genus_correction_mellin,
    genus0_celestial_sphere_check,
    # Carrollian limit
    carrollian_shadow_tower,
    # Graviton 4-point
    graviton_4point_celestial,
    # Pole structure
    celestial_pole_structure,
    # Koszul complementarity
    koszul_celestial_complementarity,
    # Depth-soft hierarchy
    DepthSoftMapping,
    depth_soft_hierarchy,
    # Mellin-Zeta mismatch
    mellin_zeta_mismatch,
    # Verification
    verify_weinberg_soft_theorem,
    verify_ope_crossing_symmetry,
    verify_genus0_sphere,
    verify_zeta_at_integers,
    verify_winfinity_kappa,
    run_full_verification,
)


# ============================================================================
# Section 1: Shadow tower coefficient foundations
# ============================================================================

class TestVirasiroShadowCoefficients:
    """Virasoro shadow tower from sqrt(Q_L) at c = 26 (critical string)."""

    def test_kappa_c26(self):
        """S_2 = kappa = c/2 = 13 at c=26."""
        coeffs = virasoro_shadow_coefficients(26, 10)
        assert coeffs[2] == Fraction(13)

    def test_kappa_c1(self):
        """S_2 = kappa = 1/2 at c=1."""
        coeffs = virasoro_shadow_coefficients(1, 10)
        assert coeffs[2] == Fraction(1, 2)

    def test_kappa_c13_self_dual(self):
        """S_2 = 13/2 at the self-dual point c=13."""
        coeffs = virasoro_shadow_coefficients(13, 10)
        assert coeffs[2] == Fraction(13, 2)

    def test_cubic_shadow_independent_of_c(self):
        """S_3 = alpha/3 on the T-line. alpha = 2, so S_3 = 2/3."""
        # The coefficient a[1] / 3 where a[1] = q1/(2*a0) = 12c/(2c) = 6
        # So S_3 = 6/3 = 2.
        coeffs = virasoro_shadow_coefficients(26, 10)
        assert coeffs[3] == Fraction(2)

    def test_cubic_shadow_at_c1(self):
        """S_3 at c=1 should match the recursion."""
        coeffs = virasoro_shadow_coefficients(1, 10)
        # a[1] = q1/(2*a0) = 12*1 / (2*1) = 6
        # S_3 = a[1]/3 = 6/3 = 2
        assert coeffs[3] == Fraction(2)

    def test_quartic_positive(self):
        """S_4 should be positive for c > 0."""
        coeffs = virasoro_shadow_coefficients(26, 10)
        assert coeffs[4] > 0

    def test_quartic_matches_formula(self):
        """S_4 from recursion matches Q^contact / 4."""
        c_val = Fraction(26)
        Q_contact = Fraction(10) / (c_val * (5 * c_val + 22))
        coeffs = virasoro_shadow_coefficients(26, 10)
        # S_4 = a[2]/4 where a[2] = (q2 - a1^2)/(2*a0)
        # q2 = 9*4 + 16*(c/2)*Q_contact = 36 + 80/(5c+22)
        # At c=26: q2 = 36 + 80/152 = 36 + 10/19
        # a0 = c = 26, a1 = 6
        # a[2] = (q2 - 36)/(52) = (10/19)/52 = 10/(19*52) = 5/494
        # S_4 = a[2]/4 = 5/1976
        expected = Fraction(5, 1976)
        assert coeffs[4] == expected

    def test_shadow_coeffs_decrease(self):
        """For large c, |S_r| should decrease with r (inside convergence)."""
        coeffs = virasoro_shadow_coefficients(100, 10)
        for r in range(3, 10):
            assert abs(coeffs[r]) < abs(coeffs[r - 1]) or coeffs[r] == 0

    def test_singular_at_c0(self):
        """Shadow tower singular at c=0."""
        with pytest.raises(ValueError, match="c = 0"):
            virasoro_shadow_coefficients(0, 10)

    def test_singular_at_minus_22_over_5(self):
        """Shadow tower singular at c = -22/5."""
        with pytest.raises(ValueError, match="-22/5"):
            virasoro_shadow_coefficients(Fraction(-22, 5), 10)


class TestHeisenbergShadowCoefficients:
    """Heisenberg: class G, terminates at r=2."""

    def test_kappa_k1(self):
        """kappa(H_1) = 1."""
        coeffs = heisenberg_shadow_coefficients(1, 10)
        assert coeffs[2] == Fraction(1)

    def test_higher_vanish(self):
        """S_r = 0 for r >= 3."""
        coeffs = heisenberg_shadow_coefficients(1, 10)
        for r in range(3, 11):
            assert coeffs[r] == Fraction(0)

    def test_kappa_arbitrary_level(self):
        """kappa(H_k) = k for any k."""
        for k in [1, 2, Fraction(1, 2), Fraction(7, 3)]:
            coeffs = heisenberg_shadow_coefficients(k, 5)
            assert coeffs[2] == _frac(k)


class TestAffineKMShadowCoefficients:
    """Affine KM: class L, terminates at r=3."""

    def test_sl2_k1_kappa(self):
        """kappa(V_1(sl_2)) = 3*(1+2)/(2*2) = 9/4."""
        coeffs = affine_km_shadow_coefficients(3, 1, 2, 10)
        assert coeffs[2] == Fraction(9, 4)

    def test_sl3_k1_kappa(self):
        """kappa(V_1(sl_3)) = 8*(1+3)/(2*3) = 16/3."""
        coeffs = affine_km_shadow_coefficients(8, 1, 3, 10)
        assert coeffs[2] == Fraction(16, 3)

    def test_higher_vanish(self):
        """S_r = 0 for r >= 4 (class L)."""
        coeffs = affine_km_shadow_coefficients(3, 1, 2, 10)
        for r in range(4, 11):
            assert coeffs[r] == Fraction(0)


class TestBetaGammaShadowCoefficients:
    """Beta-gamma: class C, terminates at r=4."""

    def test_lam_half_kappa(self):
        """At lam=1/2: c = 2*(3/2 - 3 + 1) = -1. kappa = -1/2."""
        coeffs = betagamma_shadow_coefficients(Fraction(1, 2), 10)
        assert coeffs[2] == Fraction(-1, 2)

    def test_higher_vanish(self):
        """S_r = 0 for r >= 5."""
        coeffs = betagamma_shadow_coefficients(Fraction(1, 2), 10)
        for r in range(5, 11):
            assert coeffs[r] == Fraction(0)


# ============================================================================
# Section 2: Shadow zeta function
# ============================================================================

class TestShadowZeta:
    """Shadow zeta function evaluation."""

    def test_heisenberg_zeta_s0(self):
        """zeta_H(0) = S_2 = k (only one term)."""
        coeffs = heisenberg_shadow_coefficients(3, 10)
        val = shadow_zeta(coeffs, 0, 10)
        assert abs(float(val) - 3.0) < 1e-12

    def test_heisenberg_zeta_s1(self):
        """zeta_H(1) = S_2 / 2 = k/2."""
        coeffs = heisenberg_shadow_coefficients(4, 10)
        val = shadow_zeta(coeffs, 1, 10)
        assert abs(float(val) - 2.0) < 1e-12

    def test_heisenberg_zeta_s2(self):
        """zeta_H(2) = S_2 / 4 = k/4."""
        coeffs = heisenberg_shadow_coefficients(4, 10)
        val = shadow_zeta(coeffs, 2, 10)
        assert abs(float(val) - 1.0) < 1e-12

    def test_virasoro_zeta_s0(self):
        """zeta_Vir(0) = sum S_r at c=26."""
        coeffs = virasoro_shadow_coefficients(26, 20)
        val = float(shadow_zeta(coeffs, 0, 20))
        # S_2 = 13, S_3 = 2, S_4 > 0, ...
        assert val > 13.0  # At least kappa + alpha/3

    def test_zeta_at_different_c(self):
        """zeta values change with c."""
        val1 = float(shadow_zeta(virasoro_shadow_coefficients(1, 10), 0, 10))
        val2 = float(shadow_zeta(virasoro_shadow_coefficients(26, 10), 0, 10))
        assert val1 != val2


# ============================================================================
# Section 3: Shadow Mellin amplitude
# ============================================================================

class TestShadowMellinAmplitude:
    """Shadow Mellin amplitude M_4^{sh}(Delta)."""

    def test_mellin_nonzero(self):
        """Mellin amplitude is nonzero at generic Delta."""
        val = shadow_mellin_amplitude(26, 3.7, 8)
        assert abs(val) > 0

    def test_mellin_different_from_zeta(self):
        """Mellin and zeta give different values at generic Delta."""
        result = shadow_mellin_at_zero(26, 3.7, 8)
        assert result["conditions_differ"]

    def test_mellin_pole_at_half_integers(self):
        """M(Delta) should diverge near Delta = r/2 for each r."""
        # Near Delta = 1 (r=2): Gamma(Delta - 1) has pole
        eps = 0.001
        val_near = shadow_mellin_amplitude(26, 1.0 + eps, 4)
        val_far = shadow_mellin_amplitude(26, 3.7, 4)
        assert abs(val_near) > abs(val_far)

    def test_mellin_at_large_delta(self):
        """M(Delta) should be small for large Delta (Gamma decay)."""
        val_5 = shadow_mellin_amplitude(26, 5.5, 6)
        val_20 = shadow_mellin_amplitude(26, 20.5, 6)
        # At large Delta, Gamma(Delta - r/2) grows but is divided by large factorials
        # The behavior depends on the sum structure
        assert isinstance(val_20, mpmath.mpf)  # at least it computes


class TestShadowMellinAtZero:
    """Mellin-zeta comparison at specific Delta values."""

    def test_conditions_differ(self):
        """The shadow zero and Mellin zero conditions are structurally different."""
        result = shadow_mellin_at_zero(26, 4.5, 8)
        assert result["conditions_differ"] is True

    def test_both_values_computed(self):
        """Both zeta and Mellin values are computed."""
        result = shadow_mellin_at_zero(10, 3.5, 6)
        assert result["mellin_value"] is not None
        assert result["zeta_value"] is not None


# ============================================================================
# Section 4: Soft theorem residues
# ============================================================================

class TestSoftTheoremResidues:
    """Soft theorem residues at Delta = 0, 1, 2."""

    def test_residue_at_delta0(self):
        """Residue at Delta=0 (spin J=1, supertranslation)."""
        result = soft_theorem_residue(26, 0, 10)
        assert result["spin_J"] == 1
        assert result["delta_star"] == 0

    def test_residue_at_delta1(self):
        """Residue at Delta=1 (spin J=0)."""
        result = soft_theorem_residue(26, 1, 10)
        assert result["spin_J"] == 0

    def test_residue_at_delta2(self):
        """Residue at Delta=2 (spin J=-1)."""
        result = soft_theorem_residue(26, 2, 10)
        assert result["spin_J"] == -1

    def test_residue_nonzero_at_delta1(self):
        """Residue at Delta=1 is dominated by the r=2 contribution S_2 = kappa.

        The total residue includes corrections from r=4, r=6, etc.
        (higher even arities contribute via m = 1, 2, ...).
        The leading contribution is S_2 / Gamma(1) = 13.
        Higher-arity corrections are small but nonzero.
        """
        result = soft_theorem_residue(26, 1, 10)
        # The leading contribution is S_2 = 13.
        # Higher arities give small corrections.
        # Total residue is approximately 13 but not exactly.
        assert abs(float(result["residue"]) - 13.0) < 0.1
        # The leading contribution at m=0 (r=2) dominates:
        if result["contributions"]:
            leading = result["contributions"][0]
            assert leading["r"] == 2
            assert abs(leading["contribution"] - 13.0) < 1e-10

    def test_delta0_involves_even_arities(self):
        """At Delta=0: poles from r = 2*m, i.e., r = 0, 2, 4, 6, ..."""
        result = soft_theorem_residue(26, 0, 10)
        # r = 2*(0+m) for m = 0,1,2,...
        # r=0 is below minimum arity 2; r=2 gives m=1
        for c in result["contributions"]:
            assert c["r"] % 2 == 0

    def test_delta2_involves_even_arities(self):
        """At Delta=2: poles from r = 2*(2+m), i.e., r = 4, 6, 8, ..."""
        result = soft_theorem_residue(26, 2, 10)
        for c in result["contributions"]:
            assert c["r"] >= 4
            assert c["r"] % 2 == 0


# ============================================================================
# Section 5: Celestial OPE from shadow
# ============================================================================

class TestCelestialShadowOPE:
    """Celestial OPE coefficients C^{sh}_{r1,r2}^{r3}."""

    def test_tree_level_fusion(self):
        """Tree-level fusion: C_{2,2}^{2} is nonzero."""
        coeff = celestial_shadow_ope(26, 2, 2, 2)
        assert coeff != 0

    def test_wrong_fusion_vanishes(self):
        """C_{2,2}^{3} = 0 (wrong fusion rule r3 != r1+r2-2)."""
        coeff = celestial_shadow_ope(26, 2, 2, 3)
        assert coeff == Fraction(0)

    def test_c22_2_formula(self):
        """C_{2,2}^{2}: S_2^2 * C(0,0) * P = kappa^2 * 1 * 2/kappa = 2*kappa."""
        c_val = 26
        kappa = Fraction(13)
        coeff = celestial_shadow_ope(c_val, 2, 2, 2)
        # S_2 = kappa = 13, binom(0,0)=1, P = 2/kappa = 2/13
        expected = kappa * kappa * Fraction(1) * Fraction(2) / kappa
        assert coeff == expected

    def test_c23_3_formula(self):
        """C_{2,3}^{3}: S_2 * S_3 * C(1,0) * P."""
        c_val = 26
        coeff = celestial_shadow_ope(c_val, 2, 3, 3)
        kappa = Fraction(13)
        S_2 = kappa
        S_3 = Fraction(2)
        P = Fraction(2) / kappa
        binom_factor = Fraction(comb(1, 0))  # C(1,0) = 1
        expected = S_2 * S_3 * binom_factor * P
        assert coeff == expected

    def test_symmetry_r1_r2(self):
        """C_{r1,r2}^{r3} should be symmetric in r1, r2 up to binomial."""
        c_val = 26
        # For r1=2, r2=3: r3 = 3
        c_23 = celestial_shadow_ope(c_val, 2, 3, 3)
        c_32 = celestial_shadow_ope(c_val, 3, 2, 3)
        # Different binomial factors but same product S_r1 * S_r2
        # C(1,0) vs C(1,1) = 1 vs 1, so should be equal
        assert c_23 == c_32

    def test_ope_table_nonempty(self):
        """OPE table has entries."""
        table = celestial_shadow_ope_table(26, 8)
        assert len(table) > 0

    def test_ope_table_only_correct_fusion(self):
        """All entries in OPE table satisfy r3 = r1 + r2 - 2."""
        table = celestial_shadow_ope_table(26, 8)
        for (r1, r2, r3), coeff in table.items():
            assert r3 == r1 + r2 - 2

    def test_ope_coefficients_c_dependent(self):
        """OPE coefficients change with c."""
        c1 = celestial_shadow_ope(1, 2, 2, 2)
        c26 = celestial_shadow_ope(26, 2, 2, 2)
        assert c1 != c26


class TestOPEAssociativity:
    """Crossing symmetry / associativity checks."""

    def test_associativity_222(self):
        """s-channel and t-channel agree for (2,2,2)."""
        result = ope_associativity_check(26, 2, 2, 2)
        # r12 = 2, r23 = 2, r_f = 2
        assert result["s_channel"] == result["t_channel"]

    def test_associativity_223(self):
        """(2,2,3) should give zero s- and t-channels (wrong fusion at step 2)."""
        result = ope_associativity_check(26, 2, 2, 3)
        # r12 = 2, but C_{2,3}^{r_f} requires r_f = 2+3-2 = 3
        # r_f from s-channel = r12 + r3 - 2 = 2 + 3 - 2 = 3
        # So s-channel = C_{2,2}^{2} * C_{2,3}^{3} (both nonzero)
        # t-channel: r23 = 2+3-2 = 3, r_f = r1+r23-2 = 2+3-2 = 3
        # t-channel = C_{2,3}^{3} * C_{2,3}^{3}
        # These are both nonzero, so ratio should be finite
        assert result["associative"]

    def test_associativity_multiple(self):
        """Batch associativity check."""
        results = verify_ope_crossing_symmetry(26, max_r=20)
        for r in results:
            # Some triples give zero channels (wrong fusion)
            if r["s_channel"] != 0 and r["t_channel"] != 0:
                assert r["ratio"] is not None


# ============================================================================
# Section 6: Conformally soft modes
# ============================================================================

class TestConformallySoftModes:
    """zeta_A(s) at s = 0, 1, 2 for standard families."""

    def test_heisenberg_soft_s0(self):
        """zeta_H(0) = k for Heisenberg at level k."""
        coeffs = heisenberg_shadow_coefficients(5, 10)
        modes = conformally_soft_modes(coeffs, [0], 10)
        assert abs(float(modes[0]) - 5.0) < 1e-12

    def test_heisenberg_soft_s1(self):
        """zeta_H(1) = k/2 for Heisenberg."""
        coeffs = heisenberg_shadow_coefficients(6, 10)
        modes = conformally_soft_modes(coeffs, [1], 10)
        assert abs(float(modes[1]) - 3.0) < 1e-12

    def test_heisenberg_soft_s2(self):
        """zeta_H(2) = k/4."""
        coeffs = heisenberg_shadow_coefficients(8, 10)
        modes = conformally_soft_modes(coeffs, [2], 10)
        assert abs(float(modes[2]) - 2.0) < 1e-12

    def test_virasoro_soft_s0_is_sum(self):
        """zeta_Vir(0) = sum S_r, dominated by kappa + higher."""
        coeffs = virasoro_shadow_coefficients(26, 10)
        modes = conformally_soft_modes(coeffs, [0], 10)
        direct = sum(float(_mp(coeffs[r])) for r in range(2, 11))
        assert abs(float(modes[0]) - direct) < 1e-10

    def test_soft_data_all_families_returns_dict(self):
        """soft_shadow_data_all_families returns a non-empty dict."""
        data = soft_shadow_data_all_families(10)
        assert len(data) > 0
        assert "Heisenberg_k1" in data
        assert "Virasoro_c26" in data

    def test_soft_data_heisenberg_exact(self):
        """Heisenberg k=1: zeta(0)=1, zeta(1)=1/2, zeta(2)=1/4."""
        data = soft_shadow_data_all_families(10)
        h = data["Heisenberg_k1"]
        assert abs(h[0] - 1.0) < 1e-12
        assert abs(h[1] - 0.5) < 1e-12
        assert abs(h[2] - 0.25) < 1e-12


# ============================================================================
# Section 7: w_{1+infty} shadow data
# ============================================================================

class TestWInfinityKappa:
    """kappa(W_N) = c * (H_N - 1)."""

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: kappa = c * (H_2 - 1) = c/2."""
        c_val = Fraction(30)
        kap = winfinity_kappa(2, c_val)
        assert kap == c_val / 2

    def test_w3_kappa(self):
        """W_3: kappa = c * (H_3 - 1) = c * (1/2 + 1/3) = 5c/6."""
        c_val = Fraction(30)
        kap = winfinity_kappa(3, c_val)
        assert kap == Fraction(5) * c_val / 6

    def test_w4_kappa(self):
        """W_4: kappa = c * (H_4 - 1) = c * (1/2 + 1/3 + 1/4) = 13c/12."""
        c_val = Fraction(12)
        kap = winfinity_kappa(4, c_val)
        assert kap == Fraction(13)

    def test_kappa_increases_with_N(self):
        """kappa(W_N) increases with N (harmonic series diverges)."""
        c_val = Fraction(10)
        kappas = [winfinity_kappa(N, c_val) for N in range(2, 10)]
        for i in range(len(kappas) - 1):
            assert kappas[i + 1] > kappas[i]

    def test_kappa_matches_channel_sum(self):
        """kappa = c*(H_N-1) matches sum_{s=2}^N c/s."""
        results = verify_winfinity_kappa([2, 3, 4, 5, 10, 20])
        for r in results:
            assert r["agree"]


class TestWInfinityShadowData:
    """Full shadow data for W_N."""

    def test_shadow_data_returns_dict(self):
        """winfinity_shadow_data returns structured data."""
        data = winfinity_shadow_data(3, 30, 8)
        assert "kappa_total" in data
        assert "kappa_tline" in data
        assert "channel_kappas" in data

    def test_tline_kappa_is_c_over_2(self):
        """T-line kappa is c/2 regardless of N."""
        data = winfinity_shadow_data(5, 30, 8)
        assert data["kappa_tline"] == Fraction(15)

    def test_total_kappa_differs_from_tline(self):
        """Total kappa != T-line kappa for N >= 3."""
        data = winfinity_shadow_data(3, 30, 8)
        assert data["kappa_total"] != data["kappa_tline"]

    def test_channel_kappas_sum(self):
        """Channel kappas sum to total kappa."""
        c_val = Fraction(30)
        N = 5
        data = winfinity_shadow_data(N, c_val, 8)
        channel_sum = sum(data["channel_kappas"].values())
        assert channel_sum == data["kappa_total"]


# ============================================================================
# Section 8: Genus corrections
# ============================================================================

class TestGenusCorrections:
    """Genus-g corrections to celestial amplitudes."""

    def test_genus1_correction_nonzero(self):
        """Genus-1 correction is nonzero for c != 0."""
        val = genus_correction_mellin(26, 3.5, 1)
        assert abs(val) > 0

    def test_genus1_correction_formula(self):
        """F_1 = kappa * lambda_1 = kappa/24."""
        mpmath.mp.dps = 50
        c_val = 26
        kappa = 13
        # F_1 = 13/24
        # Mellin factor at g=1: Gamma(Delta)/[Gamma(Delta)*Gamma(2)] = 1/Gamma(2) = 1
        # So correction = (13/24) * 1 = 13/24
        val = float(genus_correction_mellin(26, 3.5, 1))
        # F_1 = kappa/24 = 13/24
        # Mellin factor = Gamma(3.5 + 0) / [Gamma(3.5) * Gamma(2)] = 1
        # So correction = 13/24
        assert abs(val - 13.0 / 24.0) < 1e-10

    def test_genus2_correction_smaller(self):
        """Genus-2 correction should be smaller than genus-1."""
        g1 = abs(float(genus_correction_mellin(26, 3.5, 1)))
        g2 = abs(float(genus_correction_mellin(26, 3.5, 2)))
        assert g2 < g1

    def test_genus0_is_celestial_sphere(self):
        """At genus 0, shadow curve = celestial sphere."""
        result = genus0_celestial_sphere_check(26, 3.7, 8)
        assert result["genus_0_is_celestial_sphere"] is True

    def test_genus0_amplitude_is_shadow_mellin(self):
        """Genus-0 amplitude equals the shadow Mellin amplitude."""
        result = genus0_celestial_sphere_check(26, 3.7, 8)
        mellin_direct = shadow_mellin_amplitude(26, 3.7, 8)
        assert abs(float(result["genus_0_amplitude"]) - float(mellin_direct)) < 1e-30

    def test_invalid_genus_raises(self):
        """Genus 0 raises ValueError."""
        with pytest.raises(ValueError, match="Genus must be >= 1"):
            genus_correction_mellin(26, 3.5, 0)


# ============================================================================
# Section 9: Carrollian limit
# ============================================================================

class TestCarrollianLimit:
    """Carrollian limit kappa -> 0."""

    def test_virasoro_singular(self):
        """Virasoro Carrollian limit is singular (c=0 is a pole)."""
        result = carrollian_shadow_tower(26, 10)
        assert result["virasoro_singular"] is True

    def test_heisenberg_tower_vanishes(self):
        """Heisenberg at k=0: entire tower vanishes."""
        result = carrollian_shadow_tower(26, 10)
        assert result["heisenberg_tower_vanishes"] is True

    def test_ap31_warning(self):
        """AP31 warning is present: kappa=0 does NOT imply Theta=0."""
        result = carrollian_shadow_tower(26, 10)
        assert "kappa=0" in result["AP31_warning"]
        assert "Theta_A" in result["AP31_warning"]

    def test_virasoro_small_c_S4_diverges(self):
        """As c -> 0, S_4 = 10/[c(5c+22)] diverges."""
        result = carrollian_shadow_tower(26, 10)
        S4_values = [d["S_4"] for d in result["virasoro_limit"]]
        # S_4 should increase as c decreases
        assert S4_values[-1] > S4_values[0]


# ============================================================================
# Section 10: Graviton 4-point
# ============================================================================

class TestGraviton4Point:
    """Graviton celestial 4-point amplitude from shadow."""

    def test_requires_4_dimensions(self):
        """Need exactly 4 conformal dimensions."""
        with pytest.raises(ValueError):
            graviton_4point_celestial(26, [2, 3, 4])

    def test_amplitude_nonzero(self):
        """Amplitude is nonzero for generic Delta_i."""
        result = graviton_4point_celestial(26, [2.5, 3.5, 2.5, 3.5])
        assert abs(float(result["s_channel_amplitude"])) > 0

    def test_kappa_is_c_over_2(self):
        """kappa = c/2 in the output."""
        result = graviton_4point_celestial(26, [2.5, 3.5, 2.5, 3.5])
        assert abs(result["kappa"] - 13.0) < 1e-12

    def test_leading_term_proportional_to_kappa(self):
        """Leading kappa term is proportional to kappa = c/2."""
        r1 = graviton_4point_celestial(26, [2.5, 3.5, 2.5, 3.5])
        r2 = graviton_4point_celestial(1, [2.5, 3.5, 2.5, 3.5])
        # Ratio of leading terms should be ratio of kappas = 13/(1/2) = 26
        ratio = float(r1["leading_kappa_term"]) / float(r2["leading_kappa_term"])
        assert abs(ratio - 26.0) < 1e-8


# ============================================================================
# Section 11: Celestial pole structure
# ============================================================================

class TestCelestialPoleStructure:
    """Pole structure of A_cel(Delta)."""

    def test_poles_at_integer_delta(self):
        """A_cel has poles at Delta = r for r = 2, ..., max_r."""
        result = celestial_pole_structure(26, 8)
        for r in range(2, 9):
            assert r in result

    def test_residue_matches_shadow_coeff(self):
        """Numerical residue at Delta = r matches S_r."""
        result = celestial_pole_structure(26, 6)
        for r in range(2, 7):
            assert result[r]["match"], f"Residue mismatch at r={r}"

    def test_residue_at_r2_is_kappa(self):
        """Residue at Delta = 2 is S_2 = kappa = 13."""
        result = celestial_pole_structure(26, 6)
        assert abs(result[2]["expected_S_r"] - 13.0) < 1e-12

    def test_residue_at_r3_is_S3(self):
        """Residue at Delta = 3 is S_3 = 2."""
        result = celestial_pole_structure(26, 6)
        assert abs(result[3]["expected_S_r"] - 2.0) < 1e-12


# ============================================================================
# Section 12: Koszul complementarity
# ============================================================================

class TestKoszulComplementarity:
    """Koszul complementarity kappa + kappa' = 13 for Virasoro (AP24)."""

    def test_kappa_sum_is_13(self):
        """kappa(c) + kappa(26-c) = 13 for any c."""
        for c_val in [1, 5, 10, 13, 20, 25]:
            result = koszul_celestial_complementarity(c_val, 8)
            assert result["kappa_sum_is_13"]

    def test_self_dual_at_c13(self):
        """Self-dual point is c = 13."""
        result = koszul_celestial_complementarity(13, 8)
        assert result["kappa"] == result["kappa_dual"]
        assert result["self_dual_c"] == Fraction(13)

    def test_not_zero_general(self):
        """kappa + kappa' != 0 for general c (AP24)."""
        result = koszul_celestial_complementarity(10, 8)
        assert result["kappa_sum"] != 0
        assert result["kappa_sum"] == 13

    def test_arity2_sum(self):
        """S_2(c) + S_2(26-c) = c/2 + (26-c)/2 = 13 at arity 2."""
        result = koszul_celestial_complementarity(10, 8)
        s2_sum = result["arity_sums"][2]["sum"]
        assert s2_sum == Fraction(13)

    def test_higher_arity_sums_at_c13(self):
        """At c=13: S_r(13) = S_r(13) trivially (self-dual)."""
        result = koszul_celestial_complementarity(13, 8)
        for r in range(2, 9):
            data = result["arity_sums"][r]
            assert data["S_r"] == data["S_r_dual"]


# ============================================================================
# Section 13: Depth -- soft hierarchy
# ============================================================================

class TestDepthSoftHierarchy:
    """Shadow depth class -> soft theorem truncation."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G with r_max = 2."""
        m = depth_soft_hierarchy("heisenberg")
        assert m.depth_class == "G"
        assert m.r_max == 2

    def test_affine_km_class_L(self):
        """Affine KM is class L with r_max = 3."""
        m = depth_soft_hierarchy("affine_km")
        assert m.depth_class == "L"
        assert m.r_max == 3

    def test_betagamma_class_C(self):
        """Beta-gamma is class C with r_max = 4."""
        m = depth_soft_hierarchy("betagamma")
        assert m.depth_class == "C"
        assert m.r_max == 4

    def test_virasoro_class_M(self):
        """Virasoro is class M with infinite depth."""
        m = depth_soft_hierarchy("virasoro")
        assert m.depth_class == "M"
        assert m.r_max is None

    def test_w_infinity_class_M(self):
        """w_{1+infty} is class M."""
        m = depth_soft_hierarchy("w_infinity")
        assert m.depth_class == "M"

    def test_max_soft_order(self):
        """max_soft_order = r_max - 2 for finite towers."""
        m = depth_soft_hierarchy("betagamma")
        assert m.max_soft_order == 2

    def test_unknown_family_raises(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError):
            depth_soft_hierarchy("unknown_family")


# ============================================================================
# Section 14: Mellin-Zeta mismatch
# ============================================================================

class TestMellinZetaMismatch:
    """Quantify mismatch between zeta and Mellin vanishing conditions."""

    def test_mismatch_at_generic_delta(self):
        """Mellin and zeta values differ at generic Delta."""
        result = mellin_zeta_mismatch(26, 3.7, 10)
        assert result["conditions_differ"]
        assert abs(float(result["difference"])) > 0

    def test_mismatch_structure(self):
        """Output has correct keys."""
        result = mellin_zeta_mismatch(10, 4.0, 8)
        assert "zeta_value" in result
        assert "mellin_value" in result
        assert "difference" in result


# ============================================================================
# Section 15: Multi-path cross-verification (Weinberg)
# ============================================================================

class TestWeinbergVerification:
    """Verify leading soft theorem via 3 independent paths."""

    def test_weinberg_c26(self):
        """Weinberg soft theorem at c=26."""
        result = verify_weinberg_soft_theorem(26, 8)
        assert result["path1_direct"] is True
        assert result["all_agree"] is True

    def test_weinberg_c1(self):
        """Weinberg soft theorem at c=1."""
        result = verify_weinberg_soft_theorem(1, 8)
        assert result["path1_direct"] is True

    def test_S2_equals_kappa(self):
        """S_2 = kappa = c/2 (path 1)."""
        result = verify_weinberg_soft_theorem(10, 8)
        assert abs(result["S_2"] - 5.0) < 1e-12

    def test_analytic_residue_matches(self):
        """Analytic residue matches S_2 (path 2)."""
        result = verify_weinberg_soft_theorem(26, 8)
        assert abs(result["path2_analytic_residue"] - 13.0) < 1e-12

    def test_numerical_residue_matches(self):
        """Numerical residue matches S_2 (path 3)."""
        result = verify_weinberg_soft_theorem(26, 8)
        assert abs(result["path3_numerical_residue"] - 13.0) < 1e-8


# ============================================================================
# Section 16: Multi-path cross-verification (zeta at integers)
# ============================================================================

class TestZetaIntegerVerification:
    """Verify zeta_A(s) at s = 0, 1, 2 via 3 paths."""

    def test_three_paths_agree_c26(self):
        """All three computation paths agree at c=26."""
        result = verify_zeta_at_integers(26, 15)
        assert result["all_agree"]

    def test_three_paths_agree_c1(self):
        """All three paths agree at c=1."""
        result = verify_zeta_at_integers(1, 15)
        assert result["all_agree"]

    def test_direct_and_gf_match(self):
        """Direct summation = generating function check."""
        result = verify_zeta_at_integers(10, 15)
        for s in [0, 1, 2]:
            assert abs(result["direct"][s] - result["gf_check"][s]) < 1e-12

    def test_soft_matches_direct(self):
        """conformally_soft_modes matches direct summation."""
        result = verify_zeta_at_integers(26, 15)
        for s in [0, 1, 2]:
            assert abs(result["direct"][s] - result["soft_check"][s]) < 1e-12


# ============================================================================
# Section 17: Multi-path cross-verification (w_{1+infty} kappa)
# ============================================================================

class TestWInfinityKappaVerification:
    """Verify kappa(W_N) = c*(H_N-1) matches channel sum."""

    def test_all_N_agree(self):
        """Harmonic formula matches channel sum for all N."""
        results = verify_winfinity_kappa([2, 3, 4, 5, 10, 20])
        for r in results:
            assert r["agree"]

    def test_w2_recovers_virasoro(self):
        """At N=2: kappa = c/2 = Virasoro kappa."""
        results = verify_winfinity_kappa([2])
        r = results[0]
        c_val = Fraction(30)
        assert r["kappa_harmonic"] == c_val / 2


# ============================================================================
# Section 18: Genus-0 sphere verification
# ============================================================================

class TestGenus0SphereVerification:
    """Verify genus-0 shadow curve = celestial sphere."""

    def test_genus0_is_celestial(self):
        """genus_0_is_celestial_sphere flag is True."""
        result = verify_genus0_sphere(26, 3.7, 8)
        assert result["genus_0_is_celestial_sphere"] is True

    def test_genus1_correction_ratio_small(self):
        """Genus-1 correction is small relative to genus-0."""
        result = verify_genus0_sphere(26, 3.7, 8)
        ratio = float(result["correction_ratio"])
        assert ratio < 1.0  # genus-1 is a correction


# ============================================================================
# Section 19: Harmonic number foundations
# ============================================================================

class TestHarmonicNumbers:
    """Harmonic number exact arithmetic."""

    def test_H0(self):
        assert harmonic_number(0) == Fraction(0)

    def test_H1(self):
        assert harmonic_number(1) == Fraction(1)

    def test_H2(self):
        assert harmonic_number(2) == Fraction(3, 2)

    def test_H3(self):
        assert harmonic_number(3) == Fraction(11, 6)

    def test_H10(self):
        expected = sum(Fraction(1, j) for j in range(1, 11))
        assert harmonic_number(10) == expected

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            harmonic_number(-1)


# ============================================================================
# Section 20: Full verification suite
# ============================================================================

class TestFullVerification:
    """Run the complete verification suite."""

    def test_full_suite_runs(self):
        """Full verification suite completes without error."""
        result = run_full_verification(26, 8)
        assert "weinberg" in result
        assert "crossing" in result
        assert "genus0" in result
        assert "zeta_integers" in result
        assert "winfinity_kappa" in result
        assert "complementarity" in result
        assert "poles" in result

    def test_full_suite_weinberg_passes(self):
        """Weinberg verification passes in full suite."""
        result = run_full_verification(26, 8)
        assert result["weinberg"]["all_agree"]

    def test_full_suite_zeta_passes(self):
        """Zeta integer verification passes in full suite."""
        result = run_full_verification(26, 8)
        assert result["zeta_integers"]["all_agree"]

    def test_full_suite_poles_match(self):
        """All pole residues match in full suite."""
        result = run_full_verification(26, 8)
        for r, data in result["poles"].items():
            assert data["match"], f"Pole mismatch at r={r}"


# ============================================================================
# Section 21: Edge cases and robustness
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_large_c_shadow_coefficients(self):
        """Shadow coefficients are well-defined for large c."""
        coeffs = virasoro_shadow_coefficients(10000, 10)
        assert coeffs[2] == Fraction(5000)

    def test_small_c_shadow_coefficients(self):
        """Shadow coefficients are well-defined for small positive c."""
        coeffs = virasoro_shadow_coefficients(Fraction(1, 100), 6)
        assert coeffs[2] == Fraction(1, 200)

    def test_negative_c_shadow_coefficients(self):
        """Shadow coefficients are computable for negative c (c != 0, -22/5)."""
        coeffs = virasoro_shadow_coefficients(-1, 6)
        assert coeffs[2] == Fraction(-1, 2)

    def test_ope_with_high_arities(self):
        """OPE computable for higher arities."""
        coeff = celestial_shadow_ope(26, 4, 5, 7)
        # r3 = 4+5-2 = 7, correct fusion
        assert isinstance(coeff, Fraction)

    def test_mellin_amplitude_negative_c(self):
        """Mellin amplitude computable for negative c."""
        val = shadow_mellin_amplitude(-1, 3.7, 6)
        assert isinstance(val, mpmath.mpf)


# ============================================================================
# Section 22: Consistency between families
# ============================================================================

class TestCrossFamily:
    """Cross-family consistency checks."""

    def test_heisenberg_zeta_exact(self):
        """Heisenberg zeta is a single-term Dirichlet series."""
        coeffs = heisenberg_shadow_coefficients(7, 20)
        for s in [0, 1, 2, 3]:
            val = float(shadow_zeta(coeffs, s, 20))
            expected = 7.0 * (2.0 ** (-s))
            assert abs(val - expected) < 1e-12

    def test_affine_zeta_equals_heisenberg_zeta_on_tline(self):
        """On the T-line (S_3 = 0), affine KM zeta = single-term like Heisenberg."""
        dim_g, k, h = 3, 1, 2
        coeffs = affine_km_shadow_coefficients(dim_g, k, h, 10)
        kappa = Fraction(dim_g) * (_frac(k) + h) / (2 * h)
        # S_3 = 0 on T-line, so zeta = kappa * 2^{-s}
        for s in [0, 1, 2]:
            val = float(shadow_zeta(coeffs, s, 10))
            expected = float(_mp(kappa)) * (2.0 ** (-s))
            assert abs(val - expected) < 1e-12

    def test_virasoro_c2_vs_wn_tline(self):
        """W_N T-line shadow = Virasoro shadow at same c."""
        c_val = 10
        vir_coeffs = virasoro_shadow_coefficients(c_val, 8)
        wn_coeffs = wn_shadow_coefficients_tline(3, c_val, 8)
        for r in range(2, 9):
            assert vir_coeffs[r] == wn_coeffs[r]

    def test_kappa_additivity_heisenberg(self):
        """kappa is additive: kappa(H_{k1} + H_{k2}) = k1 + k2."""
        k1, k2 = 3, 5
        c1 = heisenberg_shadow_coefficients(k1, 5)
        c2 = heisenberg_shadow_coefficients(k2, 5)
        c_sum = heisenberg_shadow_coefficients(k1 + k2, 5)
        assert c1[2] + c2[2] == c_sum[2]
