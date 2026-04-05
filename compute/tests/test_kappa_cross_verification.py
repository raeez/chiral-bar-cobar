r"""Cross-verification tests for kappa(A) across FIVE independent methods.

kappa(A) is the single most important invariant in the modular Koszul duality
programme. It has been wrong 19 times in project history (AP1). This test suite
provides FIVE independent computation paths for every kappa value.

FIVE METHODS:
  M1: Genus-1 bar complex (F_1 = kappa/24)
  M2: OPE residue / Killing form
  M3: Character / partition function asymptotics
  M4: Shadow metric (Q_L(0) = 4*kappa^2)
  M5: Complementarity (kappa + kappa' = constant)

ALL FIVE MUST AGREE. Any disagreement is a bug.

Organization:
  1. Per-family method agreement (85+ tests)
  2. Manuscript cross-check (17+ tests)
  3. Complementarity sum verification (15+ tests)
  4. Additivity verification (10+ tests)
  5. DS reduction verification (5+ tests)
  6. Edge case / limiting value tests (10+ tests)
  7. Non-simply-laced families (12+ tests)

Total: 150+ tests.
"""

import pytest
from sympy import Rational, simplify, S, oo, Symbol


from compute.lib.kappa_cross_verification import (
    verify_kappa,
    kappa_method1_genus1,
    kappa_method2_ope,
    kappa_method3_character,
    kappa_method4_shadow_metric,
    kappa_method5_complementarity,
    complementarity_sum,
    verify_additivity,
    verify_ds_reduction,
    verify_manuscript_values,
    full_landscape_verification,
    _get_lie_data,
    LAMBDA_FP,
)


def _eq(a, b):
    """Compare two sympy/Rational values for equality."""
    if a is None or b is None:
        return a is None and b is None
    return simplify(S(a) - S(b)) == 0


# ============================================================================
# Section 1: Per-family 5-method agreement
# ============================================================================

class TestHeisenbergFiveMethods:
    """Heisenberg H_k: kappa = k."""

    @pytest.mark.parametrize("k", [1, 2, 3, -1, Rational(1, 2), Rational(7, 3)])
    def test_all_methods_agree(self, k):
        r = verify_kappa("heisenberg", k=k)
        assert r.all_agree, f"Methods disagree for Heis k={k}: {r.disagreements}"
        assert _eq(r.kappa_value, k), f"Expected kappa={k}, got {r.kappa_value}"

    def test_method1_genus1(self):
        assert _eq(kappa_method1_genus1("heisenberg", k=1), 1)
        assert _eq(kappa_method1_genus1("heisenberg", k=3), 3)

    def test_method2_ope(self):
        assert _eq(kappa_method2_ope("heisenberg", k=1), 1)
        assert _eq(kappa_method2_ope("heisenberg", k=-2), -2)

    def test_method3_character(self):
        assert _eq(kappa_method3_character("heisenberg", k=1), 1)

    def test_method4_shadow(self):
        assert _eq(kappa_method4_shadow_metric("heisenberg", k=1), 1)

    def test_method5_complementarity(self):
        assert _eq(kappa_method5_complementarity("heisenberg", k=1), 1)
        assert _eq(kappa_method5_complementarity("heisenberg", k=-3), -3)


class TestVirasoroFiveMethods:
    """Virasoro Vir_c: kappa = c/2."""

    @pytest.mark.parametrize("c", [1, 2, Rational(1, 2), Rational(7, 10), 13, 25, 26])
    def test_all_methods_agree(self, c):
        r = verify_kappa("virasoro", c=c)
        assert r.all_agree, f"Methods disagree for Vir c={c}: {r.disagreements}"
        assert _eq(r.kappa_value, c / 2), f"Expected kappa={c/2}, got {r.kappa_value}"

    def test_self_dual_point(self):
        """At c=13, kappa = 13/2 and kappa' = 13/2 (self-dual point)."""
        r = verify_kappa("virasoro", c=13)
        assert _eq(r.kappa_value, Rational(13, 2))

    def test_critical_string(self):
        """At c=26, kappa = 13 and kappa' = 0."""
        r = verify_kappa("virasoro", c=26)
        assert _eq(r.kappa_value, 13)

    def test_minimal_model_values(self):
        """Minimal model central charges: c(p,q) = 1 - 6(p-q)^2/(pq)."""
        # c(3,2) = 1/2 (Ising): kappa = 1/4
        r = verify_kappa("virasoro", c=Rational(1, 2))
        assert _eq(r.kappa_value, Rational(1, 4))
        # c(4,3) = 7/10 (tricritical Ising): kappa = 7/20
        r = verify_kappa("virasoro", c=Rational(7, 10))
        assert _eq(r.kappa_value, Rational(7, 20))


class TestAffineSl2FiveMethods:
    """Affine sl_2 at level k: kappa = 3(k+2)/4."""

    @pytest.mark.parametrize("k", [1, 2, 3, -1, Rational(1, 2)])
    def test_all_methods_agree(self, k):
        r = verify_kappa("affine", lie_type="A", rank=1, k=k)
        expected = Rational(3) * (k + 2) / 4
        assert r.all_agree, f"Methods disagree for sl_2 k={k}: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_k1_matches_census(self):
        """At k=1: kappa = 3*3/4 = 9/4."""
        r = verify_kappa("affine", lie_type="A", rank=1, k=1)
        assert _eq(r.kappa_value, Rational(9, 4))


