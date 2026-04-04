r"""Tests for the moonshine shadow atlas module.

65+ tests covering:
  1. Root system combinatorics (_root_count, _coxeter_number)
  2. Faber-Pandharipande intersection numbers
  3. Arithmetic functions (sigma_k, ramanujan_tau, eta_coefficients)
  4. Niemeier lattice registry (24 lattices, rank, root counts, Coxeter)
  5. Niemeier shadow tower data (kappa=24, class G, depth 2)
  6. Niemeier genus amplitudes (F_1=1, F_2=7/240)
  7. Niemeier theta series (integrality, r(1)=|R|, c_delta formula)
  8. Niemeier complementarity (kappa+kappa'=0)
  9. Niemeier planted-forest corrections (all zero)
  10. Monster module (kappa=12, shadow class M, J-function coefficients)
  11. Monster representation decomposition (McKay observation)
  12. McKay-Thompson series (identity = J)
  13. Umbral moonshine data (M_24, Leech special case)
  14. Mathieu moonshine coefficients
  15. Thompson group VOA (c=47/2, kappa=47/4)
  16. Comparison functions (kappa, F_1, shadow class)
  17. Theta series collision analysis
  18. Shadow tower resolving power
  19. Full atlas construction
  20. Verification functions

Mathematical ground truth:
  - Frenkel-Lepowsky-Meurman (1988): Vertex Operator Algebras and the Monster
  - Conway-Norton (1979): Monstrous Moonshine
  - Eguchi-Ooguri-Tachikawa (2010): Mathieu moonshine
  - Cheng-Duncan-Harvey (2014): Umbral Moonshine
  - OEIS A000521 (j-function), A014708 (J = j - 744)
"""

import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.moonshine_shadow_atlas import (
    ALL_NIEMEIER_LABELS,
    KAPPA_NIEMEIER,
    KNOWN_J_COEFFICIENTS,
    KNOWN_T_2A_COEFFICIENTS,
    MONSTER_CENTRAL_CHARGE,
    NIEMEIER_REGISTRY,
    THOMPSON_CENTRAL_CHARGE,
    UMBRAL_GROUPS,
    _coxeter_number,
    _eta_coefficients,
    _ramanujan_tau,
    _root_count,
    _sigma_k,
    faber_pandharipande,
    full_atlas,
    genus1_comparison,
    griess_shadow_S3_bound,
    j_function_coefficients,
    j_invariant_polar_coefficient,
    kappa_comparison,
    lattices_sharing_root_count,
    mathieu_moonshine_coefficients,
    mathieu_rep_check,
    mckay_thompson_2A,
    mckay_thompson_identity,
    monster_genus_amplitude,
    monster_kappa,
    monster_partition_coefficients,
    monster_rep_decomposition,
    monster_shadow_data,
    niemeier_c_delta,
    niemeier_complementarity,
    niemeier_genus2_scalar_amplitude,
    niemeier_genus_amplitude,
    niemeier_genus_expansion,
    niemeier_planted_forest_g2,
    niemeier_shadow_data,
    niemeier_theta_coefficient,
    niemeier_theta_series,
    niemeier_total_genus2,
    root_count_collision_resolution,
    shadow_class_comparison,
    shadow_tower_resolving_power,
    thompson_genus1_amplitude,
    thompson_kappa,
    thompson_shadow_data,
    theta_distinguishes_all_24,
    umbral_moonshine_data,
    verify_all_niemeier_shadow_identical,
    verify_complementarity_sum_zero,
    verify_j_function_coefficients,
    verify_monster_kappa_distinct,
    verify_theta_integrality,
    verify_theta_r1_equals_roots,
)


# =========================================================================
# 1. Root system combinatorics
# =========================================================================


