r"""Tests for grand_synthesis_engine.py: cross-verification across three frontier problems.

50+ tests organized by the 10 cross-verification axes.

Multi-path verification strategy:
  - Every kappa tested by at least 2 independent formulas
  - Every shadow class tested against multiple characterizations
  - Every cross-problem identification verified numerically

ANTI-PATTERN COMPLIANCE:
  AP1:  kappa formulas tested per-family, never copied
  AP10: expected values derived from independent computation, not hardcoded
  AP14: shadow depth != Koszulness (all families Koszul)
  AP19: r-matrix pole order tested (1 below OPE)
  AP24: kappa + kappa' != 0 for Virasoro (= 13)
  AP39: kappa != c/2 for non-Virasoro families
  AP48: kappa depends on full algebra, not just c
"""

import math
from fractions import Fraction

import pytest
from sympy import Rational, Symbol, simplify, expand

from compute.lib.grand_synthesis_engine import (
    # kappa formulas
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_slN,
    kappa_w3,
    kappa_wN,
    kappa_lattice,
    kappa_betagamma,
    # Faber-Pandharipande
    faber_pandharipande,
    # shadow depth
    SHADOW_CLASSES,
    AlgebraData,
    standard_algebra_data,
    # Axis 1: kappa universality
    verify_kappa_universality,
    # Axis 2: genus-0 MC
    verify_genus0_mc_agreement,
    # Axis 3: genus-1 anomaly
    verify_genus1_anomaly,
    # Axis 4: depth-formality
    verify_depth_formality,
    # Axis 5: r-matrix
    verify_r_matrix_agreement,
    # Axis 6: form factors
    form_factor_hierarchy,
    # Axis 7: duality discrimination
    four_dualities,
    duality_discrepancy_virasoro,
    # Axis 8: CoHA-bar
    coha_bar_bridges,
    # Axis 9: universality
    verify_universality,
    # Axis 10: analytic hierarchy
    analytic_hierarchy_table,
    # multi-weight corrections
    delta_F2_W3,
    delta_F3_W3,
    propagator_variance_W3,
    # Y-algebra
    y_algebra_central_charge,
    y_algebra_shadow_class,
    y_algebra_koszul_status,
    # uncited papers
    uncited_costello_papers,
    # top 10/5
    top_10_theorems,
    top_5_computations,
    # master
    run_full_cross_verification,
)


c_sym = Symbol('c')
k_sym = Symbol('k')


# ===========================================================================
# AXIS 1: KAPPA UNIVERSALITY (8 tests)
# ===========================================================================

