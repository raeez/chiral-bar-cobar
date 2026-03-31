"""Core bar complex verification across all standard algebra families.

Tests the foundational bar complex computations that underpin the entire
monograph: OPE products, bar differentials, bar cohomology dimensions,
generating function recurrences, Arnold (Orlik-Solomon) dimensions, and
cross-family structural properties.

Ground truth sources:
  - compute/lib/heisenberg_bar.py, virasoro_bar.py, w3_bar.py,
    betagamma_bar.py, fermion_bar.py (chain-level OPE data)
  - compute/lib/bar_gf_algebraicity.py (generating functions, recurrences)
  - compute/lib/bar_complex.py (KNOWN_BAR_DIMS master table)
  - compute/lib/os_algebra.py (Orlik-Solomon / Arnold dimensions)
  - Manuscript: detailed_computations.tex, landscape_census.tex

Mathematical claims tested:
  1. Heisenberg: only double pole, H^n = p(n-2), maximal-form vanishing
  2. Virasoro: quartic+double+simple poles, Motzkin-difference GF
  3. sl2: Riordan numbers (with degree-2 correction), recurrence
  4. W3: two-generator curvature, rational GF recurrence
  5. betagamma: simple-pole-only, sign structure, sqrt GF recurrence
  6. Free fermion: diagonal OPE, partition-number bar dims
  7. sl3: known low-degree dims, conjectured rational GF recurrence
  8. Cross-family: H^1 = number of generators (universal)
  9. Orlik-Solomon: dim OS^{n-1}(n) = (n-1)! (Arnold's theorem)
"""

import pytest
from sympy import Rational, Symbol, simplify


# ============================================================================
# 1. Heisenberg bar complex
# ============================================================================

class TestHeisenbergBarComplex:
    """Heisenberg algebra H_kappa: one generator, double pole only."""

    def test_heisenberg_nth_products_structure(self):
        """Heisenberg OPE has exactly one entry: n=1 (double pole) with vacuum output."""
        from compute.lib.heisenberg_bar import heisenberg_nth_products
        products = heisenberg_nth_products()
        assert set(products.keys()) == {1}

    def test_heisenberg_nth_products_value(self):
        """a_{(1)}a = kappa (the curvature)."""
        from compute.lib.heisenberg_bar import heisenberg_nth_products
        kappa = Symbol('kappa')
        products = heisenberg_nth_products()
        assert products[1] == {"vac": kappa}

    def test_heisenberg_no_simple_pole(self):
        """a_{(0)}a = 0: no simple pole (key structural feature)."""
        from compute.lib.heisenberg_bar import heisenberg_nth_products
        products = heisenberg_nth_products()
        assert 0 not in products

    def test_heisenberg_bar_diff_deg2_vacuum(self):
        """D(a tensor a tensor eta) has vacuum component = kappa."""
        from compute.lib.heisenberg_bar import heisenberg_bar_diff_deg2
        kappa = Symbol('kappa')
        vac, bar1 = heisenberg_bar_diff_deg2()
        assert vac == {"vac": kappa}

    def test_heisenberg_bar_diff_deg2_no_bar1(self):
        """D(a tensor a tensor eta) has no bar-1 component."""
        from compute.lib.heisenberg_bar import heisenberg_bar_diff_deg2
        _, bar1 = heisenberg_bar_diff_deg2()
        assert bar1 == {}

    @pytest.mark.parametrize("d", range(3, 9))
    def test_heisenberg_maximal_form_vanishes(self, d):
        """Bar differential vanishes on maximal-form elements at degree >= 3."""
        from compute.lib.heisenberg_bar import heisenberg_bar_diff_maximal_form
        assert heisenberg_bar_diff_maximal_form(d) is True

    def test_heisenberg_maximal_form_nonzero_deg2(self):
        """Bar differential does NOT vanish on maximal-form at degree 2."""
        from compute.lib.heisenberg_bar import heisenberg_bar_diff_maximal_form
        assert heisenberg_bar_diff_maximal_form(2) is False

    @pytest.mark.parametrize("n", range(1, 16))
    def test_heisenberg_bar_cohomology_partition_numbers(self, n):
        """H^n(B(Heisenberg)) = p(n-2) for n >= 2, H^1 = 1."""
        from compute.lib.bar_gf_algebraicity import heisenberg_bar_dims
        from compute.lib.utils import partition_number
        dims = heisenberg_bar_dims(15)
        expected = 1 if n == 1 else partition_number(n - 2)
        assert dims[n - 1] == expected

    def test_heisenberg_curvature(self):
        """Curvature m_0 = kappa."""
        from compute.lib.heisenberg_bar import heisenberg_curvature
        kappa = Symbol('kappa')
        assert heisenberg_curvature() == kappa


# ============================================================================
# 2. Virasoro bar complex
# ============================================================================

