r"""Tests for the geometric Langlands shadow engine.

Verifies the dictionary between the shadow obstruction tower and the
geometric Langlands programme.  Eight independent verification paths:

    Path 1: Hitchin fiber dimensions from Lie theory
    Path 2: Oper monodromy = -Id (Koszul sign, thm:shadow-connection)
    Path 3: Conformal block ranks match Verlinde formula
    Path 4: kappa + kappa' = 13 for Virasoro, = 0 for KM (AP24)
    Path 5: Feigin-Frenkel center dimensions at critical level
    Path 6: Quantum parameter degenerations
    Path 7: S-duality exchanges A-brane and B-brane data
    Path 8: Weil-Petersson metric positivity

80+ tests covering:
    - Spectral curve construction and shadow coefficients
    - Hitchin fiber dimensions for all types
    - Shadow oper and connection coefficients
    - Oper monodromy is Koszul sign -1
    - Hecke eigenvalue computation
    - Conformal block ranks via Verlinde
    - Quantum parameter at critical and generic levels
    - Feigin-Frenkel center = oper jet space (the FF theorem)
    - A-brane / B-brane data from bar / cobar
    - S-duality from Koszul duality
    - Weil-Petersson metric positivity
    - Schmid orbit and boundary behavior
    - Full geometric Langlands dictionary
    - Affine specializations (sl_2 through sl_5)
    - Cross-verification: kappa complementarity (AP24)
    - Cross-verification: Verlinde at genus 1
    - Cross-verification: FF theorem for sl_2, sl_3
"""

from __future__ import annotations

import cmath
import math

import pytest

from compute.lib.bc_geometric_langlands_shadow_engine import (
    # Section 1: Spectral curve
    hitchin_spectral_curve,
    # Section 2: Fiber dimension
    hitchin_fiber_dimension,
    # Section 3: Shadow oper
    shadow_oper,
    # Section 4: Oper monodromy
    oper_monodromy,
    # Section 5: Hecke eigenvalue
    hecke_eigenvalue_at_point,
    # Section 6: Conformal block rank
    conformal_block_rank,
    # Section 7: Quantum parameter
    quantum_parameter,
    # Section 8: Feigin-Frenkel center
    feigin_frenkel_center_dim,
    # Section 9-10: Branes
    kapustin_witten_a_brane,
    kapustin_witten_b_brane,
    # Section 11: S-duality
    s_duality_from_koszul,
    s_duality_from_koszul_affine,
    # Section 12: WP metric
    weil_petersson_metric,
    # Section 13: Schmid orbit
    schmid_orbit,
    # Section 14: Full dictionary
    koszul_geometric_langlands,
    # Section 15: Affine
    affine_kappa,
    affine_c,
    affine_hitchin_fiber_dim,
    affine_oper_monodromy,
    affine_s_duality,
    # Section 16: Verlinde
    verlinde_sl_N,
    # Section 17: Cross-verification
    verify_kappa_complementarity_virasoro,
    verify_kappa_complementarity_affine,
    verify_verlinde_at_genus1,
    verify_ff_center_matches_opers,
    correspondence_table,
)


# =========================================================================
# Path 1: Hitchin spectral curve and fiber dimensions
# =========================================================================

class TestHitchinSpectralCurve:
    """Tests for the spectral curve from shadow data."""

    def test_virasoro_spectral_curve_basic(self):
        """Spectral curve for Virasoro at c = 25."""
        data = hitchin_spectral_curve(25.0)
        assert abs(data['kappa'] - 12.5) < 1e-12

    def test_spectral_curve_kappa_is_c_over_2(self):
        """kappa(Vir_c) = c/2 for all c."""
        for c in [1.0, 6.0, 13.0, 25.0, 26.0]:
            data = hitchin_spectral_curve(c)
            assert abs(data['kappa'] - c / 2.0) < 1e-12

    def test_spectral_curve_shadow_coefficients_s2(self):
        """S_2 = kappa = c/2 for Virasoro."""
        for c in [1.0, 10.0, 25.0]:
            data = hitchin_spectral_curve(c)
            # S_2 = a_0 / 2 = c / 2 = kappa
            assert abs(data['shadow_coeffs'][2] - c / 2.0) < 1e-10

    def test_spectral_curve_discriminant_type_virasoro(self):
        """Virasoro (class M) has irreducible discriminant (Delta != 0)."""
        data = hitchin_spectral_curve(25.0)
        assert data['discriminant_type'] == 'irreducible'

    def test_spectral_curve_c0_raises(self):
        """c = 0 is a pole of the shadow tower."""
        with pytest.raises(ValueError):
            hitchin_spectral_curve(0.0)

    def test_spectral_curve_c_minus_22_over_5_raises(self):
        """c = -22/5 is a pole of S_4."""
        with pytest.raises(ValueError):
            hitchin_spectral_curve(-22.0 / 5.0)

    def test_spectral_curve_q_coefficients(self):
        """Q_L coefficients: q0 = c^2, q1 = 12c, q2 = alpha."""
        c = 10.0
        data = hitchin_spectral_curve(c)
        q0, q1, q2 = data['Q_coeffs']
        assert abs(q0 - c ** 2) < 1e-10
        assert abs(q1 - 12.0 * c) < 1e-10
        alpha_expected = (180.0 * c + 872.0) / (5.0 * c + 22.0)
        assert abs(q2 - alpha_expected) < 1e-10


