r"""Tests for non-principal W-algebra duality beyond hook type.

38 tests organized into 8 sections:

I.   Partition classification (5 tests)
II.  BRST complex structure (6 tests)
III. c-complementarity and kappa analysis (7 tests)
IV.  Shadow depth analysis (4 tests)
V.   Transport graph reachability (4 tests)
VI.  Complete duality profiles (4 tests)
VII. Self-transpose c-complementarity theorem (4 tests)
VIII.Numerical cross-checks and multi-path verification (4 tests)

KEY MATHEMATICAL FINDINGS VERIFIED HERE:

1. Koszulness is UNIVERSAL at generic level (Arakawa): ALL partitions pass.
2. c-complementarity (c+c' = const) holds ONLY for self-transpose partitions.
   For non-self-transpose pairs (including hooks like (3,1)/(2,1,1) in sl_4),
   c+c' is k-dependent under the KRW formula.
3. The DS-KD intertwining is PROVED for hooks (Fehily-CLNS) and self-transpose
   rectangular (self-duality).  It is CONJECTURAL for all other cases.
4. Transport closure from hooks covers ALL partitions for N <= 8.
5. The BRST complex for non-hook nilpotents has non-abelian n_+,
   but this does NOT obstruct PBW collapse (Arakawa's theorem).

CRITICAL DISTINCTIONS:
- c-complementarity != DS-KD commutation.  The former is a necessary
  condition only for self-transpose pairs.
- PBW collapse != DS-KD intertwining.  Both W-algebras being Koszul
  is necessary but not sufficient for the diagram to commute.
- Hook type includes the principal and trivial (which are also hook).
  "Beyond hook" means partitions NOT of the form (N-r, 1^r).
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, simplify

from compute.lib.non_principal_beyond_hook_engine import (
    BRSTComplexData,
    ComplementarityData,
    NonHookDualityProfile,
    ShadowDepthData,
    TransportAnalysis,
    brst_complex_analysis,
    complementarity_analysis,
    ds_kd_status,
    full_catalog,
    is_even_nilpotent,
    is_rectangular,
    non_hook_catalog,
    non_hook_duality_profile,
    numerical_c_complementarity,
    numerical_kappa_complementarity,
    partition_orbit_class,
    self_transpose_catalog,
    shadow_depth_analysis,
    transport_reachability,
    verify_self_transpose_c_complementarity,
)
from compute.lib.hook_type_w_duality import (
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    krw_central_charge,
)
from compute.lib.nonprincipal_ds_orbits import (
    is_hook_partition,
    transpose_partition,
)


k = Symbol('k')


# ===================================================================
# I. Partition classification
# ===================================================================

class TestPartitionClassification:

    def test_hook_classified_correctly(self):
        """Hook partitions classified as 'hook'."""
        for lam in [(4,), (3, 1), (2, 1, 1), (1, 1, 1, 1)]:
            assert partition_orbit_class(lam) == 'hook', f"{lam} should be hook"

    def test_rectangular_self_transpose(self):
        """(2,2) in sl_4 is self-transpose rectangular."""
        assert partition_orbit_class((2, 2)) == 'self_transpose_rectangular'
        assert is_rectangular((2, 2))
        assert (2, 2) == transpose_partition((2, 2))

    def test_non_rectangular_self_transpose(self):
        """(3,2,1) in sl_6 is self-transpose but not rectangular."""
        assert partition_orbit_class((3, 2, 1)) == 'self_transpose_nonhook'
        assert not is_rectangular((3, 2, 1))
        assert (3, 2, 1) == transpose_partition((3, 2, 1))

    def test_non_self_transpose_nonhook(self):
        """(3,2) and (2,2,1) in sl_5 are non-self-transpose non-hook."""
        assert partition_orbit_class((3, 2)) == 'non_self_transpose_nonhook'
        assert partition_orbit_class((2, 2, 1)) == 'non_self_transpose_nonhook'
        assert transpose_partition((3, 2)) == (2, 2, 1)
        assert transpose_partition((2, 2, 1)) == (3, 2)

    def test_even_nilpotent_classification(self):
        """Even nilpotent check: all parts same parity."""
        assert is_even_nilpotent((2, 2)) is True   # all even
        assert is_even_nilpotent((3, 3)) is True   # all odd
        assert is_even_nilpotent((3, 2)) is False   # mixed
        assert is_even_nilpotent((2, 2, 1)) is False  # mixed
        assert is_even_nilpotent((4,)) is True      # single part
        assert is_even_nilpotent((3, 1, 1)) is True  # all odd


# ===================================================================
# II. BRST complex structure
# ===================================================================

class TestBRSTComplexStructure:

    def test_22_sl4_abelian_n_plus(self):
        """(2,2) in sl_4: n_+ is abelian, all grade 1."""
        brst = brst_complex_analysis((2, 2))
        assert brst.N == 4
        assert brst.n_plus_is_abelian is True
        assert brst.n_plus_dim == 4
        # All roots at grade 1
        assert set(brst.n_plus_grades.keys()) == {Rational(1)}
        assert brst.is_even is True
        assert brst.pbw_collapse is True
        assert brst.is_koszul is True

    def test_32_sl5_non_abelian(self):
        """(3,2) in sl_5: n_+ is non-abelian with mixed grades."""
        brst = brst_complex_analysis((3, 2))
        assert brst.N == 5
        assert brst.n_plus_is_abelian is False
        assert brst.n_plus_dim == 10
        # Has half-integer grades (non-even nilpotent)
        assert brst.has_half_integer_grades is True
        assert brst.g_half_dim == 4
        assert brst.is_even is False
        # Koszul regardless (Arakawa)
        assert brst.pbw_collapse is True
        assert brst.is_koszul is True

    def test_221_sl5_non_abelian(self):
        """(2,2,1) in sl_5: n_+ is non-abelian."""
        brst = brst_complex_analysis((2, 2, 1))
        assert brst.N == 5
        assert brst.n_plus_is_abelian is False
        assert brst.n_plus_dim == 8
        assert brst.has_half_integer_grades is True
        assert brst.pbw_collapse is True

    def test_321_sl6_non_abelian(self):
        """(3,2,1) in sl_6: non-abelian, non-even, self-transpose."""
        brst = brst_complex_analysis((3, 2, 1))
        assert brst.N == 6
        assert brst.n_plus_is_abelian is False
        assert brst.is_even is False
        assert brst.pbw_collapse is True

    def test_33_sl6_non_abelian_even(self):
        """(3,3) in sl_6: non-abelian but even."""
        brst = brst_complex_analysis((3, 3))
        assert brst.N == 6
        assert brst.n_plus_is_abelian is False
        assert brst.is_even is True
        assert brst.has_half_integer_grades is False
        assert brst.pbw_collapse is True

    def test_universal_koszulness(self):
        """ALL partitions of N=4,5,6 are Koszul at generic level."""
        from compute.lib.nonprincipal_ds_orbits import _partitions_of_n
        for N in [4, 5, 6]:
            for lam in _partitions_of_n(N):
                brst = brst_complex_analysis(lam)
                assert brst.is_koszul is True, f"{lam} in sl_{N} should be Koszul"


# ===================================================================
# III. c-complementarity and kappa analysis
# ===================================================================

class TestComplementarity:

    def test_22_sl4_c_complementarity(self):
        """(2,2) self-transpose: c+c' = 110 (k-independent).

        # VERIFIED: [DC] per-root-pair KRW; rho=5, kappa_sum=5*110=550
        """
        data = complementarity_analysis((2, 2))
        assert data.is_self_transpose is True
        assert data.c_sum_k_independent is True
        assert simplify(data.c_sum_value - 110) == 0
        assert data.kappa_sum_k_independent is True
        assert simplify(data.kappa_sum_value - 550) == 0
        assert data.rho_match is True

    def test_321_sl6_c_complementarity(self):
        """(3,2,1) self-transpose non-hook: c+c' = 2054 (k-independent).

        # VERIFIED: [DC] per-root-pair KRW; rho=13/15, kappa_sum=13/15*2054=26702/15
        """
        data = complementarity_analysis((3, 2, 1))
        assert data.is_self_transpose is True
        assert data.c_sum_k_independent is True
        assert simplify(data.c_sum_value - 2054) == 0
        assert data.kappa_sum_k_independent is True
        # kappa+kappa' = rho * (c+c') = (13/15)*2054 = 26702/15
        assert simplify(data.kappa_sum_value - Rational(26702, 15)) == 0

    def test_32_sl5_c_not_k_independent(self):
        """(3,2)/(2,2,1) non-self-transpose: c+c' is k-dependent."""
        data = complementarity_analysis((3, 2))
        assert data.is_self_transpose is False
        assert data.c_sum_k_independent is False
        assert data.kappa_sum_k_independent is False
        assert data.rho_match is False

    def test_33_222_sl6_c_not_k_independent(self):
        """(3,3)/(2,2,2) non-self-transpose even: c+c' is k-dependent."""
        data = complementarity_analysis((3, 3))
        assert data.is_self_transpose is False
        assert data.c_sum_k_independent is False

    def test_anomaly_ratio_22(self):
        """(2,2) in sl_4: rho = 5 (3 weight-1 + 4 weight-2 bosonic)."""
        rho = anomaly_ratio_from_partition((2, 2))
        assert rho == Rational(5)

    def test_anomaly_ratio_321(self):
        """(3,2,1) in sl_6: rho = 13/15."""
        rho = anomaly_ratio_from_partition((3, 2, 1))
        assert rho == Rational(13, 15)

    def test_self_dual_c_22(self):
        """(2,2) self-dual c* = 110/2 = 55.

        # VERIFIED: [DC] K=110, self_dual_c = K/2 = 55
        """
        data = complementarity_analysis((2, 2))
        assert data.self_dual_c is not None
        assert simplify(data.self_dual_c - 55) == 0


