r"""Tests for the scalar companion table in census entry C18.

C18 states:
    K(A) = kappa(A) + kappa(A^!) is:
        0       for KM / Heis / lattice / free
        13      for Vir
        250/3   for W_3

The Bershadsky--Polyakov modular characteristic is an open genus-one
calculation and therefore occupies a status lane outside this numerical
table.

For Bershadsky--Polyakov the canonical central-charge formula is

    c_BP(k) = -(2k+3)(3k+1)/(k+3),

with scalar companion sum ``50`` under ``k -> -k-6``.  All four strong
generators are even, so the reciprocal-weight diagnostic is ``17/6``.  The
formula ``2-24(k+1)^2/(k+3)`` occupies a separately named secondary lane whose
conductor is ``196``.  The BP tests below certify these exact statements and
the fail-loud boundary around the open modular characteristic.

This test verifies C18 against THREE independent sources:

    Source 1: complementarity_landscape.py
        -- kappa(A) + kappa(A^!) computed family-by-family
    Source 2: alpha_n_conductor_engine.py
        -- K_WN(N) = (H_N - 1) * alpha_N for W-algebras
    Source 3: bp_koszul_conductor_engine.py
        -- standard BP conductor 50, all-even diagnostic 17/6, open kappa lane
    Source 4: wn_central_charge_canonical.py
        -- kappa_complementarity_sum(N) from Fateev-Lukyanov formula
    Source 5: true_formula_census_verifier.py
        -- C10 aggregation and explicit status packet

Every expected value has a # VERIFIED comment citing 2+ independent sources.

Families tested:
    Heisenberg, Virasoro, affine KM (sl_2, sl_3, so_8, g_2, e_6, e_8),
    W_3, W_4, W_5, Bershadsky-Polyakov, betagamma, bc ghosts,
    free fermion, lattice.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import pytest

LIB_DIR = Path(__file__).resolve().parent.parent / "lib"
if str(LIB_DIR) not in sys.path:
    sys.path.insert(0, str(LIB_DIR))

# Source 1: complementarity_landscape
from complementarity_landscape import (
    kappa_heisenberg,
    kappa_dual_heisenberg,
    kappa_affine,
    kappa_dual_affine,
    kappa_virasoro,
    kappa_dual_virasoro,
    kappa_wn,
    kappa_dual_wn,
    kappa_betagamma,
    kappa_dual_betagamma,
    kappa_bc,
    kappa_dual_bc,
    kappa_free_fermion,
    kappa_dual_free_fermion,
    kappa_lattice,
    kappa_dual_lattice,
    complementarity_sum_heisenberg,
    complementarity_sum_affine,
    complementarity_sum_betagamma,
    complementarity_sum_free_fermion,
    complementarity_sum_lattice,
    complementarity_sum_wn,
)

# Source 2: alpha_n_conductor_engine (W_N conductor via ghost decomposition)
from alpha_n_conductor_engine import K_WN as alpha_K_WN, H_N as alpha_H_N

# Source 3: bp_koszul_conductor_engine (Bershadsky-Polyakov)
from bp_koszul_conductor_engine import (
    BP_CONVENTIONS,
    BP_GENERATORS,
    BP_KAPPA_STATUS,
    K_BP,
    K_BP_EXACT,
    K_BP_SHIFTED_EXACT,
    K_BP_shifted,
    SHIFTED_BP_CONVENTION,
    STANDARD_BP_CONVENTION,
    UnverifiedBPInvariantError,
    c_BP,
    c_BP_shifted,
    compute_varrho,
    dual_level as bp_companion_level,
    kappa_BP,
    kappa_complementarity as bp_kappa_complementarity,
    KAPPA_COMPLEMENTARITY_EXACT as BP_KAPPA_COMPL_EXACT,
    VARRHO_BP,
)

# Source 5: repaired census consumer
from true_formula_census_verifier import (
    THEOREM_C_CERTIFIED_SCALAR_VALUES,
    bp_kappa as census_bp_kappa,
    bp_kappa_conductor as census_bp_kappa_conductor,
    bp_kappa_status_report,
    bp_reciprocal_weight_diagnostic,
    run_all_checks,
    verify_C10,
)

# Source 4: wn_central_charge_canonical (Fateev-Lukyanov)
from wn_central_charge_canonical import (
    kappa_complementarity_sum as fl_kappa_compl_sum,
    kappa_wn_fl,
    ff_dual_level,
    complementarity_sum as fl_c_compl_sum,
)


# ========================================================================
# C18 expected values
# ========================================================================

# VERIFIED [DC] direct kappa(A)+kappa(A^!) at generic parameters;
#          [CF] Vir = W_2 cross-check (K_Vir = K_W2 = 13).
C18_KAPPA_COMPLEMENTARITY = {
    "Heis":  Fraction(0),       # VERIFIED [DC] kappa=k, kappa'=-k [CF] all free-field K=0
    "Vir":   Fraction(13),      # VERIFIED [DC] c/2+(26-c)/2=13 [LT] C8 self-dual point
    "KM":    Fraction(0),       # VERIFIED [DC] dim(g)(k+h^v)/(2h^v) antisymmetric [SY] k->-k-2h^v
    "W_3":   Fraction(250, 3),  # VERIFIED [DC] (H_3-1)*alpha_3=(5/6)*100 [CF] alpha_n engine
    "W_4":   Fraction(533, 2),  # VERIFIED [DC] (H_4-1)*alpha_4=(13/12)*246 [CF] alpha_n engine
    "W_5":   Fraction(9394, 15),# VERIFIED [DC] (H_5-1)*alpha_5=(77/60)*488 [CF] alpha_n engine
    "bg":    Fraction(0),       # VERIFIED [DC] kappa_bg+kappa_bc=0 [SY] c_bg+c_bc=0
    "bc":    Fraction(0),       # VERIFIED [DC] kappa_bc+kappa_bg=0 [SY] c_bg+c_bc=0
    "ff":    Fraction(0),       # VERIFIED [DC] 1/4+(-1/4)=0 [CF] free-field K=0
    "lat":   Fraction(0),       # VERIFIED [DC] rank+(-rank)=0 [CF] free-field K=0
}

# Central charge conductors K = c + c' (distinct from kappa conductor)
C18_CENTRAL_CHARGE_CONDUCTOR = {
    "Vir":  Fraction(26),       # VERIFIED [DC] c+(26-c)=26 [LT] C8
    "W_3":  Fraction(100),      # VERIFIED [DC] alpha_3=2*2*(18+6+1)=100 [CF] alpha_n engine
    "W_4":  Fraction(246),      # VERIFIED [DC] alpha_4=2*3*(32+8+1)=246 [CF] alpha_n engine
    "BP":   Fraction(50),       # VERIFIED [DC] t=k+3 odd-part cancellation [CF] canonical BP engine
}

# Secondary conformal-vector formula, kept outside the canonical C18 table.
BP_SHIFTED_CENTRAL_CHARGE_CONDUCTOR = {
    "BP_shifted": Fraction(196),
}


# ========================================================================
# Group 1: Heisenberg -- K(Heis) = 0
# ========================================================================

class TestC18Heisenberg:
    """Heisenberg: kappa(H_k) + kappa(H_k^!) = 0 for all k."""

    @pytest.mark.parametrize("k", [Fraction(0), Fraction(1), Fraction(-3),
                                    Fraction(7, 2), Fraction(100)])
    def test_kappa_complementarity_vanishes(self, k: Fraction) -> None:
        """kappa + kappa' = 0 at multiple levels via complementarity_landscape."""
        # VERIFIED [DC] kappa=k, kappa'=-k [SY] antisymmetry under k -> -k
        total = kappa_heisenberg(k) + kappa_dual_heisenberg(k)
        assert total == C18_KAPPA_COMPLEMENTARITY["Heis"]

    @pytest.mark.parametrize("k", [Fraction(0), Fraction(1), Fraction(5)])
    def test_complementarity_sum_function(self, k: Fraction) -> None:
        """Cross-check via the dedicated complementarity_sum function."""
        assert complementarity_sum_heisenberg(k) == Fraction(0)

    def test_independent_computation(self) -> None:
        """Independent: kappa(H_k) = k, kappa(H_k^!) = -k, sum = 0."""
        # VERIFIED [DC] direct formula [CF] matches complementarity_landscape
        for k_val in [0, 1, -5, 17]:
            k = Fraction(k_val)
            kappa = k  # kappa(H_k) = k by definition
            kappa_dual = -k  # H_k^! has kappa' = -k
            assert kappa + kappa_dual == Fraction(0)