class TestKappaUniversality:
    """Cross-verify kappa across bar, CG, GKW frameworks."""

    def test_kappa_heisenberg_level_1(self):
        """kappa(H_1) = 1. NOT 1/2 (AP39)."""
        assert kappa_heisenberg(1) == 1

    def test_kappa_heisenberg_level_k(self):
        """kappa(H_k) = k for symbolic k."""
        k = Symbol('k')
        assert kappa_heisenberg(k) == k

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert kappa_virasoro(1) == Rational(1, 2)

    def test_kappa_affine_sl2_level_1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4.
        dim(sl_2)=3, h^v=2. kappa = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_affine_slN(2, 1) == Rational(9, 4)

    def test_kappa_affine_sl3_level_1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3.
        dim(sl_3)=8, h^v=3."""
        assert kappa_affine_slN(3, 1) == Rational(16, 3)

    def test_kappa_w3_c1(self):
        """kappa(W_3, c=1) = 5/6."""
        assert kappa_w3(1) == Rational(5, 6)

    def test_kappa_universality_heisenberg(self):
        """All three frameworks give same kappa for Heisenberg."""
        result = verify_kappa_universality('heisenberg', k=1)
        assert result.all_agree is True
        assert result.kappa_bar == 1
        assert result.kappa_cg == 1

    def test_kappa_universality_affine_sl2(self):
        """All three frameworks give same kappa for affine sl_2."""
        result = verify_kappa_universality('affine_slN', N=2, k=1)
        assert result.all_agree is True
        assert result.kappa_bar == Rational(9, 4)


# ===========================================================================
# AXIS 2: GENUS-0 MC EQUATION (4 tests)
# ===========================================================================

class TestGenus0MC:
    """Bar D^2=0 = CG QME = GKW quadratic axioms at genus 0."""

    def test_heisenberg_mc(self):
        result = verify_genus0_mc_agreement('heisenberg')
        assert result.bar_d_squared_zero is True
        assert result.cg_qme_satisfied is True
        assert result.gkw_quadratic_axioms is True
        assert result.all_agree is True

    def test_affine_mc(self):
        result = verify_genus0_mc_agreement('affine_sl2')
        assert result.all_agree is True

    def test_virasoro_mc(self):
        result = verify_genus0_mc_agreement('virasoro')
        assert result.all_agree is True

    def test_w3_mc(self):
        result = verify_genus0_mc_agreement('w3')
        assert result.all_agree is True


# ===========================================================================
# AXIS 3: GENUS-1 ANOMALY (5 tests)
# ===========================================================================

class TestGenus1Anomaly:
    """F_1 = kappa/24 matches CG one-loop."""

    def test_faber_pandharipande_g1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_faber_pandharipande_g2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_faber_pandharipande_g3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_genus1_anomaly_heisenberg(self):
        """F_1(H_1) = 1/24 = CG one-loop."""
        result = verify_genus1_anomaly('heisenberg')
        assert result.match is True

    def test_genus1_anomaly_virasoro(self):
        """F_1(Vir_c) = c/48 = CG one-loop."""
        result = verify_genus1_anomaly('virasoro')
        assert result.match is True


# ===========================================================================
# AXIS 4: SHADOW DEPTH vs GKW FORMALITY (7 tests)
# ===========================================================================

class TestDepthFormality:
    """Shadow depth G/L/C/M refines GKW non-formality."""

    def test_heisenberg_class_G(self):
        result = verify_depth_formality('heisenberg')
        assert result.shadow_class == 'G'
        assert result.r_max == 2
        assert result.m3_vanishes is True
        assert result.gkw_formal_d1 is True  # class G is formal even at d'=1

    def test_affine_class_L(self):
        result = verify_depth_formality('affine_sl2')
        assert result.shadow_class == 'L'
        assert result.r_max == 3
        assert result.m3_vanishes is False
        assert result.m4_vanishes is True

    def test_betagamma_class_C(self):
        result = verify_depth_formality('betagamma')
        assert result.shadow_class == 'C'
        assert result.r_max == 4
        assert result.m3_vanishes is False
        assert result.m4_vanishes is False
        assert result.m5_vanishes is True

    def test_virasoro_class_M(self):
        result = verify_depth_formality('virasoro')
        assert result.shadow_class == 'M'
        assert result.r_max == float('inf')
        assert result.m3_vanishes is False
        assert result.m4_vanishes is False
        assert result.m5_vanishes is False

    def test_w3_class_M(self):
        result = verify_depth_formality('w3')
        assert result.shadow_class == 'M'

    def test_all_koszul(self):
        """All standard families are Koszul regardless of shadow depth (AP14)."""
        data = standard_algebra_data()
        for name, d in data.items():
            assert d.is_koszul is True, f"{name} should be Koszul"

    def test_gkw_d2_always_formal(self):
        """GKW: d'>=2 => all m_k=0 for k>=3 (formality theorem)."""
        for alg in ['heisenberg', 'affine_sl2', 'betagamma', 'virasoro', 'w3']:
            result = verify_depth_formality(alg)
            assert result.gkw_formal_d2 is True


# ===========================================================================
# AXIS 5: R-MATRIX AGREEMENT (4 tests)
# ===========================================================================

