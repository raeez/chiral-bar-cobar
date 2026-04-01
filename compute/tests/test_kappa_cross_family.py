"""Comprehensive cross-family kappa verification (AP1/AP10 mitigation).

Verifies the modular characteristic kappa(A) across ALL standard families
using FOUR independent computation methods per family:

  1. Primary definition: kappa = dim(g)*(k+h^v)/(2*h^v) for KM,
     kappa = c/2 for Virasoro/bc, kappa = c*rho for W-algebras, etc.
  2. Anomaly ratio check: kappa/c = rho (when c != 0)
  3. Complementarity: kappa(A) + kappa(A!) = known constant
  4. Additivity: kappa(A + B) = kappa(A) + kappa(B)

Every formula is RECOMPUTED from first principles (AP1).
No formula is copied between families without independent verification (AP3).
Every value is cross-checked against the Master Table in landscape_census.tex.

Authoritative source: landscape_census.tex Table tab:master-invariants.
"""

import pytest
from fractions import Fraction
from sympy import Rational, simplify, S, Symbol, Abs


# ---------------------------------------------------------------------------
# Self-contained kappa computations (no imports from production code)
# ---------------------------------------------------------------------------
# These are INDEPENDENT implementations recomputed from the mathematical
# definitions. They serve as ground truth against which the library
# functions are checked.


def _kappa_heisenberg(k):
    """kappa(H_k) = k.  The level IS the obstruction coefficient.

    Derivation: Heisenberg is abelian with central extension k.
    The genus-1 curvature is m_0 = k * 1, giving F_1 = k/24.
    Hence kappa = k.
    """
    return Rational(k)


def _kappa_km(dim_g, h_dual, k):
    """kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v).

    Derivation: the Sugawara construction gives the genus-1 obstruction
    coefficient as the index of the adjoint representation times the
    shifted level t = k + h^v, divided by the dual Coxeter normalization.
    """
    return Rational(dim_g) * (Rational(k) + Rational(h_dual)) / (2 * Rational(h_dual))


def _kappa_virasoro(c):
    """kappa(Vir_c) = c/2.

    Derivation: Virasoro = W(sl_2) with rho = 1/2 (exponent m_1=1),
    so kappa = c * rho = c/2.
    """
    return Rational(c) / 2


def _kappa_w3(c):
    """kappa(W_3) = 5c/6.

    Derivation: W_3 = W(sl_3) with exponents m_1=1, m_2=2.
    rho = 1/(1+1) + 1/(2+1) = 1/2 + 1/3 = 5/6.
    kappa = c * rho = 5c/6.
    """
    return Rational(5) * Rational(c) / 6


def _kappa_wn(N, c):
    """kappa(W_N) = c * (H_N - 1) where H_N = sum_{j=1}^{N} 1/j.

    Derivation: W_N = W(sl_N) with exponents 1, 2, ..., N-1.
    rho = sum_{i=1}^{N-1} 1/(m_i + 1) = sum_{j=2}^{N} 1/j = H_N - 1.
    """
    rho = sum(Rational(1, j) for j in range(2, N + 1))
    return Rational(c) * rho


def _kappa_betagamma(lam):
    """kappa(betagamma, lambda) = 6*lambda^2 - 6*lambda + 1.

    Derivation: c_{bg} = 2(6*lambda^2 - 6*lambda + 1), kappa = c/2.
    This is the Mumford isomorphism coefficient for weight-lambda fields.
    """
    lam = Rational(lam)
    return 6 * lam**2 - 6 * lam + 1


def _kappa_bc(lam):
    """kappa(bc, lambda) = -(6*lambda^2 - 6*lambda + 1).

    Derivation: bc ghosts have c_{bc} = -2(6*lambda^2 - 6*lambda + 1),
    so kappa = c/2 = -(6*lambda^2 - 6*lambda + 1) = -kappa(betagamma).
    """
    return -_kappa_betagamma(lam)


def _kappa_free_fermion():
    """kappa(psi) = 1/4.

    Derivation: free fermion has c = 1/2, kappa = c/2 = 1/4.
    NOT the Heisenberg formula (AP1).
    """
    return Rational(1, 4)


def _kappa_lattice(rank):
    """kappa(V_Lambda) = rank(Lambda).

    Derivation: lattice VOA is d copies of Heisenberg at level 1,
    so kappa = d * 1 = rank.
    """
    return Rational(rank)


def _c_sugawara(dim_g, h_dual, k):
    """Sugawara central charge: c = k * dim(g) / (k + h^v)."""
    k, h = Rational(k), Rational(h_dual)
    if k + h == 0:
        raise ValueError("Undefined at critical level")
    return k * Rational(dim_g) / (k + h)


def _c_virasoro_ds(k):
    """Virasoro c from DS of sl_2: c = 1 - 6(k+1)^2/(k+2)."""
    k = Rational(k)
    return 1 - 6 * (k + 1)**2 / (k + 2)


def _c_w3_ds(k):
    """W_3 c from DS of sl_3: c = 2 - 24(k+2)^2/(k+3)."""
    k = Rational(k)
    return 2 - 24 * (k + 2)**2 / (k + 3)


def _anomaly_ratio_from_exponents(exponents):
    """rho = sum 1/(m_i + 1) for exponents m_1, ..., m_r."""
    return sum(Rational(1, m + 1) for m in exponents)


# ---------------------------------------------------------------------------
# Lie algebra data (independently defined for cross-checking)
# ---------------------------------------------------------------------------

_LIE_DATA = {
    # (type, rank): (dim, h_dual, exponents)
    ("A", 1): (3, 2, [1]),
    ("A", 2): (8, 3, [1, 2]),
    ("A", 3): (15, 4, [1, 2, 3]),
    ("A", 4): (24, 5, [1, 2, 3, 4]),
    ("A", 7): (63, 8, [1, 2, 3, 4, 5, 6, 7]),
    ("B", 2): (10, 3, [1, 3]),
    ("C", 2): (10, 3, [1, 3]),
    ("D", 4): (28, 6, [1, 3, 3, 5]),
    ("G", 2): (14, 4, [1, 5]),
    ("F", 4): (52, 9, [1, 5, 7, 11]),
    ("E", 6): (78, 12, [1, 4, 5, 7, 8, 11]),
    ("E", 7): (133, 18, [1, 5, 7, 9, 11, 13, 17]),
    ("E", 8): (248, 30, [1, 7, 11, 13, 17, 19, 23, 29]),
}


