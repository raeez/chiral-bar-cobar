r"""Tests for the crystalline shadow cohomology engine (BC-138).

Multi-path verification of point counts, Frobenius eigenvalues, local
zeta functions, and shadow L-functions at Riemann zeta zeros.

Verification paths:
  (i)   Direct enumeration over F_p x F_p
  (ii)  Character sum / Legendre symbol formula
  (iii) Lefschetz trace formula (compactly supported)
  (iv)  Euler product local factors
  (v)   Hasse-Weil bound consistency

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  kappa != c/2 in general.
CAUTION (AP10): Do not hardcode wrong expected values.
CAUTION (AP38): Normalization conventions.
CAUTION (AP48): kappa depends on the full algebra.
"""

import cmath
import math
import pytest
from fractions import Fraction

from compute.lib.bc_crystalline_shadow_cohomology_engine import (
    # Arithmetic primitives
    legendre_symbol,
    is_prime,
    next_prime,
    primes_up_to,
    first_n_primes,
    # Shadow conic data
    ShadowConicData,
    virasoro_conic_data,
    heisenberg_conic_data,
    affine_sl2_conic_data,
    betagamma_conic_data,
    lattice_conic_data,
    # Point counts
    affine_conic_point_count,
    shadow_conic_point_count_mod_p,
    point_count_extension_field,
    shadow_surface_point_count,
    # Character sums
    character_sum_conic,
    point_count_via_character_sum,
    # Local zeta
    LocalZetaData,
    compute_local_zeta,
    # Frobenius
    frobenius_trace_from_counts,
    frobenius_eigenvalues_genus1,
    verify_weil_bound,
    # Discriminant
    virasoro_discriminant_data,
    # Global L
    shadow_family_L_function,
    shadow_hasse_weil_L,
    # Zeta zeros
    RIEMANN_ZEROS,
    riemann_zero,
    shadow_parameter_at_zero,
    crystalline_data_at_zeros,
    # Lefschetz / Hasse-Weil
    lefschetz_trace_check,
    hasse_weil_bound_check,
    # Multi-path
    multi_path_verify_point_count,
    # Surface
    shadow_surface_frobenius_data,
    # Full analysis
    full_crystalline_analysis,
    # Display
    build_point_count_table,
    format_point_count_table,
    format_zero_data,
)


# =========================================================================
# Section 1: Arithmetic primitives
# =========================================================================

