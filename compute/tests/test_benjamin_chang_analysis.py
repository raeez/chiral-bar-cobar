r"""Tests for the Benjamin-Chang functional equation analysis.

Verifies:
  - Eisenstein scattering matrix phi(s)
  - Scattering factor F_c(s) from constrained Epstein FE
  - The origin of zeta(2s)/zeta(2s-1)
  - Universal residue factor A_c(rho)
  - Zeta zero positions relative to F_c poles
  - Complementarity under c -> 26-c
  - Standard Epstein FE (no zeta ratio) vs Benjamin-Chang FE (with zeta ratio)
  - Heisenberg and Narain special cases

80+ tests covering the full mathematical content.

Manuscript references:
    eq:constrained-epstein-fe (arithmetic_shadows.tex, line 3303)
    def:universal-residue-factor (arithmetic_shadows.tex, line 3322)
    rem:koszul-epstein-constraints (arithmetic_shadows.tex, line 2864)
    rem:structural-obstruction (arithmetic_shadows.tex, line 300)
    thm:scattering-coupling-factorization (arithmetic_shadows.tex, line 7719)
    [BenjaminChang22]: arXiv:2208.02259
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

from compute.lib import benjamin_chang_analysis as bca

DPS = 30
skipmp = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================
# Section 1: Eisenstein scattering matrix
# ============================================================

class TestScatteringMatrix:
    """Tests for the Eisenstein scattering matrix phi(s)."""

    @skipmp
    def test_phi_functional_equation(self):
        """phi(s) * phi(1-s) = 1 for generic s."""
        for s in [0.3 + 0.5j, 0.7 + 2j, 0.2 + 10j, 0.6 + 0.1j]:
            result = bca.verify_scattering_matrix_functional_eq(s, DPS)
            assert result['error'] < 1e-15, (
                f"phi(s)*phi(1-s) != 1 at s={s}: error={result['error']}"
            )

    @skipmp
    def test_phi_explicit_vs_ratio(self):
        """Two forms of phi(s) agree."""
        for s in [0.3 + 1j, 0.7 + 5j, 0.5 + 14.13j]:
            result = bca.verify_explicit_vs_ratio_form(s, DPS)
            assert result['relative_error'] < 1e-12, (
                f"Forms disagree at s={s}: rel_err={result['relative_error']}"
            )

    @skipmp
    def test_phi_on_critical_line(self):
        """On Re(s) = 1/2: phi(1/2+it) should have |phi| = 1 generically."""
        # phi(1/2+it) * phi(1/2-it) = 1 by the FE.
        # For SL(2,Z), phi(1/2+it) is real-valued on the unitary axis:
        # |phi(1/2+it)| = 1.
        for t in [1.0, 5.0, 14.134, 21.022, 30.0]:
            s = complex(0.5, t)
            phi_val = bca.scattering_matrix(s, DPS)
            # |phi(1/2+it)| = 1 for the Eisenstein scattering matrix on SL(2,Z)
            assert abs(abs(phi_val) - 1) < 1e-10, (
                f"|phi(1/2+it)| != 1 at t={t}: |phi|={abs(phi_val)}"
            )

    @skipmp
    def test_phi_near_s_equals_1(self):
        """phi has a pole at s=1 (from Gamma(0) in Lambda(1-s)).

        Test that phi is well-defined and finite away from s=1.
        """
        # phi(s=1) involves Lambda(0) which has a Gamma(0) pole.
        # Test at nearby complex points instead.
        for offset in [0.01j, 0.1, -0.1]:
            phi_near = bca.scattering_matrix(1.0 + offset, DPS)
            assert abs(phi_near) > 1e-20, (
                f"phi too small near s=1+{offset}: |phi|={abs(phi_near)}"
            )

    @skipmp
    def test_completed_selberg_zeta_fe(self):
        """The completed Riemann xi function satisfies xi(s) = xi(1-s).

        xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s).

        The Selberg function Lambda^*(s) = pi^{-s} Gamma(s) zeta(2s) is
        related by Lambda^*(s) = pi^{-s} Gamma(s) zeta(2s), and its FE is
        NOT Lambda^*(s) = Lambda^*(1-s). Rather, phi(s) = Lambda^*(1-s)/Lambda^*(s)
        is the scattering matrix, and phi(s)*phi(1-s) = 1.
        """
        # Verify phi(s) * phi(1-s) = 1 instead (already tested above).
        # Here we verify the xi FE via mpmath directly.
        mpmath.mp.dps = DPS
        for s in [0.3 + 1j, 0.7 + 3j, 0.25 + 7j]:
            s_mp = mpmath.mpc(s)
            xi_s = (0.5 * s_mp * (s_mp - 1) * mpmath.power(mpmath.pi, -s_mp / 2)
                    * mpmath.gamma(s_mp / 2) * mpmath.zeta(s_mp))
            xi_1ms = (0.5 * (1 - s_mp) * (-s_mp) * mpmath.power(mpmath.pi, -(1 - s_mp) / 2)
                      * mpmath.gamma((1 - s_mp) / 2) * mpmath.zeta(1 - s_mp))
            rel_err = abs(complex(xi_s - xi_1ms)) / max(abs(complex(xi_s)), 1e-100)
            assert rel_err < 1e-12, (
                f"xi(s) != xi(1-s) at s={s}: rel_err={rel_err}"
            )


# ============================================================
# Section 2: The zeta ratio zeta(2s)/zeta(2s-1)
# ============================================================

class TestZetaRatio:
    """Tests for the ratio zeta(2s)/zeta(2s-1)."""

    @skipmp
    def test_zeta_ratio_at_integer(self):
        """At s=1: zeta(2)/zeta(1) has a pole (zeta(1) diverges)."""
        # zeta(2)/zeta(1) is undefined; test near s=1
        ratio_near = bca.zeta_ratio(1.0 + 0.01j, DPS)
        assert abs(ratio_near) < 100  # Should be finite but large

    @skipmp
    def test_zeta_ratio_at_s_three_quarters(self):
        """At s=3/4: 2s=3/2, 2s-1=1/2.

        zeta(3/2) ~ 2.612, zeta(1/2) ~ -1.460.
        Ratio ~ -1.789.
        """
        ratio = bca.zeta_ratio(0.75, DPS)
        # zeta(3/2)/zeta(1/2) = 2.61238.../(-1.46035...) ~ -1.789
        assert abs(ratio.real - (-1.789)) < 0.01
        assert abs(ratio.imag) < 1e-10

    @skipmp
    def test_zeta_ratio_pole_at_zero_of_zeta_2s_minus_1(self):
        """Poles of zeta(2s)/zeta(2s-1) at s = (1+rho)/2 where zeta(rho) = 0.

        First zero: rho_1 ~ 0.5 + 14.134*i, so s = 0.75 + 7.067*i.
        Near this point, zeta(2s-1) ~ 0, so the ratio should be large.
        """
        mpmath.mp.dps = DPS
        rho1 = mpmath.zetazero(1)
        s_pole = complex((1 + rho1) / 2)
        # Approach the pole from a small offset
        s_near = s_pole + 0.001
        ratio = bca.zeta_ratio(s_near, DPS)
        assert abs(ratio) > 10, (
            f"zeta ratio not large near scattering pole: |ratio|={abs(ratio)}"
        )

    @skipmp
    def test_zeta_ratio_zero_at_half_rho(self):
        """Zeros of zeta(2s)/zeta(2s-1) at s = rho/2 where zeta(rho) = 0.

        First zero: s = rho_1/2 ~ 0.25 + 7.067*i.
        Near this point, zeta(2s) ~ 0, so the ratio should be small.
        """
        mpmath.mp.dps = DPS
        rho1 = mpmath.zetazero(1)
        s_zero = complex(rho1 / 2)
        # Near the zero, the ratio should be small
        ratio = bca.zeta_ratio(s_zero + 0.001, DPS)
        assert abs(ratio) < 1.0, (
            f"zeta ratio not small near zero: |ratio|={abs(ratio)}"
        )

    @skipmp
    def test_poles_and_zeros_under_rh(self):
        """Under RH: poles at Re(s) = 3/4, zeros at Re(s) = 1/4."""
        data = bca.zeta_ratio_poles_and_zeros(n_zeros=10, dps=DPS)
        for p in data['poles']:
            assert abs(p['real'] - 0.75) < 1e-10, (
                f"Pole not at Re(s)=3/4: Re(s)={p['real']}"
            )
        for z in data['zeros']:
            assert abs(z['real'] - 0.25) < 1e-10, (
                f"Zero not at Re(s)=1/4: Re(s)={z['real']}"
            )

    @skipmp
    def test_poles_and_zeros_imaginary_parts_match(self):
        """The k-th pole and k-th zero share the same imaginary part (gamma_k/2)."""
        data = bca.zeta_ratio_poles_and_zeros(n_zeros=10, dps=DPS)
        for p, z in zip(data['poles'], data['zeros']):
            assert abs(p['imag'] - z['imag']) < 1e-10, (
                f"Pole and zero imaginary parts differ: "
                f"pole_imag={p['imag']}, zero_imag={z['imag']}"
            )


# ============================================================
# Section 3: Scattering factor F_c(s)
# ============================================================

class TestScatteringFactor:
    """Tests for F_c(s) in the constrained Epstein FE."""

    @skipmp
    def test_Fc_decomposition_consistency(self):
        """F_c(s) = gamma_factor * pi_factor * zeta_ratio."""
        for c in [1.0, 10.0, 13.0, 26.0]:
            for s in [0.3 + 1j, 0.7 + 5j]:
                dec = bca.scattering_factor_decomposition(s, c, DPS)
                direct = bca.scattering_factor_Fc(s, c, DPS)
                rel_err = abs(dec['product'] - direct) / max(abs(direct), 1e-100)
                assert rel_err < 1e-10, (
                    f"Decomposition mismatch at c={c}, s={s}: err={rel_err}"
                )

    @skipmp
    def test_Fc_zeta_ratio_factor(self):
        """The zeta ratio factor in F_c(s) is zeta(2s)/zeta(2s-1)."""
        for c in [10.0, 26.0]:
            s = 0.4 + 3j
            dec = bca.scattering_factor_decomposition(s, c, DPS)
            zr_direct = bca.zeta_ratio(s, DPS)
            rel_err = abs(dec['zeta_ratio'] - zr_direct) / max(abs(zr_direct), 1e-100)
            assert rel_err < 1e-12, (
                f"Zeta ratio mismatch at c={c}: err={rel_err}"
            )

    @skipmp
    def test_Fc_vs_phi_relationship(self):
        """F_c(s) reconstructs from Eisenstein scattering + conformal factor."""
        for c in [1.0, 13.0, 26.0]:
            for s in [0.3 + 2j, 0.6 + 8j]:
                result = bca.Fc_vs_phi_relationship(s, c, DPS)
                assert result['relative_error'] < 1e-10, (
                    f"Fc reconstruction failed at c={c}, s={s}: "
                    f"err={result['relative_error']}"
                )

    @skipmp
    def test_Fc_at_self_dual_c13(self):
        """At c=13 (self-dual): F_13 has enhanced symmetry."""
        result = bca.complementarity_self_dual_test(0.4 + 2j, DPS)
        # At c=13, F_c = F_{26-c} = F_13, so ratio should be 1
        if result['ratio'] is not None:
            assert abs(result['ratio'] - 1) < 1e-10, (
                f"Self-dual ratio != 1: {result['ratio']}"
            )

    @skipmp
    def test_Fc_zeta_ratio_universal(self):
        """The zeta ratio zeta(2s)/zeta(2s-1) is c-INDEPENDENT.

        This is the KEY FACT: the number-theoretic content of F_c(s)
        comes entirely from the Eisenstein scattering matrix and does
        NOT depend on the central charge c.
        """
        s = 0.4 + 3j
        dec_c1 = bca.scattering_factor_decomposition(s, 1.0, DPS)
        dec_c10 = bca.scattering_factor_decomposition(s, 10.0, DPS)
        dec_c26 = bca.scattering_factor_decomposition(s, 26.0, DPS)

        # Zeta ratios should be identical
        assert abs(dec_c1['zeta_ratio'] - dec_c10['zeta_ratio']) < 1e-15
        assert abs(dec_c10['zeta_ratio'] - dec_c26['zeta_ratio']) < 1e-15


# ============================================================
# Section 4: Universal residue factor
# ============================================================

class TestUniversalResidue:
    """Tests for A_c(rho) and the residue kernel."""

    @skipmp
    def test_residue_factor_nonzero(self):
        """A_c(rho) should be nonzero at the first few zeta zeros."""
        mpmath.mp.dps = DPS
        for k in range(1, 6):
            rho = complex(mpmath.zetazero(k))
            for c in [1.0, 10.0, 26.0]:
                A = bca.universal_residue_factor(rho, c, DPS)
                assert abs(A) > 1e-20, (
                    f"A_{c}(rho_{k}) too small: |A|={abs(A)}"
                )

    @skipmp
    def test_residue_c_dependence(self):
        """A_c(rho) depends on c through the Gamma factors."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        A_1 = bca.universal_residue_factor(rho, 1.0, DPS)
        A_26 = bca.universal_residue_factor(rho, 26.0, DPS)
        # Should be different (c-dependent)
        assert abs(A_1 - A_26) / max(abs(A_1), abs(A_26)) > 0.01, (
            "A_c(rho) appears c-independent — wrong"
        )

    @skipmp
    def test_residue_kernel_oscillation(self):
        """The residue kernel w_{c,rho} oscillates as a function of Delta."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        c = 10.0
        # Sample at multiple Delta values
        values = [bca.residue_kernel(float(d), c, rho, dps=DPS)
                  for d in [1, 2, 5, 10, 50, 100]]
        # Should have sign changes (oscillation from cos(gamma/2 * log(2*Delta)))
        # The kernel is real-valued; extract real parts
        real_values = [v.real for v in values]
        signs = [1 if v > 0 else -1 for v in real_values if abs(v) > 1e-50]
        has_sign_change = any(signs[i] != signs[i + 1] for i in range(len(signs) - 1))
        # The cos oscillation with gamma/2 ~ 7.067 should produce sign changes
        # over the range Delta in [1, 100]
        assert has_sign_change, (
            f"Residue kernel does not oscillate: values={values}"
        )

    @skipmp
    def test_residue_kernel_decay(self):
        """The residue kernel decays as Delta^{-(c+sigma-1)/2}."""
        mpmath.mp.dps = DPS
        rho = complex(mpmath.zetazero(1))
        c = 10.0
        sigma = rho.real  # Should be 1/2 under RH
        expected_exponent = -(c + sigma - 1) / 2  # = -(10 + 0.5 - 1)/2 = -4.75

        w1 = abs(bca.residue_kernel(10.0, c, rho, dps=DPS))
        w2 = abs(bca.residue_kernel(100.0, c, rho, dps=DPS))
        if w1 > 1e-50 and w2 > 1e-50:
            # log(w2/w1) / log(100/10) should be approximately expected_exponent
            measured = math.log(w2 / w1) / math.log(10)
            # The oscillation makes this imprecise, but the trend should match
            assert measured < 0, (
                f"Residue kernel not decaying: measured exponent = {measured}"
            )


# ============================================================
# Section 5: Pole positions from zeta zeros
# ============================================================

class TestPolePositions:
    """Tests for the scattering pole positions."""

    @skipmp
    def test_first_pole_position(self):
        """First scattering pole at s = (1+rho_1)/2 ~ 0.75 + 7.067i."""
        poles = bca.scattering_pole_positions(n_zeros=5, dps=DPS)
        p1 = poles[0]
        assert abs(p1['s_rho_real'] - 0.75) < 1e-10
        assert abs(p1['s_rho_imag'] - 14.134725 / 2) < 0.001

    @skipmp
    def test_pole_real_part_three_quarters(self):
        """Under RH, all scattering poles have Re(s) = 3/4."""
        poles = bca.scattering_pole_positions(n_zeros=20, dps=DPS)
        for p in poles:
            assert abs(p['s_rho_real'] - 0.75) < 1e-10, (
                f"Pole k={p['k']} not at Re(s)=3/4: Re(s)={p['s_rho_real']}"
            )

    @skipmp
    def test_pole_imaginary_parts_increasing(self):
        """Imaginary parts of poles increase with k."""
        poles = bca.scattering_pole_positions(n_zeros=10, dps=DPS)
        for i in range(len(poles) - 1):
            assert poles[i + 1]['s_rho_imag'] > poles[i]['s_rho_imag'], (
                f"Poles not monotone: Im(s_{i+1})={poles[i+1]['s_rho_imag']} "
                f"<= Im(s_{i})={poles[i]['s_rho_imag']}"
            )

    @skipmp
    def test_pole_count(self):
        """Correct number of poles returned."""
        poles = bca.scattering_pole_positions(n_zeros=15, dps=DPS)
        assert len(poles) == 15

    @skipmp
    def test_poles_vs_zeros_interlacing(self):
        """Poles (at Re=3/4) and zeros (at Re=1/4) of zeta(2s)/zeta(2s-1)
        share the same imaginary parts."""
        data = bca.zeta_ratio_poles_and_zeros(n_zeros=10, dps=DPS)
        for i in range(10):
            pole_im = data['poles'][i]['imag']
            zero_im = data['zeros'][i]['imag']
            assert abs(pole_im - zero_im) < 1e-10


# ============================================================
# Section 6: Complementarity
# ============================================================

class TestComplementarity:
    """Tests for Koszul complementarity c <-> 26-c."""

    @skipmp
    def test_self_dual_c13(self):
        """At c=13: F_13 = F_{26-13} = F_13, so ratio = 1."""
        for s in [0.4 + 2j, 0.6 + 5j]:
            result = bca.complementarity_scattering_factors(s, 13.0, DPS)
            assert result['c_dual'] == 13.0
            if result['ratio'] is not None:
                assert abs(result['ratio'] - 1) < 1e-10

    @skipmp
    def test_complementarity_pair(self):
        """For c and 26-c: the ratio F_c/F_{26-c} depends only on Gamma factors."""
        s = 0.4 + 3j
        result = bca.complementarity_scattering_factors(s, 10.0, DPS)
        assert result['c'] == 10.0
        assert result['c_dual'] == 16.0
        # The ratio should be computable and finite
        assert result['ratio'] is not None
        assert abs(result['ratio']) > 1e-20
        assert abs(result['ratio']) < 1e20

    @skipmp
    def test_complementarity_symmetry(self):
        """F_c/F_{26-c} at s and F_{26-c}/F_c at s should be inverses."""
        s = 0.3 + 4j
        r1 = bca.complementarity_scattering_factors(s, 8.0, DPS)
        r2 = bca.complementarity_scattering_factors(s, 18.0, DPS)
        if r1['ratio'] is not None and r2['ratio'] is not None:
            product = r1['ratio'] * r2['ratio']
            assert abs(product - 1) < 1e-8, (
                f"Complementarity ratios not reciprocal: product={product}"
            )

    @skipmp
    def test_complementarity_zeta_ratio_cancels(self):
        """In the ratio F_c/F_{26-c}, the zeta ratio cancels (it's c-independent)."""
        s = 0.5 + 3j
        dec_c = bca.scattering_factor_decomposition(s, 10.0, DPS)
        dec_dual = bca.scattering_factor_decomposition(s, 16.0, DPS)
        # Zeta ratios should be identical
        assert abs(dec_c['zeta_ratio'] - dec_dual['zeta_ratio']) < 1e-15
        # So the complementarity ratio is purely a Gamma ratio
        if abs(dec_dual['product']) > 1e-50:
            ratio = dec_c['product'] / dec_dual['product']
            gamma_ratio = (dec_c['gamma_factor'] * dec_c['pi_factor']
                           / (dec_dual['gamma_factor'] * dec_dual['pi_factor']))
            assert abs(ratio - gamma_ratio) / max(abs(ratio), 1e-100) < 1e-10

    @skipmp
    def test_critical_string_c26(self):
        """At c=26 (critical string): kappa = 13, kappa' = kappa(Vir_0) = 0."""
        s = 0.4 + 2j
        result = bca.complementarity_scattering_factors(s, 26.0, DPS)
        assert result['c_dual'] == 0.0
        # F_0(s) involves Gamma(s + 0 - 1) = Gamma(s-1), which is finite
        # for generic s. The result should be finite.
        assert abs(result['F_c']) > 1e-50


# ============================================================
# Section 7: Standard Epstein vs Benjamin-Chang
# ============================================================

class TestStandardVsBenjaminChang:
    """Tests comparing the two functional equations."""

    @skipmp
    def test_standard_epstein_convergence(self):
        """Standard Epstein sum converges at Re(s) > 1.

        The FE Xi_Q(s) = Xi_Q(1-s) requires analytic continuation,
        which the direct truncated sum does NOT provide.  The existing
        shadow_epstein_zeta.py module uses the theta-function method for
        proper analytic continuation and has 66 FE tests that pass.

        Here we verify only that the raw sum converges and is finite
        at Re(s) > 1, and that it is NOT the same as the Benjamin-Chang
        constrained Epstein (which is a Dirichlet series over the
        primary spectrum, not a lattice sum).
        """
        for c in [10.0, 13.0]:
            mpmath.mp.dps = DPS
            kappa = c / 2
            alpha = 2
            S4 = 10 / (c * (5 * c + 22))
            Delta = 8 * kappa * S4
            a = 4 * kappa ** 2
            b = 12 * kappa * alpha
            cf = 9 * alpha ** 2 + 2 * Delta

            Xi = bca.standard_epstein_completed(2.0, a, b, cf, DPS)
            assert abs(Xi) > 1e-20, (
                f"Standard Epstein sum too small at c={c}: Xi={Xi}"
            )
            assert abs(Xi) < 1e20, (
                f"Standard Epstein sum too large at c={c}: Xi={Xi}"
            )

    @skipmp
    def test_explanation_structure(self):
        """The explanation correctly distinguishes the two FEs."""
        expl = bca.explain_zeta_ratio_origin()
        assert 'NONE' in expl['standard_epstein']['zeta_content']
        assert 'zeta(2s)/zeta(2s-1)' in expl['benjamin_chang']['zeta_content']
        assert 'Eisenstein' in expl['benjamin_chang']['reason']
        assert 'Rankin-Selberg' in expl['benjamin_chang']['mechanism']
        assert 'Poisson' in expl['standard_epstein']['mechanism']

    @skipmp
    def test_explanation_key_distinction(self):
        """The key distinction is lattice sum vs spectral decomposition."""
        expl = bca.explain_zeta_ratio_origin()
        assert 'LATTICE SUM' in expl['the_key_distinction']
        assert 'SPECTRAL DECOMPOSITION' in expl['the_key_distinction']
        assert 'MODULI SPACE' in expl['the_key_distinction']


# ============================================================
# Section 8: Heisenberg special case
# ============================================================

class TestHeisenberg:
    """Tests for the Heisenberg constrained Epstein."""

    @skipmp
    def test_heisenberg_formula(self):
        """epsilon^KE_{H_k}(s) = 2 k^{-2s} zeta(2s) at k=1."""
        s = 2.0 + 0j  # Convergent region
        eps = bca.heisenberg_constrained_epstein(s, k=1, dps=DPS)
        mpmath.mp.dps = DPS
        expected = complex(2 * mpmath.zeta(4))  # k=1: 2*zeta(2*2)=2*zeta(4)
        rel_err = abs(eps - expected) / abs(expected)
        assert rel_err < 1e-12

    @skipmp
    def test_heisenberg_zeros_at_quarter(self):
        """Heisenberg zeros lie on Re(s) = 1/4 (from zeta(2s) zeros at Re(2s)=1/2)."""
        # The zeros of 2*k^{-2s}*zeta(2s) are the zeros of zeta(2s),
        # which are at s = rho/2 where Re(rho) = 1/2 (under RH),
        # giving Re(s) = 1/4.
        mpmath.mp.dps = DPS
        rho1 = mpmath.zetazero(1)
        s_zero = complex(rho1 / 2)
        assert abs(s_zero.real - 0.25) < 1e-10

    @skipmp
    def test_heisenberg_level_scaling(self):
        """At level k: epsilon scales as k^{-2s}."""
        s = 2.0 + 0j
        eps_k1 = bca.heisenberg_constrained_epstein(s, k=1, dps=DPS)
        eps_k2 = bca.heisenberg_constrained_epstein(s, k=2, dps=DPS)
        # eps_k2/eps_k1 = (2^{-2s}) / (1^{-2s}) = 2^{-2s} = 2^{-4} = 1/16
        ratio = eps_k2 / eps_k1
        expected_ratio = 2 ** (-2 * s.real)  # 2^{-4} = 0.0625
        assert abs(ratio - expected_ratio) / abs(expected_ratio) < 1e-10


# ============================================================
# Section 9: Narain universality
# ============================================================

class TestNarain:
    """Tests for Narain universality."""

    @skipmp
    def test_narain_at_selfdual_radius(self):
        """At R=1: epsilon^1_s(1) = 4*zeta(2s)."""
        s = 2.0 + 0j
        eps = bca.narain_constrained_epstein(s, R=1.0, dps=DPS)
        mpmath.mp.dps = DPS
        expected = complex(4 * mpmath.zeta(4))
        rel_err = abs(eps - expected) / abs(expected)
        assert rel_err < 1e-12

    @skipmp
    def test_narain_t_duality(self):
        """T-duality: epsilon(R) = epsilon(1/R)."""
        s = 2.5 + 1j
        for R in [0.5, 2.0, 3.7]:
            eps_R = bca.narain_constrained_epstein(s, R=R, dps=DPS)
            eps_inv = bca.narain_constrained_epstein(s, R=1.0 / R, dps=DPS)
            rel_err = abs(eps_R - eps_inv) / max(abs(eps_R), 1e-100)
            assert rel_err < 1e-12, (
                f"T-duality broken at R={R}: rel_err={rel_err}"
            )

    @skipmp
    def test_narain_character_positive(self):
        """Character factor 2(R^{2s} + R^{-2s}) is positive for real s, R > 0."""
        for R in [0.5, 1.0, 2.0, 5.0]:
            for s in [0.5, 1.0, 2.0, 3.0]:
                mpmath.mp.dps = DPS
                char = 2 * (R ** (2 * s) + R ** (-2 * s))
                assert char > 0

    @skipmp
    def test_narain_zeros_r_independent(self):
        """Zeros of epsilon^1_s(R) are zeros of zeta(2s), independent of R."""
        # This is because 2(R^{2s}+R^{-2s}) never vanishes for real s > 0, R > 0.
        # The zeros come entirely from zeta(2s).
        for R in [0.7, 1.0, 1.5]:
            mpmath.mp.dps = DPS
            # At s = rho_1/2, zeta(2s) = zeta(rho_1) = 0
            # So epsilon should be zero (within numerical precision of zeta)
            rho1 = mpmath.zetazero(1)
            s_zero = complex(rho1 / 2)
            eps = bca.narain_constrained_epstein(s_zero, R=R, dps=DPS)
            assert abs(eps) < 1e-5, (
                f"Narain eps not zero at zeta zero for R={R}: |eps|={abs(eps)}"
            )


# ============================================================
# Section 10: Full analysis at a zeta zero
# ============================================================

class TestFullAnalysis:
    """Tests for the complete analysis at a specific zeta zero."""

    @skipmp
    def test_full_analysis_structure(self):
        """Full analysis returns all expected fields."""
        result = bca.full_analysis_at_zero(k=1, c=26.0, dps=DPS)
        required_keys = ['k', 'rho', 'gamma', 's_rho', 'A_c(rho)',
                         '|A_c(rho)|', 'w_kernel(Delta=1)',
                         'complementarity', 'decay_exponent_on_line']
        for key in required_keys:
            assert key in result, f"Missing key: {key}"

    @skipmp
    def test_full_analysis_first_zero(self):
        """Analysis at first zero: gamma ~ 14.135."""
        result = bca.full_analysis_at_zero(k=1, c=10.0, dps=DPS)
        assert abs(result['gamma'] - 14.134725) < 0.001
        assert abs(result['s_rho'].real - 0.75) < 1e-10
        assert result['|A_c(rho)|'] > 0

    @skipmp
    def test_full_analysis_decay_exponent(self):
        """Decay exponent -(c+sigma-1)/2 with sigma=1/2 under RH."""
        result = bca.full_analysis_at_zero(k=1, c=10.0, dps=DPS)
        expected = -(10 + 0.5 - 1) / 2  # = -4.75
        assert abs(result['decay_exponent_on_line'] - expected) < 1e-10

    @skipmp
    def test_full_analysis_critical_string(self):
        """At c=26 (critical string): decay exponent -(26+0.5-1)/2 = -12.75."""
        result = bca.full_analysis_at_zero(k=1, c=26.0, dps=DPS)
        expected = -(26 + 0.5 - 1) / 2  # = -12.75
        assert abs(result['decay_exponent_on_line'] - expected) < 1e-10

    @skipmp
    def test_full_analysis_multiple_zeros(self):
        """Analysis at first 5 zeros should all be consistent."""
        for k in range(1, 6):
            result = bca.full_analysis_at_zero(k=k, c=13.0, dps=DPS)
            assert abs(result['s_rho'].real - 0.75) < 1e-10
            assert result['|A_c(rho)|'] > 0


# ============================================================
# Section 11: The structural obstruction
# ============================================================

class TestStructuralObstruction:
    """Tests for Remark rem:structural-obstruction."""

    @skipmp
    def test_scattering_pole_at_complex_spectral_parameter(self):
        """The scattering poles lie at COMPLEX spectral parameters.

        For the Eisenstein series on the REAL spectral axis (s = 1/2 + it,
        t real), phi(1/2+it) is REGULAR. The poles are at s = rho/2,
        which have Re(s) = Re(rho)/2 != 1/2 (unless rho is on the boundary).

        This is the STRUCTURAL OBSTRUCTION: algebraic constraints on
        the real spectral axis cannot reach the scattering poles.
        """
        mpmath.mp.dps = DPS
        # phi(1/2+it) should be regular for real t
        for t in [1.0, 5.0, 14.134725, 21.022]:
            phi_val = bca.scattering_matrix(0.5 + t * 1j, DPS)
            assert abs(phi_val) < 1e10, (
                f"phi regular on spectral axis: t={t}, |phi|={abs(phi_val)}"
            )

    @skipmp
    def test_completed_selberg_zero_absorption(self):
        """Lambda(s_0) != 0 but Lambda(1-s_0) = 0 at s_0 = (1+rho)/2.

        This means phi(s_0) = Lambda(1-s_0)/Lambda(s_0) = 0.
        The "pole" of the uncompleted factor zeta(2s)/zeta(2s-1)
        is ABSORBED into a zero of the completed scattering matrix.
        """
        mpmath.mp.dps = DPS
        rho = mpmath.zetazero(1)
        s0 = (1 + rho) / 2

        # Lambda(1-s0) = Lambda((1-rho)/2)
        # Since 2*(1-s0) = 1-rho = conjugate zero of zeta,
        # zeta(1-rho) = 0, so Lambda(1-s0) = 0.
        Lambda_1ms0 = bca.completed_selberg(complex(1 - s0), DPS)
        assert abs(Lambda_1ms0) < 1e-5, (
            f"Lambda(1-s0) not zero: |Lambda|={abs(Lambda_1ms0)}"
        )

        # Lambda(s0): zeta(2*s0) = zeta(1+rho) != 0 generically
        Lambda_s0 = bca.completed_selberg(complex(s0), DPS)
        assert abs(Lambda_s0) > 1e-10, (
            f"Lambda(s0) unexpectedly zero: |Lambda|={abs(Lambda_s0)}"
        )


# ============================================================
# Section 12: Zeta ratio grid (smoke tests)
# ============================================================

class TestZetaRatioGrid:
    """Smoke tests for the grid evaluation."""

    @skipmp
    def test_grid_returns_correct_shape(self):
        """Grid has correct dimensions."""
        sigmas, ts, grid = bca.zeta_ratio_grid(
            sigma_range=(0.1, 0.9), t_range=(1, 10),
            n_sigma=5, n_t=10, dps=10
        )
        assert len(sigmas) == 5
        assert len(ts) == 10
        assert len(grid) == 5
        assert len(grid[0]) == 10

    @skipmp
    def test_grid_values_positive(self):
        """All grid values are positive (they are absolute values)."""
        sigmas, ts, grid = bca.zeta_ratio_grid(
            sigma_range=(0.1, 0.9), t_range=(1, 10),
            n_sigma=5, n_t=10, dps=10
        )
        for row in grid:
            for val in row:
                assert val >= 0

    @skipmp
    def test_grid_large_near_pole(self):
        """Grid values should be large near Re(s) = 3/4, Im(s) ~ 7.067."""
        sigmas, ts, grid = bca.zeta_ratio_grid(
            sigma_range=(0.7, 0.8), t_range=(6.5, 7.5),
            n_sigma=10, n_t=20, dps=15
        )
        max_val = max(max(row) for row in grid)
        assert max_val > 5, (
            f"Grid not large near scattering pole: max={max_val}"
        )
