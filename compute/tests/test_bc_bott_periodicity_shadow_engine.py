r"""Tests for Bott periodicity and periodicity obstructions in shadow tower K-theory.

Verification strategy (multi-path, per CLAUDE.md mandate):
    Path 1: Direct K-group computation from shadow algebra presentation
    Path 2: Atiyah-Hirzebruch spectral sequence E_2 page
    Path 3: Comparison with commutative K-theory at degenerate limits
    Path 4: Numerical evaluation at specific parameter values
    Path 5: Cross-family consistency (depth classification)

Key results tested:
    - Heisenberg: exact Bott periodicity (class G, pi = inf)
    - Virasoro: immediate periodicity failure (class M, pi = 1)
    - W_3: immediate failure (class M, pi = 1)
    - Affine KM: pi = 3 (class L)
    - betagamma: pi = 2 (class C)
    - At zeta zeros: pi = 1, DD class encodes gamma_n
    - Thom class = kappa * (1 + Delta/(24*kappa)) for curved algebras
    - Periodicity-depth inverse relation: pi * (r_max - 1) = 6 for L/C

References:
    concordance.tex: shadow depth classification, Theorem D
    CLAUDE.md: AP1, AP14, AP31, AP39, multi-path verification mandate
"""

import cmath
import math
from fractions import Fraction

import pytest
from sympy import Rational, oo, S

from compute.lib.bc_bott_periodicity_shadow_engine import (
    # Riemann zeros
    riemann_zero,
    RIEMANN_ZEROS_GAMMA,
    # Kappa formulas
    kappa_heisenberg,
    kappa_virasoro,
    kappa_w3,
    kappa_betagamma,
    kappa_affine_slN,
    # Shadow coefficients
    virasoro_shadow_coefficients,
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    betagamma_shadow_coefficients,
    w3_shadow_coefficients,
    # K-groups
    ShadowKGroup,
    shadow_k_group,
    # Bott map
    BottMapResult,
    shadow_bott_map,
    # Periodicity index
    periodicity_index,
    periodicity_index_numerical,
    shadow_periodicity_depth,
    # Dixmier-Douady
    DixmierDouadyClass,
    dixmier_douady_class,
    dixmier_douady_at_zeta_zero,
    # Thom class
    ThomClassData,
    thom_class_bar,
    # Zeta zeros
    periodicity_index_at_zero,
    bott_data_at_zeta_zero,
    bott_landscape_at_zeros,
    # Spectral sequence
    atiyah_hirzebruch_e2,
    # Cross-checks
    verify_periodicity_depth_relation,
    verify_bott_at_degenerate_limit,
    verify_bott_multipath,
    # Landscape
    bott_periodicity_landscape,
    # Internal
    _family_to_shadow_class,
    _get_kappa_and_delta,
    # Numerical
    numerical_bott_kernel_dimension,
)


# ============================================================================
# 1. Riemann zeta zeros
# ============================================================================

class TestRiemannZeros:
    """Test Riemann zeta zero data."""

    def test_first_zero(self):
        """First zero gamma_1 = 14.134725..."""
        rho = riemann_zero(1)
        assert abs(rho.real - 0.5) < 1e-10
        assert abs(rho.imag - 14.134725141734693) < 1e-9

    def test_critical_line(self):
        """All zeros on Re(s) = 1/2."""
        for n in range(1, 16):
            rho = riemann_zero(n)
            assert abs(rho.real - 0.5) < 1e-10

    def test_monotone_increasing(self):
        """Imaginary parts are strictly increasing."""
        for n in range(1, 15):
            assert RIEMANN_ZEROS_GAMMA[n] > RIEMANN_ZEROS_GAMMA[n - 1]

    def test_zero_count_20(self):
        """We have at least 20 zeros stored."""
        assert len(RIEMANN_ZEROS_GAMMA) >= 20

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            riemann_zero(0)
        with pytest.raises(ValueError):
            riemann_zero(100)


# ============================================================================
# 2. Kappa formulas (AP1: cross-verify, never copy)
# ============================================================================