class TestAffineSl3FiveMethods:
    """Affine sl_3 at level k: kappa = 8(k+3)/6 = 4(k+3)/3."""

    @pytest.mark.parametrize("k", [1, 2, -1])
    def test_all_methods_agree(self, k):
        r = verify_kappa("affine", lie_type="A", rank=2, k=k)
        expected = Rational(8) * (Rational(k) + 3) / 6
        assert r.all_agree, f"Methods disagree for sl_3 k={k}: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_k1_matches_census(self):
        """At k=1: kappa = 8*4/6 = 32/6 = 16/3."""
        r = verify_kappa("affine", lie_type="A", rank=2, k=1)
        assert _eq(r.kappa_value, Rational(16, 3))


class TestAffineSlNFiveMethods:
    """Affine sl_N at level k: kappa = (N^2-1)(k+N)/(2N)."""

    @pytest.mark.parametrize("N", [4, 5, 6, 7, 8, 9])
    def test_k1_all_methods_agree(self, N):
        r = verify_kappa("affine", lie_type="A", rank=N - 1, k=1)
        expected = Rational(N**2 - 1) * (1 + N) / (2 * N)
        assert r.all_agree, f"Methods disagree for sl_{N} k=1: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"


class TestAffineBnFiveMethods:
    """Affine so_{2n+1} (type B_n): kappa = n(2n+1)(k+2n-1)/(2(2n-1))."""

    @pytest.mark.parametrize("n", [2, 3, 4, 5])
    def test_k1_all_methods_agree(self, n):
        r = verify_kappa("affine", lie_type="B", rank=n, k=1)
        dim_g = n * (2 * n + 1)
        h_dual = 2 * n - 1
        expected = Rational(dim_g) * (1 + h_dual) / (2 * h_dual)
        assert r.all_agree, f"Methods disagree for B_{n} k=1: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_B2_k1_explicit(self):
        """B_2 = so_5: dim=10, h^v=3. kappa = 10*(1+3)/(2*3) = 40/6 = 20/3."""
        r = verify_kappa("affine", lie_type="B", rank=2, k=1)
        assert _eq(r.kappa_value, Rational(20, 3))

    def test_B2_equals_C2(self):
        """B_2 and C_2 are isomorphic (so_5 = sp_4), same kappa."""
        r_b = verify_kappa("affine", lie_type="B", rank=2, k=1)
        r_c = verify_kappa("affine", lie_type="C", rank=2, k=1)
        assert _eq(r_b.kappa_value, r_c.kappa_value), (
            f"B_2 kappa={r_b.kappa_value} != C_2 kappa={r_c.kappa_value}"
        )


class TestAffineCnFiveMethods:
    """Affine sp_{2n} (type C_n): kappa = n(2n+1)(k+n+1)/(2(n+1))."""

    @pytest.mark.parametrize("n", [2, 3, 4])
    def test_k1_all_methods_agree(self, n):
        r = verify_kappa("affine", lie_type="C", rank=n, k=1)
        dim_g = n * (2 * n + 1)
        h_dual = n + 1
        expected = Rational(dim_g) * (1 + h_dual) / (2 * h_dual)
        assert r.all_agree, f"Methods disagree for C_{n} k=1: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_C3_k1_explicit(self):
        """C_3 = sp_6: dim=21, h^v=4. kappa = 21*(1+4)/(2*4) = 105/8."""
        r = verify_kappa("affine", lie_type="C", rank=3, k=1)
        assert _eq(r.kappa_value, Rational(105, 8))


class TestAffineDnFiveMethods:
    """Affine so_{2n} (type D_n): kappa = n(2n-1)(k+2n-2)/(2(2n-2))."""

    @pytest.mark.parametrize("n", [4, 5, 6])
    def test_k1_all_methods_agree(self, n):
        r = verify_kappa("affine", lie_type="D", rank=n, k=1)
        dim_g = n * (2 * n - 1)
        h_dual = 2 * n - 2
        expected = Rational(dim_g) * (1 + h_dual) / (2 * h_dual)
        assert r.all_agree, f"Methods disagree for D_{n} k=1: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_D4_k1_explicit(self):
        """D_4 = so_8: dim=28, h^v=6. kappa = 28*(1+6)/(2*6) = 196/12 = 49/3."""
        r = verify_kappa("affine", lie_type="D", rank=4, k=1)
        assert _eq(r.kappa_value, Rational(49, 3))


class TestAffineG2FiveMethods:
    """Affine G_2: dim=14, h^v=4. kappa = 14*(k+4)/(2*4) = 7(k+4)/4."""

    @pytest.mark.parametrize("k", [1, 2])
    def test_all_methods_agree(self, k):
        r = verify_kappa("affine", lie_type="G", rank=2, k=k)
        expected = Rational(7) * (k + 4) / 4
        assert r.all_agree, f"Methods disagree for G_2 k={k}: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_k1_matches_census(self):
        """At k=1: kappa = 7*5/4 = 35/4."""
        r = verify_kappa("affine", lie_type="G", rank=2, k=1)
        assert _eq(r.kappa_value, Rational(35, 4))


class TestAffineF4FiveMethods:
    """Affine F_4: dim=52, h^v=9. kappa = 52*(k+9)/(2*9) = 26(k+9)/9."""

    def test_k1_all_methods_agree(self):
        r = verify_kappa("affine", lie_type="F", rank=4, k=1)
        expected = Rational(26) * 10 / 9
        assert r.all_agree, f"Methods disagree for F_4 k=1: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_k1_explicit(self):
        """At k=1: kappa = 26*10/9 = 260/9."""
        r = verify_kappa("affine", lie_type="F", rank=4, k=1)
        assert _eq(r.kappa_value, Rational(260, 9))


class TestAffineE6FiveMethods:
    """Affine E_6: dim=78, h^v=12. kappa = 78*(k+12)/(2*12) = 13(k+12)/4."""

    def test_k1_all_methods_agree(self):
        r = verify_kappa("affine", lie_type="E", rank=6, k=1)
        expected = Rational(13) * 13 / 4
        assert r.all_agree, f"Methods disagree for E_6 k=1: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_k1_explicit(self):
        """At k=1: kappa = 13*13/4 = 169/4."""
        r = verify_kappa("affine", lie_type="E", rank=6, k=1)
        assert _eq(r.kappa_value, Rational(169, 4))


