r"""Tests for Poisson cohomology of the Sklyanin bracket on sl_2*.

THEOREM (Sklyanin-Poisson-cohomology):
H^k_pi(sl_2*, {,}_{STS}) = 0 for k = 1, 2, 3 (polynomial Poisson cohomology
of the modified Lie-Poisson bracket with Drinfeld r-matrix correction).
H^0 = C[C_{STS}] where C_{STS} = xy + z^2/4 + z/2.

THREE VERIFICATION PATHS (per CLAUDE.md multi-path mandate):

    Path 1 (Direct computation): Explicit delta_pi, ker/im in polynomial
        multivectors at low polynomial degree.
    Path 2 (Chevalley-Eilenberg): H^k_{LP}(g*) = H^k_{CE}(g, C^infty(g*)),
        Whitehead => vanishing for k = 1, 2.
    Path 3 (Spectral sequence): Filter by polynomial degree, E_1 page is
        CE with Sym coefficients, Whitehead on each graded piece.

Cross-checks:
    (a) Jacobi identity for the STS bracket (=> pi is Poisson)
    (b) delta_pi^2 = 0 (consistency of the Poisson complex)
    (c) STS Casimir generates H^0 (direct verification)
    (d) Unimodularity => Poincare duality H^3 = H^0
    (e) Explicit bracket values match sl_2 structure constants + r-matrix
    (f) LP Casimir is NOT an STS Casimir (the shift z/2 is essential)

References:
    Lichnerowicz (1977), Sklyanin (1982), Semenov-Tian-Shansky (1983)
    chiral_koszul_pairs.tex (Koszulness characterization programme)
"""

import sys
import os
import pytest
from fractions import Fraction

from sympy import (
    Rational, Symbol, diff, expand, simplify, symbols, S,
)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_sklyanin_poisson_cohomology_engine import (
    # Coordinates
    x, y, z, COORDS, N_DIM,
    # Structure
    structure_constants, killing_form, casimir_element,
    # Bivectors
    lie_poisson_bivector, r_matrix_standard, r_matrix_correction,
    sklyanin_bivector, sklyanin_bracket,
    # Jacobi
    verify_jacobi_identity,
    # Casimirs
    sklyanin_casimir,
    # Poisson differential
    hamiltonian_vector_field,
    poisson_differential_on_0forms,
    poisson_differential_on_1forms,
    poisson_differential_on_2forms,
    # d^2 = 0
    verify_d_squared_zero_on_functions,
    verify_d_squared_zero_on_vector_fields,
    # Cohomology
    compute_h0_polynomial_degree,
    compute_h1_low_degree,
    compute_h2_low_degree,
    compute_h3_low_degree,
    # CE and spectral sequence
    ce_cohomology_sl2,
    spectral_sequence_argument,
    # Full results
    verify_h2_vanishing,
    full_poisson_cohomology_summary,
    # Explicit data
    explicit_bracket_table,
    explicit_bivector_components,
)


# ============================================================================
# I. sl_2 STRUCTURE (foundational)
# ============================================================================

class TestSl2Structure:
    """Verify the sl_2 Lie algebra data."""

    def test_structure_constants_antisymmetry(self):
        """Structure constants c^k_{ij} = -c^k_{ji}."""
        sc = structure_constants()
        for k in range(3):
            for i in range(3):
                for j in range(3):
                    assert sc[k][i][j] == -sc[k][j][i], (
                        f"c^{k}_{{{i},{j}}} = {sc[k][i][j]} != -c^{k}_{{{j},{i}}} = {-sc[k][j][i]}")

    def test_structure_constants_jacobi(self):
        """Jacobi identity: c^m_{ij} c^n_{mk} + cyclic = 0."""
        sc = structure_constants()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for n in range(3):
                        total = Rational(0)
                        for m in range(3):
                            total += sc[m][i][j] * sc[n][m][k]
                            total += sc[m][j][k] * sc[n][m][i]
                            total += sc[m][k][i] * sc[n][m][j]
                        assert total == 0, (
                            f"Jacobi fails for (i,j,k,n) = ({i},{j},{k},{n}): {total}")

    def test_killing_form_values(self):
        """Killing form: B(e,f) = 4, B(h,h) = 8."""
        B = killing_form()
        assert B[0, 1] == 4    # B(e, f)
        assert B[1, 0] == 4    # B(f, e)
        assert B[2, 2] == 8    # B(h, h)
        assert B[0, 0] == 0    # B(e, e)
        assert B[1, 1] == 0    # B(f, f)
        assert B[0, 2] == 0    # B(e, h)

    def test_killing_form_symmetric(self):
        """Killing form is symmetric."""
        B = killing_form()
        for i in range(3):
            for j in range(3):
                assert B[i, j] == B[j, i]

    def test_casimir_element(self):
        """C_2 = xy + z^2/4."""
        C2 = casimir_element()
        assert expand(C2 - (x * y + z**2 / 4)) == 0

    def test_dimension(self):
        """sl_2 has dimension 3."""
        assert N_DIM == 3
        assert len(COORDS) == 3