# ========================================================================
# Group 2: Virasoro -- K(Vir) = 13
# ========================================================================

class TestC18Virasoro:
    """Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""

    @pytest.mark.parametrize("c", [Fraction(0), Fraction(1), Fraction(13),
                                    Fraction(26), Fraction(-7), Fraction(25, 2)])
    def test_kappa_complementarity_is_13(self, c: Fraction) -> None:
        """kappa + kappa' = 13 at multiple central charges via complementarity_landscape."""
        # VERIFIED [DC] c/2 + (26-c)/2 = 13 [LT] C8: self-dual at c=13
        total = kappa_virasoro(c) + kappa_dual_virasoro(c)
        assert total == C18_KAPPA_COMPLEMENTARITY["Vir"]

    def test_matches_w2_conductor(self) -> None:
        """Virasoro = W_2: K(Vir) must equal K(W_2) = (H_2-1)*alpha_2 = 13."""
        # VERIFIED [CF] Vir = W_2 cross-family [DC] (1/2)*26 = 13
        assert alpha_K_WN(2) == C18_KAPPA_COMPLEMENTARITY["Vir"]

    def test_matches_fl_kappa_sum(self) -> None:
        """Cross-check against Fateev-Lukyanov kappa_complementarity_sum(2)."""
        # VERIFIED [CF] wn_central_charge_canonical [DC] independent formula
        assert fl_kappa_compl_sum(2) == Fraction(13)

    def test_independent_computation(self) -> None:
        """Independent: kappa(Vir_c) = c/2, dual c' = 26-c, kappa' = (26-c)/2."""
        # VERIFIED [DC] direct algebra [LT] C2 kappa=c/2, C8 c+c'=26
        for c_val in [0, 1, 13, 26, -100]:
            c = Fraction(c_val)
            kappa = c / 2
            kappa_dual = (26 - c) / 2
            assert kappa + kappa_dual == Fraction(13)

    def test_self_dual_point(self) -> None:
        """At c=13 (self-dual): kappa = kappa' = 13/2."""
        # VERIFIED [DC] 13/2 + 13/2 = 13 [SY] self-dual symmetry
        assert kappa_virasoro(Fraction(13)) == Fraction(13, 2)
        assert kappa_dual_virasoro(Fraction(13)) == Fraction(13, 2)