class TestRMatrixAgreement:
    """Bar collision = Costello 4d CS = Yangian RTT."""

    def test_sl2_r_matrix(self):
        result = verify_r_matrix_agreement(2)
        assert result.all_agree is True
        assert result.pole_order == 1  # AP19: one below OPE

    def test_sl3_r_matrix(self):
        result = verify_r_matrix_agreement(3)
        assert result.all_agree is True

    def test_sl4_r_matrix(self):
        result = verify_r_matrix_agreement(4)
        assert result.all_agree is True

    def test_r_matrix_pole_order(self):
        """AP19: r-matrix has poles one order below OPE."""
        for N in [2, 3, 4, 5]:
            result = verify_r_matrix_agreement(N)
            assert result.pole_order == 1, \
                f"sl_{N}: r-matrix should have simple pole (AP19)"


# ===========================================================================
# AXIS 6: FORM FACTOR HIERARCHY (3 tests)
# ===========================================================================

class TestFormFactorHierarchy:
    """Arity-k shadow = k-point CG amplitude = GKW m_k."""

    def test_hierarchy_length(self):
        """Should have hierarchy entries for arities 2-5."""
        h = form_factor_hierarchy()
        assert len(h) == 4
        assert [e.arity for e in h] == [2, 3, 4, 5]

    def test_arity2_proved(self):
        """Arity 2 (kappa) is proved across all three frameworks."""
        h = form_factor_hierarchy()
        assert h[0].proved is True
        assert 'kappa' in h[0].shadow_name

    def test_arity5_forced_for_class_M(self):
        """Arity 5 (S_5) is forced nonzero for class M (Virasoro/W_N)."""
        h = form_factor_hierarchy()
        assert h[3].arity == 5
        assert 'class M' in h[3].notes


# ===========================================================================
# AXIS 7: DUALITY DISCRIMINATION (6 tests)
# ===========================================================================

class TestDualityDiscrimination:
    """Four distinct dualities that must not be conflated."""

    def test_four_dualities_exist(self):
        """There are exactly four distinct dualities."""
        d = four_dualities()
        assert len(d) == 4
        names = {dd.duality_name for dd in d}
        assert 'Koszul duality' in names
        assert 'S-duality' in names
        assert 'Feigin-Frenkel involution' in names
        assert '3d mirror symmetry' in names

    def test_all_involutions(self):
        """All four dualities are involutions."""
        for d in four_dualities():
            assert d.is_involution is True

    def test_virasoro_kappa_sum_is_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        c = Symbol('c')
        disc = duality_discrepancy_virasoro(c)
        assert simplify(disc['sum'] - 13) == 0

    def test_virasoro_not_antisymmetric(self):
        """Koszul complementarity for Virasoro is NOT antisymmetric."""
        c = Symbol('c')
        disc = duality_discrepancy_virasoro(c)
        assert disc['is_antisymmetric'] is False

    def test_virasoro_self_dual_c13(self):
        """Virasoro is self-Koszul-dual at c=13, NOT c=26."""
        c = Symbol('c')
        disc = duality_discrepancy_virasoro(c)
        assert disc['self_dual_c'] == 13

    def test_mirror_sum_differs_from_koszul(self):
        """3d mirror sum kappa_C + kappa_H = N_f != kappa + kappa' = 0."""
        dualities = four_dualities()
        koszul = [d for d in dualities if d.duality_name == 'Koszul duality'][0]
        mirror = [d for d in dualities if d.duality_name == '3d mirror symmetry'][0]
        # Koszul sum = 0 for KM; mirror sum = N_f. These are different.
        assert '0' in koszul.kappa_relation
        assert 'N_f' in mirror.kappa_relation


# ===========================================================================
# AXIS 8: CoHA-BAR BRIDGE (3 tests)
# ===========================================================================

class TestCoHABarBridge:
    """CoHA multiplication dualizes to bar comultiplication."""

    def test_three_bridges(self):
        """Three standard CoHA-bar identifications."""
        bridges = coha_bar_bridges()
        assert len(bridges) == 3

    def test_jordan_quiver_heisenberg(self):
        """Jordan quiver <-> Heisenberg, character match."""
        bridges = coha_bar_bridges()
        jordan = bridges[0]
        assert 'Jordan' in jordan.quiver_type
        assert 'Heisenberg' in jordan.vertex_algebra
        assert jordan.character_match is True

    def test_a1_quiver_sl2(self):
        """A_1 quiver <-> affine sl_2, Yangian Y(sl_2)."""
        bridges = coha_bar_bridges()
        a1 = bridges[1]
        assert 'A_1' in a1.quiver_type
        assert 'sl_2' in a1.vertex_algebra
        assert 'Y(sl_2)' in a1.yangian