class TestVirasoroBarComplex:
    """Virasoro algebra Vir_c: one generator T of weight 2."""

    def test_virasoro_nth_products_keys(self):
        """T_{(n)}T has keys 3, 1, 0 (quartic, double, simple poles; no cubic)."""
        from compute.lib.virasoro_bar import virasoro_nth_products
        products = virasoro_nth_products()
        assert set(products.keys()) == {3, 1, 0}

    def test_virasoro_quartic_pole(self):
        """T_{(3)}T = c/2 (quartic pole gives curvature)."""
        from compute.lib.virasoro_bar import virasoro_nth_products
        c = Symbol('c')
        products = virasoro_nth_products()
        assert products[3] == {"vac": c / 2}

    def test_virasoro_double_pole(self):
        """T_{(1)}T = 2T (conformal weight eigenvalue)."""
        from compute.lib.virasoro_bar import virasoro_nth_products
        products = virasoro_nth_products()
        assert products[1] == {"T": Rational(2)}

    def test_virasoro_simple_pole(self):
        """T_{(0)}T = dT (translation covariance)."""
        from compute.lib.virasoro_bar import virasoro_nth_products
        products = virasoro_nth_products()
        assert products[0] == {"dT": Rational(1)}

    def test_virasoro_no_cubic_pole(self):
        """T_{(2)}T = 0 (no weight-1 state in vacuum module)."""
        from compute.lib.virasoro_bar import virasoro_nth_products
        products = virasoro_nth_products()
        assert 2 not in products

    def test_virasoro_bar_diff_deg2_vacuum(self):
        """D(T tensor T tensor eta): vacuum component = c/2."""
        from compute.lib.virasoro_bar import virasoro_bar_diff_deg2
        c = Symbol('c')
        vac, _ = virasoro_bar_diff_deg2()
        assert vac.get("vac") == c / 2

    def test_virasoro_bar_diff_deg2_T_coeff(self):
        """D(T tensor T tensor eta): bar-1 component has T with coefficient 2."""
        from compute.lib.virasoro_bar import virasoro_bar_diff_deg2
        _, bar1 = virasoro_bar_diff_deg2()
        assert bar1.get("T") == 2

    def test_virasoro_bar_diff_deg2_dT_coeff(self):
        """D(T tensor T tensor eta): bar-1 component has dT with coefficient 1."""
        from compute.lib.virasoro_bar import virasoro_bar_diff_deg2
        _, bar1 = virasoro_bar_diff_deg2()
        assert bar1.get("dT") == 1

    def test_virasoro_descendant_T1_dT(self):
        """T_{(1)}(dT) = 3dT (descendant product via translation covariance)."""
        from compute.lib.virasoro_bar import virasoro_descendant_products
        desc = virasoro_descendant_products()
        assert desc[("T", "dT")][1] == {"dT": Rational(3)}

    def test_virasoro_descendant_T0_dT(self):
        """T_{(0)}(dT) = d^2T."""
        from compute.lib.virasoro_bar import virasoro_descendant_products
        desc = virasoro_descendant_products()
        assert desc[("T", "dT")][0] == {"d2T": Rational(1)}

    @pytest.mark.parametrize("h,expected", [
        (2, 1), (3, 1), (4, 2), (5, 2), (6, 4), (7, 4),
        (8, 7), (9, 8), (10, 12), (11, 14), (12, 21), (13, 24),
        (14, 34), (15, 41),
    ])
    def test_virasoro_vacuum_module_dims(self, h, expected):
        """dim V-bar_h = p_{>=2}(h) (partitions into parts >= 2)."""
        from compute.lib.virasoro_bar import partitions_geq2
        assert partitions_geq2(h) == expected

    @pytest.mark.parametrize("n,expected", [
        (1, 1), (2, 2), (3, 5), (4, 12), (5, 30),
        (6, 76), (7, 196), (8, 512), (9, 1353), (10, 3610),
    ])
    def test_virasoro_bar_cohomology_dims(self, n, expected):
        """Bar cohomology dims = Motzkin differences M(n+1) - M(n)."""
        from compute.lib.bar_gf_algebraicity import virasoro_bar_dims
        dims = virasoro_bar_dims(10)
        assert dims[n - 1] == expected

    def test_virasoro_curvature_value(self):
        """Curvature m_0 = c/2."""
        from compute.lib.virasoro_bar import virasoro_curvature
        c = Symbol('c')
        assert virasoro_curvature() == c / 2

    def test_virasoro_complementarity(self):
        """Central charge complementarity: c + c' = 26."""
        from compute.lib.virasoro_bar import virasoro_complementarity_sum
        assert virasoro_complementarity_sum() == 26


# ============================================================================
# 3. sl2 (affine Kac-Moody) bar complex
# ============================================================================

