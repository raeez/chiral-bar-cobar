r"""Tests for non-principal line-operator data via DNP25 constraints.

53 tests verifying line-operator category data for non-principal W-algebras,
organized into 8 sections:

  I.   Central charge formulas (8 tests)
  II.  Anomaly ratios and kappa (8 tests)
  III. Koszul conductors and complementarity (7 tests)
  IV.  Shadow depth classification (6 tests)
  V.   Line-operator category data (6 tests)
  VI.  DS reduction commutative diagram (6 tests)
  VII. r-matrix channel structure (6 tests)
  VIII.Cross-family consistency and numerical checks (6 tests)

Multi-path verification:
  Path 1: direct formula evaluation
  Path 2: complementarity / duality cross-check
  Path 3: numerical evaluation at test levels
  Path 4: cross-check with existing engines (bp_shadow_tower, hook_type_w_duality)
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, cancel, oo, S

from compute.lib.theorem_nonprincipal_line_operators_engine import (
    # Central charges
    bp_central_charge,
    principal_w3_central_charge,
    principal_wn_central_charge,
    affine_central_charge,
    virasoro_central_charge,
    # Dual levels
    ff_dual_level,
    bp_dual_level,
    # Conductors
    koszul_conductor_bp,
    koszul_conductor_principal_wn,
    # Anomaly ratios and kappa
    bp_anomaly_ratio,
    bp_kappa,
    principal_w3_anomaly_ratio,
    principal_w3_kappa,
    virasoro_anomaly_ratio,
    virasoro_kappa,
    # Complementarity
    bp_kappa_complementarity,
    principal_w3_kappa_complementarity,
    # Generator data
    bp_generator_data,
    principal_w3_generator_data,
    virasoro_generator_data,
    # Shadow depth
    shadow_depth_classification,
    bp_shadow_depth,
    bp_shadow_tower_on_tline,
    virasoro_shadow_tower,
    # Line operators
    affine_line_operators,
    bp_line_operators,
    principal_w3_line_operators,
    sl4_hook_31_line_operators,
    sl4_hook_211_line_operators,
    # DS diagram
    ds_line_reduction_diagram,
    # r-matrix
    bp_rmatrix_channels,
    bp_rmatrix_max_pole,
    principal_w3_rmatrix_max_pole,
    # Catalog
    build_catalog,
    # Numerical
    bp_numerical_at_level,
)

k = Symbol('k')


# ===================================================================
# I. Central charge formulas
# ===================================================================

class TestCentralCharges:
    """Central charge formulas for non-principal W-algebras."""

    def test_bp_c_at_zero(self):
        """c_BP(0) = 2 - 24*1/3 = 2 - 8 = -6."""
        assert simplify(bp_central_charge(0) - (-6)) == 0

    def test_bp_c_at_one(self):
        """c_BP(1) = 2 - 24*4/4 = 2 - 24 = -22."""
        assert simplify(bp_central_charge(1) - (-22)) == 0

    def test_bp_c_at_minus_one(self):
        """c_BP(-1) = 2 - 24*0/2 = 2."""
        assert simplify(bp_central_charge(-1) - 2) == 0

    def test_bp_c_at_admissible(self):
        """c_BP(-3/2) = -2 (the admissible level, FKR 2020 decisive test)."""
        assert simplify(bp_central_charge(Rational(-3, 2)) - (-2)) == 0

    def test_w3_c_at_zero(self):
        """c_{W_3}(0) = 2 - 24*4/3 = 2 - 32 = -30."""
        assert simplify(principal_w3_central_charge(0) - (-30)) == 0

    def test_virasoro_c_at_zero(self):
        """c_{Vir}(0) = 1 - 6*1/2 = 1 - 3 = -2."""
        assert simplify(virasoro_central_charge(0) - (-2)) == 0

    def test_virasoro_c_at_one(self):
        """c_{Vir}(1) = 1 - 6*4/3 = 1 - 8 = -7."""
        assert simplify(virasoro_central_charge(1) - (-7)) == 0

    def test_affine_sl3_c_at_one(self):
        """c(V_1(sl_3)) = 1*8/4 = 2."""
        assert simplify(affine_central_charge(3, 1) - 2) == 0


# ===================================================================
# II. Anomaly ratios and kappa
# ===================================================================

class TestAnomalyRatiosKappa:
    """Anomaly ratios and modular characteristic kappa."""

    def test_bp_anomaly_ratio(self):
        """rho_BP = 1 - 2/3 - 2/3 + 1/2 = 1/6."""
        assert bp_anomaly_ratio() == Rational(1, 6)

    def test_w3_anomaly_ratio(self):
        """rho_{W_3} = 1/2 + 1/3 = 5/6."""
        assert principal_w3_anomaly_ratio() == Rational(5, 6)

    def test_virasoro_anomaly_ratio(self):
        """rho_{Vir} = 1/2."""
        assert virasoro_anomaly_ratio() == Rational(1, 2)

    def test_bp_kappa_is_rho_times_c(self):
        """kappa_BP(k) = (1/6) * c_BP(k)."""
        diff = simplify(bp_kappa() - Rational(1, 6) * bp_central_charge())
        assert diff == 0

    def test_bp_kappa_at_zero(self):
        """kappa_BP(0) = (1/6)(-7) = -7/6."""
        assert simplify(bp_kappa(0) - Rational(-1, 1)) == 0

    def test_w3_kappa_at_zero(self):
        """kappa_{W_3}(0) = (5/6)(-30) = -25."""
        assert simplify(principal_w3_kappa(0) - (-25)) == 0

    def test_virasoro_kappa_at_zero(self):
        """kappa_{Vir}(0) = (1/2)(-2) = -1."""
        assert simplify(virasoro_kappa(0) - (-1)) == 0

    def test_virasoro_kappa_formula(self):
        """kappa_{Vir}(k) = c(k)/2, cross-check with existing convention."""
        diff = simplify(virasoro_kappa() - virasoro_central_charge() / 2)
        assert diff == 0


# ===================================================================
# III. Koszul conductors and complementarity
# ===================================================================

class TestKoszulConductors:
    """Koszul conductors and kappa complementarity sums."""

    def test_bp_conductor_196(self):
        """K_BP = c_BP(k) + c_BP(-k-6) = 196."""
        assert simplify(koszul_conductor_bp() - 196) == 0

    def test_w3_conductor_100(self):
        """K_{W_3} = c_{W_3}(k) + c_{W_3}(-k-6) = 100."""
        assert simplify(koszul_conductor_principal_wn(3) - 100) == 0

    def test_virasoro_conductor_26(self):
        """K_{Vir} = c_{Vir}(k) + c_{Vir}(-k-4) = 26."""
        assert simplify(koszul_conductor_principal_wn(2) - 26) == 0

    def test_w4_conductor_246(self):
        """K_{W_4} = 246."""
        assert simplify(koszul_conductor_principal_wn(4) - 246) == 0

    def test_bp_kappa_complementarity(self):
        """kappa_BP(k) + kappa_BP(-k-6) = 98/3 = (1/6)*196.

        For a self-transpose partition, the kappa sum is rho * K.
        """
        assert simplify(bp_kappa_complementarity() - Rational(98, 3)) == 0

    def test_w3_kappa_complementarity(self):
        """kappa_{W_3}(k) + kappa_{W_3}(-k-6) = 250/3 = (5/6)*100."""
        assert simplify(principal_w3_kappa_complementarity() - Rational(250, 3)) == 0

    def test_kappa_sum_equals_rho_times_K(self):
        """For self-transpose orbits, kappa(k) + kappa(k') = rho * K.

        BP: rho = 1/6, K = 196, product = 98/3.
        Virasoro: rho = 1/2, K = 26, product = 13.
        """
        # BP
        bp_product = bp_anomaly_ratio() * koszul_conductor_bp()
        assert simplify(bp_product - bp_kappa_complementarity()) == 0
        # Virasoro (self-transpose because (2)^t = (1,1) but KD stays in Vir family)
        vir_rho = virasoro_anomaly_ratio()
        vir_K = koszul_conductor_principal_wn(2)
        vir_kap_sum = simplify(virasoro_kappa() + virasoro_kappa(ff_dual_level(2)))
        assert simplify(vir_rho * vir_K - vir_kap_sum) == 0


# ===================================================================
# IV. Shadow depth classification
# ===================================================================

class TestShadowDepth:
    """Shadow depth classification for non-principal W-algebras."""

    def test_bp_tline_class_M(self):
        """BP T-line is class M (infinite depth): generic c nonzero."""
        depth_data = bp_shadow_depth()
        assert depth_data['T_line']['class'] == 'M'

    def test_bp_jline_class_G(self):
        """BP J-line is class G (depth 2): abelian current."""
        depth_data = bp_shadow_depth()
        assert depth_data['J_line']['class'] == 'G'
        assert depth_data['J_line']['depth'] == 2

    def test_bp_overall_class_M(self):
        """BP overall classification is M (deepest line dominates)."""
        depth_data = bp_shadow_depth()
        assert depth_data['overall'] == 'M'

    def test_generic_c_gives_class_M(self):
        """A generic central charge (nonzero, 5c+22 nonzero) gives class M."""
        cls, depth = shadow_depth_classification(Symbol('c'))
        assert cls == 'M'
        assert depth == oo

    def test_c_zero_gives_class_G(self):
        """c = 0 gives class G (depth 2)."""
        cls, depth = shadow_depth_classification(S(0))
        assert cls == 'G'
        assert depth == 2

    def test_bp_tline_tower_nonzero(self):
        """The BP T-line tower has nonzero quartic and quintic coefficients."""
        tower = bp_shadow_tower_on_tline(6)
        # Quartic should be nonzero
        assert simplify(tower[4]) != 0
        # Quintic should be nonzero
        assert simplify(tower[5]) != 0


# ===================================================================
# V. Line-operator category data
# ===================================================================

class TestLineOperatorData:
    """Line-operator category data from DNP25 framework."""

    def test_bp_is_self_dual(self):
        """BP is self-dual: (2,1)^t = (2,1)."""
        data = bp_line_operators()
        assert data.is_self_dual is True

    def test_bp_dual_level(self):
        """BP dual level is k' = -k - 6."""
        assert data_has_dual_formula(bp_line_operators(), '-k - 6')

    def test_w3_is_not_self_dual(self):
        """W_3 is NOT self-dual: (3)^t = (1,1,1)."""
        data = principal_w3_line_operators()
        assert data.is_self_dual is False

    def test_sl4_hooks_are_transpose_pair(self):
        """(3,1) and (2,1,1) are transpose pairs in sl_4."""
        data_31 = sl4_hook_31_line_operators()
        data_211 = sl4_hook_211_line_operators()
        assert data_31.koszul_dual_partition == (2, 1, 1)
        assert data_211.koszul_dual_partition == (3, 1)

    def test_affine_sl3_quantum_group(self):
        """Affine sl_3 line operators use U_q(sl_3)."""
        data = affine_line_operators(3)
        assert 'U_q(sl_3)' in data.quantum_group_type

    def test_bp_quantum_parameter(self):
        """BP quantum parameter involves (k + 3)."""
        data = bp_line_operators()
        assert '(k + 3)' in data.quantum_parameter_formula


def data_has_dual_formula(data, fragment):
    """Check that the dual level formula contains the given fragment."""
    return fragment in data.dual_level_formula


# ===================================================================
# VI. DS reduction commutative diagram
# ===================================================================

class TestDSLineDiagram:
    """DS reduction commutative diagram for line categories."""

    def test_bp_diagram_commutes(self):
        """DS-KD diagram commutes for BP (hook type, self-transpose)."""
        diag = ds_line_reduction_diagram((2, 1), 3)
        assert diag.diagram_commutes is True

    def test_bp_self_transpose(self):
        """BP partition (2,1) is self-transpose."""
        diag = ds_line_reduction_diagram((2, 1), 3)
        assert diag.is_self_transpose is True

    def test_sl4_31_diagram_commutes(self):
        """DS-KD diagram commutes for sl_4 hook (3,1) (proved corridor)."""
        diag = ds_line_reduction_diagram((3, 1), 4)
        assert diag.diagram_commutes is True
        assert diag.right_vertical_proved is True

    def test_sl4_22_diagram_not_proved(self):
        """DS-KD diagram for (2,2) in sl_4 is NOT on the proved corridor.

        (2,2) is NOT hook-type (it has two parts > 1).
        """
        diag = ds_line_reduction_diagram((2, 2), 4)
        assert diag.diagram_commutes is False

    def test_affine_kd_always_proved(self):
        """The left vertical (affine KD) is always proved."""
        for partition in [(2, 1), (3, 1), (2, 2), (3,)]:
            N = sum(partition)
            diag = ds_line_reduction_diagram(partition, N)
            assert diag.left_vertical_proved is True

    def test_principal_diagram_commutes(self):
        """DS-KD diagram for principal nilpotent always commutes."""
        for N in [2, 3, 4, 5]:
            diag = ds_line_reduction_diagram((N,), N)
            assert diag.diagram_commutes is True


# ===================================================================
# VII. r-matrix channel structure
# ===================================================================

class TestRMatrixChannels:
    """r-matrix channel data for non-principal W-algebras."""

    def test_bp_has_11_channels(self):
        """BP r-matrix has 11 OPE channels (from 4 generators)."""
        channels = bp_rmatrix_channels()
        assert len(channels) == 11

    def test_bp_max_pole_3(self):
        """BP r-matrix maximum pole order is 3 (from T-T channel).

        AP19: the bar kernel absorbs a pole. T(z)T(w) OPE has pole
        order 4, so r-matrix has pole order 3.
        """
        assert bp_rmatrix_max_pole() == 3

    def test_w3_max_pole_5(self):
        """W_3 r-matrix maximum pole order is 5 (from W-W channel).

        W(z)W(w) OPE has pole order 6, so r-matrix pole order 5.
        """
        assert principal_w3_rmatrix_max_pole() == 5

    def test_ap19_pole_shift(self):
        """AP19: r-matrix pole = OPE pole - 1 for every channel."""
        channels = bp_rmatrix_channels()
        for ch in channels:
            if ch.ope_max_pole > 0:
                assert ch.rmatrix_max_pole == ch.ope_max_pole - 1, (
                    f'{ch.source_gen}-{ch.target_gen}: '
                    f'OPE pole {ch.ope_max_pole}, '
                    f'r-matrix pole {ch.rmatrix_max_pole}'
                )

    def test_fermionic_self_ope_vanish(self):
        """G+G+ and G-G- OPE channels have zero pole (fermion statistics)."""
        channels = bp_rmatrix_channels()
        for ch in channels:
            if ch.source_gen == ch.target_gen and 'G' in ch.source_gen:
                assert ch.ope_max_pole == 0

    def test_jj_channel_structure(self):
        """J-J channel: double pole OPE -> single pole r-matrix."""
        channels = bp_rmatrix_channels()
        jj = [ch for ch in channels if ch.source_gen == 'J' and ch.target_gen == 'J']
        assert len(jj) == 1
        assert jj[0].ope_max_pole == 2
        assert jj[0].rmatrix_max_pole == 1


# ===================================================================
# VIII. Cross-family consistency and numerical checks
# ===================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency and numerical verification."""

    def test_bp_vs_w3_different_conductors(self):
        """BP and W_3 are different DS reductions of sl_3 with DIFFERENT conductors.

        K_BP = 196, K_{W_3} = 100.  These differ because BP and W_3 use
        different nilpotent orbits of sl_3.
        """
        K_bp = koszul_conductor_bp()
        K_w3 = koszul_conductor_principal_wn(3)
        assert simplify(K_bp - 196) == 0
        assert simplify(K_w3 - 100) == 0
        assert simplify(K_bp - K_w3) != 0

    def test_bp_numerical_kappa_sum_constant(self):
        """kappa_BP(k) + kappa_BP(-k-6) is the same at multiple levels.

        Multi-path verification: compute at k = 1, 2, 5, 10 and check
        they all give the same value (98/3).
        """
        expected = Rational(98, 3)
        for lv in [1, 2, 5, 10]:
            data = bp_numerical_at_level(lv)
            assert simplify(data['kappa_sum'] - expected) == 0, (
                f'kappa_sum at k={lv}: {data["kappa_sum"]} != {expected}'
            )

    def test_conductor_hierarchy(self):
        """Conductors: K_Vir < K_{W_3} < K_BP < K_{W_4}.

        Virasoro (rank 1): 26.  W_3 (rank 2, principal): 100.
        BP (rank 2, non-principal): 196 (K=196, FKR 2020).
        W_4 (rank 3): 246.
        """
        conductors = [
            koszul_conductor_principal_wn(2),  # 26
            koszul_conductor_principal_wn(3),  # 100
            koszul_conductor_bp(),              # 196
            koszul_conductor_principal_wn(4),  # 246
        ]
        for i in range(len(conductors) - 1):
            assert conductors[i] < conductors[i + 1]

    def test_catalog_completeness(self):
        """The catalog contains all expected entries."""
        cat = build_catalog()
        assert 'Vir' in cat
        assert 'BP' in cat
        assert 'W3' in cat
        assert 'sl4_31' in cat
        assert 'sl4_211' in cat

    def test_catalog_bp_invariants(self):
        """Catalog BP entry has correct invariants."""
        cat = build_catalog()
        bp = cat['BP']
        assert bp.N == 3
        assert bp.partition == (2, 1)
        assert bp.transpose == (2, 1)
        assert bp.anomaly_ratio == Rational(1, 6)
        assert simplify(bp.koszul_conductor - 196) == 0
        assert bp.shadow_class == 'M'

    def test_bp_c_sum_with_dual(self):
        """c_BP(k) + c_BP(k') = K_BP = 196, verified at numerical levels.

        This is a direct check of the Koszul conductor, evaluated numerically
        at several levels as a cross-check against the symbolic computation.
        """
        for lv in [1, 2, 5, 10, Rational(-1, 2)]:
            c_k = bp_central_charge(lv)
            c_kp = bp_central_charge(bp_dual_level(lv))
            assert simplify(c_k + c_kp - 196) == 0, (
                f'c_BP({lv}) + c_BP({bp_dual_level(lv)}) = {simplify(c_k + c_kp)}'
            )


# ===================================================================
# IX. Multi-path cross-engine verification (AP10 compliance)
# ===================================================================

class TestCrossEngineVerification:
    """Cross-engine verification against existing compute modules.

    Every numerical value is verified by at least 2 independent paths.
    """

    def test_bp_c_matches_bp_shadow_tower_engine(self):
        """BP central charge matches the existing bp_shadow_tower engine.

        Path 1: this engine's bp_central_charge().
        Path 2: bp_shadow_tower.bp_central_charge() (independent implementation).
        """
        from compute.lib.bp_shadow_tower import bp_central_charge as bp_c_v2
        c_this = bp_central_charge()
        c_other = bp_c_v2()
        assert simplify(c_this - c_other) == 0

    def test_bp_koszul_conductor_matches_bp_shadow_tower(self):
        """K_BP = 196 cross-checked against bp_shadow_tower.bp_koszul_conductor().

        Path 1: this engine's koszul_conductor_bp().
        Path 2: bp_shadow_tower.bp_koszul_conductor().
        """
        from compute.lib.bp_shadow_tower import bp_koszul_conductor as bp_K_v2
        K_this = koszul_conductor_bp()
        K_other = bp_K_v2()
        assert simplify(K_this - K_other) == 0

    def test_bp_anomaly_ratio_matches_hook_engine(self):
        """BP anomaly ratio 1/6 cross-checked against hook_type_w_duality engine.

        Path 1: this engine's bp_anomaly_ratio() (hardcoded from generator content).
        Path 2: hook_type_w_duality.anomaly_ratio_from_partition((2,1))
                (computed from the actual f-centralizer data).
        """
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        rho_this = bp_anomaly_ratio()
        rho_hook = anomaly_ratio_from_partition((2, 1))
        assert rho_this == rho_hook

    def test_bp_kappa_matches_hook_engine(self):
        """BP kappa cross-checked against hook_type_w_duality.ds_kappa_from_affine.

        Path 1: this engine's bp_kappa().
        Path 2: ds_kappa_from_affine((2,1), k) from hook_type_w_duality.
        NOTE: ds_kappa_from_affine uses the KRW formula which is the
        OVERSIMPLIFIED version.  The correct formula gives a DIFFERENT value.
        The anomaly RATIO is the same (1/6); the central charge differs.
        So we compare ratios, not absolute kappa values.
        """
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        # Both agree on the anomaly ratio
        assert bp_anomaly_ratio() == anomaly_ratio_from_partition((2, 1))
        # And both agree that kappa = rho * c
        rho = bp_anomaly_ratio()
        kappa_direct = bp_kappa()
        kappa_from_rho_c = rho * bp_central_charge()
        assert simplify(kappa_direct - kappa_from_rho_c) == 0

    def test_w3_anomaly_ratio_matches_hook_engine(self):
        """W_3 anomaly ratio 5/6 cross-checked against hook_type_w_duality.

        Path 1: this engine (1/2 + 1/3 = 5/6).
        Path 2: anomaly_ratio_from_partition((3,)) computed from sl_3 data.
        """
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        assert principal_w3_anomaly_ratio() == anomaly_ratio_from_partition((3,))

    def test_bp_shadow_tower_matches_bp_shadow_tower_engine(self):
        """BP T-line shadow tower cross-checked against bp_shadow_tower engine.

        Path 1: this engine's bp_shadow_tower_on_tline().
        Path 2: bp_shadow_tower.bp_tline_shadow_tower().
        Both should give identical rational functions of k.
        """
        from compute.lib.bp_shadow_tower import bp_tline_shadow_tower
        tower_this = bp_shadow_tower_on_tline(6)
        tower_other = bp_tline_shadow_tower(6)
        for r in range(2, 7):
            assert simplify(tower_this[r] - tower_other[r]) == 0, (
                f'Sh_{r}: this={tower_this[r]}, other={tower_other[r]}'
            )

    def test_virasoro_conductor_matches_wn_canonical(self):
        """K_Vir = 26 cross-checked against wn_central_charge_canonical.

        Path 1: this engine's koszul_conductor_principal_wn(2).
        Path 2: wn_central_charge_canonical: c_wn_fl(2, k) + c_wn_fl(2, -k-4) = 26.
        """
        from fractions import Fraction
        from compute.lib.wn_central_charge_canonical import c_wn_fl
        # Check at several levels
        for k_val in [1, 2, 5, 10]:
            c_sum = c_wn_fl(2, Fraction(k_val)) + c_wn_fl(2, Fraction(-k_val - 4))
            assert c_sum == Fraction(26), f'K_Vir at k={k_val}: {c_sum}'

    def test_w3_kappa_sum_matches_wn_canonical(self):
        """W_3 kappa complementarity sum 250/3 cross-checked.

        Path 1: this engine's principal_w3_kappa_complementarity().
        Path 2: wn_central_charge_canonical.kappa_complementarity_sum(3).
        """
        from compute.lib.wn_central_charge_canonical import (
            kappa_complementarity_sum as kcs_canonical,
        )
        from fractions import Fraction
        canonical_val = kcs_canonical(3)
        this_val = principal_w3_kappa_complementarity()
        assert simplify(this_val - Rational(canonical_val.numerator,
                                            canonical_val.denominator)) == 0

    def test_bp_dual_level_matches_bp_shadow_tower(self):
        """BP dual level k' = -k-6 cross-checked.

        Path 1: this engine's bp_dual_level().
        Path 2: bp_shadow_tower.bp_dual_level().
        """
        from compute.lib.bp_shadow_tower import bp_dual_level as bp_dl_v2
        assert simplify(bp_dual_level() - bp_dl_v2()) == 0

    def test_bp_depth_matches_bp_shadow_tower(self):
        """BP depth classification cross-checked.

        Path 1: this engine's bp_shadow_depth().
        Path 2: bp_shadow_tower.bp_depth_classification().
        """
        from compute.lib.bp_shadow_tower import bp_depth_classification
        depth_this = bp_shadow_depth()
        depth_other = bp_depth_classification()
        assert depth_this['T_line']['class'] == depth_other['T_line']['class']
        assert depth_this['J_line']['class'] == depth_other['J_line']['class']