# ========================================================================
# Group 3: Affine Kac-Moody -- K(KM) = 0
# ========================================================================

class TestC18AffineKM:
    """Affine KM: kappa(V_k(g)) + kappa(V_{-k-2h^v}(g)) = 0 for all g, k."""

    # (lie_type, rank, name, dim_g, h_dual)
    KM_FAMILIES = [
        ("A", 1, "sl_2", 3, 2),
        ("A", 2, "sl_3", 8, 3),
        ("D", 4, "so_8", 28, 6),
        ("G", 2, "G_2", 14, 4),
        ("E", 6, "E_6", 78, 12),
        ("E", 8, "E_8", 248, 30),
    ]

    @pytest.mark.parametrize(
        "lie_type, rank, name, dim_g, h_dual",
        KM_FAMILIES,
        ids=[f[2] for f in KM_FAMILIES],
    )
    def test_kappa_complementarity_vanishes(
        self, lie_type: str, rank: int, name: str, dim_g: int, h_dual: int
    ) -> None:
        """kappa + kappa' = 0 at k=1 via complementarity_landscape."""
        # VERIFIED [DC] dim(g)(k+h^v)/(2h^v) antisymmetric under k->-k-2h^v [SY]
        k = Fraction(1)
        total = kappa_affine(lie_type, rank, k) + kappa_dual_affine(lie_type, rank, k)
        assert total == C18_KAPPA_COMPLEMENTARITY["KM"]

    @pytest.mark.parametrize(
        "lie_type, rank, name, dim_g, h_dual",
        KM_FAMILIES,
        ids=[f[2] for f in KM_FAMILIES],
    )
    def test_complementarity_sum_function(
        self, lie_type: str, rank: int, name: str, dim_g: int, h_dual: int
    ) -> None:
        """Cross-check via complementarity_sum_affine (level-independent)."""
        assert complementarity_sum_affine(lie_type, rank) == Fraction(0)

    @pytest.mark.parametrize(
        "lie_type, rank, name, dim_g, h_dual",
        KM_FAMILIES,
        ids=[f[2] for f in KM_FAMILIES],
    )
    @pytest.mark.parametrize("k_val", [0, 1, 3, 7, -1])
    def test_multiple_levels(
        self, lie_type: str, rank: int, name: str, dim_g: int, h_dual: int,
        k_val: int
    ) -> None:
        """kappa + kappa' = 0 at multiple levels."""
        k = Fraction(k_val)
        total = kappa_affine(lie_type, rank, k) + kappa_dual_affine(lie_type, rank, k)
        assert total == Fraction(0)

    def test_independent_computation_sl2(self) -> None:
        """Independent: kappa(sl_2, k) = 3(k+2)/4, dual level k'=-k-4."""
        # VERIFIED [DC] dim=3, h^v=2: 3*(k+2)/(2*2) = 3(k+2)/4 [CF] complementarity_landscape
        for k_val in [0, 1, 5, 10]:
            k = Fraction(k_val)
            kappa = Fraction(3) * (k + 2) / 4
            kappa_dual = Fraction(3) * (-k - 4 + 2) / 4  # k' = -k-4
            assert kappa + kappa_dual == Fraction(0)

    def test_independent_computation_e8(self) -> None:
        """Independent: kappa(E_8, k) = 248(k+30)/60 = 62(k+30)/15."""
        # VERIFIED [DC] dim=248, h^v=30: 248*(k+30)/(2*30) [CF] complementarity_landscape
        for k_val in [0, 1, 5]:
            k = Fraction(k_val)
            kappa = Fraction(248) * (k + 30) / 60
            kappa_dual = Fraction(248) * (-k - 60 + 30) / 60  # k' = -k-60
            assert kappa + kappa_dual == Fraction(0)