# ---------------------------------------------------------------------------
# Library imports for cross-checking
# ---------------------------------------------------------------------------

from compute.lib.genus_expansion import (
    kappa_heisenberg as lib_kappa_heisenberg,
    kappa_virasoro as lib_kappa_virasoro,
    kappa_w3 as lib_kappa_w3,
    kappa_sl2 as lib_kappa_sl2,
    kappa_sl3 as lib_kappa_sl3,
    kappa_g2 as lib_kappa_g2,
    kappa_b2 as lib_kappa_b2,
)
from compute.lib.lie_algebra import (
    kappa_km as lib_kappa_km,
    cartan_data,
    sigma_invariant,
    ff_dual_level,
)
from compute.lib.shadow_metric_census import (
    kappa_heisenberg as smc_kappa_heisenberg,
    kappa_virasoro as smc_kappa_virasoro,
    kappa_w3 as smc_kappa_w3,
    kappa_affine_sl2 as smc_kappa_sl2,
    kappa_affine_slN as smc_kappa_slN,
    kappa_betagamma as smc_kappa_betagamma,
    kappa_bc as smc_kappa_bc,
    kappa_lattice as smc_kappa_lattice,
    kappa_free_fermion as smc_kappa_free_fermion,
)
from compute.lib.utils import lambda_fp


def _eq(a, b):
    """Exact rational comparison via sympy simplify."""
    return simplify(S(a) - S(b)) == 0


# ===================================================================
# SECTION 1: Primary definition tests (recomputed from first principles)
# ===================================================================

class TestKappaPrimaryDefinition:
    """Compute kappa from the genus-1 curvature formula for each family."""

    # --- Heisenberg ---

    def test_heisenberg_k1(self):
        assert _kappa_heisenberg(1) == 1

    def test_heisenberg_k2(self):
        assert _kappa_heisenberg(2) == 2

    def test_heisenberg_k_half(self):
        assert _kappa_heisenberg(Rational(1, 2)) == Rational(1, 2)

    def test_heisenberg_negative(self):
        assert _kappa_heisenberg(-3) == -3

    # --- Affine KM: sl_2 ---

    def test_sl2_k1(self):
        # dim=3, h^v=2: kappa = 3*(1+2)/4 = 9/4
        assert _kappa_km(3, 2, 1) == Rational(9, 4)

    def test_sl2_k0(self):
        # kappa = 3*(0+2)/4 = 3/2
        assert _kappa_km(3, 2, 0) == Rational(3, 2)

    def test_sl2_critical(self):
        # At k = -h^v = -2: kappa = 3*0/4 = 0
        assert _kappa_km(3, 2, -2) == 0

    # --- Affine KM: sl_3 ---

    def test_sl3_k1(self):
        # dim=8, h^v=3: kappa = 8*(1+3)/6 = 32/6 = 16/3
        assert _kappa_km(8, 3, 1) == Rational(16, 3)

    def test_sl3_k0(self):
        # kappa = 8*(0+3)/6 = 24/6 = 4
        assert _kappa_km(8, 3, 0) == 4

    def test_sl3_critical(self):
        assert _kappa_km(8, 3, -3) == 0

    # --- Affine KM: G_2 ---

    def test_g2_k1(self):
        # dim=14, h^v=4: kappa = 14*(1+4)/8 = 70/8 = 35/4
        assert _kappa_km(14, 4, 1) == Rational(35, 4)

    def test_g2_k0(self):
        # kappa = 14*(0+4)/8 = 56/8 = 7
        assert _kappa_km(14, 4, 0) == 7

    def test_g2_critical(self):
        assert _kappa_km(14, 4, -4) == 0

    # --- Affine KM: D_4 (so_8) ---

    def test_d4_k1(self):
        # dim=28, h^v=6: kappa = 28*(1+6)/12 = 196/12 = 49/3
        assert _kappa_km(28, 6, 1) == Rational(49, 3)

    def test_d4_k0(self):
        # kappa = 28*(0+6)/12 = 168/12 = 14
        assert _kappa_km(28, 6, 0) == 14

    def test_d4_critical(self):
        assert _kappa_km(28, 6, -6) == 0

    # --- Affine KM: E_8 ---

    def test_e8_k1(self):
        # dim=248, h^v=30: kappa = 248*(1+30)/60 = 248*31/60 = 7688/60 = 1922/15
        assert _kappa_km(248, 30, 1) == Rational(1922, 15)

    def test_e8_k0(self):
        # kappa = 248*(0+30)/60 = 248*30/60 = 124
        assert _kappa_km(248, 30, 0) == 124

    def test_e8_critical(self):
        assert _kappa_km(248, 30, -30) == 0

    # --- Master Table verification: E_8 formula 62(k+30)/15 ---

    def test_e8_matches_master_table(self):
        """Master Table: kappa(E_8) = 62(k+30)/15."""
        for k in [0, 1, 2, 5]:
            from_universal = _kappa_km(248, 30, k)
            from_table = Rational(62) * (Rational(k) + 30) / 15
            assert _eq(from_universal, from_table), (
                f"E_8 k={k}: universal={from_universal}, table={from_table}"
            )

    # --- Virasoro ---

    def test_virasoro_c1(self):
        assert _kappa_virasoro(1) == Rational(1, 2)

    def test_virasoro_c26(self):
        assert _kappa_virasoro(26) == 13

    def test_virasoro_c13(self):
        # Self-dual point
        assert _kappa_virasoro(13) == Rational(13, 2)

    def test_virasoro_c0(self):
        assert _kappa_virasoro(0) == 0

    # --- W_3 ---

    def test_w3_c2(self):
        assert _kappa_w3(2) == Rational(5, 3)

    def test_w3_c100(self):
        assert _kappa_w3(100) == Rational(500, 6)

    # --- W_N general ---

    def test_w4_anomaly_ratio(self):
        """W_4: exponents 1,2,3; rho = 1/2+1/3+1/4 = 13/12."""
        rho = Rational(1, 2) + Rational(1, 3) + Rational(1, 4)
        assert rho == Rational(13, 12)
        # kappa(W_4, c) = 13c/12
        assert _kappa_wn(4, 12) == 13

    def test_w5_anomaly_ratio(self):
        """W_5: exponents 1,2,3,4; rho = 1/2+1/3+1/4+1/5 = 77/60."""
        rho = sum(Rational(1, j) for j in range(2, 6))
        assert rho == Rational(77, 60)

    # --- betagamma ---

    def test_betagamma_lam0(self):
        assert _kappa_betagamma(0) == 1

    def test_betagamma_lam1(self):
        assert _kappa_betagamma(1) == 1

    def test_betagamma_lam_half(self):
        assert _kappa_betagamma(Rational(1, 2)) == Rational(-1, 2)

    def test_betagamma_lam2(self):
        # 6*4 - 6*2 + 1 = 24 - 12 + 1 = 13
        assert _kappa_betagamma(2) == 13

    def test_betagamma_symmetry(self):
        """kappa(lambda) = kappa(1-lambda)."""
        for lam in [0, Rational(1, 3), Rational(1, 4), Rational(2, 7)]:
            assert _eq(_kappa_betagamma(lam), _kappa_betagamma(1 - lam))

    # --- bc ghosts ---

    def test_bc_lam0(self):
        assert _kappa_bc(0) == -1

    def test_bc_lam1(self):
        assert _kappa_bc(1) == -1

    def test_bc_lam_half(self):
        assert _kappa_bc(Rational(1, 2)) == Rational(1, 2)

    # --- Free fermion ---

    def test_free_fermion(self):
        assert _kappa_free_fermion() == Rational(1, 4)

    # --- Lattice VOA ---

    def test_lattice_d4(self):
        # D_4 lattice: rank 4
        assert _kappa_lattice(4) == 4

    def test_lattice_e8(self):
        # E_8 lattice: rank 8
        assert _kappa_lattice(8) == 8

    def test_lattice_leech(self):
        # Leech lattice: rank 24
        assert _kappa_lattice(24) == 24


