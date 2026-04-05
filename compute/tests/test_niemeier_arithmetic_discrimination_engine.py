r"""Tests for Niemeier lattice arithmetic discrimination engine.

Comprehensive test suite verifying:
  1. All 24 Niemeier lattices: shadow arithmetic invariants
  2. Kissing number extraction via 3 independent paths
  3. Shell distribution recovery and consistency
  4. Arithmetic depth classification
  5. Arithmetic conductor computation and factorization
  6. Hecke eigenform decomposition
  7. Ramanujan conjecture verification (Deligne's theorem)
  8. Tau multiplicativity
  9. Moonshine module V^natural analysis
  10. Cross-lattice discrimination cascade
  11. Multi-path verification for every claim

Mathematical ground truth:
  - Niemeier (1968): 24 even unimodular lattices in dimension 24
  - Conway-Sloane, Ch. 16: root systems, kissing numbers
  - Ramanujan (1916) / Deligne (1974): tau(n) properties
  - lattice_foundations.tex, arithmetic_shadows.tex
"""

import math
import pytest
from fractions import Fraction
from functools import lru_cache

from compute.lib.niemeier_arithmetic_discrimination_engine import (
    # Part 1: Root system extensions
    lie_algebra_dimension,
    dual_coxeter_number,
    weyl_group_order,
    exponents,
    # Part 2: Kissing number and shells
    kissing_number,
    kissing_number_true,
    shell_number,
    shell_distribution,
    kissing_from_theta,
    shell_determines_theta,
    # Part 3: Shadow ODE recovery
    shadow_ode_shell_recovery,
    verify_shadow_shell_consistency,
    # Part 4: Arithmetic depth
    arithmetic_depth,
    total_depth,
    depth_classification,
    # Part 5: Arithmetic conductor
    arithmetic_conductor,
    arithmetic_conductor_factored,
    conductor_discriminating_power,
    c_delta_fraction,
    # Part 6: Hecke decomposition
    hecke_decomposition,
    hecke_eigenvalue_at_prime,
    ramanujan_bound_check,
    theta_hecke_eigenvalue_contribution,
    # Part 7: Moonshine module
    j_coefficient,
    monster_dim_Vn,
    monster_virasoro_shadow_tower,
    monster_shadow_data_extended,
    monster_mckay_thompson_identity,
    # Part 8: Cross-lattice discrimination
    kissing_number_collisions,
    shell_collision_analysis,
    conductor_collision_analysis,
    # Part 9: Hecke verification
    verify_deligne_bound,
    tau_multiplicativity_check,
    deligne_bound,
    # Part 10: Full cascade
    discrimination_at_level,
    full_arithmetic_discrimination_cascade,
    # Part 11: Cross-verification
    cross_verify_kissing_number,
    cross_verify_shell_recovery,
    cross_verify_all_niemeier,
    # Part 12-13: Lattice VOA shadow invariants
    lattice_voa_S3,
    lattice_voa_S4,
    lattice_voa_critical_discriminant,
    s3_discriminates,
    first_discriminating_arity,
    # Part 14: Monster vs Niemeier
    monster_vs_niemeier_comparison,
    # Part 15: Summary
    full_arithmetic_summary,
    # Internal helpers
    _ramanujan_tau,
    _sigma_k,
    _eisenstein_E12_coefficient,
    _is_prime,
)

from compute.lib.niemeier_shadow_atlas import (
    ALL_NIEMEIER_LABELS,
    KAPPA_NIEMEIER,
    NIEMEIER_REGISTRY,
    c_delta,
    coxeter_number,
    root_count,
    shadow_data,
    theta_coefficient,
)

from compute.lib.moonshine_shadow_tower import (
    monster_kappa,
    leech_kappa,
    monster_critical_discriminant,
    monster_shadow_growth_rate,
    monster_genus_amplitude,
    leech_genus_amplitude,
    _faber_pandharipande,
)

from sympy import Rational


# =========================================================================
# Section 1: Root system data verification
# =========================================================================

class TestRootSystemData:
    """Verify root system data extensions for all ADE types."""

    def test_lie_algebra_dim_A(self):
        """dim sl(n+1) = n(n+2)."""
        assert lie_algebra_dimension('A', 1) == 3    # sl(2)
        assert lie_algebra_dimension('A', 2) == 8    # sl(3)
        assert lie_algebra_dimension('A', 3) == 15   # sl(4)
        assert lie_algebra_dimension('A', 4) == 24   # sl(5)
        assert lie_algebra_dimension('A', 24) == 24 * 26  # sl(25)

    def test_lie_algebra_dim_D(self):
        """dim so(2n) = n(2n-1)."""
        assert lie_algebra_dimension('D', 4) == 28   # so(8)
        assert lie_algebra_dimension('D', 5) == 45   # so(10)
        assert lie_algebra_dimension('D', 8) == 120  # so(16)
        assert lie_algebra_dimension('D', 12) == 276  # so(24)
        assert lie_algebra_dimension('D', 24) == 24 * 47  # so(48)

    def test_lie_algebra_dim_E(self):
        assert lie_algebra_dimension('E', 6) == 78
        assert lie_algebra_dimension('E', 7) == 133
        assert lie_algebra_dimension('E', 8) == 248

    def test_weyl_group_order_A(self):
        """W(A_n) = S_{n+1}, order (n+1)!"""
        assert weyl_group_order('A', 1) == 2
        assert weyl_group_order('A', 2) == 6
        assert weyl_group_order('A', 3) == 24
        assert weyl_group_order('A', 4) == 120

    def test_weyl_group_order_D(self):
        """W(D_n) has order 2^{n-1} * n!"""
        assert weyl_group_order('D', 4) == 8 * 24  # 192
        assert weyl_group_order('D', 5) == 16 * 120  # 1920

    def test_weyl_group_order_E(self):
        assert weyl_group_order('E', 6) == 51840
        assert weyl_group_order('E', 7) == 2903040
        assert weyl_group_order('E', 8) == 696729600

    def test_exponents_A(self):
        assert exponents('A', 1) == (1,)
        assert exponents('A', 2) == (1, 2)
        assert exponents('A', 3) == (1, 2, 3)

    def test_exponents_D(self):
        assert exponents('D', 4) == (1, 3, 5, 3)  # D_4 has special exponents
        assert exponents('D', 5) == (1, 3, 5, 7, 4)

    def test_exponents_E(self):
        assert exponents('E', 6) == (1, 4, 5, 7, 8, 11)
        assert exponents('E', 7) == (1, 5, 7, 9, 11, 13, 17)
        assert exponents('E', 8) == (1, 7, 11, 13, 17, 19, 23, 29)

    def test_exponent_sum_equals_positive_roots(self):
        """Sum of exponents = |R+| = |R|/2."""
        for family, n in [('A', 3), ('A', 5), ('D', 4), ('D', 6),
                          ('E', 6), ('E', 7), ('E', 8)]:
            exp_sum = sum(exponents(family, n))
            half_roots = root_count(family, n) // 2
            assert exp_sum == half_roots, f"{family}_{n}: sum(exp)={exp_sum} != |R+|={half_roots}"

    def test_dual_coxeter_equals_coxeter_for_ADE(self):
        """For simply-laced types, h^vee = h."""
        for family, n in [('A', 1), ('A', 5), ('D', 4), ('D', 8),
                          ('E', 6), ('E', 7), ('E', 8)]:
            assert dual_coxeter_number(family, n) == coxeter_number(family, n)