# ============================================================================
# II. POISSON BIVECTORS
# ============================================================================

class TestPoissonBivectors:
    """Verify the Lie-Poisson and Sklyanin bivectors."""

    def test_lie_poisson_bracket_values(self):
        """LP bracket: {x,y} = z, {x,z} = -2x, {y,z} = 2y."""
        pi_lp = lie_poisson_bivector()
        assert expand(pi_lp[0, 1] - z) == 0        # {x_e, x_f} = z
        assert expand(pi_lp[0, 2] - (-2*x)) == 0   # {x_e, x_h} = -2x_e
        assert expand(pi_lp[1, 2] - 2*y) == 0      # {x_f, x_h} = 2x_f

    def test_lie_poisson_antisymmetric(self):
        """LP bivector is antisymmetric."""
        pi_lp = lie_poisson_bivector()
        for i in range(3):
            for j in range(3):
                assert expand(pi_lp[i, j] + pi_lp[j, i]) == 0

    def test_r_matrix_correction(self):
        """r-matrix correction: only (0,1) component is nonzero."""
        r = r_matrix_correction()
        assert r[0, 1] == Rational(1)
        assert r[1, 0] == Rational(-1)
        assert r[0, 2] == 0
        assert r[1, 2] == 0
        assert r[2, 2] == 0

    def test_sklyanin_bivector_values(self):
        """STS bracket: {x,y} = z+1, {x,z} = -2x, {y,z} = 2y."""
        pi = sklyanin_bivector()
        assert expand(pi[0, 1] - (z + 1)) == 0
        assert expand(pi[0, 2] - (-2*x)) == 0
        assert expand(pi[1, 2] - 2*y) == 0

    def test_sklyanin_bivector_antisymmetric(self):
        """Sklyanin bivector is antisymmetric."""
        pi = sklyanin_bivector()
        for i in range(3):
            for j in range(3):
                assert expand(pi[i, j] + pi[j, i]) == 0

    def test_sklyanin_bracket_function(self):
        """sklyanin_bracket(x, y) = z + 1."""
        assert expand(sklyanin_bracket(x, y) - (z + 1)) == 0
        assert expand(sklyanin_bracket(x, z) - (-2*x)) == 0
        assert expand(sklyanin_bracket(y, z) - 2*y) == 0

    def test_sklyanin_bracket_antisymmetry(self):
        """{f, g} = -{g, f}."""
        for f_expr, g_expr in [(x, y), (x, z), (y, z), (x**2, y*z)]:
            fg = sklyanin_bracket(f_expr, g_expr)
            gf = sklyanin_bracket(g_expr, f_expr)
            assert expand(fg + gf) == 0

    def test_explicit_bracket_table(self):
        """Cross-check explicit bracket table."""
        table = explicit_bracket_table()
        assert expand(table[('x', 'y')] - (z + 1)) == 0
        assert expand(table[('x', 'z')] - (-2*x)) == 0
        assert expand(table[('y', 'z')] - 2*y) == 0

    def test_explicit_bivector_components(self):
        """Cross-check explicit bivector components."""
        bv = explicit_bivector_components()
        assert expand(bv[(0, 1)] - (z + 1)) == 0
        assert expand(bv[(0, 2)] - (-2*x)) == 0
        assert expand(bv[(1, 2)] - 2*y) == 0


# ============================================================================
# III. JACOBI IDENTITY
# ============================================================================

class TestJacobiIdentity:
    """Verify Jacobi for both LP and STS brackets."""

    def test_jacobi_lie_poisson(self):
        """LP bracket satisfies Jacobi (from Lie algebra Jacobi)."""
        pi_lp = lie_poisson_bivector()
        result = verify_jacobi_identity(pi_lp)
        assert result['satisfied'], f"Jacobi violations: {result['violations']}"

    def test_jacobi_sklyanin(self):
        """STS bracket satisfies Jacobi (from CYBE for r-matrix)."""
        pi_sts = sklyanin_bivector()
        result = verify_jacobi_identity(pi_sts)
        assert result['satisfied'], f"Jacobi violations: {result['violations']}"


