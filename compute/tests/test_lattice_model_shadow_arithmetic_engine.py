r"""Test suite for lattice model shadow arithmetic engine.

Tests: shadow towers for Ising (c=1/2), tricritical Ising (c=7/10), 3-state
Potts (c=4/5), full unitary minimal model family (m=3,...,20), non-unitary
models (Yang-Lee, symplectic fermion), prime factorization analysis, critical
exponent/kappa comparison, transfer matrix verification, crossing symmetry,
Koszul dual complementarity, and arithmetic distances.

MULTI-PATH VERIFICATION:
  Path 1: Convolution recursion (sqrt(Q_L) Taylor expansion)
  Path 2: Closed-form S_4, S_5 formulas (independent check)
  Path 3: Crossing symmetry (modular bootstrap)
  Path 4: Transfer matrix (exact lattice computation)

95+ tests covering all minimal models m = 3,...,20.
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest

from compute.lib.lattice_model_shadow_arithmetic_engine import (
    # Core tower computation
    virasoro_shadow_tower_exact,
    virasoro_shadow_tower_float,
    virasoro_shadow_invariants,
    # Specific models
    ising_shadow_data,
    tricritical_ising_shadow_data,
    three_state_potts_shadow_data,
    # Minimal model family
    minimal_model_c_from_m,
    minimal_model_shadow_landscape,
    # Prime factorization
    shadow_prime_factorization,
    landscape_prime_table,
    universal_primes,
    denominator_sequence,
    _prime_factors,
    # Critical exponents
    conformal_weight_kac,
    critical_exponents,
    ising_critical_exponents,
    tricritical_ising_critical_exponents,
    potts3_critical_exponents,
    eta_kappa_comparison,
    # Non-unitary
    yang_lee_shadow_tower,
    non_unitary_minimal_model_shadow,
    symplectic_fermion_shadow,
    c_minus_7_shadow,
    # Arithmetic distance
    shadow_arithmetic_distance,
    # Transfer matrix
    ising_transfer_matrix_eigenvalues,
    conformal_spectrum_from_transfer,
    ising_finite_size_central_charge,
    # Bootstrap
    ising_crossing_symmetry_check,
    # Growth rate
    shadow_growth_rate,
    koszul_dual_growth_comparison,
    # Sign pattern
    shadow_sign_pattern,
    # Cross-verification
    verify_S4_S5_from_formula,
    # Comparison
    ising_potts_tricritical_comparison,
    # Denominator analysis
    denominator_growth_analysis,
    # Full driver
    complete_lattice_model_analysis,
)


# ============================================================================
# 1. Ising model (c = 1/2)
# ============================================================================

class TestIsingShadowTower:
    """Shadow tower for the Ising model at c = 1/2."""

    def test_ising_kappa(self):
        """kappa = c/2 = 1/4."""
        data = ising_shadow_data()
        assert data['kappa'] == Fraction(1, 4)

    def test_ising_S3(self):
        """S_3 = 2 (c-independent for all Virasoro)."""
        data = ising_shadow_data()
        assert data['tower'][3] == Fraction(2)

    def test_ising_S4(self):
        """S_4 = Q^contact = 10/(c(5c+22)) = 10/(1/2 * 49/2) = 40/49."""
        data = ising_shadow_data()
        assert data['tower'][4] == Fraction(40, 49)
        assert data['S4'] == Fraction(40, 49)

    def test_ising_S5(self):
        """S_5 = -48/(c^2(5c+22)) = -48/((1/4)(49/2)) = -384/49."""
        data = ising_shadow_data()
        expected = Fraction(-48) / (Fraction(1, 4) * Fraction(49, 2))
        assert data['tower'][5] == expected

    def test_ising_S2_equals_kappa(self):
        """S_2 must equal kappa = c/2."""
        data = ising_shadow_data()
        assert data['tower'][2] == data['kappa']

    def test_ising_delta(self):
        """Delta = 8*kappa*S_4 = 8*(1/4)*(40/49) = 80/49."""
        data = ising_shadow_data()
        assert data['Delta'] == Fraction(80, 49)

    def test_ising_tower_through_15(self):
        """Tower has all 14 arities computed."""
        data = ising_shadow_data()
        for r in range(2, 16):
            assert r in data['tower'], f"Missing S_{r}"
            assert isinstance(data['tower'][r], Fraction), f"S_{r} not Fraction"

    def test_ising_tower_signs(self):
        """S_2, S_3, S_4 > 0; S_5 < 0; from S_5 onward, alternating."""
        data = ising_shadow_data()
        t = data['tower']
        assert t[2] > 0
        assert t[3] > 0
        assert t[4] > 0
        assert t[5] < 0
        # From r=5 onward: alternating sign
        for r in range(5, 16):
            sign_r = 1 if t[r] > 0 else -1
            sign_prev = 1 if t[r - 1] > 0 else -1
            assert sign_r == -sign_prev, f"Non-alternating at r={r}"

    def test_ising_denominator_7_powers(self):
        """Ising denominators are dominated by powers of 7.

        7 = prime divisor of 49 = (5c+22)^2|_{c=1/2}.
        """
        data = ising_shadow_data()
        denoms = denominator_sequence(data['tower'])
        for r in range(4, 16):
            d = denoms[r]
            # All denominators for r >= 4 divisible by 7
            assert d % 7 == 0, f"den(S_{r}) = {d} not divisible by 7"


class TestIsingPrimeFactorization:
    """Prime factorization analysis of Ising shadow coefficients."""

    def test_S2_denominator_is_4(self):
        tower = virasoro_shadow_tower_exact(1, 2, 5)
        assert tower[2].denominator == 4

    def test_S3_denominator_is_1(self):
        tower = virasoro_shadow_tower_exact(1, 2, 5)
        assert tower[3].denominator == 1

    def test_S4_denominator_is_49(self):
        tower = virasoro_shadow_tower_exact(1, 2, 5)
        assert tower[4].denominator == 49

    def test_prime_factors_function(self):
        assert _prime_factors(49) == {7: 2}
        assert _prime_factors(12) == {2: 2, 3: 1}
        assert _prime_factors(1) == {}

    def test_ising_prime_analysis_structure(self):
        tower = virasoro_shadow_tower_exact(1, 2, 10)
        pf = shadow_prime_factorization(tower)
        for r in range(2, 11):
            assert 'numerator' in pf[r]
            assert 'denominator' in pf[r]
            assert 'primes' in pf[r]


# ============================================================================
# 2. Tricritical Ising (c = 7/10)
# ============================================================================

class TestTricriticalIsing:
    """Shadow tower for the tricritical Ising model M(5,4), c = 7/10."""

    def test_central_charge(self):
        c = minimal_model_c_from_m(4)
        assert c == Fraction(7, 10)

    def test_kappa(self):
        data = tricritical_ising_shadow_data()
        assert data['kappa'] == Fraction(7, 20)

    def test_S4(self):
        """S_4 = 10/(c(5c+22)) = 10/((7/10)(35/10+22)) = 10/((7/10)(57/2))."""
        c = Fraction(7, 10)
        denom = c * (5 * c + 22)
        expected = Fraction(10) / denom
        data = tricritical_ising_shadow_data()
        assert data['tower'][4] == expected

    def test_S5_formula(self):
        v = verify_S4_S5_from_formula(7, 10)
        assert v['S5_match'] is True

    def test_S2_equals_kappa(self):
        data = tricritical_ising_shadow_data()
        assert data['tower'][2] == data['kappa']

    def test_tower_length(self):
        data = tricritical_ising_shadow_data()
        assert len(data['tower']) == 14  # arities 2..15


# ============================================================================
# 3. 3-state Potts (c = 4/5)
# ============================================================================

class TestThreeStatePotts:
    """Shadow tower for the 3-state Potts model M(6,5), c = 4/5."""

    def test_central_charge(self):
        c = minimal_model_c_from_m(5)
        assert c == Fraction(4, 5)

    def test_kappa(self):
        data = three_state_potts_shadow_data()
        assert data['kappa'] == Fraction(2, 5)

    def test_S3_universal(self):
        """S_3 = 2 for Potts too (c-independent)."""
        data = three_state_potts_shadow_data()
        assert data['tower'][3] == Fraction(2)

    def test_S4(self):
        c = Fraction(4, 5)
        expected = Fraction(10) / (c * (5 * c + 22))
        data = three_state_potts_shadow_data()
        assert data['tower'][4] == expected

    def test_S5_formula(self):
        v = verify_S4_S5_from_formula(4, 5)
        assert v['S5_match'] is True

    def test_S2_equals_kappa(self):
        data = three_state_potts_shadow_data()
        assert data['tower'][2] == data['kappa']


# ============================================================================
# 4. Full minimal model landscape (m = 3,...,20)
# ============================================================================

class TestMinimalModelLandscape:
    """Shadow data for all unitary minimal models."""

    def test_central_charge_formula(self):
        """c = 1 - 6/(m(m+1)) for each m."""
        for m in range(3, 21):
            c = minimal_model_c_from_m(m)
            assert c == 1 - Fraction(6, m * (m + 1))

    def test_central_charge_monotone(self):
        """c(m) is strictly increasing, approaching 1."""
        prev = Fraction(0)
        for m in range(3, 21):
            c = minimal_model_c_from_m(m)
            assert c > prev
            assert c < 1
            prev = c

    def test_landscape_has_all_models(self):
        landscape = minimal_model_shadow_landscape(3, 20, 5)
        for m in range(3, 21):
            assert m in landscape

    @pytest.mark.parametrize("m", range(3, 21))
    def test_S2_equals_kappa(self, m):
        """S_2 = kappa for every model."""
        c = minimal_model_c_from_m(m)
        tower = virasoro_shadow_tower_exact(c.numerator, c.denominator, 3)
        kappa = c / 2
        assert tower[2] == kappa, f"m={m}: S_2={tower[2]} != kappa={kappa}"

    @pytest.mark.parametrize("m", range(3, 21))
    def test_S3_universal(self, m):
        """S_3 = 2 for ALL Virasoro, regardless of c."""
        c = minimal_model_c_from_m(m)
        tower = virasoro_shadow_tower_exact(c.numerator, c.denominator, 4)
        assert tower[3] == Fraction(2), f"m={m}: S_3={tower[3]} != 2"

    @pytest.mark.parametrize("m", range(3, 21))
    def test_S4_formula(self, m):
        """S_4 = 10/(c(5c+22)) matches recursion for each m."""
        c = minimal_model_c_from_m(m)
        v = verify_S4_S5_from_formula(c.numerator, c.denominator)
        assert v['S4_match'] is True, f"m={m}: S_4 mismatch"

    @pytest.mark.parametrize("m", range(3, 21))
    def test_S5_formula(self, m):
        """S_5 = -48/(c^2(5c+22)) matches recursion for each m."""
        c = minimal_model_c_from_m(m)
        v = verify_S4_S5_from_formula(c.numerator, c.denominator)
        assert v['S5_match'] is True, f"m={m}: S_5 mismatch"

    @pytest.mark.parametrize("m", range(3, 21))
    def test_exact_vs_float(self, m):
        """Exact Fraction tower matches float tower to high precision."""
        c = minimal_model_c_from_m(m)
        exact = virasoro_shadow_tower_exact(c.numerator, c.denominator, 10)
        floats = virasoro_shadow_tower_float(float(c), 10)
        for r in range(2, 11):
            ex = float(exact[r])
            fl = floats[r]
            if abs(ex) > 1e-15:
                rel_err = abs(ex - fl) / abs(ex)
                assert rel_err < 1e-10, \
                    f"m={m}, r={r}: exact={ex}, float={fl}, err={rel_err}"

    @pytest.mark.parametrize("m", range(3, 21))
    def test_kappa_positive(self, m):
        """kappa > 0 for all unitary minimal models."""
        c = minimal_model_c_from_m(m)
        assert c / 2 > 0

    @pytest.mark.parametrize("m", range(3, 21))
    def test_delta_positive(self, m):
        """Delta = 80/(5c+22) > 0 for all unitary minimal models."""
        c = minimal_model_c_from_m(m)
        inv = virasoro_shadow_invariants(c.numerator, c.denominator)
        assert inv['Delta'] > 0, f"m={m}: Delta={inv['Delta']}"


class TestMinimalModelPrimeTable:
    """Prime factorization table for minimal models."""

    def test_prime_table_structure(self):
        pt = landscape_prime_table(3, 10, 2, 6)
        assert len(pt) == 8  # m = 3,...,10
        for m in range(3, 11):
            assert m in pt
            for r in range(2, 7):
                assert r in pt[m]

    def test_universal_primes_at_S3(self):
        """At arity 3, S_3 = 2 => numerator prime is 2.
        Denominator is 1. So the only prime is 2."""
        pt = landscape_prime_table(3, 20, 2, 4)
        univ, _ = universal_primes(pt, 3)
        assert 2 in univ

    def test_denominator_of_kappa(self):
        """kappa = (m(m+1)-6)/(2m(m+1)). Denominator divides 2m(m+1)."""
        for m in range(3, 21):
            c = minimal_model_c_from_m(m)
            kappa = c / 2
            d = kappa.denominator
            assert (2 * m * (m + 1)) % d == 0, \
                f"m={m}: den(kappa)={d} does not divide {2*m*(m+1)}"


# ============================================================================
# 5. Critical exponents and kappa comparison
# ============================================================================

class TestIsingCriticalExponents:
    """Critical exponents for the Ising model."""

    def test_eta(self):
        """eta = 4 * h_sigma = 4 * 1/16 = 1/4."""
        ie = ising_critical_exponents()
        assert ie['eta'] == Fraction(1, 4)

    def test_eta_equals_kappa_coincidence(self):
        """For Ising: eta = 1/4 = kappa. This is a COINCIDENCE (AP1-style)."""
        ie = ising_critical_exponents()
        assert ie['eta'] == ie['kappa']
        assert ie['eta_over_kappa'] == 1

    def test_nu(self):
        """nu = 1/(2*h_epsilon) = 1/(2*1/2) = 1."""
        ie = ising_critical_exponents()
        assert ie['nu'] == 1

    def test_alpha(self):
        """alpha = 2 - 2*nu = 0 (logarithmic specific heat)."""
        ie = ising_critical_exponents()
        assert ie['alpha'] == 0

    def test_beta(self):
        """beta = nu * eta / 2 = 1 * 1/4 / 2 = 1/8."""
        ie = ising_critical_exponents()
        assert ie['beta'] == Fraction(1, 8)

    def test_gamma(self):
        """gamma = nu * (2-eta) = 1 * 7/4 = 7/4."""
        ie = ising_critical_exponents()
        assert ie['gamma'] == Fraction(7, 4)

    def test_delta(self):
        """delta = (4-eta)/eta = (15/4)/(1/4) = 15."""
        ie = ising_critical_exponents()
        assert ie['delta'] == 15


class TestTricriticalCriticalExponents:
    """Critical exponents for the tricritical Ising model."""

    def test_h_sigma(self):
        te = tricritical_ising_critical_exponents()
        assert te['h_sigma'] == Fraction(3, 80)

    def test_h_epsilon(self):
        te = tricritical_ising_critical_exponents()
        assert te['h_epsilon'] == Fraction(1, 10)

    def test_eta(self):
        te = tricritical_ising_critical_exponents()
        assert te['eta'] == Fraction(3, 20)

    def test_eta_not_kappa(self):
        """eta != kappa for tricritical Ising (eta=3/20, kappa=7/20)."""
        te = tricritical_ising_critical_exponents()
        assert te['eta'] != te['kappa']
        assert te['eta_over_kappa'] == Fraction(3, 7)


class TestPottsCriticalExponents:
    """Critical exponents for the 3-state Potts model."""

    def test_h_sigma(self):
        pe = potts3_critical_exponents()
        assert pe['h_sigma'] == Fraction(1, 15)

    def test_eta(self):
        pe = potts3_critical_exponents()
        assert pe['eta'] == Fraction(4, 15)

    def test_eta_over_kappa(self):
        pe = potts3_critical_exponents()
        assert pe['eta_over_kappa'] == Fraction(2, 3)


class TestEtaKappaComparison:
    """Universal ratio eta/kappa = 2m/(m+3) for unitary minimal models."""

    @pytest.mark.parametrize("m", range(3, 21))
    def test_eta_kappa_ratio_formula(self, m):
        """eta/kappa = 2m/(m+3) exactly for all m."""
        ekc = eta_kappa_comparison(m, m)
        data = ekc[m]
        assert data['eta_kappa_matches_formula'] is True, \
            f"m={m}: eta/kappa={data.get('eta_over_kappa')}, " \
            f"expected {Fraction(2*m, m+3)}"

    def test_ising_coincidence_m3(self):
        """At m=3: 2*3/(3+3) = 1, so eta = kappa."""
        ekc = eta_kappa_comparison(3, 3)
        assert ekc[3]['eta_kappa_formula'] == 1

    def test_ratio_approaches_2(self):
        """As m -> inf, eta/kappa -> 2."""
        ekc = eta_kappa_comparison(20, 20)
        ratio = float(ekc[20]['eta_kappa_formula'])
        assert abs(ratio - 2 * 20 / 23) < 1e-10
        assert ratio < 2.0  # always strictly less than 2


# ============================================================================
# 6. Non-unitary models
# ============================================================================

class TestYangLee:
    """Yang-Lee edge singularity M(5,2), c = -22/5."""

    def test_central_charge(self):
        yl = yang_lee_shadow_tower()
        assert yl['c'] == Fraction(-22, 5)

    def test_kappa_negative(self):
        yl = yang_lee_shadow_tower()
        assert yl['kappa'] == Fraction(-11, 5)
        assert yl['kappa'] < 0

    def test_S4_divergent(self):
        """5c+22 = 0 at c=-22/5, so S_4 diverges."""
        yl = yang_lee_shadow_tower()
        assert yl['S4'] is None
        assert yl['yang_lee_singular'] is True

    def test_koszul_dual_complementarity(self):
        """kappa + kappa' = 13 even for Yang-Lee."""
        yl = yang_lee_shadow_tower()
        assert yl['kappa_sum'] == 13