# =========================================================================
# Section 2: Kissing numbers — all 24 lattices
# =========================================================================

class TestKissingNumbers:
    """Verify kissing numbers for all 24 Niemeier lattices."""

    # Ground truth from Conway-Sloane Table 16.1
    KNOWN_KISSING = {
        'D24': 1104,
        'D16_E8': 720,
        '3E8': 720,
        'A24': 600,
        '2D12': 528,
        'A17_E7': 432,
        'D10_2E7': 432,
        'A15_D9': 384,
        '3D8': 336,
        '2A12': 312,
        'A11_D7_E6': 288,
        '4E6': 288,
        '2A9_D6': 240,
        '4D6': 240,
        '3A8': 216,
        '2A7_2D5': 192,
        '4A6': 168,
        '4A5_D4': 144,
        '6D4': 144,
        '6A4': 120,
        '8A3': 96,
        '12A2': 72,
        '24A1': 48,
        'Leech': 0,
    }

    def test_all_kissing_numbers(self):
        """Verify kissing numbers match Conway-Sloane ground truth."""
        for label, expected in self.KNOWN_KISSING.items():
            actual = kissing_number(label)
            assert actual == expected, f"{label}: got {actual}, expected {expected}"

    def test_leech_has_no_roots(self):
        assert kissing_number('Leech') == 0

    def test_leech_true_kissing(self):
        """Leech lattice true kissing number is 196560."""
        assert kissing_number_true('Leech') == 196560

    def test_non_leech_kissing_equals_true_kissing(self):
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            assert kissing_number(label) == kissing_number_true(label)

    def test_d24_has_maximum_roots(self):
        assert kissing_number('D24') == 1104
        for label in ALL_NIEMEIER_LABELS:
            assert kissing_number(label) <= 1104

    def test_kissing_from_theta_matches(self):
        """Path 2: kissing number from theta coefficient r(1)."""
        for label in ALL_NIEMEIER_LABELS:
            assert kissing_from_theta(label) == kissing_number(label), \
                f"{label}: theta path mismatch"

    def test_kissing_from_root_count(self):
        """Path 1: kissing number from root system computation."""
        for label in ALL_NIEMEIER_LABELS:
            data = NIEMEIER_REGISTRY[label]
            root_total = sum(root_count(f, n) for f, n in data['components'])
            assert root_total == kissing_number(label), \
                f"{label}: root count mismatch"


# =========================================================================
# Section 3: Kissing number collisions (the 5 pairs)
# =========================================================================

class TestKissingCollisions:
    """Verify the 5 collision pairs with identical kissing numbers."""

    KNOWN_COLLISION_PAIRS = {
        720: ['D16_E8', '3E8'],
        432: ['A17_E7', 'D10_2E7'],
        288: ['A11_D7_E6', '4E6'],
        240: ['2A9_D6', '4D6'],
        144: ['4A5_D4', '6D4'],
    }

    def test_collision_pairs_exist(self):
        collisions = kissing_number_collisions()
        assert len(collisions) == 5, f"Expected 5 collision groups, got {len(collisions)}"

    def test_collision_values(self):
        collisions = kissing_number_collisions()
        for kiss_val, expected_labels in self.KNOWN_COLLISION_PAIRS.items():
            assert kiss_val in collisions, f"Missing collision at |R|={kiss_val}"
            actual = sorted(collisions[kiss_val])
            expected = sorted(expected_labels)
            assert actual == expected, \
                f"|R|={kiss_val}: got {actual}, expected {expected}"

    def test_19_non_colliding_lattices(self):
        """19 lattices have unique kissing numbers."""
        collisions = kissing_number_collisions()
        colliding_labels = set()
        for labs in collisions.values():
            colliding_labels.update(labs)
        non_colliding = [l for l in ALL_NIEMEIER_LABELS if l not in colliding_labels]
        assert len(non_colliding) == 14, \
            f"Expected 14 non-colliding, got {len(non_colliding)}"
        # 24 total - 10 colliding = 14 non-colliding

    def test_collision_pairs_have_identical_theta(self):
        """Collision pairs have identical theta series (exact, not approximate)."""
        for kiss_val, labels in self.KNOWN_COLLISION_PAIRS.items():
            for m in range(20):
                ref = theta_coefficient(labels[0], m)
                for label in labels[1:]:
                    assert theta_coefficient(label, m) == ref, \
                        f"|R|={kiss_val}: {labels[0]} vs {label} differ at q^{m}"


# =========================================================================
# Section 4: Shell distribution
# =========================================================================

class TestShellDistribution:
    """Verify shell distribution computation and properties."""

    def test_shell_0_is_1(self):
        """N_0 = 1 (the zero vector) for all lattices."""
        for label in ALL_NIEMEIER_LABELS:
            assert shell_number(label, 0) == 1

    def test_shell_1_is_kissing(self):
        """N_1 = kissing number."""
        for label in ALL_NIEMEIER_LABELS:
            assert shell_number(label, 1) == kissing_number(label)

    def test_leech_shell_1_is_0(self):
        """Leech has no norm-2 vectors."""
        assert shell_number('Leech', 1) == 0

    def test_leech_shell_2(self):
        """Leech lattice: N_2 = 196560 (the norm-4 vectors)."""
        assert shell_number('Leech', 2) == 196560

    def test_e8_cubed_shell_1(self):
        """3E_8: N_1 = 3 * 240 = 720."""
        assert shell_number('3E8', 1) == 720

    def test_shell_distribution_returns_dict(self):
        dist = shell_distribution('Leech', max_m=5)
        assert isinstance(dist, dict)
        assert 0 in dist and 5 in dist
        assert dist[0] == 1

    def test_shells_non_negative(self):
        """All shell numbers are non-negative."""
        for label in ALL_NIEMEIER_LABELS:
            for m in range(15):
                assert shell_number(label, m) >= 0, \
                    f"{label}: N_{m} < 0"

    def test_shell_determines_theta_for_all(self):
        """N_1 alone determines the full theta series for all 24 lattices."""
        for label in ALL_NIEMEIER_LABELS:
            assert shell_determines_theta(label), \
                f"{label}: N_1 does not determine theta"