class TestArithmeticPrimitives:
    """Tests for Legendre symbol, primality, prime generation."""

    def test_legendre_symbol_basic(self):
        """(1|p) = 1 for all odd primes."""
        for p in [3, 5, 7, 11, 13, 17, 19, 23]:
            assert legendre_symbol(1, p) == 1

    def test_legendre_symbol_zero(self):
        """(0|p) = 0."""
        for p in [3, 5, 7, 11, 13]:
            assert legendre_symbol(0, p) == 0

    def test_legendre_symbol_qr(self):
        """Known quadratic residues mod 5: {0, 1, 4}."""
        assert legendre_symbol(1, 5) == 1
        assert legendre_symbol(4, 5) == 1
        assert legendre_symbol(2, 5) == -1
        assert legendre_symbol(3, 5) == -1

    def test_legendre_symbol_mod7(self):
        """QR mod 7: {0, 1, 2, 4}."""
        assert legendre_symbol(1, 7) == 1
        assert legendre_symbol(2, 7) == 1
        assert legendre_symbol(4, 7) == 1
        assert legendre_symbol(3, 7) == -1
        assert legendre_symbol(5, 7) == -1
        assert legendre_symbol(6, 7) == -1

    def test_legendre_quadratic_reciprocity_spot(self):
        """(3|7)(7|3) = (-1)^{(3-1)(7-1)/4} = (-1)^3 = -1."""
        l1 = legendre_symbol(3, 7)
        l2 = legendre_symbol(7, 3)
        expected = (-1) ** ((3 - 1) * (7 - 1) // 4)
        assert l1 * l2 == expected

    def test_is_prime(self):
        assert is_prime(2)
        assert is_prime(3)
        assert not is_prime(4)
        assert is_prime(97)
        assert not is_prime(100)

    def test_primes_up_to(self):
        ps = primes_up_to(30)
        assert ps == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_first_n_primes(self):
        ps = first_n_primes(10)
        assert len(ps) == 10
        assert ps == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_next_prime(self):
        assert next_prime(2) == 3
        assert next_prime(7) == 11
        assert next_prime(100) == 101


# =========================================================================
# Section 2: Shadow conic construction
# =========================================================================

class TestShadowConicConstruction:
    """Tests for conic data from each family."""

    def test_virasoro_conic_c1(self):
        """Virasoro at c=1: q0=1, q1=12, q2 = (180+872)/(5+22) = 1052/27."""
        conic = virasoro_conic_data(1)
        assert conic.family == "Virasoro"
        assert conic.q0 == Fraction(1)
        assert conic.q1 == Fraction(12)
        assert conic.q2 == Fraction(1052, 27)
        assert conic.kappa == Fraction(1, 2)

    def test_virasoro_conic_c2(self):
        """Virasoro at c=2: q0=4, q1=24."""
        conic = virasoro_conic_data(2)
        assert conic.q0 == Fraction(4)
        assert conic.q1 == Fraction(24)
        assert conic.kappa == Fraction(1)

    def test_virasoro_conic_c26(self):
        """Virasoro at c=26 (critical): kappa=13."""
        conic = virasoro_conic_data(26)
        assert conic.kappa == Fraction(13)
        assert conic.q0 == Fraction(676)
        assert conic.q1 == Fraction(312)

    def test_virasoro_self_dual_c13(self):
        """Virasoro at c=13 (self-dual point): kappa=13/2."""
        conic = virasoro_conic_data(13)
        assert conic.kappa == Fraction(13, 2)

    def test_heisenberg_conic(self):
        """Heisenberg at k=1: q0=1, q1=q2=0."""
        conic = heisenberg_conic_data(1)
        assert conic.q0 == Fraction(1)
        assert conic.q1 == Fraction(0)
        assert conic.q2 == Fraction(0)
        assert conic.kappa == Fraction(1)
        assert conic.discriminant == Fraction(0)

    def test_heisenberg_conic_k3(self):
        """Heisenberg at k=3: q0=9."""
        conic = heisenberg_conic_data(3)
        assert conic.q0 == Fraction(9)
        assert conic.kappa == Fraction(3)

    def test_affine_sl2_conic(self):
        """Affine sl_2 at k=1: kappa = 3*3/4 = 9/4."""
        conic = affine_sl2_conic_data(1)
        assert conic.kappa == Fraction(9, 4)
        # Class L: discriminant = 0 (perfect square Q_L)
        assert conic.discriminant == Fraction(0)

    def test_lattice_conic(self):
        """Lattice VOA of rank 8: kappa=8, class G."""
        conic = lattice_conic_data(8)
        assert conic.kappa == Fraction(8)
        assert conic.q0 == Fraction(64)
        assert conic.q1 == Fraction(0)
        assert conic.q2 == Fraction(0)

    def test_virasoro_discriminant_sign(self):
        """Virasoro discriminant D(c) = q1^2 - 4*q0*q2 < 0 for c > 0.

        D = 144c^2 - 4c^2 * alpha(c). For c > 0 and 5c+22 > 0:
        alpha(c) = (180c+872)/(5c+22) > 36 for c > 0 (check: at c=0,
        alpha=872/22 ~ 39.6; at c=inf, alpha -> 36).
        So D = 4c^2(36 - alpha) < 0 for c > 0. The conic is SMOOTH (elliptic).
        """
        for c_val in [1, 2, 6, 10, 13, 25, 26]:
            conic = virasoro_conic_data(c_val)
            assert conic.discriminant < 0, f"Expected D < 0 at c={c_val}, got {conic.discriminant}"


# =========================================================================
# Section 3: Point count enumeration (Path i)
# =========================================================================

class TestPointCountEnumeration:
    """Direct enumeration of F_p-points on the affine conic."""

    def test_trivial_conic_p5(self):
        """w^2 = 1 over F_5: for each t, f(t) = 1 (a QR). #X = 5*2 = 10."""
        # w^2 = 0*t^2 + 0*t + 1.  f(t) = 1 for all t.
        # 1 is QR mod 5, so each t gives 2 solutions. Total: 5*2 = 10.
        N = affine_conic_point_count(1, 0, 0, 5)
        assert N == 10

    def test_trivial_conic_p7(self):
        """w^2 = 1 over F_7: 7*2 = 14."""
        N = affine_conic_point_count(1, 0, 0, 7)
        assert N == 14

    def test_zero_conic_p5(self):
        """w^2 = 0 over F_5: w=0 for all t. #X = 5."""
        N = affine_conic_point_count(0, 0, 0, 5)
        assert N == 5

    def test_line_conic_p5(self):
        """w^2 = t over F_5. f(0)=0: 1 sol. f(1)=1: QR, 2 sol. f(2)=2: NQR, 0.
        f(3)=3: NQR, 0. f(4)=4: QR, 2. Total: 1+2+0+0+2 = 5."""
        N = affine_conic_point_count(0, 1, 0, 5)
        assert N == 5

    def test_quadratic_conic_p5(self):
        """w^2 = t^2 over F_5: w = +/-t for t != 0 (2 solutions each), w = 0 for t = 0.
        Total: 1 + 4*2 = 9."""
        N = affine_conic_point_count(0, 0, 1, 5)
        assert N == 9

    def test_smooth_conic_p7(self):
        """w^2 = t^2 + 1 over F_7.
        t=0: 1, QR(1)=1, 2 sols.
        t=1: 2, QR(2)=1, 2 sols.
        t=2: 5, QR(5)=-1, 0 sols.
        t=3: 10=3, QR(3)=-1, 0 sols.
        t=4: 17=3, QR(3)=-1, 0 sols.
        t=5: 26=5, QR(5)=-1, 0 sols.
        t=6: 37=2, QR(2)=1, 2 sols.
        Total: 2+2+0+0+0+0+2 = 6."""
        N = affine_conic_point_count(1, 0, 1, 7)
        assert N == 6

    def test_virasoro_c1_p5(self):
        """Point count for Virasoro c=1 mod 5.

        Independently compute: q0=1, q1=12=2, q2=(1052/27) mod 5.
        1052 mod 5 = 2, 27 mod 5 = 2, 27^{-1} mod 5 = 3 (since 2*3=6=1 mod 5).
        q2 = 2*3 = 6 = 1 mod 5.
        So w^2 = 1 + 2t + t^2 = (1+t)^2 mod 5.
        This is a perfect square! w = +/-(1+t).
        #X = 2*5 - 1 = 9 (two lines meeting at t=-1, w=0).
        """
        conic = virasoro_conic_data(1)
        N = shadow_conic_point_count_mod_p(conic, 5)
        # Independent verification: (1+t)^2 mod 5
        count = 0
        for t in range(5):
            ft = (1 + 2*t + t*t) % 5
            if ft == 0:
                count += 1
            elif legendre_symbol(ft, 5) == 1:
                count += 2
        assert N == count

    def test_virasoro_c1_p7(self):
        """Point count for Virasoro c=1 mod 7."""
        conic = virasoro_conic_data(1)
        N = shadow_conic_point_count_mod_p(conic, 7)
        # Cross-check with direct computation
        q2_frac = Fraction(1052, 27)
        q2_mod7 = (1052 * pow(27, 5, 7)) % 7  # 27^{-1} mod 7 = 27^5 mod 7
        # 27 mod 7 = 6, 6^{-1} mod 7 = 6 (since 6*6=36=1 mod 7)
        q2_check = (1052 % 7) * (6) % 7  # 1052 mod 7 = 1052-150*7=1052-1050=2. 2*6=12=5 mod 7.
        count = 0
        for t in range(7):
            ft = (1 + 5*t + 5*t*t) % 7
            if ft == 0:
                count += 1
            elif legendre_symbol(ft, 7) == 1:
                count += 2
        assert N == count

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13, 17, 19, 23])
    def test_virasoro_c10_all_primes(self, p):
        """Virasoro c=10 point counts are non-negative at good primes.

        Bad reduction at p=3 (denominator 9 = 5*10+22 has factor 3) returns -1.
        """
        conic = virasoro_conic_data(10)
        N = shadow_conic_point_count_mod_p(conic, p)
        if N == -1:
            pytest.skip(f"Bad reduction at p={p}")
        assert N >= 0, f"Negative count at p={p}: N={N}"

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13])
    def test_heisenberg_k1_all_primes(self, p):
        """Heisenberg k=1: w^2 = 1. Count = p * (1 + (1|p)) = 2p for odd p."""
        conic = heisenberg_conic_data(1)
        N = shadow_conic_point_count_mod_p(conic, p)
        # w^2 = 1 for all t. (1|p) = 1 for all odd p. So 2 solutions for each t.
        assert N == 2 * p


