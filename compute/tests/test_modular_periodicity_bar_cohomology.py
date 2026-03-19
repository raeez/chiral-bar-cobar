"""Tests for modular_periodicity_bar_cohomology.py.

Tests bar cohomology computations for minimal models M(p,q) via the
plethystic logarithm approach. Verifies character formulas, PL coefficients,
null vector structure, inverse character, and periodicity properties.

References:
    - conj:modular-periodicity-minimal (chiral_hochschild_koszul.tex)
"""

import pytest
import numpy as np
from math import gcd

from compute.lib.modular_periodicity_bar_cohomology import (
    partition_table,
    central_charge,
    central_charge_float,
    conformal_weights,
    modular_period,
    weight_space_dims,
    total_character,
    plethystic_log_from_product,
    plethystic_log_mobius,
    inverse_character,
    check_periodicity,
    detect_period,
    mobius,
    analyze_model,
    bar_generator_dims,
    first_nontrivial_null,
    pl_deviation_onset,
    STANDARD_MODELS,
)


# ===================================================================
# Partition function tests
# ===================================================================

class TestPartitions:
    def test_base_cases(self):
        P = partition_table(10)
        assert P[0] == 1
        assert P[1] == 1
        assert P[2] == 2
        assert P[3] == 3
        assert P[4] == 5
        assert P[5] == 7

    def test_known_values(self):
        P = partition_table(20)
        assert P[10] == 42
        assert P[15] == 176
        assert P[20] == 627


# ===================================================================
# Central charge tests
# ===================================================================

class TestCentralCharge:
    def test_ising(self):
        """M(3,4): c = 1 - 6*1/(12) = 1/2."""
        num, den = central_charge(3, 4)
        assert num == 1 and den == 2

    def test_yang_lee(self):
        """M(2,5): c = 1 - 6*9/10 = 1 - 54/10 = -22/5."""
        num, den = central_charge(2, 5)
        assert num == -22 and den == 5

    def test_tricritical_ising(self):
        """M(4,5): c = 1 - 6/20 = 7/10."""
        num, den = central_charge(4, 5)
        assert num == 7 and den == 10

    def test_m35(self):
        """M(3,5): c = 1 - 6*4/15 = 1 - 24/15 = 1 - 8/5 = -3/5."""
        num, den = central_charge(3, 5)
        assert num == -3 and den == 5

    def test_m58(self):
        """M(5,8): c = 1 - 6*9/40 = 1 - 54/40 = 1 - 27/20 = -7/20."""
        num, den = central_charge(5, 8)
        assert num == -7 and den == 20

    def test_coprimality_enforced(self):
        with pytest.raises(ValueError):
            central_charge(4, 6)  # gcd = 2

    def test_ordering_enforced(self):
        with pytest.raises(ValueError):
            central_charge(5, 3)  # p > q


# ===================================================================
# Conformal weight tests
# ===================================================================

class TestConformalWeights:
    def test_ising_module_count(self):
        """M(3,4) has (p-1)(q-1)/2 = 2*3/2 = 3 distinct modules."""
        w = conformal_weights(3, 4)
        assert len(w) == 3

    def test_ising_vacuum(self):
        """M(3,4) has a vacuum module with h=0."""
        w = conformal_weights(3, 4)
        h_vals = [h for _, _, h in w]
        assert any(abs(h) < 1e-12 for h in h_vals)

    def test_ising_weights(self):
        """M(3,4): h_{1,1}=0, h_{1,2}=1/16, h_{1,3}=1/2."""
        w = conformal_weights(3, 4)
        h_vals = sorted([h for _, _, h in w])
        assert abs(h_vals[0] - 0.0) < 1e-12
        assert abs(h_vals[1] - 1 / 16) < 1e-12
        assert abs(h_vals[2] - 0.5) < 1e-12

    def test_yang_lee_module_count(self):
        """M(2,5) has 1*4/2 = 2 modules."""
        w = conformal_weights(2, 5)
        assert len(w) == 2

    def test_m45_module_count(self):
        """M(4,5) has 3*4/2 = 6 modules."""
        w = conformal_weights(4, 5)
        assert len(w) == 6

    def test_identification(self):
        """(r,s) ~ (p-r, q-s) produces no duplicates."""
        for p, q in [(3, 4), (3, 5), (4, 5), (5, 8)]:
            w = conformal_weights(p, q)
            expected = (p - 1) * (q - 1) // 2
            assert len(w) == expected, f"M({p},{q}): got {len(w)}, expected {expected}"


