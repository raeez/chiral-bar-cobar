r"""Tests for non-principal W-algebra data: partition (3,2) in sl_5.

39 tests organized into 10 sections:

  I.    Orbit combinatorics (5 tests)
  II.   Generator spectrum (4 tests)
  III.  Central charge formulas (4 tests)
  IV.   Kappa and anomaly ratio (4 tests)
  V.    Koszul conductor and complementarity (4 tests)
  VI.   Nilradical structure (3 tests)
  VII.  OPE pole structure (3 tests)
  VIII. Shadow depth classification (3 tests)
  IX.   Hook comparison and obstruction analysis (5 tests)
  X.    Seven-face programme and DS-KD diagram (4 tests)

Multi-path verification:
  Path 1: direct computation from partition combinatorics
  Path 2: cross-check with existing engines (hook_type_w_duality, nonprincipal_ds_orbits)
  Path 3: numerical evaluation at specific levels
  Path 4: cross-family consistency (comparison with hook partitions in sl_5)
  Path 5: independent recomputation from KRW formula
"""

import pytest
from sympy import Rational, Symbol, factor, oo, simplify

from compute.lib.theorem_nonprincipal_sl5_32_engine import (
    # Orbit data
    orbit_data_sl5_32,
    orbit_data_sl5_221,
    # Generator spectrum
    generator_spectrum_32,
    generator_spectrum_221,
    # Central charge
    central_charge_32,
    central_charge_221,
    # Kappa
    kappa_32,
    kappa_221,
    # Conductor
    koszul_conductor_32,
    kappa_sum_32,
    conductor_k_dependence_check,
    # Nilradical
    nilradical_data_32,
    nilradical_data_221,
    # OPE poles
    ope_pole_data_32,
    ope_pole_data_221,
    # Shadow depth
    shadow_depth_32,
    shadow_depth_221,
    # Comparison
    sl5_hook_comparison_table,
    # Obstruction
    hook_transport_obstruction_32,
    # Seven faces
    seven_face_status_32,
    seven_face_status_221,
    # DS-KD diagram
    ds_kd_diagram_32,
    ds_kd_diagram_221,
    # Numerical
    numerical_data_32,
    # Constants
    PARTITION_32,
    PARTITION_221,
)

# Also import from canonical engines for cross-checking (Path 2).
from compute.lib.nonprincipal_ds_orbits import (
    centralizer_dimension_sl_n,
    is_hook_partition,
    transpose_partition,
    type_a_orbit_class,
)
from compute.lib.hook_type_w_duality import (
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    krw_central_charge,
    krw_central_charge_data,
    w_algebra_generator_data,
)

k = Symbol('k')


# ===================================================================
# I. Orbit combinatorics
# ===================================================================

class TestOrbitCombinatorics:
    """Orbit data for (3,2) and (2,2,1) in sl_5."""

    def test_partition_32_is_not_hook(self):
        """(3,2) is NOT a hook partition: both parts >= 2."""
        data = orbit_data_sl5_32()
        assert data.is_hook is False
        # Cross-check with canonical engine (Path 2)
        assert is_hook_partition((3, 2)) is False

    def test_partition_221_is_not_hook(self):
        """(2,2,1) = (3,2)^t is also NOT hook: two parts >= 2."""
        data = orbit_data_sl5_221()
        assert data.is_hook is False
        assert is_hook_partition((2, 2, 1)) is False

    def test_transpose_pair(self):
        """(3,2)^t = (2,2,1) and vice versa."""
        assert transpose_partition((3, 2)) == (2, 2, 1)
        assert transpose_partition((2, 2, 1)) == (3, 2)

    def test_centralizer_dimensions(self):
        """dim(g^f) for (3,2) and (2,2,1).

        Path 1: direct formula dim(g^f) = sum_i (lambda_t_i)^2 - 1.
        Path 2: from orbit_data function.
        """
        # Path 1: direct computation
        # (3,2)^t = (2,2,1): sum = 4 + 4 + 1 - 1 = 8
        assert centralizer_dimension_sl_n((3, 2)) == 8
        # (2,2,1)^t = (3,2): sum = 9 + 4 - 1 = 12
        assert centralizer_dimension_sl_n((2, 2, 1)) == 12
        # Path 2: from engine
        assert orbit_data_sl5_32().centralizer_dim == 8
        assert orbit_data_sl5_221().centralizer_dim == 12

    def test_orbit_dimensions(self):
        """dim(orbit) = N^2 - 1 - dim(g^f).

        (3,2): 24 - 8 = 16.
        (2,2,1): 24 - 12 = 12.
        """
        assert orbit_data_sl5_32().orbit_dim == 16
        assert orbit_data_sl5_221().orbit_dim == 12


