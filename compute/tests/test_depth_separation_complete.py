r"""Comprehensive tests for arithmetic vs homotopy depth separation.

Verifies:
  1. Additivity: d = 1 + d_arith + d_alg for all families.
  2. Class G: d_alg = 0 for all Gaussian algebras.
  3. Class L: d_alg = 1 for all Lie/tree algebras.
  4. Class C: d_alg = 2 for betagamma.
  5. Class M: d_alg = infinity for all mixed algebras.
  6. Lattice d_arith: 2 + dim S_{r/2} for even unimodular.
  7. Ising d_arith = 0: constrained Epstein analysis.
  8. Minimal model d_arith = 0: Baker-type transcendence.
  9. d_arith stabilization: constant across shadow arity.
  10. Ising paradox resolution: all 5 layers.
  11. Genus-dependent arithmetic depth.
  12. Cusp form dimension verification.
  13. Minimal model data (conformal weights, scalar primaries).
  14. Cross-family consistency checks (AP10).

Mathematical references:
    thm:depth-decomposition (arithmetic_shadows.tex)
    prop:ising-d-arith (arithmetic_shadows.tex)
    thm:ainfty-formality-depth (arithmetic_shadows.tex)
    def:arithmetic-depth-filtration (arithmetic_shadows.tex)
    rem:homotopy-becomes-arithmetic (arithmetic_shadows.tex)
"""

from __future__ import annotations

import pytest
from sympy import Rational, oo, simplify

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from depth_separation_complete import (
    DepthSeparation,
    GenusArithmeticDepth,
    build_complete_table,
    class_summary,
    constrained_epstein_terms,
    constrained_epstein_zeros_on_critical_line,
    d_arith_stabilization_analysis,
    depth_affine_km,
    depth_betagamma,
    depth_free_fermion,
    depth_heisenberg,
    depth_lattice,
    depth_virasoro_3state_potts,
    depth_virasoro_generic,
    depth_virasoro_ising,
    depth_virasoro_minimal,
    depth_virasoro_tricritical,
    depth_wN_at_c2,
    depth_wN_generic,
    dim_cusp_forms_sl2z,
    genus_arithmetic_depth_ising,
    genus_arithmetic_depth_leech,
    ising_paradox_analysis,
    minimal_model_central_charge,
    minimal_model_conformal_weights,
    minimal_model_n_primaries,
    minimal_model_scalar_primaries,
    print_table,
    verify_all_additivity,
)


# ========================================================================
# 1. Additivity: d = 1 + d_arith + d_alg
# ========================================================================

class TestAdditivity:
    """Verify d = 1 + d_arith + d_alg for all families."""

    def test_all_entries_satisfy_additivity(self):
        """Every entry in the complete table satisfies additivity."""
        table = build_complete_table()
        results = verify_all_additivity(table)
        for name, ok in results.items():
            assert ok, f"Additivity failed for {name}"

    def test_class_G_additivity(self):
        """Class G: d_alg = 0, so d = 1 + d_arith."""
        for entry in [depth_heisenberg(1), depth_free_fermion(),
                      depth_lattice(8), depth_lattice(24)]:
            assert entry.d_alg == 0
            assert entry.d_total == 1 + entry.d_arith + 0

    def test_class_L_additivity(self):
        """Class L: d_alg = 1, so d = 2 + d_arith."""
        for entry in [depth_affine_km('sl2'), depth_affine_km('sl3')]:
            assert entry.d_alg == 1
            assert entry.d_total == 1 + entry.d_arith + 1

    def test_class_C_additivity(self):
        """Class C: d_alg = 2, so d = 3 + d_arith."""
        entry = depth_betagamma(1)
        assert entry.d_alg == 2
        assert entry.d_total == 1 + entry.d_arith + 2

    def test_class_M_additivity(self):
        """Class M: d_alg = infinity, d_total = infinity."""
        for entry in [depth_virasoro_generic(1), depth_virasoro_ising(),
                      depth_wN_generic(3, 50)]:
            assert entry.d_alg is None  # infinity
            assert entry.d_total is None  # infinity
            assert entry.verify_additivity()

    def test_degenerate_heisenberg_additivity(self):
        """H_0: d = 1 + 0 + 0 = 1."""
        entry = depth_heisenberg(0)
        assert entry.d_total == 1
        assert entry.d_arith == 0
        assert entry.d_alg == 0


# ========================================================================
# 2. Class G: d_alg = 0
# ========================================================================

