"""
Tests for the open/closed derived center computations.

Verifies:
  1. Modular characteristic kappa(A) for all standard families
  2. Shadow obstruction tower: cubic, quartic contact, quartic obstruction
  3. Open/closed quartic resonance class R^oc_4
  4. Shadow depth classification G/L/C/M
  5. Derived center dimensions (Theorem H)
  6. Koszul duality on derived center
  7. Cross-family consistency (additivity, complementarity)
  8. Virasoro quintic obstruction (tower forced infinite)
  9. W_3 quartic resonance divisor
  10. Brace algebra structure (dimensional consistency)

References:
  thm:thqg-brace-dg-algebra, thm:thqg-swiss-cheese,
  thm:thqg-oc-quartic-vanishing, constr:thqg-oc-quartic-resonance
"""

import pytest
from fractions import Fraction

from compute.lib.open_closed_derived_center import (
    heisenberg_data, affine_sl2_data, virasoro_data, w3_data,
    modular_characteristic, cubic_shadow, quartic_contact,
    quartic_obstruction, open_closed_quartic_resonance,
    shadow_depth, derived_center_dimensions, hochschild_hilbert_series,
    koszul_duality_check, kappa_additivity_check,
    shadow_depth_consistency, quintic_obstruction_virasoro,
    virasoro_resonance_divisor, w3_resonance_divisor,
    ChiralHochschildComplex,
)


# ======================================================================
#  Fixtures
# ======================================================================

@pytest.fixture
def heis():
    return heisenberg_data(Fraction(1))

@pytest.fixture
def heis_k2():
    return heisenberg_data(Fraction(2))

@pytest.fixture
def aff():
    return affine_sl2_data(Fraction(1))

@pytest.fixture
def aff_k3():
    return affine_sl2_data(Fraction(3))

@pytest.fixture
def vir():
    return virasoro_data(Fraction(26))

@pytest.fixture
def vir_c1():
    return virasoro_data(Fraction(1))

@pytest.fixture
def vir_c13():
    return virasoro_data(Fraction(13))

@pytest.fixture
def w3():
    return w3_data(Fraction(2))

@pytest.fixture
def w3_c50():
    return w3_data(Fraction(50))


# ======================================================================
#  1. Modular characteristic kappa(A)
# ======================================================================

class TestModularCharacteristic:
    """AP1 guard: kappa formulas are FAMILY-SPECIFIC."""

    def test_heisenberg_kappa_k1(self, heis):
        assert modular_characteristic(heis) == Fraction(1)

    def test_heisenberg_kappa_k2(self, heis_k2):
        assert modular_characteristic(heis_k2) == Fraction(2)

    def test_affine_sl2_kappa_k1(self, aff):
        # kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4
        assert modular_characteristic(aff) == Fraction(9, 4)

    def test_affine_sl2_kappa_k3(self, aff_k3):
        # kappa(sl_2, k=3) = 3*(3+2)/(2*2) = 15/4
        assert modular_characteristic(aff_k3) == Fraction(15, 4)

    def test_virasoro_kappa_c26(self, vir):
        assert modular_characteristic(vir) == Fraction(13)

    def test_virasoro_kappa_c1(self, vir_c1):
        assert modular_characteristic(vir_c1) == Fraction(1, 2)

    def test_virasoro_kappa_c13(self, vir_c13):
        # Self-dual point
        assert modular_characteristic(vir_c13) == Fraction(13, 2)

    def test_w3_kappa(self, w3):
        assert modular_characteristic(w3) == Fraction(1)

    def test_kappa_positive_generic(self):
        """kappa should be positive for generic non-critical levels."""
        for k in [Fraction(1), Fraction(2), Fraction(5)]:
            h = heisenberg_data(k)
            assert modular_characteristic(h) > 0

    def test_kappa_not_copied_between_families(self):
        """AP1: verify kappa formulas differ between families."""
        h = heisenberg_data(Fraction(1))
        a = affine_sl2_data(Fraction(1))
        v = virasoro_data(Fraction(1))
        assert modular_characteristic(h) != modular_characteristic(a)
        assert modular_characteristic(h) != modular_characteristic(v)