# ===================================================================
# II. Generator spectrum
# ===================================================================

class TestGeneratorSpectrum:
    """Strong generators of W^k(sl_5, f_{(3,2)}) and its transpose."""

    def test_32_generator_count(self):
        """W^k(sl_5, f_{(3,2)}) has 8 strong generators: 4 bos + 4 ferm."""
        spec = generator_spectrum_32()
        assert len(spec.generators) == 8
        assert spec.num_bosonic == 4
        assert spec.num_fermionic == 4

    def test_32_conformal_weights(self):
        """Generator weights: h = 1, 3/2 (x2), 2 (x2), 5/2 (x2), 3.

        Path 1: from engine.
        Path 2: cross-check with hook_type_w_duality canonical engine.
        """
        spec = generator_spectrum_32()
        expected = {
            Rational(1): 1,
            Rational(3, 2): 2,
            Rational(2): 2,
            Rational(5, 2): 2,
            Rational(3): 1,
        }
        assert spec.weight_multiplicities == expected
        # Path 2: verify via canonical engine
        gen_data = w_algebra_generator_data((3, 2))
        weights = {}
        for _, w, _ in gen_data.strong_generators:
            weights[w] = weights.get(w, 0) + 1
        assert weights == expected

    def test_221_generator_count(self):
        """W^k(sl_5, f_{(2,2,1)}) has 12 strong generators: 8 bos + 4 ferm."""
        spec = generator_spectrum_221()
        assert len(spec.generators) == 12
        assert spec.num_bosonic == 8
        assert spec.num_fermionic == 4

    def test_221_conformal_weights(self):
        """Generator weights for (2,2,1): h = 1 (x4), 3/2 (x4), 2 (x4)."""
        spec = generator_spectrum_221()
        expected = {
            Rational(1): 4,
            Rational(3, 2): 4,
            Rational(2): 4,
        }
        assert spec.weight_multiplicities == expected


# ===================================================================
# III. Central charge formulas
# ===================================================================

class TestCentralCharge:
    """KRW central charge for (3,2) and (2,2,1)."""

    def test_32_central_charge_formula(self):
        """c(3,2; k) = 2(k - 49)/(k + 5).

        Path 1: from engine.
        Path 2: direct KRW: leading = 4 - 2 = 2, quad = 108.
            c = 2 - 108/(k+5) = (2(k+5) - 108)/(k+5) = (2k - 98)/(k+5).
        """
        c = central_charge_32()
        expected = 2 * (k - 49) / (k + 5)
        assert simplify(c - expected) == 0
        # Path 2: verify the leading and quadratic terms
        data = krw_central_charge_data((3, 2))
        assert data.leading_term == 2
        assert data.quadratic_coeff == 108

    def test_221_central_charge_formula(self):
        """c(2,2,1; k) = 6(k - 10)/(k + 5).

        Leading = 8 - 2 = 6, quad = 90.
        c = 6 - 90/(k+5) = (6k + 30 - 90)/(k+5) = 6(k - 10)/(k+5).
        """
        c = central_charge_221()
        expected = 6 * (k - 10) / (k + 5)
        assert simplify(c - expected) == 0
        data = krw_central_charge_data((2, 2, 1))
        assert data.leading_term == 6
        assert data.quadratic_coeff == 90

    def test_32_central_charge_at_zero(self):
        """c(3,2; 0) = -98/5.

        Path 3: numerical evaluation.
        """
        assert simplify(central_charge_32(0) - Rational(-98, 5)) == 0

    def test_central_charge_vanishing_levels(self):
        """c(3,2; k) vanishes at k=49. c(2,2,1; k) vanishes at k=10."""
        assert simplify(central_charge_32(49)) == 0
        assert simplify(central_charge_221(10)) == 0


