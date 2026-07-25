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
    ClaimPacket,
    ClaimStatus,
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    krw_central_charge,
    krw_central_charge_data,
    w_algebra_generator_data,
)

k = Symbol('k')


def _assert_unresolved(packet: ClaimPacket, status: ClaimStatus) -> None:
    """Assert a typed open/conditional obligation (value withheld)."""

    assert isinstance(packet, ClaimPacket)
    assert packet.status is status
    assert packet.value is None
    assert packet.hypotheses


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
        """W^k(sl_5, f_{(3,2)}) has 8 strong generators, all even.

        In type A every strong generator from the sl_2-block pairing is
        even (non_principal_w_bar_engine.type_a_strong_generators).
        """
        spec = generator_spectrum_32()
        assert len(spec.generators) == 8
        assert spec.num_bosonic == 8
        assert spec.num_fermionic == 0

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
        """W^k(sl_5, f_{(2,2,1)}) has 12 strong generators, all even."""
        spec = generator_spectrum_221()
        assert len(spec.generators) == 12
        assert spec.num_bosonic == 12
        assert spec.num_fermionic == 0

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
        """c(3,2; k) = (-30k^2 - 178k - 260)/(k+5) via per-root-pair KRW.

        Path 1: from engine (canonical krw_central_charge oracle).
        Path 2: direct per-root-pair recomputation from
                x = h/2 = diag(1, 0, -1, 1/2, -1/2):
                |x|^2 = 5/2, ghost sum 50, dim(g_{1/2})/2 = 2, so
                c(k) = 24k/(k+5) - 30k - 52.
        """
        c = central_charge_32()
        expected = (-30 * k**2 - 178 * k - 260) / (k + 5)
        assert simplify(c - expected) == 0
        # Path 2: independent inline evaluation.
        inline = 24 * k / (k + 5) - 30 * k - 52
        assert simplify(c - inline) == 0

    def test_221_central_charge_formula(self):
        """c(2,2,1; k) = -6(2k+5)(k+1)/(k+5) via per-root-pair KRW.

        x = h/2 = diag(1/2, -1/2, 1/2, -1/2, 0): |x|^2 = 1, ghost sum 4,
        dim(g_{1/2})/2 = 2, so c(k) = 24k/(k+5) - 12k - 6.
        """
        c = central_charge_221()
        expected = (-12 * k**2 - 42 * k - 30) / (k + 5)
        assert simplify(c - expected) == 0
        inline = 24 * k / (k + 5) - 12 * k - 6
        assert simplify(c - inline) == 0

    def test_32_central_charge_at_zero(self):
        """c(3,2; 0) = -260/5 = -52; c(3,2; 1) = -468/6 = -78.

        Path 3: numerical evaluation against the canonical anchors.
        """
        assert simplify(central_charge_32(0) + 52) == 0
        assert simplify(central_charge_32(1) + 78) == 0

    def test_central_charge_vanishing_levels(self):
        """Real zeros of the canonical formulas are negative and non-generic.

        c(3,2; k): numerator -30k^2 - 178k - 260 has discriminant
        178^2 - 4*30*260 = 484 = 22^2, zeros k = -13/5 and k = -10/3.
        c(2,2,1; k) = -6(2k+5)(k+1)/(k+5): zeros k = -1, -5/2.
        All zeros lie in k < 0; for k >= 0 both central charges are
        strictly negative.
        """
        assert simplify(central_charge_32(Rational(-13, 5))) == 0
        assert simplify(central_charge_32(Rational(-10, 3))) == 0
        assert simplify(central_charge_221(-1)) == 0
        assert simplify(central_charge_221(Rational(-5, 2))) == 0
        for kv in [0, 1, 10, 100]:
            assert central_charge_32(kv) < 0
            assert central_charge_221(kv) < 0


# ===================================================================
# IV. Kappa and anomaly ratio
# ===================================================================

class TestKappaAndAnomalyRatio:
    """rho and kappa are typed OPEN/CONDITIONAL packets.

    No derivation of the anomaly ratio rho exists for these orbits (the
    generator-weight reciprocal sum is not a derivation).  rho is
    therefore an OPEN typed packet, and kappa = rho * c is CONDITIONAL
    through it.  Nothing here fabricates a scalar rho.
    """

    def test_32_anomaly_ratio(self):
        """rho_{(3,2)} is an OPEN typed obligation, not a scalar.

        Named obligations: a nonseparating genus-one calculation, and a
        theorem identifying rho with a specified modular channel.
        """
        spec = generator_spectrum_32()
        _assert_unresolved(spec.anomaly_ratio, ClaimStatus.OPEN)
        # Canonical engine returns the same typed lane.
        _assert_unresolved(
            anomaly_ratio_from_partition((3, 2)), ClaimStatus.OPEN
        )

    def test_221_anomaly_ratio(self):
        """rho_{(2,2,1)} is an OPEN typed obligation, not a scalar."""
        spec = generator_spectrum_221()
        _assert_unresolved(spec.anomaly_ratio, ClaimStatus.OPEN)
        _assert_unresolved(
            anomaly_ratio_from_partition((2, 2, 1)), ClaimStatus.OPEN
        )

    def test_32_kappa_formula(self):
        """kappa(3,2) = rho * c passes through OPEN rho: typed CONDITIONAL."""
        _assert_unresolved(kappa_32(), ClaimStatus.CONDITIONAL)

    def test_32_kappa_at_zero(self):
        """kappa at a numerical level is still a typed packet (rho OPEN)."""
        _assert_unresolved(kappa_32(0), ClaimStatus.CONDITIONAL)


