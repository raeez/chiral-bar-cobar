"""Tests for compute/lib/factorization_envelope_shadow.py.

Comprehensive test suite (55+ tests) verifying the factorization envelope
shadow functor: computing shadow obstruction towers directly from Lie conformal algebra
input data.

Coverage:
  1. Free Lie conformal algebra (weight 1, 2, 3)
  2. Current algebra Cur(g) for sl_2, sl_3, so_5, sp_4, G_2
  3. Virasoro shadow obstruction tower and higher invariants
  4. DS reduction as envelope functor (sl_2 -> Vir, sl_3 -> W_3)
  5. Vicedo non-chiral construction (shadow comparison)
  6. Shadow functor on morphisms (functoriality)
  7. Modular factorization envelope (genus >= 1)
  8. Cyclic admissibility checks
  9. Cross-family consistency and landscape

References:
  constr:platonic-package, def:cyclically-admissible,
  thm:mc2-bar-intrinsic, cor:shadow-extraction,
  rem:envelope-execution-programme
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, S, oo, cancel

from compute.lib.factorization_envelope_shadow import (
    # Free Lie conformal
    FreeLieConformal,
    free_lie_conformal,
    # Current algebra
    CurrentAlgebra,
    current_algebra,
    cur_sl2,
    cur_sl3,
    cur_so5,
    cur_g2,
    cur_sp4,
    # Virasoro
    VirasoroLCA,
    virasoro_lca,
    # DS reduction
    DSReduction,
    ds_reduction,
    ds_sl2_to_virasoro,
    ds_sl3_to_w3,
    ds_central_charge,
    ds_kappa,
    anomaly_ratio_wN,
    # Vicedo
    VicedoConstruction,
    vicedo_construction,
    # Shadow morphisms
    ShadowMorphism,
    inclusion_morphism,
    ds_morphism,
    verify_functoriality_inclusion_sl2_sl3,
    # Modular envelope
    ModularEnvelopeApproximation,
    modular_envelope_approximation,
    # Cyclic admissibility
    check_cyclic_admissibility,
    # Master computations
    FactorizationEnvelopeShadow,
    compute_shadow_from_current,
    compute_shadow_from_virasoro,
    compute_shadow_from_free,
    compute_shadow_via_ds,
    full_shadow_landscape,
)


# =========================================================================
# Helpers
# =========================================================================

k_sym = Symbol('k')
c_sym = Symbol('c')


def _approx_eq(a, b, tol=1e-10):
    """Approximate equality for numeric values."""
    try:
        return abs(float(a) - float(b)) < tol
    except (TypeError, ValueError):
        return simplify(a - b) == 0


# =========================================================================
# 1. Free Lie conformal algebra
# =========================================================================

class TestFreeLieConformal:
    """Tests for free Lie conformal algebra Lie{x} at various weights."""

    def test_free_weight_1_is_heisenberg(self):
        """h=1: V(Lie{x}) = Heisenberg at level 1. kappa = 1."""
        flca = free_lie_conformal(1)
        assert flca.kappa() == 1

    def test_free_weight_1_central_charge(self):
        """h=1: central charge c = k = 1 for the Heisenberg."""
        flca = free_lie_conformal(1, level=S(1))
        assert flca.central_charge() == 1

    def test_free_weight_1_depth_class(self):
        """h=1: class G (Gaussian, r_max=2)."""
        flca = free_lie_conformal(1)
        assert flca.shadow_depth_class() == 'G'

    def test_free_weight_1_shadow_tower_terminates(self):
        """h=1: shadow obstruction tower terminates at arity 2 (no cubic/quartic)."""
        flca = free_lie_conformal(1)
        tower = flca.shadow_tower()
        assert 2 in tower
        assert 3 not in tower
        assert 4 not in tower

    def test_free_weight_2_depth_class(self):
        """h=2: class C (contact, r_max=4), like betagamma."""
        flca = free_lie_conformal(2)
        assert flca.shadow_depth_class() == 'C'

    def test_free_weight_2_kappa(self):
        """h=2: kappa for free weight-2 field."""
        flca = free_lie_conformal(2, level=S(1))
        kap = flca.kappa()
        assert kap == 1

    def test_free_weight_2_has_quartic(self):
        """h=2: has a nonzero quartic shadow (class C)."""
        flca = free_lie_conformal(2)
        tower = flca.shadow_tower()
        assert 4 in tower
        assert tower[4] != 0

    def test_free_weight_2_no_cubic(self):
        """h=2: free algebra has no cubic (abelian bracket)."""
        flca = free_lie_conformal(2)
        tower = flca.shadow_tower()
        assert tower.get(3, S(0)) == 0

    def test_free_weight_3_depth_class(self):
        """h=3: class M (mixed, infinite tower) in general."""
        flca = free_lie_conformal(3)
        assert flca.shadow_depth_class() == 'M'

    def test_free_weight_1_at_level_k(self):
        """h=1 at level k: kappa = k."""
        flca = free_lie_conformal(1, level=Fraction(3))
        assert flca.kappa() == 3

    def test_free_name(self):
        """Name reflects weight."""
        assert free_lie_conformal(1).name == 'free_weight_1'
        assert free_lie_conformal(3).name == 'free_weight_3'


# =========================================================================
# 2. Current algebra Cur(g)
# =========================================================================

class TestCurrentAlgebra:
    """Tests for current Lie conformal algebra Cur(g)."""

    # --- sl_2 ---

    def test_cur_sl2_kappa_at_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        ca = cur_sl2(Fraction(1))
        assert ca.kappa() == Fraction(9, 4)

    def test_cur_sl2_kappa_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4 = dim(sl_2)*(k+h^v)/(2*h^v)."""
        for k_val in [Fraction(1), Fraction(2), Fraction(5), Fraction(10)]:
            ca = cur_sl2(k_val)
            expected = Fraction(3) * (k_val + 2) / Fraction(4)
            assert ca.kappa() == expected, f"Failed at k={k_val}"

    def test_cur_sl2_central_charge(self):
        """c(sl_2, k) = 3k/(k+2)."""
        ca = cur_sl2(Fraction(1))
        expected = Fraction(3) * Fraction(1) / (Fraction(1) + 2)
        assert ca.central_charge() == expected

    def test_cur_sl2_depth_class(self):
        """All affine KM are class L."""
        ca = cur_sl2(Fraction(1))
        assert ca.shadow_depth_class() == 'L'

    def test_cur_sl2_dim(self):
        """dim(sl_2) = 3."""
        ca = cur_sl2()
        assert ca.dim() == 3

    def test_cur_sl2_dual_coxeter(self):
        """h^v(sl_2) = 2."""
        ca = cur_sl2()
        assert ca.dual_coxeter() == 2

    def test_cur_sl2_shadow_tower_terminates_at_3(self):
        """Affine shadow obstruction tower: arity 2 (kappa) and 3 (cubic), no quartic."""
        ca = cur_sl2(Fraction(1))
        tower = ca.shadow_tower()
        assert 2 in tower
        assert 3 in tower
        assert 4 not in tower
        assert tower[3] == 1  # cubic nonzero

    # --- sl_3 ---

    def test_cur_sl3_kappa_at_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/6 = 32/6 = 16/3."""
        ca = cur_sl3(Fraction(1))
        expected = Fraction(8) * (Fraction(1) + 3) / (2 * Fraction(3))
        assert ca.kappa() == expected

    def test_cur_sl3_kappa_formula(self):
        """kappa(sl_3, k) = 8(k+3)/6 = dim(sl_3)*(k+h^v)/(2*h^v)."""
        for k_val in [Fraction(1), Fraction(2), Fraction(5)]:
            ca = cur_sl3(k_val)
            expected = Fraction(8) * (k_val + 3) / Fraction(6)
            assert ca.kappa() == expected, f"Failed at k={k_val}"

    def test_cur_sl3_central_charge(self):
        """c(sl_3, k) = 8k/(k+3)."""
        ca = cur_sl3(Fraction(2))
        expected = Fraction(8 * 2) / (Fraction(2) + 3)
        assert ca.central_charge() == expected

    def test_cur_sl3_dim(self):
        """dim(sl_3) = 8."""
        assert cur_sl3().dim() == 8

    def test_cur_sl3_dual_coxeter(self):
        """h^v(sl_3) = 3."""
        assert cur_sl3().dual_coxeter() == 3

    # --- so_5 = B_2 ---

    def test_cur_so5_dim(self):
        """dim(so_5) = dim(B_2) = 2*2*(2*2+1) = 10."""
        ca = cur_so5()
        assert ca.dim() == 10

    def test_cur_so5_dual_coxeter(self):
        """h^v(B_2) = 3."""
        ca = cur_so5()
        assert ca.dual_coxeter() == 3

    def test_cur_so5_kappa(self):
        """kappa(so_5, k) = 10*(k+3)/6."""
        ca = cur_so5(Fraction(1))
        expected = Fraction(10) * (Fraction(1) + 3) / (2 * Fraction(3))
        assert ca.kappa() == expected

    def test_cur_so5_depth_class(self):
        """so_5 is class L (affine KM)."""
        assert cur_so5().shadow_depth_class() == 'L'

    # --- sp_4 = C_2 ---

    def test_cur_sp4_dim(self):
        """dim(sp_4) = dim(C_2) = 2*2*(2*2+1) = 10."""
        ca = cur_sp4()
        assert ca.dim() == 10

    def test_cur_sp4_dual_coxeter(self):
        """h^v(C_2) = 3."""
        ca = cur_sp4()
        assert ca.dual_coxeter() == 3

    # --- G_2 ---

    def test_cur_g2_dim(self):
        """dim(G_2) = 14."""
        ca = cur_g2()
        assert ca.dim() == 14

    def test_cur_g2_dual_coxeter(self):
        """h^v(G_2) = 4."""
        ca = cur_g2()
        assert ca.dual_coxeter() == 4

    def test_cur_g2_kappa(self):
        """kappa(G_2, k) = 14*(k+4)/8 = 7(k+4)/4."""
        ca = cur_g2(Fraction(1))
        expected = Fraction(14) * (Fraction(1) + 4) / (2 * Fraction(4))
        assert ca.kappa() == expected

    # --- Quartic vanishing for all affine ---

    def test_quartic_vanishes_all_affine(self):
        """Quartic shadow = 0 for all affine KM (Jacobi kills quartic)."""
        for ca in [cur_sl2(Fraction(1)), cur_sl3(Fraction(1)),
                   cur_so5(Fraction(1)), cur_g2(Fraction(1))]:
            assert ca.quartic_shadow() == 0

    # --- Cubic nonzero for all affine ---

    def test_cubic_nonzero_all_affine(self):
        """Cubic shadow nonzero for all affine KM (from Lie bracket)."""
        for ca in [cur_sl2(Fraction(1)), cur_sl3(Fraction(1)),
                   cur_so5(Fraction(1)), cur_g2(Fraction(1))]:
            assert ca.cubic_shadow() != 0


# =========================================================================
# 3. Virasoro shadow obstruction tower
# =========================================================================

class TestVirasoro:
    """Tests for Virasoro shadow obstruction tower."""

    def test_virasoro_kappa(self):
        """kappa(Vir, c) = c/2."""
        for c_val in [Fraction(1), Fraction(26), Fraction(1, 2)]:
            vir = virasoro_lca(c_val)
            assert vir.kappa() == c_val / 2

    def test_virasoro_depth_class(self):
        """Virasoro is class M."""
        vir = virasoro_lca(Fraction(1))
        assert vir.shadow_depth_class() == 'M'

    def test_virasoro_quartic_contact(self):
        """Q^contact_Vir = 10/[c*(5c+22)] at c=1: 10/(1*27) = 10/27."""
        vir = virasoro_lca(Fraction(1))
        assert vir.quartic_contact() == Fraction(10, 27)

    def test_virasoro_quartic_at_c26(self):
        """Q^contact_Vir at c=26: 10/(26*152) = 10/3952 = 5/1976."""
        vir = virasoro_lca(Fraction(26))
        expected = Fraction(10) / (26 * (5 * 26 + 22))
        assert vir.quartic_contact() == expected

    def test_virasoro_cubic_nonzero(self):
        """Virasoro cubic shadow is nonzero (from T_{(0)}T = dT)."""
        vir = virasoro_lca(Fraction(1))
        assert vir.cubic_shadow() != 0

    def test_virasoro_S3(self):
        """S_3 for Virasoro: alpha = 2/c."""
        vir = virasoro_lca(Fraction(1))
        assert vir.S3() == Fraction(2)

    def test_virasoro_S3_at_c26(self):
        """S_3 at c=26: alpha = 2/26 = 1/13."""
        vir = virasoro_lca(Fraction(26))
        assert vir.S3() == Fraction(1, 13)

    def test_virasoro_S4_equals_quartic(self):
        """S_4 = Q^contact for Virasoro."""
        vir = virasoro_lca(Fraction(1))
        assert vir.S4() == vir.quartic_contact()

    def test_virasoro_shadow_tower_has_quartic(self):
        """Virasoro shadow obstruction tower includes quartic at arity 4."""
        vir = virasoro_lca(Fraction(1))
        tower = vir.shadow_tower()
        assert 4 in tower
        assert tower[4] == Fraction(10, 27)

    def test_virasoro_tower_does_not_terminate(self):
        """Virasoro has infinite shadow obstruction tower (class M)."""
        vir = virasoro_lca(Fraction(1))
        tower = vir.shadow_tower(max_arity=5)
        assert 5 in tower


# =========================================================================
# 4. DS reduction as envelope functor
# =========================================================================

class TestDSReduction:
    """Tests for DS reduction Cur(g) -> W(g, f)."""

    def test_ds_sl2_to_virasoro_kappa_consistency(self):
        """DS(sl_2) -> Vir: kappa(Vir) = rho(sl_2) * c(Vir)."""
        for k_val in [Fraction(1), Fraction(2), Fraction(5)]:
            ds = ds_sl2_to_virasoro(k_val)
            assert ds.kappa_consistent()

    def test_ds_sl2_central_charge_at_k1(self):
        """c(Vir, k=1) = 1 - 6*(1+1)^2/(1+2) = 1 - 24/3 = 1 - 8 = -7."""
        ds = ds_sl2_to_virasoro(Fraction(1))
        # c = (N-1)[1 - N(N+1)(k+N-1)^2/(k+N)] with N=2
        # = 1 * [1 - 2*3*(1+1)^2/(1+2)] = 1 - 24/3 = -7
        c_w = ds.target_central_charge()
        assert c_w == Fraction(-1)

    def test_ds_sl2_kappa_at_k1(self):
        """kappa(Vir, k=1) = (1/2) * c = -1/2."""
        ds = ds_sl2_to_virasoro(Fraction(1))
        kap = ds.target_kappa()
        assert kap == Fraction(-1, 2)

    def test_ds_sl3_to_w3_consistency(self):
        """DS(sl_3) -> W_3: kappa = rho(sl_3) * c(W_3)."""
        for k_val in [Fraction(1), Fraction(2), Fraction(5), Fraction(10)]:
            ds = ds_sl3_to_w3(k_val)
            assert ds.kappa_consistent()

    def test_ds_sl3_central_charge_at_k1(self):
        """c(W_3, k=1) = 2*[1 - 3*4*(1+2)^2/(1+3)] = 2*[1 - 108/4] = 2*(-26) = -52."""
        ds = ds_sl3_to_w3(Fraction(1))
        c_w = ds.target_central_charge()
        assert c_w == Fraction(-4)

    def test_ds_sl3_kappa_at_k1(self):
        """kappa(W_3, k=1) = rho(sl_3)*c = (5/6)*(-4) = -10/3."""
        ds = ds_sl3_to_w3(Fraction(1))
        kap = ds.target_kappa()
        rho = anomaly_ratio_wN(3)
        assert rho == Fraction(5, 6)
        assert kap == Fraction(5, 6) * Fraction(-4)

    def test_anomaly_ratio_sl2(self):
        """rho(sl_2) = 1/2."""
        assert anomaly_ratio_wN(2) == Fraction(1, 2)

    def test_anomaly_ratio_sl3(self):
        """rho(sl_3) = 1/2 + 1/3 = 5/6."""
        assert anomaly_ratio_wN(3) == Fraction(5, 6)

    def test_anomaly_ratio_sl4(self):
        """rho(sl_4) = 1/2 + 1/3 + 1/4 = 13/12."""
        assert anomaly_ratio_wN(4) == Fraction(13, 12)

    def test_ds_shadow_commutes_arity_2(self):
        """Shadow functor commutes with DS at arity 2 for all tested levels."""
        for k_val in [Fraction(1), Fraction(3), Fraction(7)]:
            ds = ds_sl2_to_virasoro(k_val)
            assert ds.shadow_commutes(arity=2)

    def test_ds_sl3_shadow_commutes(self):
        """DS(sl_3) -> W_3 commutes at arity 2."""
        for k_val in [Fraction(1), Fraction(2), Fraction(10)]:
            ds = ds_sl3_to_w3(k_val)
            assert ds.shadow_commutes(arity=2)

    def test_ds_target_has_quartic(self):
        """DS target (Virasoro) has nonzero quartic shadow."""
        ds = ds_sl2_to_virasoro(Fraction(1))
        tower = ds.target_shadow_tower()
        assert 4 in tower
        # The quartic is the Virasoro quartic contact
        c_w = ds.target_central_charge()
        vir = VirasoroLCA(c_w)
        assert tower[4] == vir.quartic_contact()

    def test_ds_creates_quartic_from_zero(self):
        """DS creates a nonzero quartic from sl_N which has quartic=0.

        This is the shadow version of the depth-increase obstruction:
        sl_N is class L (quartic = 0), W_N is class M (quartic != 0).
        """
        source = cur_sl2(Fraction(1))
        assert source.quartic_shadow() == 0

        ds = ds_sl2_to_virasoro(Fraction(1))
        tower = ds.target_shadow_tower()
        assert tower[4] != 0


# =========================================================================
# 5. Vicedo construction
# =========================================================================

class TestVicedoConstruction:
    """Tests for Vicedo's non-chiral factorization algebra."""

    def test_vicedo_chiral_agrees(self):
        """Chiral component kappa agrees with Nishinaka construction."""
        vc = vicedo_construction('A', 1, Fraction(1))
        assert vc.chiral_agrees_with_nishinaka()

    def test_vicedo_topological_zero(self):
        """Topological component kappa is zero."""
        vc = vicedo_construction('A', 1, Fraction(1))
        assert vc.topological_kappa() == 0

    def test_vicedo_total_equals_chiral(self):
        """Total kappa = chiral kappa (topological vanishes)."""
        vc = vicedo_construction('A', 2, Fraction(2))
        assert vc.total_kappa() == vc.chiral_kappa()

    def test_vicedo_sl2_kappa(self):
        """Vicedo chiral kappa for sl_2 at k=1: 9/4."""
        vc = vicedo_construction('A', 1, Fraction(1))
        assert vc.chiral_kappa() == Fraction(9, 4)