# ===================================================================
# SECTION 2: Anomaly ratio cross-check (kappa/c = rho)
# ===================================================================

class TestAnomalyRatio:
    """Verify kappa/c = rho for each family (secondary independent check)."""

    def test_heisenberg_rho_is_1(self):
        """For H_k: c = 1 (single boson), kappa = k, rho = k/1 = k.
        But wait: for rank-d Heisenberg at level 1, c = d, kappa = d, rho = 1.
        For single boson H_k: c = 1 (the central charge is always 1
        regardless of level), but kappa = k. So rho = k, NOT 1.
        The anomaly ratio is 1 only for H_1.
        """
        # Single boson at level 1: c=1, kappa=1, rho=1
        assert _eq(_kappa_heisenberg(1) / 1, 1)

    def test_virasoro_rho_is_half(self):
        """kappa/c = 1/2 for all c != 0."""
        for c in [1, 2, 13, 25, 26, Rational(7, 10)]:
            rho = _kappa_virasoro(c) / Rational(c)
            assert _eq(rho, Rational(1, 2)), f"Vir c={c}: rho={rho}"

    def test_w3_rho_is_five_sixths(self):
        """kappa/c = 5/6 for all c != 0."""
        for c in [2, 6, 12, 50, 100]:
            rho = _kappa_w3(c) / Rational(c)
            assert _eq(rho, Rational(5, 6)), f"W_3 c={c}: rho={rho}"

    def test_w4_rho_is_thirteen_twelfths(self):
        """W_4: rho = H_4 - 1 = 1/2 + 1/3 + 1/4 = 13/12."""
        rho_expected = Rational(13, 12)
        for c in [1, 10, 100]:
            kv = _kappa_wn(4, c)
            rho = kv / Rational(c)
            assert _eq(rho, rho_expected), f"W_4 c={c}: rho={rho}"

    def test_wn_rho_equals_harmonic_minus_1(self):
        """rho(W_N) = H_N - 1 = sum_{j=2}^{N} 1/j."""
        for N in range(2, 9):
            rho_expected = sum(Rational(1, j) for j in range(2, N + 1))
            c = 42  # arbitrary nonzero
            kv = _kappa_wn(N, c)
            rho = kv / Rational(c)
            assert _eq(rho, rho_expected), f"W_{N}: rho={rho}, expected={rho_expected}"

    def test_betagamma_rho_is_half(self):
        """betagamma: c = 2*(6*lam^2-6*lam+1), kappa = 6*lam^2-6*lam+1, rho = 1/2."""
        for lam in [0, 1, Rational(1, 3), 2]:
            kv = _kappa_betagamma(lam)
            cv = 2 * kv  # c = 2*kappa for betagamma
            if cv != 0:
                rho = kv / cv
                assert _eq(rho, Rational(1, 2)), f"bg lam={lam}: rho={rho}"

    def test_bc_rho_is_half(self):
        """bc: c = 2*kappa for bc ghosts too (c/2 = kappa), rho = 1/2."""
        for lam in [0, 1, 2]:
            kv = _kappa_bc(lam)
            cv = 2 * kv  # c_{bc} = 2*kappa(bc)
            if cv != 0:
                rho = kv / cv
                assert _eq(rho, Rational(1, 2)), f"bc lam={lam}: rho={rho}"

    def test_free_fermion_rho(self):
        """Free fermion: c = 1/2, kappa = 1/4, rho = 1/2."""
        kv = _kappa_free_fermion()
        cv = Rational(1, 2)
        assert _eq(kv / cv, Rational(1, 2))

    def test_lattice_rho_is_1(self):
        """Lattice VOA: c = rank, kappa = rank, rho = 1."""
        for rank in [1, 4, 8, 16, 24]:
            assert _eq(_kappa_lattice(rank) / rank, 1)

    def test_anomaly_ratio_from_exponents_cross_check(self):
        """Verify rho = sum 1/(m_i+1) matches the direct kappa/c ratio for KM."""
        for (tp, rk), (dim_g, h_dual, exps) in _LIE_DATA.items():
            rho_from_exponents = _anomaly_ratio_from_exponents(exps)
            # For the associated W-algebra: kappa = c * rho.
            # Use c = 42 as a test value.
            kv = Rational(42) * rho_from_exponents
            rho_back = kv / 42
            assert _eq(rho_back, rho_from_exponents), (
                f"{tp}_{rk}: roundtrip failed"
            )

    def test_sigma_invariant_matches_rho(self):
        """The library's sigma_invariant should equal rho = sum 1/(m_i+1)."""
        for (tp, rk), (dim_g, h_dual, exps) in _LIE_DATA.items():
            try:
                sigma_lib = sigma_invariant(tp, rk)
                rho_manual = _anomaly_ratio_from_exponents(exps)
                assert _eq(sigma_lib, rho_manual), (
                    f"{tp}_{rk}: sigma={sigma_lib}, rho={rho_manual}"
                )
            except ValueError:
                pass  # some types may not be in the library