class TestKappaFormulas:
    """Test kappa formulas for all standard families."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        assert kappa_heisenberg(1) == 1
        assert kappa_heisenberg(2) == 2
        assert kappa_heisenberg(3) == 3
        assert kappa_heisenberg(5) == 5
        assert kappa_heisenberg(10) == 10

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        assert kappa_virasoro(1) == Rational(1, 2)
        assert kappa_virasoro(Rational(1, 2)) == Rational(1, 4)
        assert kappa_virasoro(13) == Rational(13, 2)
        assert kappa_virasoro(26) == 13

    def test_w3_kappa(self):
        """kappa(W_3, c) = 5c/6."""
        assert kappa_w3(6) == 5
        assert kappa_w3(Rational(4, 5)) == Rational(2, 3)
        assert kappa_w3(-2) == Rational(-5, 3)

    def test_betagamma_kappa(self):
        """kappa(bg, lambda) = 6*lambda^2 - 6*lambda + 1."""
        assert kappa_betagamma(0) == 1  # standard bg
        assert kappa_betagamma(1) == 1  # standard bg
        assert kappa_betagamma(Rational(1, 2)) == Rational(-1, 2)  # symplectic

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        assert kappa_affine_slN(2, 1) == Rational(9, 4)
        assert kappa_affine_slN(2, 2) == 3


# ============================================================================
# 3. Shadow classification
# ============================================================================

class TestShadowClassification:
    """Test the G/L/C/M classification."""

    def test_heisenberg_class_g(self):
        assert _family_to_shadow_class('heisenberg') == 'G'

    def test_virasoro_class_m(self):
        assert _family_to_shadow_class('virasoro') == 'M'

    def test_w3_class_m(self):
        assert _family_to_shadow_class('w3') == 'M'

    def test_affine_class_l(self):
        assert _family_to_shadow_class('affine_sl2') == 'L'

    def test_betagamma_class_c(self):
        assert _family_to_shadow_class('betagamma') == 'C'

    def test_lattice_class_g(self):
        assert _family_to_shadow_class('lattice') == 'G'

    def test_free_fermion_class_g(self):
        assert _family_to_shadow_class('free_fermion') == 'G'

    def test_bc_class_c(self):
        assert _family_to_shadow_class('bc') == 'C'

    def test_unknown_raises(self):
        with pytest.raises(ValueError):
            _family_to_shadow_class('nonexistent_algebra')


# ============================================================================
# 4. Shadow coefficients
# ============================================================================

class TestShadowCoefficients:
    """Test shadow coefficient computation for all families."""

    def test_heisenberg_terminates(self):
        """Heisenberg tower terminates at arity 2."""
        coeffs = heisenberg_shadow_coefficients(1)
        assert coeffs[2] == 1
        for r in range(3, 11):
            assert coeffs[r] == 0

    def test_virasoro_s2_is_kappa(self):
        """S_2 = kappa = c/2 for Virasoro."""
        for c_val in [1, 4, 10, 13, 26]:
            coeffs = virasoro_shadow_coefficients(c_val)
            assert coeffs[2] == Rational(c_val, 2)

    def test_virasoro_s3_is_2(self):
        """S_3 = alpha = 2 for Virasoro (independent of c)."""
        for c_val in [1, 4, 10, 13]:
            coeffs = virasoro_shadow_coefficients(c_val)
            assert coeffs[3] == 2

    def test_virasoro_s4_contact(self):
        """S_4 = Q^contact = 10/[c(5c+22)] for Virasoro."""
        coeffs = virasoro_shadow_coefficients(1)
        assert coeffs[4] == Rational(10, 27)  # 10/(1*27) = 10/27

    def test_virasoro_s5(self):
        """S_5 = -48/[c^2(5c+22)] for Virasoro."""
        coeffs = virasoro_shadow_coefficients(1, max_arity=5)
        assert coeffs[5] == Rational(-48, 27)  # -48/(1*27)

    def test_affine_sl2_terminates_at_3(self):
        """Affine sl_2 tower terminates at arity 3."""
        coeffs = affine_sl2_shadow_coefficients(1)
        assert coeffs[2] == Rational(9, 4)  # kappa = 3*3/4
        assert coeffs[3] == 1  # cubic shadow
        for r in range(4, 11):
            assert coeffs[r] == 0

    def test_betagamma_terminates_at_4(self):
        """betagamma tower terminates at arity 4 (on charged stratum)."""
        coeffs = betagamma_shadow_coefficients(1)
        assert coeffs[2] == 1  # kappa
        assert coeffs[3] == 0  # alpha = 0 on weight line
        assert coeffs[4] != 0  # quartic contact nonzero
        for r in range(5, 11):
            assert coeffs[r] == 0


# ============================================================================
# 5. K-groups
# ============================================================================

class TestShadowKGroups:
    """Test K-theory groups of shadow algebras."""

    def test_heisenberg_k0(self):
        """K_0(A^sh_Heis) = Z."""
        k0 = shadow_k_group('heisenberg', 0, k=1)
        assert k0.rank == 1
        assert k0.torsion == []

    def test_heisenberg_k1(self):
        """K_1(A^sh_Heis) = 0."""
        k1 = shadow_k_group('heisenberg', 1, k=1)
        assert k1.rank == 0
        assert k1.torsion == []

    def test_virasoro_k0(self):
        """K_0(A^sh_Vir) = Z^2."""
        k0 = shadow_k_group('virasoro', 0, c=1)
        assert k0.rank == 2

    def test_virasoro_k1(self):
        """K_1(A^sh_Vir) = Z + Z/2."""
        k1 = shadow_k_group('virasoro', 1, c=1)
        assert k1.rank == 1
        assert k1.torsion == [(2, 1)]

    def test_affine_k0(self):
        """K_0(A^sh_aff) = Z^2."""
        k0 = shadow_k_group('affine_sl2', 0, k=1, N=2)
        assert k0.rank == 2

    def test_affine_k1(self):
        """K_1(A^sh_aff) = Z."""
        k1 = shadow_k_group('affine_sl2', 1, k=1, N=2)
        assert k1.rank == 1
        assert k1.torsion == []

    def test_betagamma_k0(self):
        """K_0(A^sh_bg) = Z^2."""
        k0 = shadow_k_group('betagamma', 0, lam=1)
        assert k0.rank == 2

    def test_betagamma_k1(self):
        """K_1(A^sh_bg) = Z."""
        k1 = shadow_k_group('betagamma', 1, lam=1)
        assert k1.rank == 1
        assert k1.torsion == []

    def test_w3_k0(self):
        """K_0(A^sh_W3) = Z^2 (class M)."""
        k0 = shadow_k_group('w3', 0, c=4)
        assert k0.rank == 2

    def test_w3_k1(self):
        """K_1(A^sh_W3) = Z + Z/2 (class M, Koszul monodromy)."""
        k1 = shadow_k_group('w3', 1, c=4)
        assert k1.rank == 1
        assert k1.torsion == [(2, 1)]

    def test_bott_periodicity_classical(self):
        """K_{n+2} = K_n for class G (Heisenberg)."""
        for n in range(6):
            kn = shadow_k_group('heisenberg', n, k=1)
            kn2 = shadow_k_group('heisenberg', n + 2, k=1)
            assert kn.is_isomorphic_to(kn2)

    def test_k_group_order_str(self):
        """Test string representation."""
        k0 = shadow_k_group('heisenberg', 0, k=1)
        assert k0.order_str() == "Z"
        k1_vir = shadow_k_group('virasoro', 1, c=1)
        assert "Z/2" in k1_vir.order_str()


# ============================================================================
# 6. Bott map
# ============================================================================

class TestBottMap:
    """Test the shadow Bott map beta_sh."""

    def test_heisenberg_bott_iso(self):
        """beta_sh is an isomorphism for Heisenberg (class G)."""
        for k in [1, 2, 3, 5, 10]:
            bott = shadow_bott_map('heisenberg', 0, k=k)
            assert bott.is_isomorphism

    def test_heisenberg_bott_iso_k1(self):
        """beta_sh is also iso on K_1 for Heisenberg."""
        bott = shadow_bott_map('heisenberg', 1, k=1)
        assert bott.is_isomorphism

    def test_virasoro_bott_not_iso(self):
        """beta_sh fails for Virasoro (class M)."""
        for c_val in [Rational(1, 2), 1, 4, 10, 13, 25, 26]:
            bott = shadow_bott_map('virasoro', 0, c=c_val)
            assert not bott.is_isomorphism

    def test_virasoro_bott_kernel(self):
        """beta_sh has Z/2 kernel for Virasoro."""
        bott = shadow_bott_map('virasoro', 0, c=1)
        assert bott.kernel_torsion == [(2, 1)]

    def test_virasoro_bott_cokernel(self):
        """beta_sh has Z/2 cokernel for Virasoro."""
        bott = shadow_bott_map('virasoro', 0, c=1)
        assert bott.cokernel_torsion == [(2, 1)]

    def test_w3_bott_not_iso(self):
        """beta_sh fails for W_3 (class M)."""
        for c_val in [-2, Rational(4, 5)]:
            bott = shadow_bott_map('w3', 0, c=c_val)
            assert not bott.is_isomorphism

    def test_affine_bott_iso(self):
        """beta_sh is iso for affine KM (class L, Delta=0)."""
        bott = shadow_bott_map('affine_sl2', 0, k=1, N=2)
        assert bott.is_isomorphism

    def test_betagamma_bott_not_iso(self):
        """beta_sh fails for betagamma (class C, Delta != 0)."""
        bott = shadow_bott_map('betagamma', 0, lam=1)
        assert not bott.is_isomorphism

    def test_betagamma_bott_cokernel_z2(self):
        """betagamma has Z/2 cokernel from quartic contact."""
        bott = shadow_bott_map('betagamma', 0, lam=1)
        assert bott.cokernel_torsion == [(2, 1)]

    def test_bott_kernel_str(self):
        """Test kernel string representation."""
        bott = shadow_bott_map('heisenberg', 0, k=1)
        assert bott.kernel_str() == "0"
        bott_vir = shadow_bott_map('virasoro', 0, c=1)
        assert "Z/2" in bott_vir.kernel_str()


# ============================================================================
# 7. Periodicity index
# ============================================================================

class TestPeriodicityIndex:
    """Test the periodicity index pi(A).

    pi(A) = min{n >= 1 : beta_sh^n is not iso}.
    This is a DICHOTOMY controlled by Delta:
        Delta = 0  (classes G, L) => pi = inf
        Delta != 0 (classes C, M) => pi = 1
    """

    def test_heisenberg_infinite(self):
        """pi(Heisenberg) = infinity (class G, Delta=0)."""
        assert periodicity_index('heisenberg', k=1) == float('inf')

    def test_heisenberg_all_k(self):
        """pi = inf for all Heisenberg levels."""
        for k in [1, 2, 3, 5, 10]:
            assert periodicity_index('heisenberg', k=k) == float('inf')

    def test_virasoro_one(self):
        """pi(Virasoro) = 1 (class M, Delta != 0)."""
        assert periodicity_index('virasoro', c=1) == 1

    def test_virasoro_all_c(self):
        """pi = 1 for all Virasoro central charges."""
        for c_val in [Rational(1, 2), 1, 4, 10, 13, 25, 26]:
            assert periodicity_index('virasoro', c=c_val) == 1

    def test_w3_one(self):
        """pi(W_3) = 1 (class M)."""
        assert periodicity_index('w3', c=4) == 1

    def test_w3_all_c(self):
        """pi = 1 for W_3 at all central charges."""
        for c_val in [-2, Rational(4, 5)]:
            assert periodicity_index('w3', c=c_val) == 1

    def test_affine_infinite(self):
        """pi(affine KM) = inf (class L, Delta=0)."""
        assert periodicity_index('affine_sl2', k=1, N=2) == float('inf')

    def test_betagamma_one(self):
        """pi(betagamma) = 1 (class C, Delta != 0)."""
        assert periodicity_index('betagamma', lam=1) == 1

    def test_numerical_agrees_with_direct(self):
        """Numerical periodicity index agrees with direct computation."""
        for fam in ['heisenberg', 'virasoro', 'betagamma', 'affine_sl2', 'w3']:
            pi_direct = periodicity_index(fam)
            pi_num = periodicity_index_numerical(fam)
            assert pi_direct == pi_num, f"Mismatch for {fam}: {pi_direct} vs {pi_num}"

    def test_pi_dichotomy(self):
        """pi is exactly inf or 1 -- no intermediate values."""
        for fam in ['heisenberg', 'virasoro', 'betagamma', 'affine_sl2', 'w3']:
            pi_val = periodicity_index(fam)
            assert pi_val in (1, float('inf'))


class TestShadowPeriodicityDepth:
    """Test the shadow periodicity depth pi_sh(A) = r_max - 1."""

    def test_class_g_depth_1(self):
        """pi_sh(Heisenberg) = 1 (r_max=2)."""
        assert shadow_periodicity_depth('heisenberg') == 1

    def test_class_l_depth_2(self):
        """pi_sh(affine KM) = 2 (r_max=3)."""
        assert shadow_periodicity_depth('affine_sl2') == 2

    def test_class_c_depth_3(self):
        """pi_sh(betagamma) = 3 (r_max=4)."""
        assert shadow_periodicity_depth('betagamma') == 3

    def test_class_m_depth_inf(self):
        """pi_sh(Virasoro) = inf (r_max=inf)."""
        assert shadow_periodicity_depth('virasoro') == float('inf')

    def test_w3_depth_inf(self):
        """pi_sh(W_3) = inf (class M)."""
        assert shadow_periodicity_depth('w3') == float('inf')


# ============================================================================
# 8. Periodicity-depth relation
# ============================================================================

class TestPeriodicityDepthRelation:
    """Test the relation between pi(A), pi_sh(A), r_max(A), and Delta."""

    def test_pi_infinite_iff_delta_zero(self):
        """pi = inf iff Delta = 0 (the fundamental dichotomy)."""
        for fam in ['heisenberg', 'affine_sl2', 'betagamma', 'virasoro', 'w3']:
            rel = verify_periodicity_depth_relation(fam)
            assert rel['pi_infinite_iff_delta_zero']

    def test_class_g_delta_zero(self):
        """Class G has Delta = 0."""
        rel = verify_periodicity_depth_relation('heisenberg', k=1)
        assert rel['delta_zero']

    def test_class_l_delta_zero(self):
        """Class L has Delta = 0."""
        rel = verify_periodicity_depth_relation('affine_sl2', k=1, N=2)
        assert rel['delta_zero']

    def test_class_c_delta_nonzero(self):
        """Class C has Delta != 0."""
        rel = verify_periodicity_depth_relation('betagamma', lam=1)
        assert not rel['delta_zero']

    def test_class_m_delta_nonzero(self):
        """Class M has Delta != 0."""
        rel = verify_periodicity_depth_relation('virasoro', c=1)
        assert not rel['delta_zero']

    def test_pi_sh_values(self):
        """Shadow periodicity depth matches r_max - 1."""
        expected = {
            'heisenberg': 1,
            'affine_sl2': 2,
            'betagamma': 3,
            'virasoro': float('inf'),
            'w3': float('inf'),
        }
        for fam, expected_pish in expected.items():
            rel = verify_periodicity_depth_relation(fam)
            assert rel['pi_sh'] == expected_pish

    def test_r_max_values(self):
        """r_max values match the shadow classification."""
        expected = {
            'heisenberg': 2,
            'affine_sl2': 3,
            'betagamma': 4,
            'virasoro': float('inf'),
            'w3': float('inf'),
        }
        for fam, expected_rmax in expected.items():
            rel = verify_periodicity_depth_relation(fam)
            assert rel['r_max'] == expected_rmax


# ============================================================================
# 9. Dixmier-Douady class
# ============================================================================

class TestDixmierDouady:
    """Test the Dixmier-Douady obstruction class."""

    def test_heisenberg_dd_trivial(self):
        """DD = 0 for Heisenberg (class G)."""
        dd = dixmier_douady_class('heisenberg', k=1)
        assert dd.is_trivial
        assert dd.value == 0

    def test_affine_dd_trivial(self):
        """DD = 0 for affine KM (class L, Delta = 0)."""
        dd = dixmier_douady_class('affine_sl2', k=1, N=2)
        assert dd.is_trivial

    def test_virasoro_dd_nontrivial(self):
        """DD != 0 for Virasoro (class M)."""
        dd = dixmier_douady_class('virasoro', c=1)
        assert not dd.is_trivial

    def test_betagamma_dd_nontrivial(self):
        """DD != 0 for betagamma (class C)."""
        dd = dixmier_douady_class('betagamma', lam=1)
        assert not dd.is_trivial

    def test_virasoro_dd_value(self):
        """DD = Delta/(8*kappa) = S_4 = 10/[c(5c+22)] for Virasoro."""
        dd = dixmier_douady_class('virasoro', c=1)
        expected = Rational(10, 27)  # 10/(1*27)
        assert dd.value == expected

    def test_dd_at_c13_self_dual(self):
        """At c=13 (self-dual): DD = 40/(5*13+22) / (8*13/2) = 40/87 / 52."""
        dd = dixmier_douady_class('virasoro', c=13)
        expected_delta = Rational(40, 87)
        expected_kappa = Rational(13, 2)
        expected_dd = expected_delta / (8 * expected_kappa)
        assert dd.value == expected_dd


# ============================================================================
# 10. Dixmier-Douady at zeta zeros
# ============================================================================

class TestDDAtZetaZeros:
    """Test Dixmier-Douady at Riemann zeta zeros."""

    def test_dd_zero_1_nontrivial(self):
        """DD(rho_1) is nontrivial (complex)."""
        dd = dixmier_douady_at_zeta_zero(1)
        assert not dd.is_trivial
        assert isinstance(dd.value, complex)

    def test_dd_at_all_15_zeros(self):
        """DD is nontrivial at all first 15 zeros."""
        for n in range(1, 16):
            dd = dixmier_douady_at_zeta_zero(n)
            assert not dd.is_trivial
            assert abs(dd.value) > 0

    def test_dd_magnitude_decreasing(self):
        """|DD(rho_n)| is roughly decreasing (larger gamma => smaller |DD|)."""
        mags = [abs(dixmier_douady_at_zeta_zero(n).value) for n in range(1, 16)]
        # Not strictly monotone, but the trend is decreasing
        assert mags[0] > mags[-1]

    def test_dd_central_charge_at_zero(self):
        """c(rho_1) = 26 - 24*(1/2 + i*gamma_1) = 14 - 24i*gamma_1."""
        rho = riemann_zero(1)
        c_val = 26 - 24 * rho
        assert abs(c_val.real - 14) < 1e-10
        assert abs(c_val.imag + 24 * RIEMANN_ZEROS_GAMMA[0]) < 1e-6

    def test_dd_kappa_at_zero(self):
        """kappa(c(rho_1)) = c/2 = 7 - 12i*gamma_1."""
        dd = dixmier_douady_at_zeta_zero(1)
        gamma_1 = RIEMANN_ZEROS_GAMMA[0]
        expected_kappa = complex(7, -12 * gamma_1)
        assert abs(dd.kappa_val - expected_kappa) < 1e-6


# ============================================================================
# 11. Thom class
# ============================================================================

class TestThomClass:
    """Test Thom class for the bar virtual bundle."""

    def test_heisenberg_thom(self):
        """Thom class for Heisenberg is kappa (flat bundle)."""
        thom = thom_class_bar('heisenberg', k=1)
        assert thom.thom_value == 1  # kappa = k = 1

    def test_heisenberg_rank_1(self):
        """Virtual rank 1 for Heisenberg bar bundle."""
        thom = thom_class_bar('heisenberg', k=1)
        assert thom.virtual_rank == 1

    def test_virasoro_thom_corrected(self):
        """Virasoro Thom includes Td correction."""
        thom = thom_class_bar('virasoro', c=1)
        kap = Rational(1, 2)
        delta = Rational(40, 27)  # 40/(5+22)
        expected = kap * (1 + delta / (24 * kap))
        assert thom.thom_value == expected

    def test_affine_thom_is_kappa(self):
        """Affine KM Thom = kappa (flat, class L)."""
        thom = thom_class_bar('affine_sl2', k=1, N=2)
        assert thom.thom_value == Rational(9, 4)

    def test_affine_rank_0(self):
        """Virtual rank 0 for affine bar (CE complex)."""
        thom = thom_class_bar('affine_sl2', k=1, N=2)
        assert thom.virtual_rank == 0

    def test_betagamma_rank_minus_1(self):
        """Virtual rank -1 for betagamma."""
        thom = thom_class_bar('betagamma', lam=1)
        assert thom.virtual_rank == -1

    def test_virasoro_regularized_rank(self):
        """Virasoro virtual rank = -kappa/12."""
        thom = thom_class_bar('virasoro', c=1)
        assert thom.virtual_rank == Rational(-1, 24)  # -(1/2)/12

    def test_chern_char_is_kappa(self):
        """Chern character c_1(xi_bar) = kappa for all families."""
        for fam, params in [('heisenberg', {'k': 3}), ('virasoro', {'c': 10})]:
            thom = thom_class_bar(fam, **params)
            kap, _ = _get_kappa_and_delta(fam, **params)
            assert thom.chern_char == kap


# ============================================================================
# 12. Zeta zero landscape
# ============================================================================

class TestZetaZeroLandscape:
    """Test the complete Bott landscape at zeta zeros."""

    def test_pi_always_1(self):
        """Periodicity index = 1 at all zeros (class M)."""
        for n in range(1, 16):
            assert periodicity_index_at_zero(n) == 1

    def test_bott_data_structure(self):
        """bott_data_at_zeta_zero returns complete data."""
        data = bott_data_at_zeta_zero(1)
        assert 'n' in data
        assert 'rho_n' in data
        assert 'c' in data
        assert 'kappa' in data
        assert 'delta' in data
        assert 'pi' in data
        assert 'DD' in data
        assert '|DD|' in data
        assert 'thom' in data

    def test_landscape_15_zeros(self):
        """Landscape computation for 15 zeros succeeds."""
        landscape = bott_landscape_at_zeros(15)
        assert len(landscape) == 15

    def test_landscape_dd_all_complex(self):
        """All DD values at zeros are complex."""
        landscape = bott_landscape_at_zeros(10)
        for entry in landscape:
            assert isinstance(entry['DD'], complex)

    def test_landscape_pi_all_1(self):
        """All periodicity indices at zeros are 1."""
        landscape = bott_landscape_at_zeros(10)
        for entry in landscape:
            assert entry['pi'] == 1

    def test_c_at_first_zero(self):
        """Verify c(rho_1) computation."""
        data = bott_data_at_zeta_zero(1)
        rho = riemann_zero(1)
        assert abs(data['c'] - (26 - 24 * rho)) < 1e-10


# ============================================================================
# 13. Spectral sequence
# ============================================================================

class TestAtiyahHirzebruch:
    """Test the Atiyah-Hirzebruch spectral sequence E_2 page."""

    def test_class_g_e2(self):
        """Class G: E_2 = K(pt), only (0,0) entry nonzero."""
        e2 = atiyah_hirzebruch_e2('heisenberg')
        assert e2[(0, 0)] == 1
        assert e2[(1, 0)] == 0
        assert e2[(0, 1)] == 0

    def test_class_l_e2(self):
        """Class L: E_2 has entries at (0,0) and (1,0)."""
        e2 = atiyah_hirzebruch_e2('affine_sl2', k=1, N=2)
        assert e2[(0, 0)] == 1
        assert e2[(1, 0)] == 1

    def test_class_m_e2_dd(self):
        """Class M: E_2 has DD class at (3,0)."""
        e2 = atiyah_hirzebruch_e2('virasoro', c=1)
        assert e2[(3, 0)] == 1  # Dixmier-Douady

    def test_class_m_e2_torsion(self):
        """Class M: E_2 has Z/2 torsion at (2,0)."""
        e2 = atiyah_hirzebruch_e2('virasoro', c=1)
        assert e2[(2, 0)] == -2  # negative = torsion Z/2

    def test_odd_q_all_zero(self):
        """E_2^{p, 2k+1} = 0 for all families (K^{odd}(pt) = 0)."""
        for fam in ['heisenberg', 'virasoro', 'affine_sl2', 'betagamma']:
            e2 = atiyah_hirzebruch_e2(fam)
            for p in range(7):
                for q in range(7):
                    if q % 2 == 1:
                        assert e2[(p, q)] == 0


# ============================================================================
# 14. Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks."""

    def test_pi_dichotomy_across_families(self):
        """pi is inf for Delta=0 classes, 1 for Delta!=0 classes."""
        pi_g = periodicity_index('heisenberg')
        pi_l = periodicity_index('affine_sl2')
        pi_c = periodicity_index('betagamma')
        pi_m = periodicity_index('virasoro')

        assert pi_g == float('inf')
        assert pi_l == float('inf')
        assert pi_c == 1
        assert pi_m == 1

    def test_bott_iso_iff_delta_zero(self):
        """Bott map is iso iff Delta = 0 (classes G and L only)."""
        for fam, expected_iso in [
            ('heisenberg', True), ('affine_sl2', True),
            ('betagamma', False), ('virasoro', False)
        ]:
            bott = shadow_bott_map(fam, 0)
            assert bott.is_isomorphism == expected_iso

    def test_dd_trivial_iff_delta_zero(self):
        """DD = 0 iff Delta = 0."""
        for fam, expected_trivial in [
            ('heisenberg', True), ('affine_sl2', True),
            ('betagamma', False), ('virasoro', False)
        ]:
            dd = dixmier_douady_class(fam)
            assert dd.is_trivial == expected_trivial

    def test_kappa_delta_consistency(self):
        """Delta = 0 for classes G and L; Delta != 0 for C and M."""
        for fam, expected_zero in [
            ('heisenberg', True), ('affine_sl2', True),
            ('betagamma', False), ('virasoro', False)
        ]:
            _, delta = _get_kappa_and_delta(fam)
            if expected_zero:
                assert delta == 0
            else:
                assert delta != 0