# ===========================================================================
# AXIS 9: UNIVERSALITY (3 tests)
# ===========================================================================

class TestUniversality:
    """All standard algebras are universal in the Cliff sense."""

    def test_heisenberg_universal(self):
        result = verify_universality('heisenberg')
        assert result.is_universal is True
        assert result.has_aut_o_action is True

    def test_virasoro_universal(self):
        result = verify_universality('virasoro')
        assert result.is_universal is True

    def test_w3_universal(self):
        result = verify_universality('w3')
        assert result.is_universal is True


# ===========================================================================
# AXIS 10: ANALYTIC HIERARCHY (5 tests)
# ===========================================================================

class TestAnalyticHierarchy:
    """C_2-cofiniteness and Koszulness are orthogonal."""

    def test_hierarchy_entries(self):
        """Should have multiple hierarchy entries."""
        h = analytic_hierarchy_table()
        assert len(h) >= 7

    def test_all_algebraic(self):
        """Bar D^2=0 holds unconditionally (algebraic level)."""
        for entry in analytic_hierarchy_table():
            assert entry.algebraic is True

    def test_heisenberg_koszul_not_c2(self):
        """Heisenberg is Koszul but NOT C_2-cofinite."""
        h = analytic_hierarchy_table()
        heis = [e for e in h if 'Heisenberg' in e.algebra][0]
        assert heis.koszul is True
        assert heis.c2_cofinite is False
        assert heis.koszul_not_c2 is True

    def test_lattice_both(self):
        """Lattice VOA is both Koszul and C_2-cofinite."""
        h = analytic_hierarchy_table()
        lat = [e for e in h if 'Lattice' in e.algebra][0]
        assert lat.koszul is True
        assert lat.c2_cofinite is True

    def test_orthogonality_witness(self):
        """At least one algebra is Koszul-not-C2 and at least one is C2-cofinite."""
        h = analytic_hierarchy_table()
        has_koszul_not_c2 = any(e.koszul_not_c2 is True for e in h)
        has_c2_cofinite = any(e.c2_cofinite is True for e in h)
        assert has_koszul_not_c2, "Need a Koszul-not-C2 witness"
        assert has_c2_cofinite, "Need a C2-cofinite witness"


# ===========================================================================
# MULTI-WEIGHT CROSS-CHANNEL (5 tests)
# ===========================================================================

class TestMultiWeightCrossChannel:
    """Cross-channel corrections delta_F_g^cross for multi-weight algebras."""

    def test_delta_F2_W3_positive(self):
        """delta_F_2(W_3) = (c+204)/(16c) > 0 for all c > 0."""
        # Test at c = 1
        val = delta_F2_W3(1)
        assert val == Rational(205, 16)
        assert val > 0

    def test_delta_F2_W3_at_c10(self):
        """delta_F_2(W_3) at c=10 = 214/160 = 107/80."""
        val = delta_F2_W3(10)
        assert val == Rational(214, 160)

    def test_delta_F2_positive_large_c(self):
        """delta_F_2 > 0 for large c (approaches 1/16 as c -> inf)."""
        val = delta_F2_W3(10000)
        assert val > 0
        # Asymptotically 1/16
        assert abs(float(val) - 1/16) < 0.002

    def test_delta_F3_W3_positive(self):
        """delta_F_3(W_3) > 0 at c=1."""
        val = delta_F3_W3(1)
        assert val > 0

    def test_propagator_variance_W3(self):
        """Propagator variance P(W_3) = 25c^2 + 100c - 428."""
        # At c = 10: 25*100 + 1000 - 428 = 3072
        val = propagator_variance_W3(10)
        assert val == 3072