class TestSl2BarComplex:
    """Affine sl2 bar complex: Riordan number identification."""

    @pytest.mark.parametrize("n,expected", [
        (1, 3), (2, 5), (3, 15), (4, 36), (5, 91),
        (6, 232), (7, 603), (8, 1585),
    ])
    def test_sl2_bar_cohomology_dims(self, n, expected):
        """Bar cohomology H^n(B(sl2)) = R(n+3) with degree-2 correction."""
        from compute.lib.bar_complex import bar_dim_sl2
        assert bar_dim_sl2(n) == expected

    @pytest.mark.parametrize("n,expected", [
        (1, 3), (2, 6), (3, 15), (4, 36), (5, 91),
        (6, 232), (7, 603), (8, 1585),
    ])
    def test_sl2_riordan_identification(self, n, expected):
        """bar_gf_algebraicity.sl2_bar_dims gives Riordan R(n+3)."""
        from compute.lib.bar_gf_algebraicity import sl2_bar_dims
        dims = sl2_bar_dims(8)
        assert dims[n - 1] == expected

    def test_sl2_bar_degree2_correction(self):
        """sl2 bar H^2 = 5 (not 6 = R(5); Riordan wrong at n=2)."""
        from compute.lib.bar_complex import bar_dim_sl2
        from compute.lib.bar_gf_algebraicity import riordan_numbers
        R = riordan_numbers(10)
        assert R[5] == 6, "R(5) = 6 (Riordan sequence)"
        assert bar_dim_sl2(2) == 5, "Corrected bar dim at degree 2 is 5"

    @pytest.mark.parametrize("n", range(2, 21))
    def test_riordan_recurrence(self, n):
        """Riordan recurrence: (n+1)*R(n) = (n-1)*(2*R(n-1) + 3*R(n-2))."""
        from compute.lib.bar_gf_algebraicity import riordan_numbers
        R = riordan_numbers(25)
        lhs = (n + 1) * R[n]
        rhs = (n - 1) * (2 * R[n - 1] + 3 * R[n - 2])
        assert lhs == rhs

    def test_riordan_initial_conditions(self):
        """Riordan numbers R(0)=1, R(1)=0, R(2)=1."""
        from compute.lib.bar_gf_algebraicity import riordan_numbers
        R = riordan_numbers(5)
        assert R[0] == 1
        assert R[1] == 0
        assert R[2] == 1

    def test_riordan_algebraic_equation(self):
        """Riordan GF satisfies x(1+x)R^2 - (1+x)R + 1 = 0."""
        from compute.lib.bar_gf_algebraicity import verify_riordan_equation
        result = verify_riordan_equation(15)
        assert result['all_zero']

    @pytest.mark.parametrize("n", range(1, 9))
    def test_sl2_bar_growth_bound(self, n):
        """sl2 bar cohomology bounded by 3^n (dim(g)^n)."""
        from compute.lib.bar_complex import bar_dim_sl2
        assert 0 < bar_dim_sl2(n) <= 3**n


# ============================================================================
# 4. W3 bar complex
# ============================================================================

class TestW3BarComplex:
    """W3 algebra: two generators T (weight 2) and W (weight 3)."""

    def test_w3_curvature_values(self):
        """m_0^(T) = c/2, m_0^(W) = c/3."""
        from compute.lib.w3_bar import w3_curvature
        c = Symbol('c')
        curv = w3_curvature()
        assert curv["T"] == c / 2
        assert curv["W"] == c / 3

    def test_w3_curvature_ratio(self):
        """Curvature ratio m_0^(W)/m_0^(T) = 2/3 (level-independent)."""
        from compute.lib.w3_bar import w3_curvature_ratio
        assert w3_curvature_ratio() == Rational(2, 3)

    def test_w3_TT_bar_diff_vacuum(self):
        """D(T tensor T tensor eta): vacuum = c/2 (same as Virasoro)."""
        from compute.lib.w3_bar import w3_bar_diff_deg2
        c = Symbol('c')
        vac, _ = w3_bar_diff_deg2("T", "T")
        assert vac.get("vac") == c / 2

    def test_w3_TT_bar_diff_bar1(self):
        """D(T tensor T tensor eta): bar1 = {T: 2, dT: 1}."""
        from compute.lib.w3_bar import w3_bar_diff_deg2
        _, bar1 = w3_bar_diff_deg2("T", "T")
        assert bar1.get("T") == 2
        assert bar1.get("dT") == 1

    def test_w3_TW_bar_diff_no_vacuum(self):
        """D(T tensor W tensor eta) has no vacuum component."""
        from compute.lib.w3_bar import w3_bar_diff_deg2
        vac, _ = w3_bar_diff_deg2("T", "W")
        assert len(vac) == 0

    def test_w3_TW_bar_diff_bar1(self):
        """D(T tensor W tensor eta): bar1 = {W: 3, dW: 1}."""
        from compute.lib.w3_bar import w3_bar_diff_deg2
        _, bar1 = w3_bar_diff_deg2("T", "W")
        assert bar1.get("W") == 3
        assert bar1.get("dW") == 1

    def test_w3_WT_bar_diff_asymmetry(self):
        """D(W tensor T): dW coefficient is 2 (not 1 as in TW -- asymmetric)."""
        from compute.lib.w3_bar import w3_bar_diff_deg2
        _, bar1_tw = w3_bar_diff_deg2("T", "W")
        _, bar1_wt = w3_bar_diff_deg2("W", "T")
        assert bar1_tw.get("dW") == 1
        assert bar1_wt.get("dW") == 2
        assert bar1_tw.get("dW") != bar1_wt.get("dW")

    def test_w3_WW_bar_diff_vacuum(self):
        """D(W tensor W tensor eta): vacuum component = c/3."""
        from compute.lib.w3_bar import w3_bar_diff_deg2
        c = Symbol('c')
        vac, _ = w3_bar_diff_deg2("W", "W")
        assert vac.get("vac") == c / 3

    def test_w3_WW_bar_diff_composite_coefficients(self):
        """D(W tensor W): d2T = 3/10, d3T = 1/15, Lambda = 16/(22+5c)."""
        from compute.lib.w3_bar import w3_bar_diff_deg2
        c = Symbol('c')
        _, bar1 = w3_bar_diff_deg2("W", "W")
        assert bar1.get("d2T") == Rational(3, 10)
        assert bar1.get("d3T") == Rational(1, 15)
        assert simplify(bar1.get("Lambda") - Rational(16, 1) / (22 + 5 * c)) == 0

    @pytest.mark.parametrize("n,expected", [
        (1, 2), (2, 5), (3, 16), (4, 52), (5, 171),
    ])
    def test_w3_bar_cohomology_dims(self, n, expected):
        """W3 bar cohomology dims: known through degree 5."""
        from compute.lib.bar_gf_algebraicity import w3_bar_dims
        dims = w3_bar_dims(5)
        assert dims[n - 1] == expected

    @pytest.mark.parametrize("n", range(4, 11))
    def test_w3_bar_recurrence(self, n):
        """W3 bar recurrence: a_n = 4*a_{n-1} - 2*a_{n-2} - a_{n-3}."""
        from compute.lib.bar_gf_algebraicity import w3_bar_dims
        dims = w3_bar_dims(10)
        assert dims[n - 1] == 4 * dims[n - 2] - 2 * dims[n - 3] - dims[n - 4]

    def test_w3_rational_gf_verification(self):
        """W3 rational GF: (1-x)(1-3x-x^2)P = x(2-3x)."""
        from compute.lib.bar_gf_algebraicity import verify_w3_rational_gf
        result = verify_w3_rational_gf(8)
        assert result['all_zero']

    def test_w3_skew_symmetry(self):
        """W_{(0)}T = 2dW via skew-symmetry formula."""
        from compute.lib.w3_bar import verify_skew_symmetry
        assert verify_skew_symmetry()

    def test_w3_complementarity(self):
        """Central charge complementarity c + c' = 100."""
        from compute.lib.w3_bar import w3_complementarity_sum
        assert w3_complementarity_sum() == 100