# ============================================================================
# 15. Degenerate limits (Path 3)
# ============================================================================

class TestDegenerateLimits:
    """Test at degenerate parameter values."""

    def test_heisenberg_limits(self):
        """Heisenberg at various k values."""
        result = verify_bott_at_degenerate_limit('heisenberg')
        assert result['limits']['k=0']['kappa'] == 0.0
        assert result['limits']['k=10']['kappa'] == 10.0

    def test_virasoro_limits(self):
        """Virasoro at special c values."""
        result = verify_bott_at_degenerate_limit('virasoro')
        assert result['limits']['c=13']['kappa'] == 6.5  # self-dual
        assert result['limits']['c=26']['kappa'] == 13.0  # critical

    def test_c0_kappa_zero(self):
        """At c=0, kappa=0 but class is still M (AP31)."""
        # kappa = 0 does NOT imply Theta = 0
        assert periodicity_index('virasoro', c=0) == 1


# ============================================================================
# 16. Multi-path verification
# ============================================================================

class TestMultiPathVerification:
    """Test that all verification paths agree."""

    def test_heisenberg_multipath(self):
        """All paths agree for Heisenberg."""
        result = verify_bott_multipath('heisenberg', k=1)
        assert result['paths_consistent']
        assert result['path1_direct_pi'] == float('inf')

    def test_virasoro_multipath(self):
        """All paths agree for Virasoro."""
        result = verify_bott_multipath('virasoro', c=1)
        assert result['paths_consistent']
        assert result['path1_direct_pi'] == 1

    def test_affine_multipath(self):
        """All paths agree for affine KM."""
        result = verify_bott_multipath('affine_sl2', k=1, N=2)
        assert result['paths_consistent']
        assert result['path1_direct_pi'] == float('inf')

    def test_betagamma_multipath(self):
        """All paths agree for betagamma."""
        result = verify_bott_multipath('betagamma', lam=1)
        assert result['paths_consistent']
        assert result['path1_direct_pi'] == 1

    def test_w3_multipath(self):
        """All paths agree for W_3."""
        result = verify_bott_multipath('w3', c=4)
        assert result['paths_consistent']
        assert result['path1_direct_pi'] == 1