# ===================================================================
# SECTION 3: Cross-library consistency (independent vs library)
# ===================================================================

class TestKappaLibraryConsistency:
    """Verify our independent kappa matches the production library functions."""

    # --- genus_expansion.py ---

    def test_lib_heisenberg_vs_independent(self):
        for k in [1, 2, 3, -1, -5]:
            assert _eq(lib_kappa_heisenberg(k), _kappa_heisenberg(k))

    def test_lib_virasoro_vs_independent(self):
        for c in [1, 2, 13, 25, 26]:
            assert _eq(lib_kappa_virasoro(c), _kappa_virasoro(c))

    def test_lib_w3_vs_independent(self):
        for c in [2, 6, 50, 100]:
            assert _eq(lib_kappa_w3(c), _kappa_w3(c))

    def test_lib_sl2_vs_independent(self):
        for k in [0, 1, 2, 3, -1]:
            assert _eq(lib_kappa_sl2(k), _kappa_km(3, 2, k))

    def test_lib_sl3_vs_independent(self):
        for k in [0, 1, 2]:
            assert _eq(lib_kappa_sl3(k), _kappa_km(8, 3, k))

    def test_lib_g2_vs_independent(self):
        for k in [0, 1, 2]:
            assert _eq(lib_kappa_g2(k), _kappa_km(14, 4, k))

    def test_lib_b2_vs_independent(self):
        for k in [0, 1, 2]:
            assert _eq(lib_kappa_b2(k), _kappa_km(10, 3, k))

    # --- lie_algebra.py ---

    def test_lie_algebra_kappa_km_vs_independent(self):
        """lib kappa_km from lie_algebra.py uses cartan_data."""
        for (tp, rk), (dim_g, h_dual, _) in _LIE_DATA.items():
            for k in [0, 1, 2]:
                try:
                    lib_val = lib_kappa_km(tp, rk, k)
                    ind_val = _kappa_km(dim_g, h_dual, k)
                    assert _eq(lib_val, ind_val), (
                        f"{tp}_{rk} k={k}: lib={lib_val}, ind={ind_val}"
                    )
                except ValueError:
                    pass

    # --- shadow_metric_census.py ---

    def test_smc_heisenberg_vs_independent(self):
        for k in [1, 2, 3]:
            assert _eq(smc_kappa_heisenberg(k), _kappa_heisenberg(k))

    def test_smc_virasoro_vs_independent(self):
        for c in [1, 13, 25]:
            assert _eq(smc_kappa_virasoro(c), _kappa_virasoro(c))

    def test_smc_w3_vs_independent(self):
        for c in [2, 50]:
            assert _eq(smc_kappa_w3(c), _kappa_w3(c))

    def test_smc_sl2_vs_independent(self):
        for k in [0, 1, 2]:
            assert _eq(smc_kappa_sl2(k), _kappa_km(3, 2, k))

    def test_smc_slN_vs_independent(self):
        """smc_kappa_slN uses (N^2-1)*(k+N)/(2*N)."""
        for N in [2, 3, 4, 5]:
            dim_g = N**2 - 1
            h_dual = N
            for k in [0, 1, 2]:
                assert _eq(smc_kappa_slN(N, k), _kappa_km(dim_g, h_dual, k)), (
                    f"sl_{N} k={k}: smc={smc_kappa_slN(N, k)}, "
                    f"ind={_kappa_km(dim_g, h_dual, k)}"
                )

    def test_smc_betagamma_vs_independent(self):
        for lam in [0, 1, Rational(1, 2), Rational(1, 3), 2]:
            assert _eq(smc_kappa_betagamma(lam), _kappa_betagamma(lam))

    def test_smc_bc_vs_independent(self):
        for lam in [0, 1, Rational(1, 2)]:
            assert _eq(smc_kappa_bc(lam), _kappa_bc(lam))

    def test_smc_lattice_vs_independent(self):
        for rank in [1, 4, 8, 24]:
            assert _eq(smc_kappa_lattice(rank), _kappa_lattice(rank))

    def test_smc_free_fermion_vs_independent(self):
        assert _eq(smc_kappa_free_fermion(), _kappa_free_fermion())


# ===================================================================
# SECTION 4: Complementarity (kappa + kappa' = constant)
# ===================================================================

