"""Tests for compute/lib/bar_cohomology_wn_universal_engine.py.

Universal bar cohomology H*(B(W_N)) for all N >= 2.

Verification paths:
  1. Cross-check vacuum dims against _wn_vacuum_dims (ds_spectral_sequence.py)
  2. Cross-check vacuum dims against wn_vacuum_character_coeffs (vvmf_verifications.py)
  3. Cross-check vacuum dims against explicit W_4 engine
  4. Cross-check W_3 known GF against KNOWN_BAR_DIMS (bar_complex.py)
  5. Cross-check kappa coefficients against known values for specific N
  6. Verify kappa additivity (kappa(W_{N+1}) = kappa(W_N) + c/(N+1))
  7. Central charge complementarity c(k) + c(-k-2N) = const
  8. V-bar stabilization: for N >= h+2, dim V-bar_h is independent of N
  9. Exterior algebra character: product structure
  10. Growth rate comparison across families

References:
  ds_spectral_sequence.py: _wn_vacuum_dims
  vvmf_verifications.py: wn_vacuum_character_coeffs
  bar_cohomology_w4_explicit_engine.py: w4_vacuum_dims, w4_augmentation_dims
  bar_cohomology_w3_explicit_engine.py: w3_bar_dims
  bar_complex.py: KNOWN_BAR_DIMS
  landscape_census.tex (bar dimension tables)
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, simplify

from compute.lib.bar_cohomology_wn_universal_engine import (
    WNBarCohomologyEngine,
    bar_chain_dim_wn,
    bar_euler_char_wn,
    detect_linear_recurrence,
    exterior_algebra_character,
    known_gf_dims,
    sl_n_vacuum_dims,
    ds_vacuum_ratio,
    vbar_dim_at_fixed_weight,
    vbar_polynomial_in_N,
    virasoro_known_gf_dims,
    w3_known_gf_dims,
    wn_augmentation_dims,
    wn_central_charge,
    wn_complementarity_sum,
    wn_kappa_coefficient,
    wn_kappa_symbolic,
    wn_kappa_table,
    wn_vacuum_dims,
)


# ============================================================================
# Module import
# ============================================================================

class TestImport:
    def test_module_loads(self):
        import compute.lib.bar_cohomology_wn_universal_engine
        assert hasattr(compute.lib.bar_cohomology_wn_universal_engine, 'wn_vacuum_dims')


# ============================================================================
# Vacuum module dimensions
# ============================================================================

class TestVacuumDims:
    """Verify W_N vacuum module dimensions by multiple paths."""

    def test_vacuum_has_dim_1(self):
        """dim V_0 = 1 (vacuum) for all N."""
        for N in range(2, 8):
            assert wn_vacuum_dims(N, 4)[0] == 1

    def test_weight_1_empty(self):
        """dim V_1 = 0 (no weight-1 states) for all N."""
        for N in range(2, 8):
            assert wn_vacuum_dims(N, 4)[1] == 0

    def test_weight_2_universal(self):
        """dim V_2 = 1 for all N >= 2: just L_{-2}|0>."""
        for N in range(2, 8):
            assert wn_vacuum_dims(N, 4)[2] == 1

    def test_weight_3_step(self):
        """dim V_3 = 1 for N=2 (L_{-3}), dim V_3 = 2 for N >= 3 (L_{-3}, W3_{-3})."""
        assert wn_vacuum_dims(2, 4)[3] == 1
        for N in range(3, 8):
            assert wn_vacuum_dims(N, 4)[3] == 2

    def test_cross_check_ds_spectral_sequence(self):
        """Cross-check against _wn_vacuum_dims from ds_spectral_sequence.py."""
        from compute.lib.ds_spectral_sequence import _wn_vacuum_dims
        for N in [2, 3, 4, 5, 6]:
            ours = wn_vacuum_dims(N, 10)
            theirs = _wn_vacuum_dims(N, 10)
            for h in range(11):
                assert ours[h] == theirs[h], \
                    f"W_{N} at weight {h}: {ours[h]} != {theirs[h]}"

    def test_cross_check_vvmf(self):
        """Cross-check against wn_vacuum_character_coeffs from vvmf."""
        from compute.lib.vvmf_verifications import wn_vacuum_character_coeffs
        for N in [2, 3, 4, 5]:
            ours = wn_vacuum_dims(N, 10)
            theirs = wn_vacuum_character_coeffs(N, max_weight=10)
            for h in range(11):
                assert ours[h] == theirs[h], \
                    f"W_{N} at weight {h}: {ours[h]} != {theirs[h]}"

    def test_cross_check_w4_explicit(self):
        """Cross-check W_4 against the explicit W_4 engine."""
        from compute.lib.bar_cohomology_w4_explicit_engine import w4_vacuum_dims
        ours = wn_vacuum_dims(4, 10)
        theirs = w4_vacuum_dims(10)
        for h in range(11):
            assert ours[h] == theirs[h], \
                f"W_4 at weight {h}: {ours[h]} != {theirs[h]}"

    def test_virasoro_known_values(self):
        """W_2 vacuum = partitions into parts >= 2."""
        # p_{>=2}(h): 0,0,1,1,2,2,4,4,7,8,12
        known = {0: 1, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 7, 9: 8, 10: 12}
        vac = wn_vacuum_dims(2, 10)
        for h in range(11):
            assert vac[h] == known[h], f"Vir at h={h}: {vac[h]} != {known[h]}"

    def test_w5_known_values(self):
        """W_5 has generators at weights 2,3,4,5."""
        v = wn_vacuum_dims(5, 8)
        # Weight 2: just L_{-2} -> dim 1
        assert v[2] == 1
        # Weight 3: L_{-3}, W3_{-3} -> dim 2
        assert v[3] == 2
        # Weight 4: L_{-4}, L_{-2}^2, W3_{-4}, W4_{-4} -> dim 4
        assert v[4] == 4
        # Weight 5: L_{-5}, L_{-3}L_{-2}, W3_{-5}, W3_{-3}L_{-2},
        #           W4_{-5}, W5_{-5} -> dim 6
        assert v[5] == 6

    def test_w6_known_values(self):
        """W_6 has generators at weights 2,3,4,5,6."""
        v = wn_vacuum_dims(6, 6)
        assert v[5] == 6  # same as W_5 (W_6 mode starts at weight 6)
        # Weight 6: W_5 had dim 11; W_6 adds W6_{-6} -> dim 12
        assert v[6] == 12


# ============================================================================
# Augmentation ideal
# ============================================================================

class TestAugmentationDims:
    def test_vbar_0_is_zero(self):
        """V-bar_0 = 0 (vacuum subtracted)."""
        for N in range(2, 6):
            assert wn_augmentation_dims(N, 4).get(0, 0) == 0

    def test_vbar_equals_vacuum_minus_1_at_0(self):
        """V-bar_h = V_h for h >= 2."""
        for N in range(2, 6):
            vac = wn_vacuum_dims(N, 8)
            vbar = wn_augmentation_dims(N, 8)
            for h in range(2, 9):
                assert vbar[h] == vac[h]


# ============================================================================
# Kappa
# ============================================================================

class TestKappa:
    def test_virasoro_kappa(self):
        """kappa(W_2) = c/2, coefficient = 1/2."""
        assert wn_kappa_coefficient(2) == Fraction(1, 2)

    def test_w3_kappa(self):
        """kappa(W_3) = c/2 + c/3 = 5c/6."""
        assert wn_kappa_coefficient(3) == Fraction(5, 6)

    def test_w4_kappa(self):
        """kappa(W_4) = c/2 + c/3 + c/4 = 13c/12."""
        assert wn_kappa_coefficient(4) == Fraction(13, 12)

    def test_w5_kappa(self):
        """kappa(W_5) = 77c/60."""
        assert wn_kappa_coefficient(5) == Fraction(77, 60)

    def test_w6_kappa(self):
        """kappa(W_6) = 29c/20."""
        assert wn_kappa_coefficient(6) == Fraction(29, 20)

    def test_kappa_additivity(self):
        """kappa(W_{N+1}) = kappa(W_N) + c/(N+1)."""
        for N in range(2, 10):
            left = wn_kappa_coefficient(N + 1)
            right = wn_kappa_coefficient(N) + Fraction(1, N + 1)
            assert left == right, f"Failed at N={N}: {left} != {right}"

    def test_kappa_symbolic(self):
        """kappa(W_N) is (H_N - 1) * c as sympy expression."""
        c = Symbol('c')
        assert wn_kappa_symbolic(2) == Rational(1, 2) * c
        assert wn_kappa_symbolic(3) == Rational(5, 6) * c
        assert wn_kappa_symbolic(4) == Rational(13, 12) * c

    def test_kappa_table(self):
        """Kappa table is consistent."""
        table = wn_kappa_table(6)
        assert table[2] == Fraction(1, 2)
        assert table[3] == Fraction(5, 6)
        assert table[6] == Fraction(29, 20)

    def test_kappa_cross_check_w4_engine(self):
        """Cross-check kappa(W_4) against the W_4 explicit engine."""
        from compute.lib.bar_cohomology_w4_explicit_engine import w4_kappa
        c = Symbol('c')
        assert simplify(w4_kappa(c) - wn_kappa_symbolic(4)) == 0


# ============================================================================
# Central charge
# ============================================================================

class TestCentralCharge:
    def test_virasoro_central_charge(self):
        """c(W_2, k) = 1 - 6(k+1)^2/(k+2).
        At k=1: c = 1 - 6*4/3 = -7."""
        k = Symbol('k')
        c = wn_central_charge(2, k)
        assert simplify(c.subs(k, 1) + 7) == 0

    def test_w3_central_charge(self):
        """c(W_3, k) = 2 - 24(k+2)^2/(k+3).
        At k=1: c = 2 - 24*9/4 = -52."""
        k = Symbol('k')
        c = wn_central_charge(3, k)
        assert simplify(c.subs(k, 1) + 52) == 0

    def test_w3_central_charge_k0(self):
        """c(W_3, k=0) = 2 - 24*4/3 = -30."""
        k = Symbol('k')
        c = wn_central_charge(3, k)
        assert simplify(c.subs(k, 0) + 30) == 0

    def test_complementarity_virasoro(self):
        """c(k) + c(-k-4) = 26 for W_2.
        Formula: 2(N-1)(2N^2+2N+1) = 2*1*13 = 26."""
        total = wn_complementarity_sum(2)
        assert total == 26

    def test_complementarity_w3(self):
        """c(k) + c(-k-6) = 100 for W_3.
        Formula: 2*2*25 = 100."""
        total = wn_complementarity_sum(3)
        assert total == 100

    def test_complementarity_w4(self):
        """c(k) + c(-k-8) = 246 for W_4.
        Formula: 2*3*41 = 246."""
        total = wn_complementarity_sum(4)
        assert total == 246

    def test_complementarity_formula(self):
        """Complementarity sum = 2(N-1)(2N^2+2N+1) for all N."""
        for N in range(2, 8):
            total = wn_complementarity_sum(N)
            expected = 2 * (N - 1) * (2 * N**2 + 2 * N + 1)
            assert total == expected, f"W_{N}: {total} != {expected}"


# ============================================================================
# Known bar cohomology GFs
# ============================================================================

class TestKnownGFs:
    def test_virasoro_first_values(self):
        """Virasoro dims: 1, 2, 5, 12, 30, 76, 196."""
        dims = virasoro_known_gf_dims(7)
        assert dims == [1, 2, 5, 12, 30, 76, 196]

    def test_w3_first_values(self):
        """W_3 dims: 2, 5, 16, 52, 171."""
        dims = w3_known_gf_dims(5)
        assert dims == [2, 5, 16, 52, 171]

    def test_w3_cross_check_known_bar_dims(self):
        """Cross-check against KNOWN_BAR_DIMS from bar_complex.py."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        w3_known = KNOWN_BAR_DIMS.get('W3', {})
        w3_ours = w3_known_gf_dims(5)
        for n in range(1, 6):
            assert w3_ours[n - 1] == w3_known[n], \
                f"W_3 at degree {n}: {w3_ours[n-1]} != {w3_known[n]}"

    def test_virasoro_motzkin(self):
        """Virasoro dims are Motzkin differences M(n+1) - M(n) starting at n=1.
        M(0)=1,M(1)=1,M(2)=2,M(3)=4,M(4)=9,M(5)=21,M(6)=51,M(7)=127,M(8)=323."""
        M = [1, 1, 2, 4, 9, 21, 51, 127, 323]
        expected = [M[n + 1] - M[n] for n in range(1, 8)]
        dims = virasoro_known_gf_dims(7)
        assert dims == expected

    def test_known_gf_returns_none_for_unknown(self):
        """known_gf_dims returns None for N >= 4."""
        assert known_gf_dims(4) is None
        assert known_gf_dims(5) is None
        assert known_gf_dims(10) is None

    def test_known_gf_returns_data_for_known(self):
        """known_gf_dims returns data for N=2,3."""
        assert known_gf_dims(2) is not None
        assert known_gf_dims(3) is not None