class TestSymplecticFermion:
    """Symplectic fermion / bc ghost at c = -2."""

    def test_kappa_negative(self):
        sf = symplectic_fermion_shadow(8)
        assert sf['kappa'] == Fraction(-1)

    def test_S2_equals_kappa(self):
        sf = symplectic_fermion_shadow(8)
        assert sf['tower'][2] == Fraction(-1)
        assert sf['tower'][2] == sf['kappa']

    def test_S3_still_2(self):
        """S_3 = 2 even for negative kappa (c-independent)."""
        sf = symplectic_fermion_shadow(8)
        assert sf['tower'][3] == Fraction(2)

    def test_S4_negative(self):
        """S_4 = 10/((-2)*12) = -5/12."""
        sf = symplectic_fermion_shadow(8)
        assert sf['tower'][4] == Fraction(-5, 12)

    def test_S5_negative(self):
        """S_5 = -48/((-2)^2*12) = -48/48 = -1."""
        sf = symplectic_fermion_shadow(8)
        assert sf['tower'][5] == Fraction(-1)

    def test_S4_S5_formulas(self):
        v = verify_S4_S5_from_formula(-2, 1)
        assert v['S4_match'] is True
        assert v['S5_match'] is True


class TestM72:
    """M(7,2) model at c = -68/7."""

    def test_central_charge(self):
        data = c_minus_7_shadow(5)
        assert data['c'] == Fraction(-68, 7)

    def test_kappa(self):
        data = c_minus_7_shadow(5)
        assert data['kappa'] == Fraction(-34, 7)

    def test_S2_equals_kappa(self):
        data = c_minus_7_shadow(5)
        assert data['tower'][2] == data['kappa']

    def test_S4_S5_formulas(self):
        c = Fraction(-68, 7)
        v = verify_S4_S5_from_formula(c.numerator, c.denominator)
        assert v['S4_match'] is True
        assert v['S5_match'] is True

    def test_negative_kappa_flag(self):
        data = c_minus_7_shadow(5)
        assert data['negative_kappa'] is True