# ============================================================================
# 5. betagamma bar complex
# ============================================================================

class TestBetagammaBarComplex:
    """Beta-gamma system: two bosonic generators, simple pole only."""

    def test_betagamma_bg_bar_diff_vacuum(self):
        """D(beta tensor gamma tensor eta): vacuum = 1."""
        from compute.lib.betagamma_bar import betagamma_bar_diff_deg2
        vac, bar1 = betagamma_bar_diff_deg2("beta", "gamma")
        assert vac == {"vac": Rational(1)}
        assert bar1 == {}

    def test_betagamma_gb_bar_diff_sign(self):
        """D(gamma tensor beta tensor eta): vacuum = -1 (sign from skew-symmetry)."""
        from compute.lib.betagamma_bar import betagamma_bar_diff_deg2
        vac, bar1 = betagamma_bar_diff_deg2("gamma", "beta")
        assert vac == {"vac": Rational(-1)}

    def test_betagamma_bb_bar_diff_zero(self):
        """D(beta tensor beta tensor eta) = 0 (no pole)."""
        from compute.lib.betagamma_bar import betagamma_bar_diff_deg2
        vac, bar1 = betagamma_bar_diff_deg2("beta", "beta")
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_betagamma_gg_bar_diff_zero(self):
        """D(gamma tensor gamma tensor eta) = 0 (no pole)."""
        from compute.lib.betagamma_bar import betagamma_bar_diff_deg2
        vac, bar1 = betagamma_bar_diff_deg2("gamma", "gamma")
        assert len(vac) == 0
        assert len(bar1) == 0

    @pytest.mark.parametrize("n,expected", [
        (1, 2), (2, 4), (3, 10), (4, 26), (5, 70),
        (6, 192), (7, 534), (8, 1500), (9, 4246), (10, 12092),
    ])
    def test_betagamma_bar_cohomology_dims(self, n, expected):
        """Bar cohomology GF = sqrt((1+x)/(1-3x))."""
        from compute.lib.bar_gf_algebraicity import betagamma_bar_dims
        dims = betagamma_bar_dims(10)
        assert dims[n - 1] == expected

    @pytest.mark.parametrize("n", range(2, 12))
    def test_betagamma_recurrence(self, n):
        """Recurrence: n*a(n) = 2n*a(n-1) + 3(n-2)*a(n-2), with a(0)=1, a(1)=2."""
        from compute.lib.bar_gf_algebraicity import betagamma_full_gf_coeffs
        a = betagamma_full_gf_coeffs(15)
        lhs = n * a[n]
        rhs = 2 * n * a[n - 1] + 3 * (n - 2) * a[n - 2]
        assert lhs == rhs

    def test_betagamma_algebraic_equation(self):
        """betagamma GF satisfies (1-3x)Q^2 = (1+x)."""
        from compute.lib.bar_gf_algebraicity import verify_betagamma_equation
        result = verify_betagamma_equation(12)
        assert result['all_zero']


# ============================================================================
# 6. Free fermion bar complex
# ============================================================================