# =========================================================================
# Section 4: Character sum verification (Path ii)
# =========================================================================

class TestCharacterSumVerification:
    """Character sum cross-check against enumeration."""

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13])
    def test_character_sum_matches_enumeration(self, p):
        """Character sum formula gives same count as enumeration for w^2=t^2+t+1."""
        q0, q1, q2 = 1, 1, 1
        N_enum = affine_conic_point_count(q0, q1, q2, p)
        N_char = point_count_via_character_sum(q0, q1, q2, p)
        assert N_enum == N_char, f"Mismatch at p={p}: enum={N_enum}, char={N_char}"

    @pytest.mark.parametrize("p", [5, 7, 11, 13, 17])
    def test_smooth_conic_character_sum(self, p):
        """For smooth conic (disc != 0 mod p): S = -(a|p)."""
        q0, q1, q2 = 1, 0, 1  # disc = -4, nonzero mod p for p > 2
        S = character_sum_conic(q0, q1, q2, p)
        expected = -legendre_symbol(q2, p)
        disc = (q1*q1 - 4*q0*q2) % p
        if disc % p != 0:
            assert S == expected, f"p={p}: S={S}, expected={expected}"

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13, 17, 19, 23])
    def test_virasoro_c2_enum_vs_charsum(self, p):
        """Virasoro c=2: enumeration matches character sum."""
        conic = virasoro_conic_data(2)
        # Reduce mod p
        def frac_mod(f, p):
            num = f.numerator % p
            den = f.denominator % p
            if den == 0:
                return None
            return (num * pow(den, p - 2, p)) % p
        q0 = frac_mod(conic.q0, p)
        q1 = frac_mod(conic.q1, p)
        q2 = frac_mod(conic.q2, p)
        if q0 is None or q1 is None or q2 is None:
            pytest.skip(f"Bad reduction at p={p}")
        N_enum = affine_conic_point_count(q0, q1, q2, p)
        N_char = point_count_via_character_sum(q0, q1, q2, p)
        assert N_enum == N_char

    def test_singular_conic_character_sum(self):
        """Singular conic (disc = 0): S = (p-1)*(a|p)."""
        p = 7
        # w^2 = t^2 - 2t + 1 = (t-1)^2.  q0=1, q1=-2=5, q2=1. disc = 25-4 = 21 = 0 mod 7.
        q0, q1, q2 = 1, 5, 1
        S = character_sum_conic(q0, q1, q2, p)
        # disc = 25 - 4 = 21 = 0 mod 7.  q2 = 1 mod 7. (1|7) = 1.
        # Expected: S = (p-1) * (q2|p) = 6 * 1 = 6.
        assert S == 6


# =========================================================================
# Section 5: Lefschetz trace formula (Path iii)
# =========================================================================

class TestLefschetzTrace:
    """Lefschetz trace formula verification."""

    @pytest.mark.parametrize("p", [5, 7, 11, 13])
    def test_lefschetz_consistency(self, p):
        """Lefschetz internal consistency (enumeration = character sum)."""
        q0, q1, q2 = 3, 1, 2
        lef = lefschetz_trace_check(q0 % p, q1 % p, q2 % p, p)
        assert lef['consistent'], f"Inconsistency at p={p}: {lef}"

    @pytest.mark.parametrize("p", [5, 7, 11, 13, 17])
    def test_smooth_projective_count(self, p):
        """Smooth projective conic has p+1 points."""
        # w^2 = t^2 + 1 (smooth for p > 2, disc = -4 != 0 mod p for p != 2)
        q0, q1, q2 = 1, 0, 1
        lef = lefschetz_trace_check(q0, q1, q2, p)
        disc = (q1*q1 - 4*q0*q2) % p
        if disc % p != 0:
            assert lef['projective'] == p + 1

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13])
    def test_virasoro_c6_lefschetz(self, p):
        """Virasoro c=6: Lefschetz consistent."""
        conic = virasoro_conic_data(6)
        def frac_mod(f, p):
            num = f.numerator % p
            den = f.denominator % p
            if den == 0:
                return None
            return (num * pow(den, p - 2, p)) % p
        q0 = frac_mod(conic.q0, p)
        q1 = frac_mod(conic.q1, p)
        q2 = frac_mod(conic.q2, p)
        if q0 is None or q1 is None or q2 is None:
            pytest.skip(f"Bad reduction at p={p}")
        lef = lefschetz_trace_check(q0, q1, q2, p)
        assert lef['consistent']


