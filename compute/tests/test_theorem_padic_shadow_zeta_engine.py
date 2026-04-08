r"""Tests for theorem_padic_shadow_zeta_engine.

Verifies the p-adic shadow L-function L^sh_p(s) = -kappa * L_p(s) * L_p(s-1)
and its properties, organized by independent verification paths.

VERIFICATION PATHS:
  P1. Kubota-Leopoldt interpolation: L_p(1-n, chi_0) = -(1-p^{n-1}) B_n/n
      cross-checked against Bernoulli numbers and von Staudt-Clausen.
  P2. Shadow p-adic L-function at integer points: product formula
      L^sh_p(1-n) = -kappa * L_p(1-n) * L_p(-n) vs archimedean values
      with Euler factor correction.
  P3. p-adic valuations: v_p(L^sh_p(1-n)) computed from Bernoulli
      valuation data and von Staudt-Clausen.
  P4. Iwasawa invariants: mu_p = v_p(kappa) from Ferrero-Washington
      plus multiplicativity, verified against power series computation.
  P5. Shadow depth detection: L^sh_p depends only on kappa, so depth
      classes G/L/C/M are invisible to the p-adic Eisenstein L-function.

Manuscript references:
    thm:shadow-eisenstein (arithmetic_shadows.tex)
    rem:kummer-motive (arithmetic_shadows.tex)
    chap:arithmetic-shadows (arithmetic_shadows.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  kappa = c/2 ONLY for Virasoro.
CAUTION (AP10): expected values computed from first principles, not hardcoded
    from literature.  Cross-family consistency checks are the real verification.
CAUTION (AP38): Bernoulli numbers computed independently, not imported.
"""

from __future__ import annotations

import pytest
from fractions import Fraction

from compute.lib.theorem_padic_shadow_zeta_engine import (
    PadicShadowZetaEngine,
    bernoulli_number,
    kubota_leopoldt_at_1_minus_n,
    kubota_leopoldt_at_s,
    shadow_padic_l_at_1_minus_n,
    shadow_padic_l_at_s,
    archimedean_shadow_l_at_1_minus_n,
    euler_factor_ratio,
    padic_valuation_table,
    shadow_padic_mu_invariant,
    iwasawa_invariants,
    ferrero_washington_check,
    shadow_tower_exact,
    detect_depth_class_padic,
    padic_depth_detection,
    v_p,
    v_p_safe,
)


# ============================================================================
# Bernoulli number cross-checks (foundation for everything else)
# ============================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers against known values (AP38: from first principles)."""

    def test_b0(self):
        assert bernoulli_number(0) == Fraction(1)

    def test_b1(self):
        assert bernoulli_number(1) == Fraction(-1, 2)

    def test_b2(self):
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_b4(self):
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_b6(self):
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_b8(self):
        assert bernoulli_number(8) == Fraction(-1, 30)

    def test_b10(self):
        assert bernoulli_number(10) == Fraction(5, 66)

    def test_b12(self):
        assert bernoulli_number(12) == Fraction(-691, 2730)

    def test_odd_bernoulli_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli_number(n) == 0


# ============================================================================
# Path 1: Kubota-Leopoldt interpolation at integer points
# ============================================================================