# ============================================================================
# IV. CASIMIRS (H^0)
# ============================================================================

class TestCasimirs:
    """Verify the Casimir structure of the STS bracket."""

    def test_sts_casimir_is_casimir(self):
        """C_{STS} = xy + z^2/4 + z/2 is a Casimir of the STS bracket."""
        result = sklyanin_casimir()
        assert result['sts_is_casimir'], (
            f"C_STS is not a Casimir: brackets = {result['sts_bracket_values']}")

    def test_lp_casimir_not_sts_casimir(self):
        """C_{LP} = xy + z^2/4 is NOT a Casimir of the STS bracket."""
        result = sklyanin_casimir()
        assert not result['lp_is_casimir_of_sts'], (
            "LP Casimir should not be an STS Casimir")

    def test_casimir_shift(self):
        """C_{STS} = C_{LP} + z/2."""
        result = sklyanin_casimir()
        assert expand(result['casimir_sts'] - result['casimir_lp'] - z/2) == 0

    def test_casimir_powers_are_casimirs(self):
        """C_{STS}^n is a Casimir for n = 2, 3."""
        C = sklyanin_casimir()['casimir_sts']
        for n in [2, 3]:
            Cn = C**n
            for coord in [x, y, z]:
                assert expand(sklyanin_bracket(expand(Cn), coord)) == 0, (
                    f"C_STS^{n} is not a Casimir: {{C^{n}, {coord}}} != 0")

    def test_h0_cumulative_degree_0(self):
        """Casimirs of degree <= 0: just constants (dim 1)."""
        result = compute_h0_polynomial_degree(max_deg=2)
        assert result['casimirs_by_degree'][0]['dim'] == 1

    def test_h0_cumulative_degree_1(self):
        """Casimirs of degree <= 1: still just constants (dim 1, no new)."""
        result = compute_h0_polynomial_degree(max_deg=2)
        assert result['casimirs_by_degree'][1]['dim'] == 1

    def test_h0_cumulative_degree_2(self):
        """Casimirs of degree <= 2: constants + C_STS (dim 2)."""
        result = compute_h0_polynomial_degree(max_deg=2)
        # C_STS = xy + z^2/4 + z/2 is inhomogeneous (deg 2 + deg 1)
        # so it only appears in the cumulative degree-2 space.
        assert result['casimirs_by_degree'][2]['dim'] == 2


# ============================================================================
# V. POISSON COMPLEX: delta_pi^2 = 0
# ============================================================================

class TestPoissonComplex:
    """Verify the Poisson differential squares to zero."""

    def test_d_squared_zero_on_coordinates(self):
        """delta_pi^2(x_i) = 0 for coordinate functions."""
        for coord in [x, y, z]:
            Xf = poisson_differential_on_0forms(coord)
            d2f = poisson_differential_on_1forms(Xf)
            for i in range(3):
                for j in range(3):
                    assert expand(d2f[i, j]) == 0, (
                        f"d^2({coord}) != 0 at ({i},{j}): {d2f[i,j]}")

    def test_d_squared_zero_on_monomials(self):
        """delta_pi^2(m) = 0 for degree-2 monomials."""
        result = verify_d_squared_zero_on_functions(
            [x*y, x*z, y*z, x**2, y**2, z**2])
        assert result['all_vanish'], "d^2 != 0 on some monomial"

    def test_d_squared_zero_on_casimir(self):
        """delta_pi^2(C_{STS}) = 0 (trivially, since delta(C) = 0)."""
        C = sklyanin_casimir()['casimir_sts']
        Xc = poisson_differential_on_0forms(C)
        # delta(C) should already be zero (Casimir)
        for comp in Xc:
            assert expand(comp) == 0, f"Hamiltonian VF of Casimir is not zero: {Xc}"

    def test_d_squared_zero_on_vector_fields(self):
        """delta_pi^2(V) = 0 for test vector fields."""
        result = verify_d_squared_zero_on_vector_fields()
        assert result['all_vanish'], "d^2 != 0 on some vector field"


# ============================================================================
# VI. H^2 VANISHING (the main theorem)
# ============================================================================

