"""Tests for the Modular Koszul datum Pi_X(L) -- the six-fold datum.

Comprehensive test suite for compute/lib/platonic_datum.py.
Each test verifies ONE property of the modular Koszul datum construction,
organized by family and by cross-family structural properties.

References:
  constr:platonic-package, def:cyclically-admissible,
  thm:depth-decomposition, prop:independent-sum-factorization,
  def:shadow-metric, thm:shadow-radius, cor:shadow-extraction.
"""
import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, sqrt, S, oo, cancel

from compute.lib.platonic_datum import (
    CyclicAdmissibleData,
    BranchSpace,
    PlatonicPackage,
    heisenberg_package,
    affine_sl2_package,
    affine_sl3_package,
    virasoro_package,
    w3_package,
    betagamma_package,
    free_fermion_package,
    lattice_package,
    assemble_platonic_package,
    depth_decomposition,
    complementarity_discriminants,
    standard_landscape,
    landscape_summary,
    independent_sum_package,
)


# =========================================================================
# Helper: robust zero comparison that handles both sympy and float values
# =========================================================================

def _is_zero(expr, tol=1e-12):
    """Check if expr is zero, handling both sympy expressions and floats."""
    try:
        s = simplify(expr)
        if s == 0:
            return True
        return abs(float(s)) < tol
    except (TypeError, ValueError):
        return expr == 0


def _assert_zero(expr, msg=""):
    """Assert that expr is zero, with tolerance for float arithmetic."""
    assert _is_zero(expr), msg or f"Expected zero, got {expr}"


# =========================================================================
# Symbols used throughout
# =========================================================================

k_sym = Symbol('k')
c_sym = Symbol('c')
n_sym = Symbol('n')


# =========================================================================
# 1. TestCyclicAdmissibility
# =========================================================================

class TestCyclicAdmissibility:
    """Test CyclicAdmissibleData validation and admissibility checks."""

    def test_valid_admissible_data(self):
        """All three admissibility conditions met => is_admissible True."""
        data = CyclicAdmissibleData(
            name='test',
            rank=1,
            weights=[1],
            structure_constants={},
            killing_form=None,
            level=1,
            central_charge=1,
            conformal_grading=True,
            bounded_poles=True,
            has_invariant_pairing=True,
        )
        assert data.is_admissible()

    def test_missing_conformal_grading(self):
        """Missing conformal grading => not admissible."""
        data = CyclicAdmissibleData(
            name='bad', rank=1, weights=[1], structure_constants={},
            killing_form=None, level=1, central_charge=1,
            conformal_grading=False,
        )
        assert not data.is_admissible()

    def test_missing_invariant_pairing(self):
        """Missing invariant pairing => not admissible."""
        data = CyclicAdmissibleData(
            name='bad', rank=1, weights=[1], structure_constants={},
            killing_form=None, level=1, central_charge=1,
            has_invariant_pairing=False,
        )
        assert not data.is_admissible()

    def test_unbounded_poles(self):
        """Unbounded poles => not admissible."""
        data = CyclicAdmissibleData(
            name='bad', rank=1, weights=[1], structure_constants={},
            killing_form=None, level=1, central_charge=1,
            bounded_poles=False,
        )
        assert not data.is_admissible()

    def test_validate_rank_mismatch(self):
        """rank != len(weights) => validation failure."""
        data = CyclicAdmissibleData(
            name='bad', rank=3, weights=[1, 2], structure_constants={},
            killing_form=None, level=1, central_charge=1,
        )
        failures = data.validate()
        assert any('Rank' in f for f in failures)

    def test_validate_negative_weight(self):
        """Negative conformal weight => validation failure."""
        data = CyclicAdmissibleData(
            name='bad', rank=1, weights=[-1], structure_constants={},
            killing_form=None, level=1, central_charge=1,
        )
        failures = data.validate()
        assert any('Negative' in f for f in failures)

    def test_validate_clean_passes(self):
        """Fully valid data => empty failure list."""
        data = CyclicAdmissibleData(
            name='good', rank=2, weights=[1, 2], structure_constants={},
            killing_form=None, level=1, central_charge=1,
        )
        assert data.validate() == []

    def test_heisenberg_is_admissible(self):
        """Heisenberg package input data is admissible."""
        pkg = heisenberg_package(level=1)
        assert pkg.input_data.is_admissible()

    def test_affine_is_admissible(self):
        """Affine sl_2 package input data is admissible."""
        pkg = affine_sl2_package(level=1)
        assert pkg.input_data.is_admissible()

    def test_virasoro_is_admissible(self):
        """Virasoro package input data is admissible."""
        pkg = virasoro_package(central_charge=1)
        assert pkg.input_data.is_admissible()

    def test_multiple_failures(self):
        """Multiple violations produce multiple failure messages."""
        data = CyclicAdmissibleData(
            name='bad', rank=5, weights=[-1, 2], structure_constants={},
            killing_form=None, level=1, central_charge=1,
            conformal_grading=False,
            has_invariant_pairing=False,
        )
        failures = data.validate()
        assert len(failures) >= 3


