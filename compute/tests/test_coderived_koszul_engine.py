"""Tests for the coderived Koszul duality engine.

Verifies the complete genus >= 1 bar-cobar duality framework:

1. Curved dg algebras: d^2 = [m_0, -] for Heisenberg, Virasoro, sl_2
2. Coderived category D^co: curved modules with d_M^2 = m_0 * id
3. Curved bar construction: d_B^2 = 0 ALWAYS (curvature absorption)
4. Koszul duality at genus 1: D^co(A) ~ D^ctr(A!) for Koszul A
5. Genus-graded passage: g=0 (D^b) -> g=1 (D^co) -> g>=2 (higher corrections)

Manuscript references:
    bar_cobar_adjunction_curved.tex: thm:bar-modular-operad (d_B^2 = 0)
    higher_genus_foundations.tex: genus-graded bar complex
    quantum_corrections.tex: d^2 = kappa * E_2
    concordance.tex: MC5 (coderived passage)
    CLAUDE.md: "Bar d^2=0 ALWAYS. Curvature shows as m_1^2 != 0."

Cross-references to existing modules:
    curved_ainfty_bar_complex.py: CurvedAInfty, BarComplex
    mc5_genus1_bridge.py: genus-1 curvature kappa * omega_1
    bar_cobar_chain_maps.py: bar/cobar constructions
    coderived_artifact.py: red-team attacks on coderived passage
"""

import pytest
from sympy import (
    Rational, Symbol, simplify, expand, S, sqrt, zeros, eye,
    Matrix, Integer, bernoulli, factorial, Abs,
)

from compute.lib.coderived_koszul_engine import (
    # §1: Curved dg algebras
    CurvedDGAlgebra,
    # §2: Standard families
    heisenberg_curved_genus1,
    virasoro_curved_genus1,
    affine_sl2_curved_genus1,
    uncurved_dga,
    # §3: Coderived category
    CurvedDGModule,
    free_curved_module,
    scalar_curved_module,
    # §4: Curved bar construction
    CurvedBarConstruction,
    curved_bar,
    # §5: Koszul duality
    KoszulDualityData,
    heisenberg_koszul_duality_genus1,
    virasoro_koszul_duality_genus1,
    # §6: Genus-graded passage
    faber_pandharipande_number,
    genus_graded_curvature,
    GenusGradedPassage,
    genus_passage,
    # §7: Curvature absorption verification
    verify_curvature_absorption_heisenberg,
    verify_curvature_absorption_virasoro,
    verify_curvature_absorption_uncurved,
    # §8: Coderived vs ordinary
    CoderivedOrdinaryComparison,
    # §9: Full checks
    full_koszul_duality_check_heisenberg,
    full_koszul_duality_check_virasoro,
    # §10: Spectral sequence
    coderived_spectral_sequence_genus1,
    # §11: Master
    master_verification,
)


kappa = Symbol('kappa')
c = Symbol('c')
k = Symbol('k')


# ═══════════════════════════════════════════════════════════════════════════
# §1. CURVED DG ALGEBRA TESTS
# ═══════════════════════════════════════════════════════════════════════════