class TestH2Vanishing:
    """The central result: H^2_pi(sl_2*, STS) = 0."""

    def test_h2_degree_0(self):
        """H^2 at degree 0 = 0."""
        result = compute_h2_low_degree(max_deg=1)
        assert result[0]['dim_h2'] == 0, (
            f"H^2(deg 0) = {result[0]['dim_h2']} != 0")

    def test_h2_degree_1(self):
        """H^2 at degree 1 = 0."""
        result = compute_h2_low_degree(max_deg=1)
        assert result[1]['dim_h2'] == 0, (
            f"H^2(deg 1) = {result[1]['dim_h2']} != 0")

    def test_h2_verify_full(self):
        """Full H^2 vanishing verification (three paths)."""
        result = verify_h2_vanishing()
        assert result['h2_vanishes'], "H^2 does not vanish at low degree"
        assert result['three_paths_agree'], "Three verification paths disagree"

    def test_h2_ce_prediction(self):
        """CE/Whitehead predicts H^2 = 0."""
        ce = ce_cohomology_sl2()
        assert ce['h2_ce'] == 0
        assert ce['whitehead_applies']
        assert ce['semisimple']

    def test_h2_spectral_sequence_prediction(self):
        """Spectral sequence predicts H^2 = 0."""
        ss = spectral_sequence_argument()
        assert ss['conclusion']['h2'] == 0

    def test_koszul_consequence(self):
        """H^2 = 0 implies unobstructedness for sl_2 deformations."""
        result = verify_h2_vanishing()
        assert 'unobstructedness' in result['koszul_consequence'].lower() or \
               'rigidity' in result['koszul_consequence'].lower()


# ============================================================================
# VII. UNIMODULARITY AND POINCARE DUALITY
# ============================================================================

class TestUnimodularity:
    """Verify unimodularity and Poincare duality."""

    def test_unimodularity(self):
        """The STS bivector is unimodular: div(pi) = 0."""
        result = full_poisson_cohomology_summary()
        assert result['is_unimodular'], (
            f"Modular VF = {result['modular_vector_field']} != 0")

    def test_poincare_duality(self):
        """Unimodular => Poincare duality H^3 = H^0."""
        result = full_poisson_cohomology_summary()
        assert result['poincare_duality']


# ============================================================================
# VIII. HAMILTONIAN VECTOR FIELDS
# ============================================================================

class TestHamiltonianVectorFields:
    """Verify Hamiltonian vector field computations."""

    def test_hamiltonian_vf_of_x(self):
        """X_x = {x, -}: components from STS bracket with x."""
        Xx = hamiltonian_vector_field(x)
        # hamiltonian_vector_field returns [{f,x}, {f,y}, {f,z}]
        assert expand(Xx[0]) == 0               # {x, x} = 0
        assert expand(Xx[1] - (z + 1)) == 0     # {x, y} = z + 1
        assert expand(Xx[2] - (-2*x)) == 0      # {x, z} = -2x

    def test_hamiltonian_vf_of_y(self):
        """X_y components."""
        Xy = hamiltonian_vector_field(y)
        assert expand(Xy[0] - (-(z + 1))) == 0  # {y, x} = -(z+1)
        assert expand(Xy[1]) == 0                 # {y, y} = 0
        assert expand(Xy[2] - 2*y) == 0          # {y, z} = 2y

    def test_delta_pi_0_of_x(self):
        """delta_pi(x)^i = pi^{ij} dx/dx_j = pi^{i0}."""
        Dx = poisson_differential_on_0forms(x)
        # pi^{00} = 0, pi^{10} = -(z+1), pi^{20} = 2x
        assert expand(Dx[0]) == 0
        assert expand(Dx[1] - (-(z + 1))) == 0
        assert expand(Dx[2] - 2*x) == 0

    def test_hamiltonian_vf_of_casimir(self):
        """X_{C_STS} = 0 (Casimir has vanishing Hamiltonian VF)."""
        C = sklyanin_casimir()['casimir_sts']
        Xc = hamiltonian_vector_field(C)
        for i, comp in enumerate(Xc):
            assert expand(comp) == 0, f"X_C component {i} = {comp} != 0"

    def test_delta_pi_0_of_casimir(self):
        """delta_pi(C_STS) = 0: Casimir is in ker(delta_pi)."""
        C = sklyanin_casimir()['casimir_sts']
        Dc = poisson_differential_on_0forms(C)
        for i, comp in enumerate(Dc):
            assert expand(comp) == 0, f"delta_pi(C)^{i} = {comp} != 0"