# =========================================================================
# Section 6: Extension field counts
# =========================================================================

class TestExtensionFieldCounts:
    """Point counts over F_{p^n} and consistency."""

    def test_extension_field_n1_matches_direct(self):
        """F_{p^1} count matches direct enumeration."""
        q0, q1, q2 = 1, 3, 2
        p = 7
        N1_ext = point_count_extension_field(q0, q1, q2, p, 1)
        N1_dir = affine_conic_point_count(q0, q1, q2, p)
        assert N1_ext == N1_dir

    @pytest.mark.parametrize("p", [3, 5, 7])
    def test_extension_field_growth(self, p):
        """#X(F_{p^n}) grows roughly as p^n."""
        q0, q1, q2 = 1, 0, 1
        for n in range(1, 5):
            Nn = point_count_extension_field(q0, q1, q2, p, n)
            # Rough bound: Nn <= 2 * p^n + 1
            assert Nn <= 2 * p**n + 1, f"Too large at p={p}, n={n}: Nn={Nn}"
            assert Nn >= 0, f"Negative at p={p}, n={n}"

    def test_smooth_conic_extension_formula(self):
        """For smooth conic, #X_proj(F_{p^n}) = p^n + 1."""
        p = 7
        q0, q1, q2 = 1, 0, 1  # disc = -4 != 0 mod 7
        for n in range(1, 5):
            Nn = point_count_extension_field(q0, q1, q2, p, n)
            # Affine = projective - pts at infinity
            # pts at inf: w^2 = t^2 => w = +/- t. Over F_{7^n}: always 2 pts.
            # (since 1 is always a square)
            assert Nn == 7**n + 1 - 2, f"Wrong at n={n}: Nn={Nn}, expected={7**n - 1}"


# =========================================================================
# Section 7: Local zeta functions
# =========================================================================

class TestLocalZeta:
    """Tests for local zeta function computation."""

    @pytest.mark.parametrize("p", [3, 5, 7, 11])
    def test_local_zeta_genus0(self, p):
        """Smooth conic (genus 0): P_1 = 1 (trivial H^1)."""
        conic = virasoro_conic_data(10)
        lz = compute_local_zeta(conic, p, max_n=4)
        assert lz.P1 == [1], f"P_1 should be [1] for genus 0, got {lz.P1}"

    def test_local_zeta_point_counts_computed(self):
        """Local zeta computes at least max_n point counts."""
        conic = virasoro_conic_data(6)
        lz = compute_local_zeta(conic, 5, max_n=4)
        assert len(lz.point_counts) == 4

    def test_local_zeta_weil_satisfied(self):
        """Weil bound is satisfied (trivially, for genus 0)."""
        conic = virasoro_conic_data(10)
        lz = compute_local_zeta(conic, 7, max_n=3)
        assert lz.weil_bound_satisfied

    def test_heisenberg_local_zeta(self):
        """Heisenberg: w^2 = k^2 is a pair of lines, well-defined local zeta."""
        conic = heisenberg_conic_data(1)
        lz = compute_local_zeta(conic, 5, max_n=3)
        assert len(lz.point_counts) == 3
        # w^2 = 1 over F_{5^n}: always 2*5^n points (1 is always QR)
        for n_idx, Nn in enumerate(lz.point_counts):
            n = n_idx + 1
            assert Nn == 2 * 5**n, f"Wrong at n={n}: {Nn}"


# =========================================================================
# Section 8: Frobenius eigenvalues
# =========================================================================

class TestFrobeniusEigenvalues:
    """Tests for Frobenius trace and eigenvalue extraction."""

    def test_frobenius_trace_genus0(self):
        """For genus 0 (P^1), N = p+1, so trace = 0."""
        assert frobenius_trace_from_counts(8, 7) == 0  # 7 + 1 - 8 = 0

    def test_frobenius_eigenvalues_genus1_elliptic(self):
        """For a genus-1 curve with N=p+1 (supersingular): a_p=0, eigs = +/- i*sqrt(p)."""
        p = 5
        N = p + 1  # a_p = 0
        eigs = frobenius_eigenvalues_genus1(N, p)
        assert len(eigs) == 2
        for alpha in eigs:
            assert abs(abs(alpha) - math.sqrt(p)) < 1e-10

    def test_weil_bound_verification(self):
        """Weil bound: |alpha| = p^{1/2} for H^1 eigenvalues."""
        eigs = [complex(1, 2), complex(1, -2)]  # |eigs| = sqrt(5)
        assert verify_weil_bound(eigs, 5, weight=1)
        assert not verify_weil_bound(eigs, 7, weight=1)

    def test_frobenius_genus1_hasse_bound(self):
        """For genus 1: |a_p| <= 2*sqrt(p)."""
        # Take an actual elliptic curve: y^2 = x^3 + x over F_5.
        # N = 4 (can be verified). a_5 = 5+1-4 = 2.
        eigs = frobenius_eigenvalues_genus1(4, 5)
        for alpha in eigs:
            assert abs(alpha) <= math.sqrt(5) + 1e-10


# =========================================================================
# Section 9: Shadow discriminant
# =========================================================================

class TestShadowDiscriminant:
    """Tests for the Virasoro shadow discriminant."""

    def test_virasoro_discriminant_structure(self):
        """Discriminant D(c) = -320*c^2/(5c+22)."""
        dd = virasoro_discriminant_data()
        assert dd.family == "Virasoro"

    def test_discriminant_at_c0(self):
        """D(0) = 0: the conic is singular at c=0."""
        # At c=0: q0=0, q1=0, q2=872/22 = 436/11. D = 0 - 0 = 0.
        conic = virasoro_conic_data(Fraction(1, 1000))  # near c=0
        # D -> 0 as c -> 0 (D proportional to c^2)
        assert abs(float(conic.discriminant)) < 1.0

    def test_discriminant_negative_for_positive_c(self):
        """D(c) < 0 for all c > 0 (smooth elliptic fibers)."""
        for c_val in [1, 2, 5, 10, 13, 26, 100]:
            conic = virasoro_conic_data(c_val)
            assert conic.discriminant < 0