class TestHitchinFiberDimension:
    """Tests for Hitchin fiber dimensions."""

    def test_sl2_genus2(self):
        """dim h^{-1}(b) for SL_2 on genus-2 curve: (4-1)*(2-1) = 3."""
        assert hitchin_fiber_dimension(2, 2) == 3

    def test_sl2_genus3(self):
        """SL_2, genus 3: 3 * 2 = 6."""
        assert hitchin_fiber_dimension(3, 2) == 6

    def test_sl3_genus2(self):
        """SL_3, genus 2: (9-1)*(2-1) = 8."""
        assert hitchin_fiber_dimension(2, 3) == 8

    def test_sl4_genus2(self):
        """SL_4, genus 2: (16-1)*(2-1) = 15."""
        assert hitchin_fiber_dimension(2, 4) == 15

    def test_genus0(self):
        """Genus 0: fiber dimension is 0."""
        assert hitchin_fiber_dimension(0, 2) == 0

    def test_genus1(self):
        """Genus 1: fiber dimension is 0 for all ranks."""
        for N in [2, 3, 4, 5]:
            assert hitchin_fiber_dimension(1, N) == 0

    def test_sl5_genus3(self):
        """SL_5, genus 3: (25-1)*(3-1) = 48."""
        assert hitchin_fiber_dimension(3, 5) == 48

    def test_fiber_dim_equals_hitchin_base_dim(self):
        """Generic Hitchin fiber = Hitchin base dimension."""
        for N in [2, 3, 4]:
            for g in [2, 3]:
                dim_fiber = hitchin_fiber_dimension(g, N)
                dim_base = (N ** 2 - 1) * (g - 1)
                assert dim_fiber == dim_base


# =========================================================================
# Path 2: Oper monodromy = -Id (Koszul sign)
# =========================================================================

class TestOperMonodromy:
    """Tests that the oper monodromy is the Koszul sign -1."""

    def test_local_monodromy_is_minus_one(self):
        """Local monodromy around each singularity is -1."""
        for c in [1.0, 6.0, 13.0, 25.0, 50.0]:
            data = oper_monodromy(c)
            assert data['local_monodromy'] == -1

    def test_monodromy_is_minus_id(self):
        """The monodromy_is_minus_id flag is True."""
        data = oper_monodromy(25.0)
        assert data['monodromy_is_minus_id'] is True

    def test_residue_is_minus_half(self):
        """Residue of shadow connection at singularity is -1/2."""
        for c in [1.0, 10.0, 25.0]:
            data = oper_monodromy(c)
            assert abs(data['residue'] - (-0.5)) < 1e-14

    def test_global_monodromy_is_plus_one(self):
        """Global monodromy (product of local) is +1 = (-1)^2."""
        data = oper_monodromy(25.0)
        assert data['global_monodromy'] == 1

    def test_two_singularities(self):
        """Shadow connection has exactly two singularities (zeros of Q_L)."""
        data = oper_monodromy(25.0)
        assert len(data['singularities']) == 2

    def test_singularity_type_complex_for_virasoro(self):
        """For Virasoro, singularities are complex conjugate.

        alpha = (180c + 872)/(5c + 22) > 36 for all finite c > 0,
        so disc = 144 - 4*alpha < 0 always. This means Q_L(t) > 0
        for all real t (no real zeros), and the shadow connection
        is regular on the real line.
        """
        for c in [1.0, 10.0, 100.0, 1000.0]:
            data = oper_monodromy(c)
            assert data['singularity_type'] == 'complex_conjugate'

    def test_disc_negative_for_all_positive_c(self):
        """disc_reduced = 144 - 4*alpha < 0 for all c > 0 (Virasoro class M).

        This is because alpha(c) = (180c + 872)/(5c + 22) > 36 for all
        finite c > 0, and 4*36 = 144.
        """
        for c in [0.1, 1.0, 13.0, 100.0]:
            data = oper_monodromy(c)
            assert data['disc_reduced'] < 0

    def test_c0_raises(self):
        """c = 0 is degenerate."""
        with pytest.raises(ValueError):
            oper_monodromy(0.0)