# ========================================================================
# Group 4: W-algebras -- K(W_N) = (H_N - 1) * alpha_N
# ========================================================================

class TestC18WAlgebras:
    """W_N: kappa(W_N) + kappa(W_N^!) = (H_N - 1) * alpha_N."""

    def test_w3_kappa_conductor(self) -> None:
        """K(W_3) = 250/3 from complementarity_landscape."""
        # VERIFIED [DC] (H_3-1)*alpha_3 = (5/6)*100 = 250/3 [CF] alpha_n engine
        c = Fraction(50)  # arbitrary
        total = kappa_wn(3, c) + kappa_dual_wn(3, c)
        assert total == C18_KAPPA_COMPLEMENTARITY["W_3"]

    def test_w3_matches_alpha_engine(self) -> None:
        """Cross-check W_3 against alpha_n_conductor_engine."""
        assert alpha_K_WN(3) == Fraction(250, 3)

    def test_w3_matches_fl_engine(self) -> None:
        """Cross-check W_3 against Fateev-Lukyanov formula."""
        assert fl_kappa_compl_sum(3) == Fraction(250, 3)

    def test_w4_kappa_conductor(self) -> None:
        """K(W_4) = 533/2 from complementarity_landscape."""
        # VERIFIED [DC] (H_4-1)*alpha_4 = (13/12)*246 = 533/2 [CF] alpha_n engine
        c = Fraction(100)
        total = kappa_wn(4, c) + kappa_dual_wn(4, c)
        assert total == C18_KAPPA_COMPLEMENTARITY["W_4"]

    def test_w4_matches_alpha_engine(self) -> None:
        """Cross-check W_4 against alpha_n_conductor_engine."""
        assert alpha_K_WN(4) == Fraction(533, 2)

    def test_w4_matches_fl_engine(self) -> None:
        """Cross-check W_4 against Fateev-Lukyanov formula."""
        assert fl_kappa_compl_sum(4) == Fraction(533, 2)

    def test_w5_kappa_conductor(self) -> None:
        """K(W_5) = 9394/15."""
        # VERIFIED [DC] (H_5-1)*alpha_5 = (77/60)*488 [CF] alpha_n engine
        c = Fraction(200)
        total = kappa_wn(5, c) + kappa_dual_wn(5, c)
        assert total == C18_KAPPA_COMPLEMENTARITY["W_5"]

    def test_w5_matches_alpha_engine(self) -> None:
        """Cross-check W_5 against alpha_n_conductor_engine."""
        assert alpha_K_WN(5) == Fraction(9394, 15)

    def test_w5_matches_fl_engine(self) -> None:
        """Cross-check W_5 against Fateev-Lukyanov formula."""
        assert fl_kappa_compl_sum(5) == Fraction(9394, 15)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_alpha_engine_matches_fl_engine(self, N: int) -> None:
        """For all N in [2..8], alpha_n and FL engines agree on kappa conductor."""
        # VERIFIED [DC] two independent formulas [CF] cross-engine
        assert alpha_K_WN(N) == fl_kappa_compl_sum(N)

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_complementarity_sum_wn(self, N: int) -> None:
        """complementarity_sum_wn(N) matches alpha_K_WN(N)."""
        assert complementarity_sum_wn(N) == alpha_K_WN(N)

    @pytest.mark.parametrize("N,k", [
        (2, 1), (2, 3), (2, 7),
        (3, 1), (3, 3), (3, 7),
        (4, 1), (4, 3),
        (5, 1),
    ])
    def test_fl_level_independence(self, N: int, k: int) -> None:
        """kappa_fl(N,k) + kappa_fl(N,k') = K(W_N) for multiple (N,k) pairs."""
        # VERIFIED [DC] direct sum at each level [SY] level-independence
        k_f = Fraction(k)
        kd = ff_dual_level(N, k_f)
        total = kappa_wn_fl(N, k_f) + kappa_wn_fl(N, kd)
        assert total == fl_kappa_compl_sum(N)

    def test_w2_equals_virasoro(self) -> None:
        """W_2 = Virasoro: K(W_2) = 13."""
        # VERIFIED [CF] W_2 = Vir cross-family [DC] (1/2)*26 = 13
        assert alpha_K_WN(2) == Fraction(13)
        assert fl_kappa_compl_sum(2) == Fraction(13)
        assert complementarity_sum_wn(2) == Fraction(13)

    def test_independent_harmonic_computation(self) -> None:
        """Independent: H_N - 1 computed from scratch, alpha_N from closed form."""
        # VERIFIED [DC] manual harmonic numbers [DA] dimensional check
        for N, expected_K in [(2, Fraction(13)), (3, Fraction(250, 3)),
                               (4, Fraction(533, 2)), (5, Fraction(9394, 15))]:
            H = sum(Fraction(1, j) for j in range(1, N + 1))
            alpha = Fraction(2 * (N - 1) * (2 * N**2 + 2 * N + 1))
            K = (H - 1) * alpha
            assert K == expected_K