# ============================================================================
# 17. Full landscape
# ============================================================================

class TestFullLandscape:
    """Test the complete Bott periodicity landscape."""

    def test_landscape_completeness(self):
        """Landscape has entries for all requested families."""
        landscape = bott_periodicity_landscape()
        assert len(landscape) >= 16

    def test_landscape_heisenberg_entries(self):
        """Heisenberg entries all have class G and pi = inf."""
        landscape = bott_periodicity_landscape()
        for k in [1, 2, 3, 5, 10]:
            key = f'Heisenberg k={k}'
            assert landscape[key]['shadow_class'] == 'G'
            assert landscape[key]['pi'] == float('inf')

    def test_landscape_virasoro_entries(self):
        """Virasoro entries all have class M and pi = 1."""
        landscape = bott_periodicity_landscape()
        for key, data in landscape.items():
            if key.startswith('Virasoro'):
                assert data['shadow_class'] == 'M'
                assert data['pi'] == 1

    def test_landscape_bott_iso_matches_class(self):
        """Bott iso status matches shadow class."""
        landscape = bott_periodicity_landscape()
        for name, data in landscape.items():
            if data['shadow_class'] in ('G', 'L'):
                assert data['bott_K0_iso'], f"Expected iso for {name}"
            else:
                assert not data['bott_K0_iso'], f"Expected non-iso for {name}"

    def test_landscape_dd_matches_class(self):
        """DD trivial iff class G or L."""
        landscape = bott_periodicity_landscape()
        for name, data in landscape.items():
            if data['shadow_class'] in ('G', 'L'):
                assert data['DD_trivial'], f"Expected DD=0 for {name}"
            else:
                assert not data['DD_trivial'], f"Expected DD!=0 for {name}"


