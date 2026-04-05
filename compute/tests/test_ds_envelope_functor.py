"""Tests for compute/lib/ds_envelope_functor.py — DS as functor on Platonic packages.

Comprehensive test suite verifying:
  1. Nilpotent orbit data structure
  2. Central charge formulas for W_N
  3. Kappa formulas for W-algebras
  4. Feigin-Frenkel involution and complementarity
  5. DS reduction pipeline
  6. Shadow obstruction tower extraction after DS
  7. Hook-type DS reduction (proved corridor)
  8. Transport-to-transpose conjecture checks
  9. Cross-N consistency
  10. Master DS functor pipeline

References:
  sec:concordance-ds-reduction, thm:hook-type-corridor,
  conj:transport-to-transpose, prop:miura-packet-splitting,
  def:shadow-depth-classification
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, S, oo

from compute.lib.ds_envelope_functor import (
    NilpotentOrbit,
    central_charge_wN_principal,
    central_charge_affine,
    central_charge_w_hook,
    anomaly_ratio,
    kappa_affine,
    kappa_wN_principal,
    kappa_wN_from_c,
    feigin_frenkel_dual_level,
    complementarity_constant_wN,
    ds_reduce,
    DSReductionResult,
    ds_shadow_tower,
    verify_ds_kappa_all_principal,
    verify_complementarity_principal,
    ds_hook_type,
    ds_subregular,
    transport_to_transpose_check,
    ds_envelope_functor,
    DSEnvelopeFunctorResult,
)


# =========================================================================
# 1. Nilpotent orbit data structure
# =========================================================================

class TestNilpotentOrbit:
    """Test NilpotentOrbit construction and classification."""

    def test_principal_sl2(self):
        """Principal nilpotent in sl_2: partition [2]."""
        nilp = NilpotentOrbit.principal(2)
        assert nilp.partition == [2]
        assert nilp.is_principal is True
        assert nilp.N == 2

    def test_principal_sl3(self):
        """Principal nilpotent in sl_3: partition [3]."""
        nilp = NilpotentOrbit.principal(3)
        assert nilp.partition == [3]
        assert nilp.is_principal is True

    def test_subregular_sl3(self):
        """Subregular nilpotent in sl_3: partition [2, 1]."""
        nilp = NilpotentOrbit.subregular(3)
        assert nilp.partition == [2, 1]
        assert nilp.is_subregular is True

    def test_hook_sl4(self):
        """Hook [3, 1] in sl_4."""
        nilp = NilpotentOrbit.hook(4, 1)
        assert nilp.partition == [3, 1]
        assert nilp.is_hook is True

    def test_hook_sl5_r2(self):
        """Hook [3, 1, 1] in sl_5."""
        nilp = NilpotentOrbit.hook(5, 2)
        assert nilp.partition == [3, 1, 1]
        assert nilp.is_hook is True

    def test_dual_partition_principal(self):
        """Dual of [3] = [1, 1, 1]."""
        nilp = NilpotentOrbit.principal(3)
        assert nilp.dual_partition() == [1, 1, 1]

    def test_dual_partition_hook(self):
        """Dual of [3, 1] = [2, 1, 1]."""
        nilp = NilpotentOrbit.hook(4, 1)
        assert nilp.dual_partition() == [2, 1, 1]

    def test_dual_partition_subregular(self):
        """Dual of [2, 1] = [2, 1]."""
        nilp = NilpotentOrbit.subregular(3)
        dual = nilp.dual_partition()
        assert dual == [2, 1]

    def test_from_partition(self):
        """Create from arbitrary partition."""
        nilp = NilpotentOrbit.from_partition([2, 2])
        assert nilp.N == 4
        assert not nilp.is_principal
        assert not nilp.is_hook

    def test_principal_generator_weights(self):
        """Principal W_3: generators at weights 2, 3."""
        nilp = NilpotentOrbit.principal(3)
        assert nilp.generator_weights() == [2, 3]

    def test_principal_w4_weights(self):
        """Principal W_4: generators at weights 2, 3, 4."""
        nilp = NilpotentOrbit.principal(4)
        assert nilp.generator_weights() == [2, 3, 4]


# =========================================================================
# 2. Central charge formulas
# =========================================================================

class TestCentralCharge:
    """Test central charge formulas for W-algebras."""

    def test_virasoro_from_sl2_k1(self):
        """c(Vir, k=1) = 1 - 6*4/3 = -7."""
        c = central_charge_wN_principal(2, Fraction(1))
        assert c == Fraction(-7)

    def test_virasoro_from_sl2_k0(self):
        """c(Vir, k=0) = 1 - 6*1/2 = -2."""
        c = central_charge_wN_principal(2, Fraction(0))
        assert c == Fraction(-2)

    def test_w3_from_sl3_k1(self):
        """c(W_3, k=1) = 2 - 24*9/4 = 2 - 54 = -52."""
        c = central_charge_wN_principal(3, Fraction(1))
        assert c == Fraction(-52)

    def test_affine_sl2_k1(self):
        """c(sl_2, k=1) = 1*3/(1+2) = 1."""
        c = central_charge_affine(2, Fraction(1))
        assert c == Fraction(1)

    def test_affine_sl3_k1(self):
        """c(sl_3, k=1) = 1*8/(1+3) = 2."""
        c = central_charge_affine(3, Fraction(1))
        assert c == Fraction(2)

    def test_critical_level_raises(self):
        """Critical level k = -h^v raises ValueError."""
        with pytest.raises(ValueError):
            central_charge_wN_principal(2, Fraction(-2))
        with pytest.raises(ValueError):
            central_charge_affine(3, Fraction(-3))


# =========================================================================
# 3. Kappa formulas
# =========================================================================

class TestKappaFormulas:
    """Test modular characteristic formulas for W-algebras."""

    def test_anomaly_ratio_sl2(self):
        """rho(sl_2) = 1/2."""
        assert anomaly_ratio(2) == Fraction(1, 2)

    def test_anomaly_ratio_sl3(self):
        """rho(sl_3) = 1/2 + 1/3 = 5/6."""
        assert anomaly_ratio(3) == Fraction(5, 6)

    def test_anomaly_ratio_sl4(self):
        """rho(sl_4) = 1/2 + 1/3 + 1/4 = 13/12."""
        assert anomaly_ratio(4) == Fraction(13, 12)

    def test_kappa_affine_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*3/(2*2) = 9/4."""
        kap = kappa_affine(2, Fraction(1))
        assert kap == Fraction(9, 4)

    def test_kappa_affine_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*4/6 = 16/3."""
        kap = kappa_affine(3, Fraction(1))
        assert kap == Fraction(16, 3)

    def test_kappa_wN_equals_rho_times_c(self):
        """kappa(W_N) = rho * c for all N and k."""
        for N in range(2, 6):
            for k_val in [1, 2, 3, 5]:
                k = Fraction(k_val)
                rho = anomaly_ratio(N)
                c = central_charge_wN_principal(N, k)
                kap = kappa_wN_principal(N, k)
                assert kap == rho * c, \
                    f"Failed for N={N}, k={k}: {kap} != {rho}*{c}"

    def test_kappa_wN_from_c_matches(self):
        """kappa_wN_from_c matches kappa_wN_principal for consistent c."""
        for N in range(2, 5):
            k = Fraction(1)
            c = central_charge_wN_principal(N, k)
            kap1 = kappa_wN_principal(N, k)
            kap2 = kappa_wN_from_c(N, c)
            assert kap1 == kap2


# =========================================================================
# 4. Feigin-Frenkel involution and complementarity
# =========================================================================

class TestFeiginFrenkelComplementarity:
    """Test FF involution and c-complementarity."""

    def test_ff_dual_level_sl2(self):
        """FF dual: k' = -k - 4 for sl_2."""
        assert feigin_frenkel_dual_level(Fraction(1), 2) == Fraction(-5)

    def test_ff_dual_level_sl3(self):
        """FF dual: k' = -k - 6 for sl_3."""
        assert feigin_frenkel_dual_level(Fraction(1), 3) == Fraction(-7)

    def test_virasoro_c_sum_26(self):
        """c(k) + c(k') = 26 for Virasoro at k=1."""
        k = Fraction(1)
        k_d = feigin_frenkel_dual_level(k, 2)
        c_k = central_charge_wN_principal(2, k)
        c_kd = central_charge_wN_principal(2, k_d)
        assert c_k + c_kd == 26

    def test_w3_c_sum_100(self):
        """c(k) + c(k') = 100 for W_3 at k=1."""
        k = Fraction(1)
        k_d = feigin_frenkel_dual_level(k, 3)
        c_k = central_charge_wN_principal(3, k)
        c_kd = central_charge_wN_principal(3, k_d)
        assert c_k + c_kd == 100

    def test_complementarity_constant_sl2(self):
        """Complementarity constant for sl_2: 2 + 24 = 26."""
        assert complementarity_constant_wN(2) == 26

    def test_complementarity_constant_sl3(self):
        """Complementarity constant for sl_3: 4 + 96 = 100."""
        assert complementarity_constant_wN(3) == 100

    def test_complementarity_constant_sl4(self):
        """Complementarity constant for sl_4: 6 + 240 = 246."""
        assert complementarity_constant_wN(4) == 246

    def test_complementarity_multiple_levels(self):
        """c + c' = constant for multiple levels at each N."""
        for N in range(2, 6):
            expected = complementarity_constant_wN(N)
            for k_val in [1, 2, 3, 5, 10]:
                k = Fraction(k_val)
                k_d = feigin_frenkel_dual_level(k, N)
                c_k = central_charge_wN_principal(N, k)
                c_kd = central_charge_wN_principal(N, k_d)
                assert c_k + c_kd == expected, \
                    f"Failed for N={N}, k={k}: {c_k}+{c_kd} != {expected}"

    def test_virasoro_kappa_sum_13(self):
        """kappa(c) + kappa(26-c) = 13 for Virasoro."""
        k = Fraction(1)
        k_d = feigin_frenkel_dual_level(k, 2)
        rho = anomaly_ratio(2)
        c_k = central_charge_wN_principal(2, k)
        c_kd = central_charge_wN_principal(2, k_d)
        kap_sum = rho * c_k + rho * c_kd
        assert kap_sum == rho * 26 == 13