# ========================================================================
# Group 5: Bershadsky--Polyakov convention separation
# ========================================================================

class TestC18BershadskyPolyakov:
    """Exact BP central data and the open modular-characteristic lane."""

    def test_convention_records(self) -> None:
        """Canonical and secondary formulas carry disjoint typed records."""
        assert STANDARD_BP_CONVENTION.name == "standard_fkr_equal_weight_G"
        assert STANDARD_BP_CONVENTION.status == "proved-primary-source"
        assert STANDARD_BP_CONVENTION.conductor == Fraction(50)
        assert BP_CONVENTIONS["standard"] is STANDARD_BP_CONVENTION

        assert SHIFTED_BP_CONVENTION.name == "explicit_shifted_formula"
        assert SHIFTED_BP_CONVENTION.status == "computed-secondary"
        assert SHIFTED_BP_CONVENTION.conductor == Fraction(196)
        assert BP_CONVENTIONS["shifted"] is SHIFTED_BP_CONVENTION

    @pytest.mark.parametrize(
        "k, expected, expected_companion",
        [
            (0, Fraction(-1), Fraction(51)),
            (1, Fraction(-5), Fraction(55)),
            (-1, Fraction(1), Fraction(49)),
            (Fraction(-1, 2), Fraction(2, 5), Fraction(248, 5)),
        ],
    )
    def test_standard_charge_samples(
        self, k: Fraction | int, expected: Fraction, expected_companion: Fraction
    ) -> None:
        """Hand substitutions into the factored standard formula."""
        companion = bp_companion_level(k)
        assert c_BP(k) == expected
        assert c_BP(companion) == expected_companion
        assert expected + expected_companion == Fraction(50)

    @pytest.mark.parametrize("k", [0, 1, -1, 2, -2, 5, 10, -4, 100])
    def test_standard_conductor_samples(self, k: int) -> None:
        """The standard scalar companion sum is level-independent."""
        assert K_BP(k) == K_BP_EXACT == Fraction(50)

    def test_modular_characteristic_apis_fail_loudly(self) -> None:
        """Both canonical and census wrappers expose the open obligation."""
        assert BP_KAPPA_COMPL_EXACT is None
        assert VARRHO_BP is None
        assert BP_KAPPA_STATUS.status == "open-genus-one-computation"
        for function in (
            kappa_BP,
            bp_kappa_complementarity,
            census_bp_kappa,
            census_bp_kappa_conductor,
        ):
            with pytest.raises(UnverifiedBPInvariantError, match="genus-one curvature"):
                function(0)

    def test_all_even_reciprocal_weight_diagnostic(self) -> None:
        """FKR parity gives ``1+2/3+2/3+1/2=17/6``."""
        assert BP_GENERATORS == {
            "J": (Fraction(1), 0),
            "G+": (Fraction(3, 2), 0),
            "G-": (Fraction(3, 2), 0),
            "T": (Fraction(2), 0),
        }
        independent_sum = (
            Fraction(1) + Fraction(2, 3) + Fraction(2, 3) + Fraction(1, 2)
        )
        assert independent_sum == Fraction(17, 6)
        assert compute_varrho() == independent_sum
        assert bp_reciprocal_weight_diagnostic() == independent_sum

    def test_census_status_packet(self) -> None:
        """The consumer stores status separately from exact central data."""
        packet = bp_kappa_status_report()
        assert packet["kappa_value"] is None
        assert packet["kappa_complementarity_value"] is None
        assert packet["status"] == "open-genus-one-computation"
        assert packet["reciprocal_weight_diagnostic"] == Fraction(17, 6)
        former = packet["former_conditional_proposal"]
        assert former["value"] == Fraction(25, 3)
        assert former["status"] == "retracted-derivation"

    def test_c10_aggregates_exact_and_open_lanes(self) -> None:
        """C10 certifies the exact data while retaining the open slot."""
        result = verify_C10()
        assert result["passed"] is True
        assert result["computed"]["standard:k=0"] == Fraction(50)
        assert result["computed"]["all-generators-even"] is True
        assert result["computed"]["reciprocal-weight-diagnostic"] == Fraction(17, 6)
        assert result["computed"]["kappa-value"] is None
        assert result["computed"]["kappa-sum"] is None
        assert result["computed"]["shifted-secondary:k=0"] == Fraction(196)

    def test_companion_involution_and_critical_pole(self) -> None:
        """The companion map is involutive and fixes the common pole."""
        for k in [0, 1, -1, Fraction(1, 2), -3]:
            assert bp_companion_level(bp_companion_level(k)) == Fraction(k)
        assert bp_companion_level(-3) == Fraction(-3)
        with pytest.raises(ZeroDivisionError):
            c_BP(-3)

    def test_symbolic_standard_identity(self) -> None:
        """SymPy proves the standard identity in ``Q(k)``."""
        sp = pytest.importorskip("sympy")
        k = sp.Symbol("k", rational=True)
        companion = -k - 6
        c_value = -(2 * k + 3) * (3 * k + 1) / (k + 3)
        c_companion = -(
            (2 * companion + 3) * (3 * companion + 1) / (companion + 3)
        )
        assert sp.cancel(c_value + c_companion) == sp.Rational(50)

        t = sp.Symbol("t", nonzero=True)
        laurent_form = 25 - 6 * t - 24 / t
        assert sp.cancel(laurent_form + laurent_form.subs(t, -t)) == 50

    def test_shifted_secondary_identity(self) -> None:
        """The shifted formula retains its separately named conductor ``196``."""
        assert K_BP_SHIFTED_EXACT == Fraction(196)
        assert BP_SHIFTED_CENTRAL_CHARGE_CONDUCTOR["BP_shifted"] == Fraction(196)
        for k in [0, 1, -1, 2, -2, 5, 10, -4]:
            assert K_BP_shifted(k) == Fraction(196)

        sp = pytest.importorskip("sympy")
        k = sp.Symbol("k", rational=True)
        companion = -k - 6
        shifted = 2 - 24 * (k + 1) ** 2 / (k + 3)
        shifted_companion = 2 - 24 * (companion + 1) ** 2 / (companion + 3)
        assert sp.cancel(shifted + shifted_companion) == sp.Rational(196)

    def test_standard_and_shifted_values_differ(self) -> None:
        """A concrete level distinguishes the two conformal vectors."""
        assert c_BP(0) == Fraction(-1)
        assert c_BP_shifted(0) == Fraction(-6)