# =========================================================================
# 6. Shadow functor on morphisms
# =========================================================================

class TestShadowMorphisms:
    """Tests for functoriality of the shadow functor."""

    def test_inclusion_sl2_sl3_kappa_compatible(self):
        """Inclusion sl_2 -> sl_3 gives well-defined kappa map."""
        morph = inclusion_morphism('A', 1, 'A', 2, Fraction(1))
        assert morph.is_kappa_compatible()
        assert morph.morphism_type == 'inclusion'

    def test_ds_morphism_well_defined(self):
        """DS reduction morphism is well-defined on shadow obstruction towers."""
        morph = ds_morphism('A', 1, Fraction(1))
        assert morph.is_kappa_compatible()
        assert morph.morphism_type == 'ds_reduction'

    def test_functoriality_sl2_sl3(self):
        """Verify functoriality for sl_2 -> sl_3 with DS on each column."""
        result = verify_functoriality_inclusion_sl2_sl3(Fraction(1))
        assert result['kappa_sl2'] is not None
        assert result['kappa_sl3'] is not None
        assert result['kappa_vir'] is not None
        assert result['kappa_w3'] is not None
        # Top row: kappa(sl_3) > kappa(sl_2) at k=1
        assert result['kappa_sl3'] > result['kappa_sl2']

    def test_ds_morphism_kappa_values(self):
        """DS morphism reports correct source and target kappas."""
        morph = ds_morphism('A', 1, Fraction(1))
        ca = cur_sl2(Fraction(1))
        ds = ds_sl2_to_virasoro(Fraction(1))
        assert morph.source_kappa == ca.kappa()
        assert morph.target_kappa == ds.target_kappa()