# ============================================================================
# Recurrence detection
# ============================================================================

class TestRecurrenceDetection:
    def test_w3_rational(self):
        """W_3 GF is rational (linear recurrence exists)."""
        dims = w3_known_gf_dims(15)
        rec = detect_linear_recurrence(dims)
        assert rec is not None
        assert rec["order"] == 3
        assert rec["coefficients"] == [4, -2, -1]

    def test_geometric_sequence(self):
        """Detect recurrence in a simple geometric sequence."""
        seq = [2 ** n for n in range(10)]
        rec = detect_linear_recurrence(seq)
        assert rec is not None
        assert rec["order"] == 1
        assert rec["coefficients"] == [2]

    def test_fibonacci(self):
        """Detect recurrence in Fibonacci."""
        fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        rec = detect_linear_recurrence(fib)
        assert rec is not None
        assert rec["order"] == 2
        assert rec["coefficients"] == [1, 1]

    def test_virasoro_not_rational(self):
        """Virasoro GF is NOT rational (algebraic degree 2)."""
        dims = virasoro_known_gf_dims(15)
        rec = detect_linear_recurrence(dims, max_order=8)
        assert rec is None


# ============================================================================
# Bar chain group dimensions
# ============================================================================

class TestBarChainDims:
    def test_bar_deg0_equals_vbar(self):
        """B^0_h = V-bar_h (bar degree 0 = augmentation ideal)."""
        for N in [2, 3, 4]:
            vbar = wn_augmentation_dims(N, 10)
            for h in range(2, 11):
                # B^0_h = dim Vbar_h (one factor)
                # But bar_chain_dim_wn computes with n+1 factors at bar degree n.
                # At bar degree 0: 1 factor from V-bar, OS^0 = 0! = 1.
                assert bar_chain_dim_wn(N, 0, h, 10) == vbar.get(h, 0), \
                    f"W_{N} B^0_{h}: {bar_chain_dim_wn(N, 0, h, 10)} != {vbar.get(h, 0)}"

    def test_bar_deg1_minimum_weight(self):
        """B^1_h = 0 for h < 4 (need two V-bar elements, each >= 2)."""
        for N in [2, 3, 4]:
            assert bar_chain_dim_wn(N, 1, 2, 10) == 0
            assert bar_chain_dim_wn(N, 1, 3, 10) == 0

    def test_bar_deg1_weight4_virasoro(self):
        """B^1_4(Vir) = dim(V-bar pairs at weight 4) * 1!.
        Only pair: (2,2) -> 1*1 = 1 tuple, times 1! = 1."""
        assert bar_chain_dim_wn(2, 1, 4, 10) == 1

    def test_bar_deg1_weight5_virasoro(self):
        """B^1_5(Vir): pairs summing to 5 from V-bar.
        (2,3) and (3,2): 1*1 + 1*1 = 2 tuples, times 1! = 2."""
        assert bar_chain_dim_wn(2, 1, 5, 10) == 2