class TestAffineE7FiveMethods:
    """Affine E_7: dim=133, h^v=18. kappa = 133*(k+18)/(2*18) = 133(k+18)/36."""

    def test_k1_all_methods_agree(self):
        r = verify_kappa("affine", lie_type="E", rank=7, k=1)
        expected = Rational(133) * 19 / 36
        assert r.all_agree, f"Methods disagree for E_7 k=1: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_k1_explicit(self):
        """At k=1: kappa = 133*19/36 = 2527/36."""
        r = verify_kappa("affine", lie_type="E", rank=7, k=1)
        assert _eq(r.kappa_value, Rational(2527, 36))


class TestAffineE8FiveMethods:
    """Affine E_8: dim=248, h^v=30. kappa = 248*(k+30)/(2*30) = 124(k+30)/30 = 62(k+30)/15."""

    def test_k1_all_methods_agree(self):
        r = verify_kappa("affine", lie_type="E", rank=8, k=1)
        expected = Rational(62) * 31 / 15
        assert r.all_agree, f"Methods disagree for E_8 k=1: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_k1_matches_census(self):
        """At k=1: kappa = 62*31/15 = 1922/15."""
        r = verify_kappa("affine", lie_type="E", rank=8, k=1)
        assert _eq(r.kappa_value, Rational(1922, 15))


class TestW3FiveMethods:
    """W_3: kappa = 5c/6."""

    @pytest.mark.parametrize("c", [2, Rational(1, 2), 50, 100])
    def test_all_methods_agree(self, c):
        r = verify_kappa("w3", c=c)
        expected = Rational(5) * c / 6
        assert r.all_agree, f"Methods disagree for W_3 c={c}: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"