# ============================================================================
# IX. CROSS-CHECKS AND CONSISTENCY
# ============================================================================

class TestCrossChecks:
    """Cross-checks between different computation paths."""

    def test_lp_vs_sts_bracket_difference(self):
        """STS - LP = constant r-matrix correction."""
        pi_lp = lie_poisson_bivector()
        pi_sts = sklyanin_bivector()
        r = r_matrix_correction()
        for i in range(3):
            for j in range(3):
                assert expand(pi_sts[i, j] - pi_lp[i, j] - r[i, j]) == 0

    def test_bracket_leibniz(self):
        """{fg, h} = f{g,h} + g{f,h} (Leibniz rule)."""
        f_expr, g_expr, h_expr = x, y, z
        fg_h = sklyanin_bracket(f_expr * g_expr, h_expr)
        f_gh = f_expr * sklyanin_bracket(g_expr, h_expr)
        g_fh = g_expr * sklyanin_bracket(f_expr, h_expr)
        assert expand(fg_h - f_gh - g_fh) == 0, "Leibniz fails for (x, y, z)"

    def test_bracket_leibniz_quadratic(self):
        """{f, g} satisfies Leibniz for quadratic f."""
        f_expr = x**2 + y*z
        g_expr = z
        fg = sklyanin_bracket(f_expr, g_expr)
        # By direct computation
        expected = 2*x * sklyanin_bracket(x, z) + y * sklyanin_bracket(z, z) + z * sklyanin_bracket(y, z)
        # {z, z} = 0
        expected2 = 2*x * (-2*x) + z * 2*y
        assert expand(fg - expected2) == 0

    def test_h0_h2_consistency(self):
        """H^0 nontrivial but H^2 = 0: consistent with rigidity."""
        h0 = compute_h0_polynomial_degree(max_deg=2)
        h2 = compute_h2_low_degree(max_deg=1)
        # H^0(<=2) = 2 (constants + C_STS); Casimir exists
        assert h0['casimirs_by_degree'][2]['dim'] == 2
        # H^2(<=0) = H^2(<=1) = 0
        assert h2[0]['dim_h2'] == 0
        assert h2[1]['dim_h2'] == 0

    def test_full_cohomology_summary(self):
        """Full summary is internally consistent."""
        result = full_poisson_cohomology_summary()
        assert result['h1'] == 0
        assert result['h2'] == 0
        assert result['is_unimodular']


# ============================================================================
# X. LP CASIMIR VERIFICATION (independent path)
# ============================================================================

class TestLPCasimir:
    """Verify the LP Casimir is correct for the LP bracket."""

    def test_lp_casimir_is_lp_casimir(self):
        """C_{LP} = xy + z^2/4 is a Casimir of the LP bracket."""
        C_lp = casimir_element()
        pi_lp = lie_poisson_bivector()
        coords_list = [x, y, z]
        for idx, coord in enumerate(coords_list):
            bracket = S.Zero
            for i in range(3):
                for j in range(3):
                    if pi_lp[i, j] != 0:
                        bracket += pi_lp[i, j] * diff(C_lp, coords_list[i]) * diff(coord, coords_list[j])
            assert expand(bracket) == 0, (
                f"{{C_LP, {coord}}}_LP = {bracket} != 0")

    def test_casimir_degree_2_invariant(self):
        """The Casimir has degree 2 (quadratic invariant)."""
        from sympy import degree as sym_degree, Poly
        C = casimir_element()
        p = Poly(C, x, y, z)
        assert p.total_degree() == 2


# ============================================================================
# XI. MULTI-PATH CROSS-CHECKS (AP10 compliance)
# ============================================================================