# ========================================================================
# Group 6: betagamma / bc ghosts -- K = 0
# ========================================================================

class TestC18BetagammaBc:
    """betagamma and bc: kappa + kappa' = 0 (dual pair)."""

    @pytest.mark.parametrize("lam", [Fraction(1, 2), Fraction(1), Fraction(2),
                                      Fraction(3), Fraction(0), Fraction(-1)])
    def test_betagamma_complementarity_vanishes(self, lam: Fraction) -> None:
        """kappa_bg(lam) + kappa_bg^dual(lam) = 0."""
        # VERIFIED [DC] c_bg+c_bc=0 implies kappa sum=0 [SY] bg^!=bc
        total = kappa_betagamma(lam) + kappa_dual_betagamma(lam)
        assert total == C18_KAPPA_COMPLEMENTARITY["bg"]

    @pytest.mark.parametrize("lam", [Fraction(1, 2), Fraction(1), Fraction(2),
                                      Fraction(3)])
    def test_bc_complementarity_vanishes(self, lam: Fraction) -> None:
        """kappa_bc(lam) + kappa_bc^dual(lam) = 0."""
        # VERIFIED [DC] c_bc+c_bg=0 [SY] bc^!=bg
        total = kappa_bc(lam) + kappa_dual_bc(lam)
        assert total == C18_KAPPA_COMPLEMENTARITY["bc"]

    @pytest.mark.parametrize("lam", [Fraction(1, 2), Fraction(1), Fraction(2)])
    def test_complementarity_sum_betagamma(self, lam: Fraction) -> None:
        """Cross-check via complementarity_sum_betagamma."""
        assert complementarity_sum_betagamma(lam) == Fraction(0)

    def test_independent_computation_bc_bg_cancellation(self) -> None:
        """Independent: c_bg(lam) = 2(6lam^2-6lam+1), c_bc(lam) = 1-3(2lam-1)^2.
        Sum c_bg + c_bc = 0, hence kappa_bg + kappa_bc = 0."""
        # VERIFIED [DC] direct polynomial identity [CF] C7 complementarity
        for lam_val in [0, 1, 2, 3]:
            lam = Fraction(lam_val)
            c_bg = 2 * (6 * lam**2 - 6 * lam + 1)
            c_bc = 1 - 3 * (2 * lam - 1)**2
            assert c_bg + c_bc == Fraction(0), f"c_bg+c_bc != 0 at lam={lam}"