# ===================================================================
# V. Koszul conductor and complementarity
# ===================================================================

class TestConductorAndComplementarity:
    """Koszul conductor and kappa complementarity for the (3,2)/(2,2,1) pair."""

    def test_conductor_formula(self):
        """K(k) = c(3,2;k) + c(2,2,1;-k-10) = 110 - 18k = 2(55 - 9k).

        Path 1: from engine.
        Path 2: direct recomputation from the two canonical central
                charges (the pole at k = -5 cancels; the sum is a
                polynomial, yet still k-dependent).
        """
        K = koszul_conductor_32()
        expected = 110 - 18 * k
        assert simplify(K - expected) == 0
        # Path 2: recompute from the canonical central charges.
        direct = simplify(central_charge_32() + central_charge_221(-k - 10))
        assert simplify(K - direct) == 0

    def test_conductor_is_k_dependent(self):
        """The conductor for (3,2)/(2,2,1) is k-DEPENDENT.

        K(k) = 110 - 18k: K(0) = 110, K(1) = 92.  Non-self-transpose
        pairs have differing KRW quadratic coefficients, so no level
        reflection makes the sum constant.
        """
        K0, K1, are_different = conductor_k_dependence_check()
        assert are_different is True
        assert simplify(K0 - 110) == 0
        assert simplify(K1 - 92) == 0

    def test_kappa_sum_k_dependent(self):
        """The kappa sum is a typed OPEN packet (passes through OPEN rho).

        kappa = rho * c with rho underived on both sides: the sum carries
        the obligation instead of a rational function.  The exact,
        rho-free shadow of the same phenomenon is the k-dependence of the
        conductor (previous test).
        """
        _assert_unresolved(kappa_sum_32(), ClaimStatus.OPEN)

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
        # Value: K = 212 (per-root-pair formula for self-transpose (3,1,1))
        # VERIFIED: [DC] per-root-pair formula; [CF] matches butson engine
        assert simplify(K - 212) == 0


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

        c(3,2; k) = (-30k^2 - 178k - 260)/(k+5) vanishes only at
        k = -13/5 and k = -10/3 (both negative), so c is generically
        nonzero; 5c + 22 likewise vanishes only at isolated levels.
        """
        sd = shadow_depth_32()
        assert sd.c_is_generically_nonzero is True
        assert sd.five_c_plus_22_generically_nonzero is True
        # c(3,2) is negative for all k >= 0.
        assert central_charge_32(0) < 0
        assert central_charge_32(1) < 0
        # 5c+22 at k=1: 5*(-78) + 22 = -368, nonzero.
        c_at_1 = central_charge_32(Rational(1))
        assert simplify(5 * c_at_1 + 22) == -368


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
        """rho comparison is OPEN; conductor k-dependence is the computed
        obstruction.

        Both rho packets are typed OPEN (no derivation exists), so the
        match verdict is None -- undetermined, not False.  The exact
        obstruction is carried by the conductor (next test) and the
        spectra mismatch.
        """
        obs = hook_transport_obstruction_32()
        _assert_unresolved(obs.rho_source, ClaimStatus.OPEN)
        _assert_unresolved(obs.rho_target, ClaimStatus.OPEN)
        assert obs.rho_match is None

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

        Exact scalar lane: conductor = c_32 + c_221_dual, with the
        canonical anchor c(3,2; 1) = (-30 - 178 - 260)/6 = -78.
        Typed lane: the kappa entries pass through OPEN rho and are
        ClaimPackets, never scalars.
        """
        nd = numerical_data_32(1)
        assert simplify(nd['conductor'] - (nd['c_32'] + nd['c_221_dual'])) == 0
        # Canonical anchors.
        assert simplify(nd['c_32'] - (-78)) == 0
        assert simplify(nd['c_221_dual'] - nd['conductor'] + nd['c_32']) == 0
        # K(1) = 110 - 18 = 92.
        assert simplify(nd['conductor'] - 92) == 0
        # dual_level = -1 - 10 = -11
        assert simplify(nd['dual_level'] - (-11)) == 0
        # Typed kappa lane.
        _assert_unresolved(nd['kappa_32'], ClaimStatus.CONDITIONAL)
        _assert_unresolved(nd['kappa_221_dual'], ClaimStatus.CONDITIONAL)
        _assert_unresolved(nd['kappa_sum'], ClaimStatus.OPEN)