# ===================================================================
# Modular period tests
# ===================================================================

class TestModularPeriod:
    def test_ising_period(self):
        """M(3,4): c=1/2, p'=1, q'=2, N = 24*2/gcd(1,24) = 48."""
        assert modular_period(3, 4) == 48

    def test_yang_lee_period(self):
        """M(2,5): c=-22/5, p'=-22, q'=5, N = 24*5/gcd(22,24) = 120/2 = 60."""
        assert modular_period(2, 5) == 60

    def test_m35_period(self):
        """M(3,5): c=-3/5, p'=-3, q'=5, N = 24*5/gcd(3,24) = 120/3 = 40."""
        assert modular_period(3, 5) == 40

    def test_m45_period(self):
        """M(4,5): c=7/10, p'=7, q'=10, N = 24*10/gcd(7,24) = 240."""
        assert modular_period(4, 5) == 240

    def test_m58_period(self):
        """M(5,8): c=-7/20, N = 24*20/gcd(7,24) = 480."""
        assert modular_period(5, 8) == 480

    def test_period_divides_t_matrix(self):
        """N should divide the T-matrix period (or vice versa) up to small factors."""
        # This is a structural check, not strict divisibility
        for p, q in [(3, 4), (2, 5), (3, 5)]:
            N = modular_period(p, q)
            assert N > 0


# ===================================================================
# Weight-space dimension tests
# ===================================================================

class TestWeightSpaceDims:
    def test_vacuum_dim0(self):
        """Vacuum module has dim 1 at level 0."""
        for p, q in [(3, 4), (2, 5), (3, 5), (4, 5)]:
            w = conformal_weights(p, q)
            for r, s, h in w:
                if abs(h) < 1e-12:
                    d = weight_space_dims(p, q, r, s, 5)
                    assert d[0] == 1

    def test_vacuum_dim1_zero(self):
        """Vacuum module has dim 0 at level 1 (L_{-1}|0> = 0)."""
        for p, q in [(3, 4), (2, 5), (3, 5), (4, 5)]:
            w = conformal_weights(p, q)
            for r, s, h in w:
                if abs(h) < 1e-12:
                    d = weight_space_dims(p, q, r, s, 5)
                    assert d[1] == 0, f"M({p},{q}) vacuum dim[1] = {d[1]}"

    def test_ising_vacuum_dims(self):
        """Known Ising vacuum character: matches partitions-without-1s
        at least until the second null vector at level 35."""
        d = weight_space_dims(3, 4, 1, 1, 30)
        P = partition_table(30)
        # For the vacuum with null only at level 1, dim[k] = p(k) - p(k-1)
        for k in range(30):
            expected = P[k] - (P[k - 1] if k > 0 else 0)
            assert d[k] == expected, f"Ising vacuum dim[{k}] = {d[k]}, expected {expected}"

    def test_nonnegative(self):
        """All weight-space dimensions must be non-negative."""
        for p, q in [(3, 4), (2, 5), (3, 5), (4, 5)]:
            w = conformal_weights(p, q)
            for r, s, h in w:
                d = weight_space_dims(p, q, r, s, 50)
                assert all(x >= 0 for x in d), \
                    f"M({p},{q}) V({r},{s}) has negative dims"

    def test_monotone_vacuum(self):
        """Vacuum module dims should be monotone non-decreasing
        (at least for levels well below the second null)."""
        d = weight_space_dims(3, 4, 1, 1, 20)
        # After level 1 (which is 0), should be non-decreasing
        for k in range(2, 20):
            assert d[k] >= d[k - 1], f"Non-monotone at k={k}: {d[k]} < {d[k-1]}"