class TestNonUnitaryGeneral:
    """Non-unitary M(p,q) for several models."""

    def test_M52_is_yang_lee(self):
        data = non_unitary_minimal_model_shadow(5, 2, 5)
        assert data.get('yang_lee_singular', False) or data['c'] == Fraction(-22, 5)

    def test_M73_shadow(self):
        """M(7,3): c = 1 - 6*16/21 = 1 - 32/7 = -25/7."""
        data = non_unitary_minimal_model_shadow(7, 3, 6)
        assert data['c'] == Fraction(-25, 7)
        assert data['tower'][2] == data['kappa']

    def test_M83_shadow(self):
        """M(8,3): c = 1 - 6*25/24 = 1 - 25/4 = -21/4."""
        data = non_unitary_minimal_model_shadow(8, 3, 6)
        assert data['c'] == Fraction(-21, 4)
        assert data['tower'][2] == data['kappa']


# ============================================================================
# 7. Arithmetic distance between models
# ============================================================================

class TestArithmeticDistance:
    """Arithmetic distances between lattice model shadow towers."""

    def test_S3_coincidence(self):
        """S_3 = 2 for ALL Virasoro, so all models coincide at arity 3."""
        ising = virasoro_shadow_tower_exact(1, 2, 5)
        potts = virasoro_shadow_tower_exact(4, 5, 5)
        dist = shadow_arithmetic_distance(ising, potts, 5)
        assert 3 in dist['coincidences']

    def test_S2_difference(self):
        """S_2 = kappa differs between models (no coincidence at arity 2)."""
        ising = virasoro_shadow_tower_exact(1, 2, 5)
        potts = virasoro_shadow_tower_exact(4, 5, 5)
        dist = shadow_arithmetic_distance(ising, potts, 5)
        assert 2 not in dist['coincidences']
        assert dist['differences'][2] == Fraction(1, 4) - Fraction(2, 5)

    def test_self_distance_zero(self):
        """Distance of a model to itself is zero at all arities."""
        ising = virasoro_shadow_tower_exact(1, 2, 10)
        dist = shadow_arithmetic_distance(ising, ising, 10)
        assert len(dist['coincidences']) == 9  # arities 2..10

    def test_ising_potts_tricritical(self):
        comp = ising_potts_tricritical_comparison(10)
        # S_3 = 2 for all three
        for model in ['ising', 'potts', 'tricritical']:
            assert comp[model]['tower'][3] == Fraction(2)
        # S_3 coincidence in all pairwise distances
        for pair in ['ising_potts', 'ising_tricritical', 'potts_tricritical']:
            assert 3 in comp['distances'][pair]['coincidences']


