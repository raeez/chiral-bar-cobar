"""Tests for the Feigin-Frenkel channel shear matrix.

Verifies the channel decomposition of the modular characteristic
kappa = kappa_dp + kappa_sp and its transformation under FF duality
k -> -k - 2h^vee, as proved in Proposition prop:ff-channel-shear
(kac_moody_framework.tex).

For affine KM algebra g-hat_k:
  kappa_dp = k * dim(g) / (2 * h^vee)      (double-pole / level)
  kappa_sp = dim(g) / 2                     (simple-pole / structure)
  kappa    = (k + h^vee) * dim(g) / (2 * h^vee)

Shear matrix under k -> -k - 2h^vee:
  (kappa_dp', kappa_sp') = ((-1, -2), (0, 1)) * (kappa_dp, kappa_sp)

For W_N algebras:
  kappa(W_N) = c * sum_{s=2}^N 1/s = c * (H_N - 1)
  where H_N = sum_{j=1}^N 1/j is the N-th harmonic number.
"""

import pytest
from sympy import Rational, Symbol, Matrix, simplify, sympify, log, N as neval

from compute.lib.lie_algebra import cartan_data, ff_dual_level, kappa_km

k = Symbol('k')


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def kappa_dp(dim_g, h_dual, level):
    """Double-pole channel: kappa_dp = k * dim(g) / (2 * h^vee)."""
    return sympify(level) * Rational(dim_g) / (2 * Rational(h_dual))


def kappa_sp(dim_g):
    """Simple-pole channel: kappa_sp = dim(g) / 2."""
    return Rational(dim_g, 2)


def harmonic_number(n):
    """H_n = sum_{j=1}^n 1/j."""
    return sum(Rational(1, j) for j in range(1, n + 1))


def shear_matrix():
    """The FF shear matrix acting on (kappa_dp, kappa_sp)."""
    return Matrix([[-1, -2], [0, 1]])


# ---------------------------------------------------------------------------
# Lie algebra data for tests
# ---------------------------------------------------------------------------

ALGEBRAS = [
    # (type, rank, dim, h_dual, name)
    ("A", 1, 3, 2, "sl_2"),
    ("A", 2, 8, 3, "sl_3"),
    ("B", 2, 10, 3, "sp_4"),     # B_2 = C_2 = sp_4, h_dual = 3
    ("G", 2, 14, 4, "g_2"),
]

TEST_LEVELS = [1, 2, 3, 5, 10, Rational(1, 2), Rational(-1, 3)]


# ===========================================================================
# I. CHANNEL DECOMPOSITION AND SUMMATION
# ===========================================================================

class TestChannelDecomposition:
    """kappa_dp + kappa_sp = kappa = dim(g) * (k + h^vee) / (2 * h^vee)."""

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_channel_sum_symbolic(self, typ, rank, dim_g, h_dual, name):
        """kappa_dp(k) + kappa_sp = kappa(k) symbolically."""
        dp = kappa_dp(dim_g, h_dual, k)
        sp = kappa_sp(dim_g)
        total = simplify(dp + sp)
        expected = kappa_km(typ, rank, k)
        assert simplify(total - expected) == 0, \
            f"{name}: kappa_dp + kappa_sp = {total} != kappa = {expected}"

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_channel_sum_numeric(self, typ, rank, dim_g, h_dual, name):
        """kappa_dp + kappa_sp = kappa at specific integer levels."""
        for lev in TEST_LEVELS:
            dp = kappa_dp(dim_g, h_dual, lev)
            sp = kappa_sp(dim_g)
            total = dp + sp
            expected = Rational(dim_g) * (Rational(lev) + h_dual) / (2 * h_dual)
            assert total == expected, \
                f"{name} at k={lev}: {total} != {expected}"

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_cartan_data_consistency(self, typ, rank, dim_g, h_dual, name):
        """Verify our test parameters match the Lie algebra module."""
        data = cartan_data(typ, rank)
        assert data.dim == dim_g, f"{name}: dim mismatch"
        assert data.h_dual == h_dual, f"{name}: h_dual mismatch"