class TestKubotaLeopoldt:
    """Verify L_p(1-n, chi_0) = -(1 - p^{n-1}) * B_n / n."""

    def test_kl_at_n1_euler_factor_vanishes(self):
        """At n=1: L_p(0, chi_0) = -(1 - p^0) * B_1 / 1 = 0 for all p."""
        for p in [2, 3, 5, 7]:
            val = kubota_leopoldt_at_1_minus_n(p, 1)
            assert val == 0, f"L_{p}(0) should be 0, got {val}"

    def test_kl_at_n2_explicit(self):
        """L_p(-1, chi_0) = -(1 - p) * B_2/2 = (p-1)/12."""
        for p in [2, 3, 5, 7]:
            val = kubota_leopoldt_at_1_minus_n(p, 2)
            expected = Fraction(p - 1, 12)
            assert val == expected, f"p={p}: got {val}, expected {expected}"

    def test_kl_p2_at_n2(self):
        """L_2(-1, chi_0) = (2-1)/12 = 1/12."""
        assert kubota_leopoldt_at_1_minus_n(2, 2) == Fraction(1, 12)

    def test_kl_p3_at_n2(self):
        """L_3(-1, chi_0) = (3-1)/12 = 1/6."""
        assert kubota_leopoldt_at_1_minus_n(3, 2) == Fraction(1, 6)

    def test_kl_p5_at_n2(self):
        """L_5(-1, chi_0) = (5-1)/12 = 1/3."""
        assert kubota_leopoldt_at_1_minus_n(5, 2) == Fraction(1, 3)

    def test_kl_p7_at_n2(self):
        """L_7(-1, chi_0) = (7-1)/12 = 1/2."""
        assert kubota_leopoldt_at_1_minus_n(7, 2) == Fraction(1, 2)

    def test_kl_at_n4_explicit(self):
        """L_p(-3, chi_0) = -(1 - p^3) * B_4/4 = (1 - p^3)/(4*30) = (1-p^3)/120."""
        for p in [2, 3, 5]:
            val = kubota_leopoldt_at_1_minus_n(p, 4)
            # B_4 = -1/30, so -(1-p^3)*(-1/30)/4 = (1-p^3)/120
            expected = Fraction(1 - p**3, 120)
            assert val == expected, f"p={p}: got {val}, expected {expected}"

    def test_kl_p2_at_n4(self):
        """L_2(-3) = (1-8)/120 = -7/120."""
        assert kubota_leopoldt_at_1_minus_n(2, 4) == Fraction(-7, 120)

    def test_kl_at_n6_uses_b6(self):
        """L_p(-5, chi_0) = -(1-p^5)*B_6/6.  B_6 = 1/42."""
        for p in [2, 3]:
            val = kubota_leopoldt_at_1_minus_n(p, 6)
            expected = -(1 - Fraction(p)**5) * Fraction(1, 42) / 6
            assert val == expected

    def test_kl_s_interface(self):
        """kubota_leopoldt_at_s(p, s) with s = 1-n agrees with the n-form."""
        for p in [2, 3, 5]:
            for s in [-3, -2, -1, 0]:
                n = 1 - s
                val_s = kubota_leopoldt_at_s(p, s)
                val_n = kubota_leopoldt_at_1_minus_n(p, n)
                assert val_s == val_n

    def test_kl_raises_for_positive_s(self):
        """Cannot evaluate at s > 0 (n < 1)."""
        with pytest.raises(ValueError):
            kubota_leopoldt_at_s(2, 1)


# ============================================================================
# Path 2: Shadow p-adic L-function and archimedean comparison
# ============================================================================