# ============================================================================
# V-bar stabilization
# ============================================================================

class TestVbarStabilization:
    def test_stabilizes_at_N_h_plus_2(self):
        """V-bar_h stabilizes for N >= h (all generators have modes at weight h)."""
        for h in range(2, 8):
            dims_by_N = []
            for N in range(2, h + 4):
                d = wn_augmentation_dims(N, h).get(h, 0)
                dims_by_N.append((N, d))
            # Check that the last two are equal
            if len(dims_by_N) >= 2:
                assert dims_by_N[-1][1] == dims_by_N[-2][1], \
                    f"h={h}: not stabilized at N={dims_by_N[-1][0]}"

    def test_stable_value_is_w_infinity(self):
        """The stable value of V-bar_h equals dim(W_inf vacuum)_h.

        For W_infinity: chi(q) = prod_{n>=2} 1/(1-q^n)^{n-1}.
        For large N: chi_{W_N}(q) approaches prod_{n>=2} 1/(1-q^n)^{min(n-1, N-1)}.
        For N >= h: all exponents at weights <= h are n-1, giving the W_inf limit.
        """
        # Compute W_N for large N (N = 20 should suffice for weights up to 8)
        large_N_dims = wn_vacuum_dims(20, 8)
        for h in range(2, 9):
            large = large_N_dims.get(h, 0)
            # This should match W_N for N >= h+2
            our_stable = wn_vacuum_dims(h + 2, h).get(h, 0)
            assert large == our_stable, \
                f"h={h}: W_inf={large}, W_{h+2}={our_stable}"

    def test_monotone_in_N(self):
        """V-bar_h(W_{N+1}) >= V-bar_h(W_N) (adding generators only increases)."""
        for h in range(2, 10):
            for N in range(2, h + 2):
                d_N = wn_augmentation_dims(N, h).get(h, 0)
                d_N1 = wn_augmentation_dims(N + 1, h).get(h, 0)
                assert d_N1 >= d_N, \
                    f"h={h}, N={N}: dim decreases {d_N} -> {d_N1}"


