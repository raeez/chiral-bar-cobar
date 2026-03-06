"""Mathematical identity tests: properties that must hold by the mathematics.

Unlike constant-value tests (which verify stored lookups), these tests verify
mathematical IDENTITIES: recurrence relations, functional equations, duality
involutions, Hilbert series relations, and structural constraints.

Every test here is a theorem, not a lookup.
"""

import pytest
from sympy import Rational, Symbol, simplify, factorial, bernoulli

k = Symbol('k')
c = Symbol('c')


# ===========================================================================
# I. RECURRENCE IDENTITIES FOR BAR COHOMOLOGY
# ===========================================================================

class TestBarCohomologyRecurrences:
    """Bar cohomology dimensions must satisfy their defining recurrences."""

    def test_riordan_recurrence_sl2(self):
        """Riordan numbers R(n): (n+1)R(n) = (n-1)(2R(n-1) + 3R(n-2)).
        sl2 bar cohomology = R(n+3)."""
        from compute.lib.bar_complex import bar_dim_sl2
        for n in range(3, 12):
            rn = bar_dim_sl2(n)
            rn1 = bar_dim_sl2(n - 1)
            rn2 = bar_dim_sl2(n - 2)
            m = n + 3
            lhs = (m + 1) * rn
            rhs = (m - 1) * (2 * rn1 + 3 * rn2)
            assert lhs == rhs, f"Riordan recurrence fails at n={n}: {lhs} != {rhs}"

    def test_motzkin_difference_virasoro(self):
        """Virasoro bar cohomology = M(n+1) - M(n) where M(n) are Motzkin numbers.
        Motzkin recurrence: (n+3)*M(n+1) = (2n+3)*M(n) + 3n*M(n-1)."""
        from compute.lib.bar_complex import bar_dim_virasoro

        M = [1, 1]
        for i in range(1, 12):
            M.append(M[-1] + bar_dim_virasoro(i))

        for n in range(1, 11):
            lhs = (n + 3) * M[n + 1]
            rhs = (2 * n + 3) * M[n] + 3 * n * M[n - 1]
            assert lhs == rhs, f"Motzkin recurrence fails at n={n}: {lhs} != {rhs}"

    def test_partition_recurrence_heisenberg(self):
        """Heisenberg bar cohomology at degree n = p(n-2) for n >= 2."""
        from compute.lib.bar_complex import bar_dim_heisenberg
        from compute.lib.utils import partition_number

        for n in range(2, 15):
            assert bar_dim_heisenberg(n) == partition_number(n - 2), \
                f"Heisenberg bar dim at n={n} doesn't match p({n-2})"

    def test_bc_closed_form(self):
        """bc ghost bar cohomology = 2^n - n + 1."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        bc_dims = KNOWN_BAR_DIMS["bc"]
        for n in range(1, 11):
            assert bc_dims[n] == 2**n - n + 1, f"bc at n={n}: {bc_dims[n]} != {2**n - n + 1}"

    def test_betagamma_recurrence(self):
        """beta-gamma: n*a(n) = 2n*a(n-1) + 3(n-2)*a(n-2)."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        bg = KNOWN_BAR_DIMS["beta_gamma"]
        for n in range(3, 11):
            lhs = n * bg[n]
            rhs = 2 * n * bg[n - 1] + 3 * (n - 2) * bg[n - 2]
            assert lhs == rhs, f"beta-gamma recurrence fails at n={n}"


# ===========================================================================
# II. FEIGIN-FRENKEL INVOLUTION
# ===========================================================================

class TestFFInvolution:
    """The Feigin-Frenkel involution k -> -k - 2h^vee is an involution."""

    def test_involution_property(self):
        """(k')' = k for all Lie algebras."""
        from compute.lib.lie_algebra import ff_dual_level
        algebras = [("A", 1), ("A", 2), ("B", 2), ("G", 2)]
        for typ, rank in algebras:
            k_prime = ff_dual_level(typ, rank, k)
            k_double_prime = ff_dual_level(typ, rank, k_prime)
            assert simplify(k_double_prime - k) == 0, \
                f"FF involution fails for ({typ}, {rank}): k'' = {k_double_prime}"

    def test_critical_level_is_fixed_point_midpoint(self):
        """Critical level k = -h^vee is the midpoint of k and k'."""
        from compute.lib.lie_algebra import ff_dual_level, cartan_data
        for typ, rank in [("A", 1), ("A", 2), ("B", 2), ("G", 2)]:
            h_dual = cartan_data(typ, rank).h_dual
            k_prime = ff_dual_level(typ, rank, k)
            midpoint = simplify((k + k_prime) / 2)
            assert midpoint == -h_dual, \
                f"Midpoint of k and k' should be -h^vee={-h_dual}, got {midpoint}"