class TestWNFiveMethods:
    """W_N: kappa = (H_N - 1) * c."""

    def test_w4_all_methods_agree(self):
        # H_4 - 1 = 1/2 + 1/3 + 1/4 = 13/12
        r = verify_kappa("wn", N=4, c=2)
        expected = Rational(13, 12) * 2
        assert r.all_agree, f"Methods disagree for W_4: {r.disagreements}"
        assert _eq(r.kappa_value, expected)

    def test_w5_all_methods_agree(self):
        # H_5 - 1 = 1/2 + 1/3 + 1/4 + 1/5 = 77/60
        r = verify_kappa("wn", N=5, c=2)
        expected = Rational(77, 60) * 2
        assert r.all_agree, f"Methods disagree for W_5: {r.disagreements}"
        assert _eq(r.kappa_value, expected)

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: H_2 - 1 = 1/2, kappa = c/2."""
        r = verify_kappa("wn", N=2, c=10)
        assert _eq(r.kappa_value, 5), f"W_2 at c=10: expected kappa=5, got {r.kappa_value}"

    def test_w3_consistency(self):
        """W_3 via W_N formula agrees with dedicated W_3 formula."""
        c_val = Rational(6)
        r_wn = verify_kappa("wn", N=3, c=c_val)
        r_w3 = verify_kappa("w3", c=c_val)
        assert _eq(r_wn.kappa_value, r_w3.kappa_value), (
            f"W_N(N=3) gives {r_wn.kappa_value}, W_3 gives {r_w3.kappa_value}"
        )


class TestBetagammaFiveMethods:
    """betagamma at weight lambda: kappa = 6*lam^2 - 6*lam + 1."""

    @pytest.mark.parametrize("lam", [0, 1, Rational(1, 2), 2])
    def test_all_methods_agree(self, lam):
        r = verify_kappa("betagamma", lam=lam)
        expected = 6 * Rational(lam)**2 - 6 * Rational(lam) + 1
        assert r.all_agree, f"Methods disagree for bg lam={lam}: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_standard_betagamma(self):
        """At lambda=1: kappa = 6-6+1 = 1."""
        r = verify_kappa("betagamma", lam=1)
        assert _eq(r.kappa_value, 1)

    def test_symplectic_betagamma(self):
        """At lambda=1/2: kappa = 6/4-3+1 = 3/2-3+1 = -1/2."""
        r = verify_kappa("betagamma", lam=Rational(1, 2))
        assert _eq(r.kappa_value, Rational(-1, 2))

    def test_bc_betagamma_duality(self):
        """kappa(bg, lam) + kappa(bc, 1-lam) = 0."""
        for lam_val in [0, 1, Rational(1, 2), 2]:
            kb = kappa_method2_ope("betagamma", lam=lam_val)
            kc = kappa_method2_ope("bc", spin=1 - Rational(lam_val))
            assert _eq(kb + kc, 0), (
                f"bg(lam={lam_val}) + bc(spin={1-Rational(lam_val)}) = "
                f"{kb} + {kc} = {kb+kc} != 0"
            )


class TestBcGhostsFiveMethods:
    """bc ghosts at spin j: kappa = -(6j^2 - 6j + 1)."""

    @pytest.mark.parametrize("j", [0, 1, 2, Rational(1, 2)])
    def test_all_methods_agree(self, j):
        r = verify_kappa("bc", spin=j)
        expected = -(6 * Rational(j)**2 - 6 * Rational(j) + 1)
        assert r.all_agree, f"Methods disagree for bc j={j}: {r.disagreements}"
        assert _eq(r.kappa_value, expected), f"Expected {expected}, got {r.kappa_value}"

    def test_conformal_ghosts(self):
        """At j=2 (conformal ghosts b_2 c_{-1}): kappa = -(24-12+1) = -13."""
        r = verify_kappa("bc", spin=2)
        assert _eq(r.kappa_value, -13)


class TestFreeFermionFiveMethods:
    """Free fermion psi: kappa = 1/4."""

    def test_all_methods_agree(self):
        r = verify_kappa("free_fermion")
        assert r.all_agree, f"Methods disagree: {r.disagreements}"
        assert _eq(r.kappa_value, Rational(1, 4))


class TestLatticeFiveMethods:
    """Lattice VOA V_Lambda: kappa = rank(Lambda)."""

    @pytest.mark.parametrize("rank", [1, 4, 8, 16, 24])
    def test_all_methods_agree(self, rank):
        r = verify_kappa("lattice", rank=rank)
        assert r.all_agree, f"Methods disagree for lattice rank={rank}: {r.disagreements}"
        assert _eq(r.kappa_value, rank)

    def test_D4_lattice(self):
        r = verify_kappa("lattice", rank=4)
        assert _eq(r.kappa_value, 4)

    def test_E8_lattice(self):
        r = verify_kappa("lattice", rank=8)
        assert _eq(r.kappa_value, 8)

    def test_Leech_lattice(self):
        r = verify_kappa("lattice", rank=24)
        assert _eq(r.kappa_value, 24)


# ============================================================================
# Section 2: Manuscript cross-check
# ============================================================================

class TestManuscriptValues:
    """Verify against the authoritative values in landscape_census.tex."""

    def test_all_manuscript_values(self):
        results = verify_manuscript_values()
        for label, agree, computed, expected in results:
            assert agree, f"{label}: computed {computed} != expected {expected}"

    def test_free_fermion_kappa_quarter(self):
        """Tab:free-energy-landscape: free fermion kappa = 1/4."""
        assert _eq(kappa_method2_ope("free_fermion"), Rational(1, 4))

    def test_bc_ghosts_lambda0_kappa_minus1(self):
        """Tab:free-energy-landscape: bc ghosts (lambda=0) kappa = -1."""
        assert _eq(kappa_method2_ope("bc", spin=0), -1)

    def test_betagamma_lambda1_kappa_1(self):
        """Tab:free-energy-landscape: betagamma (lambda=1) kappa = 1."""
        assert _eq(kappa_method2_ope("betagamma", lam=1), 1)

    def test_betagamma_lambda_half_kappa_minus_half(self):
        """Tab:free-energy-landscape: betagamma (lambda=1/2) kappa = -1/2."""
        assert _eq(kappa_method2_ope("betagamma", lam=Rational(1, 2)), Rational(-1, 2))

    def test_heisenberg_k1_kappa_1(self):
        """Tab:free-energy-landscape: H_1 kappa = 1."""
        assert _eq(kappa_method2_ope("heisenberg", k=1), 1)

    def test_sl2_k1_kappa_9_4(self):
        """Tab:free-energy-landscape: sl_2 at k=1, kappa = 9/4."""
        assert _eq(kappa_method2_ope("affine", lie_type="A", rank=1, k=1), Rational(9, 4))

    def test_sl3_k1_kappa_16_3(self):
        """Tab:free-energy-landscape: sl_3 at k=1, kappa = 16/3."""
        assert _eq(kappa_method2_ope("affine", lie_type="A", rank=2, k=1), Rational(16, 3))

    def test_G2_k1_kappa_35_4(self):
        """Tab:free-energy-landscape: G_2 at k=1, kappa = 35/4."""
        assert _eq(kappa_method2_ope("affine", lie_type="G", rank=2, k=1), Rational(35, 4))

    def test_E8_k1_kappa_1922_15(self):
        """Tab:free-energy-landscape: E_8 at k=1, kappa = 1922/15."""
        assert _eq(kappa_method2_ope("affine", lie_type="E", rank=8, k=1), Rational(1922, 15))

    def test_virasoro_kappa_c_over_2(self):
        """Tab:free-energy-landscape: Vir_c, kappa = c/2."""
        assert _eq(kappa_method2_ope("virasoro", c=26), 13)

    def test_w3_kappa_5c_over_6(self):
        """Tab:free-energy-landscape: W_3, kappa = 5c/6."""
        assert _eq(kappa_method2_ope("w3", c=6), 5)

    def test_lattice_D4_kappa_4(self):
        """Tab:free-energy-landscape: V_{D_4}, kappa = 4."""
        assert _eq(kappa_method2_ope("lattice", rank=4), 4)

    def test_lattice_E8_kappa_8(self):
        """Tab:free-energy-landscape: V_{E_8}, kappa = 8."""
        assert _eq(kappa_method2_ope("lattice", rank=8), 8)

    def test_lattice_Leech_kappa_24(self):
        """Tab:free-energy-landscape: Leech V_Lambda, kappa = 24."""
        assert _eq(kappa_method2_ope("lattice", rank=24), 24)

    def test_F1_equals_kappa_over_24(self):
        """Verify F_1 = kappa/24 for all families with explicit kappa."""
        for (fam, params_tuple), kappa_expected in [
            (("free_fermion", ()), Rational(1, 4)),
            (("heisenberg", ("k", 1)), Rational(1)),
            (("virasoro", ("c", 26)), Rational(13)),
        ]:
            # Parse params_tuple back to kwargs
            if params_tuple:
                kwargs = {params_tuple[0]: params_tuple[1]}
            else:
                kwargs = {}
            m1 = kappa_method1_genus1(fam, **kwargs)
            assert _eq(m1, kappa_expected), (
                f"{fam}({kwargs}): genus-1 gives kappa={m1}, expected {kappa_expected}"
            )


# ============================================================================
# Section 3: Complementarity sum verification
# ============================================================================

class TestComplementaritySums:
    """Verify kappa(A) + kappa(A!) is level-independent."""

    def test_heisenberg_sum_zero(self):
        """Heisenberg: kappa + kappa' = 0."""
        for k_val in [1, 2, 3, -1, Rational(1, 2)]:
            s = complementarity_sum("heisenberg", k=k_val)
            assert _eq(s, 0), f"Heis k={k_val}: sum = {s} != 0"

    def test_virasoro_sum_13(self):
        """Virasoro: kappa + kappa' = 13 (AP24)."""
        for c_val in [1, 2, 13, 25, 26, Rational(1, 2)]:
            s = complementarity_sum("virasoro", c=c_val)
            assert _eq(s, 13), f"Vir c={c_val}: sum = {s} != 13"

    def test_affine_sum_zero(self):
        """Affine KM: kappa + kappa' = 0 (FF involution)."""
        test_cases = [
            ("A", 1, 1), ("A", 1, 2), ("A", 2, 1),
            ("B", 2, 1), ("C", 2, 1),
            ("G", 2, 1), ("F", 4, 1),
            ("E", 6, 1), ("E", 7, 1), ("E", 8, 1),
        ]
        for type_, rank, k_val in test_cases:
            s = complementarity_sum("affine", lie_type=type_, rank=rank, k=k_val)
            assert _eq(s, 0), f"Affine ({type_},{rank}) k={k_val}: sum = {s} != 0"

    def test_betagamma_bc_sum_zero(self):
        """betagamma/bc pairs: kappa + kappa' = 0."""
        for lam_val in [0, 1, Rational(1, 2), 2]:
            s = complementarity_sum("betagamma", lam=lam_val)
            assert _eq(s, 0), f"bg(lam={lam_val}): sum = {s} != 0"

    def test_w3_sum_250_over_3(self):
        """W_3: kappa + kappa' = 250/3."""
        for c_val in [2, 50, Rational(1, 2)]:
            s = complementarity_sum("w3", c=c_val)
            assert _eq(s, Rational(250, 3)), f"W_3 c={c_val}: sum = {s} != 250/3"

    def test_lattice_sum_zero(self):
        """Lattice VOAs: kappa + kappa' = 0."""
        for rank_val in [1, 4, 8, 24]:
            s = complementarity_sum("lattice", rank=rank_val)
            assert _eq(s, 0), f"Lattice rank={rank_val}: sum = {s} != 0"

    def test_virasoro_not_zero(self):
        """CRITICAL (AP24): Virasoro sum is 13, NOT 0."""
        s = complementarity_sum("virasoro", c=10)
        assert not _eq(s, 0), "Virasoro sum should NOT be 0 (AP24)"
        assert _eq(s, 13), f"Virasoro sum should be 13, got {s}"

    def test_complementarity_level_independent_affine(self):
        """Verify sum is the same at different levels for affine sl_2."""
        sums = []
        for k_val in [1, 2, 3, 5, 10, -1, Rational(1, 2)]:
            s = complementarity_sum("affine", lie_type="A", rank=1, k=k_val)
            sums.append(s)
        # All should be 0
        for s in sums:
            assert _eq(s, 0)

    def test_complementarity_level_independent_virasoro(self):
        """Verify sum is the same at different c values for Virasoro."""
        sums = []
        for c_val in [1, 5, 13, 25, 26, -10, Rational(7, 10)]:
            s = complementarity_sum("virasoro", c=c_val)
            sums.append(s)
        # All should be 13
        for s in sums:
            assert _eq(s, 13)