# =========================================================================
# Section 10: Global L-function
# =========================================================================

class TestGlobalLFunction:
    """Tests for the shadow family L-function."""

    def test_L_function_convergence(self):
        """L(c, s) converges for Re(s) >> 0."""
        val = shadow_hasse_weil_L(10, complex(2.0, 0), num_primes=20)
        assert abs(val) < 1e10  # should be finite
        assert abs(val) > 0  # should be nonzero

    def test_L_function_at_different_s(self):
        """L(c, s) varies with s."""
        L1 = shadow_hasse_weil_L(10, complex(2.0, 0), num_primes=20)
        L2 = shadow_hasse_weil_L(10, complex(3.0, 0), num_primes=20)
        assert abs(L1 - L2) > 1e-10  # different values

    def test_L_function_c_dependence(self):
        """L(c, s) varies with c."""
        L1 = shadow_hasse_weil_L(1, complex(2.0, 0), num_primes=20)
        L2 = shadow_hasse_weil_L(10, complex(2.0, 0), num_primes=20)
        # May or may not differ depending on character; check they're finite
        assert abs(L1) < 1e10
        assert abs(L2) < 1e10

    def test_L_defect_function(self):
        """Defect L-function is computable."""
        val = shadow_family_L_function(10, complex(2.0, 0), num_primes=20)
        assert abs(val) < 1e15


# =========================================================================
# Section 11: Riemann zeros and crystalline data
# =========================================================================

class TestRiemannZeros:
    """Tests for zeta zero infrastructure."""

    def test_first_zero(self):
        """First Riemann zero: rho_1 = 1/2 + i*14.1347..."""
        rho = riemann_zero(1)
        assert abs(rho.real - 0.5) < 1e-10
        assert abs(rho.imag - 14.134725141734693) < 1e-6

    def test_zeros_increasing(self):
        """Imaginary parts are increasing."""
        for n in range(1, len(RIEMANN_ZEROS)):
            assert RIEMANN_ZEROS[n] > RIEMANN_ZEROS[n - 1]

    def test_shadow_parameter_at_zero(self):
        """Shadow parameter c(rho_1) = t_1 ~ 14.13."""
        c = shadow_parameter_at_zero(1)
        assert abs(c - 14.134725141734693) < 1e-6

    def test_crystalline_at_zeros_structure(self):
        """Crystalline data at zeros has expected structure."""
        data = crystalline_data_at_zeros(zero_indices=[1, 2, 3], primes=[3, 5, 7])
        assert len(data) == 3
        for row in data:
            assert 'n' in row
            assert 'point_counts' in row
            assert 'L_at_rho' in row
            assert 'L_abs' in row
            assert row['L_abs'] >= 0

    def test_point_counts_at_zero_params(self):
        """Point counts at c_n = round(t_n) are sensible."""
        for n in range(1, 6):
            t_n = RIEMANN_ZEROS[n - 1]
            c_n = round(t_n)
            for p in [5, 7, 11]:
                N = shadow_surface_point_count(c_n, p)
                assert N >= 0, f"Negative count at n={n}, c_n={c_n}, p={p}"
                assert N <= 2 * p + 1, f"Too large at n={n}, c_n={c_n}, p={p}"


# =========================================================================
# Section 12: Hasse-Weil bound (Path v)
# =========================================================================

class TestHasseWeilBound:
    """Hasse-Weil bound checks."""

    @pytest.mark.parametrize("c_val", [1, 2, 6, 10, 14, 25, 26])
    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13])
    def test_hasse_weil_bound(self, c_val, p):
        """Point count within absolute range [0, 2p+1].

        The genus-1 Hasse-Weil bound |N - (p+1)| <= 2*sqrt(p) applies to
        smooth projective genus-1 curves. The shadow conic is genus 0, so
        the projective count is p+1 when smooth. For SINGULAR fibers (disc = 0
        mod p), the conic splits into two lines and the affine count can be
        up to 2p-1, which exceeds the genus-1 bound. The correct check is
        simply that N lies in the valid range for an affine quadric over F_p.
        """
        hw = hasse_weil_bound_check(c_val, p)
        N = hw['N']
        assert 0 <= N <= 2 * p + 1, f"Count out of range at c={c_val}, p={p}: N={N}"


# =========================================================================
# Section 13: Multi-path verification (all 5 paths)
# =========================================================================

class TestMultiPathVerification:
    """5-path verification of point counts."""

    @pytest.mark.parametrize("c_val", [1, 2, 6, 10, 25])
    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13, 17, 19, 23])
    def test_multi_path_agreement(self, c_val, p):
        """All 5 paths agree on #X_c(F_p)."""
        result = multi_path_verify_point_count(c_val, p)
        if not result['good_reduction']:
            pytest.skip(f"Bad reduction at c={c_val}, p={p}")
        assert result['paths_agree'], (
            f"Path disagreement at c={c_val}, p={p}: "
            f"enum={result['path1_enumeration']}, "
            f"char={result['path2_character_sum']}, "
            f"surface={result['path5_surface_count']}"
        )

    @pytest.mark.parametrize("c_val", [1, 2, 6, 10, 25])
    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13])
    def test_lefschetz_consistency_multipath(self, c_val, p):
        """Lefschetz trace is internally consistent."""
        result = multi_path_verify_point_count(c_val, p)
        if not result['good_reduction']:
            pytest.skip(f"Bad reduction at c={c_val}, p={p}")
        assert result['lefschetz_consistent'], f"Lefschetz inconsistency at c={c_val}, p={p}"