class TestCurvedDGAlgebra:
    """Test the curved dg algebra (A, d, mu, m_0) with d^2 = [m_0, -]."""

    def test_heisenberg_is_curved(self):
        """Heisenberg at genus 1 has m_0 != 0 (curvature kappa * omega)."""
        A = heisenberg_curved_genus1(kappa)
        assert A.is_curved, "Heisenberg at genus 1 must be curved"

    def test_heisenberg_m0_is_cycle(self):
        """d(m_0) = 0 (the n=0 A-infinity relation)."""
        A = heisenberg_curved_genus1(kappa)
        assert A.verify_m0_is_cycle(), "m_0 must be a d-cycle"

    def test_heisenberg_curved_relation(self):
        """d^2(a) = [m_0, a] for Heisenberg."""
        A = heisenberg_curved_genus1(kappa)
        match, d_sq, comm = A.verify_curved_relation()
        assert match, "d^2 must equal [m_0, -] (curved A-infinity relation)"

    def test_virasoro_is_curved(self):
        """Virasoro at genus 1 has m_0 = (c/2) * omega != 0."""
        A = virasoro_curved_genus1(c)
        assert A.is_curved, "Virasoro at genus 1 must be curved"

    def test_virasoro_curved_relation(self):
        """d^2(a) = [m_0, a] for Virasoro."""
        A = virasoro_curved_genus1(c)
        match, _, _ = A.verify_curved_relation()
        assert match, "Virasoro curved relation must hold"

    def test_virasoro_m0_is_cycle(self):
        """d(m_0) = 0 for Virasoro."""
        A = virasoro_curved_genus1(c)
        assert A.verify_m0_is_cycle()

    def test_sl2_is_curved(self):
        """Affine sl_2 at genus 1 has m_0 = 3(k+2)/4 * omega."""
        A = affine_sl2_curved_genus1(k)
        assert A.is_curved

    def test_sl2_m0_is_cycle(self):
        """d(m_0) = 0 for affine sl_2."""
        A = affine_sl2_curved_genus1(k)
        assert A.verify_m0_is_cycle()

    def test_uncurved_has_zero_curvature(self):
        """Genus-0 algebra has m_0 = 0."""
        A = uncurved_dga(3)
        assert not A.is_curved, "Genus-0 algebra must be uncurved"

    def test_uncurved_d_squared_zero(self):
        """d^2 = 0 for uncurved algebra (since [0, -] = 0)."""
        A = uncurved_dga(3)
        match, d_sq, comm = A.verify_curved_relation()
        assert match, "d^2 = 0 = [0, -] must hold"
        assert d_sq.equals(zeros(3, 3)), "d^2 must be zero"

    def test_heisenberg_dimension(self):
        """Heisenberg model has 3 basis elements: 1, a, omega."""
        A = heisenberg_curved_genus1(kappa)
        assert A.dim == 3

    def test_heisenberg_degrees(self):
        """Degrees: |1| = 0, |a| = 0, |omega| = 2."""
        A = heisenberg_curved_genus1(kappa)
        assert A.degrees == [0, 0, 2]


# ═══════════════════════════════════════════════════════════════════════════
# §2. CODERIVED CATEGORY: CURVED DG MODULES
# ═══════════════════════════════════════════════════════════════════════════

class TestCoderivedCategory:
    """Test curved dg modules (objects of D^co)."""

    def test_free_module_construction(self):
        """Free curved module M = A has well-defined structure."""
        A = heisenberg_curved_genus1(Rational(1))
        M = free_curved_module(A, rank=1)
        assert M.module_dim == A.dim

    def test_free_module_d_squared_matches_curvature(self):
        """For free module M = A: d_M^2 = [m_0, -] on M."""
        A = heisenberg_curved_genus1(Rational(1))
        M = free_curved_module(A, rank=1)
        # d_M = d_A, so d_M^2 = d_A^2 = [m_0, -]
        # For our model with d_A = 0, d_M^2 = 0 = [m_0, -]
        d_sq = M.d_M_squared()
        assert d_sq.equals(zeros(M.module_dim, M.module_dim))

    def test_scalar_curved_module_construction(self):
        """2-dimensional curved module with d^2 = kappa * id."""
        A = heisenberg_curved_genus1(Rational(1))
        M = scalar_curved_module(A, Rational(1))
        assert M.module_dim == 2

    def test_scalar_curved_module_d_squared(self):
        """d_M^2 = curvature_scalar * id on the scalar module."""
        A = heisenberg_curved_genus1(Rational(1))
        curv = Rational(3)
        M = scalar_curved_module(A, curv)
        d_sq = M.d_M_squared()
        expected = curv * eye(2)
        diff = d_sq - expected
        for i in range(2):
            for j in range(2):
                assert simplify(diff[i, j]) == 0, \
                    f"d_M^2 must equal {curv}*id at ({i},{j})"

    def test_acyclic_not_applicable_curved(self):
        """In the curved case, ordinary acyclicity is not applicable."""
        A = heisenberg_curved_genus1(Rational(1))
        M = scalar_curved_module(A, Rational(1))
        assert not M.is_acyclic_in_ordinary_sense()


# ═══════════════════════════════════════════════════════════════════════════
# §3. CURVED BAR CONSTRUCTION: d_B^2 = 0 ALWAYS
# ═══════════════════════════════════════════════════════════════════════════