class TestRootCount:
    """Verify root counts for simple root systems."""

    def test_A_n_root_count(self):
        """A_n has n(n+1) roots."""
        assert _root_count('A', 1) == 2
        assert _root_count('A', 2) == 6
        assert _root_count('A', 3) == 12
        assert _root_count('A', 4) == 20
        assert _root_count('A', 24) == 24 * 25

    def test_D_n_root_count(self):
        """D_n has 2n(n-1) roots."""
        assert _root_count('D', 4) == 24
        assert _root_count('D', 5) == 40
        assert _root_count('D', 8) == 112
        assert _root_count('D', 24) == 2 * 24 * 23

    def test_E_root_count(self):
        """E_6, E_7, E_8 have 72, 126, 240 roots respectively."""
        assert _root_count('E', 6) == 72
        assert _root_count('E', 7) == 126
        assert _root_count('E', 8) == 240

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            _root_count('B', 3)


class TestCoxeterNumber:
    """Verify Coxeter numbers for simple root systems."""

    def test_A_n_coxeter(self):
        """h(A_n) = n+1."""
        assert _coxeter_number('A', 1) == 2
        assert _coxeter_number('A', 5) == 6
        assert _coxeter_number('A', 24) == 25

    def test_D_n_coxeter(self):
        """h(D_n) = 2(n-1)."""
        assert _coxeter_number('D', 4) == 6
        assert _coxeter_number('D', 8) == 14

    def test_E_coxeter(self):
        assert _coxeter_number('E', 6) == 12
        assert _coxeter_number('E', 7) == 18
        assert _coxeter_number('E', 8) == 30

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            _coxeter_number('F', 4)


# =========================================================================
# 2. Faber-Pandharipande intersection numbers
# =========================================================================


class TestFaberPandharipande:

    def test_lambda1(self):
        """lambda_1 = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_lambda2(self):
        """lambda_2 = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_lambda3(self):
        """lambda_3 = 31/967680."""
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_positive(self):
        """All lambda_g are positive for g >= 1."""
        for g in range(1, 7):
            assert faber_pandharipande(g) > 0

    def test_genus_zero_raises(self):
        with pytest.raises(ValueError):
            faber_pandharipande(0)


# =========================================================================
# 3. Arithmetic functions
# =========================================================================


class TestArithmeticFunctions:

    def test_sigma_0(self):
        """sigma_0(n) = number of divisors."""
        assert _sigma_k(1, 0) == 1
        assert _sigma_k(6, 0) == 4  # 1,2,3,6
        assert _sigma_k(12, 0) == 6  # 1,2,3,4,6,12

    def test_sigma_1(self):
        """sigma_1(n) = sum of divisors."""
        assert _sigma_k(1, 1) == 1
        assert _sigma_k(6, 1) == 12
        assert _sigma_k(12, 1) == 28

    def test_sigma_3(self):
        """sigma_3(1) = 1, sigma_3(2) = 9."""
        assert _sigma_k(1, 3) == 1
        assert _sigma_k(2, 3) == 1 + 8

    def test_sigma_nonpositive(self):
        assert _sigma_k(0, 1) == 0
        assert _sigma_k(-1, 1) == 0

    def test_ramanujan_tau_1(self):
        """tau(1) = 1."""
        assert _ramanujan_tau(1) == 1

    def test_ramanujan_tau_2(self):
        """tau(2) = -24."""
        assert _ramanujan_tau(2) == -24

    def test_ramanujan_tau_3(self):
        """tau(3) = 252."""
        assert _ramanujan_tau(3) == 252

    def test_ramanujan_tau_nonpositive(self):
        assert _ramanujan_tau(0) == 0
        assert _ramanujan_tau(-1) == 0

    def test_eta_coefficients_power24(self):
        """eta^24 has leading coefficient 1 and second coefficient -24."""
        coeffs = _eta_coefficients(5, 24)
        assert coeffs[0] == 1
        # coefficient of q^1 in prod(1-q^m)^24 is -24
        assert coeffs[1] == -24

    def test_eta_coefficients_inverse(self):
        """eta^{-24} = 1/prod(1-q^m)^24 = partition function p_24."""
        coeffs = _eta_coefficients(3, -24)
        assert coeffs[0] == 1
        # p_24(1) = 24 (24 ways to partition 1 into 24 colors)
        assert coeffs[1] == 24