class TestClassG:
    """All Gaussian algebras have d_alg = 0."""

    def test_heisenberg_d_alg_zero(self):
        for k in [0, 1, 2, 10]:
            entry = depth_heisenberg(k)
            assert entry.d_alg == 0
            assert entry.shadow_class == 'G'

    def test_free_fermion_d_alg_zero(self):
        entry = depth_free_fermion()
        assert entry.d_alg == 0
        assert entry.shadow_class == 'G'

    def test_lattice_d_alg_zero(self):
        for rank in [8, 16, 24, 32, 48]:
            entry = depth_lattice(rank)
            assert entry.d_alg == 0
            assert entry.shadow_class == 'G'

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (AP1)."""
        for k in [1, 2, 5, 10]:
            entry = depth_heisenberg(k)
            assert entry.kappa == Rational(k)

    def test_free_fermion_kappa(self):
        """kappa(ff) = 1/4 = c/2 (AP1)."""
        entry = depth_free_fermion()
        assert entry.kappa == Rational(1, 4)


# ========================================================================
# 3. Class L: d_alg = 1
# ========================================================================

class TestClassL:
    """All Lie/tree algebras have d_alg = 1."""

    def test_affine_d_alg_one(self):
        for lie_type in ['sl2', 'sl3', 'E8']:
            entry = depth_affine_km(lie_type)
            assert entry.d_alg == 1
            assert entry.shadow_class == 'L'

    def test_affine_d_total_three(self):
        """All affine at generic level have d = 3."""
        for lie_type in ['sl2', 'sl3', 'E8']:
            entry = depth_affine_km(lie_type)
            assert entry.d_total == 3

    def test_affine_d_arith_one(self):
        """All affine at generic level have d_arith = 1."""
        for lie_type in ['sl2', 'sl3', 'E8']:
            entry = depth_affine_km(lie_type)
            assert entry.d_arith == 1


# ========================================================================
# 4. Class C: d_alg = 2
# ========================================================================

class TestClassC:
    """betagamma has d_alg = 2."""

    def test_betagamma_d_alg_two(self):
        entry = depth_betagamma(1)
        assert entry.d_alg == 2
        assert entry.shadow_class == 'C'

    def test_betagamma_d_total_four(self):
        entry = depth_betagamma(1)
        assert entry.d_total == 4

    def test_betagamma_kappa(self):
        """kappa(betagamma, lambda=1) = 1 (AP1)."""
        entry = depth_betagamma(1)
        assert entry.kappa == Rational(1)


# ========================================================================
# 5. Class M: d_alg = infinity
# ========================================================================

class TestClassM:
    """All mixed algebras have d_alg = infinity."""

    def test_virasoro_d_alg_infinity(self):
        for c in [1, 26, Rational(1, 2)]:
            entry = depth_virasoro_generic(c)
            assert entry.d_alg is None  # infinity
            assert entry.shadow_class == 'M'

    def test_wN_d_alg_infinity(self):
        for n in [3, 4]:
            entry = depth_wN_generic(n, 50)
            assert entry.d_alg is None
            assert entry.shadow_class == 'M'

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 (AP1, AP20: specify WHICH algebra)."""
        for c in [1, 2, 26]:
            entry = depth_virasoro_generic(c)
            assert entry.kappa == Rational(c, 2)

    def test_minimal_model_d_alg_infinity(self):
        """Minimal models have d_alg = infinity (class M, not class G!)."""
        for p, q in [(3, 4), (4, 5), (5, 6)]:
            entry = depth_virasoro_minimal(p, q)
            assert entry.d_alg is None  # infinity
            assert entry.shadow_class == 'M'


# ========================================================================
# 6. Lattice d_arith = 2 + dim S_{r/2}
# ========================================================================