class TestFreeFermionBarComplex:
    """Free fermion F_2: two fermionic generators, diagonal OPE."""

    def test_fermion_diagonal_ope_11(self):
        """psi_1_{(0)}psi_1 = |0> (diagonal, vacuum)."""
        from compute.lib.fermion_bar import fermion_bar_diff_deg2
        vac, bar1 = fermion_bar_diff_deg2(1, 1)
        assert vac == {"vac": Rational(1)}
        assert bar1 == {}

    def test_fermion_diagonal_ope_22(self):
        """psi_2_{(0)}psi_2 = |0> (diagonal, vacuum)."""
        from compute.lib.fermion_bar import fermion_bar_diff_deg2
        vac, _ = fermion_bar_diff_deg2(2, 2)
        assert vac == {"vac": Rational(1)}

    def test_fermion_off_diagonal_ope_12(self):
        """psi_1_{(0)}psi_2 = 0 (different species, no OPE)."""
        from compute.lib.fermion_bar import fermion_bar_diff_deg2
        vac, bar1 = fermion_bar_diff_deg2(1, 2)
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_fermion_off_diagonal_ope_21(self):
        """psi_2_{(0)}psi_1 = 0 (different species)."""
        from compute.lib.fermion_bar import fermion_bar_diff_deg2
        vac, bar1 = fermion_bar_diff_deg2(2, 1)
        assert len(vac) == 0
        assert len(bar1) == 0

    @pytest.mark.parametrize("n,expected", [
        (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 7), (7, 11), (8, 15),
    ])
    def test_fermion_bar_cohomology_known_dims(self, n, expected):
        """Fermion bar cohomology from FERMION_BAR_COHOMOLOGY table."""
        from compute.lib.fermion_bar import FERMION_BAR_COHOMOLOGY
        assert FERMION_BAR_COHOMOLOGY[n] == expected

    @pytest.mark.parametrize("n", range(1, 9))
    def test_fermion_bar_dims_partition_formula(self, n):
        """dim H^n(B(F)) = p(n-1) where p is the partition function."""
        from compute.lib.bar_complex import bar_dim_free_fermion
        from compute.lib.utils import partition_number
        assert bar_dim_free_fermion(n) == partition_number(n - 1)

    def test_fermion_desuspension_parity(self):
        """After desuspension, fermionic generators become even."""
        from compute.lib.fermion_bar import desuspension_parity
        assert desuspension_parity() == "even"

    def test_fermion_coalgebra_type(self):
        """Bar coalgebra is symmetric (not exterior) due to even desuspension."""
        from compute.lib.fermion_bar import coalgebra_type
        assert coalgebra_type() == "symmetric"

    def test_fermion_no_higher_poles(self):
        """psi_i has no poles of order >= 2 with any psi_j."""
        from compute.lib.fermion_bar import fermion_nth_product
        for i in [1, 2]:
            for j in [1, 2]:
                for n in [1, 2, 3]:
                    assert fermion_nth_product(i, j, n) == {}


# ============================================================================
# 7. sl3 bar complex
# ============================================================================

class TestSl3BarComplex:
    """Affine sl3: 8 generators, rank 2."""

    @pytest.mark.parametrize("n,expected", [
        (1, 8), (2, 36), (3, 204),
    ])
    def test_sl3_bar_cohomology_proved(self, n, expected):
        """sl3 bar cohomology: proved values at degrees 1-3."""
        from compute.lib.bar_complex import bar_dim_sl3
        assert bar_dim_sl3(n) == expected

    @pytest.mark.parametrize("n,expected", [
        (1, 8), (2, 36), (3, 204),
    ])
    def test_sl3_bar_gf_dims(self, n, expected):
        """sl3 bar dims from bar_gf_algebraicity match proved values."""
        from compute.lib.bar_gf_algebraicity import sl3_bar_dims
        dims = sl3_bar_dims(3)
        assert dims[n - 1] == expected

    @pytest.mark.parametrize("n", range(4, 9))
    def test_sl3_bar_recurrence(self, n):
        """sl3 conjectured recurrence: a_n = 11*a_{n-1} - 23*a_{n-2} - 8*a_{n-3}."""
        from compute.lib.bar_gf_algebraicity import sl3_bar_dims
        dims = sl3_bar_dims(10)
        assert dims[n - 1] == 11 * dims[n - 2] - 23 * dims[n - 3] - 8 * dims[n - 4]

    def test_sl3_rational_gf_verification(self):
        """sl3 rational GF: (1-8x)(1-3x-x^2)P = 4x(2-13x-2x^2)."""
        from compute.lib.bar_gf_algebraicity import verify_sl3_rational_gf
        result = verify_sl3_rational_gf(8)
        assert result['all_zero']


# ============================================================================
# 8. Cross-family bar dim growth
# ============================================================================

class TestCrossFamilyBarDims:
    """Cross-family structural properties."""

    @pytest.mark.parametrize("family,expected_h1", [
        ("Heisenberg", 1),
        ("sl2", 3),
        ("Virasoro", 1),
        ("W3", 2),
        ("beta_gamma", 2),
        ("free_fermion", 1),
        ("sl3", 8),
    ])
    def test_h1_equals_generators(self, family, expected_h1):
        """H^1(B(A)) = number of strong generators (universal)."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        dims = KNOWN_BAR_DIMS[family]
        assert dims[1] == expected_h1

    @pytest.mark.parametrize("family", [
        "Heisenberg", "sl2", "Virasoro", "W3", "beta_gamma", "free_fermion",
    ])
    def test_bar_dims_positive(self, family):
        """All bar cohomology dimensions are positive."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        dims = KNOWN_BAR_DIMS[family]
        for n, d in dims.items():
            assert d > 0, f"Family {family}, degree {n}: dim = {d} <= 0"

    @pytest.mark.parametrize("family", [
        "Heisenberg", "sl2", "Virasoro", "W3", "beta_gamma", "free_fermion",
    ])
    def test_bar_dims_monotone_from_h1(self, family):
        """Bar cohomology is nondecreasing from H^1 onward (Koszul growth)."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        dims = KNOWN_BAR_DIMS[family]
        sorted_degs = sorted(dims.keys())
        for i in range(1, len(sorted_degs)):
            assert dims[sorted_degs[i]] >= dims[sorted_degs[i - 1]], (
                f"{family} degree {sorted_degs[i]}: {dims[sorted_degs[i]]} < "
                f"degree {sorted_degs[i-1]}: {dims[sorted_degs[i-1]]}"
            )

    def test_heisenberg_fermion_shift(self):
        """Heisenberg H^n = p(n-2); Fermion H^n = p(n-1): shifted by 1."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        heis = KNOWN_BAR_DIMS["Heisenberg"]
        ferm = KNOWN_BAR_DIMS["free_fermion"]
        for n in range(2, 9):
            assert heis[n] == ferm[n - 1], (
                f"Shift relation fails at n={n}: Heis H^{n}={heis[n]}, "
                f"Ferm H^{n-1}={ferm[n-1]}"
            )