# ============================================================================
# Exterior algebra character
# ============================================================================

class TestExteriorAlgebra:
    def test_constant_term(self):
        """Exterior algebra character has constant term 1."""
        for N in [2, 3, 4, 5]:
            ext = exterior_algebra_character(N, 10)
            assert ext[0] == 1

    def test_virasoro_exterior(self):
        """For Virasoro: prod_{n>=2} (1+q^n) = partitions into distinct parts >= 2."""
        ext = exterior_algebra_character(2, 10)
        # Distinct partitions of h with parts >= 2:
        # h=0: {}, h=2: {2}, h=3: {3}, h=4: {4}, h=5: {5,{2,3}},
        # h=6: {6,{2,4}}, h=7: {7,{2,5},{3,4}}
        expected = {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3}
        for h in range(8):
            assert ext[h] == expected[h], \
                f"Vir exterior at h={h}: {ext[h]} != {expected[h]}"

    def test_monotone_in_N(self):
        """Exterior character of W_{N+1} >= W_N at each weight."""
        for N in range(2, 6):
            ext_N = exterior_algebra_character(N, 10)
            ext_N1 = exterior_algebra_character(N + 1, 10)
            for h in range(11):
                assert ext_N1[h] >= ext_N[h], \
                    f"N={N}, h={h}: ext decreases"