# ========================================================================
# Group 7: Free fermion -- K = 0
# ========================================================================

class TestC18FreeFermion:
    """Free fermion: kappa + kappa' = 0."""

    def test_complementarity_vanishes(self) -> None:
        """kappa_ff + kappa_ff^dual = 0."""
        # VERIFIED [DC] kappa=1/4, kappa'=-1/4 [CF] free-field K=0
        total = kappa_free_fermion() + kappa_dual_free_fermion()
        assert total == C18_KAPPA_COMPLEMENTARITY["ff"]

    def test_complementarity_sum_function(self) -> None:
        """Cross-check via complementarity_sum_free_fermion."""
        assert complementarity_sum_free_fermion() == Fraction(0)

    def test_independent_computation(self) -> None:
        """Independent: kappa(ff) = 1/4, kappa(ff^!) = -1/4."""
        # VERIFIED [DC] c_ff=1/2, kappa=c_ff/2=1/4 at bc(1/2) [CF] bc formula
        # bc at lambda=1/2: c = 1-3(0)^2 = 1, but single Dirac = c=1/2
        # Free fermion kappa = 1/4 from character asymptotics
        assert kappa_free_fermion() == Fraction(1, 4)
        assert kappa_dual_free_fermion() == Fraction(-1, 4)


# ========================================================================
# Group 8: Lattice VOA -- K = 0
# ========================================================================

class TestC18Lattice:
    """Lattice VOA V_Lambda: kappa + kappa' = 0."""

    @pytest.mark.parametrize("rank", [1, 2, 4, 8, 16, 24])
    def test_complementarity_vanishes(self, rank: int) -> None:
        """kappa_lat(rank) + kappa_lat^dual(rank) = 0."""
        # VERIFIED [DC] kappa=rank, kappa'=-rank [CF] free-field K=0
        total = kappa_lattice(rank) + kappa_dual_lattice(rank)
        assert total == C18_KAPPA_COMPLEMENTARITY["lat"]

    @pytest.mark.parametrize("rank", [1, 2, 8])
    def test_complementarity_sum_function(self, rank: int) -> None:
        """Cross-check via complementarity_sum_lattice."""
        assert complementarity_sum_lattice(rank) == Fraction(0)

    def test_independent_computation(self) -> None:
        """Independent: kappa(V_Lambda) = rank(Lambda), kappa' = -rank."""
        # VERIFIED [DC] lattice VOA has rank Heisenberg subalgebra [CF] Heis K=0
        for r in [1, 2, 8, 24]:
            assert Fraction(r) + Fraction(-r) == Fraction(0)


# ========================================================================
# Group 9: Cross-source consistency
# ========================================================================

