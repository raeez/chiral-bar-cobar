"""Tests for compute/lib/w4_ope_complete.py — Complete W_4 OPE extraction.

Verifies the FULL lambda-bracket algebra of W(sl_4) via quantum Miura
transformation and Wick contractions. This is the MC4 stage-4 verification
layer.

Test structure:
  A. Import and basic functionality (5 tests)
  B. Central charge and Feigin-Frenkel duality (6 tests)
  C. Generator construction (5 tests)
  D. Virasoro sub-algebra T x T (5 tests)
  E. Primary conditions T x W_3, T x W_4 (5 tests)
  F. W_3 x W_3 OPE and c_334 extraction (6 tests)
  G. W_4 x W_4 OPE and c_444 extraction (5 tests)
  H. W_3 x W_4 OPE and mixed coefficients (5 tests)
  I. Composite field Lambda (4 tests)
  J. Classical limit and zero/pole structure (4 tests)
  K. Metric adjoint relations (3 tests)
  L. MC4 stabilization (3 tests)
  M. Unitary minimal models (2 tests)
  N. Cross-consistency (3 tests)

Total: 61 tests.

References:
  concordance.tex: rem:mc4-winfty-computation-target
  w4_ds_ope_extraction.py: known closed-form formulas
  w4_ds_ope.py: Miura transform and Wick engine
"""

import pytest
from sympy import Rational, Symbol, simplify, cancel, expand, oo

# Test level: k=1 gives c = 3 - 60*16/5 = -189
# This is a clean rational value suitable for exact verification.
K_TEST = Rational(1)
C_TEST = 3 - Rational(60) * (K_TEST + 3) ** 2 / (K_TEST + 4)

# Second test level: k=2 gives c = 3 - 60*25/6 = -247
K_TEST2 = Rational(2)
C_TEST2 = 3 - Rational(60) * (K_TEST2 + 3) ** 2 / (K_TEST2 + 4)


# ═══════════════════════════════════════════════════════════════
# A. Import and basic functionality
# ═══════════════════════════════════════════════════════════════

class TestImport:
    """Module imports and basic function availability."""

    def test_module_loads(self):
        import compute.lib.w4_ope_complete
        assert hasattr(compute.lib.w4_ope_complete, 'central_charge')

    def test_central_charge_function(self):
        from compute.lib.w4_ope_complete import central_charge
        assert central_charge(K_TEST) == C_TEST

    def test_dual_level_function(self):
        from compute.lib.w4_ope_complete import dual_level
        assert dual_level(K_TEST) == -K_TEST - 8

    def test_compute_generators_returns_dict(self):
        from compute.lib.w4_ope_complete import compute_w4_generators
        gens = compute_w4_generators(K_TEST)
        assert 'T' in gens and 'W3' in gens and 'W4' in gens

    def test_compute_all_opes_returns_6_brackets(self):
        from compute.lib.w4_ope_complete import compute_all_opes
        opes = compute_all_opes(K_TEST)
        assert len(opes) == 6
        expected_keys = {'TT', 'TW3', 'TW4', 'W3W3', 'W3W4', 'W4W4'}
        assert set(opes.keys()) == expected_keys


# ═══════════════════════════════════════════════════════════════
# B. Central charge and Feigin-Frenkel duality
# ═══════════════════════════════════════════════════════════════

class TestCentralCharge:
    """Central charge computation and FF duality."""

    def test_c_at_k1(self):
        from compute.lib.w4_ope_complete import central_charge
        assert central_charge(Rational(1)) == Rational(-189)

    def test_c_at_k2(self):
        from compute.lib.w4_ope_complete import central_charge
        assert central_charge(Rational(2)) == Rational(-247)

    def test_complementarity_sum_246(self):
        """c(k) + c(-k-8) = 246 for all k (sl_4 complementarity)."""
        from compute.lib.w4_ope_complete import central_charge, dual_level
        k = Symbol('k')
        s = simplify(central_charge(k) + central_charge(dual_level(k)))
        assert s == 246

    def test_ff_duality_report(self):
        from compute.lib.w4_ope_complete import verify_ff_duality
        result = verify_ff_duality(K_TEST)
        assert result['comp_correct']

    def test_ff_duality_c_values(self):
        from compute.lib.w4_ope_complete import verify_ff_duality
        result = verify_ff_duality(K_TEST)
        assert cancel(result['c_k'] + result['c_kp']) == 246

    def test_ff_duality_at_k2(self):
        from compute.lib.w4_ope_complete import verify_ff_duality
        result = verify_ff_duality(K_TEST2)
        assert result['comp_correct']


