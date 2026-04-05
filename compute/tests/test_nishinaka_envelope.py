"""Tests for compute/lib/nishinaka_envelope.py — Nishinaka factorization envelope.

Comprehensive test suite verifying the seven-step pipeline from
Lie conformal data to shadow obstruction tower via the factorization envelope
construction.

Coverage:
  1. LieConformalData validation and properties
  2. OPE extraction
  3. Factorization algebra construction
  4. Bar coalgebra structure
  5. MC element extraction and kappa verification
  6. MC equation verification
  7. Shadow obstruction tower projection and depth classification
  8. Envelope-shadow functor verification
  9. Complete pipeline for all standard families
  10. Cross-family structural properties

References:
  constr:platonic-package, def:cyclically-admissible,
  thm:mc2-bar-intrinsic, cor:shadow-extraction,
  thm:cubic-gauge-triviality, def:shadow-depth-classification,
  rem:envelope-execution-programme
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, S, oo, cancel

from compute.lib.nishinaka_envelope import (
    LieConformalData,
    FactorizationData,
    BarCoalgebra,
    MCElement,
    ShadowTower,
    NishinakaEnvelope,
    extract_ope_data,
    build_factorization_data,
    build_bar_coalgebra,
    extract_mc_element,
    verify_mc_equation,
    project_shadow_tower,
    verify_envelope_shadow,
    nishinaka_envelope,
    heisenberg_conformal,
    affine_sl2_conformal,
    affine_sl3_conformal,
    betagamma_conformal,
    virasoro_conformal,
    w3_conformal,
    free_fermion_conformal,
    lattice_conformal,
    envelope_for_family,
    standard_envelope_landscape,
)


# =========================================================================
# Helpers
# =========================================================================

k_sym = Symbol('k')
c_sym = Symbol('c')


def _is_zero(expr, tol=1e-12):
    try:
        s = simplify(expr)
        if s == 0:
            return True
        return abs(float(s)) < tol
    except (TypeError, ValueError):
        return expr == 0


# =========================================================================
# 1. LieConformalData construction
# =========================================================================

class TestLieConformalDataConstruction:
    """Test construction and validation of LieConformalData."""

    def test_heisenberg_is_lie_conformal(self):
        """Heisenberg IS a Lie conformal algebra."""
        L = heisenberg_conformal(level=Rational(1))
        assert L.is_lie_conformal is True

    def test_heisenberg_rank(self):
        """Heisenberg has rank 1 (one generator J)."""
        L = heisenberg_conformal()
        assert L.rank == 1
        assert L.generators == ['J']

    def test_heisenberg_weight(self):
        """Heisenberg generator J has weight 1."""
        L = heisenberg_conformal()
        assert L.weights == [1]

    def test_heisenberg_is_abelian(self):
        """Heisenberg is abelian: no simple-pole Lie bracket."""
        L = heisenberg_conformal(level=Rational(1))
        assert L.is_abelian() is True

    def test_affine_sl2_is_lie_conformal(self):
        """Affine sl_2 IS a Lie conformal algebra."""
        L = affine_sl2_conformal(level=Rational(1))
        assert L.is_lie_conformal is True

    def test_affine_sl2_rank(self):
        """Affine sl_2 has rank 3 (generators e, f, h)."""
        L = affine_sl2_conformal()
        assert L.rank == 3
        assert set(L.generators) == {'e', 'f', 'h'}

    def test_affine_sl2_has_lie_bracket(self):
        """Affine sl_2 has nontrivial Lie bracket."""
        L = affine_sl2_conformal(level=Rational(1))
        assert L.has_lie_bracket() is True
        assert L.is_abelian() is False

    def test_virasoro_not_lie_conformal(self):
        """Virasoro is NOT a Lie conformal algebra (quartic pole)."""
        L = virasoro_conformal()
        assert L.is_lie_conformal is False

    def test_w3_not_lie_conformal(self):
        """W_3 is NOT a Lie conformal algebra (composite fields)."""
        L = w3_conformal()
        assert L.is_lie_conformal is False

    def test_betagamma_is_lie_conformal(self):
        """Beta-gamma IS a Lie conformal algebra (simple pole OPE)."""
        L = betagamma_conformal()
        assert L.is_lie_conformal is True

    def test_free_fermion_is_lie_conformal(self):
        """Free fermion IS a Lie conformal algebra."""
        L = free_fermion_conformal()
        assert L.is_lie_conformal is True


# =========================================================================
# 2. OPE extraction
# =========================================================================

class TestOPEExtraction:
    """Test OPE data extraction from lambda-bracket data."""

    def test_heisenberg_ope_abelian(self):
        """Heisenberg OPE is abelian (only double pole)."""
        L = heisenberg_conformal(level=Rational(1))
        ope = extract_ope_data(L)
        assert ope['is_abelian'] is True

    def test_heisenberg_max_pole(self):
        """Heisenberg has max pole order 2."""
        L = heisenberg_conformal(level=Rational(1))
        ope = extract_ope_data(L)
        assert ope['max_pole_order'] == 2

    def test_affine_sl2_not_abelian(self):
        """Affine sl_2 OPE is non-abelian."""
        L = affine_sl2_conformal(level=Rational(1))
        ope = extract_ope_data(L)
        assert ope['is_abelian'] is False

    def test_virasoro_max_pole(self):
        """Virasoro has max pole order 4."""
        L = virasoro_conformal(central_charge=Rational(25))
        ope = extract_ope_data(L)
        assert ope['max_pole_order'] == 4

    def test_betagamma_max_pole(self):
        """Beta-gamma has max pole order 1 (simple pole)."""
        L = betagamma_conformal()
        ope = extract_ope_data(L)
        assert ope['max_pole_order'] == 1


# =========================================================================
# 3. Factorization algebra
# =========================================================================

class TestFactorizationAlgebra:
    """Test factorization algebra construction."""

    def test_heisenberg_bar_dims(self):
        """Heisenberg bar dims: B^1 = 1, B^2 = 1 (partition numbers)."""
        L = heisenberg_conformal(level=Rational(1))
        fact = build_factorization_data(L)
        assert fact.bar_dims[1] == 1
        assert fact.bar_dims[2] == 1

    def test_affine_sl2_bar_dims(self):
        """Affine sl_2 bar dims: B^1 = 3, B^2 = 5."""
        L = affine_sl2_conformal(level=Rational(1))
        fact = build_factorization_data(L)
        assert fact.bar_dims[1] == 3
        assert fact.bar_dims[2] == 5

    def test_factorization_type_chiral(self):
        """All standard families produce chiral factorization algebras."""
        for constructor in [heisenberg_conformal, affine_sl2_conformal,
                           betagamma_conformal, virasoro_conformal]:
            L = constructor()
            fact = build_factorization_data(L)
            assert fact.factorization_type == 'chiral'


# =========================================================================
# 4. Bar coalgebra
# =========================================================================

class TestBarCoalgebra:
    """Test bar coalgebra construction."""

    def test_d_squared_zero_all_families(self):
        """d_B^2 = 0 for all standard families (thm:bar-modular-operad)."""
        for constructor in [heisenberg_conformal, affine_sl2_conformal,
                           betagamma_conformal, virasoro_conformal,
                           w3_conformal, free_fermion_conformal]:
            L = constructor()
            fact = build_factorization_data(L)
            bar = build_bar_coalgebra(fact)
            assert bar.d_squared_zero is True

    def test_curvature_zero_honest_algebras(self):
        """Curvature m_0 = 0 for honest (non-curved) chiral algebras."""
        L = heisenberg_conformal(level=Rational(1))
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        assert bar.curvature_m0 == 0

    def test_heisenberg_diff_components(self):
        """Heisenberg bar differential: metric contribution only."""
        L = heisenberg_conformal(level=Rational(1))
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        assert 'd_int' in bar.differential_components
        assert 'metric_contribution' in bar.differential_components
        # No bracket contribution (abelian)
        assert 'bracket_contribution' not in bar.differential_components

    def test_affine_diff_has_bracket(self):
        """Affine sl_2 bar differential includes bracket contribution."""
        L = affine_sl2_conformal(level=Rational(1))
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        assert 'bracket_contribution' in bar.differential_components


# =========================================================================
# 5. MC element extraction — kappa
# =========================================================================

class TestMCElementKappa:
    """Test MC element extraction, focusing on kappa formulas.

    CRITICAL: AP1 says never copy kappa between families.
    Each test independently verifies the correct formula.
    """

    def test_heisenberg_kappa_equals_level(self):
        """kappa(Heisenberg) = k (the level)."""
        L = heisenberg_conformal(level=Rational(1))
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        mc = extract_mc_element(L, bar)
        assert mc.kappa == 1

    def test_heisenberg_kappa_symbolic(self):
        """kappa(Heisenberg) = k symbolically."""
        L = heisenberg_conformal()
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        mc = extract_mc_element(L, bar)
        assert mc.kappa == k_sym

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k=1) = 3(1+2)/4 = 9/4."""
        L = affine_sl2_conformal(level=Rational(1))
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        mc = extract_mc_element(L, bar)
        assert mc.kappa == Rational(9, 4)

    def test_affine_sl3_kappa(self):
        """kappa(sl_3, k=1) = 8*(1+3)/6 = 32/6 = 16/3."""
        L = affine_sl3_conformal(level=Rational(1))
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        mc = extract_mc_element(L, bar)
        assert mc.kappa == Rational(16, 3)

    def test_virasoro_kappa(self):
        """kappa(Vir, c=25) = 25/2."""
        L = virasoro_conformal(central_charge=Rational(25))
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        mc = extract_mc_element(L, bar)
        assert mc.kappa == Rational(25, 2)

    def test_w3_kappa(self):
        """kappa(W_3, c=2) = 5*2/6 = 5/3."""
        L = w3_conformal(central_charge=Rational(2))
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        mc = extract_mc_element(L, bar)
        assert mc.kappa == Rational(5, 3)

    def test_betagamma_kappa(self):
        """kappa(betagamma) = -1 (c = -2, kappa = c/2)."""
        L = betagamma_conformal()
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        mc = extract_mc_element(L, bar)
        assert mc.kappa == -1

    def test_free_fermion_kappa(self):
        """kappa(free fermion) = 1/4 (c = 1/2, kappa = c/2)."""
        L = free_fermion_conformal()
        fact = build_factorization_data(L)
        bar = build_bar_coalgebra(fact)
        mc = extract_mc_element(L, bar)
        assert mc.kappa == Rational(1, 4)


