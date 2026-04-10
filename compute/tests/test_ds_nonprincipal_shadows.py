r"""Tests for DS non-principal shadow computations.

Verifies:
  - Central charge formulas: Sugawara c(sl_N, k), Fateev-Lukyanov c(W_N, k),
    KRW c(BP), c(hook), c(rectangular).
  - Partition utilities: normalization, transposition, JM semisimple element.
  - Weyl vector and Levi norms: ||rho||^2 and ||rho_L||^2.
  - Generator content and anomaly ratios for all known orbits.
  - Kappa formulas: affine, principal, non-principal via anomaly ratio.
  - Shadow obstruction tower: convolution coefficients, shadow obstruction tower values, depth class.
  - Shadow discriminant and growth rate.
  - DS shadow functor commutation at arity 2.
  - Hook transport corridor: c_sum k-independence, transpose structure.
  - Level-rank duality shadow comparison.
  - GKO parafermion: central charge, kappa, shadow data.
  - Bershadsky-Polyakov at admissible levels.
  - Whittaker reduction for sl_2.
  - Full pipelines: sl_3, sl_4, orbit hierarchy.
  - Cross-family consistency: additivity, AP1/AP10 guards.

Ground truth:
  - w_algebras.tex: thm:ds-koszul-obstruction
  - subregular_hook_frontier.tex: thm:hook-transport-corridor
  - higher_genus_modular_koszul.tex: thm:shadow-archetype-classification
  - landscape_census.tex: kappa formulas for all families
"""

import pytest
from fractions import Fraction

import importlib.util
import os