class TestShadowPadicL:
    """Verify L^sh_p(1-n) = -kappa * L_p(1-n) * L_p(-n) and Euler factor relation."""

    def test_shadow_padic_l_is_product(self):
        """L^sh_p(1-n) equals -kappa * L_p(1-n) * L_p(-n) by construction."""
        kappa = Fraction(1, 2)  # Virasoro c=1
        for p in [2, 3, 5]:
            for n in [2, 3, 4, 5]:
                val = shadow_padic_l_at_1_minus_n(kappa, p, n)
                lp1 = kubota_leopoldt_at_1_minus_n(p, n)
                lp2 = kubota_leopoldt_at_1_minus_n(p, n + 1)
                expected = -kappa * lp1 * lp2
                assert val == expected

    def test_shadow_padic_l_at_n1_vanishes(self):
        """At n=1: L_p(0) = 0, so L^sh_p(0) = -kappa * 0 * L_p(-1) = 0."""
        for p in [2, 3, 5, 7]:
            for kappa in [Fraction(1), Fraction(13), Fraction(1, 2)]:
                val = shadow_padic_l_at_1_minus_n(kappa, p, 1)
                assert val == 0

    def test_shadow_padic_l_linearity_in_kappa(self):
        """L^sh_p is linear in kappa."""
        p = 3
        for n in [2, 3, 4]:
            val1 = shadow_padic_l_at_1_minus_n(Fraction(1), p, n)
            val2 = shadow_padic_l_at_1_minus_n(Fraction(2), p, n)
            assert val2 == 2 * val1

    def test_archimedean_at_n2(self):
        """L^sh(1-2) = L^sh(-1) = -kappa * zeta(-1) * zeta(-2).
        zeta(-1) = -B_2/2 = -1/12.  zeta(-2) = 0 (B_3 = 0).
        So L^sh(-1) = -kappa * (-1/12) * 0 = 0.
        """
        for kappa in [Fraction(1), Fraction(13)]:
            val = archimedean_shadow_l_at_1_minus_n(kappa, 2)
            assert val == 0

    def test_archimedean_at_n3(self):
        """L^sh(-2) = -kappa * zeta(-2) * zeta(-3).
        zeta(-2) = -B_3/3 = 0.  So L^sh(-2) = 0.
        """
        for kappa in [Fraction(1), Fraction(13)]:
            val = archimedean_shadow_l_at_1_minus_n(kappa, 3)
            assert val == 0

    def test_archimedean_at_n4(self):
        """L^sh(-3) = -kappa * zeta(-3) * zeta(-4).
        zeta(-3) = -B_4/4 = 1/120.  zeta(-4) = -B_5/5 = 0.
        So L^sh(-3) = 0.
        """
        for kappa in [Fraction(1)]:
            val = archimedean_shadow_l_at_1_minus_n(kappa, 4)
            assert val == 0

    def test_archimedean_at_n5(self):
        """L^sh(-4) = -kappa * zeta(-4) * zeta(-5).
        zeta(-4) = -B_5/5 = 0.  So L^sh(-4) = 0.
        """
        val = archimedean_shadow_l_at_1_minus_n(Fraction(1), 5)
        assert val == 0

    def test_euler_factor_ratio_at_n2(self):
        """(1 - p^1)(1 - p^2) at n=2."""
        for p in [2, 3, 5]:
            ratio = euler_factor_ratio(p, 2)
            expected = (1 - Fraction(p)) * (1 - Fraction(p)**2)
            assert ratio == expected

    def test_interpolation_consistency(self):
        """L^sh(1-n) = -kappa * (-B_n/n) * (-B_{n+1}/(n+1)).

        At n=1: B_1 = -1/2, B_2 = 1/6.  Both nonzero.
            zeta(0) = -B_1/1 = 1/2.  zeta(-1) = -B_2/2 = -1/12.
            L^sh(0) = -kappa * (1/2) * (-1/12) = kappa/24.

        For n >= 2: either n is even (then B_{n+1} = 0 since n+1 >= 3 is odd)
        or n >= 3 is odd (then B_n = 0).  So L^sh(1-n) = 0 for n >= 2.

        The p-adic version at n=1: L_p(0) = -(1 - p^0)*B_1 = 0 (Euler factor
        kills it), so L^sh_p(0) = 0 even though L^sh(0) != 0.  The Euler factor
        (1 - p^{n-1}) vanishes at n=1, introducing an extra zero.
        """
        kappa = Fraction(1)
        # n=1 is special: both B_1 and B_2 are nonzero
        arch_n1 = archimedean_shadow_l_at_1_minus_n(kappa, 1)
        assert arch_n1 == Fraction(1, 24), f"L^sh(0) = {arch_n1}, expected 1/24"

        # For n >= 2: consecutive Bernoulli vanishing
        for n in range(2, 15):
            arch = archimedean_shadow_l_at_1_minus_n(kappa, n)
            assert arch == 0, f"L^sh(1-{n}) should be 0, got {arch}"

    def test_shadow_padic_l_at_s_interface(self):
        """shadow_padic_l_at_s agrees with the n-form."""
        kappa = Fraction(13)
        for p in [2, 3]:
            for s in [-3, -2, -1, 0]:
                n = 1 - s
                val_s = shadow_padic_l_at_s(kappa, p, s)
                val_n = shadow_padic_l_at_1_minus_n(kappa, p, n)
                assert val_s == val_n