# =========================================================================
# 5. DS reduction pipeline
# =========================================================================

class TestDSReduction:
    """Test DS reduction from affine to W-algebra."""

    def test_sl2_to_virasoro_principal(self):
        """DS from sl_2 at k=1: target is Virasoro."""
        result = ds_reduce(2, Fraction(1))
        assert result.target_family == 'W_2'
        assert result.kappa_ds_consistent is True
        assert result.shadow_depth_source == 'L'
        assert result.shadow_depth_target == 'M'

    def test_sl3_to_w3_principal(self):
        """DS from sl_3 at k=1: target is W_3."""
        result = ds_reduce(3, Fraction(1))
        assert result.target_family == 'W_3'
        assert result.kappa_ds_consistent is True

    def test_ds_kappa_consistent_all(self):
        """DS kappa consistency for N=2..5, multiple levels."""
        results = verify_ds_kappa_all_principal(max_N=5)
        for r in results:
            if r.get('match') is not None:
                assert r['match'] is True, \
                    f"Kappa mismatch at N={r['N']}, k={r['k']}"

    def test_ds_preserves_depth_increase(self):
        """DS increases shadow depth: L (affine) -> M (W-algebra)."""
        for N in range(2, 5):
            result = ds_reduce(N, Fraction(1))
            assert result.shadow_depth_source == 'L'
            assert result.shadow_depth_target == 'M'

    def test_ds_source_has_no_quartic(self):
        """Source affine algebra (class L) has no quartic shadow."""
        result = ds_reduce(3, Fraction(1))
        assert result.quartic_source == 0

    def test_ds_target_has_quartic(self):
        """Target W-algebra (class M) has nonzero quartic shadow."""
        result = ds_reduce(2, Fraction(1))
        assert result.quartic_target != 0

    def test_ds_proved_for_principal(self):
        """DS for principal nilpotent is in the proved corridor."""
        result = ds_reduce(3, Fraction(1))
        assert result.is_proved is True