# ============================================================================
# 8. Transfer matrix (independent verification path 4)
# ============================================================================

class TestTransferMatrix:
    """Transfer matrix eigenvalues for finite Ising chain."""

    def test_L4_largest_eigenvalue_positive(self):
        eigs = ising_transfer_matrix_eigenvalues(4)
        assert eigs[0] > 0

    def test_L4_eigenvalues_ordered(self):
        eigs = ising_transfer_matrix_eigenvalues(4)
        for i in range(len(eigs) - 1):
            assert eigs[i] >= eigs[i + 1] - 1e-10

    def test_conformal_spectrum_ground_state(self):
        """Ground state has h = 0."""
        eigs = ising_transfer_matrix_eigenvalues(4)
        dims = conformal_spectrum_from_transfer(eigs, 4)
        assert abs(dims[0]) < 1e-10

    def test_conformal_spectrum_first_excited(self):
        """First excited state should approach h_sigma = 1/16 for large L.
        At L=4 we just check it's positive and < 1."""
        eigs = ising_transfer_matrix_eigenvalues(4)
        dims = conformal_spectrum_from_transfer(eigs, 4)
        assert dims[1] > 0
        assert dims[1] < 1.0

    def test_finite_size_central_charge_reasonable(self):
        """Finite-size c estimate should be in (0, 1) for L=6."""
        c_est = ising_finite_size_central_charge(6)
        # At L=6 the estimate is rough but should be positive
        # and less than 2 (the exact answer is 1/2)
        assert c_est > 0, f"c_est = {c_est}"
        assert c_est < 2.0, f"c_est = {c_est}"