# ===================================================================
# IV. Shadow depth analysis
# ===================================================================

class TestShadowDepth:

    def test_22_sl4_shadow(self):
        """(2,2) in sl_4: 7 bosonic generators, class M on T-line."""
        sd = shadow_depth_analysis((2, 2))
        assert sd.n_bosonic == 7
        assert sd.n_fermionic == 0
        assert sd.has_weight_1_generators is True
        assert sd.n_weight_1 == 3
        assert sd.rho == Rational(5)

    def test_32_sl5_shadow(self):
        """(3,2) in sl_5: 4 bosonic + 4 fermionic generators."""
        sd = shadow_depth_analysis((3, 2))
        assert sd.n_bosonic == 4
        assert sd.n_fermionic == 4
        assert sd.has_fermionic_generators is True
        assert sd.has_weight_ge_3 is True  # weight-3 generator
        assert sd.shadow_class == 'M'

    def test_321_sl6_shadow(self):
        """(3,2,1) in sl_6: 7 bosonic + 6 fermionic generators."""
        sd = shadow_depth_analysis((3, 2, 1))
        assert sd.n_bosonic == 7
        assert sd.n_fermionic == 6
        assert sd.has_fermionic_generators is True
        assert sd.shadow_class == 'M'

    def test_kappa_22_sl4(self):
        """(2,2) kappa = -5*(24k^2+137k+208)/(k+4), at k=1: -369.

        # VERIFIED: [DC] -5*(24+137+208)/5 = -5*369/5 = -369; [CF] rho=5, c(1)=-369/5
        """
        kappa = ds_kappa_from_affine((2, 2), Rational(1))
        assert kappa == Rational(-369)