# ===================================================================
# IV. Kappa and anomaly ratio
# ===================================================================

class TestKappaAndAnomalyRatio:
    """Modular characteristic and anomaly ratio."""

    def test_32_anomaly_ratio(self):
        """rho_{(3,2)} = 1/5.

        Path 1: from engine.
        Path 2: explicit sum: 1/1 - 2*(2/3) + 2*(1/2) - 2*(2/5) + 1/3
                              = 1 - 4/3 + 1 - 4/5 + 1/3
                              = (15 - 20 + 15 - 12 + 5)/15 = 3/15 = 1/5.
        """
        spec = generator_spectrum_32()
        assert spec.anomaly_ratio == Rational(1, 5)
        # Path 2: recompute from first principles
        rho = (Rational(1) - 2 * Rational(2, 3) + 2 * Rational(1, 2)
               - 2 * Rational(2, 5) + Rational(1, 3))
        assert rho == Rational(1, 5)
        # Path 2b: canonical engine cross-check
        assert anomaly_ratio_from_partition((3, 2)) == Rational(1, 5)

    def test_221_anomaly_ratio(self):
        """rho_{(2,2,1)} = 10/3.

        Explicit: 4/1 - 4*(2/3) + 4/2 = 4 - 8/3 + 2 = (12 - 8 + 6)/3 = 10/3.
        """
        spec = generator_spectrum_221()
        assert spec.anomaly_ratio == Rational(10, 3)
        rho = 4 * Rational(1) - 4 * Rational(2, 3) + 4 * Rational(1, 2)
        assert rho == Rational(10, 3)

    def test_32_kappa_formula(self):
        """kappa(3,2; k) = 2(k-49)/(5(k+5)).

        kappa = rho * c = (1/5) * 2(k-49)/(k+5).
        """
        kap = kappa_32()
        expected = 2 * (k - 49) / (5 * (k + 5))
        assert simplify(kap - expected) == 0

    def test_32_kappa_at_zero(self):
        """kappa(3,2; 0) = 2*(-49)/(5*5) = -98/25.

        Path 3: numerical evaluation.
        """
        assert simplify(kappa_32(0) - Rational(-98, 25)) == 0


# ===================================================================
# V. Koszul conductor and complementarity
# ===================================================================

class TestConductorAndComplementarity:
    """Koszul conductor and kappa complementarity for the (3,2)/(2,2,1) pair."""

    def test_conductor_formula(self):
        """K(k) = c(3,2;k) + c(2,2,1;-k-10) = 2(4k+11)/(k+5).

        Path 1: from engine.
        Path 5: independent recomputation.
        """
        K = koszul_conductor_32()
        expected = 2 * (4 * k + 11) / (k + 5)
        assert simplify(K - expected) == 0
        # Path 5: recompute independently
        c1 = 2 * (k - 49) / (k + 5)
        # At dual level k' = -k - 10:
        # c(2,2,1; -k-10) = 6(-k - 10 - 10)/(-k - 10 + 5)
        #                  = 6(-k - 20)/(-k - 5)
        #                  = 6(k + 20)/(k + 5)
        c2 = 6 * (k + 20) / (k + 5)
        K_check = simplify(c1 + c2)
        assert simplify(K_check - expected) == 0

    def test_conductor_is_k_dependent(self):
        """The conductor for (3,2)/(2,2,1) is k-DEPENDENT.

        This is a NEW phenomenon for non-self-transpose non-hook partitions.
        Verify by evaluating at k=0 and k=1.
        """
        K0, K1, are_different = conductor_k_dependence_check()
        assert are_different is True
        # K(0) = 2*11/5 = 22/5
        assert simplify(K0 - Rational(22, 5)) == 0
        # K(1) = 2*15/6 = 5
        assert simplify(K1 - 5) == 0

    def test_kappa_sum_k_dependent(self):
        """kappa(3,2;k) + kappa(2,2,1;-k-10) is k-dependent.

        This follows from rho_{(3,2)} != rho_{(2,2,1)}.
        """
        ks = kappa_sum_32()
        # Evaluate at k=0 and k=1
        ks0 = simplify(ks.subs(k, 0))
        ks1 = simplify(ks.subs(k, 1))
        assert simplify(ks0 - ks1) != 0

    def test_self_transpose_conductor_k_independent(self):
        """Cross-family check: (3,1,1) = (3,1,1)^t is self-transpose.

        For self-transpose partitions, the conductor IS k-independent.
        Path 4: cross-family consistency.
        """
        lam = (3, 1, 1)
        c_k = krw_central_charge(lam, k)
        c_kp = krw_central_charge(lam, -k - 10)
        K = simplify(c_k + c_kp)
        # Should be constant: check derivative is zero
        assert simplify(K.diff(k)) == 0
        # Value: K = 20
        assert simplify(K - 20) == 0