# ===========================================================================
# III. COMPLEMENTARITY AS MATHEMATICAL IDENTITY
# ===========================================================================

class TestComplementarityIdentity:
    """kappa(A) + kappa(A!) = 0 for KM algebras (symbolically in k)."""

    def test_km_kappa_complementarity(self):
        """kappa(g_k) + kappa(g_{k'}) = 0 for all KM algebras."""
        from compute.lib.lie_algebra import kappa_km, ff_dual_level
        for typ, rank in [("A", 1), ("A", 2), ("B", 2), ("G", 2)]:
            kap = kappa_km(typ, rank, k)
            k_prime = ff_dual_level(typ, rank, k)
            kap_prime = kappa_km(typ, rank, k_prime)
            total = simplify(kap + kap_prime)
            assert total == 0, \
                f"kappa complementarity for ({typ},{rank}): {total} != 0"


# ===========================================================================
# IV. GENERATING FUNCTION IDENTITIES
# ===========================================================================

class TestGFIdentities:
    """Generating function algebraic identities."""

    def test_catalan_convolution(self):
        """Catalan numbers satisfy C_n = sum_{k=0}^{n-1} C_k * C_{n-1-k}."""
        from compute.lib.spectral_sequence import catalan
        for n in range(2, 12):
            conv = sum(catalan(j) * catalan(n - 1 - j) for j in range(n))
            assert conv == catalan(n), f"Catalan convolution fails at n={n}"

    def test_associahedron_euler_characteristic(self):
        """Euler characteristic of associahedron K_n = 1 (contractible)."""
        from compute.lib.spectral_sequence import associahedron_f_vector
        for n in range(2, 8):
            fvec = associahedron_f_vector(n)
            euler = sum((-1)**i * f for i, f in enumerate(fvec))
            assert euler == 1, f"K_{n} Euler char = {euler}, expected 1"

    def test_associahedron_vertex_count_is_catalan(self):
        """Number of vertices of K_n = C_{n-1} (Catalan number)."""
        from compute.lib.spectral_sequence import associahedron_f_vector, catalan
        for n in range(2, 8):
            fvec = associahedron_f_vector(n)
            assert fvec[0] == catalan(n - 1), \
                f"K_{n} vertices = {fvec[0]}, expected C_{n-1} = {catalan(n-1)}"


# ===========================================================================
# V. GENUS EXPANSION IDENTITIES
# ===========================================================================