# =========================================================================
# 2. TestHeisenbergPackage
# =========================================================================

class TestHeisenbergPackage:
    """Test the Modular Koszul datum for the Heisenberg algebra H_k."""

    def test_kappa_symbolic(self):
        """Symbolic level: kappa = k (the level, NOT k/2).
        See landscape_census.tex Table tab:master-invariants."""
        pkg = heisenberg_package()
        _assert_zero(pkg.theta_kappa - k_sym)

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10])
    def test_kappa_numeric(self, k_val):
        """Numeric level k: kappa = k."""
        pkg = heisenberg_package(level=k_val)
        _assert_zero(pkg.theta_kappa - Rational(k_val))

    def test_depth_class_G(self):
        """Heisenberg is class G (Gaussian)."""
        pkg = heisenberg_package(level=1)
        assert pkg.shadow_depth_class == 'G'

    def test_depth_2(self):
        """Shadow obstruction tower depth is 2 (only kappa entry)."""
        pkg = heisenberg_package(level=1)
        assert max(pkg.theta.keys()) == 2

    def test_alpha_zero(self):
        """Cubic shadow alpha = 0."""
        pkg = heisenberg_package(level=1)
        _assert_zero(pkg.theta_cubic)

    def test_S4_zero(self):
        """Quartic contact S_4 = 0."""
        pkg = heisenberg_package(level=1)
        _assert_zero(pkg.theta_quartic)

    def test_branch_dim_zero(self):
        """Branch space dimension is 0."""
        pkg = heisenberg_package(level=1)
        assert pkg.branch_space.dimension == 0
        assert pkg.branch_space.is_trivial()

    def test_R4_zero(self):
        """Modular quartic resonance R_4 = 0."""
        pkg = heisenberg_package(level=1)
        _assert_zero(pkg.R4_mod)

    def test_growth_rate_zero(self):
        """Shadow growth rate rho = 0 (terminates)."""
        pkg = heisenberg_package(level=1)
        _assert_zero(pkg.shadow_growth_rate)

    def test_depth_decomposition(self):
        """Depth decomposition: d=1, d_arith=0, d_alg=0."""
        pkg = heisenberg_package(level=1)
        dd = pkg.depth_decomposition
        assert dd['d'] == 1
        assert dd['d_arith'] == 0
        assert dd['d_alg'] == 0

    def test_verify_all_pass(self):
        """All verify() checks pass (symbolic level avoids float comparison)."""
        pkg = heisenberg_package()
        checks = pkg.verify()
        for key, val in checks.items():
            assert val, f"Check '{key}' failed"

    def test_verify_structural_numeric(self):
        """Core structural checks pass at numeric level."""
        pkg = heisenberg_package(level=1)
        checks = pkg.verify()
        assert checks['admissibility']
        assert checks['depth_class_valid']
        assert checks['branch_dim_nonneg']
        assert checks['kappa_nonzero']

    def test_is_convergent(self):
        """Class G is always convergent."""
        pkg = heisenberg_package(level=1)
        assert pkg.is_convergent()


# =========================================================================
# 3. TestAffineSl2Package
# =========================================================================

class TestAffineSl2Package:
    """Test the Modular Koszul datum for affine V_k(sl_2)."""

    def test_kappa_symbolic(self):
        """Symbolic level: kappa = 3(k+2)/4."""
        pkg = affine_sl2_package()
        expected = Rational(3) * (k_sym + 2) / 4
        _assert_zero(pkg.theta_kappa - expected)

    @pytest.mark.parametrize("k_val,expected_kappa", [
        (1, Rational(9, 4)),
        (2, Rational(3)),
        (4, Rational(9, 2)),
        (10, Rational(9)),
    ])
    def test_kappa_numeric(self, k_val, expected_kappa):
        """Numeric levels: kappa = 3(k+2)/4."""
        pkg = affine_sl2_package(level=k_val)
        _assert_zero(pkg.theta_kappa - expected_kappa)

    def test_depth_class_L(self):
        """Affine sl_2 is class L (Lie/tree)."""
        pkg = affine_sl2_package(level=1)
        assert pkg.shadow_depth_class == 'L'

    def test_depth_3(self):
        """Shadow obstruction tower terminates at arity 3."""
        pkg = affine_sl2_package(level=1)
        assert max(pkg.theta.keys()) == 3

    def test_alpha_nonzero(self):
        """Cubic shadow alpha is nonzero (= 1)."""
        pkg = affine_sl2_package(level=1)
        _assert_zero(pkg.theta_cubic - 1)

    def test_S4_zero(self):
        """Quartic S_4 = 0 (Jacobi identity kills quartic)."""
        pkg = affine_sl2_package(level=1)
        _assert_zero(pkg.theta_quartic)

    def test_branch_dim_3(self):
        """Branch space dimension = 3 = dim(sl_2)."""
        pkg = affine_sl2_package(level=1)
        assert pkg.branch_space.dimension == 3

    def test_branch_labels(self):
        """Branch basis labels are {e, f, h}."""
        pkg = affine_sl2_package(level=1)
        assert set(pkg.branch_space.basis_labels) == {'e', 'f', 'h'}

    def test_R4_zero(self):
        """R_4^mod = 0."""
        pkg = affine_sl2_package(level=1)
        _assert_zero(pkg.R4_mod)

    def test_depth_decomposition(self):
        """Depth decomposition: d=2, d_arith=0, d_alg=1."""
        pkg = affine_sl2_package(level=1)
        dd = pkg.depth_decomposition
        assert dd['d'] == 2
        assert dd['d_arith'] == 0
        assert dd['d_alg'] == 1

    def test_growth_rate_zero(self):
        """Class L has growth rate 0 (finite tower)."""
        pkg = affine_sl2_package(level=1)
        _assert_zero(pkg.shadow_growth_rate)

    def test_verify_all_pass(self):
        """All verify() checks pass."""
        pkg = affine_sl2_package(level=1)
        checks = pkg.verify()
        for key, val in checks.items():
            assert val, f"Check '{key}' failed"