class TestLatticeArithmeticDepth:
    """Verify d_arith for even unimodular lattice VOAs."""

    def test_E8_d_arith(self):
        """E_8 lattice: rank 8, weight 4, dim S_4 = 0, d_arith = 2."""
        entry = depth_lattice(8)
        assert entry.d_arith == 2
        assert entry.d_total == 3  # = 1 + 2 + 0

    def test_rank16_d_arith(self):
        """rank 16: weight 8, dim S_8 = 0, d_arith = 2."""
        entry = depth_lattice(16)
        assert entry.d_arith == 2
        assert entry.d_total == 3

    def test_Leech_d_arith(self):
        """Leech: rank 24, weight 12, dim S_12 = 1, d_arith = 3."""
        entry = depth_lattice(24)
        assert entry.d_arith == 3
        assert entry.d_total == 4  # = 1 + 3 + 0

    def test_rank32_d_arith(self):
        """rank 32: weight 16, dim S_16 = 1, d_arith = 3."""
        entry = depth_lattice(32)
        assert entry.d_arith == 3
        assert entry.d_total == 4

    def test_rank48_d_arith(self):
        """rank 48: weight 24, dim S_24 = 2, d_arith = 4."""
        entry = depth_lattice(48)
        assert entry.d_arith == 4
        assert entry.d_total == 5  # = 1 + 4 + 0

    def test_lattice_d_arith_formula(self):
        """d_arith = 2 + dim S_{r/2} for rank r, r % 8 == 0, r >= 8."""
        for rank in [8, 16, 24, 32, 40, 48, 56, 64, 72, 96]:
            entry = depth_lattice(rank)
            k = rank // 2
            expected = 2 + dim_cusp_forms_sl2z(k)
            assert entry.d_arith == expected, (
                f"rank {rank}: d_arith = {entry.d_arith}, expected {expected}"
            )


# ========================================================================
# 7. Ising d_arith = 0
# ========================================================================

class TestIsingArithmeticDepth:
    """The Ising model has d_arith = 0 (prop:ising-d-arith)."""

    def test_ising_d_arith_zero(self):
        entry = depth_virasoro_ising()
        assert entry.d_arith == 0

    def test_ising_central_charge(self):
        entry = depth_virasoro_ising()
        assert entry.kappa == Rational(1, 4)  # c/2 = 1/4

    def test_ising_class_M(self):
        """Ising is class M (NOT class G, despite being a "simple" model)."""
        entry = depth_virasoro_ising()
        assert entry.shadow_class == 'M'
        assert entry.d_alg is None  # infinity

    def test_ising_epstein_two_terms(self):
        """The constrained Epstein zeta for Ising has exactly 2 terms."""
        terms = constrained_epstein_terms(3, 4)
        assert len(terms) == 2

    def test_ising_epstein_values(self):
        """Epstein terms: (2, 1) and (1/4, 1) giving 2^{-s} + 4^s."""
        terms = constrained_epstein_terms(3, 4)
        values = sorted([float(a) for a, _ in terms])
        assert len(values) == 2
        # The terms should be (2*Delta_epsilon, 1) and (2*Delta_sigma, 1)
        # Delta_epsilon = 2 * (1/2) = 1, so 2*Delta = 2
        # Delta_sigma = 2 * (1/16) = 1/8, so 2*Delta = 1/4
        assert Rational(1, 4) in [a for a, _ in terms]
        assert Rational(2) in [a for a, _ in terms] or Rational(1) in [a for a, _ in terms]

    def test_ising_zeros_imaginary_axis(self):
        """All Epstein zeros lie on Re(s) = 0."""
        analysis = constrained_epstein_zeros_on_critical_line(3, 4)
        assert analysis['d_arith'] == 0


# ========================================================================
# 8. Minimal model d_arith = 0
# ========================================================================

class TestMinimalModelArithmeticDepth:
    """All minimal models have d_arith = 0."""

    @pytest.mark.parametrize("p,q", [(3, 4), (4, 5), (5, 6), (5, 4), (7, 6)])
    def test_minimal_model_d_arith_zero(self, p, q):
        entry = depth_virasoro_minimal(p, q)
        assert entry.d_arith == 0

    def test_tricritical_ising(self):
        """M(4,5) at c=7/10: d_arith = 0."""
        entry = depth_virasoro_tricritical()
        assert entry.d_arith == 0
        assert entry.kappa == Rational(7, 20)

    def test_3state_potts(self):
        """M(5,6) at c=4/5: d_arith = 0."""
        entry = depth_virasoro_3state_potts()
        assert entry.d_arith == 0
        assert entry.kappa == Rational(2, 5)


# ========================================================================
# 9. d_arith stabilization
# ========================================================================

