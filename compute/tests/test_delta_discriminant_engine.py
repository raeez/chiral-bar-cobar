r"""Tests for the delta discriminant engine: Delta = 8*kappa*S_4.

Verifies:
  1. Core formula Delta = 8*kappa*S_4 (linearity in both arguments)
  2. Class G families: Heisenberg, lattice, free fermion (Delta = 0)
  3. Class L families: affine KM at generic k (Delta = 0)
  4. Class M families: Virasoro at generic c, W_3 (Delta != 0)
  5. Class C: betagamma neutral line (Delta = 0; quartic on charged stratum)
  6. Virasoro closed-form Delta = 40/(5c+22)
  7. W_3 W-line closed-form Delta = 20480/[3(5c+22)^3]
  8. Virasoro discriminant complementarity: Delta(c)+Delta(26-c) = 6960/[(5c+22)(152-5c)]
  9. Self-dual point c=13
  10. Kappa formulas: family-specific, cross-checked with census
  11. S_4 formulas: family-specific
  12. Shadow class classification from (kappa, alpha, S_4)
  13. Delta linearity (NOT quadratic, AP21)
  14. c-cancellation in Virasoro Delta (kappa*S_4 regular at c=0)
  15. Full landscape atlas consistency

Ground truth:
  thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
  C1-C4, C30 (CLAUDE.md True Formula Census)
  discriminant_atlas.py (existing engine, independent implementation)

  # VERIFIED: Delta(Vir_c) = 40/(5c+22) by
  #   [DC] 8*(c/2)*10/[c(5c+22)] = 40/(5c+22)
  #   [LT] eq:discriminant-complementarity, Faber tables
  #   [CF] cross-check with discriminant_atlas.py
"""

import sys
sys.path.insert(0, 'compute')

import pytest
from fractions import Fraction

from lib.delta_discriminant_engine import (
    # Core
    delta_discriminant,
    # Kappa
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_km,
    kappa_w_n,
    kappa_betagamma,
    kappa_lattice,
    kappa_free_fermion,
    # S_4
    S4_heisenberg,
    S4_lattice,
    S4_free_fermion,
    S4_affine_km,
    S4_virasoro,
    S4_w3_T_line,
    S4_w3_W_line,
    S4_betagamma_neutral_line,
    # Delta per family
    delta_heisenberg,
    delta_lattice,
    delta_free_fermion,
    delta_affine_km,
    delta_virasoro,
    delta_w3_T_line,
    delta_w3_W_line,
    delta_betagamma_neutral,
    # Classification
    classify_from_delta,
    # Complementarity
    virasoro_discriminant_complementarity,
    # Landscape
    full_discriminant_landscape,
    # Checks
    verify_delta_linearity_in_kappa,
    verify_virasoro_c_cancellation,
)


# ====================================================================
# 1. Core formula: Delta = 8*kappa*S_4
# ====================================================================

class TestCoreFormula:
    """Delta = 8*kappa*S_4 basic properties."""

    def test_delta_basic(self):
        """Delta(1, 1) = 8."""
        assert delta_discriminant(Fraction(1), Fraction(1)) == Fraction(8)

    def test_delta_zero_kappa(self):
        """Delta = 0 when kappa = 0 (uncurved algebra)."""
        assert delta_discriminant(Fraction(0), Fraction(5)) == Fraction(0)

    def test_delta_zero_s4(self):
        """Delta = 0 when S_4 = 0 (class G or L)."""
        assert delta_discriminant(Fraction(7, 2), Fraction(0)) == Fraction(0)

    def test_delta_linearity_in_kappa(self):
        """Delta is LINEAR in kappa at fixed S_4 (C30, AP21: NOT quadratic)."""
        S4 = Fraction(10, 27)
        for n in range(1, 8):
            assert (delta_discriminant(Fraction(n), S4) ==
                    n * delta_discriminant(Fraction(1), S4))

    def test_delta_linearity_in_s4(self):
        """Delta is linear in S_4 at fixed kappa."""
        kappa = Fraction(5, 3)
        for n in range(1, 8):
            assert (delta_discriminant(kappa, Fraction(n)) ==
                    n * delta_discriminant(kappa, Fraction(1)))

    def test_delta_bilinear(self):
        """Delta(a*kappa, b*S4) = a*b*Delta(kappa, S4)."""
        kappa = Fraction(3, 7)
        S4 = Fraction(11, 5)
        base = delta_discriminant(kappa, S4)
        for a, b in [(2, 3), (5, 7), (1, 10)]:
            assert delta_discriminant(a * kappa, b * S4) == a * b * base