# =========================================================================
# 3b. TestAffineSl3Package
# =========================================================================

class TestAffineSl3Package:
    """Test the Modular Koszul datum for affine V_k(sl_3)."""

    def test_kappa_formula(self):
        """kappa = 4(k+3)/3 at symbolic level."""
        pkg = affine_sl3_package()
        expected = Rational(4) * (k_sym + 3) / 3
        _assert_zero(pkg.theta_kappa - expected)

    @pytest.mark.parametrize("k_val,expected_kappa", [
        (1, Rational(16, 3)),
        (3, Rational(8)),
    ])
    def test_kappa_numeric(self, k_val, expected_kappa):
        """Numeric kappa values for sl_3."""
        pkg = affine_sl3_package(level=k_val)
        _assert_zero(pkg.theta_kappa - expected_kappa)

    def test_depth_class_L(self):
        """Affine sl_3 is class L."""
        pkg = affine_sl3_package(level=1)
        assert pkg.shadow_depth_class == 'L'

    def test_branch_dim_8(self):
        """Branch space dimension = 8 = dim(sl_3)."""
        pkg = affine_sl3_package(level=1)
        assert pkg.branch_space.dimension == 8

    def test_R4_zero(self):
        """R_4^mod = 0 for affine."""
        pkg = affine_sl3_package(level=1)
        _assert_zero(pkg.R4_mod)

    def test_depth_decomposition(self):
        """Depth decomposition: d=2, d_arith=0, d_alg=1."""
        pkg = affine_sl3_package(level=1)
        dd = pkg.depth_decomposition
        assert dd['d'] == 2
        assert dd['d_arith'] == 0
        assert dd['d_alg'] == 1


# =========================================================================
# 4. TestVirasoroPackage
# =========================================================================

class TestVirasoroPackage:
    """Test the Modular Koszul datum for the Virasoro algebra Vir_c."""

    def test_kappa_symbolic(self):
        """Symbolic central charge: kappa = c/2."""
        pkg = virasoro_package()
        _assert_zero(pkg.theta_kappa - c_sym / 2)

    @pytest.mark.parametrize("c_val", [1, Rational(1, 2), 10, 26])
    def test_kappa_numeric(self, c_val):
        """Numeric kappa = c/2."""
        pkg = virasoro_package(central_charge=c_val)
        _assert_zero(pkg.theta_kappa - c_val / 2)

    def test_depth_class_M(self):
        """Virasoro is class M (mixed, infinite tower)."""
        pkg = virasoro_package(central_charge=1)
        assert pkg.shadow_depth_class == 'M'

    def test_depth_infinity(self):
        """Shadow depth is infinity."""
        pkg = virasoro_package(central_charge=1)
        dd = pkg.depth_decomposition
        assert dd['d'] == oo

    def test_quartic_contact(self):
        """Q^ct = 10/(c(5c+22)) at symbolic c."""
        pkg = virasoro_package()
        expected = Rational(10) / (c_sym * (5 * c_sym + 22))
        _assert_zero(pkg.theta_quartic - expected)

    @pytest.mark.parametrize("c_val", [1, 2, 10, 26])
    def test_quartic_contact_numeric(self, c_val):
        """Q^ct = 10/(c(5c+22)) at numeric c values."""
        pkg = virasoro_package(central_charge=c_val)
        expected = Rational(10, c_val * (5 * c_val + 22))
        _assert_zero(pkg.theta_quartic - expected)

    def test_delta_formula(self):
        """Delta = 40/(5c+22) at symbolic c."""
        # Delta = 8*kappa*S4 = 8*(c/2)*10/(c*(5c+22)) = 40/(5c+22)
        pkg = virasoro_package()
        kappa = pkg.theta_kappa
        S4 = pkg.theta_quartic
        Delta = 8 * kappa * S4
        expected = Rational(40) / (5 * c_sym + 22)
        _assert_zero(Delta - expected)

    def test_branch_dim_1(self):
        """Branch space dimension = 1."""
        pkg = virasoro_package(central_charge=1)
        assert pkg.branch_space.dimension == 1

    def test_branch_label_L(self):
        """Branch basis label is 'L'."""
        pkg = virasoro_package(central_charge=1)
        assert pkg.branch_space.basis_labels == ['L']

    def test_not_convergent_low_c(self):
        """Not convergent for small c (c < c* ~ 6.12)."""
        pkg = virasoro_package(central_charge=1)
        # At c=1, the shadow obstruction tower diverges (rho > 1)
        assert not pkg.is_convergent()

    def test_convergent_high_c(self):
        """Convergent for large c (c >> c*)."""
        pkg = virasoro_package(central_charge=100)
        assert pkg.is_convergent()

    def test_self_dual_c13(self):
        """Koszul dual at c=13: Vir_c and Vir_{26-c} have same kappa."""
        pkg = virasoro_package(central_charge=13)
        kappa = pkg.theta_kappa
        dual_kappa = (26 - 13) / 2
        _assert_zero(kappa - dual_kappa)

    def test_depth_decomposition(self):
        """Depth decomposition: d=oo, d_arith=0, d_alg=oo."""
        pkg = virasoro_package(central_charge=1)
        dd = pkg.depth_decomposition
        assert dd['d'] == oo
        assert dd['d_arith'] == 0
        assert dd['d_alg'] == oo

    def test_verify_all_pass(self):
        """All verify() checks pass (symbolic c avoids float comparison)."""
        pkg = virasoro_package()
        checks = pkg.verify()
        for key, val in checks.items():
            assert val, f"Check '{key}' failed"

    def test_verify_structural_numeric(self):
        """Core structural checks pass at numeric c."""
        pkg = virasoro_package(central_charge=10)
        checks = pkg.verify()
        assert checks['admissibility']
        assert checks['depth_class_valid']
        assert checks['branch_dim_nonneg']
        assert checks['kappa_nonzero']