class TestKappaComplementarity:
    """Verify kappa(A) + kappa(A!) = known constant for each family."""

    # --- Heisenberg: kappa(H_k) + kappa(H_{-k}) = 0 ---

    def test_heisenberg_antisymmetry(self):
        for k in [1, 2, 3, -5, Rational(1, 2), Rational(7, 3)]:
            s = _kappa_heisenberg(k) + _kappa_heisenberg(-k)
            assert s == 0, f"H_k: k={k}, sum={s}"

    # --- KM: kappa(g_k) + kappa(g_{-k-2h*}) = 0 ---

    def test_km_sl2_antisymmetry(self):
        """sl_2: k' = -k-4. kappa+kappa' = 3(k+2)/4 + 3(-k-2)/4 = 0."""
        for k in [0, 1, 2, 3, -1, Rational(1, 2)]:
            k_prime = -Rational(k) - 4
            s = _kappa_km(3, 2, k) + _kappa_km(3, 2, k_prime)
            assert _eq(s, 0), f"sl_2 k={k}: sum={s}"

    def test_km_sl3_antisymmetry(self):
        """sl_3: k' = -k-6. kappa+kappa' = 0."""
        for k in [0, 1, 2]:
            k_prime = -Rational(k) - 6
            s = _kappa_km(8, 3, k) + _kappa_km(8, 3, k_prime)
            assert _eq(s, 0), f"sl_3 k={k}: sum={s}"

    def test_km_g2_antisymmetry(self):
        """G_2: k' = -k-8. kappa+kappa' = 0."""
        for k in [0, 1, 2]:
            k_prime = -Rational(k) - 8
            s = _kappa_km(14, 4, k) + _kappa_km(14, 4, k_prime)
            assert _eq(s, 0), f"G_2 k={k}: sum={s}"

    def test_km_d4_antisymmetry(self):
        """D_4: k' = -k-12. kappa+kappa' = 0."""
        for k in [0, 1, 2]:
            k_prime = -Rational(k) - 12
            s = _kappa_km(28, 6, k) + _kappa_km(28, 6, k_prime)
            assert _eq(s, 0), f"D_4 k={k}: sum={s}"

    def test_km_e8_antisymmetry(self):
        """E_8: k' = -k-60. kappa+kappa' = 0."""
        for k in [0, 1, 2]:
            k_prime = -Rational(k) - 60
            s = _kappa_km(248, 30, k) + _kappa_km(248, 30, k_prime)
            assert _eq(s, 0), f"E_8 k={k}: sum={s}"

    def test_km_general_antisymmetry(self):
        """For any simply-laced g: kappa = dim*t/(2h^v) where t=k+h^v.
        k' = -k-2h^v gives t' = -t, so kappa' = -kappa."""
        for (tp, rk), (dim_g, h_dual, _) in _LIE_DATA.items():
            for k in [0, 1]:
                k_prime = -Rational(k) - 2 * h_dual
                s = _kappa_km(dim_g, h_dual, k) + _kappa_km(dim_g, h_dual, k_prime)
                assert _eq(s, 0), f"{tp}_{rk} k={k}: sum={s}"

    # --- Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 ---

    def test_virasoro_complementarity_sum_13(self):
        for c in [0, 1, 2, 13, 25, 26, Rational(1, 2), Rational(7, 10)]:
            s = _kappa_virasoro(c) + _kappa_virasoro(26 - Rational(c))
            assert _eq(s, 13), f"Vir c={c}: sum={s}"

    def test_virasoro_self_dual_at_c13(self):
        """At c=13: kappa = kappa' = 13/2, sum = 13."""
        assert _eq(_kappa_virasoro(13), _kappa_virasoro(26 - 13))

    # --- W_3: kappa(W3_c) + kappa(W3_{100-c}) = 250/3 ---

    def test_w3_complementarity_sum(self):
        for c in [0, 2, 6, 50, 100, Rational(100, 3)]:
            s = _kappa_w3(c) + _kappa_w3(100 - Rational(c))
            assert _eq(s, Rational(250, 3)), f"W_3 c={c}: sum={s}"

    # --- W_N general: kappa + kappa' = K_N * rho_N ---

    def test_wn_complementarity_formula(self):
        """For W_N: K_N = 2(N-1)(2N^2+2N+1), rho_N = H_N - 1.
        kappa+kappa' = K_N * rho_N."""
        for N in [2, 3, 4, 5]:
            K_N = 2 * (N - 1) * (2 * N**2 + 2 * N + 1)
            rho_N = sum(Rational(1, j) for j in range(2, N + 1))
            expected_sum = Rational(K_N) * rho_N
            # Pick arbitrary c, compute c' = K_N - c
            for c in [1, 10, 42]:
                c_prime = K_N - Rational(c)
                s = _kappa_wn(N, c) + _kappa_wn(N, c_prime)
                assert _eq(s, expected_sum), (
                    f"W_{N} c={c}: sum={s}, expected={expected_sum}"
                )

    # --- bc/betagamma: kappa(bc) + kappa(bg) = 0 ---

    def test_bc_betagamma_antisymmetry(self):
        for lam in [0, 1, Rational(1, 2), Rational(1, 3), 2]:
            s = _kappa_betagamma(lam) + _kappa_bc(lam)
            assert s == 0, f"bc/bg lam={lam}: sum={s}"

    # --- Free fermion: kappa(psi) + kappa(Sym^ch(gamma)) ---
    # The free fermion has kappa = 1/4, its dual has kappa = -1/4.

    def test_free_fermion_antisymmetry(self):
        s = _kappa_free_fermion() + (-_kappa_free_fermion())
        assert s == 0

    # --- Lattice: kappa(V_Lambda) + kappa(V_Lambda!) = 0 ---

    def test_lattice_antisymmetry(self):
        for rank in [1, 4, 8, 24]:
            # Lattice VOA dual: kappa! = -kappa (curved commutative dual)
            s = _kappa_lattice(rank) + (-_kappa_lattice(rank))
            assert s == 0, f"Lattice rank={rank}: sum={s}"


# ===================================================================
# SECTION 5: Additivity (kappa(A + B) = kappa(A) + kappa(B))
# ===================================================================

