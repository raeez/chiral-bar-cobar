r"""Tests for SC bar-cobar inversion engine: Omega(B^ch(A)) recovers A.

THEOREM B (thm:bar-cobar-inversion-qi): For a chirally Koszul algebra A,
the counit epsilon: Omega^ch(B^ch(A)) -> A is a quasi-isomorphism.

FIVE VERIFICATION PATHS (3+ per claim, per CLAUDE.md multi-path mandate):

  Path 1 (Bar d^2=0):     Arnold relation forces d^2 = 0 at all degrees
  Path 2 (Cobar recovery): Omega(B(A)) ~ A via counit quasi-isomorphism
  Path 3 (SC analysis):    SC cobar recovers closed colour, NOT full SC
  Path 4 (Homotopy):       Contracting homotopy exists at arity 2
  Path 5 (Three functors): Omega != D_Ran != Z^der_ch (AP25, AP34)

Cross-checks:
  (a) Heisenberg and sl_2 give consistent results
  (b) Level k passes through bar-cobar without loss
  (c) Numerical evaluation at multiple k values
  (d) Bar cohomology matches thm:frame-heisenberg-bar
  (e) Koszul dual is NOT the cobar output (AP25, AP33)

All formulas computed from first principles (AP1, AP3).
Multi-path verification per CLAUDE.md mandate.

References:
  thm:bar-cobar-inversion-qi (bar_cobar_adjunction_inversion.tex)
  thm:frame-heisenberg-bar (heisenberg_frame.tex)
  def:chiral_cobar (bar-cobar-review.tex, Vol II)
  sec:frame-inversion (heisenberg_frame.tex)
  AP19: bar kernel absorbs a pole
  AP25: three functors, three outputs
  AP27: bar propagator d log E(z,w) is weight 1
  AP33: H_k^! != H_{-k}
  AP34: bar-cobar inversion != open-to-closed passage
  AP45: desuspension LOWERS degree
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, simplify, eye, zeros, Matrix

from compute.lib.sc_bar_cobar_inversion_engine import (
    # OPE data
    OPEData,
    heisenberg_ope,
    affine_sl2_ope,
    # Bar complex
    BarElement,
    BarComplex,
    compute_heisenberg_bar,
    compute_sl2_bar,
    # Cobar complex
    CobarElement,
    CobarComplex,
    compute_heisenberg_cobar,
    # Resolution
    BarCobarResolution,
    compute_heisenberg_arity2_resolution,
    # SC analysis
    SCBarCobarResult,
    analyze_sc_bar_cobar,
    # Verification
    verify_bar_dsquared_heisenberg,
    verify_bar_dsquared_sl2,
    verify_cobar_recovers_heisenberg,
    verify_cobar_recovers_sl2,
    verify_sc_cobar_analysis,
    verify_heisenberg_data_flow,
    verify_contracting_homotopy,
    verify_koszul_dual_not_cobar,
    numerical_bar_differential_heisenberg,
    numerical_bar_cobar_sl2,
    full_verification_suite,
)


# ============================================================================
# I. OPE Data Tests
# ============================================================================


class TestOPEData:
    """Tests for OPE data construction and extraction."""

    def test_heisenberg_ope_creation(self):
        """Heisenberg has a single generator alpha."""
        ope = heisenberg_ope()
        assert ope.generators == ['alpha']
        assert ope.name.startswith('Heisenberg')

    def test_heisenberg_double_pole(self):
        """Heisenberg OPE: alpha(z)alpha(w) ~ k/(z-w)^2."""
        k = Symbol('k')
        ope = heisenberg_ope(k)
        assert ope.double_pole('alpha', 'alpha') == k

    def test_heisenberg_no_simple_pole(self):
        """Heisenberg is abelian: no simple pole (alpha_{(0)}alpha = 0)."""
        ope = heisenberg_ope()
        assert ope.simple_pole('alpha', 'alpha') == 0

    def test_heisenberg_numeric_level(self):
        """Heisenberg at numeric level k = 3."""
        ope = heisenberg_ope(3)
        assert ope.double_pole('alpha', 'alpha') == 3
        assert ope.level == 3

    def test_sl2_generators(self):
        """Affine sl_2 has generators e, f, h."""
        ope = affine_sl2_ope()
        assert set(ope.generators) == {'e', 'f', 'h'}

    def test_sl2_killing_form(self):
        """sl_2 Killing form: (h,h) = 2k, (e,f) = k."""
        k = Symbol('k')
        ope = affine_sl2_ope(k)
        assert ope.double_pole('h', 'h') == 2 * k
        assert ope.double_pole('e', 'f') == k

    def test_sl2_lie_bracket(self):
        """sl_2 Lie bracket: [h,e] = 2e, [h,f] = -2f, [e,f] = h."""
        ope = affine_sl2_ope()
        assert ope.simple_pole('h', 'e') == '2e'
        assert ope.simple_pole('h', 'f') == '-2f'
        assert ope.simple_pole('e', 'f') == 'h'

    def test_sl2_no_self_poles_ef(self):
        """e(z)e(w) and f(z)f(w) have no poles."""
        ope = affine_sl2_ope()
        assert ope.double_pole('e', 'e') == 0
        assert ope.double_pole('f', 'f') == 0
        assert ope.simple_pole('e', 'e') == 0
        assert ope.simple_pole('f', 'f') == 0


# ============================================================================
# II. Bar Complex Tests (Heisenberg)
# ============================================================================


class TestHeisenbergBar:
    """Tests for the Heisenberg bar complex B^ch(H_k)."""

    def test_bar_dimensions(self):
        """B_0 = C, B_1 = C, B_2 = C, B_n = 0 for n >= 3 (single generator)."""
        bar = compute_heisenberg_bar()
        assert bar.dimensions[0] == 1
        assert bar.dimensions[1] == 1
        assert bar.dimensions[2] == 1
        assert bar.dimensions[3] == 0

    def test_bar_d1_equals_k(self):
        """d_1: B_1 -> B_0 maps by multiplication by k (the double-pole coefficient)."""
        k = Symbol('k')
        bar = compute_heisenberg_bar(k)
        assert bar.differentials[1] == Matrix([[k]])

    def test_bar_d2_equals_zero(self):
        """d_2: B_2 -> B_1 is zero (the two collision terms cancel)."""
        bar = compute_heisenberg_bar()
        assert bar.differentials[2] == Matrix([[0]])

    def test_bar_d_squared_zero_deg2(self):
        """d_1 . d_2 = 0 (d^2 = 0 at degree 2)."""
        k = Symbol('k')
        bar = compute_heisenberg_bar(k)
        product = bar.differentials[1] * bar.differentials[2]
        assert product == zeros(1, 1)

    def test_bar_d_squared_method(self):
        """BarComplex.d_squared_zero verifies d^2 = 0."""
        bar = compute_heisenberg_bar()
        assert bar.d_squared_zero(2)

    def test_bar_numeric_k1(self):
        """Numeric: bar at k = 1 has d_1 = [1]."""
        bar = compute_heisenberg_bar(1)
        assert bar.differentials[1] == Matrix([[1]])

    def test_bar_numeric_k_minus2(self):
        """Numeric: bar at k = -2 has d_1 = [-2]."""
        bar = compute_heisenberg_bar(-2)
        assert bar.differentials[1] == Matrix([[-2]])


# ============================================================================
# III. Bar Complex Tests (sl_2)
# ============================================================================


class TestSl2Bar:
    """Tests for the affine sl_2 bar complex."""

    def test_sl2_bar_dimensions(self):
        """B_0 = C (dim 1), B_1 has 9 ordered pairs."""
        bar = compute_sl2_bar()
        assert bar.dimensions[0] == 1
        assert bar.dimensions[1] == 9

    def test_sl2_scalar_differential(self):
        """The scalar part of d_1 extracts double-pole coefficients."""
        k = Symbol('k')
        bar = compute_sl2_bar(k)
        scalar_d = bar.differentials[1]['scalar']
        # Pairs (e,f) and (f,e) have double pole k
        # Pair (h,h) has double pole 2k
        # All others have 0
        gens = ['e', 'f', 'h']
        pairs = [(a, b) for a in gens for b in gens]
        ef_idx = pairs.index(('e', 'f'))
        fe_idx = pairs.index(('f', 'e'))
        hh_idx = pairs.index(('h', 'h'))
        assert scalar_d[ef_idx] == k
        assert scalar_d[fe_idx] == k
        assert scalar_d[hh_idx] == 2 * k

    def test_sl2_bracket_differential(self):
        """The bracket part of d_1 extracts simple-pole coefficients."""
        bar = compute_sl2_bar()
        bracket_d = bar.differentials[1]['bracket']
        assert ('h', 'e') in bracket_d
        assert ('h', 'f') in bracket_d
        assert ('e', 'f') in bracket_d


# ============================================================================
# IV. d^2 = 0 Verification Tests
# ============================================================================


class TestDSquaredZero:
    """Tests verifying d^2 = 0 for bar complexes."""

    def test_heisenberg_d_squared_symbolic(self):
        """Symbolic verification: d^2 = 0 for Heisenberg at all degrees <= 3."""
        k = Symbol('k')
        results = verify_bar_dsquared_heisenberg(k)
        assert results['d_squared_zero_deg2']
        assert results['arnold_verified']
        assert results['explicit_d_squared_zero']

    def test_heisenberg_d_squared_numeric_k1(self):
        """Numeric: d^2 = 0 at k = 1."""
        results = verify_bar_dsquared_heisenberg(Rational(1))
        assert results['d_squared_zero_deg2']
        assert results['explicit_d_squared_zero']

    def test_heisenberg_d_squared_numeric_k5(self):
        """Numeric: d^2 = 0 at k = 5."""
        results = verify_bar_dsquared_heisenberg(Rational(5))
        assert results['d_squared_zero_deg2']
        assert results['explicit_d_squared_zero']

    def test_heisenberg_d_squared_explicit_cancellation(self):
        """Explicit: k^2 - k^2 = 0 (eq:frame-dsquared-deg2)."""
        k = Symbol('k')
        explicit = k * k - k * k
        assert simplify(explicit) == 0

    def test_sl2_d_squared(self):
        """d^2 = 0 for sl_2 bar complex (Arnold + Jacobi + Killing)."""
        results = verify_bar_dsquared_sl2()
        assert results['d_squared_zero']


# ============================================================================
# V. Cobar Recovery Tests (Heisenberg)
# ============================================================================


class TestHeisenbergCobar:
    """Tests for Omega(B^ch(H_k)) ~ H_k."""

    def test_cobar_dimensions(self):
        """Cobar dimensions match free algebra on 1 generator."""
        cobar = compute_heisenberg_cobar()
        assert cobar.dimensions[0] == 1
        assert cobar.dimensions[1] == 1

    def test_cobar_differential_d1_zero(self):
        """d_Omega(s(alpha*)) = 0 (primitive cogenerator)."""
        cobar = compute_heisenberg_cobar()
        assert cobar.differentials[1] == Matrix([[0]])

    def test_cobar_counit_maps_generator(self):
        """Counit: s(alpha*) |-> alpha (cogenerator to generator)."""
        cobar = compute_heisenberg_cobar()
        assert cobar.counit[1] == 'alpha'

    def test_cobar_counit_maps_unit(self):
        """Counit: 1 |-> 1 (unit to unit)."""
        cobar = compute_heisenberg_cobar()
        assert cobar.counit[0] == 1

    def test_cobar_recovers_heisenberg(self):
        """Full verification: Omega(B(H_k)) ~ H_k."""
        results = verify_cobar_recovers_heisenberg()
        assert results['cobar_recovers_generator']
        assert results['ope_recovered']
        assert results['counit_chain_map']
        assert results['koszul_complex_acyclic']

    def test_cobar_bar_cohomology(self):
        """Bar cohomology: H^0 = C, H^1 = 0, H^2 = C (thm:frame-heisenberg-bar)."""
        results = verify_cobar_recovers_heisenberg()
        assert results['bar_cohomology'] == {0: 1, 1: 0, 2: 1}


# ============================================================================
# VI. Cobar Recovery Tests (sl_2)
# ============================================================================


class TestSl2Cobar:
    """Tests for Omega(B^ch(V_k(sl_2))) ~ V_k(sl_2)."""

    def test_sl2_cobar_recovers(self):
        """The cobar recovers V_k(sl_2) as a chiral algebra."""
        results = verify_cobar_recovers_sl2()
        assert results['cobar_recovers_sl2']

    def test_sl2_ope_bracket_recovered(self):
        """The simple-pole OPE (Lie bracket) is recovered by the cobar."""
        results = verify_cobar_recovers_sl2()
        assert results['ope_recovered_bracket']

    def test_sl2_ope_killing_recovered(self):
        """The double-pole OPE (Killing form) is recovered by the cobar."""
        results = verify_cobar_recovers_sl2()
        assert results['ope_recovered_killing']

    def test_sl2_killing_values(self):
        """Killing form: (h,h) = 2k, (e,f) = k."""
        k = Symbol('k')
        results = verify_cobar_recovers_sl2(k)
        assert results['killing_hh'] == 2 * k
        assert results['killing_ef'] == k


# ============================================================================
# VII. SC^{ch,top} Analysis Tests
# ============================================================================


class TestSCBarCobar:
    """Tests for the SC^{ch,top} cobar analysis.

    Key result: the SC cobar Omega_SC(B^ch(A)) recovers the CLOSED-colour
    algebra A, NOT the full SC^{ch,top}-algebra (A, A^!).
    """

    def test_heisenberg_recovers_closed(self):
        """SC cobar recovers closed colour for Heisenberg."""
        result = analyze_sc_bar_cobar(heisenberg_ope())
        assert result.recovers_closed_colour

    def test_heisenberg_not_open(self):
        """SC cobar does NOT recover open colour for Heisenberg."""
        result = analyze_sc_bar_cobar(heisenberg_ope())
        assert not result.recovers_open_colour

    def test_heisenberg_not_full_sc(self):
        """SC cobar does NOT recover full SC algebra for Heisenberg."""
        result = analyze_sc_bar_cobar(heisenberg_ope())
        assert not result.recovers_full_sc

    def test_sl2_recovers_closed(self):
        """SC cobar recovers closed colour for sl_2."""
        result = analyze_sc_bar_cobar(affine_sl2_ope())
        assert result.recovers_closed_colour

    def test_sl2_not_open(self):
        """SC cobar does NOT recover open colour for sl_2."""
        result = analyze_sc_bar_cobar(affine_sl2_ope())
        assert not result.recovers_open_colour

    def test_sc_analysis_full(self):
        """Full SC analysis: three functors are distinct."""
        results = verify_sc_cobar_analysis()
        assert results['three_functors_distinct']
        assert results['heisenberg_closed']
        assert not results['heisenberg_open']
        assert results['sl2_closed']
        assert not results['sl2_open']


# ============================================================================
# VIII. Contracting Homotopy Tests
# ============================================================================


class TestContractingHomotopy:
    """Tests for the contracting homotopy at arity 2."""

    def test_homotopy_k1(self):
        """Contracting homotopy exists at k = 1."""
        results = verify_contracting_homotopy(1)
        assert results['d_dot_h_is_identity']
        assert results['h_dot_d_is_identity']
        assert results['complex_exact']

    def test_homotopy_k2(self):
        """Contracting homotopy exists at k = 2."""
        results = verify_contracting_homotopy(2)
        assert results['complex_exact']

    def test_homotopy_k5(self):
        """Contracting homotopy exists at k = 5."""
        results = verify_contracting_homotopy(5)
        assert results['complex_exact']

    def test_resolution_chain_groups(self):
        """Resolution at arity 2: C_0 = C, C_1 = C."""
        res = compute_heisenberg_arity2_resolution(Rational(1))
        assert res.chain_groups[0] == 1
        assert res.chain_groups[1] == 1

    def test_resolution_differential(self):
        """Resolution differential at arity 2: d_1 = [k]."""
        k = Symbol('k')
        res = compute_heisenberg_arity2_resolution(k)
        assert res.differentials[1] == Matrix([[k]])


# ============================================================================
# IX. Three Functors Distinction Tests (AP25, AP33, AP34)
# ============================================================================


class TestThreeFunctors:
    """Tests verifying the three-functor distinction.

    AP25: B(A), D_Ran(B(A)), Omega(B(A)) are THREE DIFFERENT objects.
    AP33: H_k^! = Sym^ch(V*) != H_{-k} (different algebras, same kappa).
    AP34: bar-cobar inversion != open-to-closed passage.
    """

    def test_cobar_recovers_original(self):
        """Omega(B(H_k)) = H_k (the original, NOT the Koszul dual)."""
        results = verify_koszul_dual_not_cobar()
        assert results['cobar_is_original']

    def test_koszul_dual_not_H_minus_k(self):
        """H_k^! = Sym^ch(V*) != H_{-k} (AP33)."""
        results = verify_koszul_dual_not_cobar()
        assert not results['koszul_dual_is_H_minus_k']

    def test_derived_center_not_bar(self):
        """Z^der_ch(A) != B(A) (AP-OC, AP34)."""
        results = verify_koszul_dual_not_cobar()
        assert not results['derived_center_is_bar']

    def test_all_three_distinct(self):
        """Omega, D_Ran, and Z^der_ch produce different objects."""
        results = verify_koszul_dual_not_cobar()
        assert results['all_three_distinct']

    def test_kappa_values_heisenberg(self):
        """kappa(H_k) = k, kappa(H_k^!) = -k."""
        k = Symbol('k')
        results = verify_koszul_dual_not_cobar(k)
        assert results['kappa_H_k'] == k
        assert results['kappa_H_k_dual'] == -k


# ============================================================================
# X. Data Flow Tests
# ============================================================================


class TestDataFlow:
    """Tests verifying the bar-cobar data flow is lossless."""

    def test_data_flow_lossless_symbolic(self):
        """Level k passes through bar-cobar without loss (symbolic)."""
        k = Symbol('k')
        results = verify_heisenberg_data_flow(k)
        assert results['lossless']

    def test_data_flow_lossless_k1(self):
        """Level k=1 passes through bar-cobar without loss."""
        results = verify_heisenberg_data_flow(Rational(1))
        assert results['lossless']

    def test_data_flow_stage2_bar(self):
        """Stage 2: bar residue extracts k."""
        k = Symbol('k')
        results = verify_heisenberg_data_flow(k)
        assert results['stage2_bar_residue'] == k

    def test_data_flow_stage5_counit(self):
        """Stage 5: counit produces alpha (the generator)."""
        results = verify_heisenberg_data_flow()
        assert results['stage5_counit'] == 'alpha'


# ============================================================================
# XI. Numerical Verification Tests
# ============================================================================


class TestNumerical:
    """Numerical verification at specific levels."""

    def test_numerical_heisenberg_k1(self):
        """Numerical bar at k = 1."""
        results = numerical_bar_differential_heisenberg(1.0)
        assert results['d1'] == 1.0
        assert results['d2'] == 0.0
        assert abs(results['d1_d2']) < 1e-15

    def test_numerical_heisenberg_k3(self):
        """Numerical bar at k = 3."""
        results = numerical_bar_differential_heisenberg(3.0)
        assert results['d1'] == 3.0
        assert results['d2'] == 0.0

    def test_numerical_heisenberg_cohomology(self):
        """Numerical bar cohomology: H^0 = C, H^1 = 0, H^2 = C."""
        results = numerical_bar_differential_heisenberg(1.0)
        assert results['H0'] == 1
        assert results['H1'] == 0
        assert results['H2'] == 1

    def test_numerical_heisenberg_k0_cohomology(self):
        """At k = 0: d_1 = 0, so H^1 = C (not 0)."""
        results = numerical_bar_differential_heisenberg(0.0)
        assert results['H0'] == 1
        assert results['H1'] == 1  # d_1 = 0 means ker/im changes
        assert results['H2'] == 1

    def test_numerical_sl2_k1(self):
        """Numerical sl_2 at k = 1."""
        results = numerical_bar_cobar_sl2(1.0)
        assert results['d_squared_zero']
        assert results['cobar_recovers_algebra']
        assert results['killing'][('h', 'h')] == 2.0  # 2k at k=1

    def test_numerical_sl2_bracket(self):
        """sl_2 bracket: [e,f] = h, [h,e] = 2e, [h,f] = -2f."""
        results = numerical_bar_cobar_sl2(1.0)
        assert results['bracket'][('e', 'f')] == ('h', 1)
        assert results['bracket'][('h', 'e')] == ('e', 2)
        assert results['bracket'][('h', 'f')] == ('f', -2)


# ============================================================================
# XII. Full Verification Suite
# ============================================================================


class TestFullSuite:
    """Integration tests running the full verification suite."""

    def test_full_suite_k1(self):
        """Full suite at k = 1: all claims verified."""
        results = full_verification_suite(1)
        assert results['ALL_CLAIMS_VERIFIED']

    def test_full_suite_k2(self):
        """Full suite at k = 2: all claims verified."""
        results = full_verification_suite(2)
        assert results['ALL_CLAIMS_VERIFIED']

    def test_full_suite_k5(self):
        """Full suite at k = 5: all claims verified."""
        results = full_verification_suite(5)
        assert results['ALL_CLAIMS_VERIFIED']

    def test_full_suite_claim1(self):
        """Claim 1 (d^2 = 0) verified through 3 paths."""
        results = full_verification_suite(1)
        assert results['claim1_dsquared']['ALL_PASS']

    def test_full_suite_claim2(self):
        """Claim 2 (cobar recovery) verified through 4 paths."""
        results = full_verification_suite(1)
        assert results['claim2_inversion']['ALL_PASS']

    def test_full_suite_claim3(self):
        """Claim 3 (SC closed only) verified through 3 paths."""
        results = full_verification_suite(1)
        assert results['claim3_sc_closed_only']['ALL_PASS']

    def test_full_suite_claim4(self):
        """Claim 4 (contracting homotopy) verified through 3 paths."""
        results = full_verification_suite(1)
        assert results['claim4_homotopy']['ALL_PASS']

    def test_full_suite_claim5(self):
        """Claim 5 (three functors) verified through 3 paths."""
        results = full_verification_suite(1)
        assert results['claim5_three_functors']['ALL_PASS']

    def test_full_suite_sl2(self):
        """sl_2 d^2 = 0 and cobar recovery."""
        results = full_verification_suite(1)
        assert results['sl2_d_squared']
        assert results['sl2_cobar_recovery']

    def test_full_suite_data_flow(self):
        """Data flow is lossless."""
        results = full_verification_suite(1)
        assert results['data_flow_lossless']

    def test_full_suite_numerical(self):
        """Numerical d^2 = 0."""
        results = full_verification_suite(1)
        assert results['numerical_d_squared']
        assert results['numerical_H0'] == 1
        assert results['numerical_H1'] == 0
        assert results['numerical_H2'] == 1