class TestShadowOper:
    """Tests for the shadow oper construction."""

    def test_oper_at_t0(self):
        """Shadow oper at t = 0: connection coeff = -6/c."""
        c = 10.0
        data = shadow_oper(c, 0.0)
        # A(0) = -(6c) / (c^2) = -6/c
        expected = -6.0 / c
        assert abs(data['connection_coeff'] - expected) < 1e-12

    def test_flat_section_at_t0_is_one(self):
        """Flat section Phi(0) = sqrt(Q(0)/Q(0)) = 1."""
        data = shadow_oper(10.0, 0.0)
        assert abs(data['flat_section'] - 1.0) < 1e-12

    def test_q_value_at_t0(self):
        """Q_L(0) = c^2."""
        c = 7.0
        data = shadow_oper(c, 0.0)
        assert abs(data['Q_value'] - c ** 2) < 1e-10

    def test_q_prime_at_t0(self):
        """Q_L'(0) = 12c."""
        c = 7.0
        data = shadow_oper(c, 0.0)
        assert abs(data['Q_prime'] - 12.0 * c) < 1e-10

    def test_regularity_at_origin(self):
        """Shadow oper is regular at t = 0 for c != 0."""
        data = shadow_oper(10.0, 0.0)
        assert data['is_regular'] is True


# =========================================================================
# Path 3: Conformal block ranks match Verlinde
# =========================================================================

class TestConformalBlockRank:
    """Tests that conformal block ranks match Verlinde formula."""

    def test_virasoro_genus0(self):
        """Virasoro conformal blocks at genus 0: rank 1."""
        data = conformal_block_rank(25.0, 0)
        assert data['rank'] == 1

    def test_virasoro_genus1(self):
        """Virasoro conformal blocks at genus 1: rank 1."""
        data = conformal_block_rank(25.0, 1)
        assert data['rank'] == 1

    def test_virasoro_genus2(self):
        """Virasoro conformal blocks at genus 2: rank 1."""
        data = conformal_block_rank(25.0, 2)
        assert data['rank'] == 1

    def test_sl2_level1_genus0(self):
        """sl_2 at k=1 (c=1): genus 0 rank 1."""
        c = 3.0 * 1 / (1 + 2)  # = 1.0
        data = conformal_block_rank(c, 0)
        assert data['rank'] == 1

    def test_sl2_level1_genus1(self):
        """sl_2 at k=1 (c=1): genus 1 Verlinde = k+1 = 2."""
        c = 1.0  # c(sl_2, k=1) = 3*1/3 = 1
        data = conformal_block_rank(c, 1)
        assert data['rank'] == 2
        assert data['identified_level'] == 1

    def test_sl2_level2_genus1(self):
        """sl_2 at k=2 (c=3/2): genus 1 Verlinde = k+1 = 3."""
        c = 3.0 * 2 / (2 + 2)  # = 1.5
        data = conformal_block_rank(c, 1)
        assert data['rank'] == 3

    def test_sl2_level3_genus1(self):
        """sl_2 at k=3 (c=9/5): genus 1 = 4."""
        c = 3.0 * 3 / (3 + 2)  # = 1.8
        data = conformal_block_rank(c, 1)
        assert data['rank'] == 4

    def test_negative_genus_raises(self):
        """Negative genus raises ValueError."""
        with pytest.raises(ValueError):
            conformal_block_rank(25.0, -1)


class TestVerlinde:
    """Tests for the Verlinde formula for sl_N."""

    def test_verlinde_sl2_genus0(self):
        """V_0(sl_2, k) = 1 for all k."""
        for k in [1, 2, 3, 5]:
            assert verlinde_sl_N(2, k, 0) == 1

    def test_verlinde_sl2_genus1(self):
        """V_1(sl_2, k) = k + 1."""
        for k in [1, 2, 3, 4, 5]:
            assert verlinde_sl_N(2, k, 1) == k + 1

    def test_verlinde_sl3_genus1(self):
        """V_1(sl_3, k) = C(k+2, 2) = (k+1)(k+2)/2."""
        for k in [1, 2, 3]:
            expected = (k + 1) * (k + 2) // 2
            assert verlinde_sl_N(3, k, 1) == expected

    def test_verlinde_sl2_k1_genus2(self):
        """V_2(sl_2, 1) = 1 (known value)."""
        # Verlinde for sl_2, k=1, g=2:
        # S_{0,0} = sin(pi/3) = sqrt(3)/2
        # S_{0,1} = sin(2pi/3) = sqrt(3)/2
        # dim = (3/2) * (S_{0,0}^{-2} + S_{0,1}^{-2})
        #     = (3/2) * (4/3 + 4/3) = (3/2)(8/3) = 4
        # Actually, let me recalculate properly.
        # For k=1, kh=3: normalization = (3/2)^{g-1} = 3/2
        # S-matrix diagonal: sin(pi*1/3) = sqrt(3)/2, sin(pi*2/3) = sqrt(3)/2
        # Sum = 2 * (sqrt(3)/2)^{2-4} = 2 * (sqrt(3)/2)^{-2} = 2 * 4/3 = 8/3
        # Total = (3/2) * (8/3) = 4
        result = verlinde_sl_N(2, 1, 2)
        assert result == 4

    def test_verlinde_sl2_k2_genus2(self):
        """V_2(sl_2, 2) = 10 (known value).

        kh = 4. Normalization = 2.
        j=0: sin(pi/4) = sqrt(2)/2, (sqrt(2)/2)^{-2} = 2
        j=1: sin(pi/2) = 1, 1^{-2} = 1
        j=2: sin(3pi/4) = sqrt(2)/2, 2
        Sum = 2 + 1 + 2 = 5.  Total = 2 * 5 = 10.
        """
        assert verlinde_sl_N(2, 2, 2) == 10