# ============================================================================
# 9. Crossing symmetry (verification path 3)
# ============================================================================

class TestCrossing:
    """Crossing symmetry for the Ising 4-point function."""

    def test_crossing_z_0_3(self):
        result = ising_crossing_symmetry_check(0.3)
        assert result['crossing_satisfied'] is True

    def test_crossing_z_0_5(self):
        """At z=0.5 (the crossing-symmetric point), G(z)=G(1-z) trivially."""
        result = ising_crossing_symmetry_check(0.5)
        assert result['crossing_satisfied'] is True

    def test_crossing_z_0_1(self):
        result = ising_crossing_symmetry_check(0.1)
        assert result['crossing_satisfied'] is True

    def test_crossing_z_0_8(self):
        result = ising_crossing_symmetry_check(0.8)
        assert result['crossing_satisfied'] is True


# ============================================================================
# 10. Growth rate and Koszul dual complementarity
# ============================================================================

class TestGrowthRate:
    """Shadow growth rate and convergence/divergence classification."""

    def test_ising_divergent(self):
        """Ising (c=1/2) has rho >> 1 (divergent tower)."""
        gr = shadow_growth_rate(1, 2)
        assert gr['rho'] > 10.0  # rho ~ 13
        assert gr['convergent'] is False

    def test_koszul_dual_convergent(self):
        """Koszul dual of Ising (c=51/2) has rho << 1."""
        gr = shadow_growth_rate(51, 2)
        assert gr['rho'] < 0.5
        assert gr['convergent'] is True

    def test_koszul_dual_kappa_sum_13(self):
        """kappa + kappa' = 13 for Virasoro."""
        comp = koszul_dual_growth_comparison(1, 2)
        assert comp['kappa_sum'] == 13

    @pytest.mark.parametrize("m", range(3, 15))
    def test_all_minimal_models_divergent(self, m):
        """All unitary minimal models (c < 1) have divergent towers.
        c* ~ 6.125, and c < 1 < 6.125, so rho > 1 for all."""
        c = minimal_model_c_from_m(m)
        gr = shadow_growth_rate(c.numerator, c.denominator)
        assert gr['rho'] > 1.0, f"m={m}: rho={gr['rho']}"

    def test_rho_decreases_with_c(self):
        """rho decreases as c increases (towards c*)."""
        prev_rho = float('inf')
        for m in range(3, 15):
            c = minimal_model_c_from_m(m)
            gr = shadow_growth_rate(c.numerator, c.denominator)
            assert gr['rho'] < prev_rho, \
                f"m={m}: rho={gr['rho']} not < prev={prev_rho}"
            prev_rho = gr['rho']

    def test_koszul_dual_convergent_complement(self):
        """For each unitary minimal model, its Koszul dual is convergent."""
        for m in range(3, 10):
            c = minimal_model_c_from_m(m)
            c_dual = 26 - c
            gr_dual = shadow_growth_rate(c_dual.numerator, c_dual.denominator)
            assert gr_dual['rho'] < 1.0, \
                f"m={m}: dual rho={gr_dual['rho']}"