# =========================================================================
# Section 5: Shadow ODE shell recovery (Path 2 verification)
# =========================================================================

class TestShadowODERecovery:
    """Verify that shadow ODE recovery matches direct theta computation."""

    def test_recovery_matches_direct_all_lattices(self):
        """Path 1 vs Path 2: direct theta == shadow ODE recovery."""
        for label in ALL_NIEMEIER_LABELS:
            assert verify_shadow_shell_consistency(label, max_m=8), \
                f"{label}: shadow ODE recovery mismatch"

    def test_recovery_leech(self):
        """Leech lattice recovery check."""
        recovered = shadow_ode_shell_recovery('Leech', max_m=5)
        assert recovered[0] == 1
        assert recovered[1] == 0
        assert recovered[2] == 196560

    def test_recovery_d24(self):
        """D_24 recovery: N_1 = 1104."""
        recovered = shadow_ode_shell_recovery('D24', max_m=3)
        assert recovered[1] == 1104

    def test_recovery_3e8(self):
        """3E_8 recovery."""
        recovered = shadow_ode_shell_recovery('3E8', max_m=3)
        assert recovered[1] == 720


# =========================================================================
# Section 6: Arithmetic depth
# =========================================================================

class TestArithmeticDepth:
    """Verify arithmetic depth classification."""

    def test_all_depth_1_basic(self):
        """ALL 24 Niemeier lattices have d_arith = 1.

        No Niemeier lattice is purely Eisenstein because 65520/691
        is not an integer, so c_Delta != 0 for all.
        """
        for label in ALL_NIEMEIER_LABELS:
            assert arithmetic_depth(label) == 1, f"{label}: d_arith != 1"

    def test_total_depth_all_2(self):
        """All: d = 1 + 1 = 2 (1 for kappa + 1 for cusp form)."""
        for label in ALL_NIEMEIER_LABELS:
            assert total_depth(label) == 2, f"{label}: total depth != 2"

    def test_depth_classification_groups(self):
        """Depth classification: all 24 at depth 1."""
        groups = depth_classification()
        assert 1 in groups
        assert len(groups[1]) == 24

    def test_leech_c_delta_nonzero(self):
        """Even Leech has c_Delta != 0 (it equals -65520/691)."""
        cd = c_delta('Leech')
        assert cd != 0
        assert cd == Fraction(-65520, 691)

    def test_leech_purely_eisenstein_is_false(self):
        """Leech theta is NOT purely Eisenstein (c_Delta != 0).

        Wait: this contradicts the arithmetic_depth definition.
        Let me re-examine: Theta_Leech = E_{12} + c_Delta * Delta.
        c_Delta(Leech) = (691*0 - 65520)/691 = -65520/691 != 0.
        So Leech IS NOT purely Eisenstein.
        The arithmetic_depth should be 1 for Leech too!

        Actually, for Leech: N_roots = 0, and
        c_Delta = (691*0 - 65520)/691 = -65520/691.
        This is nonzero, so the cuspidal part is nonzero.

        The Leech theta series is:
        Theta_Leech = 1 + 0*q + 196560*q^2 + ...
        = E_{12} - (65520/691)*Delta

        So d_arith = 1 for Leech too.  The d_arith = 0 case would require
        c_Delta = 0, i.e., 691*N_roots = 65520, i.e., N_roots = 65520/691.
        Since 65520/691 is not an integer, d_arith = 0 for NO Niemeier lattice.

        CORRECTION: the original claim in the engine that "Leech has d_arith = 0"
        was wrong.  All 24 Niemeier lattices have d_arith = 1.
        """
        # This test documents that d_arith = 0 is IMPOSSIBLE for Niemeier lattices.
        # Every Niemeier lattice has c_Delta != 0.
        for label in ALL_NIEMEIER_LABELS:
            cd = c_delta(label)
            assert cd != 0, f"{label}: c_Delta = 0 (impossible for integer N_roots)"

    def test_all_depth_1(self):
        """CORRECTED: ALL 24 Niemeier lattices have d_arith = 1.

        No Niemeier lattice is purely Eisenstein because 65520/691
        is not an integer, so c_Delta = (691*N - 65520)/691 != 0 for
        all integer N.
        """
        # The arithmetic_depth function should return 1 for ALL, including Leech
        # But wait: let's check the implementation.
        # arithmetic_depth returns 0 if c_delta == 0, else 1.
        # For Leech: c_delta = -65520/691 != 0, so it returns 1.
        # Wait, earlier I wrote the docstring saying Leech has d_arith=0. Let me
        # check the actual implementation...
        # The implementation checks c_delta(label) == 0.
        # c_delta('Leech') = Fraction(691*0 - 65520, 691) = Fraction(-65520, 691) != 0.
        # So arithmetic_depth('Leech') = 1.  GOOD.
        for label in ALL_NIEMEIER_LABELS:
            assert arithmetic_depth(label) == 1, f"{label}: expected d_arith=1"


# =========================================================================
# Section 7: Arithmetic conductor
# =========================================================================