# =========================================================================
# Path 4: kappa complementarity (AP24)
# =========================================================================

class TestKappaComplementarity:
    """Tests for kappa + kappa' = 13 (Virasoro) and = 0 (KM)."""

    def test_virasoro_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c in [0.5, 1.0, 6.0, 13.0, 25.0, 26.0]:
            result = verify_kappa_complementarity_virasoro(c)
            assert result['is_correct']
            assert abs(result['sum'] - 13.0) < 1e-12

    def test_virasoro_self_dual_at_c13(self):
        """At c = 13: kappa = kappa' = 13/2."""
        result = verify_kappa_complementarity_virasoro(13.0)
        assert abs(result['kappa'] - 6.5) < 1e-12
        assert abs(result['kappa_dual'] - 6.5) < 1e-12

    def test_affine_sl2_kappa_sum_is_zero(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0."""
        for k in [1.0, 2.0, 3.0, 5.0, 10.0]:
            result = verify_kappa_complementarity_affine(2, k)
            assert result['is_correct']
            assert abs(result['sum']) < 1e-12

    def test_affine_sl3_kappa_sum_is_zero(self):
        """kappa(sl_3, k) + kappa(sl_3, -k-6) = 0."""
        for k in [1.0, 3.0, 5.0]:
            result = verify_kappa_complementarity_affine(3, k)
            assert result['is_correct']

    def test_affine_sl4_kappa_sum_is_zero(self):
        """kappa(sl_4, k) + kappa(sl_4, -k-8) = 0."""
        result = verify_kappa_complementarity_affine(4, 2.0)
        assert result['is_correct']

    def test_affine_sl5_kappa_sum_is_zero(self):
        """kappa(sl_5, k) + kappa(sl_5, -k-10) = 0."""
        result = verify_kappa_complementarity_affine(5, 1.0)
        assert result['is_correct']

    def test_virasoro_not_zero(self):
        """kappa + kappa' for Virasoro is 13, NOT 0 (AP24 warning)."""
        result = verify_kappa_complementarity_virasoro(10.0)
        assert abs(result['sum']) > 12.0  # far from zero

    def test_kappa_dual_is_ff_involution_affine(self):
        """k_dual = -k - 2h^v (Feigin-Frenkel involution)."""
        result = verify_kappa_complementarity_affine(3, 5.0)
        assert abs(result['k_dual'] - (-5.0 - 6.0)) < 1e-12


# =========================================================================
# Path 5: Feigin-Frenkel center dimensions
# =========================================================================

class TestFeiginFrenkelCenter:
    """Tests for the FF center at critical level."""

    def test_sl2_dims_sequence(self):
        """dim Z_n(sl_2) = {1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12}."""
        data = feigin_frenkel_center_dim(2, 10)
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12]
        assert data['dims'] == expected

    def test_sl2_generating_weights(self):
        """sl_2 generators have weight 2 (one Casimir of degree 2)."""
        data = feigin_frenkel_center_dim(2)
        assert data['generating_weights'] == [2]

    def test_sl3_generating_weights(self):
        """sl_3 generators have weights 2 and 3."""
        data = feigin_frenkel_center_dim(3)
        assert data['generating_weights'] == [2, 3]

    def test_sl4_generating_weights(self):
        """sl_4 generators have weights 2, 3, 4."""
        data = feigin_frenkel_center_dim(4)
        assert data['generating_weights'] == [2, 3, 4]

    def test_ff_equals_opers_sl2(self):
        """FF theorem: dim Z_n = dim Op_n for sl_2."""
        result = verify_ff_center_matches_opers(2, 15)
        assert result['match']

    def test_ff_equals_opers_sl3(self):
        """FF theorem: dim Z_n = dim Op_n for sl_3."""
        result = verify_ff_center_matches_opers(3, 12)
        assert result['match']

    def test_ff_equals_opers_sl4(self):
        """FF theorem: dim Z_n = dim Op_n for sl_4."""
        result = verify_ff_center_matches_opers(4, 10)
        assert result['match']

    def test_sl2_dim_weight0(self):
        """dim Z_0 = 1 (vacuum)."""
        data = feigin_frenkel_center_dim(2)
        assert data['dims'][0] == 1

    def test_sl2_dim_weight1(self):
        """dim Z_1 = 0 (no parts >= 2 summing to 1)."""
        data = feigin_frenkel_center_dim(2)
        assert data['dims'][1] == 0

    def test_is_polynomial_algebra(self):
        """The FF center is a polynomial algebra."""
        data = feigin_frenkel_center_dim(2)
        assert data['is_polynomial']

    def test_rank_1_raises(self):
        """rank < 2 raises ValueError."""
        with pytest.raises(ValueError):
            feigin_frenkel_center_dim(1)

    def test_sl3_first_few_dims(self):
        """sl_3 center dimensions.

        sl_3 opers: d^3 + q_2(z)*d + q_3(z), with q_2 weight 2, q_3 weight 3.
        GF = prod_{s>=2} 1/(1-q^s)^{min(s-1,2)}.
        Dims: 1, 0, 1, 2, 3, 4, 8, 10, ...

        Weight 3 has 2 states: (q_2)_1 and (q_3)_0.
        """
        data = feigin_frenkel_center_dim(3, 7)
        dims = data['dims']
        assert dims[0] == 1
        assert dims[1] == 0
        assert dims[2] == 1
        assert dims[3] == 2  # (q_2)_1 and (q_3)_0
        assert dims[4] == 3  # (q_2)_0^2, (q_2)_2, (q_3)_1
        assert dims[5] == 4
        assert dims[6] == 8