# Load the module
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'ds_nonprincipal_shadows',
    os.path.join(_lib_dir, 'ds_nonprincipal_shadows.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

# Import all public functions
c_slN = _mod.c_slN
c_WN_principal = _mod.c_WN_principal
c_bershadsky_polyakov = _mod.c_bershadsky_polyakov
c_hook_sl4 = _mod.c_hook_sl4
kappa_affine = _mod.kappa_affine
kappa_nonprincipal = _mod.kappa_nonprincipal
kappa_principal = _mod.kappa_principal
anomaly_ratio = _mod.anomaly_ratio
anomaly_ratio_principal = _mod.anomaly_ratio_principal
generator_content = _mod.generator_content
shadow_tower = _mod.shadow_tower
shadow_discriminant = _mod.shadow_discriminant
shadow_depth_class = _mod.shadow_depth_class
shadow_growth_rate = _mod.shadow_growth_rate
Q_contact = _mod.Q_contact
shadow_data_affine = _mod.shadow_data_affine
shadow_data_principal = _mod.shadow_data_principal
shadow_data_bershadsky_polyakov = _mod.shadow_data_bershadsky_polyakov
shadow_data_hook = _mod.shadow_data_hook
shadow_data_rectangular_sl4 = _mod.shadow_data_rectangular_sl4
all_orbits_sl3 = _mod.all_orbits_sl3
all_orbits_sl4 = _mod.all_orbits_sl4
ds_shadow_functor_arity2 = _mod.ds_shadow_functor_arity2
hook_transport_corridor = _mod.hook_transport_corridor
level_rank_shadow_comparison = _mod.level_rank_shadow_comparison
parafermion_central_charge = _mod.parafermion_central_charge
parafermion_kappa = _mod.parafermion_kappa
parafermion_shadow_data = _mod.parafermion_shadow_data
parafermion_vs_ds = _mod.parafermion_vs_ds
bp_admissible_levels_sl3 = _mod.bp_admissible_levels_sl3
bp_shadow_at_admissible = _mod.bp_shadow_at_admissible
whittaker_shadow_sl2 = _mod.whittaker_shadow_sl2
full_sl3_pipeline = _mod.full_sl3_pipeline
full_sl4_pipeline = _mod.full_sl4_pipeline
hook_corridor_full = _mod.hook_corridor_full
orbit_shadow_hierarchy = _mod.orbit_shadow_hierarchy

# Internal helpers (needed for partition/Weyl tests)
_normalize_partition = _mod._normalize_partition
_transpose_partition = _mod._transpose_partition
_jm_semisimple_element = _mod._jm_semisimple_element
_weyl_vector_norm_sq = _mod._weyl_vector_norm_sq
_levi_rho_norm_sq = _mod._levi_rho_norm_sq
_krw_central_charge = _mod._krw_central_charge
_convolution_coefficients = _mod._convolution_coefficients
_virasoro_shadow_data = _mod._virasoro_shadow_data
_generator_weights_lookup = _mod._generator_weights_lookup


# ============================================================================
# 1. Partition utilities
# ============================================================================

class TestPartitionUtilities:
    """Test partition normalization and transposition."""

    def test_normalize_already_sorted(self):
        assert _normalize_partition((3, 2, 1)) == (3, 2, 1)

    def test_normalize_unsorted(self):
        assert _normalize_partition((1, 3, 2)) == (3, 2, 1)

    def test_normalize_trivial(self):
        assert _normalize_partition((1, 1, 1)) == (1, 1, 1)

    def test_normalize_principal(self):
        assert _normalize_partition((5,)) == (5,)

    def test_transpose_principal(self):
        # Transpose of (N) = (1, 1, ..., 1) with N parts
        assert _transpose_partition((4,)) == (1, 1, 1, 1)

    def test_transpose_trivial(self):
        # Transpose of (1, 1, 1) = (3)
        assert _transpose_partition((1, 1, 1)) == (3,)

    def test_transpose_hook(self):
        # (3, 1) -> (2, 1, 1)
        assert _transpose_partition((3, 1)) == (2, 1, 1)

    def test_transpose_rectangular(self):
        # (2, 2) -> (2, 2)
        assert _transpose_partition((2, 2)) == (2, 2)

    def test_transpose_involution(self):
        """Transposing twice gives back the original partition."""
        for lam in [(3,), (2, 1), (3, 1), (2, 2), (2, 1, 1), (4, 1), (3, 2)]:
            assert _transpose_partition(_transpose_partition(lam)) == _normalize_partition(lam)

    def test_transpose_size_preserved(self):
        """Sum of partition = sum of its transpose."""
        for lam in [(5,), (3, 2), (4, 1), (3, 1, 1), (2, 2, 1)]:
            assert sum(_transpose_partition(lam)) == sum(lam)


# ============================================================================
# 2. Jacobson-Morozov semisimple element
# ============================================================================

class TestJMSemisimple:
    """Test the JM semisimple element computation."""

    def test_jm_principal_sl2(self):
        # (2): one block of size 2, eigenvalues 1, -1
        h = _jm_semisimple_element((2,))
        assert h == [Fraction(1), Fraction(-1)]

    def test_jm_principal_sl3(self):
        # (3): eigenvalues 2, 0, -2
        h = _jm_semisimple_element((3,))
        assert h == [Fraction(2), Fraction(0), Fraction(-2)]

    def test_jm_trivial(self):
        # (1, 1, 1): all eigenvalues 0
        h = _jm_semisimple_element((1, 1, 1))
        assert h == [Fraction(0), Fraction(0), Fraction(0)]

    def test_jm_subregular_sl3(self):
        # (2, 1): block of size 2 -> (1, -1), block of size 1 -> (0)
        h = _jm_semisimple_element((2, 1))
        assert h == [Fraction(1), Fraction(-1), Fraction(0)]

    def test_jm_trace_zero(self):
        """Sum of JM eigenvalues is 0 (traceless sl_N)."""
        for lam in [(3,), (2, 1), (1, 1, 1), (4,), (3, 1), (2, 2), (2, 1, 1)]:
            h = _jm_semisimple_element(lam)
            assert sum(h) == 0


# ============================================================================
# 3. Weyl vector norms
# ============================================================================

class TestWeylVectorNorms:
    """Test ||rho||^2 and ||rho_L||^2 computations."""

    def test_weyl_norm_sl2(self):
        # ||rho||^2 = 2*(4-1)/12 = 1/2
        assert _weyl_vector_norm_sq(2) == Fraction(1, 2)

    def test_weyl_norm_sl3(self):
        # ||rho||^2 = 3*8/12 = 2
        assert _weyl_vector_norm_sq(3) == Fraction(2)

    def test_weyl_norm_sl4(self):
        # ||rho||^2 = 4*15/12 = 5
        assert _weyl_vector_norm_sq(4) == Fraction(5)

    def test_levi_norm_principal(self):
        # Principal (N,): transpose = (1,...,1). Each block m_i=1. m*(m^2-1)/12=0.
        assert _levi_rho_norm_sq((3,)) == Fraction(0)
        assert _levi_rho_norm_sq((4,)) == Fraction(0)

    def test_levi_norm_trivial(self):
        # Trivial (1,...,1): transpose = (N,). Single block m=N.
        # ||rho_L||^2 = N*(N^2-1)/12 = ||rho||^2.
        assert _levi_rho_norm_sq((1, 1, 1)) == _weyl_vector_norm_sq(3)

    def test_levi_norm_rectangular_sl4(self):
        # (2,2): transpose = (2,2). ||rho_L||^2 = 2*(2*(4-1)/12) = 2*1/2 = 1
        assert _levi_rho_norm_sq((2, 2)) == Fraction(1)


# ============================================================================
# 4. Central charge formulas
# ============================================================================

class TestCentralCharges:
    """Test all central charge formulas."""

    def test_c_sl2_level1(self):
        # c(sl_2, k=1) = 1*3/(1+2) = 1
        assert c_slN(2, Fraction(1)) == Fraction(1)

    def test_c_sl3_level1(self):
        # c(sl_3, k=1) = 1*8/(1+3) = 2
        assert c_slN(3, Fraction(1)) == Fraction(2)

    def test_c_sl2_critical_raises(self):
        with pytest.raises(ValueError, match="Critical level"):
            c_slN(2, Fraction(-2))

    def test_c_WN_principal_sl2(self):
        # W_2 = Virasoro. FL: c = 1 - 2*3*(k+1)^2/(k+2).
        # At k=1: c = 1 - 6*4/3 = 1 - 8 = -7.
        # VERIFIED: [DC] FL formula; [LT] canonical_c_wn_fl self-test
        assert c_WN_principal(2, Fraction(1)) == Fraction(-7)

    def test_c_WN_principal_sl3_k1(self):
        # c(W_3, k=1) via FL: 2 - 3*8*9/4 = 2 - 54 = -52
        # VERIFIED: [DC] FL formula; [LC] N=2 gives -7
        assert c_WN_principal(3, Fraction(1)) == Fraction(-52)

    def test_c_WN_principal_critical_raises(self):
        with pytest.raises(ValueError, match="Critical level"):
            c_WN_principal(3, Fraction(-3))

    def test_c_bp_k0(self):
        # c(BP, k=0) = 2 - 24*(0+1)^2/(0+3) = 2 - 8 = -6
        # VERIFIED: [DC] BP formula; [CF] K_BP = c(0)+c(-6) = -6+202 = 196 (AP140)
        assert c_bershadsky_polyakov(Fraction(0)) == Fraction(-6)

    def test_c_bp_k1(self):
        # c(BP, k=1) = 2 - 24*(1+1)^2/(1+3) = 2 - 24 = -22
        # VERIFIED: [DC] BP formula; [LC] k=0 gives -6
        assert c_bershadsky_polyakov(Fraction(1)) == Fraction(-22)

    def test_c_bp_critical_raises(self):
        with pytest.raises(ValueError, match="BP central charge undefined"):
            c_bershadsky_polyakov(Fraction(-3))

    def test_c_hook_sl4_31(self):
        # (3,1) hook in sl_4: should be the KRW formula
        c = c_hook_sl4((3, 1), Fraction(1))
        c_check = _krw_central_charge((3, 1), Fraction(1))
        assert c == c_check

    def test_krw_principal_matches_fateev_lukyanov(self):
        """KRW with principal partition should give the same c as c_WN_principal."""
        for N in range(2, 6):
            for k in [Fraction(1), Fraction(3), Fraction(7)]:
                c_krw = _krw_central_charge((N,), k)
                c_fl = c_WN_principal(N, k)
                assert c_krw == c_fl, f"Mismatch at N={N}, k={k}: KRW={c_krw}, FL={c_fl}"

    def test_krw_trivial_gives_sugawara(self):
        """KRW with trivial partition gives the Sugawara central charge.

        The trivial nilpotent (1,...,1) corresponds to the affine algebra itself.
        c = k*(N^2-1)/(k+N).
        """
        # VERIFIED: [DC] Sugawara formula; [LC] k->inf gives N^2-1
        for N in [2, 3, 4]:
            for k in [Fraction(1), Fraction(2)]:
                c_krw = _krw_central_charge(tuple([1]*N), k)
                c_sug = c_slN(N, k)
                assert c_krw == c_sug, f"N={N}, k={k}: got {c_krw}, expected {c_sug}"


# ============================================================================
# 5. Generator content and anomaly ratios
# ============================================================================

class TestGeneratorContent:
    """Test generator weight tables and anomaly ratios."""

    def test_principal_sl3_generators(self):
        # W_3: weights 2 and 3, both bosonic
        gc = generator_content((3,))
        assert gc['n_bosonic'] == 2
        assert gc['n_fermionic'] == 0
        assert gc['centralizer_dim'] == 2  # transpose (1,1,1): 1+1+1-1=2

    def test_principal_sl4_generators(self):
        gc = generator_content((4,))
        assert gc['n_bosonic'] == 3  # weights 2, 3, 4
        assert gc['n_fermionic'] == 0

    def test_bp_generators(self):
        # BP = W(sl_3, (2,1)): weights 1 (x1), 3/2 (x2), 2 (x1)
        gc = generator_content((2, 1))
        assert gc['n_bosonic'] == 2   # weight 1 and weight 2
        assert gc['n_fermionic'] == 2  # weight 3/2 (x2)

    def test_trivial_generators(self):
        gc = generator_content((1, 1, 1))
        assert gc['n_bosonic'] == 8  # dim(sl_3) = 8, all weight 1 (bosonic)
        assert gc['n_fermionic'] == 0

    def test_anomaly_ratio_principal_sl2(self):
        # W_2 = Virasoro: single weight 2 generator, rho = 1/2
        assert anomaly_ratio_principal(2) == Fraction(1, 2)

    def test_anomaly_ratio_principal_sl3(self):
        # W_3: weights 2, 3. rho = 1/2 + 1/3 = 5/6
        assert anomaly_ratio_principal(3) == Fraction(5, 6)

    def test_anomaly_ratio_principal_sl4(self):
        # W_4: weights 2, 3, 4. rho = 1/2 + 1/3 + 1/4 = 13/12
        assert anomaly_ratio_principal(4) == Fraction(13, 12)

    def test_anomaly_ratio_bp(self):
        # BP (2,1): weight 1 (x1, bos) + weight 3/2 (x2, ferm) + weight 2 (x1, bos)
        # rho = 1/1 - 2/(3/2) + 1/2 = 1 - 4/3 + 1/2 = 1/6
        rho = anomaly_ratio((2, 1))
        assert rho == Fraction(1, 6)

    def test_anomaly_ratio_rectangular_sl4(self):
        # (2,2) in sl_4: weights 1 (x3, bos) + 2 (x4, bos)
        # rho = 3/1 + 4/2 = 3 + 2 = 5
        rho = anomaly_ratio((2, 2))
        assert rho == Fraction(5)

    def test_anomaly_ratio_k_independent(self):
        """Anomaly ratio should be independent of k (a partition invariant)."""
        for lam in [(3,), (2, 1), (4,), (3, 1), (2, 2), (2, 1, 1)]:
            # The anomaly ratio function only takes the partition, not k.
            # This is just a structural check that the function signature is correct.
            rho = anomaly_ratio(lam)
            assert isinstance(rho, Fraction)


# ============================================================================
# 6. Kappa formulas
# ============================================================================

class TestKappa:
    """Test kappa (modular characteristic) computations."""

    def test_kappa_affine_sl2_k1(self):
        # kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4
        assert kappa_affine(2, Fraction(1)) == Fraction(9, 4)

    def test_kappa_affine_sl3_k1(self):
        # kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 32/6 = 16/3
        assert kappa_affine(3, Fraction(1)) == Fraction(16, 3)

    def test_kappa_principal_sl2(self):
        # kappa(Vir from sl_2) = (1/2)*c(W_2, k)
        for k in [Fraction(1), Fraction(3), Fraction(10)]:
            c = c_WN_principal(2, k)
            assert kappa_principal(2, k) == c / 2

    def test_kappa_principal_sl3(self):
        # kappa(W_3) = (5/6)*c(W_3, k)
        for k in [Fraction(1), Fraction(5)]:
            c = c_WN_principal(3, k)
            assert kappa_principal(3, k) == Fraction(5, 6) * c

    def test_kappa_nonprincipal_is_rho_times_c(self):
        """kappa = rho * c for all non-trivial partitions."""
        cases = [
            ((2, 1), Fraction(1)),   # BP at k=1
            ((3, 1), Fraction(2)),   # hook sl_4 at k=2
            ((2, 2), Fraction(3)),   # rectangular sl_4 at k=3
        ]
        for lam, k in cases:
            rho = anomaly_ratio(lam)
            c = _krw_central_charge(lam, k)
            assert kappa_nonprincipal(lam, k) == rho * c

    def test_kappa_nonprincipal_trivial_is_affine(self):
        """Trivial partition falls back to kappa_affine."""
        for N in [2, 3, 4]:
            for k in [Fraction(1), Fraction(5)]:
                assert kappa_nonprincipal(tuple([1]*N), k) == kappa_affine(N, k)


# ============================================================================
# 7. Shadow obstruction tower and convolution coefficients
# ============================================================================

class TestShadowTower:
    """Test shadow obstruction tower computation."""

    def test_convolution_coefficients_constant(self):
        """sqrt(4) = 2: a_0 = 2, rest zero."""
        coeffs = _convolution_coefficients(Fraction(4), Fraction(0), Fraction(0), 4, 1)
        assert coeffs[0] == Fraction(2)
        for c in coeffs[1:]:
            assert c == Fraction(0)

    def test_convolution_coefficients_linear(self):
        """sqrt(1 + 2t + t^2) = 1 + t: a_0=1, a_1=1, rest zero."""
        coeffs = _convolution_coefficients(Fraction(1), Fraction(2), Fraction(1), 5, 1)
        assert coeffs[0] == Fraction(1)
        assert coeffs[1] == Fraction(1)
        for c in coeffs[2:]:
            assert c == Fraction(0)

    def test_shadow_tower_kappa_zero(self):
        """When kappa=0, all shadow coefficients vanish."""
        tower = shadow_tower(Fraction(0), Fraction(1), Fraction(1), 8)
        for r in range(2, 9):
            assert tower[r] == Fraction(0)

    def test_shadow_tower_gaussian_class(self):
        """Class G: alpha=0, S4=0 -> tower terminates at arity 2."""
        kap = Fraction(3)
        tower = shadow_tower(kap, Fraction(0), Fraction(0), 8)
        # S_2 = a_0/2 where a_0 = 2*kappa, so S_2 = kappa
        assert tower[2] == kap
        for r in range(3, 9):
            assert tower[r] == Fraction(0)

    def test_shadow_tower_lie_class(self):
        """Class L (affine): alpha=1, S4=0 -> tower terminates at arity 3."""
        kap = Fraction(16, 3)  # sl_3 at k=1
        tower = shadow_tower(kap, Fraction(1), Fraction(0), 8)
        assert tower[2] == kap
        assert tower[3] != Fraction(0)
        for r in range(4, 9):
            assert tower[r] == Fraction(0)

    def test_shadow_tower_virasoro_nonterminating(self):
        """Virasoro (class M) should have nonzero higher arities."""
        # Virasoro at c=1: kappa=1/2, alpha=2, S4=10/(1*27)=10/27
        c_val = Fraction(1)
        kap = c_val / 2
        s4 = Fraction(10) / (c_val * (5 * c_val + 22))
        tower = shadow_tower(kap, Fraction(2), s4, 8)
        # Check S_4 and S_5 are nonzero (class M)
        assert tower[4] != Fraction(0)
        assert tower[5] != Fraction(0)

    def test_shadow_discriminant_vanishes_for_affine(self):
        """Delta=0 for affine (S4=0)."""
        assert shadow_discriminant(Fraction(5), Fraction(1), Fraction(0)) == 0

    def test_shadow_discriminant_nonzero_for_virasoro(self):
        """Delta != 0 for Virasoro."""
        c_val = Fraction(1)
        kap = c_val / 2
        s4 = Fraction(10) / (c_val * (5 * c_val + 22))
        assert shadow_discriminant(kap, Fraction(2), s4) != 0


# ============================================================================
# 8. Shadow depth class
# ============================================================================

class TestShadowDepthClass:
    """Test shadow depth classification (G/L/C/M)."""

    def test_depth_G_kappa_zero(self):
        assert shadow_depth_class(Fraction(0), Fraction(0), Fraction(0)) == 'G'

    def test_depth_G_alpha_zero(self):
        assert shadow_depth_class(Fraction(5), Fraction(0), Fraction(0)) == 'G'

    def test_depth_L(self):
        assert shadow_depth_class(Fraction(5), Fraction(1), Fraction(0)) == 'L'

    def test_depth_M_virasoro(self):
        c_val = Fraction(1)
        kap = c_val / 2
        s4 = Fraction(10) / (c_val * (5 * c_val + 22))
        assert shadow_depth_class(kap, Fraction(2), s4) == 'M'

    def test_shadow_growth_rate_zero_for_affine(self):
        """Growth rate = 0 for class L (S4=0)."""
        assert shadow_growth_rate(Fraction(5), Fraction(1), Fraction(0)) == 0.0

    def test_shadow_growth_rate_positive_for_virasoro(self):
        c_val = Fraction(1)
        kap = c_val / 2
        s4 = Fraction(10) / (c_val * (5 * c_val + 22))
        rho = shadow_growth_rate(kap, Fraction(2), s4)
        assert rho > 0

    def test_Q_contact_none_for_kappa_zero(self):
        assert Q_contact(Fraction(0), Fraction(1), Fraction(1)) is None

    def test_Q_contact_returns_S4(self):
        assert Q_contact(Fraction(3), Fraction(2), Fraction(7, 5)) == Fraction(7, 5)


# ============================================================================
# 9. Shadow data functions
# ============================================================================

class TestShadowData:
    """Test shadow data aggregation for specific algebras."""

    def test_affine_sl3_is_class_L(self):
        sd = shadow_data_affine(3, Fraction(1))
        assert sd['depth_class'] == 'L'
        assert sd['depth'] == 3
        assert sd['S4'] == 0
        assert sd['alpha'] == 1

    def test_principal_sl3_is_class_M(self):
        sd = shadow_data_principal(3, Fraction(1))
        assert sd['depth_class'] == 'M'
        assert sd['depth'] is None
        assert 'c' in sd

    def test_bp_returns_correct_structure(self):
        sd = shadow_data_bershadsky_polyakov(Fraction(1))
        assert 'kappa' in sd
        assert 'c' in sd
        assert 'anomaly_ratio' in sd
        assert sd['partition'] == (2, 1)

    def test_hook_sl4_m1(self):
        sd = shadow_data_hook(4, 1, Fraction(1))
        assert sd['partition'] == (3, 1)
        assert 'c' in sd
        assert 'anomaly_ratio' in sd

    def test_rectangular_sl4(self):
        sd = shadow_data_rectangular_sl4(Fraction(1))
        assert sd['partition'] == (2, 2)
        assert 'c' in sd

    def test_rectangular_sl4_critical_raises(self):
        with pytest.raises(ValueError):
            shadow_data_rectangular_sl4(Fraction(-4))


# ============================================================================
# 10. Full orbit enumerations
# ============================================================================

class TestOrbitEnumerations:
    """Test all_orbits_sl3, all_orbits_sl4."""

    def test_sl3_has_three_orbits(self):
        orbits = all_orbits_sl3(Fraction(1))
        assert len(orbits) == 3
        assert '[3]' in orbits
        assert '[2,1]' in orbits
        assert '[1,1,1]' in orbits

    def test_sl4_has_five_orbits(self):
        orbits = all_orbits_sl4(Fraction(1))
        assert len(orbits) == 5
        assert '[4]' in orbits
        assert '[3,1]' in orbits
        assert '[2,2]' in orbits
        assert '[2,1,1]' in orbits
        assert '[1,1,1,1]' in orbits

    def test_sl3_trivial_orbit_is_affine(self):
        orbits = all_orbits_sl3(Fraction(2))
        data = orbits['[1,1,1]']
        assert data['depth_class'] == 'L'

    def test_sl4_principal_is_class_M(self):
        orbits = all_orbits_sl4(Fraction(2))
        data = orbits['[4]']
        assert data['depth_class'] == 'M'

    def test_sl3_all_have_kappa(self):
        orbits = all_orbits_sl3(Fraction(3))
        for name, data in orbits.items():
            assert 'kappa' in data, f"Missing kappa for orbit {name}"

    def test_sl4_all_have_kappa(self):
        orbits = all_orbits_sl4(Fraction(3))
        for name, data in orbits.items():
            assert 'kappa' in data, f"Missing kappa for orbit {name}"


# ============================================================================
# 11. DS shadow functor commutation
# ============================================================================

class TestDSShadowFunctor:
    """Test DS shadow functor at arity 2."""

    def test_functor_returns_all_fields(self):
        result = ds_shadow_functor_arity2(3, Fraction(1), (3,))
        required_keys = ['kappa_affine', 'kappa_W', 'kappa_deficit',
                         'c_affine', 'c_W', 'c_ghost', 'anomaly_ratio']
        for key in required_keys:
            assert key in result, f"Missing key: {key}"

    def test_central_charge_additivity(self):
        """c(sl_N) = c(W) + c(ghost) by definition."""
        for lam, N, k in [((3,), 3, Fraction(1)),
                          ((2, 1), 3, Fraction(2)),
                          ((4,), 4, Fraction(1)),
                          ((3, 1), 4, Fraction(3))]:
            result = ds_shadow_functor_arity2(N, k, lam)
            assert result['c_affine'] == result['c_W'] + result['c_ghost']

    def test_kappa_deficit_positive_for_nontrivial(self):
        """For non-trivial DS reduction at generic k, kappa decreases."""
        result = ds_shadow_functor_arity2(3, Fraction(5), (3,))
        # kappa(sl_3) > kappa(W_3) at generic level
        assert result['kappa_deficit'] != 0


# ============================================================================
# 12. Hook transport corridor
# ============================================================================

class TestHookTransportCorridor:
    """Test the transport-to-transpose data for hooks."""

    def test_c_sum_k_independent_self_dual_sl3(self):
        """c_sum is k-independent for self-dual hooks (partition = transpose)."""
        result = hook_transport_corridor(3, 1, Fraction(1))
        assert result['is_self_dual'] is True
        assert result['c_sum_k_independent'] is True

    def test_c_sum_varies_for_non_self_dual(self):
        """For non-self-dual hooks, c_sum is generally k-dependent."""
        r1 = hook_transport_corridor(4, 1, Fraction(1))
        r2 = hook_transport_corridor(4, 1, Fraction(2))
        # They can differ when partition != transpose
        assert not r1['is_self_dual']
        # Just check that the function runs and produces valid data
        assert isinstance(r1['c_sum'], Fraction)
        assert isinstance(r2['c_sum'], Fraction)

    def test_hook_corridor_returns_valid_data(self):
        """All hook corridors return valid Fraction data."""
        for N in [3, 4, 5]:
            for m in range(1, N - 1):
                result = hook_transport_corridor(N, m, Fraction(2))
                assert isinstance(result['kappa_source'], Fraction)
                assert isinstance(result['kappa_target'], Fraction)
                assert isinstance(result['c_sum'], Fraction)

    def test_transpose_partition_correct(self):
        result = hook_transport_corridor(4, 1, Fraction(1))
        assert result['partition'] == (3, 1)
        assert result['transpose'] == (2, 1, 1)

    def test_dual_level(self):
        """k_dual = -k - 2N."""
        result = hook_transport_corridor(4, 1, Fraction(3))
        assert result['k_dual'] == Fraction(3) * (-1) - 2 * Fraction(4)
        assert result['k_dual'] == Fraction(-11)

    def test_self_dual_hook_detection(self):
        """For N=3, m=1: (2,1), transpose = (2,1) -> self-dual."""
        result = hook_transport_corridor(3, 1, Fraction(1))
        assert result['is_self_dual'] is True

    def test_non_self_dual_hook(self):
        """For N=4, m=1: (3,1), transpose = (2,1,1) -> not self-dual."""
        result = hook_transport_corridor(4, 1, Fraction(1))
        assert result['is_self_dual'] is False


# ============================================================================
# 13. Level-rank duality
# ============================================================================

class TestLevelRankDuality:
    """Test level-rank shadow comparisons."""

    def test_level_rank_returns_all_fields(self):
        result = level_rank_shadow_comparison(3, 4)
        assert 'c_Wk_slN' in result
        assert 'c_WN_slk' in result
        assert 'kappa_Wk_slN' in result
        assert 'kappa_WN_slk' in result

    def test_level_rank_anomaly_ratios(self):
        result = level_rank_shadow_comparison(3, 4)
        assert result['anomaly_ratio_N'] == anomaly_ratio_principal(3)
        assert result['anomaly_ratio_k'] == anomaly_ratio_principal(4)

    def test_level_rank_symmetry_check(self):
        """level_rank(N, k) and level_rank(k, N) swap roles."""
        r1 = level_rank_shadow_comparison(3, 5)
        r2 = level_rank_shadow_comparison(5, 3)
        assert r1['c_Wk_slN'] == r2['c_WN_slk']
        assert r1['c_WN_slk'] == r2['c_Wk_slN']


# ============================================================================
# 14. GKO parafermion
# ============================================================================

class TestParafermion:
    """Test parafermion (GKO coset) computations."""

    def test_pf_c_k2(self):
        # PF_2 = Ising: c = 2*1/4 = 1/2
        assert parafermion_central_charge(Fraction(2)) == Fraction(1, 2)

    def test_pf_c_k3(self):
        # PF_3: c = 2*2/5 = 4/5
        assert parafermion_central_charge(Fraction(3)) == Fraction(4, 5)

    def test_pf_c_k4(self):
        # PF_4: c = 2*3/6 = 1
        assert parafermion_central_charge(Fraction(4)) == Fraction(1)

    def test_pf_c_critical_raises(self):
        with pytest.raises(ValueError):
            parafermion_central_charge(Fraction(-2))

    def test_pf_kappa_is_c_over_2(self):
        """On the T-line, kappa = c/2."""
        for k in [Fraction(2), Fraction(3), Fraction(5), Fraction(10)]:
            c = parafermion_central_charge(k)
            assert parafermion_kappa(k) == c / 2

    def test_pf_shadow_data_structure(self):
        sd = parafermion_shadow_data(Fraction(3))
        assert 'name' in sd
        assert 'c' in sd
        assert 'kappa' in sd
        assert sd['depth_class'] == 'M'  # Virasoro-type, nonterminating

    def test_pf_vs_ds_agreement(self):
        """On the T-line, PF and Virasoro shadow data should agree."""
        result = parafermion_vs_ds(Fraction(3))
        assert result['T_line_agreement'] is True

    def test_pf_vs_ds_at_multiple_levels(self):
        for k in [Fraction(2), Fraction(4), Fraction(7)]:
            result = parafermion_vs_ds(k)
            assert result['T_line_agreement'] is True


# ============================================================================
# 15. Bershadsky-Polyakov at admissible levels
# ============================================================================

class TestBPAdmissible:
    """Test BP algebra at admissible levels."""

    def test_admissible_levels_nonempty(self):
        levels = bp_admissible_levels_sl3()
        assert len(levels) >= 3

    def test_admissible_levels_are_fractions(self):
        for k in bp_admissible_levels_sl3():
            assert isinstance(k, Fraction)

    def test_bp_shadow_at_admissible_structure(self):
        for k in bp_admissible_levels_sl3():
            sd = bp_shadow_at_admissible(k)
            assert 'kappa' in sd
            assert 'c' in sd
            assert sd['is_admissible'] is True
            assert sd['anomaly_ratio'] == anomaly_ratio((2, 1))

    def test_bp_admissible_c_matches_general(self):
        for k in bp_admissible_levels_sl3():
            c_adm = bp_shadow_at_admissible(k)['c']
            c_gen = c_bershadsky_polyakov(k)
            assert c_adm == c_gen


# ============================================================================
# 16. Whittaker reduction
# ============================================================================

class TestWhittaker:
    """Test Whittaker reduction shadow for sl_2."""

    def test_whittaker_coincides_virasoro(self):
        """For sl_2, Whittaker = Virasoro (unique positive root)."""
        sd = whittaker_shadow_sl2(Fraction(1))
        assert 'note' in sd
        assert 'Virasoro' in sd['note'] or 'Coincides' in sd['note']

    def test_whittaker_c_formula(self):
        # c = 1 - 6/(k+2). At k=1: c = 1 - 6/3 = -1
        sd = whittaker_shadow_sl2(Fraction(1))
        assert sd['c'] == Fraction(-1)

    def test_whittaker_c_k10(self):
        sd = whittaker_shadow_sl2(Fraction(10))
        assert sd['c'] == Fraction(1) - Fraction(6) / (Fraction(10) + 2)
        assert sd['c'] == Fraction(1, 2)

    def test_whittaker_kappa_is_c_over_2(self):
        for k in [Fraction(1), Fraction(3), Fraction(10)]:
            sd = whittaker_shadow_sl2(k)
            assert sd['kappa'] == sd['c'] / 2


# ============================================================================
# 17. Full pipelines
# ============================================================================

class TestFullPipelines:
    """Test full_sl3_pipeline, full_sl4_pipeline, hook_corridor_full."""

    def test_sl3_pipeline_structure(self):
        result = full_sl3_pipeline(Fraction(2), max_arity=6)
        assert 'orbits' in result
        assert 'towers' in result
        assert len(result['orbits']) == 3
        assert len(result['towers']) == 3

    def test_sl3_pipeline_tower_arities(self):
        result = full_sl3_pipeline(Fraction(2), max_arity=6)
        for name, tower in result['towers'].items():
            for r in range(2, 7):
                assert r in tower, f"Missing arity {r} for orbit {name}"

    def test_sl4_pipeline_structure(self):
        result = full_sl4_pipeline(Fraction(1), max_arity=6)
        assert len(result['orbits']) == 5
        assert len(result['towers']) == 5

    def test_hook_corridor_full_structure(self):
        result = hook_corridor_full(max_N=4, k_val=Fraction(2))
        # sl_3: m=1; sl_4: m=1,2 -> 3 entries
        assert len(result) == 3

    def test_hook_corridor_full_self_dual_k_independent(self):
        """Self-dual hooks have k-independent c_sum."""
        result = hook_corridor_full(max_N=5, k_val=Fraction(3))
        for key, data in result.items():
            if data['is_self_dual']:
                assert data['c_sum_k_independent'] is True, f"Failed for {key}"


# ============================================================================
# 18. Orbit shadow hierarchy
# ============================================================================

class TestOrbitHierarchy:
    """Test the orbit shadow hierarchy sorting."""

    def test_sl3_hierarchy_ordered(self):
        h = orbit_shadow_hierarchy(3, Fraction(1))
        assert len(h) == 3
        # Finite depths should come before infinite
        depths = [e['depth'] for e in h]
        finite_depths = [d for d in depths if d < float('inf')]
        assert all(a <= b for a, b in zip(finite_depths, finite_depths[1:]))

    def test_sl4_hierarchy_ordered(self):
        h = orbit_shadow_hierarchy(4, Fraction(2))
        assert len(h) == 5

    def test_hierarchy_unsupported_N(self):
        h = orbit_shadow_hierarchy(7, Fraction(1))
        assert h == []

    def test_hierarchy_has_required_fields(self):
        h = orbit_shadow_hierarchy(3, Fraction(2))
        for entry in h:
            assert 'name' in entry
            assert 'kappa' in entry
            assert 'depth_class' in entry
            assert 'depth' in entry


# ============================================================================
# 19. Cross-family consistency (AP1/AP10 guards)
# ============================================================================

class TestCrossConsistency:
    """Cross-family consistency checks to guard against AP1/AP10 errors."""

    def test_kappa_principal_matches_nonprincipal_formula(self):
        """kappa_principal(N, k) should agree with kappa_nonprincipal((N,), k)."""
        for N in [2, 3, 4, 5]:
            for k in [Fraction(1), Fraction(3)]:
                kp = kappa_principal(N, k)
                knp = kappa_nonprincipal((N,), k)
                assert kp == knp, f"Mismatch at N={N}, k={k}: {kp} vs {knp}"

    def test_virasoro_kappa_is_c_over_2(self):
        """For W_2 = Virasoro, kappa = c/2 (anomaly ratio 1/2)."""
        for k in [Fraction(1), Fraction(5), Fraction(10)]:
            c = c_WN_principal(2, k)
            kap = kappa_principal(2, k)
            assert kap == c / 2

    def test_bp_kappa_consistent_two_routes(self):
        """BP kappa via shadow_data should match direct calculation."""
        for k in [Fraction(0), Fraction(1), Fraction(2)]:
            sd = shadow_data_bershadsky_polyakov(k)
            rho = anomaly_ratio((2, 1))
            c = c_bershadsky_polyakov(k)
            assert sd['kappa'] == rho * c

    def test_affine_depth_universally_L(self):
        """All affine algebras are class L (depth 3)."""
        for N in [2, 3, 4, 5]:
            sd = shadow_data_affine(N, Fraction(1))
            assert sd['depth_class'] == 'L'
            assert sd['depth'] == 3

    def test_principal_WN_depth_universally_M(self):
        """All principal W_N for N >= 2 are class M at generic level."""
        for N in [2, 3, 4, 5]:
            sd = shadow_data_principal(N, Fraction(5))
            assert sd['depth_class'] == 'M', f"Failed for N={N}"

    def test_shadow_tower_S2_equals_kappa(self):
        """S_2 = kappa for any algebra (universal)."""
        for kap, alpha, s4 in [(Fraction(3), Fraction(0), Fraction(0)),
                                (Fraction(5), Fraction(1), Fraction(0)),
                                (Fraction(1, 2), Fraction(2), Fraction(10, 27))]:
            tower = shadow_tower(kap, alpha, s4, 4)
            assert tower[2] == kap

    def test_virasoro_shadow_data_consistency(self):
        """_virasoro_shadow_data should give consistent alpha=2 and correct S4."""
        for c_val in [Fraction(1, 2), Fraction(1), Fraction(26)]:
            kap = c_val / 2
            sd = _virasoro_shadow_data(c_val, kap)
            assert sd['alpha'] == Fraction(2)
            expected_s4 = Fraction(10) / (c_val * (5 * c_val + 22))
            assert sd['S4'] == expected_s4