# ===================================================================
# VI. Nilradical structure
# ===================================================================

class TestNilradicalStructure:
    """Nilradical m+ in the DS grading."""

    def test_32_nilradical_non_abelian(self):
        """m+ for (3,2) is non-abelian (dim = 10).

        This is NOT what distinguishes (3,2) from hook partitions:
        hook partitions in sl_5 also have non-abelian nilradicals.
        The distinction is combinatorial (not hook-shaped).
        """
        data = nilradical_data_32()
        assert data.dim_m_plus == 10
        assert data.is_abelian is False
        assert data.sample_bracket is not None

    def test_221_nilradical_non_abelian(self):
        """m+ for (2,2,1) is also non-abelian."""
        data = nilradical_data_221()
        assert data.is_abelian is False

    def test_32_nilradical_grade_structure(self):
        """m+ for (3,2) has grades 1/2, 1, 3/2, 2 under ad(h/2).

        Grade 1/2: dim 4 (E_14, E_25, E_42, E_53)
        Grade 1:   dim 3 (E_12, E_23, E_45)
        Grade 3/2: dim 2 (E_15, E_43)
        Grade 2:   dim 1 (E_13)
        Total: 10.
        """
        data = nilradical_data_32()
        assert data.grade_dims[Rational(1, 2)] == 4
        assert data.grade_dims[Rational(1)] == 3
        assert data.grade_dims[Rational(3, 2)] == 2
        assert data.grade_dims[Rational(2)] == 1
        assert sum(data.grade_dims.values()) == 10


# ===================================================================
# VII. OPE pole structure
# ===================================================================

class TestOPEPoleStructure:
    """OPE pole orders and r-matrix pole orders (AP19)."""

    def test_32_max_ope_pole(self):
        """Max OPE pole for (3,2): 6 (from h=3 self-OPE: W_3 * W_3).

        By conformal weight addition: max pole in a(z)b(w) is h_a + h_b.
        For the h=3 bosonic generator: max pole = 3 + 3 = 6.
        """
        data = ope_pole_data_32()
        assert data.max_ope_pole == 6

    def test_32_max_rmatrix_pole(self):
        """Max r-matrix pole for (3,2): 5 (= 6 - 1 by AP19).

        AP19: the bar kernel d log(z-w) absorbs one pole order.
        """
        data = ope_pole_data_32()
        assert data.max_rmatrix_pole == 5

    def test_221_max_poles(self):
        """Max OPE pole for (2,2,1): 4 (from h=2 self-OPE).
        Max r-matrix pole: 3.
        """
        data = ope_pole_data_221()
        assert data.max_ope_pole == 4
        assert data.max_rmatrix_pole == 3


# ===================================================================
# VIII. Shadow depth classification
# ===================================================================

class TestShadowDepth:
    """Shadow depth classification on the T-line."""

    def test_32_class_M(self):
        """W^k(sl_5, f_{(3,2)}) is class M (infinite shadow depth)."""
        sd = shadow_depth_32()
        assert sd.t_line_class == 'M'
        assert sd.t_line_depth == oo
        assert sd.overall_class == 'M'

    def test_221_class_M(self):
        """W^k(sl_5, f_{(2,2,1)}) is also class M."""
        sd = shadow_depth_221()
        assert sd.t_line_class == 'M'
        assert sd.t_line_depth == oo

    def test_32_generically_nondegenerate(self):
        """c and 5c+22 are generically nonzero for (3,2).

        c = 0 at k=49 (isolated); 5c+22 = 0 at k = -61/16 (isolated).
        """
        sd = shadow_depth_32()
        assert sd.c_is_generically_nonzero is True
        assert sd.five_c_plus_22_generically_nonzero is True
        # Verify the isolated vanishing
        assert simplify(central_charge_32(49)) == 0
        # 5c+22 vanishes at the root of 5*c_32(k)+22=0; verify it's generically nonzero
        c_at_1 = central_charge_32(Rational(1))
        assert simplify(5 * c_at_1 + 22) != 0  # generically nonzero