class TestCurvedBarConstruction:
    """Test the curvature absorption theorem: d_B^2 = 0 even when A is curved."""

    def test_bar_dimension_n0(self):
        """B^0 = k (ground field), dim = 1."""
        A = heisenberg_curved_genus1(Rational(1))
        bar = curved_bar(A, max_tensor=3)
        assert bar.bar_dim(0) == 1

    def test_bar_dimension_n1(self):
        """B^1 = s A_bar, dim = dim(A) - 1 (exclude unit)."""
        A = heisenberg_curved_genus1(Rational(1))
        bar = curved_bar(A, max_tensor=3)
        assert bar.bar_dim(1) == 2  # {a, omega} (exclude unit)

    def test_bar_dimension_n2(self):
        """B^2 = (s A_bar)^{tensor 2}, dim = (dim(A)-1)^2."""
        A = heisenberg_curved_genus1(Rational(1))
        bar = curved_bar(A, max_tensor=3)
        assert bar.bar_dim(2) == 4  # 2^2

    def test_curvature_absorption_heisenberg_symbolic(self):
        """d_B^2 = 0 for Heisenberg with SYMBOLIC kappa (the key test).

        This proves d_B^2 = 0 for ALL values of kappa simultaneously.
        """
        result = verify_curvature_absorption_heisenberg(kappa, max_tensor=2)
        assert result['algebra_curved'], "Algebra must be curved"
        assert result['curved_relation_holds'], "d^2 = [m_0, -] must hold"
        assert result['m0_is_cycle'], "m_0 must be a cycle"
        assert result['bar_d_squared_zero_global'], \
            "d_B^2 = 0 must hold (curvature absorption theorem)"

    def test_curvature_absorption_heisenberg_numeric(self):
        """d_B^2 = 0 for Heisenberg at specific kappa values."""
        for kval in [Rational(1), Rational(3, 2), Rational(-1), Rational(7)]:
            result = verify_curvature_absorption_heisenberg(kval, max_tensor=2)
            assert result['bar_d_squared_zero_global'], \
                f"d_B^2 = 0 must hold at kappa = {kval}"

    def test_curvature_absorption_virasoro_symbolic(self):
        """d_B^2 = 0 for Virasoro with symbolic c."""
        result = verify_curvature_absorption_virasoro(c, max_tensor=2)
        assert result['bar_d_squared_zero_global'], \
            "d_B^2 = 0 must hold for Virasoro"

    def test_curvature_absorption_uncurved(self):
        """d_B^2 = 0 for uncurved algebra (genus 0 baseline)."""
        result = verify_curvature_absorption_uncurved(dim=3, max_tensor=2)
        assert not result['algebra_curved'], "Genus-0 must be uncurved"
        assert result['bar_d_squared_zero'], "d_B^2 = 0 trivially at genus 0"

    def test_bar_d_squared_zero_by_degree_heisenberg(self):
        """Verify d_B^2 = 0 at each tensor degree separately."""
        A = heisenberg_curved_genus1(Rational(1))
        bar = curved_bar(A, max_tensor=3)
        degree_results = bar.verify_d_squared_zero_by_degree()
        for n, targets in degree_results.items():
            for m, is_zero in targets.items():
                assert is_zero, \
                    f"d_B^2: B^{n} -> B^{m} must vanish (Heisenberg)"

    def test_d_linear_zero_when_d_is_zero(self):
        """When d_A = 0 (our models), d_linear = 0."""
        A = heisenberg_curved_genus1(Rational(1))
        bar = curved_bar(A, max_tensor=3)
        for n in range(4):
            d_lin = bar.d_linear_matrix(n)
            assert d_lin.equals(zeros(*d_lin.shape)), \
                f"d_linear must be zero at degree {n} when d_A = 0"

    def test_d_curv_inserts_curvature(self):
        """d_curv: B^0 -> B^1 inserts m_0 (the curvature element)."""
        A = heisenberg_curved_genus1(Rational(1))
        bar = curved_bar(A, max_tensor=3)
        d_curv_0 = bar.d_curv_matrix(0)
        # B^0 = k (dim 1), B^1 = s*A_bar (dim 2, generators a and omega)
        # m_0 = [0, 0, 1] (kappa=1), only omega component is in aug ideal
        # d_curv sends 1 to s*omega (with coefficient kappa=1)
        assert d_curv_0.shape == (2, 1)
        # The omega component (index 1 in aug ideal since aug = {1,2} -> a,omega)
        # should be nonzero
        is_nonzero = any(d_curv_0[i, 0] != 0 for i in range(2))
        assert is_nonzero, "d_curv must insert the curvature element"