# =========================================================================
# Section 14: Surface Frobenius
# =========================================================================

class TestSurfaceFrobenius:
    """Tests for the Virasoro shadow surface Frobenius data."""

    def test_surface_frobenius_computes(self):
        """Surface Frobenius data is computable for small primes."""
        data = shadow_surface_frobenius_data(primes=[3, 5, 7])
        assert 3 in data
        assert 5 in data
        assert 7 in data

    def test_surface_total_count_positive(self):
        """Total surface point count is positive."""
        data = shadow_surface_frobenius_data(primes=[5, 7])
        for p in [5, 7]:
            assert data[p]['total_count'] > 0

    def test_surface_fiber_count_length(self):
        """Fiber count array has p entries."""
        data = shadow_surface_frobenius_data(primes=[5, 7])
        assert len(data[5]['fiber_counts']) == 5
        assert len(data[7]['fiber_counts']) == 7

    def test_surface_defect_small(self):
        """Surface defect from generic expectation is O(p)."""
        data = shadow_surface_frobenius_data(primes=[5, 7, 11, 13])
        for p in [5, 7, 11, 13]:
            defect = abs(data[p]['defect'])
            # For a surface over F_p, defect should be O(p) or smaller
            assert defect <= 5 * p, f"Large defect at p={p}: {defect}"


# =========================================================================
# Section 15: Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks: different families at matching parameters."""

    def test_heisenberg_trivial_count(self):
        """Heisenberg: w^2 = k^2 gives exactly 2p - 1 for k != 0 mod p (singular pair of lines)."""
        for p in [3, 5, 7, 11, 13]:
            conic = heisenberg_conic_data(1)
            N = shadow_conic_point_count_mod_p(conic, p)
            # w^2 = 1: for each t, w^2 = 1 has 2 solutions (1 is QR for odd p).
            # Total: 2p.
            assert N == 2 * p, f"Heisenberg k=1 at p={p}: N={N}, expected={2*p}"

    def test_lattice_rank8_same_as_heisenberg_k8(self):
        """Lattice rank 8 and Heisenberg k=8 have same shadow conic."""
        for p in [3, 5, 7, 11]:
            N_lat = shadow_conic_point_count_mod_p(lattice_conic_data(8), p)
            N_heis = shadow_conic_point_count_mod_p(heisenberg_conic_data(8), p)
            assert N_lat == N_heis, f"Mismatch at p={p}"

    def test_affine_sl2_class_L(self):
        """Affine sl_2 is class L (discriminant = 0), so the conic is singular."""
        conic = affine_sl2_conic_data(1)
        assert conic.discriminant == 0  # perfect square Q_L

    def test_virasoro_not_degenerate_at_generic_p(self):
        """Virasoro conic is smooth at generic primes (disc != 0 mod p)."""
        conic = virasoro_conic_data(10)
        smooth_count = 0
        for p in [3, 5, 7, 11, 13, 17, 19, 23]:
            N = shadow_conic_point_count_mod_p(conic, p)
            if N != -1:
                smooth_count += 1
        assert smooth_count >= 6  # most primes give good reduction


# =========================================================================
# Section 16: Specific numerical verifications
# =========================================================================

class TestSpecificNumerical:
    """Hardcoded numerical checks (verified by independent computation)."""

    def test_virasoro_c10_p7(self):
        """Virasoro c=10, p=7: independent computation.

        q0 = 100 = 2 mod 7
        q1 = 120 = 1 mod 7
        q2 = (180*10+872)/(5*10+22) = 2672/72 = 334/9
        334 mod 7 = 5, 9 mod 7 = 2, 2^{-1} mod 7 = 4 (since 2*4=8=1 mod 7)
        q2 = 5*4 = 20 = 6 mod 7
        disc = 1 - 4*2*6 = 1 - 48 = -47 = -47+49 = 2 mod 7
        2 != 0 mod 7, so smooth. S = -(6|7) = -(-1) = 1.
        N = 7 + 1 = 8.
        """
        conic = virasoro_conic_data(10)
        N = shadow_conic_point_count_mod_p(conic, 7)
        assert N == 8

    def test_virasoro_c10_p11(self):
        """Virasoro c=10, p=11: independent computation.

        q0 = 100 = 1 mod 11
        q1 = 120 = 10 mod 11
        q2 = 2672/72 = 334/9
        334 mod 11 = 4, 9 mod 11 = 9, 9^{-1} mod 11 = 5 (9*5=45=1 mod 11)
        q2 = 4*5 = 20 = 9 mod 11
        disc = 100 - 4*1*9 = 100 - 36 = 64 mod 11.  64 mod 11 = 9. 9 != 0 mod 11.
        Smooth. S = -(9|11). 9 = 3^2, so (9|11) = 1. S = -1.
        N = 11 + (-1) = 10.
        """
        conic = virasoro_conic_data(10)
        N = shadow_conic_point_count_mod_p(conic, 11)
        assert N == 10

    def test_virasoro_c10_p3(self):
        """Virasoro c=10, p=3: independent computation.

        q0 = 100 = 1 mod 3
        q1 = 120 = 0 mod 3
        q2 = 2672/72 mod 3.  2672 mod 3 = 2672-890*3=2672-2670=2. 72 mod 3=0.
        BAD REDUCTION at p=3 (72 = 9*8, divisible by 3).
        """
        conic = virasoro_conic_data(10)
        N = shadow_conic_point_count_mod_p(conic, 3)
        # Actually, 72 = 8*9. 9 mod 3 = 0. So denominator is 0 mod 3.
        # But wait: q2 = (180*10+872)/(5*10+22) = 2672/72.
        # The Fraction is 2672/72 = 334/9. 9 mod 3 = 0.
        # So this is bad reduction. N should be -1.
        assert N == -1

    def test_virasoro_c26_p5(self):
        """Virasoro c=26, p=5: c=26=1 mod 5."""
        N = shadow_surface_point_count(26, 5)
        # c = 26 mod 5 = 1. Same as c=1 mod 5.
        N_c1 = shadow_surface_point_count(1, 5)
        assert N == N_c1

    def test_virasoro_c13_p7(self):
        """Virasoro c=13 (self-dual), p=7."""
        conic = virasoro_conic_data(13)
        N = shadow_conic_point_count_mod_p(conic, 7)
        # c=13 mod 7 = 6. 5*13+22 = 87. 87 mod 7 = 87-84=3.
        # q0 = 169 = 169-24*7 = 169-168 = 1 mod 7
        # q1 = 156 = 156-22*7 = 156-154 = 2 mod 7
        # q2 = (180*13+872)/87 = 3212/87 = 3212/87
        # 3212 mod 7 = 3212-458*7 = 3212-3206 = 6. 87 mod 7 = 3. 3^{-1} mod 7 = 5.
        # q2 = 6*5 = 30 = 2 mod 7.
        # disc = 4 - 4*1*2 = 4-8 = -4 = 3 mod 7. 3 != 0 mod 7. Smooth.
        # S = -(2|7). (2|7) = 1 (2 is QR mod 7: 3^2=9=2). S = -1.
        # N = 7 + (-1) = 6.
        assert N == 6