# =========================================================================
# 4. Niemeier lattice registry
# =========================================================================


class TestNiemeierRegistry:

    def test_exactly_24_lattices(self):
        assert len(NIEMEIER_REGISTRY) == 24
        assert len(ALL_NIEMEIER_LABELS) == 24

    def test_all_rank_24(self):
        for label, data in NIEMEIER_REGISTRY.items():
            assert data['rank'] == 24, f"{label} has rank {data['rank']}"

    def test_root_rank_24_or_zero(self):
        """Root rank is 24 for all non-Leech, 0 for Leech."""
        for label, data in NIEMEIER_REGISTRY.items():
            if label == 'Leech':
                assert data['root_rank'] == 0
            else:
                assert data['root_rank'] == 24

    def test_leech_zero_roots(self):
        assert NIEMEIER_REGISTRY['Leech']['num_roots'] == 0

    def test_3E8_root_count(self):
        """3E_8 has 3*240 = 720 roots."""
        assert NIEMEIER_REGISTRY['3E8']['num_roots'] == 720

    def test_24A1_root_count(self):
        """24A_1 has 24*2 = 48 roots."""
        assert NIEMEIER_REGISTRY['24A1']['num_roots'] == 48

    def test_D24_root_count(self):
        """D_24 has 2*24*23 = 1104 roots."""
        assert NIEMEIER_REGISTRY['D24']['num_roots'] == 2 * 24 * 23

    def test_uniform_coxeter_numbers(self):
        """Niemeier's theorem: all components have the same Coxeter number."""
        for label, data in NIEMEIER_REGISTRY.items():
            h_vals = data['coxeter_numbers']
            if h_vals:
                assert all(h == h_vals[0] for h in h_vals), (
                    f"{label}: non-uniform Coxeter numbers {h_vals}"
                )

    def test_3E8_coxeter_30(self):
        assert NIEMEIER_REGISTRY['3E8']['coxeter_numbers'] == [30, 30, 30]

    def test_24A1_coxeter_2(self):
        assert all(h == 2 for h in NIEMEIER_REGISTRY['24A1']['coxeter_numbers'])


# =========================================================================
# 5. Niemeier shadow tower data
# =========================================================================


class TestNiemeierShadowData:

    def test_kappa_24(self):
        """All Niemeier lattice VOAs have kappa = 24."""
        assert KAPPA_NIEMEIER == Rational(24)

    def test_class_G(self):
        """All 24 are class G (Gaussian)."""
        for label in ALL_NIEMEIER_LABELS:
            sd = niemeier_shadow_data(label)
            assert sd['shadow_class'] == 'G'

    def test_depth_2(self):
        for label in ALL_NIEMEIER_LABELS:
            sd = niemeier_shadow_data(label)
            assert sd['shadow_depth'] == 2

    def test_S3_zero(self):
        for label in ALL_NIEMEIER_LABELS:
            sd = niemeier_shadow_data(label)
            assert sd['S3'] == 0

    def test_S4_zero(self):
        for label in ALL_NIEMEIER_LABELS:
            sd = niemeier_shadow_data(label)
            assert sd['S4'] == 0

    def test_critical_discriminant_zero(self):
        """Delta = 8*kappa*S4 = 0 for all Niemeier lattice VOAs."""
        for label in ALL_NIEMEIER_LABELS:
            sd = niemeier_shadow_data(label)
            assert sd['critical_discriminant'] == 0

    def test_growth_rate_zero(self):
        for label in ALL_NIEMEIER_LABELS:
            sd = niemeier_shadow_data(label)
            assert sd['shadow_growth_rate'] == 0

    def test_unknown_lattice_raises(self):
        with pytest.raises(ValueError):
            niemeier_shadow_data('Golay')