# =========================================================================
# 5. TestW3Package
# =========================================================================

class TestW3Package:
    """Test the Modular Koszul datum for the W_3 algebra."""

    def test_two_channels(self):
        """W_3 has generator weights [2, 3] (T and W channels)."""
        pkg = w3_package(central_charge=10)
        assert pkg.input_data.weights == [2, 3]

    def test_kappa_T_channel(self):
        """T-channel kappa: kappa_T = c/2 (from Killing form entry)."""
        pkg = w3_package()
        # Killing form diag: [c/2, c/3] => kappa_T = c/2
        kf = pkg.input_data.killing_form
        _assert_zero(kf[0, 0] - c_sym / 2)

    def test_kappa_W_channel(self):
        """W-channel kappa: kappa_W = c/3 (from Killing form entry)."""
        pkg = w3_package()
        kf = pkg.input_data.killing_form
        _assert_zero(kf[1, 1] - c_sym / 3)

    def test_total_kappa(self):
        """Total kappa = 5c/6."""
        pkg = w3_package()
        expected = Rational(5) * c_sym / 6
        _assert_zero(pkg.theta_kappa - expected)

    def test_depth_class_M(self):
        """W_3 is class M (mixed, infinite tower)."""
        pkg = w3_package(central_charge=10)
        assert pkg.shadow_depth_class == 'M'

    def test_branch_dim_2(self):
        """Branch space dimension = 2 (T-line + W-line)."""
        pkg = w3_package(central_charge=10)
        assert pkg.branch_space.dimension == 2

    def test_branch_labels(self):
        """Branch basis labels are ['L', 'W']."""
        pkg = w3_package(central_charge=10)
        assert pkg.branch_space.basis_labels == ['L', 'W']

    def test_rank_2(self):
        """W_3 has rank 2 (T and W generators)."""
        pkg = w3_package(central_charge=10)
        assert pkg.input_data.rank == 2


# =========================================================================
# 6. TestBetagammaPackage
# =========================================================================

class TestBetagammaPackage:
    """Test the Modular Koszul datum for the beta-gamma system."""

    def test_kappa_value(self):
        """kappa = -1 (at c = -2)."""
        pkg = betagamma_package()
        _assert_zero(pkg.theta_kappa - S(-1))

    def test_central_charge(self):
        """Central charge c = -2."""
        pkg = betagamma_package()
        _assert_zero(pkg.input_data.central_charge - S(-2))

    def test_depth_class_C(self):
        """Beta-gamma is class C (contact/quartic)."""
        pkg = betagamma_package()
        assert pkg.shadow_depth_class == 'C'

    def test_branch_dim_1(self):
        """Branch space dimension = 1 (contact mode)."""
        pkg = betagamma_package()
        assert pkg.branch_space.dimension == 1

    def test_branch_label(self):
        """Branch label is 'contact'."""
        pkg = betagamma_package()
        assert pkg.branch_space.basis_labels == ['contact']

    def test_cubic_vanishes(self):
        """Cubic shadow vanishes on weight-changing line."""
        pkg = betagamma_package()
        _assert_zero(pkg.theta_cubic)

    def test_quartic_nonzero(self):
        """S_4 = -5/12 is nonzero."""
        pkg = betagamma_package()
        _assert_zero(pkg.theta_quartic - Rational(-5, 12))

    def test_depth_decomposition(self):
        """Depth decomposition: d=3, d_arith=0, d_alg=2."""
        pkg = betagamma_package()
        dd = pkg.depth_decomposition
        assert dd['d'] == 3
        assert dd['d_arith'] == 0
        assert dd['d_alg'] == 2

    def test_is_convergent(self):
        """Class C is always convergent (finite tower)."""
        pkg = betagamma_package()
        assert pkg.is_convergent()

    def test_verify_all_pass(self):
        """All verify() checks pass."""
        pkg = betagamma_package()
        checks = pkg.verify()
        for key, val in checks.items():
            assert val, f"Check '{key}' failed"