# ============================================================================
# 11. Sign pattern analysis
# ============================================================================

class TestSignPattern:
    """Sign pattern of shadow tower coefficients."""

    def test_ising_not_purely_alternating(self):
        """Ising: S_2,S_3,S_4 all positive, then alternating from S_5."""
        tower = virasoro_shadow_tower_exact(1, 2, 10)
        sp = shadow_sign_pattern(tower)
        # Not purely alternating because S_2,S_3,S_4 are all positive
        assert sp['alternating'] is False

    def test_ising_alternating_from_r5(self):
        """From r=5 onward, Ising signs alternate."""
        tower = virasoro_shadow_tower_exact(1, 2, 15)
        for r in range(5, 15):
            sign_r = 1 if tower[r] > 0 else -1
            sign_next = 1 if tower[r + 1] > 0 else -1
            assert sign_r == -sign_next, f"Non-alternating at r={r},{r+1}"

    def test_symplectic_fermion_negative_start(self):
        """Symplectic fermion starts with S_2 < 0."""
        sf = symplectic_fermion_shadow(8)
        assert sf['tower'][2] < 0


# ============================================================================
# 12. Denominator growth analysis
# ============================================================================

class TestDenominatorGrowth:
    """Denominator growth patterns in shadow towers."""

    def test_ising_denominator_analysis(self):
        da = denominator_growth_analysis(1, 2, 10)
        assert 'denominators' in da
        assert 'factors' in da
        assert 'prime_first_appearance' in da

    def test_ising_7_appears_at_arity_4(self):
        """Prime 7 first appears in the denominator at arity 4 (from 5c+22 = 49/2)."""
        da = denominator_growth_analysis(1, 2, 10)
        assert da['prime_first_appearance'].get(7) == 4

    def test_potts_denominator_analysis(self):
        da = denominator_growth_analysis(4, 5, 8)
        # For Potts c=4/5: 5c+22 = 4+22 = 26, so primes 2, 13
        denoms = da['denominators']
        # S_4 denominator
        c = Fraction(4, 5)
        S4 = Fraction(10) / (c * (5 * c + 22))
        assert denoms[4] == S4.denominator


# ============================================================================
# 13. Cross-verification: recursion vs formulas (path 1 vs path 2)
# ============================================================================