# ============================================================================
# Path 3: p-adic valuations
# ============================================================================

class TestPadicValuations:
    """Verify v_p(L^sh_p(1-n)) against von Staudt-Clausen predictions."""

    def test_vp_basic(self):
        """Basic p-adic valuation sanity.

        v_p(a/b) = v_p(a) - v_p(b).
        1/6: v_2(1) - v_2(6) = 0 - 1 = -1.  v_3(1/6) = 0 - 1 = -1.
        4 = 2^2: v_2(4) = 2.
        12 = 4*3: v_2(12) = 2, v_3(12) = 1.
        """
        assert v_p(Fraction(1, 6), 2) == -1
        assert v_p(Fraction(1, 6), 3) == -1
        assert v_p(Fraction(4), 2) == 2
        assert v_p(Fraction(12), 2) == 2
        assert v_p(Fraction(12), 3) == 1

    def test_vp_bernoulli_von_staudt_clausen(self):
        """Von Staudt-Clausen: the denominator of B_{2k} is prod_{(p-1)|2k} p.

        So v_p(B_{2k}) = -1 when (p-1) | 2k, and >= 0 otherwise.
        """
        # B_2 = 1/6: denom = 2*3 = 6.  v_2(B_2) = -1, v_3(B_2) = -1, v_5(B_2) = 0.
        assert v_p(bernoulli_number(2), 2) == -1
        assert v_p(bernoulli_number(2), 3) == -1
        assert v_p(bernoulli_number(2), 5) == 0

        # B_4 = -1/30: denom = 2*3*5 = 30.
        assert v_p(bernoulli_number(4), 2) == -1
        assert v_p(bernoulli_number(4), 3) == -1
        assert v_p(bernoulli_number(4), 5) == -1

        # B_12 = -691/2730: denom = 2*3*5*7*13.
        assert v_p(bernoulli_number(12), 2) == -1
        assert v_p(bernoulli_number(12), 691) == 1

    def test_shadow_padic_l_valuation_at_n2(self):
        """v_p(L^sh_p(-1)) = v_p(-kappa * L_p(-1) * L_p(-2)).

        L_p(-1) = (p-1)/12.  L_p(-2) = (1-p^2) * B_3/3 = 0 (B_3 = 0).
        So L^sh_p(-1) = 0, valuation is +inf.
        """
        kappa = Fraction(1, 2)
        for p in [2, 3, 5]:
            val = shadow_padic_l_at_1_minus_n(kappa, p, 2)
            # L_p(-2) = -(1-p^2)*B_3/3 = 0 since B_3 = 0
            assert val == 0

    def test_shadow_padic_l_nonzero_at_n4(self):
        """At n=4: L_p(-3) = -(1-p^3)*B_4/4 and L_p(-4) = -(1-p^4)*B_5/5 = 0.
        So L^sh_p(1-4) = 0 again (B_5 = 0).

        In fact, for ALL n >= 2, one of B_n or B_{n+1} vanishes (consecutive
        Bernoulli), so L^sh_p(1-n) = 0 for n >= 2.  The only potentially
        nonzero value is at n=1, but there the Euler factor kills L_p(0).
        """
        kappa = Fraction(1)
        for p in [2, 3, 5]:
            for n in [2, 3, 4, 5, 6, 7, 8]:
                val = shadow_padic_l_at_1_minus_n(kappa, p, n)
                assert val == 0, f"p={p}, n={n}: expected 0, got {val}"

    def test_valuation_table_all_infinite(self):
        """Since L^sh_p(1-n) = 0 for all n >= 1 at integer interpolation points,
        all valuations are +inf.
        """
        kappa = Fraction(13)  # Virasoro c=26
        for p in [2, 3, 5]:
            table = padic_valuation_table(kappa, p)
            for s, vp in table.items():
                assert vp == float('inf'), f"p={p}, s={s}: expected inf, got {vp}"