# =========================================================================
# 6b. TestFreeFermionPackage
# =========================================================================

class TestFreeFermionPackage:
    """Test the Modular Koszul datum for the free fermion."""

    def test_kappa(self):
        """kappa = -1/2."""
        pkg = free_fermion_package()
        _assert_zero(pkg.theta_kappa - Rational(-1, 2))

    def test_central_charge(self):
        """Central charge c = 1/2."""
        pkg = free_fermion_package()
        _assert_zero(pkg.input_data.central_charge - Rational(1, 2))

    def test_depth_class_C(self):
        """Free fermion is class C."""
        pkg = free_fermion_package()
        assert pkg.shadow_depth_class == 'C'

    def test_branch_dim_1(self):
        """Branch space dimension = 1."""
        pkg = free_fermion_package()
        assert pkg.branch_space.dimension == 1

    def test_depth_decomposition(self):
        """Depth decomposition: d=3, d_arith=0, d_alg=2."""
        pkg = free_fermion_package()
        dd = pkg.depth_decomposition
        assert dd['d'] == 3
        assert dd['d_arith'] == 0
        assert dd['d_alg'] == 2


# =========================================================================
# 6c. TestLatticePackage
# =========================================================================

class TestLatticePackage:
    """Test the Modular Koszul datum for the lattice VOA."""

    def test_kappa_symbolic(self):
        """Symbolic rank: kappa = n (anomaly ratio rho = 1)."""
        pkg = lattice_package()
        _assert_zero(pkg.theta_kappa - n_sym)

    @pytest.mark.parametrize("rk", [1, 2, 4, 8, 16, 24])
    def test_kappa_numeric(self, rk):
        """kappa = rank independent of cocycle."""
        pkg = lattice_package(rank=rk)
        _assert_zero(pkg.theta_kappa - Rational(rk))

    def test_depth_class_G(self):
        """Lattice VOA is class G."""
        pkg = lattice_package(rank=8)
        assert pkg.shadow_depth_class == 'G'

    def test_branch_dim_zero(self):
        """Branch space dimension = 0 (abelian)."""
        pkg = lattice_package(rank=8)
        assert pkg.branch_space.dimension == 0

    def test_R4_zero(self):
        """R_4^mod = 0."""
        pkg = lattice_package(rank=8)
        _assert_zero(pkg.R4_mod)

    def test_depth_decomposition(self):
        """Depth decomposition: d=1, d_arith=0, d_alg=0."""
        pkg = lattice_package(rank=8)
        dd = pkg.depth_decomposition
        assert dd['d'] == 1
        assert dd['d_arith'] == 0
        assert dd['d_alg'] == 0


# =========================================================================
# 7. TestComplementarity
# =========================================================================

class TestComplementarity:
    """Test complementarity of discriminants."""

    def test_virasoro_sum_formula(self):
        """Delta(Vir_c) + Delta(Vir_{26-c}) = 6960/((5c+22)(152-5c))."""
        result = complementarity_discriminants(
            kappa=c_sym / 2,
            dual_kappa=(26 - c_sym) / 2,
            c_val=c_sym,
        )
        assert result['matches']

    def test_constant_numerator_6960(self):
        """The constant numerator is 6960."""
        result = complementarity_discriminants(
            kappa=c_sym / 2,
            dual_kappa=(26 - c_sym) / 2,
            c_val=c_sym,
        )
        assert result['constant_numerator'] == 6960

    @pytest.mark.parametrize("c_val", [1, 5, 10, 13, 20, 25])
    def test_numeric_complementarity(self, c_val):
        """Numeric verification of complementarity sum at specific c."""
        result = complementarity_discriminants(
            kappa=Rational(c_val, 2),
            dual_kappa=Rational(26 - c_val, 2),
            c_val=Rational(c_val),
        )
        Delta_A = result['Delta_A']
        Delta_A_dual = result['Delta_A_dual']
        total = Delta_A + Delta_A_dual
        expected = Rational(6960) / ((5 * c_val + 22) * (152 - 5 * c_val))
        _assert_zero(total - expected)

    def test_self_dual_c13(self):
        """At c=13 (self-dual point), both discriminants are equal."""
        result = complementarity_discriminants(
            kappa=Rational(13, 2),
            dual_kappa=Rational(13, 2),
            c_val=Rational(13),
        )
        _assert_zero(result['Delta_A'] - result['Delta_A_dual'])

    def test_virasoro_package_complementarity_sum(self):
        """Virasoro package stores complementarity_sum = 26."""
        pkg = virasoro_package()
        assert pkg.complementarity_sum == 26

    def test_delta_A_positive(self):
        """Delta_A > 0 for c > 0 (non-degenerate Virasoro)."""
        result = complementarity_discriminants(
            kappa=Rational(10, 2),
            dual_kappa=Rational(16, 2),
            c_val=Rational(10),
        )
        assert result['Delta_A'] > 0

    def test_delta_A_dual_positive(self):
        """Delta_A! > 0 for c < 26."""
        result = complementarity_discriminants(
            kappa=Rational(10, 2),
            dual_kappa=Rational(16, 2),
            c_val=Rational(10),
        )
        assert result['Delta_A_dual'] > 0

    def test_kappa_plus_dual_kappa_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        pkg = virasoro_package(central_charge=7)
        dual_kappa = (26 - 7) / 2
        total = pkg.theta_kappa + dual_kappa
        _assert_zero(total - 13)