# =========================================================================
# 6. Niemeier genus amplitudes
# =========================================================================


class TestNiemeierGenusAmplitudes:

    def test_F1(self):
        """F_1 = 24 * 1/24 = 1."""
        assert niemeier_genus_amplitude(1) == Rational(1)

    def test_F2(self):
        """F_2 = 24 * 7/5760 = 7/240."""
        assert niemeier_genus_amplitude(2) == Rational(7, 240)

    def test_genus_expansion_keys(self):
        exp = niemeier_genus_expansion(4)
        assert set(exp.keys()) == {1, 2, 3, 4}

    def test_genus_expansion_F1(self):
        assert niemeier_genus_expansion(3)[1] == Rational(1)

    def test_genus2_scalar(self):
        assert niemeier_genus2_scalar_amplitude() == Rational(7, 240)

    def test_planted_forest_g2_zero(self):
        """S_3 = 0 implies planted-forest correction vanishes."""
        assert niemeier_planted_forest_g2() == Rational(0)

    def test_total_genus2(self):
        """Total = scalar + planted_forest = 7/240 + 0 = 7/240."""
        assert niemeier_total_genus2() == Rational(7, 240)


# =========================================================================
# 7. Niemeier theta series
# =========================================================================


class TestNiemeierThetaSeries:

    def test_r0_is_one(self):
        """r(0) = 1 for all lattices (counting zero vector)."""
        for label in ALL_NIEMEIER_LABELS:
            assert niemeier_theta_coefficient(label, 0) == 1

    def test_r1_equals_num_roots(self):
        """r(1) = number of roots for all lattices."""
        for label in ALL_NIEMEIER_LABELS:
            expected = NIEMEIER_REGISTRY[label]['num_roots']
            assert niemeier_theta_coefficient(label, 1) == expected

    def test_leech_r1_zero(self):
        """Leech lattice has no roots: r(1) = 0."""
        assert niemeier_theta_coefficient('Leech', 1) == 0

    def test_3E8_r1(self):
        assert niemeier_theta_coefficient('3E8', 1) == 720

    def test_integrality(self):
        """All theta coefficients must be non-negative integers."""
        for label in ALL_NIEMEIER_LABELS:
            for n in range(6):
                r = niemeier_theta_coefficient(label, n)
                assert isinstance(r, int), f"{label}, n={n}: not int"
                assert r >= 0, f"{label}, n={n}: negative"

    def test_negative_n_zero(self):
        assert niemeier_theta_coefficient('Leech', -1) == 0

    def test_c_delta_formula(self):
        """c_delta = (691*N - 65520)/691 for each lattice."""
        for label in ALL_NIEMEIER_LABELS:
            N = NIEMEIER_REGISTRY[label]['num_roots']
            expected = Fraction(691 * N - 65520, 691)
            assert niemeier_c_delta(label) == expected

    def test_c_delta_leech(self):
        """Leech: N=0, c_delta = -65520/691."""
        assert niemeier_c_delta('Leech') == Fraction(-65520, 691)

    def test_theta_series_length(self):
        ts = niemeier_theta_series('3E8', 5)
        assert len(ts) == 6

    def test_theta_series_tuple_type(self):
        ts = niemeier_theta_series('Leech', 3)
        assert isinstance(ts, tuple)


# =========================================================================
# 8. Niemeier complementarity
# =========================================================================


class TestNiemeierComplementarity:

    def test_kappa_sum_zero(self):
        """kappa + kappa' = 0 for all lattice VOAs (AP24: KM/free-field pattern)."""
        for label in ALL_NIEMEIER_LABELS:
            comp = niemeier_complementarity(label)
            assert comp['kappa_sum'] == Rational(0)

    def test_kappa_dual_minus_24(self):
        for label in ALL_NIEMEIER_LABELS:
            comp = niemeier_complementarity(label)
            assert comp['kappa_dual'] == Rational(-24)

    def test_complementarity_type(self):
        comp = niemeier_complementarity('3E8')
        assert comp['complementarity_type'] == 'KM/free-field'