# =========================================================================
# Path 6: Quantum parameter
# =========================================================================

class TestQuantumParameter:
    """Tests for the quantum parameter hbar = 1/(k + h^v)."""

    def test_sl2_level1(self):
        """sl_2 at k=1: hbar = 1/(1+2) = 1/3."""
        data = quantum_parameter(1.0, 2)
        assert abs(data['hbar'] - 1.0 / 3.0) < 1e-14

    def test_sl2_critical_level(self):
        """sl_2 at k=-2 (critical): hbar = infinity."""
        data = quantum_parameter(-2.0, 2)
        assert data['is_critical']
        assert data['hbar'] == float('inf')

    def test_sl3_level1(self):
        """sl_3 at k=1: hbar = 1/(1+3) = 1/4."""
        data = quantum_parameter(1.0, 3)
        assert abs(data['hbar'] - 0.25) < 1e-14

    def test_q_is_root_of_unity_at_integer_level(self):
        """At integer level: q = exp(pi i/(k+h^v)) is a root of unity."""
        data = quantum_parameter(1.0, 2)
        q = data['q']
        # q^6 = exp(6 * pi i / 3) = exp(2 pi i) = 1
        q6 = q ** 6
        assert abs(q6 - 1.0) < 1e-10

    def test_critical_q_is_none(self):
        """At critical level, q is None (degenerate)."""
        data = quantum_parameter(-2.0, 2)
        assert data['q'] is None

    def test_shifted_level(self):
        """Shifted level is k + h^v."""
        data = quantum_parameter(3.0, 2)
        assert abs(data['shifted_level'] - 5.0) < 1e-14

    def test_rationality_integer_level(self):
        """Integer level gives rational hbar."""
        data = quantum_parameter(1.0, 2)
        assert data['is_rational']

    def test_kappa_from_hbar(self):
        """kappa = dim(g) / (2 h^v hbar) for sl_2."""
        k = 3.0
        h_v = 2
        data = quantum_parameter(k, h_v)
        kappa = 3 * (k + h_v) / (2 * h_v)  # dim(sl_2) = 3
        kappa_from_hbar = 3 / (2 * h_v * data['hbar'])
        assert abs(kappa - kappa_from_hbar) < 1e-10


# =========================================================================
# Path 7: S-duality from Koszul duality
# =========================================================================

class TestSDualityKoszul:
    """Tests for S-duality from Koszul duality."""

    def test_virasoro_c_dual(self):
        """Vir_c^! = Vir_{26-c}."""
        data = s_duality_from_koszul(10.0)
        assert abs(data['c_dual'] - 16.0) < 1e-12

    def test_virasoro_self_dual_c13(self):
        """Self-dual at c = 13."""
        data = s_duality_from_koszul(13.0)
        assert data['is_self_dual']

    def test_virasoro_not_self_dual_c25(self):
        """Not self-dual at c = 25."""
        data = s_duality_from_koszul(25.0)
        assert not data['is_self_dual']

    def test_brane_exchange(self):
        """S-duality exchanges A-brane and B-brane types."""
        data = s_duality_from_koszul(10.0)
        assert data['A_brane']['brane_type'] == 'A'
        assert data['B_brane']['brane_type'] == 'B'
        assert data['exchanges_brane_types']

    def test_kappa_sum_virasoro(self):
        """kappa + kappa' = 13 (Virasoro, AP24)."""
        data = s_duality_from_koszul(10.0)
        assert abs(data['kappa_sum'] - 13.0) < 1e-12

    def test_affine_sl2_kappa_anti_symmetric(self):
        """Affine sl_2: kappa + kappa' = 0."""
        data = s_duality_from_koszul_affine(2, 3.0)
        assert data['is_anti_symmetric']
        assert abs(data['kappa_sum']) < 1e-12

    def test_affine_sl3_kappa_anti_symmetric(self):
        """Affine sl_3: kappa + kappa' = 0."""
        data = s_duality_from_koszul_affine(3, 2.0)
        assert data['is_anti_symmetric']

    def test_affine_ff_involution(self):
        """k_dual = -k - 2h^v for affine."""
        data = s_duality_from_koszul_affine(2, 3.0)
        assert abs(data['k_dual'] - (-3.0 - 4.0)) < 1e-12

    def test_self_dual_point_value(self):
        """Self-dual c = 13.0."""
        data = s_duality_from_koszul(13.0)
        assert abs(data['self_dual_c'] - 13.0) < 1e-12