# ============================================================================
# Section 4: Additivity verification
# ============================================================================

class TestAdditivity:
    """Verify kappa(A tensor B) = kappa(A) + kappa(B)."""

    def test_heisenberg_additive(self):
        """Two Heisenberg at levels k1, k2: kappa = k1 + k2."""
        k1, k2 = 3, 5
        agree, ka, kb, ks = verify_additivity(
            "heisenberg", {"k": k1},
            "heisenberg", {"k": k2},
        )
        assert _eq(ks, k1 + k2)

    def test_lattice_is_sum_of_heisenberg(self):
        """Lattice of rank d = d copies of Heisenberg at level 1."""
        for d in [4, 8, 24]:
            kappa_lattice = kappa_method2_ope("lattice", rank=d)
            kappa_sum = d * kappa_method2_ope("heisenberg", k=1)
            assert _eq(kappa_lattice, kappa_sum), (
                f"Lattice rank={d}: kappa={kappa_lattice} != {d}*kappa(H_1)={kappa_sum}"
            )

    def test_betagamma_plus_bc_zero(self):
        """betagamma + bc at complementary weights: kappa = 0."""
        for lam_val in [0, 1, Rational(1, 2)]:
            j_val = 1 - Rational(lam_val)
            agree, ka, kb, ks = verify_additivity(
                "betagamma", {"lam": lam_val},
                "bc", {"spin": j_val},
            )
            assert _eq(ks, 0), (
                f"bg(lam={lam_val}) + bc(spin={j_val}): kappa = {ks} != 0"
            )

    def test_two_virasoro(self):
        """Two Virasoros: kappa = c1/2 + c2/2."""
        c1, c2 = 10, 16
        agree, ka, kb, ks = verify_additivity(
            "virasoro", {"c": c1},
            "virasoro", {"c": c2},
        )
        assert _eq(ks, Rational(c1 + c2, 2))

    def test_affine_plus_fermion(self):
        """sl_2 + fermion: kappa = 3(k+2)/4 + 1/4."""
        k_val = 1
        agree, ka, kb, ks = verify_additivity(
            "affine", {"lie_type": "A", "rank": 1, "k": k_val},
            "free_fermion", {},
        )
        expected = Rational(3) * (k_val + 2) / 4 + Rational(1, 4)
        assert _eq(ks, expected)

    def test_three_heisenberg_commutative_associative(self):
        """Additivity is commutative and associative."""
        k1, k2, k3 = 2, 3, 5
        # (k1 + k2) + k3
        s12 = kappa_method2_ope("heisenberg", k=k1) + kappa_method2_ope("heisenberg", k=k2)
        s123a = s12 + kappa_method2_ope("heisenberg", k=k3)
        # k1 + (k2 + k3)
        s23 = kappa_method2_ope("heisenberg", k=k2) + kappa_method2_ope("heisenberg", k=k3)
        s123b = kappa_method2_ope("heisenberg", k=k1) + s23
        assert _eq(s123a, s123b)
        assert _eq(s123a, k1 + k2 + k3)


