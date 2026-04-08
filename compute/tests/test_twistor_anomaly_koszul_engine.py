r"""Tests for twistor anomaly Koszul engine.

Multi-path verification of the twistor-space anomaly cancellation
as a Koszulness/shadow condition.

VERIFICATION PATHS:
  Path 1: Direct computation from Lie algebra data
  Path 2: Cross-check against lie_algebra.py (cartan_data)
  Path 3: Algebraic identities (AP24: complementarity)
  Path 4: Costello's published results (2111.08879)
  Path 5: Deligne exceptional series characterization
  Path 6: Numerical evaluation at specific levels
  Path 7: Dimensional/degree analysis

REFERENCE: Costello (2111.08879), Costello-Li (2104.14064),
  Deligne (1996), Landsberg-Manivel (2002).
"""

import pytest
from fractions import Fraction

from compute.lib.twistor_anomaly_koszul_engine import (
    # Lie algebra data
    get_lie_data,
    LIE_ALGEBRA_TABLE,
    # Kappa and shadow
    kappa_affine,
    kappa_at_k0,
    central_charge_affine,
    ff_dual_level,
    shadow_class_affine,
    shadow_depth_affine,
    # Anomaly
    anomaly_coefficient,
    dim_over_h_dual,
    anomaly_relates_to_kappa,
    # Selection
    is_costello_allowed,
    is_in_deligne_series,
    costello_equals_deligne,
    COSTELLO_ALLOWED_SDYM,
    DELIGNE_EXCEPTIONAL_SERIES,
    # Fourth-order Casimir
    fourth_order_casimir_ratio,
    quartic_factorizes,
    has_independent_quartic_casimir,
    number_of_independent_casimirs,
    quartic_obstruction_mechanism,
    casimir_degrees,
    # Kappa effective
    kappa_eff_sdym,
    kappa_eff_with_axion,
    # QCD
    kappa_qcd,
    nf_for_kappa_zero,
    holomorphic_beta_coefficient,
    four_d_beta_coefficient,
    nf_conformal_holomorphic,
    nf_conformal_4d,
    kappa_qcd_nf9_su3,
    level_for_kappa_zero_nf9_su3,
    verify_nf9_kappa_zero,
    # Profiles
    compute_shadow_profile,
    full_landscape_profiles,
    # Deligne
    deligne_series_kappa_sequence,
    deligne_series_anomaly_sequence,
    deligne_dim_formula_check,
    # Complementarity
    complementarity_check,
    # Casimir
    casimir_2_adjoint,
    dynkin_index_adjoint,
    # Diagnostics
    disallowed_obstruction,
    selection_theorem_check,
    selection_all_agree,
    summary_table,
    q_contact_interpretation,
)


# ============================================================================
# 1. Lie algebra data verification (Path 1: direct computation)
# ============================================================================

class TestLieAlgebraData:
    """Verify Lie algebra dimensions, Coxeter numbers, etc."""

    def test_su2_data(self):
        d = get_lie_data('SU(2)')
        assert d.dim == 3
        assert d.dual_coxeter == 2
        assert d.rank == 1
        assert d.simply_laced is True

    def test_su3_data(self):
        d = get_lie_data('SU(3)')
        assert d.dim == 8
        assert d.dual_coxeter == 3
        assert d.rank == 2

    def test_su4_data(self):
        d = get_lie_data('SU(4)')
        assert d.dim == 15
        assert d.dual_coxeter == 4
        assert d.rank == 3

    def test_so8_data(self):
        """SO(8) = D_4: the triality group."""
        d = get_lie_data('SO(8)')
        assert d.dim == 28
        assert d.dual_coxeter == 6
        assert d.rank == 4
        assert d.simply_laced is True

    def test_g2_data(self):
        d = get_lie_data('G2')
        assert d.dim == 14
        assert d.dual_coxeter == 4
        assert d.rank == 2
        assert d.simply_laced is False
        # G_2: h = 6, h^vee = 4 (non-simply-laced!)

    def test_f4_data(self):
        d = get_lie_data('F4')
        assert d.dim == 52
        assert d.dual_coxeter == 9
        assert d.rank == 4
        assert d.simply_laced is False

    def test_e6_data(self):
        d = get_lie_data('E6')
        assert d.dim == 78
        assert d.dual_coxeter == 12
        assert d.rank == 6

    def test_e7_data(self):
        d = get_lie_data('E7')
        assert d.dim == 133
        assert d.dual_coxeter == 18
        assert d.rank == 7

    def test_e8_data(self):
        d = get_lie_data('E8')
        assert d.dim == 248
        assert d.dual_coxeter == 30
        assert d.rank == 8

    def test_dim_formula_a_type(self):
        """dim(sl_{n+1}) = n(n+2) = n^2 + 2n."""
        for n in range(1, 8):
            name = f'SU({n+1})'
            d = get_lie_data(name)
            assert d.dim == n * (n + 2), f"dim(sl_{n+1}) wrong"

    def test_dim_formula_d_type(self):
        """dim(so_{2n}) = n(2n-1)."""
        for n, name in [(4, 'SO(8)'), (5, 'SO(10)'), (6, 'SO(12)'), (7, 'SO(14)')]:
            d = get_lie_data(name)
            assert d.dim == n * (2 * n - 1), f"dim(so_{2*n}) wrong"