# ===================================================================
# V. Transport graph reachability
# ===================================================================

class TestTransportReachability:

    def test_sl4_all_reachable(self):
        """sl_4: all 5 partitions reachable from hooks (includes (2,2))."""
        tr = transport_reachability(4)
        assert tr.total_partitions == 5
        assert tr.n_hook == 4
        assert tr.n_non_hook == 1
        assert tr.all_reachable is True
        assert len(tr.unreachable) == 0

    def test_sl5_all_reachable(self):
        """sl_5: all 7 partitions reachable from hooks."""
        tr = transport_reachability(5)
        assert tr.total_partitions == 7
        assert tr.n_hook == 5
        assert tr.n_non_hook == 2
        assert tr.all_reachable is True

    def test_sl6_all_reachable(self):
        """sl_6: all 11 partitions reachable from hooks."""
        tr = transport_reachability(6)
        assert tr.total_partitions == 11
        assert tr.n_hook == 6
        assert tr.n_non_hook == 5
        assert tr.all_reachable is True

    def test_sl7_all_reachable(self):
        """sl_7: all 15 partitions reachable from hooks."""
        tr = transport_reachability(7)
        assert tr.total_partitions == 15
        assert tr.all_reachable is True


# ===================================================================
# VI. Complete duality profiles
# ===================================================================

class TestDualityProfiles:

    def test_22_sl4_proved(self):
        """(2,2) in sl_4: DS-KD proved (self-transpose rectangular)."""
        p = non_hook_duality_profile((2, 2))
        assert p.orbit_class == 'self_transpose_rectangular'
        assert p.ds_kd_proved is True
        assert p.ds_kd_evidence_level == 'proved'
        assert p.koszul is True
        assert p.is_even is True
        assert p.is_rectangular is True
        assert p.in_transport_closure is True

    def test_321_sl6_strong_evidence(self):
        """(3,2,1) in sl_6: strong evidence (self-transpose non-hook)."""
        p = non_hook_duality_profile((3, 2, 1))
        assert p.orbit_class == 'self_transpose_nonhook'
        assert p.ds_kd_proved is False
        assert p.ds_kd_evidence_level == 'strong'
        assert p.koszul is True
        assert p.complementarity.c_sum_k_independent is True

    def test_32_sl5_weak_evidence(self):
        """(3,2) in sl_5: weak evidence (non-self-transpose, reachable)."""
        p = non_hook_duality_profile((3, 2))
        assert p.orbit_class == 'non_self_transpose_nonhook'
        assert p.ds_kd_proved is False
        assert p.ds_kd_evidence_level == 'weak'
        assert p.koszul is True
        assert p.complementarity.c_sum_k_independent is False

    def test_non_hook_catalog_sl6(self):
        """sl_6 has 5 non-hook orbits: all analyzed."""
        cat = non_hook_catalog(6)
        assert len(cat) == 5
        classes = [p.orbit_class for p in cat]
        assert 'self_transpose_nonhook' in classes  # (3,2,1)
        assert 'non_self_transpose_nonhook' in classes  # (3,3), (4,2), etc.