# ============================================================================
# Section 5: DS reduction verification
# ============================================================================

class TestDSReduction:
    """Verify kappa(W_N) = sigma(sl_N) * c through the DS formula."""

    def test_virasoro_ds_from_sl2(self):
        """Virasoro = W(sl_2): sigma(sl_2) = 1/2, kappa = c/2."""
        # sigma(sl_2) = 1/(1+1) = 1/2
        # kappa(Vir, c) = (1/2)*c
        kappa_vir = kappa_method2_ope("virasoro", c=10)
        assert _eq(kappa_vir, Rational(1, 2) * 10)

    def test_w3_ds_from_sl3(self):
        """W_3 = W(sl_3): sigma(sl_3) = 1/2 + 1/3 = 5/6, kappa = 5c/6."""
        kappa_w3 = kappa_method2_ope("w3", c=6)
        assert _eq(kappa_w3, Rational(5, 6) * 6)

    def test_w4_sigma(self):
        """W_4 = W(sl_4): sigma(sl_4) = 1/2+1/3+1/4 = 13/12."""
        kappa_w4 = kappa_method2_ope("wn", N=4, c=12)
        assert _eq(kappa_w4, Rational(13, 12) * 12)
        assert _eq(kappa_w4, 13)

    def test_sigma_monotone_increasing(self):
        """sigma(sl_N) = H_N - 1 is strictly increasing in N."""
        prev = Rational(0)
        for N in range(2, 20):
            sigma = sum(Rational(1, i) for i in range(2, N + 1))
            assert sigma > prev, f"sigma not increasing: sigma(sl_{N}) = {sigma} <= {prev}"
            prev = sigma

    def test_sigma_diverges(self):
        """sigma(sl_N) = H_N - 1 -> infinity as N -> infinity (harmonic series)."""
        sigma_100 = sum(Rational(1, i) for i in range(2, 101))
        assert float(sigma_100) > 4.0, f"sigma(sl_100) = {float(sigma_100)} should be > 4"


# ============================================================================
# Section 6: Edge cases and limiting values
# ============================================================================

class TestEdgeCases:
    """Edge cases, limiting values, and AP-motivated checks."""

    def test_critical_level_affine(self):
        """At the critical level k = -h^v, kappa = 0."""
        # sl_2: h^v = 2, critical k = -2
        kappa = kappa_method2_ope("affine", lie_type="A", rank=1, k=-2)
        assert _eq(kappa, 0), f"sl_2 at critical level: kappa = {kappa} != 0"

        # sl_3: h^v = 3, critical k = -3
        kappa = kappa_method2_ope("affine", lie_type="A", rank=2, k=-3)
        assert _eq(kappa, 0), f"sl_3 at critical level: kappa = {kappa} != 0"

        # G_2: h^v = 4, critical k = -4
        kappa = kappa_method2_ope("affine", lie_type="G", rank=2, k=-4)
        assert _eq(kappa, 0), f"G_2 at critical level: kappa = {kappa} != 0"

    def test_virasoro_c0_kappa0(self):
        """At c=0, kappa = 0 (uncurved)."""
        kappa = kappa_method2_ope("virasoro", c=0)
        assert _eq(kappa, 0)

    def test_kappa_not_c_over_2_for_affine(self):
        """CRITICAL (AP1/AP39): kappa != c/2 for affine KM (except Heisenberg).
        For sl_2 at k=1: c = 3*1/(1+2) = 1, kappa = 9/4. c/2 = 1/2 != 9/4."""
        kappa = kappa_method2_ope("affine", lie_type="A", rank=1, k=1)
        c_value = Rational(3) * 1 / (1 + 2)  # = 1
        assert not _eq(kappa, c_value / 2), (
            f"sl_2 k=1: kappa = {kappa} should NOT equal c/2 = {c_value/2} (AP1)"
        )

    def test_kappa_not_equal_c_for_virasoro(self):
        """CRITICAL (AP48): kappa != c for Virasoro (it's c/2, not c)."""
        kappa = kappa_method2_ope("virasoro", c=10)
        assert not _eq(kappa, 10), "Virasoro kappa = c/2, NOT c (AP48)"
        assert _eq(kappa, 5)

    def test_heisenberg_not_self_dual(self):
        """CRITICAL: Heisenberg is NOT self-dual. kappa(H_k) = k != -k = kappa(H_k^!)."""
        k_val = 3
        kappa = kappa_method2_ope("heisenberg", k=k_val)
        kappa_dual = -k_val  # kappa(H_{-k}^*) = -k
        assert not _eq(kappa, kappa_dual), "Heisenberg is NOT self-dual"
        assert _eq(kappa + kappa_dual, 0)

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro is self-dual at c=13, NOT c=26 (AP8)."""
        kappa_13 = kappa_method2_ope("virasoro", c=13)
        kappa_dual_13 = kappa_method2_ope("virasoro", c=26 - 13)  # = Vir_{13}
        assert _eq(kappa_13, kappa_dual_13), f"At c=13, kappa = kappa' (self-dual)"

    def test_virasoro_not_self_dual_at_c26(self):
        """At c=26: kappa = 13, kappa' = 0. NOT self-dual."""
        kappa_26 = kappa_method2_ope("virasoro", c=26)
        kappa_dual_26 = kappa_method2_ope("virasoro", c=0)
        assert _eq(kappa_26, 13)
        assert _eq(kappa_dual_26, 0)
        assert not _eq(kappa_26, kappa_dual_26)

    def test_bc_conformal_ghosts_kappa_minus_13(self):
        """bc at j=2 (conformal ghosts): kappa = -13.
        This cancels the Virasoro at c=26: kappa(Vir_26) + kappa(bc_2) = 13 + (-13) = 0.
        This is the anomaly cancellation at the critical dimension."""
        kappa_bc = kappa_method2_ope("bc", spin=2)
        kappa_vir = kappa_method2_ope("virasoro", c=26)
        assert _eq(kappa_bc, -13)
        assert _eq(kappa_vir, 13)
        assert _eq(kappa_bc + kappa_vir, 0), "Anomaly cancellation at c=26"

    def test_negative_level_heisenberg(self):
        """kappa(H_k) at k < 0: still kappa = k (negative)."""
        kappa = kappa_method2_ope("heisenberg", k=-5)
        assert _eq(kappa, -5)

    def test_fractional_level(self):
        """kappa at fractional level (admissible levels)."""
        # sl_2 at k = -1/2 (admissible): kappa = 3*(-1/2+2)/4 = 3*(3/2)/4 = 9/8
        kappa = kappa_method2_ope("affine", lie_type="A", rank=1, k=Rational(-1, 2))
        assert _eq(kappa, Rational(9, 8))