# ===========================================================================
# II. SHEAR MATRIX VERIFICATION
# ===========================================================================

class TestShearMatrix:
    """Under k -> -k - 2h^vee: kappa_dp' = -kappa_dp - 2*kappa_sp, kappa_sp' = kappa_sp."""

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_shear_symbolic(self, typ, rank, dim_g, h_dual, name):
        """Verify shear matrix identity symbolically."""
        dp = kappa_dp(dim_g, h_dual, k)
        sp = kappa_sp(dim_g)

        # FF dual level
        k_prime = -k - 2 * h_dual
        dp_prime = kappa_dp(dim_g, h_dual, k_prime)
        sp_prime = kappa_sp(dim_g)  # independent of level

        # Shear matrix prediction
        dp_predicted = -dp - 2 * sp
        sp_predicted = sp

        assert simplify(dp_prime - dp_predicted) == 0, \
            f"{name}: kappa_dp' = {dp_prime} != -kappa_dp - 2*kappa_sp = {dp_predicted}"
        assert simplify(sp_prime - sp_predicted) == 0, \
            f"{name}: kappa_sp' = {sp_prime} != kappa_sp = {sp_predicted}"

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_shear_numeric(self, typ, rank, dim_g, h_dual, name):
        """Verify shear at specific levels."""
        for lev in TEST_LEVELS:
            dp = kappa_dp(dim_g, h_dual, lev)
            sp = kappa_sp(dim_g)
            v = Matrix([dp, sp])

            S = shear_matrix()
            v_prime = S * v

            # Direct computation at dual level
            lev_prime = -lev - 2 * h_dual
            dp_direct = kappa_dp(dim_g, h_dual, lev_prime)
            sp_direct = kappa_sp(dim_g)

            assert v_prime[0] == dp_direct, \
                f"{name} at k={lev}: shear kappa_dp' = {v_prime[0]} != direct = {dp_direct}"
            assert v_prime[1] == sp_direct, \
                f"{name} at k={lev}: shear kappa_sp' = {v_prime[1]} != direct = {sp_direct}"

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_shear_matrix_form(self, typ, rank, dim_g, h_dual, name):
        """The matrix ((−1,−2),(0,1)) applied to (kappa_dp, kappa_sp)^T
        gives the correct dual channel vector."""
        S = shear_matrix()
        dp = kappa_dp(dim_g, h_dual, k)
        sp = kappa_sp(dim_g)
        v = Matrix([dp, sp])
        result = S * v

        # The dual level
        k_prime = -k - 2 * h_dual
        dp_expected = kappa_dp(dim_g, h_dual, k_prime)
        sp_expected = sp  # level-independent

        assert simplify(result[0] - dp_expected) == 0
        assert simplify(result[1] - sp_expected) == 0


# ===========================================================================
# III. ANTI-SYMMETRY OF TOTAL KAPPA
# ===========================================================================