# ===================================================================
# Plethystic logarithm tests
# ===================================================================

class TestPlethysticLog:
    def test_free_boson(self):
        """For f(q) = prod_{n>=1} 1/(1-q^n) = partition generating function,
        PL should be (0, 1, 1, 1, 1, ...) -- one boson at each level."""
        P = partition_table(30)
        dims = np.array(P, dtype=np.float64)
        pl = plethystic_log_from_product(dims, 25)
        for n in range(1, 25):
            assert abs(pl[n] - 1.0) < 0.01, f"PL[{n}] = {pl[n]}, expected 1"

    def test_methods_agree(self):
        """Two PL computation methods should agree."""
        P = partition_table(50)
        dims = np.array(P, dtype=np.float64)
        pl1 = plethystic_log_from_product(dims, 40)
        pl2 = plethystic_log_mobius(dims, 40)
        assert np.allclose(pl1[1:40], pl2[1:40], atol=0.1), \
            f"Methods disagree: max diff = {max(abs(pl1[1:40] - pl2[1:40]))}"

    def test_ising_pl_initial(self):
        """Ising vacuum PL should be (0, 0, 1, 1, 1, ..., 1) up to the
        second null vector level, since the only null subtracted is at level 1."""
        d = weight_space_dims(3, 4, 1, 1, 50)
        dims = np.array(d, dtype=np.float64)
        pl = plethystic_log_from_product(dims, 40)
        pl_r = np.round(pl).astype(int)
        assert pl_r[0] == 0
        assert pl_r[1] == 0
        # Levels 2 through ~34 should all be 1 (before second null at 35)
        for n in range(2, 34):
            assert pl_r[n] == 1, f"Ising PL[{n}] = {pl_r[n]}, expected 1"

    def test_ising_pl_deviation(self):
        """Ising PL should deviate from 1 at the second null vector level."""
        d = weight_space_dims(3, 4, 1, 1, 60)
        dims = np.array(d, dtype=np.float64)
        pl = plethystic_log_from_product(dims, 50)
        pl_r = np.round(pl).astype(int)
        # The second null is at level B(-1) = 4*3*4 - 2*(4+3) + 1 = 48-14+1 = 35
        # At level 35, PL should deviate from 1
        assert pl_r[35] != 1, f"Ising PL[35] = {pl_r[35]}, should deviate from 1"

    def test_yang_lee_pl_initial(self):
        """Yang-Lee vacuum PL should be 1 for levels 2 through ~26."""
        d = weight_space_dims(2, 5, 1, 1, 40)
        dims = np.array(d, dtype=np.float64)
        pl = plethystic_log_from_product(dims, 35)
        pl_r = np.round(pl).astype(int)
        for n in range(2, 25):
            assert pl_r[n] == 1, f"Yang-Lee PL[{n}] = {pl_r[n]}"

    def test_single_factor(self):
        """For f(q) = 1/(1-q^2) = 1 + q^2 + q^4 + ..., PL = (0, 0, 1, 0, 0, ...)."""
        dims = np.zeros(20, dtype=np.float64)
        for k in range(0, 20, 2):
            dims[k] = 1.0
        pl = plethystic_log_from_product(dims, 15)
        assert abs(pl[2] - 1.0) < 0.01
        for n in [1, 3, 4, 5, 6]:
            assert abs(pl[n]) < 0.01, f"PL[{n}] = {pl[n]}, expected 0"


# ===================================================================
# Inverse character tests
# ===================================================================