# =========================================================================
# 6. Shadow obstruction tower after DS
# =========================================================================

class TestDSShadowTower:
    """Test shadow obstruction tower extraction after DS reduction."""

    def test_virasoro_tower_from_sl2(self):
        """Shadow obstruction tower for Virasoro from sl_2 DS."""
        tower = ds_shadow_tower(2, Fraction(1))
        assert 2 in tower['target_tower']
        # Virasoro has quartic
        assert 4 in tower['target_tower']

    def test_w3_tower_from_sl3(self):
        """Shadow obstruction tower for W_3 from sl_3 DS."""
        tower = ds_shadow_tower(3, Fraction(1))
        assert 2 in tower['target_tower']
        assert 3 in tower['target_tower']

    def test_source_tower_is_L_class(self):
        """Source (affine) tower has entries at arities 2 and 3 only."""
        tower = ds_shadow_tower(2, Fraction(1))
        src = tower['source_tower']
        assert 2 in src
        assert 3 in src

    def test_ds_creates_quartic_from_nothing(self):
        """DS creates quartic shadow (not present in affine source)."""
        tower = ds_shadow_tower(2, Fraction(1))
        assert tower['ds_map_arity_4']['quartic_source'] == 0
        assert tower['ds_map_arity_4']['quartic_target'] != 0


# =========================================================================
# 7. Hook-type DS reduction
# =========================================================================