class TestBranes:
    """Tests for A-brane and B-brane data."""

    def test_a_brane_coisotropic(self):
        """A-brane has coisotropic support."""
        data = kapustin_witten_a_brane(10.0)
        assert data['support_type'] == 'coisotropic'

    def test_b_brane_lagrangian(self):
        """B-brane has Lagrangian support."""
        data = kapustin_witten_b_brane(10.0)
        assert data['support_type'] == 'lagrangian'

    def test_a_brane_curvature(self):
        """A-brane curvature F = kappa * omega."""
        data = kapustin_witten_a_brane(10.0)
        assert abs(data['curvature_coefficient'] - 5.0) < 1e-12

    def test_a_brane_uncurved_at_c0(self):
        """A-brane uncurved when kappa = 0 (c = 0 limit)."""
        # Use small c instead of 0
        data = kapustin_witten_a_brane(1e-15)
        assert data['is_uncurved']

    def test_b_brane_monodromy_koszul(self):
        """B-brane flat bundle has Koszul monodromy -1."""
        data = kapustin_witten_b_brane(10.0)
        assert data['flat_bundle_monodromy'] == -1

    def test_b_brane_kappa_sum_13(self):
        """B-brane kappa_sum = kappa + kappa' = 13."""
        data = kapustin_witten_b_brane(10.0)
        assert abs(data['kappa_sum'] - 13.0) < 1e-12

    def test_b_brane_self_dual_c13(self):
        """B-brane recognizes self-duality at c = 13."""
        data = kapustin_witten_b_brane(13.0)
        assert data['is_self_dual']


# =========================================================================
# Path 8: Weil-Petersson metric positivity
# =========================================================================

class TestWeilPeterssonMetric:
    """Tests for the WP metric from Hodge variation."""

    def test_positive_for_positive_c(self):
        """WP metric is positive for c > 0 (unitary)."""
        for c in [1.0, 10.0, 25.0]:
            data = weil_petersson_metric(c)
            assert data['is_positive']

    def test_zamolodchikov_positive(self):
        """Zamolodchikov metric coefficient is positive for c > 0."""
        data = weil_petersson_metric(10.0)
        assert data['zamolodchikov'] > 0

    def test_kappa_in_wp(self):
        """WP data includes correct kappa."""
        data = weil_petersson_metric(10.0)
        assert abs(data['kappa'] - 5.0) < 1e-12

    def test_c0_raises(self):
        """c = 0 raises ValueError."""
        with pytest.raises(ValueError):
            weil_petersson_metric(0.0)

    def test_q0_is_c_squared(self):
        """Q_L(0) = c^2."""
        c = 7.0
        data = weil_petersson_metric(c)
        assert abs(data['Q_0'] - c ** 2) < 1e-10


# =========================================================================
# Additional: Schmid orbit tests
# =========================================================================

class TestSchmidOrbit:
    """Tests for the Schmid orbit / boundary behavior."""

    def test_monodromy_type_semisimple(self):
        """Shadow connection always has semisimple monodromy."""
        data = schmid_orbit(10.0)
        assert data['monodromy_type'] == 'semisimple'

    def test_local_monodromy_minus_one(self):
        """Local monodromy is -1."""
        data = schmid_orbit(25.0)
        assert data['local_monodromy'] == -1

    def test_residue_minus_half(self):
        """Residue is -1/2."""
        data = schmid_orbit(10.0)
        assert abs(data['residue'] - (-0.5)) < 1e-14

    def test_nilpotent_orbit_dim_zero(self):
        """Nilpotent orbit dimension is 0 for semisimple monodromy."""
        data = schmid_orbit(10.0)
        assert data['nilpotent_orbit_dim'] == 0

    def test_limiting_hodge_finite_order(self):
        """Limiting Hodge structure is of finite order."""
        data = schmid_orbit(10.0)
        assert data['limiting_hodge'] == 'finite_order'


# =========================================================================
# Full dictionary tests
# =========================================================================