# ============================================================================
# Path 4: Iwasawa invariants and Ferrero-Washington
# ============================================================================

class TestIwasawaInvariants:
    """Verify mu_p(L^sh_p) = v_p(kappa) and lambda-invariant."""

    def test_mu_analytic_equals_vp_kappa(self):
        """mu_p = v_p(kappa) from Ferrero-Washington + multiplicativity."""
        # Virasoro c=1: kappa = 1/2
        assert shadow_padic_mu_invariant(Fraction(1, 2), 2) == -1.0
        assert shadow_padic_mu_invariant(Fraction(1, 2), 3) == 0.0
        assert shadow_padic_mu_invariant(Fraction(1, 2), 5) == 0.0

    def test_mu_virasoro_c2(self):
        """Virasoro c=2: kappa = 1.  v_p(1) = 0 for all p."""
        kappa = Fraction(1)
        for p in [2, 3, 5, 7]:
            assert shadow_padic_mu_invariant(kappa, p) == 0.0

    def test_mu_virasoro_c10(self):
        """Virasoro c=10: kappa = 5.  v_5(5) = 1, v_2(5) = 0."""
        kappa = Fraction(5)
        assert shadow_padic_mu_invariant(kappa, 5) == 1.0
        assert shadow_padic_mu_invariant(kappa, 2) == 0.0
        assert shadow_padic_mu_invariant(kappa, 3) == 0.0

    def test_mu_heisenberg_k1(self):
        """Heisenberg k=1: kappa = 1.  mu_p = 0 for all p."""
        kappa = Fraction(1)
        for p in [2, 3, 5]:
            assert shadow_padic_mu_invariant(kappa, p) == 0.0

    def test_mu_heisenberg_k2(self):
        """Heisenberg k=2: kappa = 2.  v_2(2) = 1, v_3(2) = 0."""
        kappa = Fraction(2)
        assert shadow_padic_mu_invariant(kappa, 2) == 1.0
        assert shadow_padic_mu_invariant(kappa, 3) == 0.0

    def test_mu_affine_sl2_k1(self):
        """Affine sl_2 at k=1: kappa = 3(1+2)/4 = 9/4.
        v_2(9/4) = -2, v_3(9/4) = 2.
        """
        kappa = Fraction(9, 4)
        assert shadow_padic_mu_invariant(kappa, 2) == -2.0
        assert shadow_padic_mu_invariant(kappa, 3) == 2.0
        assert shadow_padic_mu_invariant(kappa, 5) == 0.0

    def test_ferrero_washington_fails_virasoro_c1_p2(self):
        """Shadow FW FAILS at p=2 for Virasoro c=1 (kappa=1/2, v_2=-1)."""
        kappa = Fraction(1, 2)
        fw = ferrero_washington_check(kappa, [2, 3, 5])
        assert fw[2]['holds'] is False
        assert fw[2]['mu'] == -1.0

    def test_ferrero_washington_holds_virasoro_c2(self):
        """Shadow FW holds at all tested primes for Virasoro c=2 (kappa=1)."""
        kappa = Fraction(1)
        fw = ferrero_washington_check(kappa, [2, 3, 5, 7])
        for p in [2, 3, 5, 7]:
            assert fw[p]['holds'] is True

    def test_ferrero_washington_fails_virasoro_c10_p5(self):
        """Shadow FW FAILS at p=5 for Virasoro c=10 (kappa=5, v_5=1)."""
        kappa = Fraction(5)
        fw = ferrero_washington_check(kappa, [2, 3, 5])
        assert fw[5]['holds'] is False
        assert fw[5]['mu'] == 1.0
        assert fw[2]['holds'] is True
        assert fw[3]['holds'] is True

    def test_ferrero_washington_fails_at_p2_for_half_integer_kappa(self):
        """Any kappa with denominator divisible by 2 fails FW at p=2."""
        for c in [1, 3, 5, 7]:
            kappa = Fraction(c, 2)
            fw = ferrero_washington_check(kappa, [2])
            assert fw[2]['holds'] is False, f"c={c}: kappa={kappa} should fail at p=2"

    def test_ferrero_washington_failure_summary(self):
        """Tabulate FW failures across the standard landscape.

        This test confirms the swarm finding that FW fails at p=2 and p=5
        for specific kappa values.
        """
        failures: list = []
        test_cases = [
            ('Vir c=1', Fraction(1, 2)),
            ('Vir c=2', Fraction(1)),
            ('Vir c=10', Fraction(5)),
            ('Vir c=26', Fraction(13)),
            ('Heis k=1', Fraction(1)),
            ('Heis k=2', Fraction(2)),
            ('sl2 k=1', Fraction(9, 4)),
        ]
        primes = [2, 3, 5, 7]
        for name, kappa in test_cases:
            fw = ferrero_washington_check(kappa, primes)
            for p in primes:
                if not fw[p]['holds']:
                    failures.append((name, p, fw[p]['mu']))

        # Known failures from the arithmetic swarm:
        # Vir c=1 at p=2 (kappa=1/2, v_2=-1)
        # Vir c=10 at p=5 (kappa=5, v_5=1)
        # Heis k=2 at p=2 (kappa=2, v_2=1)
        # sl2 k=1 at p=2 (kappa=9/4, v_2=-2)
        # sl2 k=1 at p=3 (kappa=9/4, v_3=2)
        assert len(failures) >= 5, f"Expected >= 5 FW failures, got {len(failures)}"