# ============================================================================
# Section 7: Non-simply-laced comprehensive verification
# ============================================================================

class TestNonSimplyLacedComprehensive:
    """Comprehensive tests for non-simply-laced affine algebras."""

    def test_B2_so5_data(self):
        """B_2 = so(5): dim=10, h=4, h^v=3."""
        dim, h, h_dual, _, _ = _get_lie_data("B", 2)
        assert dim == 10
        assert h == 4
        assert h_dual == 3

    def test_C2_sp4_data(self):
        """C_2 = sp(4): dim=10, h=4, h^v=3."""
        dim, h, h_dual, _, _ = _get_lie_data("C", 2)
        assert dim == 10
        assert h == 4
        assert h_dual == 3

    def test_G2_data(self):
        """G_2: dim=14, h=6, h^v=4."""
        dim, h, h_dual, _, _ = _get_lie_data("G", 2)
        assert dim == 14
        assert h == 6
        assert h_dual == 4

    def test_F4_data(self):
        """F_4: dim=52, h=12, h^v=9."""
        dim, h, h_dual, _, _ = _get_lie_data("F", 4)
        assert dim == 52
        assert h == 12
        assert h_dual == 9

    def test_non_simply_laced_h_ne_hdual(self):
        """For non-simply-laced types, h != h^v."""
        for type_, rank in [("B", 2), ("C", 3), ("G", 2), ("F", 4)]:
            _, h, h_dual, _, _ = _get_lie_data(type_, rank)
            assert h != h_dual, f"{type_}_{rank}: h={h} should differ from h^v={h_dual}"

    def test_simply_laced_h_eq_hdual(self):
        """For simply-laced types, h = h^v."""
        for type_, rank in [("A", 1), ("A", 2), ("D", 4), ("E", 6), ("E", 7), ("E", 8)]:
            _, h, h_dual, _, _ = _get_lie_data(type_, rank)
            assert h == h_dual, f"{type_}_{rank}: h={h} should equal h^v={h_dual}"

    def test_B2_C2_same_invariants(self):
        """B_2 and C_2 are isomorphic: same dim, h, h^v."""
        dim_b, h_b, hd_b, _, _ = _get_lie_data("B", 2)
        dim_c, h_c, hd_c, _, _ = _get_lie_data("C", 2)
        assert dim_b == dim_c
        assert h_b == h_c
        assert hd_b == hd_c

    def test_non_simply_laced_complementarity(self):
        """kappa + kappa' = 0 for ALL affine KM (including non-simply-laced)."""
        test_cases = [
            ("B", 2), ("B", 3), ("B", 4),
            ("C", 2), ("C", 3),
            ("G", 2),
            ("F", 4),
        ]
        for type_, rank in test_cases:
            for k_val in [1, 2]:
                s = complementarity_sum("affine", lie_type=type_, rank=rank, k=k_val)
                assert _eq(s, 0), (
                    f"Affine {type_}_{rank} k={k_val}: kappa+kappa' = {s} != 0"
                )


# ============================================================================
# Section 8: Faber-Pandharipande and F_g cross-checks
# ============================================================================

class TestFaberPandharipande:
    """Verify lambda_g^FP values and F_g = kappa * lambda_g^FP."""

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        assert _eq(LAMBDA_FP[1], Rational(1, 24))

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        assert _eq(LAMBDA_FP[2], Rational(7, 5760))

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        assert _eq(LAMBDA_FP[3], Rational(31, 967680))

    def test_F1_is_kappa_over_24(self):
        """F_1 = kappa/24 for all families."""
        test_cases = [
            ("heisenberg", {"k": 3}, 3),
            ("virasoro", {"c": 10}, 5),
            ("affine", {"lie_type": "A", "rank": 1, "k": 1}, Rational(9, 4)),
            ("free_fermion", {}, Rational(1, 4)),
            ("lattice", {"rank": 8}, 8),
        ]
        for family, params, expected_kappa in test_cases:
            kappa = kappa_method2_ope(family, **params)
            F1 = kappa * LAMBDA_FP[1]
            assert _eq(F1, Rational(expected_kappa, 24)), (
                f"{family}({params}): F_1 = {F1} != {expected_kappa}/24"
            )

    def test_F2_over_F1_universal(self):
        """The ratio F_2/F_1 = 7/240 is universal (independent of the algebra)."""
        expected_ratio = LAMBDA_FP[2] / LAMBDA_FP[1]
        assert _eq(expected_ratio, Rational(7, 240))