# ═══════════════════════════════════════════════════════════════
# C. Generator construction
# ═══════════════════════════════════════════════════════════════

class TestGenerators:
    """Generator construction via quantum Miura."""

    def test_c_matches(self):
        from compute.lib.w4_ope_complete import verify_generators_at_k
        v = verify_generators_at_k(K_TEST)
        assert v['c_match']

    def test_w3_primary(self):
        from compute.lib.w4_ope_complete import verify_generators_at_k
        v = verify_generators_at_k(K_TEST)
        assert v['w3_primary']

    def test_w4_primary(self):
        from compute.lib.w4_ope_complete import verify_generators_at_k
        v = verify_generators_at_k(K_TEST)
        assert v['w4_primary']

    def test_two_point_nonzero(self):
        from compute.lib.w4_ope_complete import verify_generators_at_k
        v = verify_generators_at_k(K_TEST)
        assert v['N3_nonzero'] and v['N4_nonzero']

    def test_generators_at_k2(self):
        from compute.lib.w4_ope_complete import verify_generators_at_k
        v = verify_generators_at_k(K_TEST2)
        assert v['c_match'] and v['w3_primary'] and v['w4_primary']


# ═══════════════════════════════════════════════════════════════
# D. Virasoro sub-algebra T x T
# ═══════════════════════════════════════════════════════════════

class TestVirasoro:
    """Virasoro sub-algebra T x T."""

    def test_virasoro_all_correct(self):
        from compute.lib.w4_ope_complete import verify_virasoro_subalgebra
        v = verify_virasoro_subalgebra(K_TEST)
        assert v['all_correct']

    def test_pole4_is_c_over_2(self):
        from compute.lib.w4_ope_complete import verify_virasoro_subalgebra
        v = verify_virasoro_subalgebra(K_TEST)
        assert v['pole4_correct']

    def test_pole2_coeff_is_2(self):
        from compute.lib.w4_ope_complete import verify_virasoro_subalgebra
        v = verify_virasoro_subalgebra(K_TEST)
        assert v['pole2_correct']

    def test_pole1_coeff_is_1(self):
        from compute.lib.w4_ope_complete import verify_virasoro_subalgebra
        v = verify_virasoro_subalgebra(K_TEST)
        assert v['pole1_correct']

    def test_no_higher_poles(self):
        from compute.lib.w4_ope_complete import verify_virasoro_subalgebra
        v = verify_virasoro_subalgebra(K_TEST)
        assert v['no_higher_poles']


# ═══════════════════════════════════════════════════════════════
# E. Primary conditions T x W_3, T x W_4
# ═══════════════════════════════════════════════════════════════

class TestPrimaryConditions:
    """Primary conditions for W_3 and W_4."""

    def test_w3_is_primary(self):
        from compute.lib.w4_ope_complete import verify_primary_conditions
        v = verify_primary_conditions(K_TEST)
        assert v['W3_primary']

    def test_w4_is_primary(self):
        from compute.lib.w4_ope_complete import verify_primary_conditions
        v = verify_primary_conditions(K_TEST)
        assert v['W4_primary']

    def test_w3_weight_is_3(self):
        from compute.lib.w4_ope_complete import verify_primary_conditions
        v = verify_primary_conditions(K_TEST)
        assert v['W3_weight_correct']

    def test_w4_weight_is_4(self):
        from compute.lib.w4_ope_complete import verify_primary_conditions
        v = verify_primary_conditions(K_TEST)
        assert v['W4_weight_correct']

    def test_primary_at_k2(self):
        from compute.lib.w4_ope_complete import verify_primary_conditions
        v = verify_primary_conditions(K_TEST2)
        assert v['W3_primary'] and v['W4_primary']


# ═══════════════════════════════════════════════════════════════
# F. W_3 x W_3 OPE and c_334 extraction
# ═══════════════════════════════════════════════════════════════