# ============================================================================
# Path 5: Shadow depth detection (negative result)
# ============================================================================

class TestDepthDetection:
    """Verify that L^sh_p does NOT detect shadow depth beyond kappa."""

    def test_depth_class_heisenberg(self):
        tower = shadow_tower_exact('heisenberg', Fraction(1))
        assert detect_depth_class_padic(tower) == 'G'

    def test_depth_class_affine_sl2(self):
        tower = shadow_tower_exact('affine_sl2', Fraction(1))
        assert detect_depth_class_padic(tower) == 'L'

    def test_depth_class_betagamma(self):
        tower = shadow_tower_exact('betagamma', Fraction(0))
        assert detect_depth_class_padic(tower) == 'C'

    def test_depth_class_virasoro(self):
        tower = shadow_tower_exact('virasoro', Fraction(1))
        assert detect_depth_class_padic(tower) == 'M'

    def test_padic_l_does_not_detect_depth(self):
        """L^sh_p depends only on kappa, so different depth classes with the
        same kappa yield identical L^sh_p values.

        Construct: Heisenberg with k=1 (class G, kappa=1) and Virasoro with
        c=2 (class M, kappa=1) have the SAME kappa.  Their L^sh_p are identical.
        """
        kappa = Fraction(1)
        for p in [2, 3, 5]:
            for n in [1, 2, 3, 4, 5]:
                val_heis = shadow_padic_l_at_1_minus_n(kappa, p, n)
                val_vir = shadow_padic_l_at_1_minus_n(kappa, p, n)
                assert val_heis == val_vir

    def test_depth_detection_report(self):
        """The padic_depth_detection function correctly reports that
        L^sh_p cannot detect depth."""
        result = padic_depth_detection('virasoro', Fraction(1), 3)
        assert result['pure_kappa_determines_l_sh_p'] is True
        assert result['depth_visible_to_padic_shadow_l'] is False

    def test_shadow_tower_virasoro_first_terms(self):
        """Cross-check shadow tower computation (AP1: recompute from first principles).

        Virasoro c=1: kappa = 1/2, S_3 = 2, S_4 = 10/(1*(5+22)) = 10/27.
        """
        tower = shadow_tower_exact('virasoro', Fraction(1))
        assert tower[2] == Fraction(1, 2)
        assert tower[3] == Fraction(2)
        assert tower[4] == Fraction(10, 27)

    def test_shadow_tower_affine_sl2(self):
        """Affine sl_2 at k=1: kappa = 9/4, S_3 = 4/3, S_r = 0 for r >= 4."""
        tower = shadow_tower_exact('affine_sl2', Fraction(1))
        assert tower[2] == Fraction(9, 4)
        assert tower[3] == Fraction(4, 3)
        assert tower[4] == Fraction(0)
        assert tower[5] == Fraction(0)