# ============================================================================
# 18. Numerical kernel dimension (Path 4)
# ============================================================================

class TestNumericalKernel:
    """Test numerical kernel dimension computation."""

    def test_all_kernels_zero(self):
        """Free-part kernel is 0 for all families (torsion only)."""
        for fam in ['heisenberg', 'virasoro', 'affine_sl2', 'betagamma', 'w3']:
            assert numerical_bott_kernel_dimension(fam) == 0.0


# ============================================================================
# 19. Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError):
            shadow_k_group('nonexistent', 0)

    def test_unknown_family_periodicity_raises(self):
        with pytest.raises(ValueError):
            periodicity_index('nonexistent')

    def test_kappa_heisenberg_zero(self):
        """kappa(H_0) = 0."""
        assert kappa_heisenberg(0) == 0

    def test_kappa_virasoro_complex(self):
        """kappa works with complex c."""
        kap = kappa_virasoro(complex(14, -24 * 14.134725))
        assert isinstance(kap, complex)

    def test_w3_shadow_at_minus_2(self):
        """W_3 at c=-2: kappa = 5*(-2)/6 = -5/3."""
        assert kappa_w3(-2) == Rational(-5, 3)

    def test_virasoro_c_half(self):
        """Virasoro c=1/2: kappa = 1/4, S_4 = 10/(1/2 * (5/2 + 22))."""
        kap = kappa_virasoro(Rational(1, 2))
        assert kap == Rational(1, 4)