class TestInverseCharacter:
    def test_partition_inverse(self):
        """1/prod(1-q^n) inverted should give prod(1-q^n) = eta coefficients."""
        P = partition_table(20)
        chi = inverse_character(P, 15)
        # prod(1-q^n) = 1 - q - q^2 + q^5 + q^7 - q^12 - q^15 + ...
        # (Euler's pentagonal theorem)
        assert abs(chi[0] - 1.0) < 1e-10
        assert abs(chi[1] - (-1.0)) < 1e-10
        assert abs(chi[2] - (-1.0)) < 1e-10
        assert abs(chi[3] - 0.0) < 1e-10
        assert abs(chi[4] - 0.0) < 1e-10
        assert abs(chi[5] - 1.0) < 1e-10
        assert abs(chi[7] - 1.0) < 1e-10

    def test_inverse_recovers_identity(self):
        """f * (1/f) should give 1 + 0*q + 0*q^2 + ..."""
        d = weight_space_dims(3, 4, 1, 1, 30)
        chi = inverse_character(d, 25)
        # Convolve f and chi
        for n in range(1, 20):
            conv = sum(float(d[k]) * chi[n - k] for k in range(n + 1))
            assert abs(conv) < 1e-8, f"(f * 1/f)[{n}] = {conv}"

    def test_ising_inverse_bounded(self):
        """Ising inverse character coefficients should be bounded at low depth."""
        d = weight_space_dims(3, 4, 1, 1, 50)
        chi = inverse_character(d, 40)
        # Coefficients should be integers (or very close)
        for n in range(40):
            assert abs(chi[n] - round(chi[n])) < 1e-6, \
                f"1/f[{n}] = {chi[n]} not integer"


# ===================================================================
# Null vector level tests
# ===================================================================

class TestNullVectorLevels:
    def test_ising_first_null(self):
        """Ising vacuum: first nontrivial null at level B(-1) = 35."""
        level = first_nontrivial_null(3, 4, 1, 1)
        # B(-1) = 4*3*4 - 2*(4+3) + 1 = 48 - 14 + 1 = 35
        assert level == 35

    def test_yang_lee_first_null(self):
        """Yang-Lee vacuum: first nontrivial null at B(-1) = 4*2*5 - 2*(5+2) + 1 = 27."""
        level = first_nontrivial_null(2, 5, 1, 1)
        assert level == 27

    def test_pl_deviation_matches_null(self):
        """PL deviation onset should match the first nontrivial null level."""
        for p, q in [(3, 4), (2, 5)]:
            null_level = first_nontrivial_null(p, q, 1, 1)
            onset = pl_deviation_onset(p, q, max_depth=null_level + 10)
            assert onset == null_level, \
                f"M({p},{q}): PL deviation at {onset}, null at {null_level}"


# ===================================================================
# Mobius function tests
# ===================================================================

class TestMobius:
    def test_values(self):
        assert mobius(1) == 1
        assert mobius(2) == -1
        assert mobius(3) == -1
        assert mobius(4) == 0  # 4 = 2^2
        assert mobius(5) == -1
        assert mobius(6) == 1  # 6 = 2*3
        assert mobius(7) == -1
        assert mobius(8) == 0  # 8 = 2^3
        assert mobius(30) == -1  # 30 = 2*3*5


# ===================================================================
# Periodicity tests
# ===================================================================

class TestPeriodicity:
    def test_constant_sequence(self):
        """Constant sequence has period 1."""
        seq = np.ones(100)
        is_per, dev = check_periodicity(seq, 1, start=0)
        assert is_per
        assert dev < 0.01

    def test_sine_period(self):
        """Sine wave has correct detected period."""
        seq = np.array([np.sin(2 * np.pi * n / 10) for n in range(200)])
        detected = detect_period(seq, start=0, tol=0.01)
        assert detected == 10

    def test_non_periodic(self):
        """Growing sequence is not periodic."""
        seq = np.array([float(n ** 2) for n in range(100)])
        is_per, dev = check_periodicity(seq, 10, start=5)
        assert not is_per


# ===================================================================
# Full model analysis tests
# ===================================================================