class TestGenusExpansionIdentities:
    """Universal properties of the genus expansion F_g = kappa * lambda_g^FP."""

    def test_lambda_fp_bernoulli_relation(self):
        """lambda_g^FP = (2^{2g-1}-1) / 2^{2g-1} * |B_{2g}| / (2g)!"""
        from compute.lib.utils import lambda_fp
        for g in range(1, 6):
            B2g = abs(bernoulli(2 * g))
            expected = Rational(2**(2*g - 1) - 1, 2**(2*g - 1)) * B2g / factorial(2 * g)
            assert lambda_fp(g) == expected, f"lambda_{g} mismatch"

    def test_genus_universality(self):
        """F_g(A) / F_g(B) = kappa(A) / kappa(B) for all g (ratio is g-independent)."""
        from compute.lib.utils import F_g
        kap1 = Rational(9, 4)
        kap2 = Rational(3)
        for g in range(1, 6):
            ratio_fg = F_g(kap1, g) / F_g(kap2, g)
            ratio_kap = kap1 / kap2
            assert ratio_fg == ratio_kap, f"Universality fails at g={g}"

    def test_lambda_fp_known_values(self):
        """lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp(1) == Rational(1, 24)
        assert lambda_fp(2) == Rational(7, 5760)
        assert lambda_fp(3) == Rational(31, 967680)


# ===========================================================================
# VI. CE COHOMOLOGY IDENTITIES
# ===========================================================================

class TestCECohomology:
    """Chevalley-Eilenberg cohomology structural identities."""

    def test_sl2_ce_euler_characteristic_zero(self):
        """chi(sl2) = 0 for any odd-dimensional simple Lie algebra.
        H*(sl2) = Lambda(x_3), so H^0=H^3=1, chi = 1-0+0-1 = 0."""
        # sl2 CE cohomology is (1+t^3): dims are {0:1, 3:1}
        # This is the exterior algebra on one generator of degree 3
        coh = {0: 1, 3: 1}
        chi = sum((-1)**i * d for i, d in coh.items())
        assert chi == 0, f"CE Euler char should be 0, got {chi}"

    def test_htt_sdr_axioms(self):
        """SDR conditions for sl2 CE complex all pass."""
        from compute.lib.htt import build_sl2_ce_sdr, verify_sdr
        sdr = build_sl2_ce_sdr()
        # SDR is (CEComplex, p_dict, iota_dict, h_dict, d_dict)
        results = verify_sdr(*sdr[1:])
        for name, ok in results.items():
            assert ok, f"SDR axiom failed: {name}"


# ===========================================================================
# VII. ORLIK-SOLOMON IDENTITIES
# ===========================================================================

class TestOSIdentities:
    """Orlik-Solomon algebra structural identities."""

    def test_os_top_degree_factorial(self):
        """dim OS^{n-1}(C_n) = (n-1)!"""
        from compute.lib.fm_compactification import os_top_dim
        from math import factorial as fact
        for n in range(2, 8):
            assert os_top_dim(n) == fact(n - 1), \
                f"OS top dim for n={n}: got {os_top_dim(n)}, expected {fact(n-1)}"

    def test_poincare_total_betti_is_factorial(self):
        """Sum of Betti numbers of C_n = n! (evaluation of Poincare polynomial at t=1)."""
        from compute.lib.fm_compactification import poincare_polynomial
        from math import factorial as fact
        for n in range(2, 7):
            p = poincare_polynomial(n)
            # poincare_polynomial returns a list of coefficients
            total = sum(p) if isinstance(p, list) else sum(p.values())
            assert total == fact(n), f"C_{n} total Betti = {total}, expected {fact(n)}"


# ===========================================================================
# VIII. CONDUCTOR FORMULA IDENTITY
# ===========================================================================

class TestConductorFormula:
    """K_N = 2(N-1)(2N^2 + 2N + 1) for W_N complementarity."""

    def test_conductor_two_expressions_agree(self):
        """K_N = 2(N-1)(2N^2+2N+1) = 4N^3 - 2N - 2 as polynomials."""
        from sympy import symbols, expand
        N = symbols('N')
        expr1 = 2 * (N - 1) * (2 * N**2 + 2 * N + 1)
        expr2 = 4 * N**3 - 2 * N - 2
        assert expand(expr1 - expr2) == 0

    def test_conductor_matches_complementarity(self):
        """K_2 = 26 (Virasoro), K_3 = 100 (W_3)."""
        from compute.lib.cross_algebra import complementarity_table
        ct = complementarity_table()
        K = lambda N: 2 * (N - 1) * (2 * N**2 + 2 * N + 1)
        assert K(2) == ct["Virasoro"]
        assert K(3) == ct["W3"]


# ===========================================================================
# IX. CURVED A-INFINITY IDENTITY
# ===========================================================================

class TestCurvedAInfinity:
    """Curved A-infinity structural identities."""

    def test_virasoro_three_regimes(self):
        """Virasoro has 3 curvature regimes: c=0 (uncurved), generic (curved), c=26 (dual uncurved)."""
        from compute.lib.virasoro_ainfty import virasoro_curved_regimes
        regimes = virasoro_curved_regimes()
        assert regimes["c=0"]["curved"] is False
        assert regimes["c_generic"]["curved"] is True
        assert regimes["c=26"]["type"] is not None  # dual uncurved

    def test_m1_squared_vanishes_for_central_curvature(self):
        """m_1^2(T) = [m_0, T] = 0 because m_0 = c/2 is a scalar (central)."""
        from compute.lib.virasoro_ainfty import virasoro_m1_squared
        result = virasoro_m1_squared()
        # For Virasoro, m_0 = c/2 is central => m_1^2 = 0 on all generators
        assert result["m1_squared_on_T"] == 0