class TestFullDictionary:
    """Tests for the full geometric Langlands dictionary."""

    def test_dictionary_keys(self):
        """Full dictionary has all expected keys."""
        data = koszul_geometric_langlands(10.0)
        expected_keys = [
            'c', 'kappa', 'kappa_dual', 'kappa_sum', 'is_self_dual',
            'spectral_curve', 'shadow_oper', 'monodromy',
            'hecke_eigenvalue_0', 'conformal_blocks',
            'a_brane', 'b_brane', 's_duality', 'weil_petersson',
            'schmid_orbit', 'depth_class', 'Delta',
            'shadow_metric_is_hitchin_disc', 'monodromy_is_koszul_sign',
            'brane_exchange_is_koszul_duality',
        ]
        for key in expected_keys:
            assert key in data, f"Missing key: {key}"

    def test_consistency_kappa(self):
        """kappa is consistent across all sub-dictionaries."""
        c = 10.0
        data = koszul_geometric_langlands(c)
        kappa = c / 2.0
        assert abs(data['kappa'] - kappa) < 1e-12
        assert abs(data['a_brane']['kappa'] - kappa) < 1e-12
        assert abs(data['weil_petersson']['kappa'] - kappa) < 1e-12

    def test_kappa_sum_13(self):
        """kappa + kappa' = 13 in full dictionary."""
        data = koszul_geometric_langlands(10.0)
        assert abs(data['kappa_sum'] - 13.0) < 1e-12

    def test_monodromy_koszul_sign(self):
        """Monodromy is Koszul sign in full dictionary."""
        data = koszul_geometric_langlands(10.0)
        assert data['monodromy_is_koszul_sign']

    def test_brane_exchange(self):
        """Brane exchange is Koszul duality."""
        data = koszul_geometric_langlands(10.0)
        assert data['brane_exchange_is_koszul_duality']

    def test_depth_class_M_for_virasoro(self):
        """Virasoro at generic c is class M (infinite depth)."""
        data = koszul_geometric_langlands(10.0)
        assert data['depth_class'] == 'M'

    def test_self_dual_at_c13(self):
        """Self-dual at c = 13."""
        data = koszul_geometric_langlands(13.0)
        assert data['is_self_dual']


# =========================================================================
# Affine specialization tests
# =========================================================================

class TestAffineSpecializations:
    """Tests for affine KM specializations."""

    def test_affine_kappa_sl2_level1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        kap = affine_kappa(2, 1.0)
        assert abs(kap - 9.0 / 4.0) < 1e-12

    def test_affine_kappa_sl3_level1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        kap = affine_kappa(3, 1.0)
        assert abs(kap - 16.0 / 3.0) < 1e-12

    def test_affine_c_sl2_level1(self):
        """c(sl_2, k=1) = 1*3/3 = 1."""
        c = affine_c(2, 1.0)
        assert abs(c - 1.0) < 1e-12

    def test_affine_c_sl2_level2(self):
        """c(sl_2, k=2) = 2*3/4 = 3/2."""
        c = affine_c(2, 2.0)
        assert abs(c - 1.5) < 1e-12

    def test_affine_c_critical_raises(self):
        """Critical level k=-h^v raises ValueError."""
        with pytest.raises(ValueError):
            affine_c(2, -2.0)

    def test_affine_fiber_dim_sl2_g2(self):
        """Hitchin fiber for SL_2, genus 2: 3."""
        assert affine_hitchin_fiber_dim(2, 2) == 3

    def test_affine_fiber_dim_sl3_g2(self):
        """Hitchin fiber for SL_3, genus 2: 8."""
        assert affine_hitchin_fiber_dim(3, 2) == 8

    def test_affine_oper_monodromy_koszul(self):
        """Affine shadow monodromy is Koszul sign -1."""
        data = affine_oper_monodromy(2, 1.0)
        assert data['shadow_monodromy'] == -1

    def test_affine_oper_critical(self):
        """Affine at critical level is flagged."""
        data = affine_oper_monodromy(2, -2.0)
        assert data['is_critical']

    def test_affine_kz_phase_sl2_level1(self):
        """KZ phase for sl_2 at k=1: 2pi/3."""
        data = affine_oper_monodromy(2, 1.0)
        assert abs(data['kz_phase'] - 2.0 * math.pi / 3.0) < 1e-12


# =========================================================================
# Hecke eigenvalue tests
# =========================================================================

class TestHeckeEigenvalue:
    """Tests for Hecke eigenvalues from the shadow."""

    def test_eigenvalue_at_origin(self):
        """Hecke eigenvalue at x=0 is 1 (identity)."""
        data = hecke_eigenvalue_at_point(10.0, 0.0)
        assert abs(data['eigenvalue'] - 1.0) < 1e-12

    def test_q_ratio_at_origin(self):
        """Q ratio at x=0 is 1."""
        data = hecke_eigenvalue_at_point(10.0, 0.0)
        assert abs(data['Q_ratio'] - 1.0) < 1e-12

    def test_eigenvalue_positive_for_small_x(self):
        """Eigenvalue is real and positive for small positive x."""
        data = hecke_eigenvalue_at_point(10.0, 0.01)
        assert isinstance(data['eigenvalue'], float)
        assert data['eigenvalue'] > 0

    def test_q0_is_c_squared(self):
        """Q(0) = c^2."""
        c = 7.0
        data = hecke_eigenvalue_at_point(c, 0.0)
        assert abs(data['Q_0'] - c ** 2) < 1e-10


# =========================================================================
# Verlinde cross-checks
# =========================================================================