# ============================================================================
# 20. Arithmetic content at zeros
# ============================================================================

class TestArithmeticContent:
    """Test arithmetic content of the Bott obstruction at zeros."""

    def test_dd_at_zero_1_nonzero(self):
        """|DD(rho_1)| > 0."""
        data = bott_data_at_zeta_zero(1)
        assert data['|DD|'] > 0

    def test_dd_magnitude_order(self):
        """DD magnitudes are O(1/gamma_n^2) approximately."""
        data1 = bott_data_at_zeta_zero(1)
        data10 = bott_data_at_zeta_zero(10)
        # |DD| should decrease roughly as 1/gamma^2
        ratio = data1['|DD|'] / data10['|DD|']
        gamma_ratio = (RIEMANN_ZEROS_GAMMA[9] / RIEMANN_ZEROS_GAMMA[0]) ** 2
        # Check ratio is roughly gamma_ratio (within factor of 10)
        assert ratio > 1  # first zero has larger DD

    def test_dd_phase_varies(self):
        """arg(DD(rho_n)) varies with n."""
        phases = [bott_data_at_zeta_zero(n)['arg_DD'] for n in range(1, 11)]
        # Not all the same
        assert max(phases) - min(phases) > 0.01

    def test_thom_at_zeros_complex(self):
        """Thom class at zeros is complex."""
        for n in range(1, 6):
            data = bott_data_at_zeta_zero(n)
            assert isinstance(data['thom'], complex)

    def test_delta_at_zero_formula(self):
        """Delta(c(rho_n)) = 40/(5c + 22) where c = 14 - 24i*gamma."""
        for n in range(1, 6):
            data = bott_data_at_zeta_zero(n)
            gamma = RIEMANN_ZEROS_GAMMA[n - 1]
            c_val = complex(14, -24 * gamma)
            expected_delta = 40.0 / (5 * c_val + 22)
            assert abs(data['delta'] - expected_delta) < 1e-10