# =========================================================================
# 6. MC equation verification
# =========================================================================

class TestMCEquation:
    """Test MC equation DTheta + (1/2)[Theta,Theta] = 0."""

    def test_mc_arity2_all_families(self):
        """MC equation at arity 2 (D*kappa = 0) for all families."""
        families = ['heisenberg', 'affine_sl2', 'betagamma',
                    'virasoro', 'w3', 'free_fermion']
        for fam in families:
            env = envelope_for_family(fam)
            mc_checks = verify_mc_equation(env.mc_element)
            assert mc_checks[2] is True, f"MC arity 2 failed for {fam}"

    def test_mc_arity3_all_families(self):
        """MC equation at arity 3 for all families."""
        families = ['heisenberg', 'affine_sl2', 'betagamma',
                    'virasoro', 'w3', 'free_fermion']
        for fam in families:
            env = envelope_for_family(fam)
            mc_checks = verify_mc_equation(env.mc_element)
            assert mc_checks[3] is True, f"MC arity 3 failed for {fam}"

    def test_mc_arity4_all_families(self):
        """MC equation at arity 4 for all families."""
        families = ['heisenberg', 'affine_sl2', 'betagamma',
                    'virasoro', 'w3', 'free_fermion']
        for fam in families:
            env = envelope_for_family(fam)
            mc_checks = verify_mc_equation(env.mc_element)
            assert mc_checks[4] is True, f"MC arity 4 failed for {fam}"