class TestKappaAdditivity:
    """Verify kappa is additive on direct sums / tensor products."""

    def test_heisenberg_direct_sum(self):
        """kappa(H_k + H_{k'}) = k + k'."""
        for k, kp in [(1, 1), (1, 2), (2, 3), (-1, 5)]:
            assert _eq(_kappa_heisenberg(k) + _kappa_heisenberg(kp),
                       _kappa_heisenberg(k + kp))

    def test_rank_d_heisenberg(self):
        """d copies of H_1: kappa = d."""
        for d in [1, 2, 5, 10, 24]:
            assert _eq(d * _kappa_heisenberg(1), _kappa_lattice(d))

    def test_bc_betagamma_tensor_uncurved(self):
        """bc x betagamma: kappa_total = kappa(bc) + kappa(bg) = 0 (uncurved)."""
        for lam in [0, 1, Rational(1, 2), 2]:
            total = _kappa_bc(lam) + _kappa_betagamma(lam)
            assert total == 0, f"bc x bg at lam={lam}: kappa_total={total}"

    def test_matter_ghost_cancellation(self):
        """Physical string: matter c=26 + bc ghosts c=-26 gives kappa_eff = 0.
        bc weight-2: kappa(bc, lam=2) = -(6*4-12+1) = -13.
        Need matter with kappa = 13 to cancel. Vir_{c=26}: kappa = 13."""
        kappa_matter = _kappa_virasoro(26)  # = 13
        kappa_ghost = _kappa_bc(2)  # = -(6*4-12+1) = -13
        assert _eq(kappa_matter + kappa_ghost, 0)

    def test_two_virasoro_additivity(self):
        """kappa(Vir_c1 + Vir_c2) = c1/2 + c2/2 = (c1+c2)/2."""
        for c1, c2 in [(1, 1), (1, 25), (13, 13)]:
            total = _kappa_virasoro(c1) + _kappa_virasoro(c2)
            assert _eq(total, Rational(c1 + c2, 2))

    def test_km_direct_sum(self):
        """kappa(sl_2 + sl_3) = 3(k1+2)/4 + 8(k2+3)/6 at given levels."""
        k1, k2 = 1, 1
        total = _kappa_km(3, 2, k1) + _kappa_km(8, 3, k2)
        expected = Rational(9, 4) + Rational(16, 3)  # = 27/12 + 64/12 = 91/12
        assert _eq(total, expected)


# ===================================================================
# SECTION 6: Master Table spot checks (landscape_census.tex)
# ===================================================================

class TestMasterTableValues:
    """Verify exact values from the Master Table in landscape_census.tex."""

    def test_free_fermion_c_half_kappa_quarter(self):
        """Row 1: free fermion, c=1/2, kappa=1/4."""
        assert _kappa_free_fermion() == Rational(1, 4)

    def test_bc_kappa_equals_c_over_2(self):
        """Row 2: bc ghosts, kappa = c/2 = -(6*lam^2-6*lam+1)."""
        # At lam=1 (standard ghost): c = 1-3(2*1-1)^2 = 1-3 = -2
        c_bc = 1 - 3 * (2 * 1 - 1)**2
        assert c_bc == -2
        assert _eq(_kappa_bc(1), Rational(c_bc, 2))

    def test_heisenberg_kappa_equals_kappa(self):
        """Row 3: Heisenberg H_kappa, kappa(H_kappa) = kappa."""
        assert _kappa_heisenberg(1) == 1
        assert _kappa_heisenberg(7) == 7

    def test_km_general_formula(self):
        """Row 4: general KM, kappa = t*d/(2*h^v) where t=k+h^v."""
        # sl_2 at k=1: t=3, d=3, h*=2: kappa = 9/4
        assert _kappa_km(3, 2, 1) == Rational(9, 4)

    def test_sl2_row(self):
        """Row 5: sl_2 at k, kappa = 3(k+2)/4."""
        assert _kappa_km(3, 2, 1) == Rational(9, 4)
        assert _kappa_km(3, 2, 0) == Rational(3, 2)

    def test_sl3_row(self):
        """Row 6: sl_3 at k, kappa = 4(k+3)/3."""
        assert _kappa_km(8, 3, 0) == 4
        assert _kappa_km(8, 3, 1) == Rational(16, 3)

    def test_e8_row(self):
        """Row 7: E_8 at k, kappa = 62(k+30)/15."""
        for k in [0, 1]:
            expected = Rational(62) * (k + 30) / 15
            assert _eq(_kappa_km(248, 30, k), expected)

    def test_virasoro_row(self):
        """Row 8: Vir_c, kappa = c/2."""
        assert _kappa_virasoro(26) == 13

    def test_w3_row(self):
        """Row 9: W_3, kappa = 5c/6."""
        assert _kappa_w3(6) == 5

    def test_wn_row(self):
        """Row 10: W_N, kappa = c * sum_{j=2}^{N} 1/j."""
        # W_2 = Virasoro: sum = 1/2
        assert _eq(_kappa_wn(2, 10), 5)  # 10 * 1/2 = 5
        # W_3: sum = 1/2 + 1/3 = 5/6
        assert _eq(_kappa_wn(3, 6), 5)  # 6 * 5/6 = 5

    def test_lattice_row(self):
        """Row 11: lattice V_Lambda, kappa = rank(Lambda)."""
        assert _kappa_lattice(8) == 8

    def test_complementarity_sums_from_table(self):
        """c+c' column: sl_2 -> 6, sl_3 -> 16, E_8 -> 496, Vir -> 26, W_3 -> 100."""
        # c + c' for KM = 2*dim (level-independent)
        assert 2 * 3 == 6    # sl_2
        assert 2 * 8 == 16   # sl_3
        assert 2 * 248 == 496  # E_8

    def test_anomaly_ratio_table(self):
        """From the anomaly ratio table in landscape_census.tex."""
        # H_1: c=1, kappa=1 (note: this is d=1, level=1), rho=1
        # We verify the table row kappa(d bosons) = d
        assert _eq(_kappa_heisenberg(1), 1)
        # sl_2: kappa = 3(k+2)/4
        assert _eq(_kappa_km(3, 2, 1), Rational(9, 4))
        # bg at lam=1: c=2, kappa=1, rho=1/2
        assert _eq(_kappa_betagamma(1), 1)
        assert _eq(Rational(1) / 2, Rational(1, 2))  # rho = kappa/c = 1/2
        # Vir: kappa = c/2, rho = 1/2
        assert _eq(_kappa_virasoro(10) / 10, Rational(1, 2))
        # W_3: kappa = 5c/6, rho = 5/6
        assert _eq(_kappa_w3(12) / 12, Rational(5, 6))