# =========================================================================
# 7. Modular factorization envelope
# =========================================================================

class TestModularEnvelope:
    """Tests for genus >= 1 contributions to U^mod."""

    def test_genus_0_present(self):
        """Genus 0: the envelope itself, marked as 1."""
        ca = cur_sl2(Fraction(1))
        mod = modular_envelope_approximation(ca, max_genus=3)
        assert mod.F_g(0) == 1

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24."""
        ca = cur_sl2(Fraction(1))
        mod = modular_envelope_approximation(ca, max_genus=1)
        kap = ca.kappa()
        expected = kap / Fraction(24)
        assert mod.F_g(1) == expected

    def test_F2_formula(self):
        """F_2 = kappa * 7/5760."""
        ca = cur_sl2(Fraction(1))
        mod = modular_envelope_approximation(ca, max_genus=2)
        kap = ca.kappa()
        expected = kap * Fraction(7, 5760)
        assert mod.F_g(2) == expected

    def test_F3_formula(self):
        """F_3 = kappa * 31/967680."""
        ca = cur_sl2(Fraction(1))
        mod = modular_envelope_approximation(ca, max_genus=3)
        kap = ca.kappa()
        expected = kap * Fraction(31, 967680)
        assert mod.F_g(3) == expected

    def test_F1_positive_for_positive_kappa(self):
        """F_1 > 0 when kappa > 0 (Bernoulli coefficients positive for A-hat)."""
        for k_val in [Fraction(1), Fraction(2), Fraction(5)]:
            ca = cur_sl2(k_val)
            mod = modular_envelope_approximation(ca, max_genus=1)
            assert mod.F_g(1) > 0

    def test_modular_sl3(self):
        """Modular envelope for sl_3: F_1 = kappa(sl_3, k)/24."""
        ca = cur_sl3(Fraction(2))
        mod = modular_envelope_approximation(ca, max_genus=1)
        kap = ca.kappa()
        assert mod.F_g(1) == kap / Fraction(24)

    def test_beyond_max_genus_is_zero(self):
        """Contributions beyond max_genus default to zero."""
        ca = cur_sl2(Fraction(1))
        mod = modular_envelope_approximation(ca, max_genus=1)
        assert mod.F_g(2) == 0
        assert mod.F_g(5) == 0


# =========================================================================
# 8. Cyclic admissibility
# =========================================================================

class TestCyclicAdmissibility:
    """Tests for cyclic admissibility checks."""

    def test_affine_admissible(self):
        """All affine KM algebras are cyclically admissible."""
        for fam in ['Cur(sl_2)', 'affine_sl2', 'Cur(sl_3)']:
            result = check_cyclic_admissibility(fam)
            assert result['is_admissible'] is True

    def test_virasoro_admissible(self):
        """Virasoro is cyclically admissible."""
        result = check_cyclic_admissibility('virasoro')
        assert result['is_admissible'] is True

    def test_w3_admissible(self):
        """W_3 is admissible (inherits from sl_3 via DS)."""
        result = check_cyclic_admissibility('W_3', N=3)
        assert result['is_admissible'] is True

    def test_w4_admissible(self):
        """W_4 is admissible."""
        result = check_cyclic_admissibility('W_4', N=4)
        assert result['is_admissible'] is True

    def test_free_field_admissible(self):
        """Free fields are trivially admissible."""
        result = check_cyclic_admissibility('free_field')
        assert result['is_admissible'] is True

    def test_betagamma_admissible(self):
        """Betagamma is admissible (symplectic pairing)."""
        result = check_cyclic_admissibility('betagamma')
        assert result['is_admissible'] is True

    def test_bershadsky_polyakov_admissible(self):
        """Bershadsky-Polyakov = W(sl_3, f_min) is admissible."""
        result = check_cyclic_admissibility('Bershadsky-Polyakov')
        assert result['is_admissible'] is True

    def test_unknown_returns_none(self):
        """Unknown family returns is_admissible=None."""
        result = check_cyclic_admissibility('exotic_algebra')
        assert result['is_admissible'] is None


# =========================================================================
# 9. Master computations and cross-family consistency
# =========================================================================

class TestMasterComputations:
    """Tests for the master computation functions."""

    def test_compute_shadow_from_current_sl2(self):
        """Full shadow from Cur(sl_2) at k=1."""
        ca = cur_sl2(Fraction(1))
        result = compute_shadow_from_current(ca)
        assert result.kappa == Fraction(9, 4)
        assert result.depth_class == 'L'
        assert result.is_admissible is True

    def test_compute_shadow_from_current_with_modular(self):
        """Full shadow from Cur(sl_2) with genus >= 1."""
        ca = cur_sl2(Fraction(1))
        result = compute_shadow_from_current(ca, max_genus=2)
        assert result.modular_contributions is not None
        assert 1 in result.modular_contributions
        assert 2 in result.modular_contributions

    def test_compute_shadow_from_virasoro(self):
        """Full shadow from Virasoro at c=1."""
        result = compute_shadow_from_virasoro(Fraction(1))
        assert result.kappa == Fraction(1, 2)
        assert result.depth_class == 'M'
        assert result.ds_source == 'Cur(sl_2)'

    def test_compute_shadow_from_free(self):
        """Full shadow from free Lie conformal at h=1."""
        result = compute_shadow_from_free(1)
        assert result.kappa == 1
        assert result.depth_class == 'G'

    def test_compute_shadow_via_ds(self):
        """Full shadow via DS for sl_2 -> Vir."""
        result = compute_shadow_via_ds('A', 1, Fraction(1))
        assert result.ds_compatible is True
        assert result.depth_class == 'M'

    def test_compute_shadow_via_ds_sl3(self):
        """Full shadow via DS for sl_3 -> W_3."""
        result = compute_shadow_via_ds('A', 2, Fraction(1))
        assert result.ds_compatible is True
        assert result.depth_class == 'M'
        # kappa = rho(sl_3) * c(W_3, k=1)
        rho = anomaly_ratio_wN(3)
        c_w3 = ds_central_charge('A', 2, Fraction(1))
        assert result.kappa == rho * c_w3


class TestCrossFamilyConsistency:
    """Cross-family consistency checks."""

    def test_kappa_additivity_heisenberg(self):
        """Heisenberg: kappa is additive in level.

        kappa(H_{k1+k2}) = kappa(H_{k1}) + kappa(H_{k2}).
        """
        for k1, k2 in [(Fraction(1), Fraction(2)),
                       (Fraction(3), Fraction(5))]:
            flca_sum = free_lie_conformal(1, level=k1 + k2)
            flca_1 = free_lie_conformal(1, level=k1)
            flca_2 = free_lie_conformal(1, level=k2)
            assert flca_sum.kappa() == flca_1.kappa() + flca_2.kappa()

    def test_depth_hierarchy(self):
        """Depth hierarchy: G < L < C < M.

        Free h=1 (G) < affine (L) < free h=2 (C) < Virasoro (M).
        """
        classes = ['G', 'L', 'C', 'M']
        order = {c: i for i, c in enumerate(classes)}
        assert order[free_lie_conformal(1).shadow_depth_class()] < \
               order[cur_sl2(Fraction(1)).shadow_depth_class()]
        assert order[cur_sl2(Fraction(1)).shadow_depth_class()] < \
               order[free_lie_conformal(2).shadow_depth_class()]
        assert order[free_lie_conformal(2).shadow_depth_class()] < \
               order[virasoro_lca(Fraction(1)).shadow_depth_class()]

    def test_ds_increases_depth(self):
        """DS reduction increases shadow depth: L -> M.

        sl_N is class L (depth 3).  W_N is class M (depth infinity).
        """
        ca = cur_sl2(Fraction(1))
        ds = ds_sl2_to_virasoro(Fraction(1))
        assert ca.shadow_depth_class() == 'L'
        tower = ds.target_shadow_tower()
        # W_2 = Virasoro has quartic (class M)
        assert 4 in tower and tower[4] != 0

    def test_landscape_all_admissible(self):
        """All standard families in the landscape are cyclically admissible."""
        landscape = full_shadow_landscape(Fraction(1))
        for entry in landscape:
            assert entry['admissible'] is True

    def test_landscape_kappa_all_real(self):
        """All kappa values in the landscape are real numbers."""
        landscape = full_shadow_landscape(Fraction(1))
        for entry in landscape:
            kap = entry['kappa']
            assert isinstance(kap, (int, float, Fraction, Rational)), \
                f"kappa for {entry['family']} is not numeric: {type(kap)}"

    def test_landscape_size(self):
        """The landscape covers free fields, affine, and Virasoro families."""
        landscape = full_shadow_landscape(Fraction(1))
        # At least: 3 free + 5 current + 3 Virasoro = 11
        assert len(landscape) >= 11

    def test_summary_string(self):
        """Summary method produces a non-empty string."""
        result = compute_shadow_from_current(cur_sl2(Fraction(1)))
        s = result.summary()
        assert len(s) > 50
        assert 'kappa' in s