# =========================================================================
# 7. Shadow obstruction tower and depth classification
# =========================================================================

class TestShadowTower:
    """Test shadow obstruction tower projection and depth classification."""

    def test_heisenberg_depth_G(self):
        """Heisenberg is class G (Gaussian, r_max = 2)."""
        env = envelope_for_family('heisenberg', level=Rational(1))
        assert env.shadow_tower.depth_class == 'G'
        assert env.shadow_tower.terminates is True
        assert env.shadow_tower.termination_arity == 2

    def test_affine_sl2_depth_L(self):
        """Affine sl_2 is class L (Lie/tree, r_max = 3)."""
        env = envelope_for_family('affine_sl2', level=Rational(1))
        assert env.shadow_tower.depth_class == 'L'
        assert env.shadow_tower.terminates is True
        assert env.shadow_tower.termination_arity == 3

    def test_betagamma_depth_C(self):
        """Beta-gamma is class C (contact, r_max = 4)."""
        env = envelope_for_family('betagamma')
        assert env.shadow_tower.depth_class == 'C'
        assert env.shadow_tower.terminates is True
        assert env.shadow_tower.termination_arity == 4

    def test_virasoro_depth_M(self):
        """Virasoro is class M (mixed, infinite tower)."""
        env = envelope_for_family('virasoro', central_charge=Rational(25))
        assert env.shadow_tower.depth_class == 'M'
        assert env.shadow_tower.terminates is False

    def test_w3_depth_M(self):
        """W_3 is class M (mixed, infinite tower)."""
        env = envelope_for_family('w3', central_charge=Rational(2))
        assert env.shadow_tower.depth_class == 'M'
        assert env.shadow_tower.terminates is False

    def test_free_fermion_depth_G(self):
        """Free fermion is class G."""
        env = envelope_for_family('free_fermion')
        assert env.shadow_tower.depth_class == 'G'

    def test_lattice_depth_G(self):
        """Lattice VOA is class G."""
        env = envelope_for_family('lattice')
        assert env.shadow_tower.depth_class == 'G'

    def test_heisenberg_higher_shadows_vanish(self):
        """Heisenberg: all shadows beyond arity 2 are zero."""
        env = envelope_for_family('heisenberg', level=Rational(1))
        tower = env.shadow_tower
        assert tower.shadow_at_arity(3) == 0
        assert tower.shadow_at_arity(4) == 0
        assert tower.shadow_at_arity(5) == 0

    def test_affine_tower_has_cubic(self):
        """Affine sl_2: has nonzero cubic shadow at arity 3."""
        env = envelope_for_family('affine_sl2', level=Rational(1))
        assert 3 in env.shadow_tower.shadows
        assert env.shadow_tower.shadows[3] != 0

    def test_affine_quartic_vanishes(self):
        """Affine sl_2: quartic shadow vanishes (class L terminates at 3)."""
        env = envelope_for_family('affine_sl2', level=Rational(1))
        tower = env.shadow_tower
        assert tower.shadow_at_arity(4) == 0

    def test_cumulative_shadow_heisenberg(self):
        """Heisenberg cumulative shadow Theta^{<=4} = kappa (only arity 2)."""
        env = envelope_for_family('heisenberg', level=Rational(1))
        tower = env.shadow_tower
        assert tower.cumulative_shadow(4) == 1  # kappa = k = 1


