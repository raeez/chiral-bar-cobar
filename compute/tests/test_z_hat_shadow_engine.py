r"""Tests for the Gukov-Pei-Putrov Z-hat shadow engine.

Tests cover:
1. Seifert data construction (Poincare, Brieskorn Sigma(2,3,7), etc.)
2. Lawrence-Zagier character for three-pole Brieskorn spheres
3. GPP Z-hat as false theta function (leading terms, support, signs)
4. Cross-verification against known literature values
5. Affine level and Sugawara central charge for GPP correspondence
6. Shadow GF density vs Z-hat density (support mismatch obstruction)
7. AJK lattice cohomology Euler characteristic reproduces Z-hat
8. Projection obstruction: Z-hat is NOT a projection of shadow GF

References:
    Lawrence-Zagier 1999 (Asian J. Math 3, 93-107)
    Gukov-Pei-Putrov-Vafa 2017 (arXiv:1701.06567)
    Akhmechet-Johnson-Krushkal 2021 (arXiv:2109.14139)

Manuscript cross-references (future integration):
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-eisenstein (arithmetic_shadows.tex)
"""

from fractions import Fraction
from math import gcd

import pytest

from compute.lib.z_hat_shadow_engine import (
    PlumbingTree,
    SeifertData,
    poincare_sphere,
    brieskorn_237,
    brieskorn_2_3_n,
    brieskorn_general,
    lawrence_zagier_character,
    character_support,
    QSeries,
    gpp_framing_shift,
    z_hat_lawrence_zagier,
    wrt_radial_limit,
    negative_level_affine_kappa,
    gpp_affine_level_for_brieskorn,
    gpp_central_charge_for_brieskorn,
    shadow_gf_support_density,
    z_hat_support_density,
    projection_obstruction_check,
    LatticeCohomology,
    ajk_lattice_cohomology_poincare,
    cross_verify_z_hat_two_paths,
    gpp_summary,
)


# =========================================================================
# Section 1: Seifert data construction (5 tests)
# =========================================================================

class TestSeifertData:

    def test_poincare_P_equals_30(self):
        """Poincare sphere Sigma(2,3,5) has P = 30."""
        assert poincare_sphere().P == 30

    def test_poincare_n_exceptional(self):
        """Three exceptional fibers."""
        assert poincare_sphere().n_exceptional == 3

    def test_brieskorn_237_P(self):
        """Sigma(2,3,7) has P = 42."""
        assert brieskorn_237().P == 42

    def test_brieskorn_2_3_n_valid(self):
        """Sigma(2,3,n) valid for n coprime to 6, n >= 5."""
        for n in [5, 7, 11, 13, 17, 19, 23]:
            s = brieskorn_2_3_n(n)
            assert s.P == 6 * n

    def test_brieskorn_2_3_n_invalid(self):
        """Sigma(2,3,4) fails (gcd(4,6) > 1)."""
        with pytest.raises(ValueError):
            brieskorn_2_3_n(4)

    def test_brieskorn_general_coprime_check(self):
        """Sigma(p,q,r) requires pairwise coprime."""
        with pytest.raises(ValueError):
            brieskorn_general(2, 4, 5)  # gcd(2,4)=2

    def test_brieskorn_general_valid(self):
        """Sigma(3, 4, 5) valid."""
        s = brieskorn_general(3, 4, 5)
        assert s.P == 60


# =========================================================================
# Section 2: Lawrence-Zagier character (8 tests)
# =========================================================================