class TestAntiSymmetry:
    """kappa(k') = -kappa(k) under FF duality (Theorem D_scal (iv))."""

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_kappa_anti_symmetry_symbolic(self, typ, rank, dim_g, h_dual, name):
        """kappa(k) + kappa(k') = 0 symbolically."""
        kap = kappa_km(typ, rank, k)
        k_prime = ff_dual_level(typ, rank, k)
        kap_prime = kappa_km(typ, rank, k_prime)
        assert simplify(kap + kap_prime) == 0, \
            f"{name}: kappa + kappa' = {simplify(kap + kap_prime)}"

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_kappa_anti_symmetry_numeric(self, typ, rank, dim_g, h_dual, name):
        """kappa(k) + kappa(k') = 0 at specific levels."""
        for lev in TEST_LEVELS:
            kap = kappa_km(typ, rank, lev)
            lev_prime = ff_dual_level(typ, rank, lev)
            kap_prime = kappa_km(typ, rank, lev_prime)
            assert kap + kap_prime == 0, \
                f"{name} at k={lev}: kappa + kappa' = {kap + kap_prime}"

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_anti_symmetry_from_channels(self, typ, rank, dim_g, h_dual, name):
        """Anti-symmetry follows from the shear matrix: (1,1) * S * (kappa_dp, kappa_sp)^T = -(kappa_dp + kappa_sp)."""
        S = shear_matrix()
        dp = kappa_dp(dim_g, h_dual, k)
        sp = kappa_sp(dim_g)
        v = Matrix([dp, sp])
        v_prime = S * v
        # Total at dual level
        total_prime = v_prime[0] + v_prime[1]
        # Total at original level
        total = dp + sp
        assert simplify(total_prime + total) == 0


# ===========================================================================
# IV. SPECTRAL PROPERTIES OF THE SHEAR MATRIX
# ===========================================================================

class TestShearMatrixSpectral:
    """The shear matrix has eigenvalues {-1, 1} and kappa is a (-1)-eigenvector."""

    def test_eigenvalues(self):
        """Eigenvalues of ((-1,-2),(0,1)) are {-1, 1}."""
        S = shear_matrix()
        eigenvals = S.eigenvals()
        # eigenvals is a dict: eigenvalue -> multiplicity
        assert set(eigenvals.keys()) == {-1, 1}, \
            f"Eigenvalues: {set(eigenvals.keys())} != {{-1, 1}}"

    def test_determinant(self):
        """det(S) = -1 (product of eigenvalues)."""
        S = shear_matrix()
        assert S.det() == -1

    def test_trace(self):
        """tr(S) = 0 (sum of eigenvalues)."""
        S = shear_matrix()
        assert S.trace() == 0

    def test_involution(self):
        """S^2 = I (the shear is an involution)."""
        S = shear_matrix()
        assert S ** 2 == Matrix.eye(2)

    def test_total_kappa_is_minus_one_eigenvector(self):
        """The total kappa vector (1,1)^T projected: S maps kappa to -kappa.

        More precisely: if v = (kappa_dp, kappa_sp), then
        (1,1) . S . v = -(1,1) . v, which means the linear form
        'total = kappa_dp + kappa_sp' is a (-1)-eigenvector of S^T.
        """
        S = shear_matrix()
        # The row vector (1,1) is a left (-1)-eigenvector of S:
        # (1,1) * S = (-1) * (1,1)
        row = Matrix([[1, 1]])
        result = row * S
        assert result == -row, \
            f"(1,1) * S = {result}, expected {-row}"

    def test_plus_one_eigenvector(self):
        """The (+1)-eigenvector of S is (-1, 1)^T (up to scale).

        S * (-1,1)^T = ((-1)(-1) + (-2)(1), (0)(-1) + (1)(1))^T = (-1, 1)^T.
        Physically: kappa_sp - kappa_dp is FF-invariant (fixed by duality).
        """
        S = shear_matrix()
        v = Matrix([-1, 1])
        assert S * v == v

    def test_minus_one_eigenvector(self):
        """The (-1)-eigenvector is (1, 1) (up to scale).

        S * (1,1)^T = (-1-2, 0+1) = (-3, 1) != -1 * (1,1)
        So (1,1) is NOT a right eigenvector. Instead, the right (-1)-eigenvector
        is (1, 0)^T: S * (1,0) = (-1, 0) = -1 * (1, 0).
        """
        S = shear_matrix()
        v = Matrix([1, 0])
        assert S * v == -v, "kappa_dp direction is a (-1)-eigenvector"


# ===========================================================================
# V. W_N CHANNEL VECTOR
# ===========================================================================