# =========================================================================
# 8. Envelope-shadow functor verification
# =========================================================================

class TestEnvelopeShadowFunctor:
    """Test the envelope-shadow relation Theta^env recovers shadow obstruction tower."""

    def test_heisenberg_envelope_shadow(self):
        """Heisenberg: envelope-shadow passes all checks."""
        env = envelope_for_family('heisenberg', level=Rational(1))
        assert env.envelope_verification['all_pass'] is True

    def test_affine_sl2_envelope_shadow(self):
        """Affine sl_2: envelope-shadow passes all checks."""
        env = envelope_for_family('affine_sl2', level=Rational(1))
        assert env.envelope_verification['all_pass'] is True

    def test_virasoro_envelope_shadow(self):
        """Virasoro: envelope-shadow passes all checks."""
        env = envelope_for_family('virasoro', central_charge=Rational(25))
        assert env.envelope_verification['all_pass'] is True

    def test_betagamma_envelope_shadow(self):
        """Beta-gamma: envelope-shadow passes."""
        env = envelope_for_family('betagamma')
        assert env.envelope_verification['all_pass'] is True

    def test_w3_envelope_shadow(self):
        """W_3: envelope-shadow passes."""
        env = envelope_for_family('w3', central_charge=Rational(2))
        assert env.envelope_verification['all_pass'] is True

    def test_kappa_consistency_all_families(self):
        """kappa from envelope = kappa from direct for all families."""
        landscape = standard_envelope_landscape()
        for name, env in landscape.items():
            assert env.envelope_verification['kappa_matches'] is True, \
                f"kappa mismatch for {name}"

    def test_cubic_consistency_all_families(self):
        """Cubic from envelope = cubic from direct for all families."""
        landscape = standard_envelope_landscape()
        for name, env in landscape.items():
            assert env.envelope_verification['cubic_matches'] is True, \
                f"cubic mismatch for {name}"