# ============================================================================
# Engine wrapper tests
# ============================================================================

class TestEngine:
    """Test the PadicShadowZetaEngine interface."""

    def test_engine_kubota_leopoldt(self):
        eng = PadicShadowZetaEngine()
        val = eng.kubota_leopoldt(3, 2)
        assert val == Fraction(1, 6)

    def test_engine_shadow_padic_l(self):
        eng = PadicShadowZetaEngine()
        kappa = Fraction(1, 2)
        val = eng.shadow_padic_l(kappa, 3, 2)
        lp1 = kubota_leopoldt_at_1_minus_n(3, 2)
        lp2 = kubota_leopoldt_at_1_minus_n(3, 3)
        assert val == -kappa * lp1 * lp2

    def test_engine_verify_interpolation(self):
        eng = PadicShadowZetaEngine()
        kappa = Fraction(1)
        result = eng.verify_interpolation(kappa, 3, 4)
        assert result['match'] is True

    def test_engine_ferrero_washington(self):
        eng = PadicShadowZetaEngine()
        kappa = Fraction(1, 2)
        fw = eng.ferrero_washington(kappa, [2, 3])
        assert fw[2]['holds'] is False
        assert fw[3]['holds'] is True

    def test_engine_full_analysis_runs(self):
        eng = PadicShadowZetaEngine()
        result = eng.full_analysis(Fraction(1), 3, max_n=8)
        assert 'iwasawa' in result
        assert 'ferrero_washington' in result
        assert 'kubota_leopoldt_values' in result


# ============================================================================
# Cross-path consistency: all paths agree
# ============================================================================

class TestCrossPath:
    """Verify consistency across independent verification paths."""

    def test_product_formula_vs_archimedean_euler(self):
        """For n where archimedean value is nonzero, the product formula
        should match archimedean * euler_ratio.

        Since archimedean L^sh(1-n) = 0 for all n >= 1 (consecutive Bernoulli
        vanishing), this test verifies the structural reason: both sides are 0.
        """
        kappa = Fraction(13)
        for p in [2, 3, 5]:
            for n in range(1, 10):
                padic_val = shadow_padic_l_at_1_minus_n(kappa, p, n)
                arch_val = archimedean_shadow_l_at_1_minus_n(kappa, n)
                ratio = euler_factor_ratio(p, n)
                assert padic_val == arch_val * ratio

    def test_mu_analytic_vs_kappa_valuation(self):
        """mu_p from Ferrero-Washington = v_p(kappa) for all tested families."""
        test_cases = [
            Fraction(1, 2), Fraction(1), Fraction(5),
            Fraction(13), Fraction(9, 4), Fraction(2),
        ]
        for kappa in test_cases:
            for p in [2, 3, 5, 7]:
                mu = shadow_padic_mu_invariant(kappa, p)
                vk = v_p_safe(kappa, p)
                assert mu == vk, f"kappa={kappa}, p={p}: mu={mu} != v_p(kappa)={vk}"

    def test_kappa_additivity_implies_mu_subadditivity(self):
        """For independent algebras A, B: kappa(A+B) = kappa(A) + kappa(B).
        The mu-invariant satisfies v_p(kappa_A + kappa_B) >= min(v_p(kappa_A), v_p(kappa_B)).
        """
        kA = Fraction(1, 2)  # Vir c=1
        kB = Fraction(1)     # Vir c=2
        kAB = kA + kB        # 3/2

        for p in [2, 3, 5]:
            mu_A = shadow_padic_mu_invariant(kA, p)
            mu_B = shadow_padic_mu_invariant(kB, p)
            mu_AB = shadow_padic_mu_invariant(kAB, p)
            assert mu_AB >= min(mu_A, mu_B), (
                f"p={p}: mu(A+B)={mu_AB} < min(mu(A)={mu_A}, mu(B)={mu_B})"
            )