class TestArithmeticConductor:
    """Verify arithmetic conductor computation."""

    def test_leech_conductor(self):
        """Leech: |691*0 - 65520| = 65520 = 2^4 * 3^2 * 5 * 7 * 13."""
        N = arithmetic_conductor('Leech')
        assert N == 65520
        factors = arithmetic_conductor_factored('Leech')
        assert factors == {2: 4, 3: 2, 5: 1, 7: 1, 13: 1}
        assert 2**4 * 3**2 * 5 * 7 * 13 == 65520

    def test_d24_conductor(self):
        """D_24: |691*1104 - 65520| = |762864 - 65520| = 697344."""
        N = arithmetic_conductor('D24')
        assert N == abs(691 * 1104 - 65520)
        assert N == 697344

    def test_3e8_conductor(self):
        """3E_8: |691*720 - 65520| = |497520 - 65520| = 432000."""
        N = arithmetic_conductor('3E8')
        assert N == abs(691 * 720 - 65520)
        assert N == 432000

    def test_24a1_conductor(self):
        """24A_1: |691*48 - 65520| = |33168 - 65520| = 32352."""
        N = arithmetic_conductor('24A1')
        assert N == abs(691 * 48 - 65520)
        assert N == 32352

    def test_conductor_all_positive(self):
        """All conductors are positive integers."""
        for label in ALL_NIEMEIER_LABELS:
            N = arithmetic_conductor(label)
            assert N > 0, f"{label}: conductor = {N}"
            assert isinstance(N, int)

    def test_conductor_factors_multiply_correctly(self):
        """Factored conductor product equals conductor."""
        for label in ALL_NIEMEIER_LABELS:
            N = arithmetic_conductor(label)
            factors = arithmetic_conductor_factored(label)
            product = 1
            for p, e in factors.items():
                product *= p ** e
            assert product == N, f"{label}: factored product {product} != {N}"

    def test_conductor_collision_pairs_differ(self):
        """Check if conductor differs for theta-collision pairs.

        The collision pairs (same |R|) have identical theta series but
        may have different conductors.  Since conductor depends only on
        N_roots, collision pairs have IDENTICAL conductors too.
        """
        collision_pairs = [
            ('D16_E8', '3E8'),       # |R| = 720
            ('A17_E7', 'D10_2E7'),   # |R| = 432
            ('A11_D7_E6', '4E6'),    # |R| = 288
            ('2A9_D6', '4D6'),       # |R| = 240
            ('4A5_D4', '6D4'),       # |R| = 144
        ]
        for l1, l2 in collision_pairs:
            # Same N_roots => same conductor
            assert arithmetic_conductor(l1) == arithmetic_conductor(l2), \
                f"{l1} vs {l2}: same |R| but different conductors"

    def test_conductor_discrimination_limited(self):
        """Conductor has same discrimination as kissing number (both depend on N_roots only)."""
        disc = conductor_discriminating_power()
        # Since conductor = |691*N - 65520| is injective in N for N >= 0
        # (691 > 0 so the map N -> 691*N - 65520 is strictly increasing),
        # the conductor discriminates exactly as well as N_roots.
        kiss_coll = kissing_number_collisions()
        cond_coll = disc['collisions']
        # Same number of collision groups
        assert len(cond_coll) == len(kiss_coll)


# =========================================================================
# Section 8: Ramanujan tau function verification
# =========================================================================

class TestRamanujanTau:
    """Verify Ramanujan tau function implementation."""

    # Known values from OEIS A000594
    KNOWN_TAU = {
        1: 1,
        2: -24,
        3: 252,
        4: -1472,
        5: 4830,
        6: -6048,
        7: -16744,
        8: 84480,
        9: -113643,
        10: -115920,
        11: 534612,
        12: -370944,
    }

    def test_known_values(self):
        for n, expected in self.KNOWN_TAU.items():
            actual = _ramanujan_tau(n)
            assert actual == expected, f"tau({n}) = {actual}, expected {expected}"

    def test_tau_1(self):
        assert _ramanujan_tau(1) == 1

    def test_tau_2(self):
        assert _ramanujan_tau(2) == -24

    def test_tau_3(self):
        assert _ramanujan_tau(3) == 252

    def test_multiplicativity(self):
        """tau(mn) = tau(m)*tau(n) for gcd(m,n) = 1."""
        result = tau_multiplicativity_check(30)
        assert result['multiplicativity_ok'], \
            f"Multiplicativity violations: {result['multiplicativity_violations']}"

    def test_hecke_relation(self):
        """tau(p^2) = tau(p)^2 - p^11."""
        result = tau_multiplicativity_check(20)
        assert result['hecke_ok'], \
            f"Hecke violations: {result['hecke_relation_violations']}"

    def test_tau_2_squared_minus_2_11(self):
        """tau(4) = tau(2)^2 - 2^11 = 576 - 2048 = -1472."""
        assert _ramanujan_tau(4) == (-24)**2 - 2**11
        assert _ramanujan_tau(4) == 576 - 2048
        assert _ramanujan_tau(4) == -1472

    def test_tau_6_equals_tau_2_times_tau_3(self):
        """tau(6) = tau(2)*tau(3) since gcd(2,3)=1."""
        assert _ramanujan_tau(6) == _ramanujan_tau(2) * _ramanujan_tau(3)
        assert _ramanujan_tau(6) == -24 * 252
        assert _ramanujan_tau(6) == -6048

    def test_tau_10_equals_tau_2_times_tau_5(self):
        assert _ramanujan_tau(10) == _ramanujan_tau(2) * _ramanujan_tau(5)
        assert _ramanujan_tau(10) == -24 * 4830
        assert _ramanujan_tau(10) == -115920


# =========================================================================
# Section 9: Deligne bound (Ramanujan conjecture)
# =========================================================================

class TestDeligneBound:
    """Verify |tau(p)| <= 2*p^{11/2} for primes p (Deligne's theorem)."""

    def test_deligne_bound_small_primes(self):
        """Check for first 25 primes."""
        result = verify_deligne_bound(100)
        assert result['all_satisfied'], \
            f"Deligne bound violated: {result['violations']}"
        assert result['num_primes_checked'] == 25  # primes up to 100

    def test_deligne_bound_at_2(self):
        """|tau(2)| = 24 <= 2*2^{11/2} = 2*sqrt(2048) ~ 90.5."""
        assert abs(_ramanujan_tau(2)) <= 2 * 2 ** 5.5

    def test_deligne_bound_at_3(self):
        """|tau(3)| = 252 <= 2*3^{11/2} ~ 780.9."""
        assert abs(_ramanujan_tau(3)) <= 2 * 3 ** 5.5

    def test_deligne_bound_at_5(self):
        """|tau(5)| = 4830 <= 2*5^{11/2} ~ 27950.8."""
        assert abs(_ramanujan_tau(5)) <= 2 * 5 ** 5.5

    def test_deligne_bound_at_7(self):
        """|tau(7)| = 16744 <= 2*7^{11/2} ~ 259274.9."""
        assert abs(_ramanujan_tau(7)) <= 2 * 7 ** 5.5

    def test_hecke_eigenvalue_at_primes(self):
        """hecke_eigenvalue_at_prime returns tau(p)."""
        for p in [2, 3, 5, 7, 11]:
            assert hecke_eigenvalue_at_prime(p) == _ramanujan_tau(p)


# =========================================================================
# Section 10: Hecke decomposition
# =========================================================================

class TestHeckeDecomposition:
    """Verify Hecke eigenform decomposition of Niemeier theta series."""

    def test_leech_not_eigenform(self):
        """Leech theta is NOT a Hecke eigenform (c_Delta != 0)."""
        dec = hecke_decomposition('Leech')
        assert dec['has_cuspidal_part']
        assert dec['num_eigencomponents'] == 2
        assert not dec['is_eigenform']

    def test_all_have_cuspidal_part(self):
        """All 24 lattices have c_Delta != 0 (cuspidal part present)."""
        for label in ALL_NIEMEIER_LABELS:
            dec = hecke_decomposition(label)
            assert dec['has_cuspidal_part'], f"{label}: no cuspidal part"
            assert dec['num_eigencomponents'] == 2

    def test_cuspidal_coefficient_matches_c_delta(self):
        """Cuspidal coefficient = c_Delta."""
        for label in ALL_NIEMEIER_LABELS:
            dec = hecke_decomposition(label)
            assert dec['cuspidal_coefficient'] == c_delta(label)

    def test_eisenstein_coefficient_is_1(self):
        """Eisenstein coefficient is always 1 (normalized)."""
        for label in ALL_NIEMEIER_LABELS:
            dec = hecke_decomposition(label)
            assert dec['eisenstein_coefficient'] == 1