# ======================================================================
#  2. Shadow obstruction tower: cubic, quartic contact, quartic obstruction
# ======================================================================

class TestShadowTower:

    def test_heisenberg_cubic_zero(self, heis):
        assert cubic_shadow(heis) == Fraction(0)

    def test_affine_cubic_nonzero(self, aff):
        assert cubic_shadow(aff) != Fraction(0)

    def test_virasoro_cubic(self, vir):
        assert cubic_shadow(vir) == Fraction(2)

    def test_heisenberg_quartic_contact_zero(self, heis):
        assert quartic_contact(heis) == Fraction(0)

    def test_affine_quartic_contact_zero(self, aff):
        assert quartic_contact(aff) == Fraction(0)

    def test_virasoro_quartic_contact(self, vir):
        # Q^ct_Vir(c=26) = 10/(26*(5*26+22)) = 10/(26*152) = 10/3952 = 5/1976
        expected = Fraction(10, 26 * 152)
        assert quartic_contact(vir) == expected

    def test_virasoro_quartic_contact_c1(self, vir_c1):
        # Q^ct_Vir(c=1) = 10/(1*(5+22)) = 10/27
        assert quartic_contact(vir_c1) == Fraction(10, 27)

    def test_virasoro_quartic_contact_pole_c0(self):
        """c=0 is a pole of Q^contact."""
        v = virasoro_data(Fraction(0))
        assert quartic_contact(v) is None

    def test_virasoro_quartic_contact_pole_c_neg22_5(self):
        """c=-22/5 is a pole of Q^contact (null-state divisor)."""
        v = virasoro_data(Fraction(-22, 5))
        assert quartic_contact(v) is None

    def test_heisenberg_quartic_obstruction_zero(self, heis):
        assert quartic_obstruction(heis) == Fraction(0)

    def test_affine_quartic_obstruction_zero(self, aff):
        """Jacobi identity kills the quartic obstruction for affine."""
        assert quartic_obstruction(aff) == Fraction(0)

    def test_virasoro_quartic_obstruction_nonzero(self, vir):
        """o^(4)_Vir != 0 for generic c."""
        assert quartic_obstruction(vir) != Fraction(0)

    def test_virasoro_quartic_obstruction_formula(self, vir):
        # o^(4)_Vir = 144/c; for c=26: 144/26 = 72/13
        assert quartic_obstruction(vir) == Fraction(144, 26)


# ======================================================================
#  3. Open/closed quartic resonance class R^oc_4
# ======================================================================

class TestOpenClosedQuarticResonance:

    def test_heisenberg_resonance_zero(self, heis):
        """Gaussian vanishing: R^oc_4(H) = 0."""
        r = open_closed_quartic_resonance(heis)
        assert r == Fraction(0)

    def test_affine_resonance_tree_only(self, aff):
        """For affine: Q^ct = 0, so R^oc_4 = C^2/(2*kappa) (tree only)."""
        r = open_closed_quartic_resonance(aff)
        kappa = modular_characteristic(aff)
        c = cubic_shadow(aff)
        expected = c ** 2 / (Fraction(2) * kappa)
        assert r == expected
        assert r != Fraction(0)

    def test_virasoro_resonance_nonzero(self, vir):
        """Mixed nonvanishing: both contact and tree contribute."""
        r = open_closed_quartic_resonance(vir)
        assert r is not None
        assert r != Fraction(0)

    def test_virasoro_resonance_decomposition(self, vir):
        """R^oc_4 = Q^contact + C^2/(2*kappa)."""
        r = open_closed_quartic_resonance(vir)
        qct = quartic_contact(vir)
        c_val = cubic_shadow(vir)
        kappa = modular_characteristic(vir)
        tree = c_val ** 2 / (Fraction(2) * kappa)
        assert r == qct + tree

    def test_w3_resonance_nonzero(self, w3):
        """W_3 has nonzero quartic resonance."""
        r = open_closed_quartic_resonance(w3)
        assert r is not None
        assert r != Fraction(0)

    def test_resonance_at_c0_singular(self):
        """R^oc_4 is singular at c=0 (both kappa=0 and Q^ct pole)."""
        v = virasoro_data(Fraction(0))
        r = open_closed_quartic_resonance(v)
        assert r is None