# ===================================================================
# IX. Hook comparison and obstruction analysis
# ===================================================================

class TestHookComparisonAndObstruction:
    """Comparison of (3,2) with hook partitions in sl_5."""

    def test_comparison_table_completeness(self):
        """The comparison table has all 7 partitions of 5."""
        table = sl5_hook_comparison_table()
        assert len(table) == 7

    def test_hook_partitions_identified(self):
        """Hooks in sl_5: (5), (4,1), (3,1,1), (2,1,1,1), (1^5)."""
        table = sl5_hook_comparison_table()
        hooks = [e.partition for e in table if e.is_hook]
        assert (5,) in hooks
        assert (4, 1) in hooks
        assert (3, 1, 1) in hooks
        assert (2, 1, 1, 1) in hooks
        assert (1, 1, 1, 1, 1) in hooks
        # (3,2) and (2,2,1) are NOT hooks
        non_hooks = [e.partition for e in table if not e.is_hook]
        assert (3, 2) in non_hooks
        assert (2, 2, 1) in non_hooks

    def test_obstruction_rho_mismatch(self):
        """The anomaly ratio mismatch is the root of conductor k-dependence."""
        obs = hook_transport_obstruction_32()
        assert obs.rho_source == Rational(1, 5)
        assert obs.rho_target == Rational(10, 3)
        assert obs.rho_match is False

    def test_obstruction_spectra_mismatch(self):
        """Generator spectra of (3,2) and (2,2,1) differ qualitatively.

        (3,2) has generators up to h=3; (2,2,1) has generators only up to h=2.
        """
        obs = hook_transport_obstruction_32()
        assert Rational(3) in obs.source_weights
        assert Rational(3) not in obs.target_weights
        assert obs.spectra_match is False

    def test_obstruction_conductor(self):
        """The conductor for (3,2) is k-dependent."""
        obs = hook_transport_obstruction_32()
        assert obs.conductor_k_dependent is True


# ===================================================================
# X. Seven-face programme and DS-KD diagram
# ===================================================================

class TestSevenFaceAndDSKD:
    """Seven-face programme status and DS-KD diagram."""

    def test_ds_kd_diagram_32_conjectural(self):
        """The DS-KD diagram for (3,2) is NOT proved."""
        diag = ds_kd_diagram_32()
        assert diag.is_hook is False
        assert diag.kd_right_proved is False
        assert diag.diagram_proved is False
        assert diag.koszul_dual_identified is False
        assert diag.proof_status == 'conjectural'
        # But DS reduction EXISTS (KRW)
        assert diag.ds_exists is True

    def test_seven_face_32_bar_proved(self):
        """Face 1 (bar complex = completed Koszulity) is PROVED for (3,2)."""
        sf = seven_face_status_32()
        assert 'PROVED' in sf.face_1_bar_complex

    def test_seven_face_32_kd_open(self):
        """Face 2 (Koszul dual identification) is OPEN for (3,2)."""
        sf = seven_face_status_32()
        assert 'OPEN' in sf.face_2_koszul_dual

    def test_numerical_data_consistency(self):
        """Numerical data at k=1 is self-consistent.

        Path 3: verify conductor = c_32 + c_221_dual.
        """
        nd = numerical_data_32(1)
        assert simplify(nd['conductor'] - (nd['c_32'] + nd['c_221_dual'])) == 0
        assert simplify(nd['kappa_sum'] - (nd['kappa_32'] + nd['kappa_221_dual'])) == 0
        # Check specific values
        # c(3,2; 1) = 2*(1-49)/(1+5) = 2*(-48)/6 = -16
        assert simplify(nd['c_32'] - (-16)) == 0
        # dual_level = -1 - 10 = -11
        assert simplify(nd['dual_level'] - (-11)) == 0