# =========================================================================
# 9. Monster module
# =========================================================================


class TestMonsterModule:

    def test_monster_central_charge(self):
        assert MONSTER_CENTRAL_CHARGE == Rational(24)

    def test_monster_kappa(self):
        """kappa(V^natural) = c/2 = 12 (Virasoro sector, no weight-1 currents)."""
        assert monster_kappa() == Rational(12)

    def test_monster_kappa_distinct_from_niemeier(self):
        """Monster kappa=12 is DIFFERENT from Niemeier kappa=24."""
        assert monster_kappa() != KAPPA_NIEMEIER

    def test_monster_shadow_data_label(self):
        sd = monster_shadow_data()
        assert sd['label'] == 'V^natural'
        assert sd['central_charge'] == Rational(24)

    def test_monster_kappa_in_shadow(self):
        sd = monster_shadow_data()
        assert sd['kappa'] == Rational(12)

    def test_monster_dim_V1_zero(self):
        """V^natural has no weight-1 currents."""
        sd = monster_shadow_data()
        assert sd['dim_V1'] == 0

    def test_monster_griess_dim(self):
        sd = monster_shadow_data()
        assert sd['griess_algebra_dim'] == 196884

    def test_monster_S3_unknown(self):
        """Higher shadows are frontier for V^natural."""
        sd = monster_shadow_data()
        assert sd['S3'] is None
        assert sd['S4'] is None

    def test_monster_shadow_class_M(self):
        sd = monster_shadow_data()
        assert 'M' in sd['shadow_class']

    def test_monster_F1(self):
        """F_1(V^natural) = 12/24 = 1/2."""
        assert monster_genus_amplitude(1) == Rational(1, 2)

    def test_monster_F2(self):
        """F_2(V^natural) = 12 * 7/5760 = 7/480."""
        assert monster_genus_amplitude(2) == Rational(12) * Rational(7, 5760)


# =========================================================================
# 10. J-function and Monster partition function
# =========================================================================


class TestJFunction:

    def test_j_polar_coefficient(self):
        assert j_invariant_polar_coefficient() == 1

    def test_j_constant_term_zero(self):
        """J(tau) = j(tau) - 744 has constant term 0."""
        coeffs = j_function_coefficients(5)
        assert coeffs[0] == 0

    def test_j_c1_196884(self):
        coeffs = j_function_coefficients(5)
        assert coeffs[1] == 196884

    def test_j_c2(self):
        coeffs = j_function_coefficients(5)
        assert coeffs[2] == 21493760

    def test_j_known_coefficients(self):
        """Verify all hardcoded known J coefficients match computation."""
        coeffs = j_function_coefficients(10)
        for n, expected in KNOWN_J_COEFFICIENTS.items():
            assert coeffs[n] == expected, f"J[{n}]: got {coeffs[n]}, expected {expected}"

    def test_monster_partition_constant_zero(self):
        pc = monster_partition_coefficients(5)
        assert pc['constant_term'] == 0

    def test_monster_partition_dim_V1(self):
        """dim V_1 of J is the coefficient of q^1 = 196884."""
        pc = monster_partition_coefficients(5)
        assert pc['dim_V1'] == 196884

    def test_monster_partition_dim_V2(self):
        pc = monster_partition_coefficients(5)
        assert pc['dim_V2'] == 21493760


# =========================================================================
# 11. Monster representation decomposition
# =========================================================================