class TestVerlindeCrossChecks:
    """Cross-verification of Verlinde formula at genus 1."""

    def test_verlinde_genus1_sl2(self):
        """Verlinde at genus 1 for sl_2 matches C(k+1, 1)."""
        for k in [1, 2, 3, 5, 8]:
            result = verify_verlinde_at_genus1(2, k)
            assert result['is_correct']

    def test_verlinde_genus1_sl3(self):
        """Verlinde at genus 1 for sl_3 matches C(k+2, 2)."""
        for k in [1, 2, 3]:
            result = verify_verlinde_at_genus1(3, k)
            assert result['is_correct']

    def test_verlinde_genus1_sl4(self):
        """Verlinde at genus 1 for sl_4 matches C(k+3, 3)."""
        for k in [1, 2]:
            result = verify_verlinde_at_genus1(4, k)
            assert result['is_correct']


# =========================================================================
# Correspondence table tests
# =========================================================================

class TestCorrespondenceTable:
    """Tests for the shadow-to-GL correspondence table."""

    def test_table_has_entries(self):
        """Table is non-empty."""
        table = correspondence_table()
        assert len(table) >= 15

    def test_key_entries_present(self):
        """Key correspondence entries are present."""
        table = correspondence_table()
        assert 'shadow_metric_Q_L' in table
        assert 'kappa' in table
        assert 'Koszul_sign_-1' in table
        assert 'bar_complex_B(A)' in table

    def test_monodromy_maps_to_oper(self):
        """Koszul sign maps to oper monodromy."""
        table = correspondence_table()
        assert table['Koszul_sign_-1'] == 'oper_monodromy'

    def test_bar_maps_to_a_brane(self):
        """Bar complex maps to A-brane."""
        table = correspondence_table()
        assert table['bar_complex_B(A)'] == 'A_brane_coisotropic'

    def test_koszul_dual_maps_to_b_brane(self):
        """Koszul dual maps to B-brane."""
        table = correspondence_table()
        assert table['Koszul_dual_A!'] == 'B_brane_Lagrangian'


# =========================================================================
# Numerical cross-checks
# =========================================================================

class TestNumericalCrossChecks:
    """Numerical cross-checks across multiple verification paths."""

    def test_spectral_and_oper_agree_on_q(self):
        """Spectral curve Q coefficients match shadow oper Q values."""
        c = 10.0
        spectral = hitchin_spectral_curve(c)
        oper = shadow_oper(c, 0.0)
        assert abs(spectral['Q_coeffs'][0] - oper['Q_value']) < 1e-10

    def test_monodromy_consistent_with_schmid(self):
        """Oper monodromy and Schmid orbit agree on local monodromy."""
        c = 10.0
        mon = oper_monodromy(c)
        sch = schmid_orbit(c)
        assert mon['local_monodromy'] == sch['local_monodromy']

    def test_kappa_consistent_across_modules(self):
        """kappa is the same in spectral curve, oper, WP, branes."""
        c = 15.0
        kappa = c / 2.0
        assert abs(hitchin_spectral_curve(c)['kappa'] - kappa) < 1e-12
        assert abs(kapustin_witten_a_brane(c)['kappa'] - kappa) < 1e-12
        assert abs(weil_petersson_metric(c)['kappa'] - kappa) < 1e-12
        assert abs(schmid_orbit(c)['kappa'] - kappa) < 1e-12

    def test_residue_consistent(self):
        """Residue -1/2 is consistent across oper_monodromy and schmid_orbit."""
        c = 10.0
        assert abs(oper_monodromy(c)['residue'] - (-0.5)) < 1e-14
        assert abs(schmid_orbit(c)['residue'] - (-0.5)) < 1e-14

    def test_verlinde_monotone_in_level(self):
        """Verlinde dimension is non-decreasing in level at fixed genus."""
        prev = 0
        for k in [1, 2, 3, 4, 5]:
            v = verlinde_sl_N(2, k, 2)
            assert v >= prev
            prev = v

    def test_ff_center_monotone(self):
        """FF center dimensions are non-decreasing in weight."""
        data = feigin_frenkel_center_dim(2, 20)
        dims = data['dims']
        for n in range(2, len(dims)):
            assert dims[n] >= dims[n - 2], \
                f"dim Z_{n} = {dims[n]} < dim Z_{n-2} = {dims[n-2]}"

    def test_flat_section_normalized(self):
        """Flat section at t=0 is normalized to 1."""
        for c in [1.0, 5.0, 13.0, 25.0]:
            data = shadow_oper(c, 0.0)
            assert abs(data['flat_section'] - 1.0) < 1e-12

    def test_full_dictionary_c1(self):
        """Full dictionary at c=1 does not crash."""
        data = koszul_geometric_langlands(1.0)
        assert data['kappa'] == 0.5

    def test_full_dictionary_c13(self):
        """Full dictionary at self-dual c=13."""
        data = koszul_geometric_langlands(13.0)
        assert data['is_self_dual']
        assert abs(data['kappa'] - 6.5) < 1e-12
        assert abs(data['kappa_dual'] - 6.5) < 1e-12

    def test_full_dictionary_c25(self):
        """Full dictionary at c=25."""
        data = koszul_geometric_langlands(25.0)
        assert abs(data['kappa'] - 12.5) < 1e-12
        assert abs(data['kappa_dual'] - 0.5) < 1e-12