class TestWNChannelVector:
    """W_N modular characteristic: kappa(W_N) = c * (H_N - 1),
    where H_N = sum_{j=1}^N 1/j is the N-th harmonic number.

    The sigma_invariant for A_{N-1} gives sum_{s=2}^N 1/s = H_N - 1.
    Reference: concordance.tex, Theorem thm:wn-obstruction.
    """

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_sigma_equals_harmonic_minus_one(self, N):
        """sigma(A_{N-1}) = H_N - 1 = sum_{s=2}^N 1/s.

        Only N <= 4 because cartan_data registry has A_1 through A_3.
        """
        from compute.lib.lie_algebra import sigma_invariant
        sigma = sigma_invariant("A", N - 1)
        expected = harmonic_number(N) - 1
        assert sigma == expected, \
            f"sigma(A_{N-1}) = {sigma} != H_{N} - 1 = {expected}"

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_wn_kappa_formula(self, N):
        """kappa(W_N^k) = c * sigma(A_{N-1}) for N where cartan_data exists."""
        from compute.lib.lie_algebra import sigma_invariant
        c = Symbol('c')
        sigma = sigma_invariant("A", N - 1)
        kap = c * sigma
        expected = c * (harmonic_number(N) - 1)
        assert simplify(kap - expected) == 0, \
            f"W_{N}: kappa = {kap} != c * (H_{N} - 1) = {expected}"

    @pytest.mark.parametrize("N,expected_sigma", [
        (2, Rational(1, 2)),       # H_2 - 1 = 1/2
        (3, Rational(5, 6)),       # H_3 - 1 = 1/2 + 1/3
        (4, Rational(13, 12)),     # H_4 - 1 = 1/2 + 1/3 + 1/4
        (5, Rational(77, 60)),     # H_5 - 1 = 1/2 + 1/3 + 1/4 + 1/5
    ])
    def test_wn_sigma_known_values(self, N, expected_sigma):
        """Verify H_N - 1 matches known harmonic number values.

        Uses sigma_invariant for N <= 4 (where cartan_data exists),
        direct computation for N = 5.
        """
        computed = harmonic_number(N) - 1
        assert computed == expected_sigma, \
            f"H_{N} - 1 = {computed} != {expected_sigma}"
        # Cross-check with sigma_invariant where available
        if N <= 4:
            from compute.lib.lie_algebra import sigma_invariant
            assert sigma_invariant("A", N - 1) == expected_sigma

    def test_harmonic_divergence(self):
        """H_N ~ log(N) as N -> infinity (Euler-Mascheroni).

        Specifically, |H_N - ln(N) - gamma| < 1/(2N) for N >= 1,
        where gamma ~ 0.5772.
        """
        from sympy import EulerGamma
        gamma = float(EulerGamma.evalf())

        for N in [10, 20, 50, 100, 1000]:
            H_N = float(harmonic_number(N))
            ln_N = float(neval(log(N)))
            # H_N - ln(N) should approach gamma
            residual = abs(H_N - ln_N - gamma)
            bound = 1.0 / (2 * N)
            assert residual < bound, \
                f"N={N}: |H_N - ln(N) - gamma| = {residual} >= 1/(2N) = {bound}"

    def test_sigma_diverges(self):
        """sigma(A_{N-1}) = H_N - 1 diverges as N -> infinity.

        This is the structural obstruction for MC4: the scalar
        modular characteristic cannot have a finite W_infinity limit.
        """
        values = []
        for N in [2, 5, 10, 20, 50]:
            sigma_N = float(harmonic_number(N) - 1)
            values.append(sigma_N)

        # Verify strict monotonic increase
        for i in range(len(values) - 1):
            assert values[i] < values[i + 1], \
                f"sigma not increasing: {values[i]} >= {values[i+1]}"

        # sigma(A_49) = H_50 - 1 > 3 (since H_50 ~ 4.499)
        assert values[-1] > 3, \
            f"sigma(A_49) = {values[-1]} should be > 3"