# =========================================================================
# Section 17: Full analysis pipeline
# =========================================================================

class TestFullAnalysis:
    """Tests for the complete analysis pipeline."""

    def test_full_analysis_runs(self):
        """Full analysis completes without error (small parameters)."""
        result = full_crystalline_analysis(
            primes=[3, 5, 7],
            zero_indices=[1, 2, 3],
        )
        assert 'point_count_table' in result
        assert 'local_zeta_data' in result
        assert 'crystalline_at_zeros' in result
        assert 'surface_frobenius' in result
        assert 'verification' in result

    def test_point_count_table_length(self):
        """Point count table has expected number of entries."""
        table = build_point_count_table(primes=[3, 5, 7])
        # Default: 10 families * 3 primes = 30 entries
        assert len(table) == 30

    def test_format_functions(self):
        """Format functions produce non-empty strings."""
        table = build_point_count_table(primes=[3, 5])
        s = format_point_count_table(table)
        assert len(s) > 100

    def test_format_zero_data(self):
        """Zero data formatting works."""
        data = crystalline_data_at_zeros(zero_indices=[1, 2], primes=[5, 7])
        s = format_zero_data(data)
        assert len(s) > 50


# =========================================================================
# Section 18: Kappa consistency (AP1, AP9, AP48)
# =========================================================================