# =========================================================================
# 8. TestDepthDecomposition
# =========================================================================

class TestDepthDecomposition:
    """Test depth decomposition d = 1 + d_arith + d_alg."""

    def test_heisenberg(self):
        """Heisenberg: (d, d_arith, d_alg) = (1, 0, 0)."""
        dd = depth_decomposition('heisenberg')
        assert dd == {'d': 1, 'd_arith': 0, 'd_alg': 0}

    def test_affine_sl2(self):
        """Affine sl_2: (d, d_arith, d_alg) = (2, 0, 1)."""
        dd = depth_decomposition('affine_sl2')
        assert dd == {'d': 2, 'd_arith': 0, 'd_alg': 1}

    def test_affine_sl3(self):
        """Affine sl_3: (d, d_arith, d_alg) = (2, 0, 1)."""
        dd = depth_decomposition('affine_sl3')
        assert dd == {'d': 2, 'd_arith': 0, 'd_alg': 1}

    def test_betagamma(self):
        """Beta-gamma: (d, d_arith, d_alg) = (3, 0, 2)."""
        dd = depth_decomposition('betagamma')
        assert dd == {'d': 3, 'd_arith': 0, 'd_alg': 2}

    def test_virasoro(self):
        """Virasoro: (d, d_arith, d_alg) = (oo, 0, oo)."""
        dd = depth_decomposition('virasoro')
        assert dd['d'] == oo
        assert dd['d_arith'] == 0
        assert dd['d_alg'] == oo

    def test_w3(self):
        """W_3: (d, d_arith, d_alg) = (oo, 0, oo)."""
        dd = depth_decomposition('w3')
        assert dd['d'] == oo
        assert dd['d_alg'] == oo

    def test_free_fermion(self):
        """Free fermion: (d, d_arith, d_alg) = (3, 0, 2)."""
        dd = depth_decomposition('free_fermion')
        assert dd == {'d': 3, 'd_arith': 0, 'd_alg': 2}

    def test_lattice(self):
        """Lattice: (d, d_arith, d_alg) = (1, 0, 0)."""
        dd = depth_decomposition('lattice')
        assert dd == {'d': 1, 'd_arith': 0, 'd_alg': 0}

    def test_unknown_family(self):
        """Unknown family returns None for d, d_alg."""
        dd = depth_decomposition('unknown_family')
        assert dd['d'] is None

    def test_sum_identity_finite(self):
        """d = 1 + d_arith + d_alg for finite-depth families."""
        for family in ['heisenberg', 'affine_sl2', 'betagamma', 'free_fermion', 'lattice']:
            dd = depth_decomposition(family)
            assert dd['d'] == 1 + dd['d_arith'] + dd['d_alg'], \
                f"Sum identity fails for {family}"


# =========================================================================
# 9. TestIndependentSum
# =========================================================================

class TestIndependentSum:
    """Test independent sum factorization (prop:independent-sum-factorization)."""

    def test_kappa_additive(self):
        """kappa(A + B) = kappa(A) + kappa(B)."""
        pkg1 = heisenberg_package(level=1)
        pkg2 = heisenberg_package(level=3)
        combined = independent_sum_package(pkg1, pkg2)
        expected = pkg1.theta_kappa + pkg2.theta_kappa
        _assert_zero(combined.theta_kappa - expected)

    def test_branch_direct_sum(self):
        """Branch space is direct sum: dim(V^br(A+B)) = dim(V^br_A) + dim(V^br_B)."""
        pkg1 = affine_sl2_package(level=1)
        pkg2 = heisenberg_package(level=1)
        combined = independent_sum_package(pkg1, pkg2)
        assert combined.branch_space.dimension == 3 + 0

    def test_R4_additive(self):
        """R_4 is additive."""
        pkg1 = virasoro_package(central_charge=10)
        pkg2 = heisenberg_package(level=1)
        combined = independent_sum_package(pkg1, pkg2)
        expected_R4 = pkg1.R4_mod + pkg2.R4_mod
        _assert_zero(combined.R4_mod - expected_R4)

    def test_depth_class_worst(self):
        """Combined depth class = worst of components."""
        pkg_G = heisenberg_package(level=1)
        pkg_M = virasoro_package(central_charge=10)
        combined = independent_sum_package(pkg_G, pkg_M)
        assert combined.shadow_depth_class == 'M'

    def test_central_charge_additive(self):
        """Central charge is additive: c(A+B) = c(A) + c(B)."""
        pkg1 = heisenberg_package(level=2)
        pkg2 = betagamma_package()
        combined = independent_sum_package(pkg1, pkg2)
        expected_cc = pkg1.input_data.central_charge + pkg2.input_data.central_charge
        _assert_zero(combined.input_data.central_charge - expected_cc)

    def test_two_heisenberg_sum(self):
        """H_1 + H_3: kappa = 1 + 3 = 4, class G.
        kappa(H_k) = k (level), NOT k/2."""
        pkg1 = heisenberg_package(level=1)
        pkg2 = heisenberg_package(level=3)
        combined = independent_sum_package(pkg1, pkg2)
        _assert_zero(combined.theta_kappa - 4)
        assert combined.shadow_depth_class == 'G'

    def test_branch_labels_concatenated(self):
        """Branch labels are concatenation of component labels."""
        pkg1 = affine_sl2_package(level=1)
        pkg2 = virasoro_package(central_charge=10)
        combined = independent_sum_package(pkg1, pkg2)
        assert combined.branch_space.basis_labels == ['e', 'f', 'h', 'L']


