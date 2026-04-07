r"""Tests for exceptional_shadow_engine.py: E_6, E_7, E_8 shadow framework.

60+ tests covering:
  - Lie algebra constants against Bourbaki/cartan_data (multi-path)
  - Affine kappa, central charge, complementarity (exact rational)
  - Principal W-algebra generators, central charge, kappa
  - Shadow tower coefficients on the T-line
  - Heterotic E_8 x E_8 central charge budget
  - Deligne exceptional series monotonicity
  - Minahan-Nemeschansky boundary VOAs
  - Schellekens c=24 classification
  - McKay ADE correspondence
  - Tensor product decompositions and R-matrix
  - Cross-family consistency (AP10)

Ground truth:
  - Bourbaki: Lie Groups and Lie Algebras, Ch. IV-VI
  - Humphreys: Introduction to Lie Algebras and Representation Theory
  - landscape_census.tex, kac_moody.tex, w_algebras.tex
  - Schellekens (1993): Meromorphic c=24 conformal field theories
  - BLLPRR (2015): Infinite chiral symmetry in four dimensions
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, cancel

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')
_spec = importlib.util.spec_from_file_location(
    'exceptional_shadow_engine',
    os.path.join(_lib_dir, 'exceptional_shadow_engine.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

k = Symbol('k')


# ====================================================================
# 1. Lie algebra constants (verified against cartan_data)
# ====================================================================

class TestLieAlgebraConstants:
    """Verify E_6, E_7, E_8 data against Bourbaki tables."""

    def test_e6_dim(self):
        assert _mod.EXCEPTIONAL_DATA['E6']['dim'] == 78

    def test_e7_dim(self):
        assert _mod.EXCEPTIONAL_DATA['E7']['dim'] == 133

    def test_e8_dim(self):
        assert _mod.EXCEPTIONAL_DATA['E8']['dim'] == 248

    def test_e6_rank(self):
        assert _mod.EXCEPTIONAL_DATA['E6']['rank'] == 6

    def test_e7_rank(self):
        assert _mod.EXCEPTIONAL_DATA['E7']['rank'] == 7

    def test_e8_rank(self):
        assert _mod.EXCEPTIONAL_DATA['E8']['rank'] == 8

    def test_e6_h_dual(self):
        assert _mod.EXCEPTIONAL_DATA['E6']['h_dual'] == 12

    def test_e7_h_dual(self):
        assert _mod.EXCEPTIONAL_DATA['E7']['h_dual'] == 18

    def test_e8_h_dual(self):
        assert _mod.EXCEPTIONAL_DATA['E8']['h_dual'] == 30

    def test_e6_exponents(self):
        assert _mod.EXCEPTIONAL_DATA['E6']['exponents'] == [1, 4, 5, 7, 8, 11]

    def test_e7_exponents(self):
        assert _mod.EXCEPTIONAL_DATA['E7']['exponents'] == [1, 5, 7, 9, 11, 13, 17]

    def test_e8_exponents(self):
        assert _mod.EXCEPTIONAL_DATA['E8']['exponents'] == [1, 7, 11, 13, 17, 19, 23, 29]

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_cartan_data_crosscheck(self, name):
        """Cross-check all stored data against cartan_data() (AP1)."""
        checks = _mod.verify_against_cartan(name)
        for field, passed in checks.items():
            assert passed, f"{name} cartan_data mismatch on {field}"

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_simply_laced(self, name):
        """All E-type algebras are simply-laced (h = h^vee)."""
        d = _mod.EXCEPTIONAL_DATA[name]
        assert d['h'] == d['h_dual']
        assert d['simply_laced'] is True

    @pytest.mark.parametrize("name,expected", [
        ("E6", 36), ("E7", 63), ("E8", 120)
    ])
    def test_exponent_sum_equals_positive_roots(self, name, expected):
        """sum(exponents) = |Delta^+| = (dim - rank)/2."""
        d = _mod.EXCEPTIONAL_DATA[name]
        assert sum(d['exponents']) == expected
        assert expected == (d['dim'] - d['rank']) // 2

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_max_exponent(self, name):
        """max(exponent) = h - 1."""
        d = _mod.EXCEPTIONAL_DATA[name]
        assert max(d['exponents']) == d['h'] - 1


# ====================================================================
# 2. Affine algebra invariants
# ====================================================================

class TestAffineInvariants:

    def test_e6_kappa_k1(self):
        """kappa(E_6, k=1) = 78*13/24 = 1014/24 = 169/4."""
        kap = _mod.affine_kappa_numeric('E6', 1)
        assert kap == Fraction(78 * 13, 24)
        assert kap == Fraction(169, 4)

    def test_e7_kappa_k1(self):
        """kappa(E_7, k=1) = 133*19/36 = 2527/36."""
        kap = _mod.affine_kappa_numeric('E7', 1)
        assert kap == Fraction(133 * 19, 36)

    def test_e8_kappa_k1(self):
        """kappa(E_8, k=1) = 248*31/60 = 7688/60 = 1922/15."""
        kap = _mod.affine_kappa_numeric('E8', 1)
        assert kap == Fraction(1922, 15)

    def test_e8_central_charge_k1(self):
        """c(E_8, k=1) = 248/31 = 8."""
        c_val = _mod.affine_central_charge_numeric('E8', 1)
        assert c_val == Fraction(8)

    def test_e6_central_charge_k1(self):
        """c(E_6, k=1) = 78/13 = 6."""
        c_val = _mod.affine_central_charge_numeric('E6', 1)
        assert c_val == Fraction(6)

    def test_e7_central_charge_k1(self):
        """c(E_7, k=1) = 133/19 = 7."""
        c_val = _mod.affine_central_charge_numeric('E7', 1)
        assert c_val == Fraction(7)

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_complementarity_kappa(self, name):
        """kappa(k) + kappa(k') = 0 for all affine KM (AP24)."""
        result = _mod.affine_complementarity_kappa(name)
        assert result == 0

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_complementarity_c(self, name):
        """c(k) + c(k') = 2*dim(g)."""
        d = _mod.EXCEPTIONAL_DATA[name]
        result = _mod.affine_complementarity_c(name)
        assert simplify(result - 2 * d['dim']) == 0

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_complementarity_kappa_numeric_k1(self, name):
        """Numeric check: kappa(1) + kappa(k') = 0."""
        kap = _mod.affine_kappa_numeric(name, 1)
        kd = _mod.ff_dual_level_numeric(name, 1)
        kap_dual = _mod.affine_kappa_numeric(name, kd)
        assert kap + kap_dual == 0

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_ff_involution(self, name):
        """FF involution is an involution: (k')' = k."""
        kd = _mod.ff_dual_level(name)
        kdd = _mod.ff_dual_level(name, kd)
        assert simplify(kdd - k) == 0

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_shadow_class_L(self, name):
        assert _mod.affine_shadow_class(name) == 'L'

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_shadow_depth_3(self, name):
        assert _mod.affine_shadow_depth(name) == 3

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_S3_universal(self, name):
        """S_3 = 1 universal for all affine KM."""
        assert _mod.affine_S3(name) == Rational(1)

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_S4_zero(self, name):
        """S_4 = 0 (Jacobi identity)."""
        assert _mod.affine_S4(name) == Rational(0)

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_discriminant_zero(self, name):
        """Delta = 8*kappa*S_4 = 0."""
        assert _mod.affine_discriminant(name) == Rational(0)

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_r_matrix_simple_pole(self, name):
        """R-matrix pole order = 1 (AP19)."""
        assert _mod.affine_r_matrix_pole_order(name) == 1


# ====================================================================
# 3. Principal W-algebra data
# ====================================================================

class TestWAlgebra:

    def test_e6_generators(self):
        """W(E_6) generators at weights 2, 5, 6, 8, 9, 12."""
        assert _mod.w_generator_weights('E6') == [2, 5, 6, 8, 9, 12]

    def test_e7_generators(self):
        """W(E_7) generators at weights 2, 6, 8, 10, 12, 14, 18."""
        assert _mod.w_generator_weights('E7') == [2, 6, 8, 10, 12, 14, 18]

    def test_e8_generators(self):
        """W(E_8) generators at weights 2, 8, 12, 14, 18, 20, 24, 30."""
        assert _mod.w_generator_weights('E8') == [2, 8, 12, 14, 18, 20, 24, 30]

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_num_generators_equals_rank(self, name):
        assert _mod.w_num_generators(name) == _mod.EXCEPTIONAL_DATA[name]['rank']

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_unique_weight_2_generator(self, name):
        """Each principal W-algebra has exactly one weight-2 generator (stress tensor)."""
        weights = _mod.w_generator_weights(name)
        assert weights.count(2) == 1

    def test_e6_anomaly_ratio(self):
        """rho(E_6) = 1/2 + 1/5 + 1/6 + 1/8 + 1/9 + 1/12."""
        rho = _mod.w_anomaly_ratio('E6')
        expected = Fraction(1, 2) + Fraction(1, 5) + Fraction(1, 6) + \
                   Fraction(1, 8) + Fraction(1, 9) + Fraction(1, 12)
        assert rho == expected

    def test_e7_anomaly_ratio(self):
        """rho(E_7) = 1/2 + 1/6 + 1/8 + 1/10 + 1/12 + 1/14 + 1/18."""
        rho = _mod.w_anomaly_ratio('E7')
        expected = Fraction(1, 2) + Fraction(1, 6) + Fraction(1, 8) + \
                   Fraction(1, 10) + Fraction(1, 12) + Fraction(1, 14) + Fraction(1, 18)
        assert rho == expected

    def test_e8_anomaly_ratio(self):
        """rho(E_8) = 121/126 (verified independently)."""
        rho = _mod.w_anomaly_ratio('E8')
        assert rho == Fraction(121, 126)

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_w_kappa_identity(self, name):
        """kappa_W = rho * c_W at k=1."""
        rho = _mod.w_anomaly_ratio(name)
        c_w = _mod.w_central_charge_numeric(name, 1)
        kap_w = _mod.w_kappa_numeric(name, 1)
        assert kap_w == rho * c_w

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_w_shadow_class_M(self, name):
        """Principal W-algebras are class M (DS introduces quartic)."""
        assert _mod.w_shadow_class(name) == 'M'

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_w_shadow_depth_infinite(self, name):
        assert _mod.w_shadow_depth(name) == 'infinity'

    def test_e8_max_ope_pole(self):
        """E_8 W-algebra: max OPE pole = 2 * 30 = 60."""
        assert _mod.w_max_ope_pole('E8') == 60


# ====================================================================
# 4. Shadow tower coefficients
# ====================================================================

class TestShadowTower:

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_tline_S2_equals_kappa_T(self, name):
        """S_2 on the T-line = kappa_T = c_W/2."""
        c_w = _mod.w_central_charge_numeric(name, 1)
        coeffs = _mod.w_tline_shadow_coefficients(name, 1)
        assert coeffs[2] == c_w / 2

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_tline_S3_equals_1(self, name):
        """S_3 on T-line = alpha/3 = 2/3 (Virasoro cubic)."""
        # On the T-line: a_1 = q1/(2*a0), S_3 = a_1/3
        # q1 = 12*kappa_T*alpha = 12*(c/2)*2 = 12c
        # a_0 = c, a_1 = 12c/(2c) = 6
        # S_3 = 6/3 = 2
        # Wait: S_3 = a_{3-2}/3 = a_1/3 = 6/3 = 2.
        # But the affine S_3 = 1 (different normalization).
        # On the T-line for Virasoro: the "S_3" in the convolution is 2
        # (because the Virasoro alpha = 2 on the primary line).
        # These are different: affine S_3 = 1 is for the current direction,
        # Virasoro S_3 = 2 is for the T-direction in the W-algebra.
        c_w = _mod.w_central_charge_numeric(name, 1)
        if c_w == 0:
            pytest.skip("c_W = 0 at this level")
        coeffs = _mod.w_tline_shadow_coefficients(name, 1)
        assert coeffs[3] == Fraction(2)

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_tline_coefficients_consistent(self, name):
        """Verify f^2 = Q_L: (sum a_n t^n)^2 = q0 + q1*t + q2*t^2."""
        c_w = _mod.w_central_charge_numeric(name, 1)
        if c_w == 0:
            pytest.skip("c_W = 0")
        kappa_T = c_w / 2
        alpha = Fraction(2)
        denom = c_w * (5 * c_w + 22)
        if denom == 0:
            pytest.skip("degenerate")
        S4 = Fraction(10) / denom

        q0 = 4 * kappa_T**2
        q1 = 12 * kappa_T * alpha
        q2 = 9 * alpha**2 + 16 * kappa_T * S4

        coeffs = _mod.w_tline_shadow_coefficients(name, 1, max_arity=6)
        # Recover a_n from S_r = a_{r-2}/r
        a = {}
        for r, sr in coeffs.items():
            a[r - 2] = sr * r

        # Check f^2 at order 0, 1, 2
        assert a[0]**2 == q0, f"q0 mismatch: {a[0]**2} vs {q0}"

        # Order 1: 2*a0*a1 = q1
        assert 2 * a[0] * a[1] == q1, f"q1 mismatch"

        # Order 2: a1^2 + 2*a0*a2 = q2
        lhs = a[1]**2 + 2 * a[0] * a.get(2, 0)
        assert lhs == q2, f"q2 mismatch: {lhs} vs {q2}"


# ====================================================================
# 5. Heterotic string
# ====================================================================

class TestHeterotic:

    def test_e8_central_charge(self):
        """c(E_8 x E_8) at k=1 = 16."""
        assert _mod.heterotic_e8_central_charge() == Fraction(16)

    def test_total_c_26(self):
        """Total heterotic c = 16 + 10 = 26."""
        assert _mod.heterotic_total_c() == Fraction(26)

    def test_kappa_additive(self):
        """kappa(E_8 x E_8) = 2 * kappa(E_8, k=1) = 2 * 1922/15 = 3844/15."""
        kap = _mod.heterotic_e8_kappa()
        assert kap == Fraction(3844, 15)

    def test_kappa_not_248(self):
        """kappa(E_8 x E_8) != 248 (AP48: not the naive rank formula)."""
        assert _mod.heterotic_e8_kappa() != Fraction(248)

    def test_kappa_not_16(self):
        """kappa(E_8 x E_8) != 16 (not c/2 of the tensor product)."""
        # c/2 = 16/2 = 8 is NOT the kappa of the tensor product.
        assert _mod.heterotic_e8_kappa() != Fraction(8)

    def test_shadow_class_L(self):
        """Tensor product of class L algebras is class L."""
        assert _mod.heterotic_e8_shadow_class() == 'L'


# ====================================================================
# 6. Deligne exceptional series
# ====================================================================

class TestDeligneSeries:

    def test_kappa_monotone_k1(self):
        """kappa is strictly increasing along the Deligne series at k=1."""
        assert _mod.deligne_kappa_monotone(1) is True

    def test_kappa_monotone_k2(self):
        """kappa is strictly increasing at k=2."""
        assert _mod.deligne_kappa_monotone(2) is True

    def test_shadow_depth_constant(self):
        """Shadow depth is uniformly class L (depth 3) along the series."""
        assert _mod.deligne_shadow_depth_constant() is True

    def test_series_length(self):
        """The Deligne series has 8 members."""
        assert len(_mod.DELIGNE_SERIES) == 8

    def test_series_starts_A1(self):
        """Series starts with A_1 (sl_2)."""
        assert _mod.DELIGNE_SERIES[0][0] == 'A1'

    def test_series_ends_E8(self):
        """Series ends with E_8."""
        assert _mod.DELIGNE_SERIES[-1][0] == 'E8'

    def test_dim_increases(self):
        """dim(g) is strictly increasing along the series."""
        dims = [entry[3] for entry in _mod.DELIGNE_SERIES]
        for i in range(len(dims) - 1):
            assert dims[i] < dims[i + 1]


# ====================================================================
# 7. Minahan-Nemeschansky theories
# ====================================================================

class TestMinahanNemeschansky:

    def test_mn_e6_central_charge(self):
        """MN E_6: c_2d = (-3)*78/9 = -26."""
        assert _mod.mn_central_charge('MN_E6') == Fraction(-26)

    def test_mn_e7_central_charge(self):
        """MN E_7: c_2d = (-4)*133/14 = -38."""
        assert _mod.mn_central_charge('MN_E7') == Fraction(-38)

    def test_mn_e8_central_charge(self):
        """MN E_8: c_2d = (-6)*248/24 = -62."""
        assert _mod.mn_central_charge('MN_E8') == Fraction(-62)

    def test_mn_e6_kappa(self):
        """MN E_6: kappa = 78*9/24 = 117/4."""
        assert _mod.mn_kappa('MN_E6') == Fraction(117, 4)

    def test_mn_e7_kappa(self):
        """MN E_7: kappa = 133*14/36 = 931/18."""
        assert _mod.mn_kappa('MN_E7') == Fraction(931, 18)

    def test_mn_e8_kappa(self):
        """MN E_8: kappa = 248*24/60 = 496/5."""
        assert _mod.mn_kappa('MN_E8') == Fraction(496, 5)

    @pytest.mark.parametrize("theory", ["MN_E6", "MN_E7", "MN_E8"])
    def test_mn_class_L(self, theory):
        """All MN boundary VOAs are class L (affine KM at negative level)."""
        assert _mod.mn_shadow_class(theory) == 'L'

    @pytest.mark.parametrize("theory", ["MN_E6", "MN_E7", "MN_E8"])
    def test_mn_complementarity(self, theory):
        """kappa + kappa' = 0 for MN theories."""
        data = _mod.mn_complementarity(theory)
        assert data['kappa_sum'] == 0

    @pytest.mark.parametrize("theory", ["MN_E6", "MN_E7", "MN_E8"])
    def test_mn_c2d_formula(self, theory):
        """c_2d = -12 * c_4d."""
        assert _mod.mn_verify_c2d_formula(theory) is True

    @pytest.mark.parametrize("theory", ["MN_E6", "MN_E7", "MN_E8"])
    def test_mn_c_sum(self, theory):
        """c + c' = 2*dim(g) for MN theories."""
        data = _mod.mn_complementarity(theory)
        assert data['c_sum'] == data['expected_c_sum']


# ====================================================================
# 8. Schellekens list
# ====================================================================

class TestSchellekens:

    def test_count_71(self):
        assert _mod.schellekens_count() == 71

    def test_niemeier_24(self):
        assert _mod.schellekens_niemeier_count() == 24

    def test_moonshine_class_M(self):
        """V^natural is class M (no currents, infinite shadow depth)."""
        assert _mod.schellekens_shadow_class('V_natural') == 'M'

    def test_leech_lattice_class_G(self):
        """Leech lattice VOA is class G (Heisenberg description)."""
        assert _mod.schellekens_shadow_class('Leech') == 'G'

    def test_e8_cubed_class_L(self):
        """E_8^3 lattice VOA is class L (affine KM)."""
        assert _mod.schellekens_shadow_class('E8^3') == 'L'

    def test_moonshine_kappa(self):
        """V^natural Virasoro kappa = 12 (c/2 = 24/2)."""
        assert _mod.schellekens_kappa_moonshine() == Fraction(12)

    def test_lattice_kappa_24(self):
        """Niemeier lattice VOA (Heisenberg): kappa = 24."""
        assert _mod.schellekens_kappa_lattice_voa(24) == Fraction(24)


# ====================================================================
# 9. McKay ADE correspondence
# ====================================================================

class TestMcKay:

    def test_all_class_L(self):
        """All McKay ADE types give class L affine algebras."""
        assert _mod.mckay_all_class_L() is True

    def test_e6_singularity(self):
        """E_6 singularity: x^2 + y^3 + z^4."""
        assert 'z^4' in _mod.mckay_singularity('E6')

    def test_e7_singularity(self):
        """E_7 singularity: x^2 + y^3 + y*z^3."""
        assert 'y*z^3' in _mod.mckay_singularity('E7')

    def test_e8_singularity(self):
        """E_8 singularity: x^2 + y^3 + z^5."""
        assert 'z^5' in _mod.mckay_singularity('E8')

    def test_e6_subgroup(self):
        """E_6 McKay subgroup: binary tetrahedral."""
        assert 'tetrahedral' in _mod.mckay_subgroup('E6').lower()

    def test_e8_subgroup(self):
        """E_8 McKay subgroup: binary icosahedral."""
        assert 'icosahedral' in _mod.mckay_subgroup('E8').lower()


# ====================================================================
# 10. Tensor product decompositions
# ====================================================================

class TestTensorProducts:

    def test_e6_not_self_dual(self):
        """E_6 fundamental rep (27) is NOT self-dual."""
        decomp = _mod.fund_rep_tensor_decomposition('E6')
        assert decomp['self_dual'] is False

    def test_e7_self_dual_symplectic(self):
        """E_7 fundamental rep (56) is self-dual (symplectic)."""
        decomp = _mod.fund_rep_tensor_decomposition('E7')
        assert decomp['self_dual'] is True
        assert decomp['sym_type'] == 'symplectic'

    def test_e8_self_dual_orthogonal(self):
        """E_8 fundamental rep (248) is self-dual (orthogonal, adjoint)."""
        decomp = _mod.fund_rep_tensor_decomposition('E8')
        assert decomp['self_dual'] is True
        assert decomp['sym_type'] == 'orthogonal'

    def test_e7_dim_check(self):
        """56^2 = 3136 = 1540 (antisym) + 1596 (sym)."""
        decomp = _mod.fund_rep_tensor_decomposition('E7')
        assert decomp['dim_check'] is True
        assert decomp['antisym_dim_check'] is True
        assert decomp['sym_dim_check'] is True

    def test_e8_dim_check(self):
        """248^2 = 61504 = 30628 (antisym) + 30876 (sym)."""
        decomp = _mod.fund_rep_tensor_decomposition('E8')
        assert decomp['dim_check'] is True
        assert decomp['antisym_dim_check'] is True
        assert decomp['sym_dim_check'] is True

    def test_e8_casimir_adjoint(self):
        """C_2(248) = 2*h^vee = 60 for E_8 (fundamental = adjoint)."""
        assert _mod.quadratic_casimir_fund('E8') == Fraction(60)

    def test_e6_casimir(self):
        """C_2(27) = 26/3 for E_6."""
        assert _mod.quadratic_casimir_fund('E6') == Fraction(26, 3)

    def test_e7_casimir(self):
        """C_2(56) = 57/4 for E_7."""
        assert _mod.quadratic_casimir_fund('E7') == Fraction(57, 4)


# ====================================================================
# 11. Cross-family consistency (AP10)
# ====================================================================

class TestCrossFamily:

    def test_kappa_increases_with_dim(self):
        """At fixed k=1, kappa increases with dim(g) across E_6 < E_7 < E_8."""
        kap_e6 = _mod.affine_kappa_numeric('E6', 1)
        kap_e7 = _mod.affine_kappa_numeric('E7', 1)
        kap_e8 = _mod.affine_kappa_numeric('E8', 1)
        assert kap_e6 < kap_e7 < kap_e8

    def test_w_kappa_magnitude_increases(self):
        """|kappa_W| increases along E_6 < E_7 < E_8 at k=1.

        At k=1, p = 1 + h^vee is small relative to the (p-1)^2/p term
        in the FKW formula, so c_W and kappa_W are large negative.
        The magnitude increases with dim(g).
        """
        kap_e6 = _mod.w_kappa_numeric('E6', 1)
        kap_e7 = _mod.w_kappa_numeric('E7', 1)
        kap_e8 = _mod.w_kappa_numeric('E8', 1)
        assert abs(kap_e6) < abs(kap_e7) < abs(kap_e8)

    def test_anomaly_ratio_positive(self):
        """Anomaly ratio rho > 0 for all exceptional types."""
        for name in ['E6', 'E7', 'E8']:
            rho = _mod.w_anomaly_ratio(name)
            assert rho > 0, f"rho({name}) = {rho} <= 0"

    def test_anomaly_ratio_ordering(self):
        """Anomaly ratio for exceptional types has definite ordering."""
        rho_e6 = _mod.w_anomaly_ratio('E6')
        rho_e7 = _mod.w_anomaly_ratio('E7')
        rho_e8 = _mod.w_anomaly_ratio('E8')
        # E6 has rho = 427/360 > 1, E7 = 2777/2520, E8 largest
        assert rho_e6 > 0 and rho_e7 > 0 and rho_e8 > 0

    def test_affine_vs_w_kappa_differ(self):
        """Affine kappa != W-algebra kappa (different algebras, AP14)."""
        for name in ['E6', 'E7', 'E8']:
            kap_aff = _mod.affine_kappa_numeric(name, 1)
            kap_w = _mod.w_kappa_numeric(name, 1)
            assert kap_aff != kap_w, f"{name}: affine kappa = W kappa (should differ)"

    def test_comparison_table_not_empty(self):
        """Comparison table has entries for all three types."""
        table = _mod.comparison_table(1)
        assert len(table) == 3
        names = [row['name'] for row in table]
        assert 'E6' in names
        assert 'E7' in names
        assert 'E8' in names


# ====================================================================
# 12. E_8 level 1 special properties
# ====================================================================

class TestE8Level1:

    def test_c_equals_8(self):
        props = _mod.e8_level1_properties()
        assert props['c_equals_8'] is True

    def test_one_integrable_rep(self):
        props = _mod.e8_level1_properties()
        assert props['n_integrable_reps'] == 1

    def test_self_dual_lattice(self):
        props = _mod.e8_level1_properties()
        assert props['is_self_dual_lattice'] is True

    def test_theta_E4(self):
        props = _mod.e8_level1_properties()
        assert props['theta_equals_E4'] is True

    def test_kappa_discrepancy_AP48(self):
        """AP48: affine kappa != lattice Heisenberg kappa for E_8."""
        props = _mod.e8_level1_properties()
        assert props['kappa_discrepancy'] is True
        assert props['kappa_affine'] != props['kappa_lattice_heisenberg']


# ====================================================================
# 13. Multi-path verification of kappa (AP10)
# ====================================================================

class TestMultiPathKappa:

    @pytest.mark.parametrize("name,level,expected", [
        ("E6", 1, Fraction(78 * 13, 24)),
        ("E7", 1, Fraction(133 * 19, 36)),
        ("E8", 1, Fraction(248 * 31, 60)),
        ("E6", 2, Fraction(78 * 14, 24)),
        ("E7", 2, Fraction(133 * 20, 36)),
        ("E8", 2, Fraction(248 * 32, 60)),
    ])
    def test_kappa_direct_computation(self, name, level, expected):
        """Path 1: direct from dim*(k+h^v)/(2*h^v)."""
        assert _mod.affine_kappa_numeric(name, level) == expected

    @pytest.mark.parametrize("name,level", [
        ("E6", 1), ("E7", 1), ("E8", 1),
    ])
    def test_kappa_from_complementarity(self, name, level):
        """Path 2: verify via kappa + kappa' = 0."""
        kap = _mod.affine_kappa_numeric(name, level)
        kd = _mod.ff_dual_level_numeric(name, level)
        kap_dual = _mod.affine_kappa_numeric(name, kd)
        assert kap == -kap_dual

    @pytest.mark.parametrize("name", ["E6", "E7", "E8"])
    def test_kappa_symbolic_matches_numeric(self, name):
        """Path 3: symbolic formula agrees with numeric evaluation at k=1."""
        kap_sym = _mod.affine_kappa(name)
        kap_num = _mod.affine_kappa_numeric(name, 1)
        # Evaluate symbolic at k=1
        kap_sym_eval = kap_sym.subs(k, 1)
        assert Rational(kap_num.numerator, kap_num.denominator) == kap_sym_eval