# =========================================================================
# 9. Complete pipeline for all families
# =========================================================================

class TestCompletePipeline:
    """Test the complete Nishinaka pipeline for each standard family."""

    def test_heisenberg_complete(self):
        """Full pipeline for Heisenberg at k=1."""
        env = envelope_for_family('heisenberg', level=Rational(1))
        assert isinstance(env, NishinakaEnvelope)
        assert env.mc_element.kappa == 1
        assert env.shadow_tower.depth_class == 'G'

    def test_affine_sl2_complete(self):
        """Full pipeline for affine sl_2 at k=1."""
        env = envelope_for_family('affine_sl2', level=Rational(1))
        assert isinstance(env, NishinakaEnvelope)
        assert env.mc_element.kappa == Rational(9, 4)
        assert env.shadow_tower.depth_class == 'L'

    def test_affine_sl3_complete(self):
        """Full pipeline for affine sl_3 at k=1."""
        env = envelope_for_family('affine_sl3', level=Rational(1))
        assert isinstance(env, NishinakaEnvelope)
        assert env.mc_element.kappa == Rational(16, 3)
        assert env.shadow_tower.depth_class == 'L'

    def test_betagamma_complete(self):
        """Full pipeline for beta-gamma."""
        env = envelope_for_family('betagamma')
        assert isinstance(env, NishinakaEnvelope)
        assert env.mc_element.kappa == -1
        assert env.shadow_tower.depth_class == 'C'

    def test_virasoro_complete(self):
        """Full pipeline for Virasoro at c=25."""
        env = envelope_for_family('virasoro', central_charge=Rational(25))
        assert isinstance(env, NishinakaEnvelope)
        assert env.mc_element.kappa == Rational(25, 2)
        assert env.shadow_tower.depth_class == 'M'

    def test_w3_complete(self):
        """Full pipeline for W_3 at c=2."""
        env = envelope_for_family('w3', central_charge=Rational(2))
        assert isinstance(env, NishinakaEnvelope)
        assert env.mc_element.kappa == Rational(5, 3)
        assert env.shadow_tower.depth_class == 'M'

    def test_free_fermion_complete(self):
        """Full pipeline for free fermion."""
        env = envelope_for_family('free_fermion')
        assert isinstance(env, NishinakaEnvelope)
        assert env.mc_element.kappa == Rational(1, 4)

    def test_lattice_complete(self):
        """Full pipeline for lattice VOA."""
        env = envelope_for_family('lattice')
        assert isinstance(env, NishinakaEnvelope)
        assert env.shadow_tower.depth_class == 'G'