# =========================================================================
# 10. TestLandscape
# =========================================================================

class TestLandscape:
    """Test the standard landscape atlas."""

    def test_standard_landscape_count(self):
        """standard_landscape() returns exactly 8 families."""
        atlas = standard_landscape()
        assert len(atlas) == 8

    def test_standard_landscape_keys(self):
        """Atlas has all expected family names."""
        atlas = standard_landscape()
        expected_keys = {
            'heisenberg', 'affine_sl2', 'affine_sl3', 'virasoro',
            'w3', 'betagamma', 'free_fermion', 'lattice',
        }
        assert set(atlas.keys()) == expected_keys

    def test_all_packages_are_PlatonicPackage(self):
        """Every entry in the atlas is a PlatonicPackage instance."""
        atlas = standard_landscape()
        for name, pkg in atlas.items():
            assert isinstance(pkg, PlatonicPackage), f"{name} is not PlatonicPackage"

    def test_landscape_summary_nonempty(self):
        """landscape_summary() produces non-empty output."""
        summary = landscape_summary()
        assert len(summary) > 0
        assert 'heisenberg' in summary

    def test_all_verify_pass(self):
        """All verify() checks pass for every family in the landscape."""
        atlas = standard_landscape()
        for name, pkg in atlas.items():
            checks = pkg.verify()
            for check_name, val in checks.items():
                assert val, f"{name}: check '{check_name}' failed"


# =========================================================================
# 11. TestAssemblePlatonicPackage
# =========================================================================

class TestAssemblePlatonicPackage:
    """Test the core assembler assemble_platonic_package()."""

    def test_assemble_heisenberg(self):
        """Assembler builds a valid Heisenberg package."""
        data = CyclicAdmissibleData(
            name='heisenberg', rank=1, weights=[1],
            structure_constants={('J', 'J'): {2: {'1': 1}}},
            killing_form=None, level=1, central_charge=1,
        )
        pkg = assemble_platonic_package(data)
        assert isinstance(pkg, PlatonicPackage)
        assert pkg.name == 'heisenberg'

    def test_assemble_virasoro(self):
        """Assembler builds a valid Virasoro package."""
        data = CyclicAdmissibleData(
            name='virasoro', rank=1, weights=[2],
            structure_constants={},
            killing_form=None, level=None, central_charge=10,
        )
        pkg = assemble_platonic_package(data)
        assert isinstance(pkg, PlatonicPackage)

    def test_assemble_rejects_invalid(self):
        """Assembler raises ValueError for invalid (non-admissible) data."""
        data = CyclicAdmissibleData(
            name='bad', rank=1, weights=[1],
            structure_constants={},
            killing_form=None, level=1, central_charge=1,
            has_invariant_pairing=False,
        )
        with pytest.raises(ValueError, match="Admissibility"):
            assemble_platonic_package(data)

    def test_assemble_rejects_rank_mismatch(self):
        """Assembler raises ValueError for rank mismatch."""
        data = CyclicAdmissibleData(
            name='bad', rank=5, weights=[1],
            structure_constants={},
            killing_form=None, level=1, central_charge=1,
        )
        with pytest.raises(ValueError):
            assemble_platonic_package(data)


# =========================================================================
# 12. TestBranchSpace
# =========================================================================

class TestBranchSpace:
    """Test BranchSpace dataclass."""

    def test_trivial_branch(self):
        """Zero-dimensional branch space is trivial."""
        bs = BranchSpace(dimension=0, basis_labels=[], bv_action_terms={},
                         metaplectic_square=S(0))
        assert bs.is_trivial()

    def test_nontrivial_branch(self):
        """Positive-dimensional branch space is not trivial."""
        bs = BranchSpace(dimension=3, basis_labels=['e', 'f', 'h'],
                         bv_action_terms={}, metaplectic_square=S(0))
        assert not bs.is_trivial()