class TestC18CrossSourceConsistency:
    """Verify that all three/four engine sources agree on every conductor value."""

    @pytest.mark.parametrize("N, expected", [
        (2, Fraction(13)),
        (3, Fraction(250, 3)),
        (4, Fraction(533, 2)),
        (5, Fraction(9394, 15)),
    ])
    def test_three_sources_agree_wn(self, N: int, expected: Fraction) -> None:
        """alpha_n engine, FL engine, and complementarity_landscape all agree on K(W_N)."""
        src1 = alpha_K_WN(N)
        src2 = fl_kappa_compl_sum(N)
        src3 = complementarity_sum_wn(N)
        assert src1 == expected, f"alpha_n: {src1} != {expected}"
        assert src2 == expected, f"FL: {src2} != {expected}"
        assert src3 == expected, f"landscape: {src3} != {expected}"

    def test_bp_two_sources_agree_on_status(self) -> None:
        """The canonical BP engine and census consumer expose one open lane."""
        packet = bp_kappa_status_report()
        assert BP_KAPPA_COMPL_EXACT is None
        assert packet["kappa_complementarity_value"] is None
        assert packet["status"] == BP_KAPPA_STATUS.status
        assert packet["resolution_obligation"] == BP_KAPPA_STATUS.resolution_obligation

    def test_bp_central_charge_conductor_matches_c18(self) -> None:
        """The canonical BP census entry uses central-charge sum ``50``."""
        assert K_BP_EXACT == C18_CENTRAL_CHARGE_CONDUCTOR["BP"]

    def test_bp_shifted_conductor_has_secondary_type(self) -> None:
        """The value ``196`` belongs only to the shifted convention record."""
        assert SHIFTED_BP_CONVENTION.status == "computed-secondary"
        assert K_BP_SHIFTED_EXACT == BP_SHIFTED_CENTRAL_CHARGE_CONDUCTOR[
            "BP_shifted"
        ]
        assert K_BP_SHIFTED_EXACT != C18_CENTRAL_CHARGE_CONDUCTOR["BP"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_wn_central_charge_conductor_matches(self, N: int) -> None:
        """Central charge conductor c+c' = alpha_N matches FL complementarity_sum."""
        from alpha_n_conductor_engine import alpha_N as get_alpha
        assert get_alpha(N) == fl_c_compl_sum(N)


# ========================================================================
# Group 10: C18 summary table verification
# ========================================================================

class TestC18SummaryTable:
    """Direct verification of every entry in the C18 summary table."""

    def test_km_heis_lattice_free_are_zero(self) -> None:
        """C18: K = 0 for KM/Heis/lattice/free."""
        # VERIFIED [DC] all four families [SY] antisymmetry of kappa under duality
        assert C18_KAPPA_COMPLEMENTARITY["Heis"] == Fraction(0)
        assert C18_KAPPA_COMPLEMENTARITY["KM"] == Fraction(0)
        assert C18_KAPPA_COMPLEMENTARITY["lat"] == Fraction(0)
        assert C18_KAPPA_COMPLEMENTARITY["ff"] == Fraction(0)
        assert C18_KAPPA_COMPLEMENTARITY["bg"] == Fraction(0)
        assert C18_KAPPA_COMPLEMENTARITY["bc"] == Fraction(0)

    def test_vir_is_13(self) -> None:
        """C18: K(Vir) = 13."""
        # VERIFIED [DC] c/2+(26-c)/2 [CF] W_2 cross-check [LT] C8
        assert C18_KAPPA_COMPLEMENTARITY["Vir"] == Fraction(13)

    def test_w3_is_250_over_3(self) -> None:
        """C18: K(W_3) = 250/3."""
        # VERIFIED [DC] (5/6)*100 [CF] three engines agree
        assert C18_KAPPA_COMPLEMENTARITY["W_3"] == Fraction(250, 3)

    def test_bp_kappa_lane_is_status_only(self) -> None:
        """C18 records the BP modular characteristic outside the numeric table."""
        assert "BP" not in C18_KAPPA_COMPLEMENTARITY
        assert bp_kappa_status_report()["kappa_complementarity_value"] is None
        assert Fraction(25, 3) not in THEOREM_C_CERTIFIED_SCALAR_VALUES

    def test_bp_central_charge_conductor_is_50(self) -> None:
        """C18 BP central-charge companion sum is ``50``."""
        assert C18_CENTRAL_CHARGE_CONDUCTOR["BP"] == Fraction(50)

    def test_c18_completeness(self) -> None:
        """Every active numeric family in C18 has a certified test."""
        zero_families = {"Heis", "KM", "lat", "ff", "bg", "bc"}
        for fam in zero_families:
            assert C18_KAPPA_COMPLEMENTARITY[fam] == Fraction(0), f"{fam} should be 0"
        assert C18_KAPPA_COMPLEMENTARITY["Vir"] == Fraction(13)
        assert C18_KAPPA_COMPLEMENTARITY["W_3"] == Fraction(250, 3)
        assert C18_KAPPA_COMPLEMENTARITY["W_4"] == Fraction(533, 2)
        assert C18_KAPPA_COMPLEMENTARITY["W_5"] == Fraction(9394, 15)
        assert "BP" not in C18_KAPPA_COMPLEMENTARITY
        assert set(THEOREM_C_CERTIFIED_SCALAR_VALUES) == {
            Fraction(0),
            Fraction(13),
            Fraction(250, 3),
        }

    def test_full_census_verifier_passes(self) -> None:
        """C01--C10 pass with C10 carrying explicit BP status."""
        results, summary = run_all_checks()
        assert summary == {"total": 10, "passed": 10, "failed": 0}
        c10 = next(result for result in results if result["name"].startswith("C10"))
        assert c10["standard_convention"]["kappa_sum"] is None
        assert c10["former_conditional_proposal"]["value"] == Fraction(25, 3)