class TestLawrenceZagierCharacter:

    def test_poincare_support_size(self):
        """Sigma(2,3,5): chi has 8 nonzero residues mod 60."""
        chi = lawrence_zagier_character(poincare_sphere())
        support = character_support(chi)
        assert len(support) == 8

    def test_poincare_support_residues(self):
        """Sigma(2,3,5): chi supported on {1,11,19,29,31,41,49,59} mod 60."""
        chi = lawrence_zagier_character(poincare_sphere())
        support = set(character_support(chi))
        expected = {1, 11, 19, 29, 31, 41, 49, 59}
        assert support == expected

    def test_poincare_char_values_low(self):
        """Sigma(2,3,5): chi(1) = chi(11) = chi(19) = chi(29) = +1."""
        chi = lawrence_zagier_character(poincare_sphere())
        for r in [1, 11, 19, 29]:
            assert chi[r] == 1

    def test_poincare_char_values_high(self):
        """Sigma(2,3,5): chi(31) = chi(41) = chi(49) = chi(59) = -1 (oddness)."""
        chi = lawrence_zagier_character(poincare_sphere())
        for r in [31, 41, 49, 59]:
            assert chi[r] == -1

    def test_character_oddness(self):
        """chi(2P - r) = -chi(r) for all r in support."""
        seifert = poincare_sphere()
        chi = lawrence_zagier_character(seifert)
        twoP = 2 * seifert.P
        for r, v in chi.items():
            neg = (twoP - r) % twoP
            if neg in chi:
                assert chi[neg] == -v

    def test_brieskorn_237_support_size(self):
        """Sigma(2,3,7): chi has 8 nonzero residues mod 84."""
        chi = lawrence_zagier_character(brieskorn_237())
        assert len(character_support(chi)) == 8

    def test_brieskorn_237_support_residues(self):
        """Sigma(2,3,7) support: {1,13,29,41,43,55,71,83} mod 84."""
        chi = lawrence_zagier_character(brieskorn_237())
        support = set(character_support(chi))
        expected = {1, 13, 29, 41, 43, 55, 71, 83}
        assert support == expected

    def test_brieskorn_2_3_11_has_support(self):
        """Sigma(2,3,11) character has 8 support residues mod 132."""
        s = brieskorn_2_3_n(11)
        chi = lawrence_zagier_character(s)
        assert len(character_support(chi)) == 8


# =========================================================================
# Section 3: GPP Z-hat as false theta (10 tests)
# =========================================================================

class TestZHatFalseTheta:

    def test_poincare_leading_exponent(self):
        """Z-hat(-Sigma(2,3,5)) unshifted leading exponent is 1/120."""
        series = z_hat_lawrence_zagier(poincare_sphere(), max_terms=200, shifted=True)
        leading = series.leading_terms(1)
        assert leading[0][0] == Fraction(1, 120)

    def test_poincare_leading_coefficient(self):
        """Z-hat(-Sigma(2,3,5)): coefficient of q^{1/120} is +1."""
        series = z_hat_lawrence_zagier(poincare_sphere(), max_terms=200, shifted=True)
        leading = series.leading_terms(1)
        assert leading[0][1] == 1

    def test_poincare_second_term(self):
        """Second term of Z-hat(-Sigma(2,3,5)): q^{121/120}."""
        series = z_hat_lawrence_zagier(poincare_sphere(), max_terms=200, shifted=True)
        leading = series.leading_terms(2)
        assert leading[1][0] == Fraction(121, 120)

    def test_poincare_exponents_are_sparse(self):
        """Z-hat exponents grow quadratically (not linearly) => sparse support."""
        series = z_hat_lawrence_zagier(poincare_sphere(), max_terms=200, shifted=True)
        exponents = sorted(series.coefficients.keys())
        # The n-th exponent should grow like n^2 / (4P) with n in support residues
        # So exponents[1] / exponents[0] >= 100 (quadratic gap)
        ratio = float(exponents[1]) / float(exponents[0])
        assert ratio >= 100

    def test_poincare_integer_coefficients(self):
        """All Z-hat coefficients are integers (+/- 1 for Brieskorn)."""
        series = z_hat_lawrence_zagier(poincare_sphere(), max_terms=100, shifted=True)
        for exp, coeff in series.coefficients.items():
            assert isinstance(coeff, int)
            assert abs(coeff) == 1

    def test_brieskorn_237_leading_exponent(self):
        """Sigma(2,3,7): leading exponent is 1/168."""
        series = z_hat_lawrence_zagier(brieskorn_237(), max_terms=200, shifted=True)
        leading = series.leading_terms(1)
        assert leading[0][0] == Fraction(1, 168)

    def test_brieskorn_237_second_exponent(self):
        """Sigma(2,3,7): second exponent is 169/168 (n=13)."""
        series = z_hat_lawrence_zagier(brieskorn_237(), max_terms=200, shifted=True)
        leading = series.leading_terms(2)
        assert leading[1][0] == Fraction(169, 168)

    def test_framing_shift_poincare(self):
        """Poincare framing shift is -3/2."""
        assert gpp_framing_shift(poincare_sphere()) == Fraction(-3, 2)

    def test_framing_shift_237(self):
        """Sigma(2,3,7) framing shift is -1/2."""
        assert gpp_framing_shift(brieskorn_237()) == Fraction(-1, 2)

    def test_framed_z_hat_poincare(self):
        """Framed Z-hat(-Sigma(2,3,5)): leading term at q^{1/120 - 3/2} = q^{-179/120}."""
        framed = z_hat_lawrence_zagier(poincare_sphere(), max_terms=100, shifted=False)
        leading = framed.leading_terms(1)
        expected = Fraction(1, 120) - Fraction(3, 2)
        assert leading[0][0] == expected