class TestMonsterRepDecomposition:

    def test_mckay_observation(self):
        """196884 = 196883 + 1 (McKay's observation)."""
        d = monster_rep_decomposition(1)
        assert d is not None
        assert d['total_dim'] == 196884
        assert d['mckay_observation'] is True
        irrep_dims = [dim for dim, _ in d['irreps']]
        assert 196883 in irrep_dims
        assert 1 in irrep_dims

    def test_V2_decomposition(self):
        d = monster_rep_decomposition(2)
        assert d is not None
        assert d['total_dim'] == 21493760
        irrep_dims = [dim for dim, _ in d['irreps']]
        assert sum(irrep_dims) == 21493760

    def test_vacuum(self):
        d = monster_rep_decomposition(0)
        assert d is not None
        assert d['total_dim'] == 1

    def test_unknown_returns_none(self):
        assert monster_rep_decomposition(100) is None


# =========================================================================
# 12. McKay-Thompson series
# =========================================================================


class TestMcKayThompson:

    def test_identity_equals_J(self):
        """T_{1A} = J(tau)."""
        t1a = mckay_thompson_identity(5)
        j_c = j_function_coefficients(5)
        assert t1a == j_c

    def test_2A_type(self):
        """T_{2A} returns a tuple of correct length."""
        t2a = mckay_thompson_2A(5)
        assert isinstance(t2a, tuple)
        assert len(t2a) == 6


# =========================================================================
# 13. Umbral moonshine data
# =========================================================================


class TestUmbralMoonshine:

    def test_leech_monstrous(self):
        """Leech lattice gives monstrous, not umbral, moonshine."""
        d = umbral_moonshine_data('Leech')
        assert 'monstrous' in d['type']

    def test_24A1_mathieu(self):
        d = umbral_moonshine_data('24A1')
        assert d['umbral_group'] == 'M_24'
        assert d['is_mathieu'] is True

    def test_24A1_order(self):
        d = umbral_moonshine_data('24A1')
        assert d['umbral_group_order'] == 244823040

    def test_12A2_umbral(self):
        d = umbral_moonshine_data('12A2')
        assert d['umbral_group'] == '2.M_12'

    def test_non_tabulated(self):
        d = umbral_moonshine_data('D24')
        assert d['type'] == 'umbral'


# =========================================================================
# 14. Mathieu moonshine coefficients
# =========================================================================


class TestMathieuMoonshine:

    def test_A0(self):
        """A_0 = -2 (vacuum subtraction)."""
        coeffs = mathieu_moonshine_coefficients(5)
        assert coeffs[0] == -2

    def test_A1(self):
        assert mathieu_moonshine_coefficients(5)[1] == 90

    def test_A2(self):
        assert mathieu_moonshine_coefficients(5)[2] == 462

    def test_length(self):
        coeffs = mathieu_moonshine_coefficients(10)
        assert len(coeffs) == 11

    def test_rep_check_A1(self):
        d = mathieu_rep_check(1)
        assert d is not None
        assert d['coefficient'] == 90
        assert d['is_representation'] is True

    def test_rep_check_A2(self):
        d = mathieu_rep_check(2)
        assert d is not None
        assert d['coefficient'] == 462

    def test_rep_check_unknown(self):
        assert mathieu_rep_check(50) is None


# =========================================================================
# 15. Thompson group VOA
# =========================================================================


class TestThompsonVOA:

    def test_central_charge(self):
        assert THOMPSON_CENTRAL_CHARGE == Rational(47, 2)

    def test_kappa(self):
        """kappa(V_Th) = c/2 = 47/4."""
        assert thompson_kappa() == Rational(47, 4)

    def test_F1(self):
        """F_1(V_Th) = (47/4)/24 = 47/96."""
        assert thompson_genus1_amplitude() == Rational(47, 96)

    def test_shadow_data(self):
        sd = thompson_shadow_data()
        assert sd['label'] == 'V_Th'
        assert sd['central_charge'] == Rational(47, 2)
        assert sd['kappa'] == Rational(47, 4)
        assert sd['F1'] == Rational(47, 96)
        assert 'M' in sd['shadow_class']

    def test_thompson_group_order(self):
        sd = thompson_shadow_data()
        assert sd['group_order'] == 90745943887872000