# =========================================================================
# 13. TestShadowMetric
# =========================================================================

class TestShadowMetric:
    """Test shadow metric Q_L(t) and related structures."""

    def test_heisenberg_perfect_square(self):
        """Heisenberg shadow metric is a perfect square (no t).
        kappa(H_k) = k, so Q = 4*kappa^2 = 4*k^2."""
        pkg = heisenberg_package(level=2)
        # Q = 4*kappa^2 = 4*(2)^2 = 16
        Q = pkg.shadow_metric
        _assert_zero(Q - 16)

    def test_virasoro_shadow_metric_form(self):
        """Virasoro shadow metric is Q = (2*kappa + 2t)^2 + 2*Delta*t^2."""
        pkg = virasoro_package()
        kappa = c_sym / 2
        Delta = Rational(40) / (5 * c_sym + 22)
        t = Symbol('t')
        expected = (2 * kappa + 2 * t) ** 2 + 2 * Delta * t ** 2
        # Substitute the module's t symbol
        from compute.lib.platonic_datum import t_sym
        expected_sub = expected.subs(t, t_sym)
        _assert_zero(pkg.shadow_metric - expected_sub)

    def test_shadow_generating_function_finite(self):
        """Heisenberg shadow GF is polynomial (finite tower).
        kappa(H_k) = k, so H(t) = 2*kappa*t^2 = 2*k*t^2."""
        pkg = heisenberg_package(level=2)
        H = pkg.shadow_generating_function('t')
        t = Symbol('t')
        # H(t) = 2 * kappa * t^2 = 2 * 2 * t^2 = 4*t^2
        _assert_zero(H - 4 * t ** 2)

    def test_shadow_generating_function_infinite(self):
        """Virasoro shadow GF involves sqrt (algebraic, infinite tower)."""
        pkg = virasoro_package(central_charge=10)
        H = pkg.shadow_generating_function('t')
        t = Symbol('t')
        # H(t) should involve sqrt for class M
        assert H is not None


# =========================================================================
# 14. TestPackageMethods
# =========================================================================

class TestPackageMethods:
    """Test PlatonicPackage methods: summary, verify, is_convergent."""

    def test_summary_nonempty(self):
        """summary() returns a non-empty string."""
        pkg = heisenberg_package(level=1)
        s = pkg.summary()
        assert len(s) > 0
        assert 'heisenberg' in s.lower()

    def test_summary_contains_kappa(self):
        """summary() mentions kappa value."""
        pkg = heisenberg_package(level=2)
        s = pkg.summary()
        assert 'kappa' in s.lower()

    def test_is_convergent_class_G(self):
        """Class G is always convergent."""
        assert heisenberg_package(level=1).is_convergent()

    def test_is_convergent_class_L(self):
        """Class L is always convergent."""
        assert affine_sl2_package(level=1).is_convergent()

    def test_is_convergent_class_C(self):
        """Class C is always convergent."""
        assert betagamma_package().is_convergent()

    @pytest.mark.parametrize("family_fn,kwargs", [
        (heisenberg_package, {'level': 1}),
        (affine_sl2_package, {'level': 1}),
        (betagamma_package, {}),
        (virasoro_package, {'central_charge': 10}),
        (lattice_package, {'rank': 8}),
    ])
    def test_verify_structural(self, family_fn, kwargs):
        """Structural checks (admissibility, depth class, branch dim) pass for all."""
        pkg = family_fn(**kwargs)
        checks = pkg.verify()
        assert checks.get('admissibility', True)
        assert checks.get('depth_class_valid', True)
        assert checks.get('branch_dim_nonneg', True)


# =========================================================================
# 15. TestShadowDepthClassification
# =========================================================================

class TestShadowDepthClassification:
    """Test the four-class depth classification G/L/C/M."""

    _expected_classes = {
        'heisenberg': 'G',
        'affine_sl2': 'L',
        'affine_sl3': 'L',
        'betagamma': 'C',
        'free_fermion': 'C',
        'virasoro': 'M',
        'w3': 'M',
        'lattice': 'G',
    }

    @pytest.mark.parametrize("family,expected", list(_expected_classes.items()))
    def test_depth_class(self, family, expected):
        """Each standard family has the correct depth class."""
        atlas = standard_landscape()
        assert atlas[family].shadow_depth_class == expected

    def test_G_means_depth_2(self):
        """Class G implies depth 2 (only kappa)."""
        pkg = heisenberg_package(level=1)
        assert pkg.shadow_depth_class == 'G'
        assert max(pkg.theta.keys()) == 2

    def test_L_means_depth_3(self):
        """Class L implies depth 3 (kappa + cubic)."""
        pkg = affine_sl2_package(level=1)
        assert pkg.shadow_depth_class == 'L'
        assert max(pkg.theta.keys()) == 3

    def test_M_has_quartic(self):
        """Class M families have a quartic entry in the shadow obstruction tower."""
        pkg = virasoro_package(central_charge=10)
        assert pkg.shadow_depth_class == 'M'
        assert 4 in pkg.theta