# =========================================================================
# Section 11: Eisenstein series verification
# =========================================================================

class TestEisensteinSeries:
    """Verify E_{12} coefficient computation."""

    def test_e12_constant_term(self):
        assert _eisenstein_E12_coefficient(0) == 1

    def test_e12_coefficient_1(self):
        """E_{12} coefficient at q^1: (65520/691) * sigma_{11}(1) = 65520/691."""
        c1 = _eisenstein_E12_coefficient(1)
        assert c1 == Rational(65520, 691)

    def test_sigma_11_values(self):
        """Verify some sigma_11 values."""
        assert _sigma_k(1, 11) == 1
        assert _sigma_k(2, 11) == 1 + 2**11  # = 2049
        assert _sigma_k(3, 11) == 1 + 3**11  # = 177148


# =========================================================================
# Section 12: j-function and Moonshine module
# =========================================================================

class TestMoonshineModule:
    """Verify Moonshine module V^natural computations."""

    def test_monster_kappa(self):
        """kappa(V^natural) = 12 (AP48: NOT 24, since dim V_1 = 0)."""
        assert int(monster_kappa()) == 12

    def test_leech_kappa(self):
        """kappa(V_Leech) = 24."""
        assert int(leech_kappa()) == 24

    def test_monster_vs_leech_kappa(self):
        """V^natural and V_Leech have DIFFERENT kappa despite same c=24."""
        assert monster_kappa() != leech_kappa()

    def test_j_coefficient_minus1(self):
        """J_{-1} = 1 (simple pole)."""
        assert j_coefficient(-1) == 1

    def test_j_coefficient_0(self):
        """J_0 = 0 (J = j - 744)."""
        assert j_coefficient(0) == 0

    def test_j_coefficient_1(self):
        """J_1 = 196884 (McKay's observation: 196884 = 196883 + 1)."""
        assert j_coefficient(1) == 196884

    def test_j_coefficient_2(self):
        assert j_coefficient(2) == 21493760

    def test_j_coefficient_3(self):
        assert j_coefficient(3) == 864299970

    def test_monster_dim_V0(self):
        assert monster_dim_Vn(0) == 1

    def test_monster_dim_V1(self):
        """dim V_1 = 0 (no weight-1 currents in V^natural)."""
        assert monster_dim_Vn(1) == 0

    def test_monster_dim_V2(self):
        """dim V_2 = J_1 = 196884."""
        assert monster_dim_Vn(2) == 196884

    def test_mckay_observation(self):
        """196884 = 196883 + 1 (smallest nontrivial + trivial rep of Monster)."""
        dim_V2 = monster_dim_Vn(2)
        assert dim_V2 == 196883 + 1

    def test_monster_shadow_class_M(self):
        """V^natural is class M (infinite shadow depth)."""
        data = monster_shadow_data_extended()
        assert data['shadow_class'] == 'M'

    def test_monster_virasoro_tower(self):
        """Virasoro shadow tower at c=24: S_2=12, S_3=2, S_4=5/1704."""
        tower = monster_virasoro_shadow_tower(6)
        assert tower[2] == Rational(12)
        assert tower[3] == Rational(2)
        assert tower[4] == Rational(5, 1704)

    def test_monster_critical_discriminant(self):
        """Delta(V^natural) = 8*12*5/1704 = 20/71 != 0."""
        delta = monster_critical_discriminant()
        assert delta == Rational(20, 71)
        assert delta != 0

    def test_mckay_thompson_identity(self):
        """Identity class McKay-Thompson = J itself."""
        mt = monster_mckay_thompson_identity()
        assert mt['conjugacy_class'] == '1A'
        assert mt['is_hauptmodul']
        assert mt['genus_of_quotient'] == 0
        assert mt['leading_coefficients'][0] == 1   # J_{-1}
        assert mt['leading_coefficients'][1] == 0   # J_0
        assert mt['leading_coefficients'][2] == 196884  # J_1


# =========================================================================
# Section 13: Cross-verification (multi-path)
# =========================================================================

class TestCrossVerification:
    """Multi-path verification of all invariants."""

    def test_cross_verify_kissing_all(self):
        """3-path cross-verification of kissing number for all 24 lattices."""
        for label in ALL_NIEMEIER_LABELS:
            result = cross_verify_kissing_number(label)
            assert result['all_agree'], \
                f"{label}: paths disagree: {result}"

    def test_cross_verify_shells_all(self):
        """2-path cross-verification of shell numbers for all 24 lattices."""
        for label in ALL_NIEMEIER_LABELS:
            result = cross_verify_shell_recovery(label, max_m=6)
            assert result['all_agree'], \
                f"{label}: shell recovery mismatch"

    def test_cross_verify_all_niemeier(self):
        """Full cross-verification summary."""
        results = cross_verify_all_niemeier()
        for label, checks in results.items():
            assert checks['kissing_cross_verified'], f"{label}: kissing failed"
            assert checks['shell_recovery_cross_verified'], f"{label}: shell failed"
            assert checks['theta_from_N1'], f"{label}: theta from N1 failed"


# =========================================================================
# Section 14: Lattice VOA shadow invariants (all zero for class G)
# =========================================================================

class TestLatticeVOAShadows:
    """All Niemeier lattice VOAs have vanishing higher shadows (class G)."""

    def test_S3_zero_for_all(self):
        for label in ALL_NIEMEIER_LABELS:
            assert lattice_voa_S3(label) == 0

    def test_S4_zero_for_all(self):
        for label in ALL_NIEMEIER_LABELS:
            assert lattice_voa_S4(label) == 0

    def test_critical_discriminant_zero_for_all(self):
        for label in ALL_NIEMEIER_LABELS:
            assert lattice_voa_critical_discriminant(label) == 0

    def test_s3_does_not_discriminate(self):
        """S_3 is 0 for all: cannot discriminate."""
        assert s3_discriminates() is False


# =========================================================================
# Section 15: Discrimination cascade
# =========================================================================