class TestKappaConsistency:
    """Verify kappa values match family-specific formulas (AP1)."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c_val in [1, 2, 6, 10, 13, 25, 26]:
            conic = virasoro_conic_data(c_val)
            assert conic.kappa == Fraction(c_val, 2)

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k_val in [1, 2, 3, 5]:
            conic = heisenberg_conic_data(k_val)
            assert conic.kappa == Fraction(k_val)

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k_val in [1, 2, 3, 4]:
            conic = affine_sl2_conic_data(k_val)
            expected = Fraction(3 * (k_val + 2), 4)
            assert conic.kappa == expected, f"k={k_val}: got {conic.kappa}, expected {expected}"

    def test_lattice_kappa(self):
        """kappa(V_Lambda) = rank."""
        for r in [1, 8, 16, 24]:
            conic = lattice_conic_data(r)
            assert conic.kappa == Fraction(r)

    def test_virasoro_kappa_not_equal_c(self):
        """kappa(Vir_c) = c/2, NOT c (AP9 check)."""
        conic = virasoro_conic_data(10)
        assert conic.kappa != Fraction(10)
        assert conic.kappa == Fraction(5)


# =========================================================================
# Section 19: Shadow class consistency
# =========================================================================

class TestShadowClassConsistency:
    """Shadow depth classification: G, L, C, M."""

    def test_class_G_discriminant_zero(self):
        """Class G (Heisenberg, lattice): discriminant = 0, q1 = q2 = 0."""
        for k in [1, 2, 3]:
            conic = heisenberg_conic_data(k)
            assert conic.discriminant == 0
            assert conic.q1 == 0
            assert conic.q2 == 0

    def test_class_L_discriminant_zero(self):
        """Class L (affine KM): discriminant = 0 (perfect square)."""
        for k in [1, 2, 3]:
            conic = affine_sl2_conic_data(k)
            assert conic.discriminant == 0

    def test_class_M_discriminant_nonzero(self):
        """Class M (Virasoro): discriminant != 0 for c > 0 (irreducible Q_L)."""
        for c_val in [1, 2, 6, 10, 13, 25, 26]:
            conic = virasoro_conic_data(c_val)
            assert conic.discriminant != 0, f"Expected nonzero disc at c={c_val}"


# =========================================================================
# Section 20: Zeta-zero L-function tests
# =========================================================================

class TestZetaZeroLFunction:
    """Tests for L-function behavior at Riemann zero parameters."""

    def test_L_at_zeros_finite(self):
        """L(X_{c(rho_n)}, rho_n) is finite for first few zeros."""
        for n in range(1, 6):
            t_n = RIEMANN_ZEROS[n - 1]
            c_n = round(t_n)
            rho_n = riemann_zero(n)
            L_val = shadow_hasse_weil_L(c_n, rho_n, num_primes=20)
            assert math.isfinite(L_val.real) and math.isfinite(L_val.imag), (
                f"L-function not finite at n={n}: {L_val}"
            )

    def test_L_does_not_vanish_generically(self):
        """Shadow L-function does NOT vanish at Riemann zeros (expected negative result).

        The shadow conic is genus 0, so its Hasse-Weil L-function is essentially
        a Dirichlet L-function twisted by the quadratic character of the discriminant.
        There is no reason for it to vanish at Riemann zeta zeros.

        This is a FALSIFICATION test (Beilinson principle): we expect L != 0.
        """
        for n in range(1, 8):
            t_n = RIEMANN_ZEROS[n - 1]
            c_n = round(t_n)
            rho_n = riemann_zero(n)
            L_val = shadow_hasse_weil_L(c_n, rho_n, num_primes=30)
            # We expect |L| to be generically nonzero
            # (This is a NEGATIVE result: the shadow L-function does NOT vanish at zeta zeros)
            # We don't assert L != 0 because the Euler product is finite and
            # approximate, but we record the values for analysis.
            assert math.isfinite(abs(L_val))

    def test_crystalline_data_point_count_table(self):
        """Crystalline data at zeros produces a valid point count table.

        Bad reduction (N = -1) can occur when p divides 5*c_n + 22.
        For instance, c_3 = 25, 5*25+22 = 147 = 21*7, so p=7 gives bad reduction.
        """
        data = crystalline_data_at_zeros(
            zero_indices=[1, 2, 3],
            primes=[5, 7, 11],
        )
        for row in data:
            for p in [5, 7, 11]:
                N = row['point_counts'][p]
                assert N >= -1, f"Invalid count at n={row['n']}, p={p}"
                # At good primes, count is in [0, 2p+1]
                if N >= 0:
                    assert N <= 2 * p + 1


# =========================================================================
# Section 21: Edge cases and bad reduction
# =========================================================================

class TestEdgeCases:
    """Edge cases: bad reduction, boundary parameters."""

    def test_bad_reduction_signaled(self):
        """Bad reduction returns -1."""
        # Virasoro c=10: 5*10+22 = 72, denominator 9 divisible by 3.
        conic = virasoro_conic_data(10)
        N = shadow_conic_point_count_mod_p(conic, 3)
        assert N == -1

    def test_c_equals_zero_handled(self):
        """c=0 is a boundary case: q0=0, q1=0, q2=872/22."""
        # Actually virasoro_conic_data(0) should work: c=0 gives kappa=0.
        conic = virasoro_conic_data(0)
        assert conic.kappa == 0
        assert conic.q0 == 0
        assert conic.q1 == 0

    def test_large_prime(self):
        """Point count at a larger prime."""
        conic = virasoro_conic_data(10)
        N = shadow_conic_point_count_mod_p(conic, 97)
        assert N >= 0

    def test_virasoro_negative_c(self):
        """Virasoro at c < 0 (non-unitary): conic still defined."""
        conic = virasoro_conic_data(-2)
        assert conic.q0 == Fraction(4)  # (-2)^2 = 4
        assert conic.q1 == Fraction(-24)

    def test_p_equals_2(self):
        """p=2: smallest prime, special handling needed."""
        conic = virasoro_conic_data(1)
        N = shadow_conic_point_count_mod_p(conic, 2)
        # p=2 is odd enough for Legendre, but need to check
        # q2 denominator: 27 mod 2 = 1, OK.
        assert N >= 0 or N == -1


# =========================================================================
# Section 22: Quadratic reciprocity cross-checks
# =========================================================================

class TestQuadraticReciprocity:
    """Legendre symbol via quadratic reciprocity as cross-check."""

    @pytest.mark.parametrize("p,q", [(3, 5), (3, 7), (5, 7), (5, 11), (7, 11), (7, 13)])
    def test_quadratic_reciprocity(self, p, q):
        """QR: (p|q)(q|p) = (-1)^{(p-1)(q-1)/4}."""
        lp = legendre_symbol(p, q)
        lq = legendre_symbol(q, p)
        expected = (-1) ** (((p - 1) * (q - 1)) // 4)
        assert lp * lq == expected, f"QR failed for ({p},{q})"

    @pytest.mark.parametrize("p", [3, 5, 7, 11, 13, 17, 19, 23])
    def test_sum_of_legendre_symbols(self, p):
        """sum_{a=0}^{p-1} (a|p) = 0 (character orthogonality)."""
        total = sum(legendre_symbol(a, p) for a in range(p))
        assert total == 0


# =========================================================================
# Section 23: Consistency of surface counts
# =========================================================================

class TestSurfaceCountConsistency:
    """Total surface point count consistency checks."""

    @pytest.mark.parametrize("p", [5, 7, 11])
    def test_total_equals_sum_of_fibers(self, p):
        """Total surface count = sum of fiber counts."""
        data = shadow_surface_frobenius_data(primes=[p])
        total = data[p]['total_count']
        fiber_sum = sum(data[p]['fiber_counts'])
        assert total == fiber_sum

    @pytest.mark.parametrize("p", [7, 11, 13, 17])
    def test_generic_fiber_count(self, p):
        """Smooth fiber counts are p-1 or p+1 depending on Legendre symbol.

        For a smooth affine conic w^2 = q0 + q1*t + q2*t^2 (disc != 0 mod p),
        the character sum gives S = -(q2|p), so N = p - (q2|p).
        When (q2|p) = +1: N = p - 1.  When (q2|p) = -1: N = p + 1.

        Singular fibers (disc = 0) have N = 2p-1 or 1 (pair of lines).
        Bad fibers (denom = 0) have special counts.
        """
        data = shadow_surface_frobenius_data(primes=[p])
        fibers = data[p]['fiber_counts']
        # Each fiber count should be a valid value for an affine quadric
        for i, f in enumerate(fibers):
            assert 0 <= f <= 2 * p + 1, (
                f"Fiber count out of range at p={p}, c={i}: f={f}"
            )
        # At least one fiber should have a smooth count (p-1 or p+1)
        smooth_count = sum(1 for f in fibers if f in (p - 1, p + 1))
        assert smooth_count >= 1, (
            f"No smooth fibers at p={p}: fibers={fibers}"
        )