# =========================================================================
# Section 4: Q-series arithmetic (5 tests)
# =========================================================================

class TestQSeries:

    def test_qseries_add(self):
        """QSeries.add accumulates coefficients."""
        s = QSeries()
        s.add(Fraction(1, 2), 3)
        s.add(Fraction(1, 2), 5)
        assert s.coefficients[Fraction(1, 2)] == 8

    def test_qseries_add_zero_removes(self):
        """Adding opposite coefficient removes entry."""
        s = QSeries()
        s.add(Fraction(1, 4), 1)
        s.add(Fraction(1, 4), -1)
        assert Fraction(1, 4) not in s.coefficients

    def test_qseries_leading_terms_sorted(self):
        """Leading terms are sorted by exponent."""
        s = QSeries()
        s.add(Fraction(3), 7)
        s.add(Fraction(1), 5)
        s.add(Fraction(2), 6)
        lead = s.leading_terms(2)
        assert lead[0][0] == Fraction(1)
        assert lead[1][0] == Fraction(2)

    def test_qseries_evaluate_small_q(self):
        """Evaluate at q = 0.1: leading term dominates."""
        s = QSeries()
        s.add(Fraction(0), 1)  # constant 1
        s.add(Fraction(1), 2)  # + 2q
        val = s.evaluate(0.1)
        assert abs(val - 1.2) < 1e-10

    def test_qseries_skip_zero_coeff(self):
        """Adding zero does nothing."""
        s = QSeries()
        s.add(Fraction(1), 0)
        assert len(s.coefficients) == 0


# =========================================================================
# Section 5: WRT radial limits (3 tests)
# =========================================================================

class TestWRTLimits:

    def test_poincare_wrt_finite(self):
        """Radial limit of Z-hat at q -> zeta_5 is finite."""
        val = wrt_radial_limit(poincare_sphere(), k=5, max_terms=50)
        assert abs(val) < 1e10  # finite

    def test_poincare_wrt_k3(self):
        """Radial limit at zeta_3 is computable."""
        val = wrt_radial_limit(poincare_sphere(), k=3, max_terms=50)
        assert abs(val) < 1e10

    def test_brieskorn_237_wrt_k4(self):
        """Sigma(2,3,7) radial limit at zeta_4."""
        val = wrt_radial_limit(brieskorn_237(), k=4, max_terms=50)
        assert abs(val) < 1e10


# =========================================================================
# Section 6: Affine level / Sugawara central charge (5 tests)
# =========================================================================

class TestAffineLevel:

    def test_poincare_affine_level(self):
        """Sigma(2,3,5): GPP level k = -2 + 1/30 = -59/30."""
        level = gpp_affine_level_for_brieskorn(poincare_sphere())
        assert level == Fraction(-59, 30)

    def test_brieskorn_237_affine_level(self):
        """Sigma(2,3,7): level = -2 + 1/42 = -83/42."""
        level = gpp_affine_level_for_brieskorn(brieskorn_237())
        assert level == Fraction(-83, 42)

    def test_poincare_central_charge(self):
        """Sigma(2,3,5): c = 3 - 6*30 = -177."""
        c = gpp_central_charge_for_brieskorn(poincare_sphere())
        assert c == -177

    def test_brieskorn_237_central_charge(self):
        """Sigma(2,3,7): c = 3 - 6*42 = -249."""
        c = gpp_central_charge_for_brieskorn(brieskorn_237())
        assert c == -249

    def test_sugawara_negative(self):
        """All Brieskorn GPP central charges are negative (non-unitary)."""
        for s in [poincare_sphere(), brieskorn_237(), brieskorn_2_3_n(11)]:
            c = gpp_central_charge_for_brieskorn(s)
            assert c < 0