class TestW3W3OPE:
    """W_3 x W_3 OPE: composite Lambda and c_334 coupling."""

    def test_c334_matches_formula(self):
        """c_334^2 from Wick contraction matches known rational formula."""
        from compute.lib.w4_ope_complete import analyze_w3w3_ope
        r = analyze_w3w3_ope(K_TEST)
        assert r['c334_match'], f"c334 mismatch at k={K_TEST}: got {r['c334_sq']}, expected {r['c334_sq_known']}"

    def test_c334_at_k2(self):
        from compute.lib.w4_ope_complete import analyze_w3w3_ope
        r = analyze_w3w3_ope(K_TEST2)
        assert r['c334_match']

    def test_two_point_N3_nonzero(self):
        from compute.lib.w4_ope_complete import analyze_w3w3_ope
        r = analyze_w3w3_ope(K_TEST)
        assert expand(r['N3']) != 0

    def test_T_at_pole4_nonzero(self):
        """C_{3,3;2;0,4} = 2 after normalization."""
        from compute.lib.w4_ope_complete import analyze_w3w3_ope
        r = analyze_w3w3_ope(K_TEST)
        assert expand(r['T_at_pole4']) != 0

    def test_w3w3_has_pole_6(self):
        """Leading pole is 6 (from two-point function c/3)."""
        from compute.lib.w4_ope_complete import analyze_w3w3_ope
        r = analyze_w3w3_ope(K_TEST)
        assert 6 in r['pole_orders']

    def test_w3w3_pole_structure(self):
        """W_3 x W_3 should have poles up to 6."""
        from compute.lib.w4_ope_complete import analyze_w3w3_ope
        r = analyze_w3w3_ope(K_TEST)
        assert max(r['pole_orders']) == 6


# ═══════════════════════════════════════════════════════════════
# G. W_4 x W_4 OPE and c_444 extraction
# ═══════════════════════════════════════════════════════════════

class TestW4W4OPE:
    """W_4 x W_4 OPE: Ward identity and c_444 self-coupling."""

    def test_ward_identity_C44T_is_2(self):
        """Universal T-coupling: C_{4,4;2;0,6} = 2."""
        from compute.lib.w4_ope_complete import analyze_w4w4_ope
        r = analyze_w4w4_ope(K_TEST)
        assert r['C_44_T_is_2'], f"Ward identity fails: C_44_T = {r['C_44_T_normalized']}"

    def test_c444_matches_formula(self):
        """c_444^2 from Wick contraction matches known rational formula."""
        from compute.lib.w4_ope_complete import analyze_w4w4_ope
        r = analyze_w4w4_ope(K_TEST)
        assert r['c444_match'], f"c444 mismatch at k={K_TEST}: got {r['c444_sq']}, expected {r['c444_sq_known']}"

    def test_c444_at_k2(self):
        from compute.lib.w4_ope_complete import analyze_w4w4_ope
        r = analyze_w4w4_ope(K_TEST2)
        assert r['c444_match']

    def test_w4w4_has_pole_8(self):
        """Leading pole is 8 (from two-point function c/4)."""
        from compute.lib.w4_ope_complete import analyze_w4w4_ope
        r = analyze_w4w4_ope(K_TEST)
        assert 8 in r['pole_orders']

    def test_two_point_N4_nonzero(self):
        from compute.lib.w4_ope_complete import analyze_w4w4_ope
        r = analyze_w4w4_ope(K_TEST)
        assert expand(r['N4']) != 0


# ═══════════════════════════════════════════════════════════════
# H. W_3 x W_4 OPE and mixed coefficients
# ═══════════════════════════════════════════════════════════════

class TestW3W4OPE:
    """W_3 x W_4 OPE: mixed Virasoro vanishing and cross-couplings."""

    def test_mixed_virasoro_vanishing(self):
        """C_{3,4;2;0,5} = 0 (mixed Virasoro vanishing)."""
        from compute.lib.w4_ope_complete import analyze_w3w4_ope
        r = analyze_w3w4_ope(K_TEST)
        assert r['T_at_pole5_zero'], f"T at pole 5 not zero: {r['T_at_pole5_raw']}"

    def test_c343_matches_formula(self):
        """C_{3,4;3;0,4}^2 matches known formula."""
        from compute.lib.w4_ope_complete import analyze_w3w4_ope
        r = analyze_w3w4_ope(K_TEST)
        assert r['C_34_3_match'], f"C_34_3 mismatch: got {r['C_34_3_sq']}, expected {r['C_34_3_sq_known']}"

    def test_c344_matches_formula(self):
        """C_{3,4;4;0,3}^2 matches known formula."""
        from compute.lib.w4_ope_complete import analyze_w3w4_ope
        r = analyze_w3w4_ope(K_TEST)
        assert r['C_34_4_match'], f"C_34_4 mismatch: got {r['C_34_4_sq']}, expected {r['C_34_4_sq_known']}"

    def test_w3w4_at_k2(self):
        from compute.lib.w4_ope_complete import analyze_w3w4_ope
        r = analyze_w3w4_ope(K_TEST2)
        assert r['T_at_pole5_zero']

    def test_w3w4_pole_structure(self):
        """W_3 x W_4 should have poles up to 7 at most."""
        from compute.lib.w4_ope_complete import analyze_w3w4_ope
        r = analyze_w3w4_ope(K_TEST)
        if r['pole_orders']:
            assert max(r['pole_orders']) <= 7