# ===========================================================================
# VI. CHANNEL DECOMPOSITION AT SPECIAL LEVELS
# ===========================================================================

class TestSpecialLevels:
    """Behavior at critical level k = -h^vee and self-dual level k = -h^vee."""

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_critical_level_dp_vanishes(self, typ, rank, dim_g, h_dual, name):
        """At k = -h^vee: kappa_dp = -dim(g)/2, kappa_sp = dim(g)/2, kappa = 0."""
        lev = -h_dual
        dp = kappa_dp(dim_g, h_dual, lev)
        sp = kappa_sp(dim_g)
        assert dp == Rational(-dim_g, 2), f"{name}: kappa_dp at critical = {dp}"
        assert sp == Rational(dim_g, 2), f"{name}: kappa_sp at critical = {sp}"
        assert dp + sp == 0, f"{name}: kappa at critical = {dp + sp}"

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_level_zero(self, typ, rank, dim_g, h_dual, name):
        """At k = 0: kappa_dp = 0, kappa = kappa_sp = dim(g)/2."""
        dp = kappa_dp(dim_g, h_dual, 0)
        sp = kappa_sp(dim_g)
        assert dp == 0, f"{name}: kappa_dp at k=0 = {dp}"
        assert dp + sp == Rational(dim_g, 2), f"{name}: kappa at k=0"

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_ff_dual_of_critical(self, typ, rank, dim_g, h_dual, name):
        """FF dual of critical level -h^vee is -h^vee (it is a fixed point)."""
        lev = -h_dual
        lev_prime = -lev - 2 * h_dual
        assert lev_prime == lev, \
            f"{name}: FF(-h^vee) = {lev_prime} != -h^vee = {lev}"

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", ALGEBRAS)
    def test_ff_dual_of_zero(self, typ, rank, dim_g, h_dual, name):
        """FF dual of k=0 is k'=-2h^vee. Kappa flips sign."""
        lev_prime = -2 * h_dual
        kap_0 = Rational(dim_g, 2)
        kap_prime = Rational(dim_g) * (lev_prime + h_dual) / (2 * h_dual)
        assert kap_prime == -kap_0, \
            f"{name}: kappa(-2h^vee) = {kap_prime} != -kappa(0) = {-kap_0}"


# ===========================================================================
# VII. CROSS-CHECKS WITH KNOWN VALUES
# ===========================================================================

class TestKnownValues:
    """Verify channel decomposition against known values from the manuscript."""

    def test_sl2_kappa_at_k1(self):
        """sl_2 at k=1: kappa = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_km("A", 1, 1) == Rational(9, 4)
        assert kappa_dp(3, 2, 1) == Rational(3, 4)
        assert kappa_sp(3) == Rational(3, 2)
        assert Rational(3, 4) + Rational(3, 2) == Rational(9, 4)

    def test_sl3_kappa_at_k1(self):
        """sl_3 at k=1: kappa = 8*(1+3)/(2*3) = 16/3."""
        assert kappa_km("A", 2, 1) == Rational(16, 3)
        assert kappa_dp(8, 3, 1) == Rational(4, 3)
        assert kappa_sp(8) == 4
        assert Rational(4, 3) + 4 == Rational(16, 3)

    def test_sp4_kappa_at_k1(self):
        """sp_4 at k=1: kappa = 10*(1+3)/(2*3) = 20/3.

        CLAUDE.md: sp_4 h_dual=3, kappa = 5(k+3)/3.
        """
        assert kappa_km("B", 2, 1) == Rational(20, 3)

    def test_g2_kappa_at_k1(self):
        """g_2 at k=1: kappa = 14*(1+4)/(2*4) = 35/4.

        CLAUDE.md: g2_kappa(k) = 7(k+4)/4.
        """
        assert kappa_km("G", 2, 1) == Rational(35, 4)