class TestDarithStabilization:
    """d_arith is constant across shadow arity (does not grow with tower)."""

    def test_stabilization_theorem(self):
        analysis = d_arith_stabilization_analysis()
        assert analysis['theorem'] == 'd_arith is independent of shadow arity r'

    def test_virasoro_irrational_stable(self):
        analysis = d_arith_stabilization_analysis()
        assert analysis['examples']['Virasoro_irrational_c']['stable'] is True

    def test_ising_stable(self):
        analysis = d_arith_stabilization_analysis()
        assert analysis['examples']['Ising']['d_arith'] == 0
        assert analysis['examples']['Ising']['stable'] is True

    def test_leech_stable(self):
        analysis = d_arith_stabilization_analysis()
        assert analysis['examples']['Leech_lattice']['d_arith'] == 3
        assert analysis['examples']['Leech_lattice']['stable'] is True


# ========================================================================
# 10. Ising paradox
# ========================================================================

class TestIsingParadox:
    """Complete Ising paradox analysis."""

    def test_paradox_statement(self):
        paradox = ising_paradox_analysis()
        assert 'd_arith = 0' in paradox['paradox']
        assert 'd_alg = infinity' in paradox['paradox']

    def test_five_resolution_layers(self):
        paradox = ising_paradox_analysis()
        assert len(paradox['resolution_layers']) == 5

    def test_algebra_data_correct(self):
        paradox = ising_paradox_analysis()
        data = paradox['algebra_data']
        assert data['c'] == Rational(1, 2)
        assert data['kappa'] == Rational(1, 4)
        assert data['S_3'] == Rational(2)
        assert data['shadow_class'] == 'M'

    def test_S4_ising(self):
        """S_4(Ising) = 10/[c(5c+22)] = 10/(1/2 * 49/2) = 40/49."""
        paradox = ising_paradox_analysis()
        S4 = paradox['algebra_data']['S_4']
        assert S4 == Rational(40, 49)

    def test_Delta_ising(self):
        """Delta(Ising) = 8 * (1/4) * (40/49) = 80/49."""
        paradox = ising_paradox_analysis()
        Delta = paradox['algebra_data']['Delta']
        assert Delta == Rational(80, 49)

    def test_fusion_ring_in_resolution(self):
        """The fusion ring is mentioned as a source of arithmetic."""
        paradox = ising_paradox_analysis()
        assert 'FUSION RING' in paradox['resolution_layers']['layer_2']

    def test_vvmf_in_resolution(self):
        """The VVMF is mentioned as a source of arithmetic."""
        paradox = ising_paradox_analysis()
        assert 'VVMF' in paradox['resolution_layers']['layer_3']


# ========================================================================
# 11. Genus-dependent arithmetic depth
# ========================================================================

class TestGenusArithmeticDepth:
    """Genus-g arithmetic depth d_arith^{(g)}."""

    def test_ising_genus1(self):
        gad = genus_arithmetic_depth_ising(1)
        assert gad.d_arith_g == 0

    def test_ising_genus2(self):
        gad = genus_arithmetic_depth_ising(2)
        assert gad.d_arith_g == 0  # still 0 at genus 2

    def test_leech_genus1(self):
        gad = genus_arithmetic_depth_leech(1)
        assert gad.d_arith_g == 3

    def test_leech_genus2_unknown(self):
        """Genus-2 Leech d_arith not computed (unknown)."""
        gad = genus_arithmetic_depth_leech(2)
        assert gad.d_arith_g is None  # unknown but > 0


# ========================================================================
# 12. Cusp form dimensions
# ========================================================================

class TestCuspFormDimensions:
    """Verify cusp form dimensions for SL(2,Z)."""

    @pytest.mark.parametrize("k,expected", [
        (0, 0), (2, 0), (4, 0), (6, 0), (8, 0), (10, 0),
        (12, 1), (14, 0), (16, 1), (18, 1), (20, 1), (22, 1),
        (24, 2), (26, 1), (28, 2), (30, 2), (32, 2), (34, 2),
        (36, 3),
    ])
    def test_cusp_form_dim(self, k, expected):
        assert dim_cusp_forms_sl2z(k) == expected, (
            f"dim S_{k}(SL(2,Z)) = {dim_cusp_forms_sl2z(k)}, expected {expected}"
        )

    def test_cusp_form_dim_odd(self):
        """Odd weight: dim = 0."""
        for k in [1, 3, 5, 7, 11, 13, 15]:
            assert dim_cusp_forms_sl2z(k) == 0

    def test_cusp_form_dim_negative(self):
        """Negative weight: dim = 0."""
        for k in [-2, -4, -12]:
            assert dim_cusp_forms_sl2z(k) == 0


# ========================================================================
# 13. Minimal model data
# ========================================================================