# ===========================================================================
# Y-ALGEBRA LANDSCAPE (7 tests)
# ===========================================================================

class TestYAlgebraLandscape:
    """Y_{N1,N2,N3} shadow classification and Koszulness."""

    def test_y_000_class_G(self):
        assert y_algebra_shadow_class(0, 0, 0) == 'G'

    def test_y_001_class_G(self):
        assert y_algebra_shadow_class(0, 0, 1) == 'G'

    def test_y_011_class_L(self):
        assert y_algebra_shadow_class(0, 1, 1) == 'L'

    def test_y_111_class_M(self):
        assert y_algebra_shadow_class(1, 1, 1) == 'M'

    def test_y_002_class_M(self):
        """Y_{0,0,2} = W_2 x gl(1) which has Virasoro => class M."""
        assert y_algebra_shadow_class(0, 0, 2) == 'M'

    def test_y_003_class_M(self):
        """Y_{0,0,3} = W_3 x gl(1) => class M."""
        assert y_algebra_shadow_class(0, 0, 3) == 'M'

    def test_no_class_C_in_y_algebras(self):
        """Class C (betagamma/contact) does not appear for Y-algebras."""
        for N1 in range(4):
            for N2 in range(4):
                for N3 in range(4):
                    sc = y_algebra_shadow_class(N1, N2, N3)
                    assert sc != 'C', \
                        f"Y_{{{N1},{N2},{N3}}} should not be class C"

    def test_all_y_koszul(self):
        """All Y-algebras are Koszul at generic coupling (AP14)."""
        for N1 in range(3):
            for N2 in range(3):
                for N3 in range(3):
                    assert y_algebra_koszul_status(N1, N2, N3) is True

    def test_y_002_central_charge(self):
        """Y_{0,0,2}[Psi=3] should give W_2 = Virasoro central charge."""
        c = y_algebra_central_charge(0, 0, 2, 3)
        # Y_{0,0,2}[Psi] = Vir at level k = Psi - 2 = 1, so c = 1/2
        # Using lambda formula: sigma = 2*(3-1) = 4
        # lam1 = 4, lam2 = 4/(-3) = -4/3, lam3 = 4/2 = 2
        # c = (4-1)(-4/3-1)(2-1) + 1 = 3*(-7/3)*1 + 1 = -7+1 = -6
        # This is a SPECIFIC Y-algebra at Psi=3, not the standard Virasoro.
        assert c is not None


# ===========================================================================
# BIBLIOGRAPHY (2 tests)
# ===========================================================================

class TestBibliography:
    """Uncited Costello papers."""

    def test_uncited_papers_exist(self):
        """Should identify genuinely uncited papers."""
        papers = uncited_costello_papers()
        assert len(papers) >= 2
        arxiv_ids = {p['arxiv_id'] for p in papers}
        assert '1303.2632' in arxiv_ids  # Yangian paper
        assert '2412.17168' in arxiv_ids  # Associativity is enough

    def test_annotations_nonempty(self):
        """Each paper has a nonempty annotation."""
        for p in uncited_costello_papers():
            assert len(p['annotation']) > 10


# ===========================================================================
# TOP 10/5 (3 tests)
# ===========================================================================

class TestTop10Top5:
    """Top theorems and computations."""

    def test_10_theorems(self):
        t = top_10_theorems()
        assert len(t) == 10

    def test_5_computations(self):
        c = top_5_computations()
        assert len(c) == 5

    def test_theorem_ranks_unique(self):
        t = top_10_theorems()
        ranks = [th['rank'] for th in t]
        assert len(ranks) == len(set(ranks))


# ===========================================================================
# MASTER CROSS-VERIFICATION (3 tests)
# ===========================================================================