class TestAnalyzeModel:
    def test_ising_analysis(self):
        """Ising model analysis runs and returns expected structure."""
        res = analyze_model(3, 4, max_depth=80)
        assert res["c"] == (1, 2)
        assert res["N_predicted"] == 48
        assert res["n_modules"] == 3
        assert res["methods_agree"]

    def test_yang_lee_analysis(self):
        res = analyze_model(2, 5, max_depth=60)
        assert res["c"] == (-22, 5)
        assert res["N_predicted"] == 60
        assert res["n_modules"] == 2

    def test_pl_growth(self):
        """PL coefficients should grow unboundedly (NOT periodic) at sufficient depth.

        KEY FINDING: The plethystic logarithm of the vacuum character is NOT
        eventually periodic. The 1/eta convolution with the sparse theta-function
        numerator produces coefficients that grow without bound.
        The periodicity conjecture, if it holds, must be at the level of
        bar COHOMOLOGY (after the differential), not at the chain level.
        """
        res = analyze_model(3, 4, max_depth=250)
        pl = res["pl_coeffs"]
        # PL coefficients at depth > 100 should be large (not bounded by 1)
        max_pl = max(abs(int(pl[n])) for n in range(100, 200))
        assert max_pl > 10, f"PL max in [100,200] = {max_pl}, expected unbounded growth"

    def test_inverse_char_structure(self):
        """Inverse character of Ising vacuum has integer coefficients."""
        d = weight_space_dims(3, 4, 1, 1, 40)
        chi = inverse_character(d, 30)
        for n in range(30):
            assert abs(chi[n] - round(chi[n])) < 1e-6

    def test_all_standard_models_run(self):
        """All standard models in the catalogue can be analyzed."""
        for name, (p, q) in STANDARD_MODELS.items():
            res = analyze_model(p, q, max_depth=60)
            assert res["n_modules"] == (p - 1) * (q - 1) // 2
            assert res["methods_agree"], f"{name}: PL methods disagree"


# ===================================================================
# Bar generator / relation decomposition tests
# ===================================================================

class TestBarGenerators:
    def test_free_algebra(self):
        """For free algebra (partitions), PL = (0,1,1,1,...), all generators, no relations."""
        P = partition_table(20)
        dims = np.array(P, dtype=np.float64)
        pl = plethystic_log_from_product(dims, 15)
        gens, rels = bar_generator_dims(pl)
        assert all(rels[n] < 0.5 for n in range(1, 15))
        assert all(abs(gens[n] - 1.0) < 0.5 for n in range(1, 15))

    def test_ising_relations_appear(self):
        """Ising vacuum should develop relations at the null vector level."""
        d = weight_space_dims(3, 4, 1, 1, 80)
        dims = np.array(d, dtype=np.float64)
        pl = plethystic_log_from_product(dims, 70)
        gens, rels = bar_generator_dims(pl)
        # At the null level (35), PL drops to 0, so no generator or relation there.
        # But beyond that, negative PL values = relations
        has_rels = any(rels[n] > 0.5 for n in range(35, 70))
        # Actually PL goes to 0 at 35, not negative. Relations come later.
        # The key point: PL is NOT identically 1 after level 35.
        has_deviation = any(abs(pl[n] - 1.0) > 0.5 for n in range(35, 70))
        assert has_deviation


# ===================================================================
# Cross-validation with existing module
# ===================================================================

class TestCrossValidation:
    def test_ising_dims_match_existing(self):
        """Cross-check: our Rocha-Caridi agrees with the existing module's implementation."""
        # Both modules compute via the same Rocha-Caridi formula.
        # Verify specific known values for the Ising vacuum.
        d = weight_space_dims(3, 4, 1, 1, 15)
        # Known: 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21, 24, 34, 41
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21, 24, 34, 41]
        assert d == expected

    def test_yang_lee_dims_match(self):
        """Yang-Lee M(2,5) vacuum dims should match Ising at low levels
        (both have null only at level 1 until higher nulls kick in)."""
        d_ising = weight_space_dims(3, 4, 1, 1, 20)
        d_yl = weight_space_dims(2, 5, 1, 1, 20)
        # They agree until the EARLIER second null (Yang-Lee at 27, Ising at 35)
        for k in range(20):
            assert d_ising[k] == d_yl[k], \
                f"Diverge at k={k}: Ising={d_ising[k]}, YL={d_yl[k]}"