# ============================================================================
# 2. Kappa verification (Path 1+2: direct computation + cross-check)
# ============================================================================

class TestKappa:
    """Verify kappa formulas from first principles (AP1)."""

    def test_kappa_su2_k0(self):
        """kappa(sl_2, 0) = 3*2/(2*2) = 3/2."""
        assert kappa_at_k0('SU(2)') == Fraction(3, 2)

    def test_kappa_su3_k0(self):
        """kappa(sl_3, 0) = 8*3/(2*3) = 4."""
        assert kappa_at_k0('SU(3)') == Fraction(4)

    def test_kappa_so8_k0(self):
        """kappa(so_8, 0) = 28*6/(2*6) = 14."""
        assert kappa_at_k0('SO(8)') == Fraction(14)

    def test_kappa_g2_k0(self):
        """kappa(G_2, 0) = 14*4/(2*4) = 7."""
        assert kappa_at_k0('G2') == Fraction(7)

    def test_kappa_f4_k0(self):
        """kappa(F_4, 0) = 52*9/(2*9) = 26."""
        assert kappa_at_k0('F4') == Fraction(26)

    def test_kappa_e6_k0(self):
        """kappa(E_6, 0) = 78*12/(2*12) = 39."""
        assert kappa_at_k0('E6') == Fraction(39)

    def test_kappa_e7_k0(self):
        """kappa(E_7, 0) = 133*18/(2*18) = 133/2."""
        assert kappa_at_k0('E7') == Fraction(133, 2)

    def test_kappa_e8_k0(self):
        """kappa(E_8, 0) = 248*30/(2*30) = 124."""
        assert kappa_at_k0('E8') == Fraction(124)

    def test_kappa_at_k0_equals_dim_over_2(self):
        """At k=0: kappa(g, 0) = dim(g)/2 for ALL algebras."""
        for name in LIE_ALGEBRA_TABLE:
            d = get_lie_data(name)
            assert kappa_at_k0(name) == Fraction(d.dim, 2), \
                f"kappa(g,0) != dim/2 for {name}"

    def test_kappa_generic_level(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        k = Fraction(5)
        assert kappa_affine('SU(2)', k) == Fraction(3) * (k + 2) / 4

    def test_kappa_cross_check_with_formula(self):
        """Cross-check: kappa = dim*(k+h^vee)/(2*h^vee)."""
        for name in LIE_ALGEBRA_TABLE:
            d = get_lie_data(name)
            k = Fraction(3)
            expected = Fraction(d.dim) * (k + d.dual_coxeter) / (2 * d.dual_coxeter)
            assert kappa_affine(name, k) == expected, \
                f"kappa formula mismatch for {name}"


# ============================================================================
# 3. Anomaly coefficient verification (Path 1+4)
# ============================================================================

class TestAnomaly:
    """Verify anomaly coefficients and their relation to kappa."""

    def test_anomaly_coefficient_formula(self):
        """a(G) = h^vee * dim(G)."""
        for name in LIE_ALGEBRA_TABLE:
            d = get_lie_data(name)
            assert anomaly_coefficient(name) == Fraction(d.dual_coxeter * d.dim)

    def test_anomaly_relates_to_kappa_identity(self):
        """a(G) = 2 * h^vee * kappa(g, 0) for all G."""
        for name in LIE_ALGEBRA_TABLE:
            assert anomaly_relates_to_kappa(name) == 0, \
                f"Anomaly-kappa relation fails for {name}"

    def test_dim_over_hdual_values(self):
        """Verify dim(G)/h^vee for Deligne series."""
        expected = {
            'SU(2)': Fraction(3, 2),
            'SU(3)': Fraction(8, 3),
            'G2':    Fraction(14, 4),  # = 7/2
            'SO(8)': Fraction(28, 6),  # = 14/3
            'F4':    Fraction(52, 9),
            'E6':    Fraction(78, 12),  # = 13/2
            'E7':    Fraction(133, 18),
            'E8':    Fraction(248, 30), # = 124/15
        }
        for name, exp in expected.items():
            assert dim_over_h_dual(name) == exp, \
                f"dim/h^vee wrong for {name}"


# ============================================================================
# 4. Costello selection rule (Path 4+5)
# ============================================================================

class TestCostelloSelection:
    """Verify Costello's group selection matches Deligne series."""

    def test_costello_equals_deligne(self):
        """The Costello-allowed set IS the Deligne exceptional series."""
        assert costello_equals_deligne()

    def test_allowed_groups(self):
        """Check each allowed group individually."""
        for name in ['SU(2)', 'SU(3)', 'SO(8)', 'G2', 'F4', 'E6', 'E7', 'E8']:
            assert is_costello_allowed(name), f"{name} should be allowed"
            assert is_in_deligne_series(name), f"{name} should be in Deligne series"

    def test_disallowed_groups(self):
        """Check that non-Deligne groups are disallowed."""
        for name in ['SU(4)', 'SU(5)', 'SU(6)', 'SO(10)', 'SO(12)', 'Sp(2)', 'Sp(3)']:
            assert not is_costello_allowed(name), f"{name} should be disallowed"
            assert not is_in_deligne_series(name), f"{name} should not be in Deligne series"

    def test_exactly_8_allowed(self):
        """Exactly 8 groups are allowed."""
        assert len(COSTELLO_ALLOWED_SDYM) == 8

    def test_selection_three_way_equivalence(self):
        """Verify (Costello allowed) <=> (Deligne) <=> (quartic factorizes)."""
        assert selection_all_agree()


# ============================================================================
# 5. Quartic factorization (Path 1+5)
# ============================================================================

class TestQuarticFactorization:
    """Verify quartic Casimir factorization is the mechanism."""

    def test_deligne_series_quartic_factorizes(self):
        """For all Deligne series algebras, the quartic factorizes."""
        for name in DELIGNE_EXCEPTIONAL_SERIES:
            assert quartic_factorizes(name), f"Quartic should factorize for {name}"

    def test_non_deligne_quartic_does_not_factorize(self):
        """For non-Deligne algebras, the quartic does NOT factorize."""
        for name in ['SU(4)', 'SU(5)', 'SU(6)', 'SO(10)', 'Sp(3)']:
            assert not quartic_factorizes(name), \
                f"Quartic should NOT factorize for {name}"

    def test_c4_ratio_computable_for_deligne(self):
        """C_4/C_2^2 is computable for all Deligne series."""
        for name in DELIGNE_EXCEPTIONAL_SERIES:
            ratio = fourth_order_casimir_ratio(name)
            assert ratio is not None, f"C_4 ratio should be computable for {name}"

    def test_c4_ratio_none_for_non_deligne(self):
        """C_4/C_2^2 is not a single ratio for non-Deligne (rank >= 3)."""
        for name in ['SU(4)', 'SU(5)', 'SO(10)']:
            ratio = fourth_order_casimir_ratio(name)
            assert ratio is None, f"C_4 ratio should be None for {name}"

    def test_su2_no_quartic_casimir(self):
        """SU(2) has rank 1: only C_2, no independent C_4."""
        assert not has_independent_quartic_casimir('SU(2)')
        assert number_of_independent_casimirs('SU(2)') == 1

    def test_su3_has_quartic_casimir(self):
        """SU(3) has rank 2: C_2 and C_3 (cubic, not quartic!).

        Exponents of A_2: [1, 2]. Casimir degrees: 2, 3.
        No degree-4 Casimir. So no independent quartic.
        """
        # A_2 exponents are [1, 2], giving Casimirs of degree 2 and 3.
        # There is NO degree-4 Casimir for SU(3).
        assert not has_independent_quartic_casimir('SU(3)')

    def test_su4_has_quartic_casimir(self):
        """SU(4) has rank 3: exponents [1,2,3], Casimir degrees [2,3,4].
        Independent quartic exists."""
        assert has_independent_quartic_casimir('SU(4)')

    def test_so8_has_quartic_casimir(self):
        """SO(8) has rank 4: exponents [1,3,3,5], Casimir degrees [2,4,4,6].
        Independent quartic exists, but it FACTORIZES (triality!)."""
        assert has_independent_quartic_casimir('SO(8)')
        assert quartic_factorizes('SO(8)')  # Deligne universality


# ============================================================================
# 6. Kappa effective (Path 1+3: direct + algebraic identity)
# ============================================================================

class TestKappaEffective:
    """Verify kappa_eff = 0 at k=0 for all groups."""

    def test_kappa_eff_zero_at_k0_all_groups(self):
        """kappa_eff(g, k=0) = 0 for ALL simple Lie algebras.

        This is because kappa(ghost) = -dim(g)/2 = -kappa(g,0).
        The genus-1 anomaly cancellation is automatic.
        """
        for name in LIE_ALGEBRA_TABLE:
            assert kappa_eff_sdym(name) == 0, \
                f"kappa_eff should be 0 at k=0 for {name}"

    def test_kappa_eff_with_axion_zero_all_levels(self):
        """With axion, kappa_eff = 0 at ALL levels."""
        for name in ['SU(2)', 'SU(3)', 'E8']:
            for k_val in [Fraction(0), Fraction(1), Fraction(5)]:
                assert kappa_eff_with_axion(name, k_val) == 0, \
                    f"kappa_eff with axion should be 0 for {name} at k={k_val}"

    def test_kappa_eff_nonzero_at_generic_level(self):
        """Without axion, kappa_eff != 0 at k != 0."""
        for name in ['SU(2)', 'E8']:
            assert kappa_eff_sdym(name, Fraction(1)) != 0


# ============================================================================
# 7. QCD matter: N_f conditions (Path 1+6)
# ============================================================================

class TestQCDMatter:
    """Verify QCD kappa and beta function conditions."""

    def test_kappa_qcd_su3_nf0(self):
        """Pure SU(3) at k=0: kappa = 4."""
        assert kappa_qcd(3, 0) == Fraction(4)

    def test_kappa_qcd_su3_nf9_k0(self):
        """SU(3), N_f=9 at k=0: kappa = 4 + 9*(-3) = 4 - 27 = -23."""
        assert kappa_qcd_nf9_su3() == Fraction(-23)

    def test_holomorphic_beta_su3_nf6(self):
        """b_0^hol(SU(3), N_f=6) = 3 - 3 = 0 (conformal)."""
        assert holomorphic_beta_coefficient(3, 6) == 0

    def test_holomorphic_beta_su3_nf9(self):
        """b_0^hol(SU(3), N_f=9) = 3 - 9/2 = -3/2 (IR free)."""
        assert holomorphic_beta_coefficient(3, 9) == Fraction(-3, 2)

    def test_4d_beta_su3_nf9(self):
        """b_0^4d(SU(3), N_f=9) = 11 - 6 = 5 (asymptotically free)."""
        assert four_d_beta_coefficient(3, 9) == Fraction(5)

    def test_nf_conformal_holomorphic_su3(self):
        """N_f = 2N = 6 for holomorphic conformal with SU(3)."""
        assert nf_conformal_holomorphic(3) == 6

    def test_nf_conformal_4d_su3(self):
        """N_f = 11N/2 = 33/2 for 4d conformal with SU(3)."""
        assert nf_conformal_4d(3) == Fraction(33, 2)

    def test_nf_for_kappa_zero_su3(self):
        """N_f for kappa = 0 with SU(3) at k=0: N_f = 4/3 (not integer!)."""
        assert nf_for_kappa_zero(3) == Fraction(4, 3)

    def test_nf9_level_for_kappa_zero(self):
        """Level k for kappa = 0 with N_f = 9, SU(3): k = 69/4."""
        assert level_for_kappa_zero_nf9_su3() == Fraction(69, 4)

    def test_verify_nf9_kappa_zero(self):
        """Verify kappa(sl_3, 69/4) + 9*(-3) = 0."""
        assert verify_nf9_kappa_zero()


# ============================================================================
# 8. Complementarity and duality (Path 3: algebraic identities)
# ============================================================================

class TestComplementarity:
    """Verify AP24 complementarity: kappa(k) + kappa(k') = 0."""

    def test_complementarity_all_km(self):
        """kappa(g,k) + kappa(g, -k-2h^vee) = 0 for all affine KM."""
        for name in LIE_ALGEBRA_TABLE:
            assert complementarity_check(name) == 0, \
                f"Complementarity fails for {name}"

    def test_ff_dual_level(self):
        """k' = -k - 2*h^vee."""
        assert ff_dual_level('SU(2)', Fraction(1)) == Fraction(-5)
        assert ff_dual_level('E8', Fraction(1)) == Fraction(-61)


# ============================================================================
# 9. Shadow tower analysis (Path 1+7)
# ============================================================================

class TestShadowTower:
    """Verify shadow classification for twistor-space groups."""

    def test_all_affine_class_l(self):
        """All affine KM algebras are class L (shadow depth 3)."""
        for name in LIE_ALGEBRA_TABLE:
            assert shadow_class_affine(name) == 'L'
            assert shadow_depth_affine(name) == 3

    def test_shadow_profile_completeness(self):
        """Shadow profile computable for all algebras."""
        profiles = full_landscape_profiles()
        assert len(profiles) == len(LIE_ALGEBRA_TABLE)
        for name, prof in profiles.items():
            assert prof.shadow_class == 'L'
            assert prof.shadow_depth == 3

    def test_disallowed_obstruction_su4(self):
        """SU(4) obstruction: kappa OK, quartic fails."""
        obs = disallowed_obstruction('SU(4)')
        assert not obs['allowed']
        assert obs['kappa_eff_zero']
        assert not obs['quartic_factorizes']

    def test_allowed_no_obstruction_e8(self):
        """E_8: no obstruction."""
        obs = disallowed_obstruction('E8')
        assert obs['allowed']


# ============================================================================
# 10. Deligne exceptional series (Path 5)
# ============================================================================

class TestDeligneSeries:
    """Verify Deligne exceptional series properties."""

    def test_deligne_dim_formula(self):
        """Vogel dimension formula matches actual dimensions."""
        assert deligne_dim_formula_check()

    def test_kappa_monotone_along_deligne(self):
        """Kappa at k=0 is monotonically increasing along the Deligne series."""
        seq = deligne_series_kappa_sequence()
        for i in range(len(seq) - 1):
            assert seq[i][1] < seq[i+1][1], \
                f"Kappa not increasing: {seq[i][0]}={seq[i][1]} >= {seq[i+1][0]}={seq[i+1][1]}"

    def test_anomaly_monotone_along_deligne(self):
        """Anomaly coefficient is monotonically increasing along the Deligne series."""
        seq = deligne_series_anomaly_sequence()
        for i in range(len(seq) - 1):
            assert seq[i][1] < seq[i+1][1]

    def test_c4_ratio_monotone_along_deligne(self):
        """C_4/C_2^2 ratio increases along the Deligne series."""
        prev = Fraction(0)
        for name in DELIGNE_EXCEPTIONAL_SERIES:
            ratio = fourth_order_casimir_ratio(name)
            assert ratio is not None
            assert ratio > prev, f"C_4 ratio not increasing at {name}"
            prev = ratio


# ============================================================================
# 11. Casimir data (Path 1+2)
# ============================================================================

class TestCasimir:
    """Verify Casimir invariant computations."""

    def test_casimir_2_adjoint(self):
        """C_2(adj) = 2*h^vee for all simple Lie algebras."""
        for name in LIE_ALGEBRA_TABLE:
            d = get_lie_data(name)
            assert casimir_2_adjoint(name) == Fraction(2 * d.dual_coxeter)

    def test_dynkin_index_adjoint(self):
        """I_2(adj) = 2*h^vee (same as C_2 with long-root normalization)."""
        for name in LIE_ALGEBRA_TABLE:
            assert dynkin_index_adjoint(name) == casimir_2_adjoint(name)

    def test_number_casimirs_equals_rank(self):
        """Number of independent Casimirs = rank."""
        for name in LIE_ALGEBRA_TABLE:
            d = get_lie_data(name)
            assert number_of_independent_casimirs(name) == d.rank


# ============================================================================
# 12. Cross-checks with existing engines (Path 2)
# ============================================================================

class TestCrossEngine:
    """Cross-check against lie_algebra.py and exceptional_shadow_engine.py."""

    def test_cross_check_lie_algebra_module(self):
        """Cross-check dims and h^vee against lie_algebra.cartan_data."""
        try:
            from compute.lib.lie_algebra import cartan_data
        except ImportError:
            pytest.skip("lie_algebra module not available")

        cross_checks = {
            'SU(2)': ('A', 1), 'SU(3)': ('A', 2), 'SU(4)': ('A', 3),
            'SO(8)': ('D', 4), 'SO(10)': ('D', 5),
            'G2': ('G', 2), 'F4': ('F', 4),
            'E6': ('E', 6), 'E7': ('E', 7), 'E8': ('E', 8),
        }
        for name, (ct, rk) in cross_checks.items():
            our_d = get_lie_data(name)
            ref_d = cartan_data(ct, rk)
            assert our_d.dim == ref_d.dim, f"dim mismatch for {name}"
            assert our_d.dual_coxeter == ref_d.h_dual, f"h^vee mismatch for {name}"
            assert our_d.coxeter == ref_d.h, f"h mismatch for {name}"

    def test_cross_check_exceptional_engine(self):
        """Cross-check E_6, E_7, E_8 kappa against exceptional_shadow_engine."""
        try:
            from compute.lib.exceptional_shadow_engine import (
                affine_kappa_numeric as exc_kappa,
            )
        except ImportError:
            pytest.skip("exceptional_shadow_engine not available")

        for name, exc_name in [('E6', 'E6'), ('E7', 'E7'), ('E8', 'E8')]:
            our_kappa = kappa_affine(name, Fraction(1))
            exc_val = exc_kappa(exc_name, 1)
            assert our_kappa == exc_val, f"kappa mismatch for {name} at k=1"

    def test_cross_check_kappa_km(self):
        """Cross-check against lie_algebra.kappa_km."""
        try:
            from compute.lib.lie_algebra import kappa_km
            from sympy import Rational
        except ImportError:
            pytest.skip("lie_algebra.kappa_km not available")

        cross = {
            'SU(2)': ('A', 1), 'SU(3)': ('A', 2), 'SU(4)': ('A', 3),
            'SO(8)': ('D', 4), 'G2': ('G', 2), 'F4': ('F', 4),
            'E6': ('E', 6), 'E7': ('E', 7), 'E8': ('E', 8),
        }
        for name, (ct, rk) in cross.items():
            our_val = kappa_affine(name, Fraction(1))
            ref_val = kappa_km(ct, rk, 1)
            assert float(our_val) == pytest.approx(float(ref_val), rel=1e-10), \
                f"kappa_km cross-check failed for {name}"


# ============================================================================
# 13. Summary and diagnostic output (Path 7: dimensional analysis)
# ============================================================================

class TestSummary:
    """Verify summary table and diagnostic functions."""

    def test_summary_table_completeness(self):
        """Summary table covers all algebras."""
        table = summary_table()
        assert len(table) == len(LIE_ALGEBRA_TABLE)

    def test_summary_table_consistency(self):
        """Each row is internally consistent."""
        for row in summary_table():
            name = row['name']
            assert row['costello_allowed'] == row['deligne_series'] == row['quartic_factorizes'], \
                f"Three-way equivalence fails in summary for {name}"

    def test_q_contact_interpretation_nonempty(self):
        """Q^contact interpretation returns a nonempty string."""
        result = q_contact_interpretation()
        assert len(result) > 50


# ============================================================================
# 14. Central charge verification (Path 6: numerical evaluation)
# ============================================================================

class TestCentralCharge:
    """Verify central charge at specific levels."""

    def test_central_charge_su2_k1(self):
        """c(sl_2, 1) = 1*3/(1+2) = 1."""
        assert central_charge_affine('SU(2)', Fraction(1)) == Fraction(1)

    def test_central_charge_e8_k1(self):
        """c(E_8, 1) = 248/31 = 8."""
        assert central_charge_affine('E8', Fraction(1)) == Fraction(8)

    def test_central_charge_e8_k2(self):
        """c(E_8, 2) = 2*248/32 = 248/16 = 31/2."""
        assert central_charge_affine('E8', Fraction(2)) == Fraction(31, 2)

    def test_kappa_not_equal_c_over_2(self):
        """AP9: kappa != c/2 for dim > 1 at generic level."""
        for name in ['SU(3)', 'E8']:
            k = Fraction(1)
            kap = kappa_affine(name, k)
            c = central_charge_affine(name, k)
            assert kap != c / 2, f"kappa should != c/2 for {name}"


# ============================================================================
# 15. Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Verify edge cases and error handling."""

    def test_unknown_algebra_raises(self):
        with pytest.raises(ValueError, match="Unknown"):
            get_lie_data('SU(100)')

    def test_critical_level_raises(self):
        with pytest.raises(ValueError, match="Critical"):
            central_charge_affine('SU(2)', Fraction(-2))

    def test_so5_equals_sp2(self):
        """SO(5) and Sp(2) are the same Lie algebra (B_2 = C_2).

        They have the same dim = 10 and h^vee = 3.
        """
        d_so5 = get_lie_data('SO(5)')
        d_sp2 = get_lie_data('Sp(2)')
        assert d_so5.dim == d_sp2.dim == 10
        assert d_so5.dual_coxeter == d_sp2.dual_coxeter == 3


# ============================================================================
# 16. Quartic obstruction mechanism (Path 1+5: refined classification)
# ============================================================================

class TestQuarticMechanism:
    """Verify the refined three-regime mechanism for quartic factorization."""

    def test_su2_low_rank(self):
        """SU(2): no quartic because rank 1."""
        assert quartic_obstruction_mechanism('SU(2)') == 'NO_QUARTIC_LOW_RANK'

    def test_su3_low_rank(self):
        """SU(3): no quartic because rank 2 with exponents [1,2]."""
        assert quartic_obstruction_mechanism('SU(3)') == 'NO_QUARTIC_LOW_RANK'

    def test_g2_low_rank(self):
        """G_2: rank 2 with exponents [1,5], no exponent = 3.

        G_2 has rank 2, so it falls in the low-rank regime.
        The exponents [1,5] give Casimir degrees [2,6] -- no degree 4.
        """
        assert quartic_obstruction_mechanism('G2') == 'NO_QUARTIC_LOW_RANK'

    def test_f4_exceptional(self):
        """F_4: exponents [1,5,7,11], no 3."""
        assert quartic_obstruction_mechanism('F4') == 'NO_QUARTIC_EXCEPTIONAL'

    def test_e6_exceptional(self):
        """E_6: exponents [1,4,5,7,8,11], no 3."""
        assert quartic_obstruction_mechanism('E6') == 'NO_QUARTIC_EXCEPTIONAL'

    def test_e7_exceptional(self):
        """E_7: exponents [1,5,7,9,11,13,17], no 3."""
        assert quartic_obstruction_mechanism('E7') == 'NO_QUARTIC_EXCEPTIONAL'

    def test_e8_exceptional(self):
        """E_8: exponents [1,7,11,13,17,19,23,29], no 3."""
        assert quartic_obstruction_mechanism('E8') == 'NO_QUARTIC_EXCEPTIONAL'

    def test_so8_triality(self):
        """SO(8) = D_4: has exponent 3 but triality makes it decomposable."""
        assert quartic_obstruction_mechanism('SO(8)') == 'QUARTIC_TRIALITY'

    def test_su4_independent(self):
        """SU(4): exponents [1,2,3], has independent C_4."""
        assert quartic_obstruction_mechanism('SU(4)') == 'QUARTIC_INDEPENDENT'

    def test_su5_independent(self):
        """SU(5): exponents [1,2,3,4], has independent C_4."""
        assert quartic_obstruction_mechanism('SU(5)') == 'QUARTIC_INDEPENDENT'

    def test_so10_independent(self):
        """SO(10) = D_5: exponents [1,3,4,5,7], has independent C_4."""
        assert quartic_obstruction_mechanism('SO(10)') == 'QUARTIC_INDEPENDENT'

    def test_sp2_independent(self):
        """Sp(2) = B_2: exponents [1,3], has degree-4 Casimir."""
        assert quartic_obstruction_mechanism('Sp(2)') == 'QUARTIC_INDEPENDENT'

    def test_mechanism_partitions_landscape(self):
        """Every algebra gets exactly one of the four mechanisms.
        Allowed algebras get LOW_RANK, EXCEPTIONAL, or TRIALITY.
        Disallowed algebras get INDEPENDENT."""
        allowed_mechanisms = {'NO_QUARTIC_LOW_RANK', 'NO_QUARTIC_EXCEPTIONAL',
                              'QUARTIC_TRIALITY'}
        for name in LIE_ALGEBRA_TABLE:
            mech = quartic_obstruction_mechanism(name)
            if is_costello_allowed(name):
                assert mech in allowed_mechanisms, \
                    f"Allowed {name} has mechanism {mech}"
            else:
                assert mech == 'QUARTIC_INDEPENDENT', \
                    f"Disallowed {name} has mechanism {mech}"


# ============================================================================
# 17. Casimir degree analysis (Path 7: degree analysis)
# ============================================================================

class TestCasimirDegrees:
    """Verify Casimir degree computations."""

    def test_su2_degrees(self):
        assert casimir_degrees('SU(2)') == [2]

    def test_su3_degrees(self):
        assert casimir_degrees('SU(3)') == [2, 3]

    def test_su4_degrees(self):
        assert casimir_degrees('SU(4)') == [2, 3, 4]

    def test_so8_degrees(self):
        """D_4 has TWO degree-4 Casimirs (exponents [1,3,3,5])."""
        assert casimir_degrees('SO(8)') == [2, 4, 4, 6]

    def test_e8_degrees(self):
        assert casimir_degrees('E8') == [2, 8, 12, 14, 18, 20, 24, 30]

    def test_g2_degrees(self):
        """G_2: degrees [2, 6]. Note: NO degree 4."""
        assert casimir_degrees('G2') == [2, 6]

    def test_f4_degrees(self):
        """F_4: degrees [2, 6, 8, 12]. Note: NO degree 4."""
        assert casimir_degrees('F4') == [2, 6, 8, 12]

    def test_no_degree_4_for_deligne_except_so8(self):
        """No Deligne algebra except SO(8) has a degree-4 Casimir."""
        for name in DELIGNE_EXCEPTIONAL_SERIES:
            degs = casimir_degrees(name)
            if name == 'SO(8)':
                assert 4 in degs  # SO(8) is the exception
            elif name in ('SU(2)', 'SU(3)'):
                assert 4 not in degs  # too low rank
            else:
                assert 4 not in degs, f"{name} should have no degree-4 Casimir"

    def test_all_non_deligne_have_degree_4(self):
        """All non-Deligne algebras in our table with rank >= 2 have degree-4 Casimir.

        This is because for A_{n>=3}, B_n, C_n, D_{n>=5}, exponent 3 appears.
        """
        for name in LIE_ALGEBRA_TABLE:
            if not is_in_deligne_series(name):
                d = get_lie_data(name)
                degs = casimir_degrees(name)
                if d.rank >= 2:
                    # All our non-Deligne examples have exponent 3
                    assert 4 in degs, f"{name} should have degree-4 Casimir"