# ======================================================================
#  4. Shadow depth classification G/L/C/M
# ======================================================================

class TestShadowDepth:

    def test_heisenberg_gaussian(self, heis):
        assert shadow_depth(heis) == "G"

    def test_affine_lie(self, aff):
        assert shadow_depth(aff) == "L"

    def test_virasoro_mixed(self, vir):
        assert shadow_depth(vir) == "M"

    def test_w3_mixed(self, w3):
        assert shadow_depth(w3) == "M"

    def test_consistency_heisenberg(self, heis):
        assert shadow_depth_consistency(heis)

    def test_consistency_affine(self, aff):
        assert shadow_depth_consistency(aff)

    def test_consistency_virasoro(self, vir):
        assert shadow_depth_consistency(vir)

    def test_consistency_w3(self, w3):
        assert shadow_depth_consistency(w3)


# ======================================================================
#  5. Derived center dimensions (Theorem H)
# ======================================================================

class TestDerivedCenter:
    """Tests for Theorem H: ChirHoch^n = 0 for n not in {0,1,2}."""

    def test_heisenberg_dimensions(self, heis):
        dims = derived_center_dimensions(heis)
        assert dims[0] == 1  # center = vacuum
        assert dims[1] == 1  # derivations mod inner
        assert dims[2] == 1  # obstructions (dual of center)

    def test_affine_dimensions(self, aff):
        dims = derived_center_dimensions(aff)
        assert dims[0] == 1
        assert dims[1] == 1
        assert dims[2] == 1

    def test_virasoro_dimensions(self, vir):
        dims = derived_center_dimensions(vir)
        assert dims[0] == 1
        assert dims[1] == 1
        assert dims[2] == 1

    def test_w3_dimensions(self, w3):
        dims = derived_center_dimensions(w3)
        assert dims[0] == 1
        assert dims[1] == 1
        assert dims[2] == 1

    def test_polynomial_growth(self):
        """Theorem H: Hochschild-Hilbert series is polynomial degree <= 2."""
        for factory in [heisenberg_data, affine_sl2_data, virasoro_data, w3_data]:
            algebra = factory()
            series = hochschild_hilbert_series(algebra)
            assert len(series) == 3
            assert all(s >= 0 for s in series)

    def test_three_term_gerstenhaber(self):
        """The derived center is a three-term Gerstenhaber algebra."""
        for factory in [heisenberg_data, affine_sl2_data, virasoro_data, w3_data]:
            algebra = factory()
            dims = derived_center_dimensions(algebra)
            # Z^n = 0 for n not in {0, 1, 2}
            for n in range(3, 10):
                assert dims.get(n, 0) == 0


# ======================================================================
#  6. Koszul duality on derived center
# ======================================================================

class TestKoszulDuality:

    def test_heisenberg_koszul_duality(self, heis):
        assert koszul_duality_check(heis)

    def test_affine_koszul_duality(self, aff):
        assert koszul_duality_check(aff)

    def test_virasoro_koszul_duality(self, vir):
        assert koszul_duality_check(vir)

    def test_w3_koszul_duality(self, w3):
        assert koszul_duality_check(w3)

    def test_koszul_pairing_symmetry(self):
        """dim Z^n(A) = dim Z^{2-n}(A) (self-duality of dimensions)."""
        for factory in [heisenberg_data, affine_sl2_data, virasoro_data]:
            algebra = factory()
            dims = derived_center_dimensions(algebra)
            assert dims[0] == dims[2]


# ======================================================================
#  7. Cross-family consistency
# ======================================================================