# ============================================================================
# Growth rate
# ============================================================================

class TestGrowthRate:
    def test_virasoro_growth_rate(self):
        """Virasoro growth rate ~ 3."""
        from compute.lib.bar_cohomology_wn_universal_engine import growth_rate_from_gf
        gr = growth_rate_from_gf(2, 20)
        assert gr is not None
        assert abs(gr["gamma_ratio"] - 3.0) < 0.25  # convergence slow at 20 terms

    def test_w3_growth_rate(self):
        """W_3 growth rate ~ (3+sqrt(13))/2 ~ 3.303."""
        from compute.lib.bar_cohomology_wn_universal_engine import growth_rate_from_gf
        gr = growth_rate_from_gf(3, 20)
        assert gr is not None
        target = (3 + 13 ** 0.5) / 2
        assert abs(gr["gamma_ratio"] - target) < 0.05

    def test_w3_faster_than_virasoro(self):
        """W_3 grows faster than Virasoro."""
        from compute.lib.bar_cohomology_wn_universal_engine import growth_rate_from_gf
        gr2 = growth_rate_from_gf(2, 20)
        gr3 = growth_rate_from_gf(3, 20)
        assert gr3["gamma_ratio"] > gr2["gamma_ratio"]


# ============================================================================
# DS reduction
# ============================================================================