# ====================================================================
# 2. Kappa formulas: family-specific
# ====================================================================

class TestKappaFormulas:
    """Verify kappa formulas from True Formula Census C1-C4."""

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k. (C1)"""
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)
        assert kappa_heisenberg(Fraction(0)) == Fraction(0)
        assert kappa_heisenberg(Fraction(5, 2)) == Fraction(5, 2)

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2. (C2) Self-dual at c=13: kappa=13/2."""
        assert kappa_virasoro(Fraction(0)) == Fraction(0)
        assert kappa_virasoro(Fraction(13)) == Fraction(13, 2)
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_kappa_affine_km_sl2(self):
        """kappa(sl_2, k) = 3(k+2)/4. (C3) dim=3, h^v=2.
        # VERIFIED [LC] k=0 -> 3/2 (NOT zero); k=-2 -> 0 (critical)
        """
        assert kappa_affine_km(3, 2, Fraction(0)) == Fraction(3, 2)
        assert kappa_affine_km(3, 2, Fraction(1)) == Fraction(9, 4)
        assert kappa_affine_km(3, 2, Fraction(-2)) == Fraction(0)

    def test_kappa_affine_km_sl3(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3. dim=8, h^v=3."""
        assert kappa_affine_km(8, 3, Fraction(0)) == Fraction(4)
        assert kappa_affine_km(8, 3, Fraction(1)) == Fraction(16, 3)

    def test_kappa_w_n_w2_equals_virasoro(self):
        """kappa(W_2) = c*(H_2-1) = c/2 = kappa(Vir_c). W_2 = Vir.
        # VERIFIED [LC] H_2 = 3/2, H_2-1 = 1/2, so kappa = c/2
        (AP136: NOT c*H_1 = c*1 = c, which would be WRONG by factor 2.)
        """
        for c_val in [1, 6, 13]:
            c = Fraction(c_val)
            assert kappa_w_n(2, c) == kappa_virasoro(c)

    def test_kappa_w3(self):
        """kappa(W_3) = c*(H_3-1) = c*5/6 = 5c/6. (C4)
        # VERIFIED [DC] H_3 = 1 + 1/2 + 1/3 = 11/6, H_3-1 = 5/6
        """
        assert kappa_w_n(3, Fraction(6)) == Fraction(5)
        assert kappa_w_n(3, Fraction(12)) == Fraction(10)

    def test_kappa_betagamma_values(self):
        """kappa(bg, lam). (C6 complement)
        # VERIFIED [LC] lam=1/2 -> 6/4-3+1 = -1/2; lam=0 -> 1; lam=1 -> 1
        """
        assert kappa_betagamma(Fraction(0)) == Fraction(1)
        assert kappa_betagamma(Fraction(1, 2)) == Fraction(-1, 2)
        assert kappa_betagamma(Fraction(1)) == Fraction(1)
        assert kappa_betagamma(Fraction(2)) == Fraction(13)


# ====================================================================
# 3. Class G: Delta = 0 (Heisenberg, lattice, free fermion)
# ====================================================================

class TestClassG:
    """Class G families: Delta = 0, S_4 = 0, alpha = 0."""

    def test_heisenberg_delta_zero(self):
        """Delta(H_k) = 0 for all k."""
        for k_val in [0, 1, 2, 5, Fraction(1, 2)]:
            assert delta_heisenberg(Fraction(k_val)) == Fraction(0)

    def test_lattice_delta_zero(self):
        """Delta(lattice, rank r) = 0 for all ranks."""
        for r in [8, 16, 24, 32]:
            assert delta_lattice(r) == Fraction(0)

    def test_free_fermion_delta_zero(self):
        """Delta(free fermion) = 0."""
        assert delta_free_fermion() == Fraction(0)

    def test_heisenberg_s4_zero(self):
        """S_4(Heisenberg) = 0 (abelian: no quartic shadow)."""
        assert S4_heisenberg() == Fraction(0)

    def test_class_g_classification(self):
        """(kappa != 0, alpha = 0, S_4 = 0) -> class G."""
        assert classify_from_delta(Fraction(1), Fraction(0), Fraction(0)) == 'G'
        assert classify_from_delta(Fraction(5), Fraction(0), Fraction(0)) == 'G'


# ====================================================================
# 4. Class L: Delta = 0 (affine KM at generic k)
# ====================================================================

class TestClassL:
    """Class L families: Delta = 0, S_4 = 0, alpha != 0."""

    def test_affine_sl2_delta_zero(self):
        """Delta(sl_2, k) = 0 for all levels k."""
        for k_val in [1, 2, 5, 10, 100]:
            assert delta_affine_km(3, 2, Fraction(k_val)) == Fraction(0)

    def test_affine_sl3_delta_zero(self):
        """Delta(sl_3, k) = 0 for all levels k."""
        for k_val in [1, 2, 5]:
            assert delta_affine_km(8, 3, Fraction(k_val)) == Fraction(0)

    def test_affine_e8_delta_zero(self):
        """Delta(e_8, k) = 0. dim=248, h^v=30."""
        assert delta_affine_km(248, 30, Fraction(1)) == Fraction(0)

    def test_affine_km_s4_zero(self):
        """S_4(affine KM) = 0 (Jacobi identity kills quartic)."""
        assert S4_affine_km() == Fraction(0)

    def test_class_l_classification(self):
        """(kappa != 0, alpha != 0, S_4 = 0) -> class L."""
        assert classify_from_delta(Fraction(3, 2), Fraction(1), Fraction(0)) == 'L'

    def test_affine_km_critical_level_kappa_zero(self):
        """At critical level k = -h^v: kappa = 0.
        Delta = 0 trivially (kappa = 0), but Koszulness fails.
        """
        assert kappa_affine_km(3, 2, Fraction(-2)) == Fraction(0)
        assert delta_affine_km(3, 2, Fraction(-2)) == Fraction(0)


# ====================================================================
# 5. Class M: Delta != 0 (Virasoro, W_3)
# ====================================================================

class TestClassM:
    """Class M families: Delta != 0, infinite shadow tower."""

    def test_virasoro_delta_nonzero(self):
        """Delta(Vir_c) != 0 for generic c (c != pole)."""
        for c_val in [1, 2, 5, 13, 25, 26]:
            D = delta_virasoro(Fraction(c_val))
            assert D != Fraction(0), f"Delta vanishes at c={c_val}"
            assert D > 0, f"Delta negative at c={c_val}"

    def test_virasoro_delta_closed_form(self):
        """Delta(Vir_c) = 40/(5c+22).
        # VERIFIED [DC] 8*(c/2)*10/[c(5c+22)] = 40/(5c+22)
        # VERIFIED [CF] matches discriminant_atlas.py
        """
        test_cases = [
            (0, Fraction(40, 22)),
            (1, Fraction(40, 27)),
            (2, Fraction(40, 32)),
            (13, Fraction(40, 87)),
            (26, Fraction(40, 152)),
        ]
        for c_val, expected in test_cases:
            assert delta_virasoro(Fraction(c_val)) == expected, \
                f"Mismatch at c={c_val}"

    def test_virasoro_from_product(self):
        """Verify Delta = 8*kappa*S_4 matches closed form for Virasoro."""
        for c_val in [1, 2, 5, 13, 25, 26]:
            c = Fraction(c_val)
            from_product = delta_discriminant(kappa_virasoro(c), S4_virasoro(c))
            from_closed = delta_virasoro(c)
            assert from_product == from_closed, f"Product != closed at c={c_val}"

    def test_w3_t_line_equals_virasoro(self):
        """W_3 T-line Delta = Virasoro Delta (same subsector)."""
        for c_val in [2, 6, 13]:
            c = Fraction(c_val)
            assert delta_w3_T_line(c) == delta_virasoro(c)

    def test_w3_w_line_closed_form(self):
        """W_3 W-line: Delta = 20480/[3(5c+22)^3].
        At c=2: 20480/[3*32^3] = 20480/98304 = 5/24.
        """
        assert delta_w3_W_line(Fraction(2)) == Fraction(20480) / (3 * 32**3)
        # Simplify: 20480/98304 = 5/24
        assert delta_w3_W_line(Fraction(2)) == Fraction(5, 24)

    def test_w3_w_line_from_product(self):
        """Verify Delta_W = 8*kappa_W*S4_W matches closed form."""
        for c_val in [2, 6, 13]:
            c = Fraction(c_val)
            kappa_W = Fraction(c, 3)
            s4_W = S4_w3_W_line(c)
            from_product = delta_discriminant(kappa_W, s4_W)
            from_closed = delta_w3_W_line(c)
            assert from_product == from_closed, f"W-line mismatch at c={c_val}"

    def test_class_m_classification(self):
        """(kappa != 0, alpha != 0, S_4 != 0) -> class M."""
        assert classify_from_delta(
            Fraction(1, 2), Fraction(2), Fraction(10, 27)) == 'M'

    def test_w3_w_line_even_cascade(self):
        """W_3 W-line: alpha = 0, Delta != 0 -> even_cascade."""
        assert classify_from_delta(
            Fraction(2, 3), Fraction(0), S4_w3_W_line(Fraction(2))) == 'even_cascade'


# ====================================================================
# 6. Class C: betagamma (Delta = 0 on neutral line)
# ====================================================================

class TestClassC:
    """Class C: betagamma system. Delta = 0 on neutral primary line,
    but quartic contact nonzero on charged stratum.
    """

    def test_betagamma_delta_zero_neutral(self):
        """Delta = 0 on neutral line for all lambda."""
        for lam_val in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]:
            assert delta_betagamma_neutral(lam_val) == Fraction(0)

    def test_betagamma_s4_zero_neutral(self):
        """S_4 = 0 on neutral primary line."""
        assert S4_betagamma_neutral_line() == Fraction(0)

    def test_betagamma_kappa_nonzero_generic(self):
        """kappa(bg) != 0 at generic lambda (not at the zero locus)."""
        assert kappa_betagamma(Fraction(1)) == Fraction(1)
        assert kappa_betagamma(Fraction(0)) == Fraction(1)
        assert kappa_betagamma(Fraction(2)) == Fraction(13)


# ====================================================================
# 7. Virasoro discriminant complementarity
# ====================================================================

class TestVirasoroComplementarity:
    """Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)]."""

    def test_complementarity_at_several_c(self):
        """Verify universal-numerator complementarity.
        # VERIFIED [DC] algebraic identity
        # VERIFIED [LT] eq:discriminant-complementarity
        """
        for c_val in [1, 2, 3, 5, 7, 10, 13, 20, 25]:
            result = virasoro_discriminant_complementarity(Fraction(c_val))
            assert result['match'], f"Complementarity fails at c={c_val}"

    def test_self_dual_c13(self):
        """At c=13: Delta(13) = Delta(13) (self-dual). Both = 40/87."""
        result = virasoro_discriminant_complementarity(Fraction(13))
        assert result['Delta'] == result['Delta_dual']
        assert result['Delta'] == Fraction(40, 87)
        assert result['sum'] == Fraction(80, 87)

    def test_complementarity_at_c0(self):
        """At c=0: Delta(0)=20/11, Delta(26)=40/152=5/19.
        Sum = 435/209 = 6960/3344. Match.
        """
        result = virasoro_discriminant_complementarity(Fraction(0))
        assert result['Delta'] == Fraction(20, 11)
        assert result['Delta_dual'] == Fraction(5, 19)
        assert result['match']

    def test_universal_numerator(self):
        """The numerator of Delta(c)+Delta(26-c) is always 6960 = 40*174."""
        for c_val in [1, 5, 13]:
            c = Fraction(c_val)
            D = delta_virasoro(c)
            D_dual = delta_virasoro(Fraction(26) - c)
            total = D + D_dual
            # The denominator is (5c+22)(152-5c)
            denom = (5 * c + 22) * (152 - 5 * c)
            numer = total * denom
            assert numer == Fraction(6960)


# ====================================================================
# 8. Delta linearity (NOT quadratic, AP21)
# ====================================================================

class TestDeltaLinearity:
    """Delta is LINEAR in kappa, not quadratic (AP21)."""

    def test_linearity_check_function(self):
        """verify_delta_linearity_in_kappa passes for standard S_4."""
        S4 = Fraction(10, 27)
        kappas = [Fraction(k) for k in range(1, 6)]
        assert verify_delta_linearity_in_kappa(S4, kappas)

    def test_not_quadratic(self):
        """If Delta were kappa^2 * S_4 instead of kappa * S_4,
        doubling kappa would quadruple Delta. Verify it only doubles.
        """
        S4 = Fraction(3, 7)
        D1 = delta_discriminant(Fraction(1), S4)
        D2 = delta_discriminant(Fraction(2), S4)
        assert D2 == 2 * D1  # linear
        assert D2 != 4 * D1  # NOT quadratic


# ====================================================================
# 9. c-cancellation in Virasoro Delta
# ====================================================================

class TestVirasoroCancellation:
    """kappa*S_4 = (c/2)*10/[c(5c+22)] = 5/(5c+22) is regular at c=0."""

    def test_c_cancellation_verification(self):
        """All entries match product vs closed form."""
        results = verify_virasoro_c_cancellation()
        for key, data in results.items():
            assert data['match'], f"Mismatch at c={key}"

    def test_delta_finite_at_c0(self):
        """Delta(Vir, c=0) = 40/22 = 20/11 (finite, not divergent)."""
        assert delta_virasoro(Fraction(0)) == Fraction(20, 11)

    def test_kappa_and_s4_separately(self):
        """At c=0: kappa=0 and S_4=inf, but Delta=20/11."""
        assert kappa_virasoro(Fraction(0)) == Fraction(0)
        # S_4 has a pole at c=0, but the product is finite.
        # We verify through the closed-form Delta.
        assert delta_virasoro(Fraction(0)) == Fraction(20, 11)


# ====================================================================
# 10. Cross-check with discriminant_atlas.py
# ====================================================================

class TestCrossCheckAtlas:
    """Cross-check against the existing discriminant_atlas.py engine."""

    def test_virasoro_delta_matches_atlas(self):
        """Our delta_virasoro matches discriminant_atlas.virasoro_Delta."""
        from lib.discriminant_atlas import virasoro_Delta as atlas_Delta
        for c_val in [0, 1, 2, 5, 13, 25, 26]:
            c = Fraction(c_val)
            assert delta_virasoro(c) == atlas_Delta(c), \
                f"Mismatch with atlas at c={c_val}"

    def test_heisenberg_matches_atlas(self):
        """Our heisenberg data matches discriminant_atlas.heisenberg_data."""
        from lib.discriminant_atlas import heisenberg_data as atlas_heis
        atlas = atlas_heis(1)
        assert delta_heisenberg(Fraction(1)) == atlas['Delta']
        assert kappa_heisenberg(Fraction(1)) == atlas['kappa'] * 2
        # Atlas uses kappa = n/2 for rank n; our Heisenberg uses kappa = k.
        # At rank 1, atlas kappa = 1/2, our kappa(H_k=1) = 1. Different conventions.
        # This is fine: the atlas uses kappa(Heisenberg rank n) = n/2 (lattice convention),
        # we use kappa(H_k) = k. Both give Delta = 0.
        assert atlas['Delta'] == Fraction(0)

    def test_affine_sl2_matches_atlas(self):
        """Our sl_2 data matches discriminant_atlas.affine_sl2_data."""
        from lib.discriminant_atlas import affine_sl2_data as atlas_sl2
        atlas = atlas_sl2(1)
        assert delta_affine_km(3, 2, Fraction(1)) == atlas['Delta']
        assert atlas['Delta'] == Fraction(0)

    def test_w3_t_line_matches_atlas(self):
        """W_3 T-line matches discriminant_atlas."""
        from lib.discriminant_atlas import w3_T_line_data as atlas_w3t
        for c_val in [2, 13]:
            c = Fraction(c_val)
            atlas = atlas_w3t(c)
            assert delta_w3_T_line(c) == atlas['Delta']

    def test_w3_w_line_matches_atlas(self):
        """W_3 W-line matches discriminant_atlas."""
        from lib.discriminant_atlas import w3_W_line_data as atlas_w3w
        for c_val in [2, 13]:
            c = Fraction(c_val)
            atlas = atlas_w3w(c)
            assert delta_w3_W_line(c) == atlas['Delta']


# ====================================================================
# 11. Full landscape atlas
# ====================================================================

class TestFullLandscape:
    """Verify the full discriminant landscape."""

    def test_landscape_nonempty(self):
        """Landscape has entries for all four classes."""
        landscape = full_discriminant_landscape()
        assert len(landscape) > 20

    def test_all_class_g_have_delta_zero(self):
        """Every class G entry has Delta = 0."""
        landscape = full_discriminant_landscape()
        for name, data in landscape.items():
            if data['shadow_class'] == 'G':
                assert data['Delta'] == Fraction(0), \
                    f"Class G entry {name} has nonzero Delta"
                assert data['finite_tower'], \
                    f"Class G entry {name} marked infinite tower"

    def test_all_class_l_have_delta_zero(self):
        """Every class L entry has Delta = 0."""
        landscape = full_discriminant_landscape()
        for name, data in landscape.items():
            if data['shadow_class'] == 'L':
                assert data['Delta'] == Fraction(0), \
                    f"Class L entry {name} has nonzero Delta"

    def test_all_class_m_have_delta_nonzero(self):
        """Every class M entry has Delta != 0."""
        landscape = full_discriminant_landscape()
        for name, data in landscape.items():
            if data['shadow_class'] == 'M':
                assert data['Delta'] != Fraction(0), \
                    f"Class M entry {name} has zero Delta"
                assert not data['finite_tower'], \
                    f"Class M entry {name} marked finite tower"

    def test_virasoro_entries_present(self):
        """Virasoro at c=1, 13, 26 present in landscape."""
        landscape = full_discriminant_landscape()
        assert 'Virasoro_c1' in landscape
        assert 'Virasoro_c13' in landscape
        assert 'Virasoro_c26' in landscape


# ====================================================================
# 12. Virasoro large-c asymptotic
# ====================================================================

class TestVirasoroAsymptotics:
    """Delta(Vir_c) = 40/(5c+22) -> 8/c at large c."""

    def test_large_c_asymptotic(self):
        """At c=1000: Delta = 40/5022 ~ 8/1000 = 0.008.
        Relative error |Delta - 8/c| / (8/c) -> 22/(5c) ~ 0.0044.
        """
        c = Fraction(1000)
        D = delta_virasoro(c)
        asymptotic = Fraction(8, 1000)
        # Exact: D = 40/5022 = 20/2511
        assert D == Fraction(40, 5022)
        rel_err = abs(D - asymptotic) / asymptotic
        assert rel_err < Fraction(1, 100)  # < 1% at c=1000

    def test_semiclassical_limit(self):
        """Delta -> 0 as c -> infinity (semiclassical: tower becomes trivial)."""
        for c_val in [100, 1000, 10000]:
            D = delta_virasoro(Fraction(c_val))
            assert D > 0
            assert D < Fraction(1)  # small at large c