# ═══════════════════════════════════════════════════════════════
# I. Composite field Lambda
# ═══════════════════════════════════════════════════════════════

class TestCompositeLambda:
    """Composite field Lambda = :TT: - (3/10)d^2T."""

    def test_quasi_primary(self):
        """Lambda is quasi-primary: T(z)Lambda(w) has no (z-w)^{-3} pole."""
        from compute.lib.w4_ope_complete import compute_composite_lambda
        r = compute_composite_lambda(K_TEST)
        assert r['quasi_primary']

    def test_norm_correct(self):
        """<Lambda|Lambda> = c(5c+22)/10."""
        from compute.lib.w4_ope_complete import compute_composite_lambda
        r = compute_composite_lambda(K_TEST)
        assert r['norm_correct'], f"Lambda norm: got {r['norm_Lambda']}, expected {r['expected_norm']}"

    def test_quasi_primary_at_k2(self):
        from compute.lib.w4_ope_complete import compute_composite_lambda
        r = compute_composite_lambda(K_TEST2)
        assert r['quasi_primary']

    def test_norm_at_k2(self):
        from compute.lib.w4_ope_complete import compute_composite_lambda
        r = compute_composite_lambda(K_TEST2)
        assert r['norm_correct']


# ═══════════════════════════════════════════════════════════════
# J. Classical limit and zero/pole structure
# ═══════════════════════════════════════════════════════════════

class TestClassicalLimitAndZeros:
    """Classical limit c -> inf and zero/pole structure."""

    def test_c334_classical_limit_is_10(self):
        """c_334^2 -> 10 as c -> infinity."""
        from compute.lib.w4_ope_complete import verify_classical_limit
        r = verify_classical_limit()
        assert r['c334_limit_correct']

    def test_c444_classical_limit_is_48_25(self):
        """c_444^2 -> 48/25 as c -> infinity."""
        from compute.lib.w4_ope_complete import verify_classical_limit
        r = verify_classical_limit()
        assert r['c444_limit_correct']

    def test_all_zeros_vanish(self):
        """Known zeros of c_334^2 and c_444^2 are actual zeros."""
        from compute.lib.w4_ope_complete import analyze_zero_pole_structure
        r = analyze_zero_pole_structure()
        assert r['all_zeros_vanish']

    def test_c334_zero_at_c0(self):
        """c_334^2 vanishes at c=0 (trivial theory)."""
        from compute.lib.w4_ds_ope_extraction import c334_squared_formula
        assert c334_squared_formula(Rational(0)) == 0


# ═══════════════════════════════════════════════════════════════
# K. Metric adjoint relations
# ═══════════════════════════════════════════════════════════════

class TestMetricAdjoint:
    """Metric adjoint (invariant form) relations between OPE coefficients."""

    def test_c343_over_c334_is_9_16(self):
        """C_{3,4;3;0,4}^2 / c_334^2 = 9/16."""
        from compute.lib.w4_ope_complete import verify_metric_adjoint_relations
        r = verify_metric_adjoint_relations()
        assert r['C_343_correct']

    def test_c344_over_c334_is_5_7(self):
        """C_{3,4;4;0,3}^2 / c_334^2 = 5/7."""
        from compute.lib.w4_ope_complete import verify_metric_adjoint_relations
        r = verify_metric_adjoint_relations()
        assert r['C_344_correct']

    def test_metric_adjoint_via_miura(self):
        """Verify metric adjoint from actual Miura extraction at k=1."""
        from compute.lib.w4_ope_complete import extract_structure_constants
        from compute.lib.w4_ds_ope_extraction import c334_squared_formula, c343_formula
        data = extract_structure_constants(K_TEST)
        c_val = data['c']
        if expand(data['c334_sq']) != 0:
            ratio = cancel(data['C_34_3_04_sq'] / data['c334_sq'])
            expected = cancel(c343_formula(c_val) / c334_squared_formula(c_val))
            assert simplify(ratio - expected) == 0


# ═══════════════════════════════════════════════════════════════
# L. MC4 stabilization
# ═══════════════════════════════════════════════════════════════