class TestMinimalModelData:
    """Verify minimal model central charges, primaries, weights."""

    def test_ising_central_charge(self):
        """M(3,4): c = 1 - 6*(3-4)^2/(3*4) = 1 - 6/12 = 1/2."""
        assert minimal_model_central_charge(3, 4) == Rational(1, 2)

    def test_tricritical_central_charge(self):
        """M(4,5): c = 1 - 6*(4-5)^2/(4*5) = 1 - 6/20 = 7/10."""
        assert minimal_model_central_charge(4, 5) == Rational(7, 10)

    def test_3state_potts_central_charge(self):
        """M(5,6): c = 1 - 6*(5-6)^2/(5*6) = 1 - 6/30 = 4/5."""
        assert minimal_model_central_charge(5, 6) == Rational(4, 5)

    def test_ising_n_primaries(self):
        """M(3,4): N = (3-1)(4-1)/2 = 3."""
        assert minimal_model_n_primaries(3, 4) == 3

    def test_tricritical_n_primaries(self):
        """M(4,5): N = (4-1)(5-1)/2 = 6."""
        assert minimal_model_n_primaries(4, 5) == 6

    def test_3state_potts_n_primaries(self):
        """M(5,6): N = (5-1)(6-1)/2 = 10."""
        assert minimal_model_n_primaries(5, 6) == 10

    def test_ising_conformal_weights(self):
        """M(3,4) weights: {0, 1/2, 1/16}."""
        weights = minimal_model_conformal_weights(3, 4)
        expected = {Rational(0), Rational(1, 2), Rational(1, 16)}
        assert set(weights) == expected

    def test_ising_scalar_primaries(self):
        """M(3,4) scalar primaries: Delta = 1 and Delta = 1/8."""
        scalars = minimal_model_scalar_primaries(3, 4)
        deltas = [d for d, _ in scalars]
        # h = 1/2 -> Delta = 2h = 1
        # h = 1/16 -> Delta = 2h = 1/8
        assert Rational(1) in deltas
        assert Rational(1, 8) in deltas
        assert len(scalars) == 2  # h=0 excluded

    def test_tricritical_conformal_weights(self):
        """M(4,5) has 6 primaries."""
        weights = minimal_model_conformal_weights(4, 5)
        assert len(weights) == 6
        # Should include h = 0
        assert Rational(0) in weights


# ========================================================================
# 14. Cross-family consistency checks (AP10)
# ========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency: not just single-family hardcoded values."""

    def test_class_determines_d_alg(self):
        """d_alg depends only on shadow class, not on specific parameters."""
        table = build_complete_table()
        for entry in table:
            if entry.shadow_class == 'G':
                assert entry.d_alg == 0, f"{entry.name}: d_alg should be 0"
            elif entry.shadow_class == 'L':
                assert entry.d_alg == 1, f"{entry.name}: d_alg should be 1"
            elif entry.shadow_class == 'C':
                assert entry.d_alg == 2, f"{entry.name}: d_alg should be 2"
            elif entry.shadow_class == 'M':
                assert entry.d_alg is None, f"{entry.name}: d_alg should be infinity"

    def test_d_arith_nonnegative(self):
        """d_arith >= 0 for all families."""
        table = build_complete_table()
        for entry in table:
            assert entry.d_arith >= 0, f"{entry.name}: d_arith = {entry.d_arith} < 0"

    def test_d_total_ge_one(self):
        """d >= 1 for all families (minimum from the "+1" in decomposition)."""
        table = build_complete_table()
        for entry in table:
            if entry.d_total is not None:
                assert entry.d_total >= 1, f"{entry.name}: d_total = {entry.d_total} < 1"

    def test_class_M_always_infinite_d(self):
        """Class M always has d = infinity."""
        table = build_complete_table()
        for entry in table:
            if entry.shadow_class == 'M':
                assert entry.d_total is None, f"{entry.name}: class M should have d = infinity"

    def test_virasoro_consistent_with_minimal_models(self):
        """Virasoro generic and minimal models have same d_alg."""
        generic = depth_virasoro_generic(1)
        ising = depth_virasoro_ising()
        assert generic.d_alg == ising.d_alg  # both infinity
        assert generic.shadow_class == ising.shadow_class  # both M

    def test_lattice_monotone_d_arith(self):
        """Lattice d_arith is non-decreasing with rank."""
        d_prev = 0
        for rank in [8, 16, 24, 32, 40, 48, 56, 64, 72, 96]:
            entry = depth_lattice(rank)
            assert entry.d_arith >= d_prev, (
                f"d_arith decreased from {d_prev} to {entry.d_arith} at rank {rank}"
            )
            d_prev = entry.d_arith

    def test_ising_not_confused_with_free_fermion(self):
        """Ising (c=1/2, class M) is NOT the same as free fermion (c=1/2, class G).

        The Ising model is a minimal model of the VIRASORO algebra at c=1/2.
        The free fermion is a FREE algebra (Clifford OPE) at c=1/2.
        Same central charge, different algebras, different shadow classes.
        """
        ising = depth_virasoro_ising()
        ff = depth_free_fermion()
        assert ising.shadow_class == 'M'
        assert ff.shadow_class == 'G'
        assert ising.d_alg is None  # infinity
        assert ff.d_alg == 0
        # Both have kappa = c/2 = 1/4
        assert ising.kappa == ff.kappa