class TestDiscriminationCascade:
    """Verify the full discrimination cascade from level 0 to 5."""

    def test_level_0_no_discrimination(self):
        """Level 0 (kappa): 0 pairs distinguished."""
        result = discrimination_at_level(0)
        assert result['distinguished_pairs'] == 0
        assert result['num_distinct'] == 1
        assert not result['is_complete']

    def test_level_1_no_discrimination(self):
        """Level 1 (full scalar tower): 0 pairs distinguished."""
        result = discrimination_at_level(1)
        assert result['distinguished_pairs'] == 0
        assert not result['is_complete']

    def test_level_2_partial_discrimination(self):
        """Level 2 (kissing number): 19 distinct values, 5 collision groups."""
        result = discrimination_at_level(2)
        assert result['num_distinct'] == 19
        assert result['collision_pairs'] > 0
        assert not result['is_complete']

    def test_level_3_complete(self):
        """Level 3 (per-factor rank+Coxeter): COMPLETE discrimination."""
        result = discrimination_at_level(3)
        assert result['num_distinct'] == 24
        assert result['distinguished_pairs'] == 276  # all C(24,2) pairs
        assert result['collision_pairs'] == 0
        assert result['is_complete']

    def test_level_5_same_as_level_2(self):
        """Level 5 (c_Delta) has same power as level 2 (both determined by N_roots)."""
        r2 = discrimination_at_level(2)
        r5 = discrimination_at_level(5)
        assert r2['num_distinct'] == r5['num_distinct']

    def test_full_cascade(self):
        """Full cascade runs without error and shows monotone improvement."""
        cascade = full_arithmetic_discrimination_cascade()
        assert len(cascade) == 6
        # Levels 0 and 1 are tied at 0
        assert cascade[0]['distinguished_pairs'] == 0
        assert cascade[1]['distinguished_pairs'] == 0
        # Level 2 jumps up
        assert cascade[2]['distinguished_pairs'] > 0
        # Level 3 is complete
        assert cascade[3]['is_complete']

    def test_total_pairs_is_276(self):
        """C(24, 2) = 276 total pairs."""
        for level in range(6):
            result = discrimination_at_level(level)
            assert result['total_pairs'] == 276


# =========================================================================
# Section 16: First discriminating arity analysis
# =========================================================================

class TestFirstDiscriminatingArity:
    """The scalar shadow tower cannot discriminate Niemeier lattices."""

    def test_scalar_tower_fails(self):
        result = first_discriminating_arity()
        assert result['scalar_tower_discriminates'] is False

    def test_bar_complex_level_3_is_minimal(self):
        result = first_discriminating_arity()
        assert result['minimal_complete_mc_level'] == 3

    def test_bar_complex_arity_1(self):
        """The per-factor data is arity-1 (generator-level) MC data."""
        result = first_discriminating_arity()
        assert result['bar_complex_arity'] == 1


# =========================================================================
# Section 17: Monster vs Niemeier comparison
# =========================================================================

class TestMonsterVsNiemeier:
    """V^natural vs all 24 lattice VOAs."""

    def test_monster_kappa_different(self):
        """kappa(V^natural) = 12 != 24 = kappa(V_Lambda) for all Lambda."""
        comp = monster_vs_niemeier_comparison()
        assert comp['monster']['kappa'] == 12
        for label in ALL_NIEMEIER_LABELS:
            assert comp['niemeier_lattices'][label]['kappa'] == 24

    def test_monster_class_different(self):
        """V^natural is class M, all lattice VOAs are class G."""
        comp = monster_vs_niemeier_comparison()
        assert comp['monster']['shadow_class'] == 'M'
        for label in ALL_NIEMEIER_LABELS:
            assert comp['niemeier_lattices'][label]['shadow_class'] == 'G'

    def test_monster_infinite_depth(self):
        comp = monster_vs_niemeier_comparison()
        assert comp['monster']['shadow_depth'] == float('inf')

    def test_lattice_finite_depth(self):
        comp = monster_vs_niemeier_comparison()
        for label in ALL_NIEMEIER_LABELS:
            assert comp['niemeier_lattices'][label]['shadow_depth'] == 2


# =========================================================================
# Section 18: Theta series known values
# =========================================================================

class TestThetaSeriesValues:
    """Verify known theta series values against Conway-Sloane."""

    def test_e8_theta_is_E4(self):
        """Theta_{E_8} = E_4. Check: theta coeff at n=1 for E_8 lattice.

        E_4 = 1 + 240*q + 2160*q^2 + 6720*q^3 + ...
        So for E_8 lattice: N_1 = 240.

        But E_8 is rank 8, not rank 24, so it's not a Niemeier lattice.
        For the Niemeier lattice 3E_8: N_1 = 3*240 = 720.
        """
        assert shell_number('3E8', 1) == 720
        # Each E_8 component contributes 240 roots
        assert root_count('E', 8) == 240

    def test_leech_shell_values(self):
        """Leech lattice first few shell numbers (Conway-Sloane)."""
        # N_0 = 1 (zero vector)
        assert shell_number('Leech', 0) == 1
        # N_1 = 0 (no roots)
        assert shell_number('Leech', 1) == 0
        # N_2 = 196560 (minimal vectors)
        assert shell_number('Leech', 2) == 196560
        # N_3 = 16773120 (known)
        assert shell_number('Leech', 3) == 16773120

    def test_d24_shell_1(self):
        """D_24: N_1 = 2*24*23 = 1104."""
        assert shell_number('D24', 1) == 1104
        assert root_count('D', 24) == 1104

    def test_a24_shell_1(self):
        """A_24: N_1 = 24*25 = 600."""
        assert shell_number('A24', 1) == 600
        assert root_count('A', 24) == 600


# =========================================================================
# Section 19: c_Delta values
# =========================================================================

class TestCDelta:
    """Verify c_Delta coefficients for all 24 lattices."""

    def test_c_delta_formula(self):
        """c_Delta = (691*N_roots - 65520) / 691."""
        for label in ALL_NIEMEIER_LABELS:
            N = kissing_number(label)
            expected = Fraction(691 * N - 65520, 691)
            actual = c_delta(label)
            assert actual == expected, f"{label}: c_delta mismatch"

    def test_c_delta_leech(self):
        """Leech: c_Delta = -65520/691."""
        assert c_delta('Leech') == Fraction(-65520, 691)

    def test_c_delta_d24(self):
        """D_24: c_Delta = (691*1104 - 65520)/691 = 697344/691."""
        assert c_delta('D24') == Fraction(691 * 1104 - 65520, 691)

    def test_c_delta_uniquely_determines_kissing(self):
        """c_Delta -> N_roots is injective (since 691*N - 65520 is linear in N)."""
        seen = {}
        for label in ALL_NIEMEIER_LABELS:
            cd = c_delta(label)
            if cd in seen:
                # Same c_Delta means same N_roots means same kissing
                assert kissing_number(label) == kissing_number(seen[cd])
            else:
                seen[cd] = label

    def test_691_divides_numerator_of_theta_coefficients(self):
        """Theta coefficient formula: numer must be divisible by 691."""
        for label in ALL_NIEMEIER_LABELS:
            N = kissing_number(label)
            for m in range(1, 8):
                sig11 = _sigma_k(m, 11)
                tau_m = _ramanujan_tau(m)
                numer = 65520 * sig11 + (691 * N - 65520) * tau_m
                assert numer % 691 == 0, \
                    f"{label}, m={m}: 691 does not divide {numer}"