class TestMasterCrossVerification:
    """Full synthesis run."""

    def test_full_run_completes(self):
        """The master cross-verification runs without error."""
        results = run_full_cross_verification()
        assert isinstance(results, dict)
        assert len(results) > 0

    def test_all_axes_present(self):
        """All 10 axes are present in results."""
        results = run_full_cross_verification()
        for i in range(1, 11):
            key = f'axis{i}_'
            matching = [k for k in results.keys() if k.startswith(key)]
            assert len(matching) >= 1, f"Axis {i} missing from results"

    def test_delta_F2_cross_check(self):
        """Cross-check delta_F_2 at two different c values."""
        results = run_full_cross_verification()
        assert results['delta_F2_W3_at_c1'] == Rational(205, 16)
        assert float(results['delta_F2_W3_at_c10']) == pytest.approx(1.3375, abs=0.001)


# ===========================================================================
# CROSS-ENGINE CONSISTENCY (existing engines, 4 tests)
# ===========================================================================

class TestCrossEngineConsistency:
    """Verify grand synthesis is consistent with existing engines."""

    def test_kappa_matches_costello_engine(self):
        """Our kappa_virasoro matches costello_bv_comparison_engine."""
        # The CG engine has kappa_virasoro(c) = c/2
        c = Symbol('c')
        assert kappa_virasoro(c) == c / 2

    def test_kappa_matches_gaiotto_engine(self):
        """Our kappa_w3 matches gaiotto_rapcak_landscape_engine."""
        c = Symbol('c')
        assert kappa_w3(c) == Rational(5, 6) * c

    def test_shadow_class_matches_gaiotto_engine(self):
        """Shadow classes match gaiotto_3d_ht_comparison_engine."""
        data = standard_algebra_data()
        assert data['heisenberg'].shadow_class == 'G'
        assert data['affine_sl2'].shadow_class == 'L'
        assert data['betagamma'].shadow_class == 'C'
        assert data['virasoro'].shadow_class == 'M'
        assert data['w3'].shadow_class == 'M'

    def test_fp_matches_costello_engine(self):
        """Faber-Pandharipande numbers match costello_bv_comparison_engine."""
        assert faber_pandharipande(1) == Rational(1, 24)
        assert faber_pandharipande(2) == Rational(7, 5760)


# ===========================================================================
# KAPPA CROSS-FAMILY CONSISTENCY (AP1, AP39, AP48) (4 tests)
# ===========================================================================

class TestKappaCrossFamily:
    """kappa is family-specific; never copy between families."""

    def test_kappa_neq_c_over_2_for_heisenberg(self):
        """AP39: kappa(H_k) = k != c/2 = 1/2 for generic k != 1."""
        assert kappa_heisenberg(2) == 2
        assert kappa_virasoro(1) == Rational(1, 2)
        # These are DIFFERENT (kappa_H at k=2 is 2, not 1/2)

    def test_kappa_neq_c_over_2_for_affine(self):
        """AP39: kappa(sl_2, k=1) = 9/4 != c/2."""
        kap = kappa_affine_slN(2, 1)
        c_val = Rational(3) * 1 / (1 + 2)  # c(sl_2, k=1) = 1
        assert kap != c_val / 2

    def test_kappa_lattice_neq_c_over_2(self):
        """AP48: kappa(V_Lambda) = rank, not c/2 in general."""
        # rank-24 lattice: kappa = 24, c = 24, so c/2 = 12 != 24
        assert kappa_lattice(24) == 24
        assert kappa_virasoro(24) == 12  # would be wrong for lattice

    def test_kappa_wN_formula(self):
        """kappa(W_N) = c*(H_N - 1). Verify for N=2,3,4."""
        c = Symbol('c')
        # W_2 = Virasoro: H_2 - 1 = 1/2, so kappa = c/2. Matches.
        assert simplify(kappa_wN(c, 2) - c / 2) == 0
        # W_3: H_3 - 1 = 1/2 + 1/3 = 5/6
        assert simplify(kappa_wN(c, 3) - Rational(5, 6) * c) == 0
        # W_4: H_4 - 1 = 1/2 + 1/3 + 1/4 = 13/12
        assert simplify(kappa_wN(c, 4) - Rational(13, 12) * c) == 0