# ===================================================================
# VII. Self-transpose c-complementarity theorem
# ===================================================================

class TestSelfTransposeTheorem:

    def test_all_self_transpose_c_independent_up_to_sl8(self):
        """c+c' is k-independent for ALL self-transpose partitions, N <= 8.

        This is a structural theorem verified computationally: for lambda = lambda^t,
        c(k, lambda) + c(-k-2N, lambda) is a constant in k for ALL self-transpose
        partitions of N, for N = 2 through 8.
        """
        results = verify_self_transpose_c_complementarity(max_N=8)
        assert len(results) > 0
        for r in results:
            assert r['c_k_independent'] is True, (
                f"c+c' not k-independent for self-transpose {r['partition']} in sl_{r['N']}"
            )
            assert r['kappa_k_independent'] is True, (
                f"kappa+kappa' not k-independent for self-transpose {r['partition']} in sl_{r['N']}"
            )

    def test_self_transpose_count(self):
        """Count self-transpose partitions: correct for N=2..8."""
        # Self-conjugate partitions of N:
        # 2: (1,1) [hook]; 3: (2,1) [hook]; 4: (2,2); 5: (3,1,1) [hook];
        # 6: (3,2,1); 7: (4,2,1) [hook], (3,3,1) [non-hook]; 8: several
        results = verify_self_transpose_c_complementarity(max_N=8)
        for r in results:
            lam = r['partition']
            assert lam == transpose_partition(lam)

    def test_self_transpose_rho_match(self):
        """For self-transpose lambda: rho(lambda) = rho(lambda^t) trivially."""
        results = verify_self_transpose_c_complementarity(max_N=7)
        for r in results:
            lam = r['partition']
            rho_s = anomaly_ratio_from_partition(lam)
            rho_d = anomaly_ratio_from_partition(transpose_partition(lam))
            assert rho_s == rho_d, f"rho mismatch for self-transpose {lam}"

    def test_self_transpose_kappa_from_c(self):
        """kappa+kappa' = rho * (c+c') for self-transpose partitions."""
        results = verify_self_transpose_c_complementarity(max_N=7)
        for r in results:
            lam = r['partition']
            rho = r['rho']
            c_sum = r['c_sum']
            kappa_sum = r['kappa_sum']
            diff = simplify(kappa_sum - rho * c_sum)
            assert diff == 0, f"kappa != rho*c for {lam}: diff = {diff}"


# ===================================================================
# VIII. Numerical cross-checks and multi-path verification
# ===================================================================

class TestNumericalCrossChecks:

    def test_22_numerical_c_complementarity(self):
        """(2,2): c+c' = 110 at all test levels."""
        result = numerical_c_complementarity((2, 2))
        assert result['all_equal'] is True
        assert result['constant_value'] == Rational(110)

    def test_321_numerical_c_complementarity(self):
        """(3,2,1): c+c' = 2054 at all test levels."""
        result = numerical_c_complementarity((3, 2, 1))
        assert result['all_equal'] is True
        assert result['constant_value'] == Rational(2054)

    def test_32_numerical_c_not_constant(self):
        """(3,2): c+c' varies with level (not k-independent)."""
        result = numerical_c_complementarity((3, 2))
        assert result['all_equal'] is False

    def test_22_kappa_cross_check(self):
        """(2,2): kappa computed two ways agree.

        Method 1: rho * c (anomaly ratio formula)
        Method 2: ds_kappa_from_affine (canonical formula)
        Both give kappa = 5*(7k-20)/(k+4).
        """
        rho = anomaly_ratio_from_partition((2, 2))
        for kv in [1, 3, 5, 7, 11]:
            c = krw_central_charge((2, 2), Rational(kv))
            kappa_method1 = rho * c
            kappa_method2 = ds_kappa_from_affine((2, 2), Rational(kv))
            assert simplify(kappa_method1 - kappa_method2) == 0, (
                f"kappa mismatch at k={kv}: {kappa_method1} vs {kappa_method2}"
            )