# ========================================================================
# 15. Class summary
# ========================================================================

class TestClassSummary:
    """Verify class summary statistics."""

    def test_class_counts(self):
        table = build_complete_table()
        summary = class_summary(table)
        # Should have all four classes
        assert 'G' in summary
        assert 'L' in summary
        assert 'C' in summary
        assert 'M' in summary

    def test_class_G_d_alg_zero(self):
        table = build_complete_table()
        summary = class_summary(table)
        assert summary['G']['d_alg_values'] == [0]

    def test_class_M_d_alg_infinite(self):
        table = build_complete_table()
        summary = class_summary(table)
        assert summary['M']['d_alg_is_infinite'] is True


# ========================================================================
# 16. Table rendering
# ========================================================================

class TestTableRendering:

    def test_table_not_empty(self):
        table = build_complete_table()
        rendered = print_table(table)
        assert len(rendered) > 0

    def test_table_has_all_entries(self):
        table = build_complete_table()
        rendered = print_table(table)
        assert 'Heisenberg' in rendered
        assert 'Ising' in rendered
        assert 'Leech' in rendered
        assert 'W_3' in rendered


# ========================================================================
# 17. Generic d_arith values
# ========================================================================

class TestGenericDarith:
    """Verify d_arith values for specific cases from the manuscript."""

    def test_heisenberg_generic_d_arith_one(self):
        """Heisenberg at k > 0: d_arith = 1."""
        for k in [1, 2, 5]:
            entry = depth_heisenberg(k)
            assert entry.d_arith == 1

    def test_heisenberg_zero_d_arith_zero(self):
        """Heisenberg at k = 0: d_arith = 0."""
        entry = depth_heisenberg(0)
        assert entry.d_arith == 0

    def test_virasoro_generic_d_arith_one(self):
        """Virasoro at generic c: d_arith = 1."""
        for c in [1, 26, 100]:
            entry = depth_virasoro_generic(c)
            assert entry.d_arith == 1

    def test_wN_generic_d_arith_one(self):
        """W_N at generic c: d_arith = 1."""
        entry = depth_wN_generic(3, 50)
        assert entry.d_arith == 1


# ========================================================================
# 18. Specific Epstein zeta analyses for multiple minimal models
# ========================================================================

class TestMultipleMinimalModels:
    """Epstein analysis for several minimal models."""

    def test_m34_ising_epstein(self):
        """M(3,4) Ising: 2 Epstein terms."""
        terms = constrained_epstein_terms(3, 4)
        assert len(terms) == 2

    def test_m45_tricritical_epstein(self):
        """M(4,5) tricritical: more terms due to more primaries."""
        terms = constrained_epstein_terms(4, 5)
        # M(4,5) has 6 primaries; at least 5 with h > 0
        assert len(terms) >= 4

    def test_m56_3state_potts_epstein(self):
        """M(5,6) 3-state Potts: 10 primaries."""
        terms = constrained_epstein_terms(5, 6)
        assert len(terms) >= 5

    def test_all_minimal_models_d_arith_zero(self):
        """Baker-type argument: d_arith = 0 for all M(p,q) tested."""
        for p, q in [(3, 4), (4, 5), (5, 6), (5, 4), (7, 6), (7, 4)]:
            analysis = constrained_epstein_zeros_on_critical_line(p, q)
            assert analysis['d_arith'] == 0, f"M({p},{q}): d_arith = {analysis['d_arith']} != 0"