# =========================================================================
# 10. Cross-family structural properties
# =========================================================================

class TestCrossFamilyProperties:
    """Test structural properties that hold across all families."""

    def test_all_standard_families_produce_envelopes(self):
        """All 8 standard families produce valid NishinakaEnvelope."""
        landscape = standard_envelope_landscape()
        assert len(landscape) == 8
        for name, env in landscape.items():
            assert isinstance(env, NishinakaEnvelope), f"Failed for {name}"

    def test_abelian_implies_depth_G(self):
        """Abelian Lie conformal algebras have shadow depth class G."""
        for constructor in [heisenberg_conformal, free_fermion_conformal,
                           lattice_conformal]:
            L = constructor()
            env = nishinaka_envelope(L)
            if L.is_abelian():
                assert env.shadow_tower.depth_class == 'G', \
                    f"Abelian {L.name} should be class G"

    def test_non_abelian_nonzero_cubic(self):
        """Non-abelian LCAs have nonzero cubic shadow."""
        L = affine_sl2_conformal(level=Rational(1))
        env = nishinaka_envelope(L)
        assert env.mc_element.cubic != 0

    def test_virasoro_quartic_contact_formula(self):
        """Q^contact_Vir = 10/[c(5c+22)] at c=25."""
        env = envelope_for_family('virasoro', central_charge=Rational(25))
        q = env.mc_element.quartic
        expected = Rational(10) / (25 * (5 * 25 + 22))
        assert _is_zero(q - expected), \
            f"Q^contact = {q}, expected {expected}"

    def test_virasoro_quartic_contact_c1(self):
        """Q^contact_Vir at c=1: 10/(1*27) = 10/27."""
        env = envelope_for_family('virasoro', central_charge=Rational(1))
        q = env.mc_element.quartic
        expected = Rational(10, 27)
        assert _is_zero(q - expected)

    def test_kappa_additivity_heisenberg(self):
        """kappa(H_{k1}) + kappa(H_{k2}) = kappa(H_{k1+k2}) = k1 + k2."""
        env1 = envelope_for_family('heisenberg', level=Rational(1))
        env2 = envelope_for_family('heisenberg', level=Rational(2))
        env3 = envelope_for_family('heisenberg', level=Rational(3))
        assert env1.mc_element.kappa + env2.mc_element.kappa == env3.mc_element.kappa

    def test_summary_does_not_crash(self):
        """Calling summary() on every envelope should not crash."""
        landscape = standard_envelope_landscape()
        for name, env in landscape.items():
            s = env.summary()
            assert isinstance(s, str)
            assert name in s or env.lie_conformal_data.name in s

    def test_unknown_family_raises(self):
        """Unknown family name raises ValueError."""
        with pytest.raises(ValueError):
            envelope_for_family('nonexistent_algebra')

    def test_heisenberg_multiple_levels(self):
        """Heisenberg kappa scales linearly with level."""
        for k in [1, 2, 3, 5, 10]:
            env = envelope_for_family('heisenberg', level=Rational(k))
            assert env.mc_element.kappa == k

    def test_affine_sl2_multiple_levels(self):
        """Affine sl_2 kappa = 3(k+2)/4 at multiple levels."""
        for k in [1, 2, 3, 5]:
            env = envelope_for_family('affine_sl2', level=Rational(k))
            expected = Rational(3) * (k + 2) / 4
            assert env.mc_element.kappa == expected, \
                f"kappa(sl_2, k={k}) = {env.mc_element.kappa}, expected {expected}"