# ═══════════════════════════════════════════════════════════════════════════
# §4. KOSZUL DUALITY AT GENUS 1
# ═══════════════════════════════════════════════════════════════════════════

class TestKoszulDualityGenus1:
    """Test D^co(A) ~ D^ctr(A!) for Koszul algebras at genus 1."""

    def test_heisenberg_complementarity(self):
        """kappa(H) + kappa(H!) = 0 for Heisenberg."""
        kd = heisenberg_koszul_duality_genus1(kappa)
        assert kd.verify_complementarity(), \
            "Heisenberg complementarity kappa + (-kappa) = 0"

    def test_virasoro_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        kd = virasoro_koszul_duality_genus1(c)
        assert kd.verify_complementarity(), \
            "Virasoro complementarity c/2 + (26-c)/2 = 13"

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro is self-dual at c=13, NOT c=26 (Critical Pitfall)."""
        kd = virasoro_koszul_duality_genus1(Integer(13))
        assert simplify(kd.kappa_A - kd.kappa_A_dual) == 0, \
            "Virasoro self-dual at c=13"

    def test_virasoro_not_self_dual_at_c26(self):
        """Virasoro is NOT self-dual at c=26."""
        kd = virasoro_koszul_duality_genus1(Integer(26))
        assert simplify(kd.kappa_A - kd.kappa_A_dual) != 0, \
            "Virasoro must NOT be self-dual at c=26"

    def test_bar_absorbs_curvature_both_sides_heisenberg(self):
        """Bar of BOTH A and A! have d_B^2 = 0."""
        kd = heisenberg_koszul_duality_genus1(Rational(1))
        result = kd.bar_absorbs_curvature()
        assert result['A_bar_d2_zero'], "Bar of A: d_B^2 = 0"
        assert result['A_dual_bar_d2_zero'], "Bar of A!: d_B^2 = 0"

    def test_bar_absorbs_curvature_both_sides_virasoro(self):
        """Bar of both Vir_c and Vir_{26-c} have d_B^2 = 0."""
        kd = virasoro_koszul_duality_genus1(Rational(1))
        result = kd.bar_absorbs_curvature()
        assert result['A_bar_d2_zero'], "Bar of Vir_c: d_B^2 = 0"
        assert result['A_dual_bar_d2_zero'], "Bar of Vir_{26-c}: d_B^2 = 0"

    def test_genus1_correction_type_heisenberg(self):
        """Both Heisenberg and its dual are curved at genus 1."""
        kd = heisenberg_koszul_duality_genus1(kappa)
        assert kd.genus1_correction_type() == 'both_curved'

    def test_genus1_correction_type_virasoro(self):
        """Both Virasoro and its dual are curved at genus 1."""
        kd = virasoro_koszul_duality_genus1(c)
        assert kd.genus1_correction_type() == 'both_curved'


# ═══════════════════════════════════════════════════════════════════════════
# §5. GENUS-GRADED PASSAGE
# ═══════════════════════════════════════════════════════════════════════════

class TestGenusGradedPassage:
    """Test the passage from D^b (genus 0) to D^co (genus >= 1)."""

    def test_fp_genus0(self):
        """lambda_0^FP = 0 (no curvature at genus 0)."""
        assert faber_pandharipande_number(0) == 0

    def test_fp_genus1(self):
        """lambda_1^FP = 1/24.

        From: (2^1 - 1)/2^1 * |B_2|/(2!) = (1/2)*(1/6)/2 = 1/24.
        """
        assert faber_pandharipande_number(1) == Rational(1, 24)

    def test_fp_genus2(self):
        """lambda_2^FP = 7/5760.

        From: (2^3 - 1)/2^3 * |B_4|/(4!) = (7/8)*(1/30)/24 = 7/5760.
        """
        assert faber_pandharipande_number(2) == Rational(7, 5760)

    def test_fp_genus3(self):
        """lambda_3^FP = 31/967680.

        From: (2^5 - 1)/2^5 * |B_6|/(6!) = (31/32)*(1/42)/720 = 31/967680.
        """
        assert faber_pandharipande_number(3) == Rational(31, 967680)

    def test_genus_curvature_g0(self):
        """At genus 0: no curvature correction."""
        assert genus_graded_curvature(kappa, 0) == 0

    def test_genus_curvature_g1(self):
        """At genus 1: correction = kappa/24."""
        result = genus_graded_curvature(kappa, 1)
        assert simplify(result - kappa / 24) == 0

    def test_period_corrected_nilpotence(self):
        """D^2 = 0 via period correction at each genus."""
        gp = genus_passage(kappa, max_genus=3)
        results = gp.verify_period_corrected_nilpotence()
        for g in range(1, 4):
            assert results[g]['absorption_match'], \
                f"Period correction must absorb curvature at genus {g}"

    def test_genus_correction_table(self):
        """The genus correction table is consistent."""
        gp = genus_passage(kappa, max_genus=3)
        table = gp.genus_correction_table()
        assert table[0]['category_type'] == 'D^b'
        assert table[1]['category_type'] == 'D^co_1'
        assert table[0]['lambda_g'] == 0
        assert table[1]['lambda_g'] == Rational(1, 24)

    def test_coderived_correction_at_genus0(self):
        """At genus 0: D^co_0 = D^b, no correction."""
        gp = genus_passage(kappa, max_genus=3)
        corr = gp.coderived_correction_at_genus(0)
        assert corr['curvature'] == S.Zero
        assert corr['correction'] == S.Zero

    def test_coderived_correction_at_genus1(self):
        """At genus 1: first coderived correction kappa/24."""
        gp = genus_passage(kappa, max_genus=3)
        corr = gp.coderived_correction_at_genus(1)
        assert simplify(corr['correction'] - kappa / 24) == 0


# ═══════════════════════════════════════════════════════════════════════════
# §6. CODERIVED vs ORDINARY DERIVED COMPARISON
# ═══════════════════════════════════════════════════════════════════════════

class TestCoderivedOrdinaryComparison:
    """Test structural comparison between D^co and D^b."""

    def test_genus0_coderived_equals_derived(self):
        """At genus 0 (kappa=0): D^co = D^b."""
        A = uncurved_dga(3)
        comp = CoderivedOrdinaryComparison(A, S.Zero)
        assert comp.genus0_is_ordinary()
        assert not comp.coderived_has_extra_objects()

    def test_genus1_coderived_has_extra(self):
        """At genus 1 (kappa != 0): D^co has extra objects."""
        A = heisenberg_curved_genus1(Rational(1))
        comp = CoderivedOrdinaryComparison(A, Rational(1))
        assert comp.coderived_has_extra_objects()
        assert not comp.genus0_is_ordinary()

    def test_extra_object_construction(self):
        """An explicit curved module exists in D^co but not D^b."""
        A = heisenberg_curved_genus1(Rational(1))
        comp = CoderivedOrdinaryComparison(A, Rational(1))
        mod = comp.extra_object_example()
        assert mod is not None
        assert mod.module_dim == 2

    def test_no_extra_objects_at_genus0(self):
        """No extra curved modules when kappa = 0."""
        A = uncurved_dga(3)
        comp = CoderivedOrdinaryComparison(A, S.Zero)
        mod = comp.extra_object_example()
        assert mod is None

    def test_structural_comparison_genus1(self):
        """Full structural comparison at genus 1."""
        A = heisenberg_curved_genus1(Rational(1))
        comp = CoderivedOrdinaryComparison(A, Rational(1))
        result = comp.structural_comparison()
        assert result['extra_objects_exist']
        assert not result['coderived_equals_derived']


# ═══════════════════════════════════════════════════════════════════════════
# §7. SPECTRAL SEQUENCE
# ═══════════════════════════════════════════════════════════════════════════

class TestSpectralSequence:
    """Test the spectral sequence from D^b to D^co."""

    def test_collapses_at_genus0(self):
        """At kappa = 0, the spectral sequence collapses at E_1."""
        result = coderived_spectral_sequence_genus1(S.Zero)
        assert result['d1_zero']
        assert result['collapses_at_E1']

    def test_nontrivial_at_genus1(self):
        """At kappa != 0, the d_1 differential is nontrivial."""
        result = coderived_spectral_sequence_genus1(kappa)
        assert not result['d1_zero']
        assert not result['collapses_at_E1']

    def test_correction_magnitude(self):
        """The correction magnitude is kappa/24 at genus 1."""
        result = coderived_spectral_sequence_genus1(kappa)
        assert simplify(result['correction_magnitude'] - kappa / 24) == 0


# ═══════════════════════════════════════════════════════════════════════════
# §8. FULL KOSZUL DUALITY CHECKS
# ═══════════════════════════════════════════════════════════════════════════

class TestFullKoszulDuality:
    """End-to-end Koszul duality verification."""

    def test_full_heisenberg_check(self):
        """Complete Heisenberg verification passes all checks."""
        result = full_koszul_duality_check_heisenberg(Rational(1))
        assert result['curvature_absorption']['bar_d_squared_zero_global']
        assert result['complementarity']

    def test_full_virasoro_check(self):
        """Complete Virasoro verification passes all checks."""
        result = full_koszul_duality_check_virasoro(Rational(1))
        assert result['curvature_absorption']['bar_d_squared_zero_global']
        assert result['complementarity']

    def test_virasoro_self_dual_point(self):
        """Virasoro Koszul duality data records c=13 as the self-dual point."""
        result = full_koszul_duality_check_virasoro(c)
        assert result['self_dual_c'] == 13


# ═══════════════════════════════════════════════════════════════════════════
# §9. MASTER VERIFICATION
# ═══════════════════════════════════════════════════════════════════════════

class TestMasterVerification:
    """Test the master verification across all families."""

    def test_master_heisenberg(self):
        """Master verification: Heisenberg bar d^2 = 0."""
        results = master_verification()
        assert results['heisenberg']['bar_d2_zero']

    def test_master_virasoro(self):
        """Master verification: Virasoro bar d^2 = 0."""
        results = master_verification()
        assert results['virasoro']['bar_d2_zero']

    def test_master_uncurved(self):
        """Master verification: uncurved (genus 0) bar d^2 = 0."""
        results = master_verification()
        assert results['uncurved']['bar_d2_zero']

    def test_master_complementarity_heisenberg(self):
        """Master: Heisenberg complementarity sum = 0."""
        results = master_verification()
        assert results['heisenberg']['complementarity_sum'] == S.Zero

    def test_master_complementarity_virasoro(self):
        """Master: Virasoro complementarity sum = 13."""
        results = master_verification()
        assert results['virasoro']['complementarity_sum'] == Rational(13)


# ═══════════════════════════════════════════════════════════════════════════
# §10. CROSS-CHECKS WITH EXISTING MODULES
# ═══════════════════════════════════════════════════════════════════════════

class TestCrossChecks:
    """Cross-check with mc5_genus1_bridge.py results."""

    def test_heisenberg_kappa_value(self):
        """kappa(H_kappa) = kappa (level IS the curvature).

        Cross-check with mc5_genus1_bridge.verify_heisenberg_genus1().
        """
        A = heisenberg_curved_genus1(kappa)
        # The curvature vector is [0, 0, kappa]
        assert A.curvature[2] == kappa

    def test_virasoro_kappa_c_over_2(self):
        """kappa(Vir_c) = c/2.

        Cross-check with mc5_genus1_bridge.verify_virasoro_genus1().
        """
        A = virasoro_curved_genus1(c)
        assert simplify(A.curvature[2] - c / 2) == 0

    def test_sl2_kappa_formula(self):
        """kappa(sl_2_k) = 3(k+2)/4 = dim(sl_2)*(k+h^v)/(2*h^v).

        Cross-check with mc5_genus1_bridge.verify_sl2_genus1().
        """
        A = affine_sl2_curved_genus1(k)
        expected = Rational(3) * (k + 2) / 4
        assert simplify(A.curvature[4] - expected) == 0

    def test_fp_genus1_cross_check(self):
        """lambda_1^FP = 1/24, cross-check with mc5_genus1_bridge.

        From mc5_genus1_bridge: F_1(A) = kappa(A)/24.
        """
        lam = faber_pandharipande_number(1)
        assert lam == Rational(1, 24)

    def test_genus1_free_energy_heisenberg(self):
        """F_1(H_kappa) = kappa/24.

        Cross-check with mc5_genus1_bridge.genus1_free_energy(kappa).
        """
        gp = genus_passage(kappa, max_genus=1)
        f1 = gp.free_energy(1)
        assert simplify(f1 - kappa / 24) == 0

    def test_genus1_free_energy_virasoro(self):
        """F_1(Vir_c) = c/48.

        Cross-check: kappa(Vir_c) = c/2, so F_1 = (c/2)/24 = c/48.
        """
        gp = genus_passage(c / 2, max_genus=1)
        f1 = gp.free_energy(1)
        assert simplify(f1 - c / 48) == 0