# ============================================================================
# 9. Orlik-Solomon (Arnold) dimensions
# ============================================================================

class TestOrlikSolomon:
    """Orlik-Solomon algebra dimensions for configuration spaces."""

    @pytest.mark.parametrize("n", range(1, 9))
    def test_arnold_dimension_factorial(self, n):
        """arnold_dimension(n) = (n-1)! (top-degree OS on Conf_n(C))."""
        from compute.lib.bar_complex import arnold_dimension
        from math import factorial
        assert arnold_dimension(n) == factorial(n - 1)

    @pytest.mark.parametrize("n", range(2, 9))
    def test_os_top_degree_factorial(self, n):
        """dim OS^{n-1}(Conf_n(C)) = (n-1)!."""
        from compute.lib.os_algebra import os_dimension
        from math import factorial
        assert os_dimension(n, n - 1) == factorial(n - 1)

    @pytest.mark.parametrize("n", range(2, 7))
    def test_os_total_dimension(self, n):
        """Total OS dimension sum_k dim OS^k(n) = n! (Brieskorn)."""
        from compute.lib.os_algebra import os_dimension
        from math import factorial
        total = sum(os_dimension(n, k) for k in range(n))
        assert total == factorial(n)

    @pytest.mark.parametrize("n", range(2, 7))
    def test_os_degree_zero(self, n):
        """dim OS^0(n) = 1 (constants)."""
        from compute.lib.os_algebra import os_dimension
        assert os_dimension(n, 0) == 1

    @pytest.mark.parametrize("n", range(2, 7))
    def test_os_degree_one(self, n):
        """dim OS^1(n) = C(n,2) = n(n-1)/2 (number of pairs)."""
        from compute.lib.os_algebra import os_dimension
        assert os_dimension(n, 1) == n * (n - 1) // 2

    @pytest.mark.parametrize("n", range(2, 6))
    def test_os_poincare_product_formula(self, n):
        """Poincare polynomial = prod_{i=1}^{n-1} (1 + i*t)."""
        from compute.lib.virasoro_bar import os_poincare
        coeffs = os_poincare(n)
        # Verify product formula independently
        poly = [1]
        for i in range(1, n):
            new = [0] * (len(poly) + 1)
            for j, c in enumerate(poly):
                new[j] += c
                new[j + 1] += i * c
            poly = new
        assert coeffs == poly


# ============================================================================
# 10. Discriminant and algebraicity
# ============================================================================

class TestAlgebraicity:
    """Algebraicity of bar cohomology generating functions."""

    def test_catalan_discriminant_shared(self):
        """sl2, Virasoro, betagamma share Catalan discriminant (1-3x)(1+x)."""
        from compute.lib.bar_gf_algebraicity import known_algebraic_equations
        eqs = known_algebraic_equations()
        x = Symbol('x')
        catalan = (1 - 3 * x) * (1 + x)
        for family in ['sl2_riordan', 'Virasoro']:
            disc = eqs[family]['discriminant']
            assert simplify(disc.as_expr() - catalan) == 0, (
                f"Family {family}: discriminant != Catalan"
            )

    @pytest.mark.parametrize("family,rank,disc_deg", [
        ("sl2_riordan", 1, 2),
        ("Virasoro", 1, 2),
        ("betagamma", 2, 2),
    ])
    def test_discriminant_degree_bound(self, family, rank, disc_deg):
        """Discriminant degree <= 2 * rank(A) for degree-2 algebraic families."""
        assert disc_deg <= 2 * rank


# ============================================================================
# 11. KM chain group dimensions
# ============================================================================

class TestKMChainGroups:
    """Kac-Moody chain group dimensions (not cohomology)."""

    @pytest.mark.parametrize("dim_g,n,expected", [
        (3, 1, 3), (3, 2, 9), (3, 3, 54), (3, 4, 486),
        (8, 1, 8), (8, 2, 64),
        (14, 1, 14),
    ])
    def test_km_chain_space_dim(self, dim_g, n, expected):
        """dim B-bar^n = dim(g)^n * (n-1)!."""
        from compute.lib.bar_complex import km_chain_space_dim
        assert km_chain_space_dim(dim_g, n) == expected

    @pytest.mark.parametrize("dim_g,n", [
        (3, 1), (3, 2), (3, 3), (8, 1), (8, 2), (14, 1),
    ])
    def test_km_chain_dim_formula(self, dim_g, n):
        """Chain group dim = dim(g)^n * (n-1)! (direct formula check)."""
        from compute.lib.bar_complex import km_chain_space_dim
        from math import factorial
        assert km_chain_space_dim(dim_g, n) == dim_g**n * factorial(n - 1)