# =========================================================================
# Section 7: Shadow GF vs Z-hat support density (5 tests)
# =========================================================================

class TestSupportDensity:

    def test_shadow_density_virasoro_c2(self):
        """Shadow GF of Vir_{c=2} has density ~1 (every arity is nonzero)."""
        data = shadow_gf_support_density(c_val=2.0, max_arity=40)
        assert data['density'] > 0.9

    def test_shadow_density_virasoro_c13(self):
        """Shadow GF of Vir_{c=13} has density ~1 (class M infinite tower)."""
        data = shadow_gf_support_density(c_val=13.0, max_arity=40)
        assert data['density'] > 0.9

    def test_z_hat_density_poincare_small(self):
        """Z-hat for Poincare is very sparse (density < 0.01)."""
        data = z_hat_support_density(poincare_sphere(), max_terms=300)
        assert data['density'] < 0.01

    def test_z_hat_density_237_small(self):
        """Z-hat for Sigma(2,3,7) is very sparse."""
        data = z_hat_support_density(brieskorn_237(), max_terms=300)
        assert data['density'] < 0.01

    def test_density_ratio_obstruction(self):
        """Shadow density >> Z-hat density (projection obstruction)."""
        shadow = shadow_gf_support_density(2.0, max_arity=40)
        z_hat = z_hat_support_density(poincare_sphere(), max_terms=200)
        assert shadow['density'] > 10 * z_hat['density']


# =========================================================================
# Section 8: Projection obstruction theorem (3 tests)
# =========================================================================

class TestProjectionObstruction:

    def test_projection_fails_poincare_c2(self):
        """No projection of shadow GF(Vir_{c=2}) equals Z-hat(Poincare)."""
        obs = projection_obstruction_check(
            poincare_sphere(), c_val=2.0, max_terms=40
        )
        assert not obs['projection_possible']

    def test_projection_fails_237_c13(self):
        """No projection of shadow GF(Vir_{c=13}) equals Z-hat(Sigma(2,3,7))."""
        obs = projection_obstruction_check(
            brieskorn_237(), c_val=13.0, max_terms=40
        )
        assert not obs['projection_possible']

    def test_obstruction_positive(self):
        """Obstruction (shadow density - Z-hat density) is strictly positive."""
        obs = projection_obstruction_check(poincare_sphere(), c_val=7.0)
        assert obs['obstruction'] > 0


# =========================================================================
# Section 9: AJK lattice cohomology (4 tests)
# =========================================================================

class TestLatticeCohomology:

    def test_ajk_construction_poincare(self):
        """AJK lattice cohomology for Poincare sphere is constructible."""
        ajk = ajk_lattice_cohomology_poincare()
        assert isinstance(ajk, LatticeCohomology)
        assert ajk.seifert.P == 30

    def test_ajk_euler_characteristic_nonzero(self):
        """Euler characteristic is nonzero q-series."""
        ajk = ajk_lattice_cohomology_poincare()
        chi = ajk.euler_characteristic()
        assert len(chi.coefficients) > 0

    def test_ajk_recovers_z_hat(self):
        """AJK Euler characteristic equals Z-hat for Poincare (leading terms)."""
        ajk = ajk_lattice_cohomology_poincare()
        chi = ajk.euler_characteristic()
        direct = z_hat_lawrence_zagier(poincare_sphere(), max_terms=80, shifted=True)
        # Compare leading 4 terms
        ajk_lead = chi.leading_terms(4)
        direct_lead = direct.leading_terms(4)
        assert ajk_lead == direct_lead

    def test_ajk_bigraded_structure(self):
        """AJK has a homological grading (sign convention for chi)."""
        ajk = ajk_lattice_cohomology_poincare()
        h_grades = {h for (h, q) in ajk.bigraded_ranks.keys()}
        assert h_grades.issubset({0, 1})  # +/- coefficients => 2 grades


# =========================================================================
# Section 10: Cross-verification (3 tests)
# =========================================================================