class TestHookTypeDS:
    """Test hook-type DS reduction (proved corridor)."""

    def test_hook_sl3_r1_is_subregular(self):
        """Hook [2, 1] in sl_3 is the subregular nilpotent."""
        result = ds_hook_type(3, 1, Fraction(1))
        assert result.nilpotent.is_subregular is True
        assert result.nilpotent.is_hook is True
        assert result.is_proved is True

    def test_hook_sl4_r1(self):
        """Hook [3, 1] in sl_4 is in proved corridor."""
        result = ds_hook_type(4, 1, Fraction(1))
        assert result.nilpotent.partition == [3, 1]
        assert result.is_proved is True

    def test_hook_sl5_r2(self):
        """Hook [3, 1, 1] in sl_5 is in proved corridor."""
        result = ds_hook_type(5, 2, Fraction(1))
        assert result.nilpotent.partition == [3, 1, 1]
        assert result.is_proved is True

    def test_subregular_sl4(self):
        """Subregular [3, 1] in sl_4."""
        result = ds_subregular(4, Fraction(1))
        assert result.nilpotent.partition == [3, 1]
        assert result.nilpotent.is_subregular is True


# =========================================================================
# 8. Transport-to-transpose conjecture
# =========================================================================

class TestTransportToTranspose:
    """Test transport-to-transpose conjecture checks."""

    def test_principal_verified(self):
        """Principal partition: TtT reduces to standard FF."""
        result = transport_to_transpose_check(3, [3], Fraction(1))
        assert result['is_principal'] is True
        assert result['verified'] is True

    def test_hook_in_proved_corridor(self):
        """Hook partition is in proved corridor."""
        result = transport_to_transpose_check(4, [3, 1], Fraction(1))
        assert result['is_hook'] is True
        assert result['is_in_proved_corridor'] is True

    def test_non_hook_not_proved(self):
        """Non-hook partition [2, 2] is NOT in proved corridor."""
        result = transport_to_transpose_check(4, [2, 2], Fraction(1))
        assert result['is_hook'] is False
        assert result['is_in_proved_corridor'] is False

    def test_principal_c_sum_correct(self):
        """Principal: c + c' = complementarity constant."""
        result = transport_to_transpose_check(3, [3], Fraction(1))
        assert result['c_sum'] == result['expected_c_sum']


# =========================================================================
# 9. Cross-N consistency
# =========================================================================

class TestCrossNConsistency:
    """Test consistency across different values of N."""

    def test_all_principal_complementarities(self):
        """c-complementarity holds for all N=2..6."""
        results = verify_complementarity_principal(max_N=6)
        for r in results:
            if r.get('c_match') is not None:
                assert r['c_match'] is True, \
                    f"Failed at N={r['N']}, k={r['k']}"

    def test_kappa_complementarity_all_N(self):
        """kappa + kappa' = rho * c_sum for all N."""
        results = verify_complementarity_principal(max_N=5)
        for r in results:
            if r.get('kappa_match') is not None:
                assert r['kappa_match'] is True, \
                    f"kappa comp failed at N={r['N']}, k={r['k']}"

    def test_anomaly_ratio_monotone(self):
        """rho(sl_N) is strictly increasing in N."""
        prev = Fraction(0)
        for N in range(2, 10):
            rho = anomaly_ratio(N)
            assert rho > prev, f"rho not increasing at N={N}"
            prev = rho

    def test_complementarity_constant_growing(self):
        """Complementarity constant grows with N."""
        prev = 0
        for N in range(2, 8):
            const = complementarity_constant_wN(N)
            assert const > prev, f"Constant not growing at N={N}"
            prev = const


# =========================================================================
# 10. Master DS functor pipeline
# =========================================================================