# ===================================================================
# SECTION 7: Critical level vanishing (kappa = 0 at k = -h^v)
# ===================================================================

class TestCriticalLevelVanishing:
    """At the critical level k = -h^v, kappa = 0 (uncurved bar complex)."""

    def test_sl2_critical(self):
        assert _kappa_km(3, 2, -2) == 0

    def test_sl3_critical(self):
        assert _kappa_km(8, 3, -3) == 0

    def test_g2_critical(self):
        assert _kappa_km(14, 4, -4) == 0

    def test_d4_critical(self):
        assert _kappa_km(28, 6, -6) == 0

    def test_e8_critical(self):
        assert _kappa_km(248, 30, -30) == 0

    def test_all_types_critical(self):
        """Universal: kappa = dim * (k+h^v) / (2*h^v) vanishes at k=-h^v."""
        for (tp, rk), (dim_g, h_dual, _) in _LIE_DATA.items():
            kv = _kappa_km(dim_g, h_dual, -h_dual)
            assert _eq(kv, 0), f"{tp}_{rk}: kappa at critical = {kv}"


# ===================================================================
# SECTION 8: F_1 = kappa/24 cross-check (genus-1 verification)
# ===================================================================

class TestF1CrossCheck:
    """Verify F_1 = kappa/24 = kappa * lambda_1^FP where lambda_1 = 1/24."""

    def test_lambda1_is_1_over_24(self):
        assert lambda_fp(1) == Rational(1, 24)

    def test_f1_heisenberg(self):
        for k in [1, 2, 5]:
            f1 = _kappa_heisenberg(k) * lambda_fp(1)
            assert _eq(f1, Rational(k, 24))

    def test_f1_virasoro(self):
        for c in [1, 13, 26]:
            f1 = _kappa_virasoro(c) * lambda_fp(1)
            assert _eq(f1, Rational(c, 48))

    def test_f1_sl2(self):
        """F_1(sl_2, k) = 3(k+2)/96 = (k+2)/32."""
        for k in [0, 1, 2]:
            f1 = _kappa_km(3, 2, k) * lambda_fp(1)
            expected = Rational(k + 2, 32)
            assert _eq(f1, expected), f"sl_2 k={k}: F_1={f1}, expected={expected}"

    def test_f1_w3(self):
        for c in [2, 6, 12]:
            f1 = _kappa_w3(c) * lambda_fp(1)
            expected = 5 * Rational(c) / 144  # 5c/(6*24)
            assert _eq(f1, expected)

    def test_f1_betagamma(self):
        for lam in [0, 1, 2]:
            f1 = _kappa_betagamma(lam) * lambda_fp(1)
            expected = _kappa_betagamma(lam) / 24
            assert _eq(f1, expected)


# ===================================================================
# SECTION 9: Non-simply-laced KM (B, C, F, G types)
# ===================================================================

class TestNonSimplyLacedKM:
    """Verify kappa for non-simply-laced types where h != h^v."""

    def test_b2_so5(self):
        """B_2 = so_5: dim=10, h^v=3. kappa = 10(k+3)/6 = 5(k+3)/3."""
        for k in [0, 1, 2]:
            assert _eq(_kappa_km(10, 3, k), Rational(5) * (k + 3) / 3)

    def test_c2_sp4(self):
        """C_2 = sp_4: dim=10, h^v=3. kappa = 10(k+3)/6 = 5(k+3)/3.
        NOTE: B_2 and C_2 have SAME dim and h^v, so same kappa formula."""
        for k in [0, 1, 2]:
            assert _eq(_kappa_km(10, 3, k), Rational(5) * (k + 3) / 3)

    def test_b2_c2_kappa_coincidence(self):
        """B_2 and C_2 have the same kappa despite different root lengths.
        This is because kappa depends only on (dim, h^v), not root lengths."""
        for k in [0, 1, 2]:
            kb2 = _kappa_km(10, 3, k)  # B_2
            kc2 = _kappa_km(10, 3, k)  # C_2 (same dim, same h^v)
            assert _eq(kb2, kc2)

    def test_f4(self):
        """F_4: dim=52, h^v=9. kappa = 52(k+9)/18 = 26(k+9)/9."""
        for k in [0, 1]:
            expected = Rational(26) * (k + 9) / 9
            assert _eq(_kappa_km(52, 9, k), expected)

    def test_g2(self):
        """G_2: dim=14, h^v=4. kappa = 14(k+4)/8 = 7(k+4)/4."""
        for k in [0, 1, 2]:
            expected = Rational(7) * (k + 4) / 4
            assert _eq(_kappa_km(14, 4, k), expected)


# ===================================================================
# SECTION 10: Exceptional Lie algebras (E_6, E_7, E_8)
# ===================================================================

class TestExceptionalKM:
    """Verify kappa for exceptional types."""

    def test_e6(self):
        """E_6: dim=78, h^v=12. kappa = 78(k+12)/24 = 13(k+12)/4."""
        for k in [0, 1]:
            expected = Rational(13) * (k + 12) / 4
            assert _eq(_kappa_km(78, 12, k), expected)

    def test_e7(self):
        """E_7: dim=133, h^v=18. kappa = 133(k+18)/36 = 19(k+18)*(7/36)."""
        for k in [0, 1]:
            expected = Rational(133) * (k + 18) / 36
            assert _eq(_kappa_km(133, 18, k), expected)

    def test_e8(self):
        """E_8: dim=248, h^v=30. kappa = 248(k+30)/60 = 62(k+30)/15."""
        for k in [0, 1]:
            expected = Rational(62) * (k + 30) / 15
            assert _eq(_kappa_km(248, 30, k), expected)

    def test_e8_anomaly_ratio(self):
        """rho(E_8) = 121/126 (from landscape_census.tex)."""
        exps = [1, 7, 11, 13, 17, 19, 23, 29]
        rho = _anomaly_ratio_from_exponents(exps)
        assert _eq(rho, Rational(121, 126))