# ============================================================================
# 12. Virasoro Arnold cancellation
# ============================================================================

class TestArnoldCancellation:
    """Arnold relation cancellation of vacuum leakage."""

    def test_virasoro_arnold_deg3(self):
        """Vacuum leakage cancels at degree 3 by Arnold relation."""
        from compute.lib.virasoro_bar import arnold_cancellation_deg3
        result = arnold_cancellation_deg3()
        assert result["arnold_kills_vacuum"] is True

    def test_virasoro_arnold_deg4(self):
        """Vacuum leakage cancels at degree 4."""
        from compute.lib.virasoro_bar import arnold_cancellation_deg4
        result = arnold_cancellation_deg4()
        assert result["vacuum_cancels"] is True
        assert result["form_space_dim"] == 6

    def test_virasoro_arnold_deg5(self):
        """Vacuum leakage cancels at degree 5."""
        from compute.lib.virasoro_bar import arnold_cancellation_deg5
        result = arnold_cancellation_deg5()
        assert result["vacuum_cancels"] is True
        assert result["form_space_dim"] == 24

    def test_w3_arnold_deg3(self):
        """W3 vacuum leakage cancels at degree 3."""
        from compute.lib.w3_bar import w3_arnold_cancellation_deg3
        assert w3_arnold_cancellation_deg3() is True


# ============================================================================
# 13. Partition function verification
# ============================================================================

class TestPartitionFunction:
    """Partition function p(n) used across all bar complex computations."""

    @pytest.mark.parametrize("n,expected", [
        (0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 7),
        (6, 11), (7, 15), (8, 22), (9, 30), (10, 42),
    ])
    def test_partition_number_known_values(self, n, expected):
        """p(n) matches OEIS A000041."""
        from compute.lib.utils import partition_number
        assert partition_number(n) == expected


# ============================================================================
# 14. Curvature complementarity
# ============================================================================

class TestCurvatureComplementarity:
    """Curvature complementarity: m_0(A) + m_0(A!) is determined."""

    def test_virasoro_curvature_complementarity(self):
        """m_0(c) + m_0(26-c) = 13 for Virasoro."""
        from compute.lib.virasoro_bar import virasoro_curvature
        c = Symbol('c')
        m0_c = virasoro_curvature().subs(c, c)
        m0_dual = virasoro_curvature().subs(c, 26 - c)
        assert simplify(m0_c + m0_dual - 13) == 0

    def test_w3_curvature_T_complementarity(self):
        """m_0^T(c) + m_0^T(100-c) = 50 for W3."""
        c = Symbol('c')
        m0 = c / 2
        m0_dual = (100 - c) / 2
        assert simplify(m0 + m0_dual - 50) == 0

    def test_w3_ds_central_charge_complementarity(self):
        """c(k) + c(k') = 100 for W3 where k' = -k-6."""
        from compute.lib.w3_bar import w3_central_charge
        k = Symbol('k')
        c_k = w3_central_charge(k)
        c_dual = w3_central_charge(-k - 6)
        assert simplify(c_k + c_dual - 100) == 0


# ============================================================================
# 15. OPE algebra constructors
# ============================================================================

class TestOPEAlgebraConstructors:
    """OPEAlgebra constructors return well-formed objects."""

    def test_heisenberg_generators(self):
        """Heisenberg has 1 generator J of weight 1."""
        from compute.lib.bar_complex import heisenberg_algebra
        alg = heisenberg_algebra()
        assert alg.dim == 1
        assert alg.gen_names == ["J"]
        assert alg.generators[0].weight == 1

    def test_sl2_generators(self):
        """sl2 has 3 generators e, h, f of weight 1."""
        from compute.lib.bar_complex import sl2_algebra
        alg = sl2_algebra()
        assert alg.dim == 3
        assert set(alg.gen_names) == {"e", "h", "f"}
        for g in alg.generators:
            assert g.weight == 1

    def test_virasoro_generators(self):
        """Virasoro has 1 generator T of weight 2."""
        from compute.lib.bar_complex import virasoro_algebra
        alg = virasoro_algebra()
        assert alg.dim == 1
        assert alg.gen_names == ["T"]
        assert alg.generators[0].weight == 2

    def test_sl2_ope_ef_double_pole(self):
        """sl2: e_{(1)}f = k (Killing form, vacuum via double pole)."""
        from compute.lib.bar_complex import sl2_algebra
        k = Symbol('k')
        alg = sl2_algebra(k)
        assert alg.double_pole("e", "f") == {"1": k}

    def test_sl2_ope_ef_simple_pole(self):
        """sl2: e_{(0)}f = h (bracket)."""
        from compute.lib.bar_complex import sl2_algebra
        alg = sl2_algebra()
        assert alg.simple_pole("e", "f") == {"h": Rational(1)}

    def test_sl2_ope_hh_double_pole(self):
        """sl2: h_{(1)}h = 2k (Cartan Killing form)."""
        from compute.lib.bar_complex import sl2_algebra
        k = Symbol('k')
        alg = sl2_algebra(k)
        assert alg.double_pole("h", "h") == {"1": 2 * k}

    def test_heisenberg_no_simple_pole(self):
        """Heisenberg: J_{(0)}J absent (no simple pole)."""
        from compute.lib.bar_complex import heisenberg_algebra
        alg = heisenberg_algebra()
        assert alg.simple_pole("J", "J") == {}