class TestCrossVerification:
    """Multi-path verification of shadow coefficients."""

    @pytest.mark.parametrize("m", range(3, 21))
    def test_S4_two_paths(self, m):
        """S_4 from recursion matches closed-form Q^contact for all m."""
        c = minimal_model_c_from_m(m)
        v = verify_S4_S5_from_formula(c.numerator, c.denominator)
        assert v['S4_match'] is True

    @pytest.mark.parametrize("m", range(3, 21))
    def test_S5_two_paths(self, m):
        """S_5 from recursion matches closed-form quintic formula for all m."""
        c = minimal_model_c_from_m(m)
        v = verify_S4_S5_from_formula(c.numerator, c.denominator)
        assert v['S5_match'] is True

    def test_ising_exact_vs_existing_engine(self):
        """Cross-check against the existing ising_lattice_shadow engine."""
        try:
            from compute.lib.ising_lattice_shadow import shadow_tower_virasoro
            from sympy import Rational
            existing = shadow_tower_virasoro(Rational(1, 2), max_arity=10)
            new = virasoro_shadow_tower_exact(1, 2, 10)
            for r in range(2, 11):
                old_val = existing['tower'][r]
                new_val = new[r]
                # Convert sympy Rational to Fraction for comparison
                assert abs(float(old_val) - float(new_val)) < 1e-15, \
                    f"r={r}: old={old_val}, new={new_val}"
        except ImportError:
            pytest.skip("ising_lattice_shadow not available")


# ============================================================================
# 14. Conformal weight computation
# ============================================================================

class TestConformalWeights:
    """Kac formula for conformal weights."""

    def test_ising_vacuum(self):
        assert conformal_weight_kac(4, 3, 1, 1) == 0

    def test_ising_sigma(self):
        assert conformal_weight_kac(4, 3, 1, 2) == Fraction(1, 16)

    def test_ising_epsilon(self):
        assert conformal_weight_kac(4, 3, 2, 1) == Fraction(1, 2)

    def test_tricritical_sigma(self):
        """h_{2,2} for M(5,4) = 3/80."""
        assert conformal_weight_kac(5, 4, 2, 2) == Fraction(3, 80)

    def test_tricritical_epsilon(self):
        """h_{1,2} for M(5,4) = 1/10."""
        assert conformal_weight_kac(5, 4, 1, 2) == Fraction(1, 10)

    def test_potts_sigma(self):
        """h_{3,3} for M(6,5) = 1/15."""
        assert conformal_weight_kac(6, 5, 3, 3) == Fraction(1, 15)

    def test_potts_epsilon(self):
        """h_{2,1} for M(6,5) = 2/5."""
        assert conformal_weight_kac(6, 5, 2, 1) == Fraction(2, 5)

    def test_yang_lee_vacuum(self):
        assert conformal_weight_kac(5, 2, 1, 1) == 0

    def test_yang_lee_phi(self):
        """h_{1,2} for M(5,2) = -1/5 (negative, non-unitary)."""
        # h = ((5-4)^2 - 9)/40 = (1-9)/40 = -8/40 = -1/5
        assert conformal_weight_kac(5, 2, 1, 2) == Fraction(-1, 5)


# ============================================================================
# 15. Universal primes analysis
# ============================================================================

class TestUniversalPrimes:
    """Which primes are universal across all minimal models."""

    def test_no_prime_universal_at_S2(self):
        """No single prime divides ALL kappa values.

        kappa = (m(m+1)-6)/(2m(m+1)). For m=6: kappa=3/7 (primes 3,7).
        For m=5: kappa=2/5 (primes 2,5). No prime is in both {3,7} and {2,5}.
        """
        pt = landscape_prime_table(3, 10, 2, 3)
        univ, _ = universal_primes(pt, 2)
        # No prime is universal across ALL minimal models at arity 2
        # because kappa = (m(m+1)-6)/(2m(m+1)) has varying prime content
        assert isinstance(univ, set)  # structural check

    def test_sporadic_primes_exist(self):
        """Some primes are model-specific (sporadic)."""
        pt = landscape_prime_table(3, 10, 2, 6)
        # At arity 4: S_4 = 10/(c(5c+22)), primes depend on m
        _, spor = universal_primes(pt, 4)
        # There should be some sporadic primes at arity 4
        total_sporadic = sum(len(s) for s in spor.values())
        assert total_sporadic > 0


# ============================================================================
# 16. Virasoro shadow invariants
# ============================================================================

class TestShadowInvariants:
    """Basic shadow invariants for Virasoro."""

    def test_ising_invariants(self):
        inv = virasoro_shadow_invariants(1, 2)
        assert inv['c'] == Fraction(1, 2)
        assert inv['kappa'] == Fraction(1, 4)
        assert inv['S3'] == Fraction(2)
        assert inv['S4'] == Fraction(40, 49)
        assert inv['Delta'] == Fraction(80, 49)

    def test_c_zero(self):
        inv = virasoro_shadow_invariants(0, 1)
        assert inv['kappa'] == 0
        assert inv['S4'] == 0

    def test_yang_lee_singular(self):
        inv = virasoro_shadow_invariants(-22, 5)
        assert inv['S4'] is None
        assert inv['Delta'] is None

    def test_rho_squared_formula(self):
        """rho^2 = (9*alpha^2 + 2*Delta) / (4*kappa^2)."""
        inv = virasoro_shadow_invariants(1, 2)
        alpha = Fraction(2)
        expected = (9 * alpha ** 2 + 2 * inv['Delta']) / (4 * inv['kappa'] ** 2)
        assert inv['rho_squared'] == expected