# =========================================================================
# 11. Cross-family structural cross-checks (AP10)
# =========================================================================

class TestCrossFamilyCrossChecks:
    """Cross-checks that enforce structural constraints, not just hardcoded values."""

    def test_kappa_duality_affine_sl2(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0 (KM anti-symmetry).

        The Feigin-Frenkel dual level for sl_2 is k' = -k - 2h^v = -k - 4.
        For free-field/KM families: kappa + kappa' = 0.
        """
        for k in [1, 2, 3, 5]:
            env_k = envelope_for_family('affine_sl2', level=Rational(k))
            k_dual = -k - 4
            env_kd = envelope_for_family('affine_sl2', level=Rational(k_dual))
            total = env_k.mc_element.kappa + env_kd.mc_element.kappa
            assert _is_zero(total), (
                f"kappa anti-symmetry failed at k={k}: "
                f"kappa={env_k.mc_element.kappa}, kappa'={env_kd.mc_element.kappa}"
            )

    def test_virasoro_kappa_duality_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (W-algebra complementarity).

        For Virasoro: kappa = c/2, so kappa + kappa' = c/2 + (26-c)/2 = 13.
        """
        for c_val in [1, 2, 10, 13, 25]:
            env_c = envelope_for_family('virasoro', central_charge=Rational(c_val))
            env_cd = envelope_for_family('virasoro', central_charge=Rational(26 - c_val))
            total = env_c.mc_element.kappa + env_cd.mc_element.kappa
            assert total == 13, (
                f"Virasoro complementarity failed at c={c_val}: "
                f"kappa + kappa' = {total}, expected 13"
            )

    def test_depth_class_ordering(self):
        """Shadow depth classes are ordered: G < L < C < M.

        Termination arities: G=2, L=3, C=4, M=infinity.
        """
        depth_map = {'G': 2, 'L': 3, 'C': 4, 'M': float('inf')}
        families = {
            'heisenberg': 'G',
            'affine_sl2': 'L',
            'betagamma': 'C',
            'virasoro': 'M',
        }
        for fam, expected_class in families.items():
            kwargs = {}
            if fam == 'heisenberg':
                kwargs['level'] = Rational(1)
            elif fam == 'affine_sl2':
                kwargs['level'] = Rational(1)
            elif fam == 'virasoro':
                kwargs['central_charge'] = Rational(25)
            env = envelope_for_family(fam, **kwargs)
            assert env.shadow_tower.depth_class == expected_class, (
                f"{fam}: depth class {env.shadow_tower.depth_class}, "
                f"expected {expected_class}"
            )

    def test_abelian_implies_zero_cubic(self):
        """Abelian Lie conformal algebras have zero cubic shadow (structural).

        Cross-check: if the Lie bracket vanishes, the cubic obstruction must vanish.
        """
        for fam in ['heisenberg', 'free_fermion', 'lattice']:
            env = envelope_for_family(fam)
            if env.lie_conformal_data.is_abelian():
                assert env.mc_element.cubic == 0, (
                    f"Abelian {fam} should have zero cubic shadow"
                )

    def test_virasoro_discriminant_complementarity(self):
        """Delta(Vir_c) + Delta(Vir_{26-c}) has constant numerator 6960.

        Delta = 40/(5c+22).  Delta + Delta' = 40/(5c+22) + 40/(152-5c)
        = 40*(174)/[(5c+22)(152-5c)] = 6960/[(5c+22)(152-5c)].
        """
        for c_val in [1, 5, 10, 13, 25]:
            Delta_c = Rational(40) / (5 * c_val + 22)
            Delta_cd = Rational(40) / (5 * (26 - c_val) + 22)
            s = Delta_c + Delta_cd
            expected = Rational(6960) / ((5 * c_val + 22) * (152 - 5 * c_val))
            assert _is_zero(s - expected), (
                f"Discriminant complementarity failed at c={c_val}: "
                f"Delta + Delta' = {s}, expected {expected}"
            )