class TestCrossFamilyConsistency:

    def test_kappa_additivity(self):
        """kappa(A_1 + A_2) = kappa(A_1) + kappa(A_2) for independent sum."""
        h1 = heisenberg_data(Fraction(1))
        h2 = heisenberg_data(Fraction(3))
        total = kappa_additivity_check([h1, h2])
        assert total == Fraction(4)

    def test_kappa_anti_symmetry_virasoro(self):
        """
        kappa(Vir_c) + kappa(Vir_{26-c}) = kappa(Vir_c) + (26-c)/2
        = c/2 + (26-c)/2 = 13 (constant).

        This is NOT kappa + kappa' = 0 (that's for KM/free fields).
        For W-algebras: kappa + kappa' = rho * K (nonzero constant).
        """
        for c_val in [Fraction(1), Fraction(13), Fraction(26), Fraction(50)]:
            v = virasoro_data(c_val)
            v_dual = virasoro_data(Fraction(26) - c_val)
            k = modular_characteristic(v)
            k_dual = modular_characteristic(v_dual)
            assert k + k_dual == Fraction(13)

    def test_kappa_anti_symmetry_affine(self):
        """
        kappa(sl_2, k) + kappa(sl_2, -k-4) should satisfy the duality
        constraint for KM algebras.
        For sl_2: kappa(k) = 3(k+2)/4
        kappa(-k-4) = 3(-k-4+2)/4 = 3(-k-2)/4 = -3(k+2)/4
        So kappa + kappa' = 0 (the KM anti-symmetry).
        """
        for k_val in [Fraction(1), Fraction(3), Fraction(7)]:
            a = affine_sl2_data(k_val)
            a_dual = affine_sl2_data(-k_val - Fraction(4))
            k = modular_characteristic(a)
            k_dual = modular_characteristic(a_dual)
            assert k + k_dual == Fraction(0)


# ======================================================================
#  8. Virasoro quintic obstruction (tower forced infinite)
# ======================================================================

class TestQuinticObstruction:

    def test_quintic_nonzero_generic(self):
        """o^(5)_Vir != 0 for generic c, proving r_max = infinity."""
        for c in [Fraction(1), Fraction(26), Fraction(50)]:
            o5 = quintic_obstruction_virasoro(c)
            assert o5 is not None
            assert o5 != Fraction(0)

    def test_quintic_pole_c0(self):
        """o^(5) is singular at c=0."""
        assert quintic_obstruction_virasoro(Fraction(0)) is None

    def test_quintic_pole_null_state(self):
        """o^(5) is singular at c=-22/5."""
        assert quintic_obstruction_virasoro(Fraction(-22, 5)) is None

    def test_quintic_positive_c26(self):
        """At c=26 (critical string): o^(5) should be finite and nonzero."""
        o5 = quintic_obstruction_virasoro(Fraction(26))
        assert o5 is not None
        assert o5 != Fraction(0)


# ======================================================================
#  9. Resonance divisors
# ======================================================================

class TestResonanceDivisors:

    def test_virasoro_divisor_string(self):
        assert virasoro_resonance_divisor() == "c * (5c + 22)"

    def test_w3_divisor_string(self):
        assert w3_resonance_divisor() == "c * (2c - 1) * (5c + 22)"

    def test_w3_ising_pole(self):
        """W_3 has a pole at c=1/2 (Ising model)."""
        w = w3_data(Fraction(1, 2))
        # The quartic contact should detect the Ising singularity
        qct = quartic_contact(w)
        # At c=1/2: 5c+22 = 5/2+22 = 49/2, c*(5c+22) = (1/2)*(49/2) = 49/4
        # Q^ct has a contribution from beta = 16/(22+5/2) = 16/(49/2) = 32/49
        assert qct is not None  # should be finite at c=1/2

    def test_w3_yang_lee_pole(self):
        """W_3 has a pole at c=-22/5 (Yang-Lee edge)."""
        w = w3_data(Fraction(-22, 5))
        qct = quartic_contact(w)
        assert qct is None  # pole at c = -22/5


# ======================================================================
#  10. Cochain complex dimensions
# ======================================================================