class TestMultiPathCrossChecks:
    """Cross-checks between independent computation paths (AP10).

    Each numerical/structural claim is verified by at least 2 independent
    methods to avoid hardcoded-wrong-value errors.
    """

    def test_h2_vanishing_path1_vs_path2(self):
        """H^2 = 0: direct computation agrees with CE/Whitehead prediction."""
        h2_direct = compute_h2_low_degree(max_deg=1)
        ce = ce_cohomology_sl2()
        # Path 1: direct
        for d in range(2):
            assert h2_direct[d]['dim_h2'] == 0
        # Path 2: CE/Whitehead
        assert ce['h2_ce'] == 0
        # Agreement
        assert h2_direct[0]['dim_h2'] == ce['h2_ce']

    def test_h2_vanishing_path1_vs_path3(self):
        """H^2 = 0: direct computation agrees with spectral sequence."""
        h2_direct = compute_h2_low_degree(max_deg=1)
        ss = spectral_sequence_argument()
        assert h2_direct[0]['dim_h2'] == ss['conclusion']['h2']
        assert h2_direct[1]['dim_h2'] == ss['conclusion']['h2']

    def test_casimir_direct_vs_bracket(self):
        """C_STS verified by two paths: direct formula vs bracket annihilation."""
        # Path 1: the explicit formula C_STS = xy + z^2/4 + z/2
        C_formula = x*y + z**2/4 + z/2
        # Path 2: verify {C, x_i} = 0 for each i
        for coord in [x, y, z]:
            assert expand(sklyanin_bracket(C_formula, coord)) == 0
        # Path 3: verify C_STS is the Casimir from the engine
        result = sklyanin_casimir()
        assert expand(result['casimir_sts'] - C_formula) == 0

    def test_jacobi_direct_vs_d_squared(self):
        """Jacobi by two paths: explicit cyclic sum vs delta_pi^2 = 0."""
        # Path 1: Jacobi on coordinate functions
        pi = sklyanin_bivector()
        jac = verify_jacobi_identity(pi)
        assert jac['satisfied']
        # Path 2: delta_pi^2 = 0 on coordinate functions
        d2 = verify_d_squared_zero_on_functions([x, y, z])
        assert d2['all_vanish']

    def test_unimodularity_direct_vs_summary(self):
        """Unimodularity by two paths: direct div(pi) and summary report."""
        # Path 1: direct divergence computation
        pi = sklyanin_bivector()
        coords_list = [x, y, z]
        for j in range(3):
            div_j = S.Zero
            for i in range(3):
                div_j += diff(pi[i, j], coords_list[i])
            assert expand(div_j) == 0
        # Path 2: from summary
        summary = full_poisson_cohomology_summary()
        assert summary['is_unimodular']

    def test_bracket_values_two_paths(self):
        """STS bracket values by two paths: bivector formula vs explicit table."""
        # Path 1: from sklyanin_bracket function
        b_xy = sklyanin_bracket(x, y)
        b_xz = sklyanin_bracket(x, z)
        b_yz = sklyanin_bracket(y, z)
        # Path 2: from explicit_bracket_table
        table = explicit_bracket_table()
        assert expand(b_xy - table[('x', 'y')]) == 0
        assert expand(b_xz - table[('x', 'z')]) == 0
        assert expand(b_yz - table[('y', 'z')]) == 0
        # Path 3: from bivector components directly
        bv = explicit_bivector_components()
        assert expand(b_xy - bv[(0, 1)]) == 0
        assert expand(b_xz - bv[(0, 2)]) == 0
        assert expand(b_yz - bv[(1, 2)]) == 0

    def test_h0_dimension_two_paths(self):
        """H^0 dimension by two paths: direct kernel vs Casimir powers."""
        # Path 1: kernel computation
        h0 = compute_h0_polynomial_degree(max_deg=4)
        # Path 2: count C_STS powers that fit in degree <= d
        # C_STS has degree 2, so C_STS^k has degree 2k
        # Expected cumulative Casimir dimension at degree d:
        #   d=0: 1 (const), d=1: 1, d=2: 2 (const + C), d=3: 2, d=4: 3 (const+C+C^2)
        expected = {0: 1, 1: 1, 2: 2, 3: 2, 4: 3}
        for d in range(5):
            assert h0['casimirs_by_degree'][d]['dim'] == expected[d], (
                f"H^0(deg<={d}): got {h0['casimirs_by_degree'][d]['dim']}, expected {expected[d]}")

    def test_bivector_lp_plus_r_equals_sts(self):
        """STS = LP + r verified component by component."""
        pi_lp = lie_poisson_bivector()
        r = r_matrix_correction()
        pi_sts = sklyanin_bivector()
        for i in range(3):
            for j in range(3):
                assert expand(pi_sts[i, j] - pi_lp[i, j] - r[i, j]) == 0

    def test_h1_vanishing_direct_vs_ce(self):
        """H^1 = 0 by two paths: direct and CE/Whitehead."""
        h1 = compute_h1_low_degree(max_deg=1)
        ce = ce_cohomology_sl2()
        for d in range(2):
            assert h1[d]['dim_h1'] == 0
        assert ce['h1_ce'] == 0