class TestCrossVerification:

    def test_cross_verify_poincare(self):
        """Two paths for Z-hat(Poincare) agree."""
        result = cross_verify_z_hat_two_paths(poincare_sphere())
        assert result['paths_agree'] is True

    def test_cross_verify_non_poincare_one_path(self):
        """Non-Poincare cross-verify returns None for AJK (single path)."""
        result = cross_verify_z_hat_two_paths(brieskorn_237())
        assert result['paths_agree'] is None
        assert result['direct_leading_terms'] is not None

    def test_leading_coefficient_all_plus_one(self):
        """For all Brieskorn Sigma(2,3,n) with n odd coprime to 6, leading coeff is +1."""
        for n in [5, 7, 11, 13]:
            s = brieskorn_2_3_n(n)
            series = z_hat_lawrence_zagier(s, max_terms=80, shifted=True)
            leading = series.leading_terms(1)
            assert leading[0][1] == 1


# =========================================================================
# Section 11: GPP summary (2 tests)
# =========================================================================

class TestGPPSummary:

    def test_summary_poincare(self):
        """GPP summary for Poincare returns all expected keys."""
        summary = gpp_summary(poincare_sphere())
        assert 'seifert' in summary
        assert 'character' in summary
        assert 'z_hat_unshifted_leading' in summary
        assert 'affine_level' in summary
        assert summary['affine_level'] == Fraction(-59, 30)
        assert summary['sugawara_central_charge'] == -177

    def test_summary_237(self):
        """GPP summary for Sigma(2,3,7)."""
        summary = gpp_summary(brieskorn_237())
        assert summary['seifert']['P'] == 42
        assert summary['sugawara_central_charge'] == -249


# =========================================================================
# Section 12: Multi-path verification (multipath verification mandate) (4 tests)
# =========================================================================

class TestMultiPathVerification:

    def test_poincare_support_three_paths(self):
        """Poincare support via (1) direct chi, (2) Z-hat exponents, (3) AJK."""
        # Path 1: direct character
        chi = lawrence_zagier_character(poincare_sphere())
        path1_size = len([v for v in chi.values() if v != 0])

        # Path 2: Z-hat series
        series = z_hat_lawrence_zagier(poincare_sphere(), max_terms=80, shifted=True)
        # Count support up to exponent 59^2/120 (first full period)
        max_exp_period_1 = Fraction(59 * 59, 120)
        path2_size = sum(
            1 for e in series.coefficients.keys() if e <= max_exp_period_1
        )

        # Path 3: AJK Euler characteristic
        ajk = ajk_lattice_cohomology_poincare()
        ajk_chi = ajk.euler_characteristic()
        path3_size = sum(
            1 for e in ajk_chi.coefficients.keys() if e <= max_exp_period_1
        )

        # All three should give 8 (the character support size)
        assert path1_size == 8
        assert path2_size == 8
        assert path3_size == 8

    def test_poincare_first_term_cross_check(self):
        """First Z-hat term 1/120 via: (1) direct LZ, (2) n=1 formula."""
        # Path 1: Z-hat leading term
        series = z_hat_lawrence_zagier(poincare_sphere(), max_terms=10, shifted=True)
        path1 = series.leading_terms(1)[0][0]

        # Path 2: n=1, 4P=120, exponent = 1/120
        P = 30
        path2 = Fraction(1 * 1, 4 * P)

        assert path1 == path2 == Fraction(1, 120)

    def test_brieskorn_237_character_three_paths(self):
        """Sigma(2,3,7) character values: direct vs oddness vs integer-arithmetic."""
        chi = lawrence_zagier_character(brieskorn_237())

        # Path 1: chi(1) = +1 by construction (normalized)
        assert chi[1] == 1

        # Path 2: chi(83) = -chi(1) by oddness (83 = 84 - 1)
        assert chi[83] == -1

        # Path 3: support is symmetric under r -> 2P - r
        support = set(character_support(chi))
        for r in support:
            assert (84 - r) % 84 in support

    def test_density_obstruction_three_algebras(self):
        """Projection obstruction holds for c in {2, 7, 13, 25}."""
        for c in [2.0, 7.0, 13.0, 25.0]:
            obs = projection_obstruction_check(
                poincare_sphere(), c_val=c, max_terms=30
            )
            assert obs['shadow_density'] > 10 * obs['z_hat_density']