# =========================================================================
# Section 20: Summary and integration
# =========================================================================

class TestSummary:
    """Full summary tests."""

    def test_full_summary_runs(self):
        summary = full_arithmetic_summary()
        assert summary['total_lattices'] == 24
        assert summary['total_pairs'] == 276
        assert summary['moonshine_distinguished']

    def test_level_3_is_complete_in_summary(self):
        summary = full_arithmetic_summary()
        assert summary['discrimination_cascade'][3]['is_complete']

    def test_level_0_and_1_are_zero_in_summary(self):
        summary = full_arithmetic_summary()
        assert summary['discrimination_cascade'][0]['distinguished_pairs'] == 0
        assert summary['discrimination_cascade'][1]['distinguished_pairs'] == 0


# =========================================================================
# Section 21: Edge cases and error handling
# =========================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_unknown_label_raises(self):
        with pytest.raises(ValueError):
            kissing_number('nonexistent')

    def test_unknown_label_conductor(self):
        with pytest.raises(ValueError):
            arithmetic_conductor('nonexistent')

    def test_shell_negative_m(self):
        """Shell number at negative m is 0 (by convention in theta_coefficient)."""
        assert shell_number('Leech', -1) == 0

    def test_all_24_registered(self):
        """All 24 Niemeier lattices are in the registry."""
        assert len(ALL_NIEMEIER_LABELS) == 24


# =========================================================================
# Section 22: Conductor factorization detailed
# =========================================================================

class TestConductorFactorization:
    """Detailed conductor factorization tests."""

    def test_3e8_factorization(self):
        """3E_8: conductor = |691*720 - 65520| = 432000."""
        N = arithmetic_conductor('3E8')
        factors = arithmetic_conductor_factored('3E8')
        # 432000 = 2^5 * 3^3 * 500 = 2^5 * 3^3 * 4 * 125 = 2^7 * 3^3 * 5^3
        # Let me compute: 432000 / 2 = 216000, /2 = 108000, /2=54000, /2=27000,
        # /2=13500, /2=6750, /2=3375.  3375/3=1125, /3=375, /3=125. 125=5^3.
        # So 432000 = 2^7 * 3^3 * 5^3.  Wait: 2^7=128, 3^3=27, 5^3=125.
        # 128*27=3456. 3456*125=432000. YES.
        product = 1
        for p, e in factors.items():
            product *= p ** e
        assert product == N

    def test_leech_factorization_detailed(self):
        """Leech: 65520 = 2^4 * 3^2 * 5 * 7 * 13."""
        factors = arithmetic_conductor_factored('Leech')
        assert factors[2] == 4
        assert factors[3] == 2
        assert factors[5] == 1
        assert factors[7] == 1
        assert factors[13] == 1


# =========================================================================
# Section 23: Sigma function verification
# =========================================================================

class TestSigmaFunction:
    """Verify divisor sum sigma_k implementation."""

    def test_sigma_0(self):
        """sigma_0(n) = number of divisors."""
        assert _sigma_k(1, 0) == 1
        assert _sigma_k(6, 0) == 4   # 1, 2, 3, 6
        assert _sigma_k(12, 0) == 6  # 1, 2, 3, 4, 6, 12

    def test_sigma_1(self):
        """sigma_1(n) = sum of divisors."""
        assert _sigma_k(1, 1) == 1
        assert _sigma_k(6, 1) == 12   # 1+2+3+6
        assert _sigma_k(12, 1) == 28  # 1+2+3+4+6+12

    def test_sigma_11_at_1(self):
        assert _sigma_k(1, 11) == 1

    def test_sigma_11_at_2(self):
        assert _sigma_k(2, 11) == 1 + 2048  # 1 + 2^11


# =========================================================================
# Section 24: Primality test
# =========================================================================

class TestPrimality:
    """Verify primality test helper."""

    def test_small_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for p in primes:
            assert _is_prime(p), f"{p} should be prime"

    def test_small_composites(self):
        composites = [1, 4, 6, 8, 9, 10, 12, 14, 15]
        for n in composites:
            assert not _is_prime(n), f"{n} should be composite"

    def test_691_is_prime(self):
        """691 is prime (important for theta series)."""
        assert _is_prime(691)