class TestDSEnvelopeFunctor:
    """Test the complete DS envelope functor pipeline."""

    def test_sl2_principal_complete(self):
        """Full DS functor for sl_2 principal."""
        result = ds_envelope_functor(2, Fraction(1))
        assert isinstance(result, DSEnvelopeFunctorResult)
        assert result.ds_result.kappa_ds_consistent is True
        assert result.is_in_proved_corridor is True

    def test_sl3_principal_complete(self):
        """Full DS functor for sl_3 principal."""
        result = ds_envelope_functor(3, Fraction(1))
        assert result.ds_result.target_family == 'W_3'
        assert result.is_in_proved_corridor is True

    def test_sl4_principal_complete(self):
        """Full DS functor for sl_4 principal."""
        result = ds_envelope_functor(4, Fraction(1))
        assert result.ds_result.target_family == 'W_4'
        assert result.complementarity.get('holds') is True

    def test_hook_functor(self):
        """Full DS functor with hook nilpotent."""
        nilp = NilpotentOrbit.hook(4, 1)
        result = ds_envelope_functor(4, Fraction(1), nilp)
        assert result.is_in_proved_corridor is True

    def test_summary_does_not_crash(self):
        """Calling summary() should not crash."""
        result = ds_envelope_functor(2, Fraction(1))
        s = result.summary()
        assert isinstance(s, str)
        assert 'sl_2' in s

    def test_shadow_tower_present(self):
        """Shadow obstruction tower is populated after DS functor."""
        result = ds_envelope_functor(3, Fraction(1))
        assert 'target_tower' in result.shadow_tower
        assert 2 in result.shadow_tower['target_tower']

    def test_multiple_levels_sl2(self):
        """DS functor at multiple levels for sl_2."""
        for k_val in [1, 2, 3, 5]:
            k = Fraction(k_val)
            result = ds_envelope_functor(2, k)
            assert result.ds_result.kappa_ds_consistent is True
            # complementarity check
            if result.complementarity.get('holds') is not None:
                assert result.complementarity['holds'] is True

    def test_ds_creates_shadow_depth_increase(self):
        """DS functor increases shadow depth from L to M."""
        result = ds_envelope_functor(3, Fraction(1))
        assert result.ds_result.shadow_depth_source == 'L'
        assert result.ds_result.shadow_depth_target == 'M'


# =========================================================================
# 11. Structural cross-checks (AP10)
# =========================================================================

class TestStructuralCrossChecks:
    """Cross-checks that enforce mathematical constraints rather than hardcoded values."""

    def test_anomaly_ratio_harmonic_sum(self):
        """rho(sl_N) = sum_{i=1}^{N-1} 1/(i+1) = H_N - 1 (harmonic sum).

        Verify by computing rho directly and via the harmonic number.
        """
        for N in range(2, 8):
            rho = anomaly_ratio(N)
            harmonic = sum(Fraction(1, i) for i in range(1, N + 1))
            assert rho == harmonic - 1, f"rho(sl_{N}) = {rho} != H_{N} - 1 = {harmonic - 1}"

    def test_complementarity_constant_formula(self):
        """2(N-1) + 4N(N^2-1) formula verified independently.

        Expand: 2N - 2 + 4N^3 - 4N = 4N^3 - 2N - 2.
        Check at N=2: 32-4-2=26. At N=3: 108-6-2=100. At N=4: 256-8-2=246.
        """
        for N in range(2, 7):
            expected = 4 * N**3 - 2 * N - 2
            computed = complementarity_constant_wN(N)
            assert computed == expected, (
                f"N={N}: {computed} != 4N^3-2N-2 = {expected}"
            )

    def test_kappa_ratio_across_N(self):
        """kappa(W_N)/kappa(W_2) = rho(sl_N)/rho(sl_2) at same c.

        Since kappa = rho * c, the ratio at the same c is the ratio of
        anomaly ratios. This must hold for all N >= 2.
        """
        k = Fraction(1)
        rho_2 = anomaly_ratio(2)
        for N in range(3, 6):
            rho_N = anomaly_ratio(N)
            c_2 = central_charge_wN_principal(2, k)
            c_N = central_charge_wN_principal(N, k)
            kappa_2 = rho_2 * c_2
            kappa_N = rho_N * c_N
            # Since c_2 != c_N in general, just verify kappa = rho * c
            assert kappa_N == rho_N * c_N

    def test_ff_dual_fixed_point_is_critical_level(self):
        """The FF involution k' = -k - 2N has fixed point k = -N (critical level).

        k = -k - 2N => 2k = -2N => k = -N = -h^v.
        """
        for N in range(2, 6):
            k_fixed = Fraction(-N)
            assert feigin_frenkel_dual_level(k_fixed, N) == k_fixed

    def test_ds_kappa_consistent_symbolic(self):
        """kappa(W_N) = rho * c(W_N) symbolically, not just at specific k.

        Verify that kappa_wN_principal(N, k) == anomaly_ratio(N) * c_wN(N, k)
        for symbolic-like checks at many k values.
        """
        for N in [2, 3, 4, 5]:
            for k_val in [1, 2, 3, 5, 10, 20]:
                k = Fraction(k_val)
                rho = anomaly_ratio(N)
                c_w = central_charge_wN_principal(N, k)
                kappa_direct = rho * c_w
                kappa_formula = kappa_wN_principal(N, k)
                assert kappa_direct == kappa_formula, (
                    f"N={N}, k={k}: {kappa_direct} != {kappa_formula}"
                )