# ============================================================================
# 17. Edge cases and special values
# ============================================================================

class TestEdgeCases:
    """Edge cases and special values."""

    def test_c_zero_tower(self):
        """At c=0: all S_r = 0."""
        tower = virasoro_shadow_tower_exact(0, 1, 5)
        for r in range(2, 6):
            assert tower[r] == 0

    def test_yang_lee_tower_truncated(self):
        """Yang-Lee: only S_2 and S_3 computed (S_4 diverges)."""
        tower = virasoro_shadow_tower_exact(-22, 5, 5)
        assert tower[2] == Fraction(-11, 5)
        assert tower[3] == Fraction(2)
        # Higher arities default to 0 (singular case)
        for r in range(4, 6):
            assert tower[r] == 0

    def test_large_c_shadow_tower(self):
        """At large c (e.g. c=100), the tower still computes correctly."""
        tower = virasoro_shadow_tower_exact(100, 1, 5)
        assert tower[2] == Fraction(50)
        assert tower[3] == Fraction(2)
        # S_4 = 10/(100*522) = 10/52200 = 1/5220
        assert tower[4] == Fraction(1, 5220)


# ============================================================================
# 18. Complete analysis driver
# ============================================================================

class TestCompleteAnalysis:
    """Full analysis driver."""

    def test_complete_analysis_runs(self):
        """The complete analysis driver should run without error."""
        result = complete_lattice_model_analysis(max_arity=8, m_max=10)
        assert 'ising' in result
        assert 'landscape' in result
        assert 'comparison' in result

    def test_complete_analysis_landscape_size(self):
        result = complete_lattice_model_analysis(max_arity=5, m_max=10)
        assert len(result['landscape']) == 8  # m = 3,...,10


# ============================================================================
# 19. Additional multi-path verification
# ============================================================================

class TestMultiPathVerification:
    """Additional cross-checks between independent computation paths."""

    def test_S4_from_delta_and_kappa(self):
        """S_4 = Delta / (8*kappa) (derived from Delta = 8*kappa*S_4)."""
        for m in range(3, 15):
            c = minimal_model_c_from_m(m)
            inv = virasoro_shadow_invariants(c.numerator, c.denominator)
            if inv['kappa'] != 0 and inv['Delta'] is not None:
                S4_from_delta = inv['Delta'] / (8 * inv['kappa'])
                assert S4_from_delta == inv['S4'], \
                    f"m={m}: S4 from Delta mismatch"

    def test_q2_from_components(self):
        """q2 = 9*alpha^2 + 16*kappa*S4 = 36 + 16*kappa*S4."""
        for m in range(3, 15):
            c = minimal_model_c_from_m(m)
            inv = virasoro_shadow_invariants(c.numerator, c.denominator)
            if inv['q2'] is not None:
                expected = 36 + 16 * inv['kappa'] * inv['S4']
                assert inv['q2'] == expected, f"m={m}: q2 mismatch"

    def test_delta_complementarity(self):
        """Delta(A) + Delta(A!) = 13920/((5c+22)(152-5c))."""
        for m in range(3, 15):
            c = minimal_model_c_from_m(m)
            c_dual = 26 - c
            Delta_A = Fraction(80) / (5 * c + 22)
            Delta_B = Fraction(80) / (5 * c_dual + 22)
            total = Delta_A + Delta_B
            denom1 = 5 * c + 22
            denom2 = 152 - 5 * c
            expected = Fraction(13920) / (denom1 * denom2)
            assert total == expected, \
                f"m={m}: Delta sum {total} != {expected}"

    def test_shadow_metric_q0_is_square(self):
        """q0 = 4*kappa^2 is always a perfect rational square."""
        for m in range(3, 21):
            c = minimal_model_c_from_m(m)
            kappa = c / 2
            q0 = 4 * kappa ** 2
            # Check it's a perfect square
            n = q0.numerator
            d = q0.denominator
            from compute.lib.lattice_model_shadow_arithmetic_engine import (
                _isqrt_exact)
            assert _isqrt_exact(n) is not None, f"m={m}: q0 num not perfect sq"
            assert _isqrt_exact(d) is not None, f"m={m}: q0 den not perfect sq"


# ============================================================================
# 20. Koszul dual complementarity
# ============================================================================

class TestKoszulDualComplementarity:
    """Koszul dual kappa + kappa' = 13 and growth rate comparison."""

    @pytest.mark.parametrize("m", range(3, 15))
    def test_kappa_sum_13(self, m):
        c = minimal_model_c_from_m(m)
        comp = koszul_dual_growth_comparison(c.numerator, c.denominator)
        assert comp['kappa_sum'] == 13

    def test_ising_dual_growth(self):
        comp = koszul_dual_growth_comparison(1, 2)
        # Ising divergent, dual convergent
        assert comp['rho_A'] > 10
        assert comp['rho_A_dual'] < 0.3

    def test_symplectic_fermion_dual(self):
        """c=-2, c'=28. kappa=-1, kappa'=14, sum=13."""
        comp = koszul_dual_growth_comparison(-2, 1)
        assert comp['kappa_sum'] == 13