# ============================================================================
# Section 9: Full landscape sweep
# ============================================================================

class TestFullLandscape:
    """Run the full landscape verification and check all pass."""

    def test_full_landscape_all_agree(self):
        """ALL families in the standard landscape should have 5-method agreement."""
        results = full_landscape_verification()
        failures = [r for r in results if not r.all_agree]
        if failures:
            msg = "FAILURES:\n"
            for r in failures:
                msg += f"  {r}\n"
                for d in r.disagreements:
                    msg += f"    {d}\n"
            pytest.fail(msg)

    def test_no_none_values_in_landscape(self):
        """Every family should return non-None values for all 5 methods."""
        results = full_landscape_verification()
        for r in results:
            assert r.method1_genus1 is not None, f"{r.family}: M1 is None"
            assert r.method2_ope is not None, f"{r.family}: M2 is None"
            assert r.method3_character is not None, f"{r.family}: M3 is None"
            assert r.method4_shadow is not None, f"{r.family}: M4 is None"
            assert r.method5_complementarity is not None, f"{r.family}: M5 is None"


# ============================================================================
# Section 10: Cross-module consistency
# ============================================================================

class TestCrossModuleConsistency:
    """Verify kappa_cross_verification agrees with existing modules."""

    def test_agrees_with_shadow_metric_census(self):
        """Compare with shadow_metric_census.py."""
        try:
            from compute.lib.shadow_metric_census import (
                kappa_heisenberg as smc_heis,
                kappa_virasoro as smc_vir,
                kappa_affine_sl2 as smc_sl2,
                kappa_betagamma as smc_bg,
            )
            # Heisenberg
            for k_val in [1, 2, -1]:
                assert _eq(kappa_method2_ope("heisenberg", k=k_val), smc_heis(k_val))
            # Virasoro
            for c_val in [1, 13, 26]:
                assert _eq(kappa_method2_ope("virasoro", c=c_val), smc_vir(c_val))
            # sl_2
            for k_val in [1, 2]:
                assert _eq(
                    kappa_method2_ope("affine", lie_type="A", rank=1, k=k_val),
                    smc_sl2(k_val)
                )
            # betagamma
            for lam_val in [0, 1, Rational(1, 2)]:
                assert _eq(kappa_method2_ope("betagamma", lam=lam_val), smc_bg(lam_val))
        except ImportError:
            pytest.skip("shadow_metric_census not available")

    def test_agrees_with_theorem_c(self):
        """Compare with theorem_c_complementarity.py."""
        try:
            from compute.lib.theorem_c_complementarity import kappa as thmc_kappa
            from fractions import Fraction
            # Heisenberg
            assert _eq(kappa_method2_ope("heisenberg", k=1), thmc_kappa("heisenberg", k=1))
            # Virasoro
            assert _eq(kappa_method2_ope("virasoro", c=13), thmc_kappa("virasoro", c=13))
            # Affine
            assert _eq(
                kappa_method2_ope("affine", lie_type="A", rank=1, k=1),
                thmc_kappa("affine", lie_type="A", rank=1, k=1)
            )
        except ImportError:
            pytest.skip("theorem_c_complementarity not available")

    def test_agrees_with_depth_classification(self):
        """Compare with depth_classification.py."""
        try:
            from compute.lib.depth_classification import (
                kappa_heisenberg as dc_heis,
                kappa_virasoro as dc_vir,
                kappa_affine as dc_aff,
                kappa_betagamma as dc_bg,
                kappa_lattice as dc_lat,
            )
            # Heisenberg
            assert _eq(kappa_method2_ope("heisenberg", k=1), dc_heis(1))
            # Virasoro
            assert _eq(kappa_method2_ope("virasoro", c=10), dc_vir(10))
            # Affine sl_2
            assert _eq(
                kappa_method2_ope("affine", lie_type="A", rank=1, k=1),
                dc_aff(3, 2, 1)  # dim=3, h^v=2, k=1
            )
            # betagamma
            assert _eq(kappa_method2_ope("betagamma", lam=1), dc_bg(1))
            # Lattice
            assert _eq(kappa_method2_ope("lattice", rank=8), dc_lat(8))
        except ImportError:
            pytest.skip("depth_classification not available")

    def test_agrees_with_genus2_landscape(self):
        """Compare with genus2_landscape.py."""
        try:
            from compute.lib.genus2_landscape import (
                kappa_heisenberg as g2_heis,
                kappa_virasoro as g2_vir,
                kappa_affine_sl2 as g2_sl2,
                kappa_w3 as g2_w3,
                kappa_betagamma as g2_bg,
                kappa_E8_lattice as g2_e8,
            )
            assert _eq(kappa_method2_ope("heisenberg", k=1), g2_heis(1))
            assert _eq(kappa_method2_ope("virasoro", c=10), g2_vir(10))
            assert _eq(
                kappa_method2_ope("affine", lie_type="A", rank=1, k=1),
                g2_sl2(1)
            )
            assert _eq(kappa_method2_ope("w3", c=6), g2_w3(6))
            assert _eq(kappa_method2_ope("betagamma", lam=1), g2_bg(1))
            assert _eq(kappa_method2_ope("lattice", rank=8), g2_e8())
        except ImportError:
            pytest.skip("genus2_landscape not available")