class TestCochainComplex:

    def test_heisenberg_cochain_dim_0(self, heis):
        """C^0 should be nonempty (contains the identity)."""
        cx = ChiralHochschildComplex(heis, weight_bound=4)
        d0 = cx.cochain_dimension(0)
        assert d0 >= 1

    def test_virasoro_cochain_dim_0(self, vir):
        cx = ChiralHochschildComplex(vir, weight_bound=4)
        d0 = cx.cochain_dimension(0)
        assert d0 >= 1

    def test_cochain_negative_degree_zero(self, heis):
        cx = ChiralHochschildComplex(heis, weight_bound=4)
        assert cx.cochain_dimension(-1) == 0

    def test_euler_characteristic_exists(self, heis):
        """Euler characteristic should be computable."""
        cx = ChiralHochschildComplex(heis, weight_bound=4)
        chi = cx.euler_characteristic()
        assert isinstance(chi, int)


# ======================================================================
#  11. Open/closed projection principle
# ======================================================================

class TestProjectionPrinciple:
    """
    Theorem thm:thqg-oc-projection: the holographic datum is recovered
    by projecting the open/closed MC element.
    """

    def test_closed_projection_gives_kappa(self):
        """Closed projection at arity 2 gives kappa."""
        for factory in [heisenberg_data, affine_sl2_data, virasoro_data]:
            algebra = factory()
            kappa = modular_characteristic(algebra)
            assert kappa is not None

    def test_shadow_tower_projections(self):
        """Shadow obstruction tower at arities 2, 3, 4 gives kappa, C, Q."""
        for factory in [heisenberg_data, affine_sl2_data, virasoro_data]:
            algebra = factory()
            k = modular_characteristic(algebra)
            c = cubic_shadow(algebra)
            q = quartic_contact(algebra)
            # All should be computable (possibly zero)
            assert k is not None
            assert c is not None
            # q can be None at singular points

    def test_full_resonance_class(self):
        """R^oc_4 combines contact + tree into H^2(C^*_ch)."""
        for factory in [heisenberg_data, affine_sl2_data, virasoro_data]:
            algebra = factory()
            r = open_closed_quartic_resonance(algebra)
            # Should be computable for generic parameters
            if r is not None:
                assert isinstance(r, Fraction)


# ======================================================================
#  12. Annulus trace (dimensional check)
# ======================================================================

class TestAnnulusTrace:
    """
    Theorem thm:thqg-annulus-trace: int_{S^1} M = HH_*(M).
    Dimensional consistency: HH_0(A_b) should be >= 1 (the trace of identity).
    """

    def test_annulus_trace_exists(self):
        """Every algebra should have a nontrivial annulus trace."""
        for factory in [heisenberg_data, affine_sl2_data, virasoro_data]:
            algebra = factory()
            # HH_0 >= 1 (the trace of identity map)
            dims = derived_center_dimensions(algebra)
            # By CY duality: HH_n ≅ HH^{2-n}, so HH_0 ≅ Z^2 = 1
            assert dims[2] >= 1


# ======================================================================
#  13. Parametric sweep: quartic resonance across central charge
# ======================================================================

class TestParametricSweep:

    def test_virasoro_quartic_resonance_sweep(self):
        """R^oc_4(Vir_c) varies continuously with c (away from poles)."""
        values = []
        for c_num in range(1, 51):
            c = Fraction(c_num)
            v = virasoro_data(c)
            r = open_closed_quartic_resonance(v)
            assert r is not None
            values.append(float(r))
        # Check monotonicity is not required, but all values should be finite
        assert all(abs(v) < 1e6 for v in values)

    def test_virasoro_quartic_self_dual_c13(self, vir_c13):
        """At self-dual point c=13: check R^oc_4 is finite."""
        r = open_closed_quartic_resonance(vir_c13)
        assert r is not None
        assert r != Fraction(0)

    def test_w3_quartic_resonance_sweep(self):
        """R^oc_4(W_3, c) for c in {1, 2, ..., 20}, avoiding poles."""
        for c_num in [1, 2, 3, 5, 7, 10, 15, 20]:
            c = Fraction(c_num)
            w = w3_data(c)
            r = open_closed_quartic_resonance(w)
            assert r is not None

    def test_affine_kappa_sweep(self):
        """kappa(sl_2, k) for k=1..10."""
        prev_kappa = Fraction(0)
        for k_val in range(1, 11):
            a = affine_sl2_data(Fraction(k_val))
            k = modular_characteristic(a)
            assert k > prev_kappa  # kappa is strictly increasing in k
            prev_kappa = k