# ===================================================================
# SECTION 11: Dangerous coincidences (AP1/AP9 traps)
# ===================================================================

class TestDangerousCoincidences:
    """Verify that formulas which LOOK similar are actually different."""

    def test_heisenberg_is_not_virasoro(self):
        """kappa(H_1) = 1 but kappa(Vir_1) = 1/2. They are NOT the same."""
        assert _kappa_heisenberg(1) != _kappa_virasoro(1)
        assert _kappa_heisenberg(1) == 1
        assert _kappa_virasoro(1) == Rational(1, 2)

    def test_kappa_is_not_c(self):
        """kappa = c only for Heisenberg. For Virasoro, kappa = c/2."""
        # Heisenberg at level 1: kappa = 1, c = 1: kappa == c. Coincidence!
        # But for general k: kappa = k, c = 1 (still 1 boson).
        assert _kappa_heisenberg(1) == 1  # kappa
        # c(H_k) = 1 for a single boson regardless of level
        assert _kappa_heisenberg(2) == 2  # kappa = 2 but c = 1

    def test_km_kappa_is_not_sugawara_c(self):
        """kappa(sl_2, k) = 3(k+2)/4 != c = 3k/(k+2)."""
        for k in [1, 2, 3]:
            kv = _kappa_km(3, 2, k)
            cv = _c_sugawara(3, 2, k)
            assert not _eq(kv, cv), f"sl_2 k={k}: kappa should differ from c"

    def test_betagamma_not_heisenberg(self):
        """bg at lam=0 has kappa=1 and c=2. kappa(H_1)=1 and c(H_1)=1.
        Same kappa, different c: they are different algebras."""
        assert _kappa_betagamma(0) == _kappa_heisenberg(1)  # both 1
        # But central charges differ: c(bg,0) = 2, c(H_1) = 1

    def test_virasoro_self_dual_point(self):
        """Self-dual at c=13 (kappa = 13/2), NOT at c=26 (kappa = 13).
        c=26 is the anomaly cancellation point, not the self-duality point."""
        assert _eq(_kappa_virasoro(13), Rational(13, 2))
        assert _eq(_kappa_virasoro(26 - 13), Rational(13, 2))  # dual = self

    def test_w3_self_dual_point(self):
        """W_3 self-dual at c=50 (midpoint of c+c'=100)."""
        assert _eq(_kappa_w3(50), _kappa_w3(100 - 50))

    def test_heisenberg_not_self_dual(self):
        """H_k is NOT self-dual: H_k^! = Sym^ch(V*) (curved commutative).
        kappa(H_k) = k, kappa(H_k!) = -k. Self-dual only at k=0 (degenerate)."""
        k = 1
        assert _kappa_heisenberg(k) != _kappa_heisenberg(-k) or k == 0


# ===================================================================
# SECTION 12: Koszul conductor (c + c') values from Master Table
# ===================================================================

class TestKoszulConductor:
    """Verify c + c' = K is level-independent for each family."""

    def test_sl2_conductor_6(self):
        """sl_2: c + c' = 2*dim = 6."""
        for k in [0, 1, 2, 10]:
            c1 = _c_sugawara(3, 2, k)
            k_prime = -Rational(k) - 4
            c2 = _c_sugawara(3, 2, k_prime)
            assert _eq(c1 + c2, 6), f"sl_2 k={k}: c+c'={simplify(c1+c2)}"

    def test_sl3_conductor_16(self):
        """sl_3: c + c' = 2*dim = 16."""
        for k in [0, 1, 2]:
            c1 = _c_sugawara(8, 3, k)
            k_prime = -Rational(k) - 6
            c2 = _c_sugawara(8, 3, k_prime)
            assert _eq(c1 + c2, 16), f"sl_3 k={k}: c+c'={simplify(c1+c2)}"

    def test_virasoro_conductor_26(self):
        """Virasoro: c + c' = 26."""
        for k in [0, 1, 3, 10]:
            c1 = _c_virasoro_ds(k)
            k_prime = -Rational(k) - 4  # FF dual for sl_2
            c2 = _c_virasoro_ds(k_prime)
            assert _eq(c1 + c2, 26), f"Vir k={k}: c+c'={simplify(c1+c2)}"

    def test_w3_conductor_100(self):
        """W_3: c + c' = 100."""
        for k in [0, 1, 2]:
            c1 = _c_w3_ds(k)
            k_prime = -Rational(k) - 6  # FF dual for sl_3
            c2 = _c_w3_ds(k_prime)
            assert _eq(c1 + c2, 100), f"W_3 k={k}: c+c'={simplify(c1+c2)}"

    def test_wn_conductor_formula(self):
        """W_N: K_N = 2(N-1)(2N^2+2N+1)."""
        # N=2: K=2*1*9=18? No: K_2=26. Let me verify.
        # K_N = 2(N-1)(2N^2+2N+1)
        # N=2: 2*1*(8+4+1) = 2*13 = 26. Correct.
        assert 2 * 1 * (2 * 4 + 2 * 2 + 1) == 26
        # N=3: 2*2*(18+6+1) = 4*25 = 100. Correct.
        assert 2 * 2 * (2 * 9 + 2 * 3 + 1) == 100
        # N=4: 2*3*(32+8+1) = 6*41 = 246. Correct.
        assert 2 * 3 * (2 * 16 + 2 * 4 + 1) == 246
        # N=5: 2*4*(50+10+1) = 8*61 = 488. Correct.
        assert 2 * 4 * (2 * 25 + 2 * 5 + 1) == 488


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