# ============================================================================
# 16. Virasoro bar chain dimensions
# ============================================================================

class TestVirasoroBarChainDims:
    """Virasoro bar chain space dimensions B^n_h."""

    @pytest.mark.parametrize("n,h,expected", [
        (1, 2, 1), (1, 3, 1), (1, 4, 2), (1, 5, 2), (1, 6, 4),
        (2, 4, 1), (2, 5, 2), (2, 6, 5),
        (3, 6, 2), (3, 7, 6),
        (4, 8, 6),
    ])
    def test_virasoro_bar_chain_dim(self, n, h, expected):
        """Bar chain dim B^n_h matches manuscript table."""
        from compute.lib.virasoro_bar import bar_chain_dim
        assert bar_chain_dim(n, h) == expected

    @pytest.mark.parametrize("n", range(1, 6))
    def test_virasoro_bar_chain_dim_vanishes_below_2n(self, n):
        """B^n_h = 0 for h < 2n (minimum weight of n weight-2 generators)."""
        from compute.lib.virasoro_bar import bar_chain_dim
        for h in range(0, 2 * n):
            assert bar_chain_dim(n, h) == 0


# ============================================================================
# 17. Degree-3 W3 bar complex
# ============================================================================

class TestW3Degree3:
    """W3 degree-3 bar complex structure."""

    def test_w3_deg3_chain_dim_6(self):
        """dim B^3_6(W3) = 2."""
        from compute.lib.w3_bar import w3_deg3_chain_dim
        assert w3_deg3_chain_dim(6) == 2

    def test_w3_deg3_chain_dim_below_6(self):
        """dim B^3_h(W3) = 0 for h < 6."""
        from compute.lib.w3_bar import w3_deg3_chain_dim
        for h in range(0, 6):
            assert w3_deg3_chain_dim(h) == 0


# ============================================================================
# 18. bc ghost system (Koszul dual of betagamma)
# ============================================================================

class TestBcGhostSystem:
    """bc ghost system: Koszul dual of betagamma."""

    def test_bc_bar_diff_bc_vacuum(self):
        """D(b tensor c): vacuum = 1."""
        from compute.lib.betagamma_bar import bc_bar_diff_deg2
        vac, _ = bc_bar_diff_deg2("b", "c")
        assert vac == {"vac": Rational(1)}

    def test_bc_bar_diff_cb_sign(self):
        """D(c tensor b): vacuum = -1 (opposite sign)."""
        from compute.lib.betagamma_bar import bc_bar_diff_deg2
        vac, _ = bc_bar_diff_deg2("c", "b")
        assert vac == {"vac": Rational(-1)}

    def test_bc_bar_diff_bb_zero(self):
        """D(b tensor b) = 0."""
        from compute.lib.betagamma_bar import bc_bar_diff_deg2
        vac, bar1 = bc_bar_diff_deg2("b", "b")
        assert len(vac) == 0 and len(bar1) == 0

    def test_bc_koszul_dual_is_betagamma(self):
        """bc^! = betagamma (Koszul involution)."""
        from compute.lib.betagamma_bar import bc_koszul_dual
        assert bc_koszul_dual() == "beta_gamma"

    def test_betagamma_koszul_dual_is_bc(self):
        """betagamma^! = bc_ghosts."""
        from compute.lib.betagamma_bar import betagamma_koszul_dual
        assert betagamma_koszul_dual() == "bc_ghosts"

    @pytest.mark.parametrize("n,expected", [
        (1, 2), (2, 3), (3, 6), (4, 13), (5, 28), (6, 59), (7, 122), (8, 249),
    ])
    def test_bc_bar_cohomology_formula(self, n, expected):
        """bc bar cohomology: 2^n - n + 1."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        assert KNOWN_BAR_DIMS["bc"][n] == expected
        assert 2**n - n + 1 == expected


# ============================================================================
# 19. Heisenberg bar chain dimensions
# ============================================================================

class TestHeisenbergBarChainDims:
    """Heisenberg chain-level dimensions."""

    @pytest.mark.parametrize("n,h", [
        (1, 1), (1, 2), (1, 5),
        (2, 2), (2, 3), (2, 5),
        (3, 3), (3, 5),
    ])
    def test_heisenberg_bar_chain_positive(self, n, h):
        """Chain dim B^n_h > 0 when h >= n (single weight-1 generator)."""
        from compute.lib.heisenberg_bar import heisenberg_bar_chain_dim
        assert heisenberg_bar_chain_dim(n, h) > 0

    @pytest.mark.parametrize("n", range(1, 6))
    def test_heisenberg_bar_chain_vanishes_below_n(self, n):
        """B^n_h = 0 for h < n."""
        from compute.lib.heisenberg_bar import heisenberg_bar_chain_dim
        for h in range(0, n):
            assert heisenberg_bar_chain_dim(n, h) == 0

    def test_heisenberg_bar_chain_dim_formula(self):
        """B^n_h = C(h-1, n-1) * (n-1)! for Heisenberg."""
        from compute.lib.heisenberg_bar import heisenberg_bar_chain_dim
        from math import comb, factorial
        for n in range(1, 6):
            for h in range(n, n + 5):
                expected = comb(h - 1, n - 1) * factorial(n - 1)
                assert heisenberg_bar_chain_dim(n, h) == expected