# =========================================================================
# 16. Comparison functions
# =========================================================================


class TestComparisons:

    def test_kappa_comparison_values(self):
        kc = kappa_comparison()
        assert kc['Niemeier'] == Rational(24)
        assert kc['Monster'] == Rational(12)
        assert kc['Thompson'] == Rational(47, 4)

    def test_genus1_comparison(self):
        g1 = genus1_comparison()
        assert g1['Niemeier'] == Rational(1)
        assert g1['Monster'] == Rational(1, 2)
        assert g1['Thompson'] == Rational(47, 96)

    def test_shadow_class_comparison(self):
        sc = shadow_class_comparison()
        assert 'G' in sc['Niemeier']
        assert 'M' in sc['Monster']
        assert 'M' in sc['Thompson']

    def test_all_three_distinct_kappas(self):
        kc = kappa_comparison()
        vals = list(kc.values())
        assert len(set(vals)) == 3, "All three kappas should be distinct"


# =========================================================================
# 17. Theta collision analysis
# =========================================================================


class TestThetaCollisions:

    def test_collisions_exist(self):
        """Some Niemeier lattices share the same number of roots."""
        collisions = lattices_sharing_root_count()
        assert len(collisions) > 0

    def test_collision_resolution(self):
        res = root_count_collision_resolution(3)
        for N, data in res.items():
            # Lattices with same N_roots have identical genus-1 theta
            assert data['theta_identical'] is True
            # But different root systems
            assert data['root_systems_differ'] is True


# =========================================================================
# 18. Shadow tower resolving power
# =========================================================================


class TestResolvingPower:

    def test_niemeier_same_kappa(self):
        rp = shadow_tower_resolving_power()
        assert rp['niemeier_all_same_kappa'] is True

    def test_monster_distinct(self):
        rp = shadow_tower_resolving_power()
        assert rp['monster_distinct_from_niemeier'] is True

    def test_thompson_distinct(self):
        rp = shadow_tower_resolving_power()
        assert rp['thompson_distinct_from_both'] is True


# =========================================================================
# 19. Full atlas
# =========================================================================


class TestFullAtlas:

    def test_atlas_has_26_entries(self):
        """24 Niemeier + Monster + Thompson = 26."""
        atlas = full_atlas(max_g=2, max_n_theta=3)
        assert len(atlas) == 26

    def test_atlas_has_monster(self):
        atlas = full_atlas(max_g=2, max_n_theta=2)
        assert 'Monster' in atlas

    def test_atlas_has_thompson(self):
        atlas = full_atlas(max_g=2, max_n_theta=2)
        assert 'Thompson' in atlas

    def test_atlas_niemeier_entries(self):
        atlas = full_atlas(max_g=2, max_n_theta=2)
        for label in ALL_NIEMEIER_LABELS:
            assert label in atlas
            assert atlas[label]['type'] == 'Niemeier lattice VOA'


# =========================================================================
# 20. Verification functions
# =========================================================================


class TestVerificationFunctions:

    def test_all_niemeier_shadow_identical(self):
        assert verify_all_niemeier_shadow_identical() is True

    def test_theta_integrality(self):
        assert verify_theta_integrality(3) is True

    def test_theta_r1_equals_roots(self):
        assert verify_theta_r1_equals_roots() is True

    def test_j_function_verification(self):
        assert verify_j_function_coefficients() is True

    def test_monster_kappa_distinct_verification(self):
        assert verify_monster_kappa_distinct() is True

    def test_complementarity_sum_zero(self):
        assert verify_complementarity_sum_zero() is True


# =========================================================================
# 21. Griess algebra frontier
# =========================================================================


class TestGriessFrontier:

    def test_griess_bound_returns_dict(self):
        d = griess_shadow_S3_bound()
        assert d['griess_dim'] == 196884
        assert d['computation_status'] == 'open'