# =========================================================================
# Section 25: Cross-family consistency checks
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10 defense)."""

    def test_kissing_decreases_with_index(self):
        """Kissing numbers decrease roughly with increasing index (Conway-Sloane order)."""
        # D_24 has the most roots, Leech has none
        assert kissing_number('D24') > kissing_number('3E8')
        assert kissing_number('3E8') > kissing_number('24A1')
        assert kissing_number('24A1') > kissing_number('Leech')

    def test_conductor_strictly_positive(self):
        """Conductor is always strictly positive for all 24."""
        for label in ALL_NIEMEIER_LABELS:
            assert arithmetic_conductor(label) > 0

    def test_sum_of_roots_formula(self):
        """N_roots = sum of root_count over components."""
        for label in ALL_NIEMEIER_LABELS:
            data = NIEMEIER_REGISTRY[label]
            computed = sum(root_count(f, n) for f, n in data['components'])
            assert computed == data['num_roots']

    def test_coxeter_uniform(self):
        """All components of a Niemeier root system have the same Coxeter number."""
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            data = NIEMEIER_REGISTRY[label]
            h_values = [coxeter_number(f, n) for f, n in data['components']]
            assert len(set(h_values)) == 1, \
                f"{label}: non-uniform Coxeter numbers {h_values}"

    def test_rank_sum_24(self):
        """Sum of ranks = 24 for all non-Leech."""
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            data = NIEMEIER_REGISTRY[label]
            rank_sum = sum(n for _, n in data['components'])
            assert rank_sum == 24, f"{label}: rank sum = {rank_sum}"


# =========================================================================
# Section 26: Monster module detailed tests
# =========================================================================

class TestMonsterDetailed:
    """Detailed tests for the Monster module V^natural."""

    def test_196884_decomposition(self):
        """196884 = 1 + 196883 (trivial + smallest nontrivial Monster irrep)."""
        assert 196884 == 1 + 196883

    def test_21493760_decomposition(self):
        """21493760 = 1 + 196883 + 21296876."""
        assert 21493760 == 1 + 196883 + 21296876

    def test_monster_genus_amplitudes(self):
        """Genus-g scalar amplitudes: F_g = 12 * lambda_g^FP."""
        F1 = monster_genus_amplitude(1)
        assert F1 == Rational(12) * _faber_pandharipande(1)
        assert F1 == Rational(1, 2)  # 12 * (1/24) = 1/2

    def test_leech_genus_amplitudes(self):
        """Leech: F_g = 24 * lambda_g^FP."""
        F1 = leech_genus_amplitude(1)
        assert F1 == Rational(24) * _faber_pandharipande(1)
        assert F1 == Rational(1)  # 24 * (1/24) = 1

    def test_genus_amplitude_ratio(self):
        """F_g(V_Leech) / F_g(V^natural) = 2 at all genera."""
        for g in range(1, 6):
            ratio = leech_genus_amplitude(g) / monster_genus_amplitude(g)
            assert ratio == 2, f"genus {g}: ratio = {ratio}"

    def test_monster_shadow_growth_rate(self):
        """Shadow growth rate at Virasoro level."""
        rho = monster_shadow_growth_rate()
        assert 0 < rho < 1  # should be subunitary
        # rho = sqrt(9*4 + 40/71) / 24 = sqrt(2596/71) / 24
        expected_sq = (9 * 4 + Rational(40, 71)) / (4 * 144)
        assert abs(rho ** 2 - float(expected_sq)) < 1e-10

    def test_monster_extended_data(self):
        """Extended data runs without error."""
        data = monster_shadow_data_extended()
        assert data['kappa'] == 12
        assert data['dim_V1'] == 0
        assert data['dim_V2'] == 196884


# =========================================================================
# Section 27: Theta Hecke contribution
# =========================================================================

class TestThetaHeckeContribution:
    """Test per-lattice Hecke eigenvalue contributions."""

    def test_leech_hecke_at_2(self):
        """Leech: cuspidal contribution at p=2 is c_Delta * tau(2)."""
        contrib = theta_hecke_eigenvalue_contribution('Leech', 2)
        cd = c_delta('Leech')
        expected = cd * _ramanujan_tau(2)
        assert contrib == expected

    def test_d24_hecke_at_2(self):
        contrib = theta_hecke_eigenvalue_contribution('D24', 2)
        cd = c_delta('D24')
        expected = cd * (-24)  # tau(2) = -24
        assert contrib == expected

    def test_collision_pairs_same_hecke_contribution(self):
        """Collision pairs have same cuspidal contribution (same c_Delta)."""
        pairs = [('D16_E8', '3E8'), ('A17_E7', 'D10_2E7')]
        for l1, l2 in pairs:
            for p in [2, 3, 5]:
                c1 = theta_hecke_eigenvalue_contribution(l1, p)
                c2 = theta_hecke_eigenvalue_contribution(l2, p)
                assert c1 == c2, f"{l1} vs {l2} at p={p}"


# =========================================================================
# Section 28: Comprehensive all-lattice tests
# =========================================================================

class TestAllLatticesComprehensive:
    """Run key checks on every single lattice."""

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_kissing_3path(self, label):
        """3-path cross-verification for each lattice."""
        result = cross_verify_kissing_number(label)
        assert result['all_agree']

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_shell_consistency(self, label):
        """Shadow ODE recovery matches direct theta."""
        assert verify_shadow_shell_consistency(label, max_m=5)

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_conductor_positive(self, label):
        assert arithmetic_conductor(label) > 0

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_shadow_class_G(self, label):
        """All Niemeier lattice VOAs are class G."""
        data = shadow_data(label)
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2
        assert data['kappa'] == 24

    @pytest.mark.parametrize("label", ALL_NIEMEIER_LABELS)
    def test_arithmetic_depth_1(self, label):
        """All have d_arith = 1."""
        assert arithmetic_depth(label) == 1


# =========================================================================
# Section 29: Collision pair resolution test
# =========================================================================

class TestCollisionResolution:
    """Verify that per-factor (rank, Coxeter) resolves all collisions."""

    COLLISION_PAIRS = [
        ('D16_E8', '3E8', 720),
        ('A17_E7', 'D10_2E7', 432),
        ('A11_D7_E6', '4E6', 288),
        ('2A9_D6', '4D6', 240),
        ('4A5_D4', '6D4', 144),
    ]

    @pytest.mark.parametrize("l1,l2,nroots", COLLISION_PAIRS)
    def test_same_kissing(self, l1, l2, nroots):
        """Collision pair has same kissing number."""
        assert kissing_number(l1) == nroots
        assert kissing_number(l2) == nroots

    @pytest.mark.parametrize("l1,l2,nroots", COLLISION_PAIRS)
    def test_same_theta(self, l1, l2, nroots):
        """Collision pair has identical theta series."""
        for m in range(10):
            assert theta_coefficient(l1, m) == theta_coefficient(l2, m)

    @pytest.mark.parametrize("l1,l2,nroots", COLLISION_PAIRS)
    def test_different_coxeter(self, l1, l2, nroots):
        """Collision pair has different per-factor structure."""
        d1 = NIEMEIER_REGISTRY[l1]['components']
        d2 = NIEMEIER_REGISTRY[l2]['components']
        assert d1 != d2, f"{l1} vs {l2}: same components"

    @pytest.mark.parametrize("l1,l2,nroots", COLLISION_PAIRS)
    def test_level3_resolves(self, l1, l2, nroots):
        """Level 3 invariant distinguishes the collision pair."""
        from compute.lib.niemeier_complete_invariant import level3_rank_coxeter
        v1 = level3_rank_coxeter(l1)
        v2 = level3_rank_coxeter(l2)
        assert v1 != v2, f"{l1} vs {l2}: same Level 3 invariant"


# =========================================================================
# Section 30: Arithmetic depth docstring correction test
# =========================================================================

class TestArithmeticDepthCorrection:
    """Document and test the correction to the arithmetic depth docstring.

    Original engine docstring claimed d_arith(Leech) = 0 (purely Eisenstein).
    This is FALSE: c_Delta(Leech) = -65520/691 != 0, so Leech theta is NOT
    purely Eisenstein.  All 24 Niemeier lattices have d_arith = 1.

    The condition c_Delta = 0 requires N_roots = 65520/691 ~ 94.82, which
    is not an integer.  No even unimodular rank-24 lattice is purely Eisenstein.
    """

    def test_no_purely_eisenstein_niemeier(self):
        """No Niemeier lattice has c_Delta = 0."""
        for label in ALL_NIEMEIER_LABELS:
            assert c_delta(label) != 0

    def test_65520_over_691_not_integer(self):
        """65520/691 is not an integer."""
        assert 65520 % 691 != 0

    def test_leech_d_arith_is_1(self):
        """Leech has d_arith = 1, not 0."""
        assert arithmetic_depth('Leech') == 1