class TestDSReduction:
    def test_sl2_vacuum_dims(self):
        """sl_2 vacuum: 3 generators at weight 1.
        chi(q) = prod_{n>=1} 1/(1-q^n)^3."""
        sl2 = sl_n_vacuum_dims(2, 6)
        # Weight 0: 1
        assert sl2[0] == 1
        # Weight 1: 3 (the generators)
        assert sl2[1] == 3
        # Weight 2: 3 choices of single modes + 6 pairs = dim(Sym^2(3)) = 6 from modes,
        # plus 3 modes at weight 2. Total: 3 generators at weight 2 (one per J^a)
        # + 3*2/2 = 3 pairs (J^a_{-1}J^b_{-1}) + 3 singles (J^a_{-2})
        # = 3 + 6 = 9. Wait, need to think more carefully.
        # prod_{n>=1} 1/(1-q^n)^3 = 1 + 3q + 9q^2 + 22q^3 + ...
        assert sl2[2] == 9

    def test_ds_ratio_weight_0(self):
        """DS ratio at weight 0 is 1/1 = 1 (both have vacuum)."""
        for N in [2, 3, 4]:
            ratio = ds_vacuum_ratio(N, 4)
            assert ratio[0] == Fraction(1)

    def test_ds_ratio_increases_with_weight(self):
        """The ratio chi(sl_N)/chi(W_N) generally increases with weight."""
        for N in [2, 3]:
            ratio = ds_vacuum_ratio(N, 8)
            # At low weights the ratio should be >= 1
            for h in range(1, 6):
                if h in ratio:
                    assert ratio[h] >= 1, \
                        f"N={N}, h={h}: ratio {ratio[h]} < 1"


# ============================================================================
# Engine class
# ============================================================================

class TestEngine:
    def test_engine_creation(self):
        for N in range(2, 8):
            eng = WNBarCohomologyEngine(N)
            assert eng.N == N
            assert eng.num_generators() == N - 1

    def test_engine_invalid_N(self):
        with pytest.raises(ValueError):
            WNBarCohomologyEngine(1)

    def test_engine_generator_weights(self):
        eng = WNBarCohomologyEngine(5)
        assert eng.generator_weights() == [2, 3, 4, 5]

    def test_engine_vacuum_dim(self):
        eng = WNBarCohomologyEngine(3, max_weight=8)
        assert eng.vacuum_dim(0) == 1
        assert eng.vacuum_dim(2) == 1
        assert eng.vacuum_dim(3) == 2

    def test_engine_vbar_dim(self):
        eng = WNBarCohomologyEngine(3, max_weight=8)
        assert eng.vbar_dim(0) == 0
        assert eng.vbar_dim(2) == 1

    def test_engine_kappa(self):
        eng = WNBarCohomologyEngine(4)
        assert eng.kappa_coefficient() == Fraction(13, 12)

    def test_engine_has_known_gf(self):
        assert WNBarCohomologyEngine(2).has_known_gf()
        assert WNBarCohomologyEngine(3).has_known_gf()
        assert not WNBarCohomologyEngine(4).has_known_gf()

    def test_engine_full_report(self):
        eng = WNBarCohomologyEngine(3, max_weight=10)
        report = eng.full_report()
        assert report["N"] == 3
        assert report["num_generators"] == 2
        assert report["has_known_gf"] is True
        assert report["is_rational"] is True
        assert report["recurrence_order"] == 3


# ============================================================================
# Euler characteristic
# ============================================================================

class TestEulerChar:
    def test_euler_char_low_weight(self):
        """At weight 2 for Virasoro: B^0_2 = 1, B^1_2 = 0 => chi = 1."""
        chi = bar_euler_char_wn(2, 2, max_bar_deg=3)
        assert chi == 1  # V-bar_2 = 1, no higher bar groups at weight 2

    def test_euler_char_weight_4_virasoro(self):
        """At weight 4 for Virasoro: B^0=2, B^1=1 => chi = 2 - 1 = 1."""
        chi = bar_euler_char_wn(2, 4, max_bar_deg=3)
        assert chi == 1

    def test_euler_char_weight_5_virasoro(self):
        """At weight 5 for Virasoro: B^0=2, B^1=2 => chi = 2 - 2 = 0."""
        chi = bar_euler_char_wn(2, 5, max_bar_deg=3)
        assert chi == 0


# ============================================================================
# Complementarity sum formula
# ============================================================================

class TestComplementaritySum:
    def test_complementarity_is_k_independent(self):
        """c(k) + c(-k-2N) is a constant (independent of k) for all N."""
        k = Symbol('k')
        for N in range(2, 7):
            s = wn_complementarity_sum(N)
            assert not s.has(k), f"W_{N}: sum {s} depends on k"

    def test_complementarity_cross_check_w4_engine(self):
        """Cross-check W_4 complementarity against the W_4 explicit engine."""
        from compute.lib.bar_cohomology_w4_explicit_engine import w4_complementarity_sum
        assert wn_complementarity_sum(4) == w4_complementarity_sum()