class TestMC4Stabilization:
    """MC4 coefficient stabilization at stage 4."""

    @pytest.mark.slow
    def test_stabilization_two_levels(self):
        """Structure constants match known formulas at k=1 and k=2."""
        from compute.lib.w4_ope_complete import verify_against_known_formulas
        for k in [K_TEST, K_TEST2]:
            r = verify_against_known_formulas(k)
            assert r['c334_match'], f"c334 unstable at k={k}"
            assert r['C_44_T_is_2'], f"Ward identity fails at k={k}"
            assert r['C_34_T_is_0'], f"Mixed vanishing fails at k={k}"

    def test_stage4_packet_at_k1(self):
        """Stage-4 packet extraction at k=1."""
        from compute.lib.w4_ope_complete import extract_stage4_packet
        p = extract_stage4_packet(K_TEST)
        assert p['w3_primary']
        assert p['w4_primary']
        assert p['C_34_T_zero']

    def test_bar_differential_input(self):
        """Bar differential input computation succeeds."""
        from compute.lib.w4_ope_complete import compute_bar_differential_input
        bar = compute_bar_differential_input(K_TEST)
        assert bar['c'] == C_TEST
        assert bar['w3_primary']
        assert bar['w4_primary']
        # Stage-3 coefficients should be finite
        s3 = bar['stage3']
        assert expand(s3['C_TT_T']) != 0
        assert expand(s3['C_TW3_W3']) != 0


# ═══════════════════════════════════════════════════════════════
# M. Unitary minimal models
# ═══════════════════════════════════════════════════════════════

class TestUnitaryMinimalModels:
    """Structure constants at unitary minimal models."""

    def test_unitarity_at_p5(self):
        """At p=5 (c=1): c_334^2 >= 0 and c_444^2 >= 0."""
        from compute.lib.w4_ope_complete import w4_unitary_minimal_models
        models = w4_unitary_minimal_models(max_p=6)
        p5 = [m for m in models if m['p'] == 5][0]
        assert p5['c'] == 1
        assert p5['unitary_ok']

    def test_unitarity_p5_through_p8(self):
        """All structure constants non-negative for p=5,...,8."""
        from compute.lib.w4_ope_complete import w4_unitary_minimal_models
        models = w4_unitary_minimal_models(max_p=8)
        for m in models:
            assert m['unitary_ok'], f"Unitarity fails at p={m['p']}, c={m['c']}"


# ═══════════════════════════════════════════════════════════════
# N. Cross-consistency checks
# ═══════════════════════════════════════════════════════════════

class TestCrossConsistency:
    """Cross-consistency between different extraction methods."""

    def test_c334_from_two_methods(self):
        """c_334^2 from analyze_w3w3_ope matches extract_structure_constants."""
        from compute.lib.w4_ope_complete import analyze_w3w3_ope, extract_structure_constants
        r1 = analyze_w3w3_ope(K_TEST)
        r2 = extract_structure_constants(K_TEST)
        assert simplify(r1['c334_sq'] - r2['c334_sq']) == 0

    def test_c444_from_two_methods(self):
        """c_444^2 from analyze_w4w4_ope matches extract_structure_constants."""
        from compute.lib.w4_ope_complete import analyze_w4w4_ope, extract_structure_constants
        r1 = analyze_w4w4_ope(K_TEST)
        r2 = extract_structure_constants(K_TEST)
        assert simplify(r1['c444_sq'] - r2['c444_sq']) == 0

    def test_pole_orders_consistent(self):
        """OPE pole orders from compute_all_opes match individual analyses."""
        from compute.lib.w4_ope_complete import ope_pole_orders, compute_all_opes
        opes = compute_all_opes(K_TEST)
        poles = ope_pole_orders(opes)
        # TT should have poles <= 4
        assert all(p <= 4 for p in poles['TT'])
        # TW3 should have poles <= 2
        assert all(p <= 2 for p in poles['TW3'])
        # TW4 should have poles <= 2
        assert all(p <= 2 for p in poles['TW4'])
        # W3W3 should have poles <= 6
        assert all(p <= 6 for p in poles['W3W3'])
        # W4W4 should have poles <= 8
        assert all(p <= 8 for p in poles['W4W4'])


# ═══════════════════════════════════════════════════════════════
# Full extraction report (integration test)
# ═══════════════════════════════════════════════════════════════

class TestFullReport:
    """Integration test: full extraction report."""

    @pytest.mark.slow
    def test_full_report_at_k1(self):
        """Full extraction report at k=1: all checks pass."""
        from compute.lib.w4_ope_complete import full_extraction_report
        report = full_extraction_report(K_TEST)
        summary = report['summary']
        failures = [k for k, v in summary.items() if v is False]
        assert summary['ALL_PASS'], f"Failures: {failures}"
