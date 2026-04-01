"""Tests for genus-1 and genus-2 free energies across the full standard landscape.

Verifies F_g(A) = kappa(A) * lambda_g^FP for all 15 standard families.

Each test independently computes kappa from the family-specific formula
(AP1: never copy between families) and checks F_1 = kappa/24, F_2 = 7*kappa/5760.

Cross-checks:
    - F_1 against independently hardcoded expected values
    - kappa against the shadow_metric_census.py and genus_expansion.py modules
    - F_2 consistency with F_1 via the ratio F_2/F_1 = 7/240
    - Additivity: F_1(H_{k1} + H_{k2}) = F_1(H_{k1}) + F_1(H_{k2})
    - Complementarity constraints (AP24)
"""

import unittest

from sympy import Rational

from compute.lib.f1_landscape import (
    F1, F2, Fg,
    LAMBDA_FP_1, LAMBDA_FP_2,
    EXPECTED_F1, EXPECTED_KAPPA,
    build_landscape,
    kappa_heisenberg, kappa_free_fermion, kappa_betagamma, kappa_bc,
    kappa_virasoro, kappa_affine, kappa_wN, kappa_lattice,
    landscape_F1, landscape_F2, landscape_table,
)


def _R(n, d=1):
    return Rational(n, d)


class TestLambdaFP(unittest.TestCase):
    """Verify the Faber-Pandharipande intersection numbers."""

    def test_lambda_fp_1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(LAMBDA_FP_1, _R(1, 24))

    def test_lambda_fp_2(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(LAMBDA_FP_2, _R(7, 5760))

    def test_lambda_fp_from_bernoulli(self):
        """Verify lambda_g^FP from Bernoulli numbers independently.

        lambda_1 = (2^1 - 1)/2^1 * |B_2|/2! = 1/2 * 1/6 / 2 = 1/24.
        lambda_2 = (2^3 - 1)/2^3 * |B_4|/4! = 7/8 * 1/30 / 24 = 7/5760.
        """
        # Genus 1: B_2 = 1/6
        lam1 = _R(2**1 - 1, 2**1) * _R(1, 6) / 2
        self.assertEqual(lam1, _R(1, 24))

        # Genus 2: B_4 = -1/30, |B_4| = 1/30
        lam2 = _R(2**3 - 1, 2**3) * _R(1, 30) / 24
        self.assertEqual(lam2, _R(7, 5760))


class TestKappaFormulas(unittest.TestCase):
    """Verify each kappa formula independently from first principles."""

    # -- Heisenberg --

    def test_kappa_heisenberg_1(self):
        self.assertEqual(kappa_heisenberg(1), _R(1))

    def test_kappa_heisenberg_generic(self):
        for k in [1, 2, 5, 10]:
            self.assertEqual(kappa_heisenberg(k), _R(k))

    # -- Free fermion --

    def test_kappa_free_fermion(self):
        """kappa(ff) = 1/4 = c/2 with c = 1/2."""
        self.assertEqual(kappa_free_fermion(), _R(1, 4))

    # -- betagamma --

    def test_kappa_betagamma_weight1(self):
        """kappa(bg, lambda=1) = 6 - 6 + 1 = 1."""
        self.assertEqual(kappa_betagamma(1), _R(1))

    def test_kappa_betagamma_weight0(self):
        """kappa(bg, lambda=0) = 0 - 0 + 1 = 1."""
        self.assertEqual(kappa_betagamma(0), _R(1))

    def test_kappa_betagamma_symplectic(self):
        """kappa(bg, lambda=1/2) = 6/4 - 3 + 1 = -1/2."""
        self.assertEqual(kappa_betagamma(_R(1, 2)), _R(-1, 2))

    # -- bc ghosts --

    def test_kappa_bc_spin0(self):
        """kappa(bc, j=0) = -(0 - 0 + 1) = -1."""
        self.assertEqual(kappa_bc(0), _R(-1))

    def test_kappa_bc_opposite_betagamma(self):
        """kappa(bc, j) = -kappa(bg, j) for all j."""
        for j in [0, 1, _R(1, 2), 2, _R(3, 2)]:
            self.assertEqual(kappa_bc(j), -kappa_betagamma(j))

    # -- Virasoro --

    def test_kappa_virasoro_half(self):
        """kappa(Vir, c=1/2) = 1/4."""
        self.assertEqual(kappa_virasoro(_R(1, 2)), _R(1, 4))

    def test_kappa_virasoro_25(self):
        """kappa(Vir, c=25) = 25/2."""
        self.assertEqual(kappa_virasoro(25), _R(25, 2))

    def test_kappa_virasoro_26(self):
        """kappa(Vir, c=26) = 13 (string theory critical)."""
        self.assertEqual(kappa_virasoro(26), _R(13))

    # -- Affine Kac-Moody --

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        self.assertEqual(kappa_affine(3, 2, 1), _R(9, 4))

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 32/6 = 16/3."""
        self.assertEqual(kappa_affine(8, 3, 1), _R(16, 3))

    def test_kappa_G2_k1(self):
        """kappa(G_2, k=1) = 14*(1+4)/(2*4) = 70/8 = 35/4."""
        self.assertEqual(kappa_affine(14, 4, 1), _R(35, 4))

    def test_kappa_E8_k1(self):
        """kappa(E_8, k=1) = 248*(1+30)/(2*30) = 248*31/60 = 7688/60 = 1922/15."""
        expected = _R(248) * _R(31) / _R(60)
        self.assertEqual(expected, _R(1922, 15))
        self.assertEqual(kappa_affine(248, 30, 1), _R(1922, 15))

    def test_kappa_sl2_matches_formula(self):
        """Verify sl_2 formula: dim=3, h*=2, kappa = 3*(k+2)/4."""
        for k in [1, 2, 5, 10]:
            expected = _R(3) * (_R(k) + 2) / 4
            self.assertEqual(kappa_affine(3, 2, k), expected)

    # -- W-algebras --

    def test_kappa_w3_c2(self):
        """kappa(W_3, c=2) = (H_3 - 1)*2 = (1/2 + 1/3)*2 = 5/6*2 = 5/3."""
        self.assertEqual(kappa_wN(3, 2), _R(5, 3))

    def test_kappa_w3_c50(self):
        """kappa(W_3, c=50) = 5/6*50 = 250/6 = 125/3."""
        self.assertEqual(kappa_wN(3, 50), _R(125, 3))

    def test_kappa_w2_equals_virasoro(self):
        """W_2 = Virasoro: kappa(W_2, c) = (H_2 - 1)*c = c/2 = kappa(Vir_c)."""
        for c in [1, 2, _R(1, 2), 25, 26]:
            self.assertEqual(kappa_wN(2, c), kappa_virasoro(c))

    def test_kappa_w3_anomaly_ratio(self):
        """rho(sl_3) = H_3 - 1 = 1/2 + 1/3 = 5/6."""
        rho = _R(1, 2) + _R(1, 3)
        self.assertEqual(rho, _R(5, 6))
        self.assertEqual(kappa_wN(3, 6), 5 * _R(1))  # 5/6 * 6 = 5

    # -- Lattice VOA --

    def test_kappa_D4_lattice(self):
        self.assertEqual(kappa_lattice(4), _R(4))

    def test_kappa_E8_lattice(self):
        self.assertEqual(kappa_lattice(8), _R(8))

    def test_kappa_Leech_lattice(self):
        self.assertEqual(kappa_lattice(24), _R(24))


class TestF1AllFamilies(unittest.TestCase):
    """Verify F_1 = kappa/24 for each of the 15 standard families."""

    def test_01_heisenberg(self):
        """F_1(H_1) = 1/24."""
        self.assertEqual(F1(kappa_heisenberg(1)), _R(1, 24))

    def test_02_free_fermion(self):
        """F_1(ff) = 1/4 / 24 = 1/96."""
        self.assertEqual(F1(kappa_free_fermion()), _R(1, 96))

    def test_03_betagamma(self):
        """F_1(bg, lambda=1) = 1/24."""
        self.assertEqual(F1(kappa_betagamma(1)), _R(1, 24))

    def test_04_bc(self):
        """F_1(bc, j=0) = -1/24."""
        self.assertEqual(F1(kappa_bc(0)), _R(-1, 24))

    def test_05_sl2_k1(self):
        """F_1(sl_2, k=1) = 9/4 / 24 = 9/96 = 3/32."""
        self.assertEqual(F1(kappa_affine(3, 2, 1)), _R(3, 32))

    def test_06_sl3_k1(self):
        """F_1(sl_3, k=1) = 16/3 / 24 = 16/72 = 2/9."""
        self.assertEqual(F1(kappa_affine(8, 3, 1)), _R(2, 9))

    def test_07_G2_k1(self):
        """F_1(G_2, k=1) = 35/4 / 24 = 35/96."""
        self.assertEqual(F1(kappa_affine(14, 4, 1)), _R(35, 96))

    def test_08_virasoro_half(self):
        """F_1(Vir, c=1/2) = 1/4 / 24 = 1/96."""
        self.assertEqual(F1(kappa_virasoro(_R(1, 2))), _R(1, 96))

    def test_09_virasoro_25(self):
        """F_1(Vir, c=25) = 25/2 / 24 = 25/48."""
        self.assertEqual(F1(kappa_virasoro(25)), _R(25, 48))

    def test_10_W3_c2(self):
        """F_1(W_3, c=2) = 5/3 / 24 = 5/72."""
        self.assertEqual(F1(kappa_wN(3, 2)), _R(5, 72))

    def test_11_W3_c50(self):
        """F_1(W_3, c=50) = 125/3 / 24 = 125/72."""
        self.assertEqual(F1(kappa_wN(3, 50)), _R(125, 72))

    def test_12_D4_lattice(self):
        """F_1(D_4) = 4/24 = 1/6."""
        self.assertEqual(F1(kappa_lattice(4)), _R(1, 6))

    def test_13_E8_lattice(self):
        """F_1(E_8) = 8/24 = 1/3."""
        self.assertEqual(F1(kappa_lattice(8)), _R(1, 3))

    def test_14_Leech(self):
        """F_1(Leech) = 24/24 = 1."""
        self.assertEqual(F1(kappa_lattice(24)), _R(1))

    def test_15_E8_affine_k1(self):
        """F_1(E_8, k=1) = 1922/15 / 24 = 1922/360 = 961/180."""
        self.assertEqual(F1(kappa_affine(248, 30, 1)), _R(961, 180))


class TestF2AllFamilies(unittest.TestCase):
    """Verify F_2 = 7*kappa/5760 for each of the 15 standard families."""

    def test_01_heisenberg(self):
        """F_2(H_1) = 7/5760."""
        self.assertEqual(F2(kappa_heisenberg(1)), _R(7, 5760))

    def test_02_free_fermion(self):
        """F_2(ff) = 7/4 / 5760 = 7/23040."""
        self.assertEqual(F2(kappa_free_fermion()), _R(7, 23040))

    def test_03_betagamma(self):
        """F_2(bg, lambda=1) = 7/5760."""
        self.assertEqual(F2(kappa_betagamma(1)), _R(7, 5760))

    def test_04_bc(self):
        """F_2(bc, j=0) = -7/5760."""
        self.assertEqual(F2(kappa_bc(0)), _R(-7, 5760))

    def test_05_sl2_k1(self):
        """F_2(sl_2, k=1) = 7*9/4 / 5760 = 63/23040 = 21/7680."""
        expected = _R(7) * _R(9, 4) / 5760
        self.assertEqual(F2(kappa_affine(3, 2, 1)), expected)
        self.assertEqual(expected, _R(21, 7680))

    def test_06_sl3_k1(self):
        """F_2(sl_3, k=1) = 7*16/3 / 5760 = 112/17280 = 7/1080."""
        expected = _R(7) * _R(16, 3) / 5760
        self.assertEqual(F2(kappa_affine(8, 3, 1)), expected)
        self.assertEqual(expected, _R(7, 1080))

    def test_07_G2_k1(self):
        """F_2(G_2, k=1) = 7*35/4 / 5760 = 245/23040 = 49/4608."""
        expected = _R(7) * _R(35, 4) / 5760
        self.assertEqual(F2(kappa_affine(14, 4, 1)), expected)
        self.assertEqual(expected, _R(49, 4608))

    def test_08_virasoro_half(self):
        """F_2(Vir, c=1/2) = 7/4 / 5760 = 7/23040."""
        self.assertEqual(F2(kappa_virasoro(_R(1, 2))), _R(7, 23040))

    def test_09_virasoro_25(self):
        """F_2(Vir, c=25) = 7*25/2 / 5760 = 175/11520 = 35/2304."""
        expected = _R(7) * _R(25, 2) / 5760
        self.assertEqual(F2(kappa_virasoro(25)), expected)
        self.assertEqual(expected, _R(35, 2304))

    def test_10_W3_c2(self):
        """F_2(W_3, c=2) = 7*5/3 / 5760 = 35/17280 = 7/3456."""
        expected = _R(7) * _R(5, 3) / 5760
        self.assertEqual(F2(kappa_wN(3, 2)), expected)
        self.assertEqual(expected, _R(7, 3456))

    def test_11_W3_c50(self):
        """F_2(W_3, c=50) = 7*125/3 / 5760 = 875/17280."""
        expected = _R(7) * _R(125, 3) / 5760
        self.assertEqual(F2(kappa_wN(3, 50)), expected)
        self.assertEqual(expected, _R(875, 17280))

    def test_12_D4_lattice(self):
        """F_2(D_4) = 7*4/5760 = 28/5760 = 7/1440."""
        self.assertEqual(F2(kappa_lattice(4)), _R(7, 1440))

    def test_13_E8_lattice(self):
        """F_2(E_8) = 7*8/5760 = 56/5760 = 7/720."""
        self.assertEqual(F2(kappa_lattice(8)), _R(7, 720))

    def test_14_Leech(self):
        """F_2(Leech) = 7*24/5760 = 168/5760 = 7/240."""
        self.assertEqual(F2(kappa_lattice(24)), _R(7, 240))

    def test_15_E8_affine_k1(self):
        """F_2(E_8, k=1) = 7*1922/15 / 5760 = 13454/(15*5760) = 13454/86400."""
        expected = _R(7) * _R(1922, 15) / 5760
        self.assertEqual(F2(kappa_affine(248, 30, 1)), expected)
        # Simplify: 7*1922 = 13454, 15*5760 = 86400
        # gcd(13454, 86400): 13454 = 2 * 6727, 86400 = 2^6 * 3^3 * 5^2
        # gcd = 2, so 6727/43200
        self.assertEqual(expected, _R(6727, 43200))


class TestExpectedValueDicts(unittest.TestCase):
    """Verify the landscape against the EXPECTED dictionaries."""

    def test_all_kappa_match(self):
        """Every family's kappa matches the EXPECTED_KAPPA dict."""
        for family in build_landscape():
            with self.subTest(family=family.name):
                self.assertIn(family.name, EXPECTED_KAPPA)
                self.assertEqual(family.kappa, EXPECTED_KAPPA[family.name],
                                 f"kappa mismatch for {family.name}: "
                                 f"{family.kappa} != {EXPECTED_KAPPA[family.name]}")

    def test_all_F1_match(self):
        """Every family's F_1 matches the EXPECTED_F1 dict."""
        for family in build_landscape():
            with self.subTest(family=family.name):
                self.assertIn(family.name, EXPECTED_F1)
                computed = F1(family.kappa)
                self.assertEqual(computed, EXPECTED_F1[family.name],
                                 f"F_1 mismatch for {family.name}: "
                                 f"{computed} != {EXPECTED_F1[family.name]}")


class TestCrossChecks(unittest.TestCase):
    """Cross-family consistency checks (AP10: not just single-family hardcoded)."""

    def test_F2_F1_ratio(self):
        """For all families, F_2/F_1 = lambda_2/lambda_1 = 7/240.

        lambda_2/lambda_1 = (7/5760)/(1/24) = 7*24/5760 = 168/5760 = 7/240.
        """
        expected_ratio = _R(7, 240)
        for family in build_landscape():
            with self.subTest(family=family.name):
                f1 = F1(family.kappa)
                f2 = F2(family.kappa)
                if f1 != 0:
                    self.assertEqual(f2 / f1, expected_ratio,
                                     f"F_2/F_1 ratio wrong for {family.name}")

    def test_additivity(self):
        """F_1 is additive: F_1(H_{k1} + H_{k2}) = F_1(H_{k1}) + F_1(H_{k2}).

        For independent direct sum, kappa is additive (prop:independent-sum-factorization).
        """
        for k1, k2 in [(1, 1), (1, 2), (3, 5), (7, 11)]:
            with self.subTest(k1=k1, k2=k2):
                self.assertEqual(
                    F1(kappa_heisenberg(k1) + kappa_heisenberg(k2)),
                    F1(kappa_heisenberg(k1)) + F1(kappa_heisenberg(k2))
                )

    def test_bc_betagamma_cancellation(self):
        """kappa(bc, j) + kappa(bg, j) = 0, so F_1 cancels.

        This is the ghost cancellation: the bc + betagamma system is anomaly-free.
        """
        for j in [0, 1, _R(1, 2), 2]:
            with self.subTest(j=j):
                total_kappa = kappa_bc(j) + kappa_betagamma(j)
                self.assertEqual(total_kappa, _R(0))
                self.assertEqual(F1(total_kappa), _R(0))

    def test_virasoro_free_fermion_coincidence(self):
        """Virasoro at c=1/2 and free fermion have the same kappa = 1/4.

        Hence F_1(Vir_{1/2}) = F_1(ff) = 1/96.
        """
        self.assertEqual(kappa_virasoro(_R(1, 2)), kappa_free_fermion())
        self.assertEqual(F1(kappa_virasoro(_R(1, 2))), F1(kappa_free_fermion()))

    def test_lattice_heisenberg_coincidence(self):
        """kappa(V_Lambda) = rank = kappa(H_{rank}).

        Lattice VOA at rank r has the same kappa as Heisenberg at level r.
        """
        for r in [1, 4, 8, 16, 24]:
            with self.subTest(rank=r):
                self.assertEqual(kappa_lattice(r), kappa_heisenberg(r))

    def test_W2_virasoro_coincidence(self):
        """W_2 = Virasoro, so kappa(W_2, c) = kappa(Vir, c) for all c."""
        for cv in [1, _R(1, 2), 25, 26, _R(13)]:
            with self.subTest(c=cv):
                self.assertEqual(kappa_wN(2, cv), kappa_virasoro(cv))

    def test_positivity_for_positive_c(self):
        """kappa > 0 for all standard families with c > 0.

        (Except bc ghosts, which have c < 0 and kappa < 0.)
        """
        positive_families = [
            ('Heisenberg', kappa_heisenberg(1)),
            ('Free fermion', kappa_free_fermion()),
            ('betagamma', kappa_betagamma(1)),
            ('sl_2 k=1', kappa_affine(3, 2, 1)),
            ('Virasoro c=25', kappa_virasoro(25)),
            ('W_3 c=2', kappa_wN(3, 2)),
            ('D_4 lattice', kappa_lattice(4)),
            ('E_8 lattice', kappa_lattice(8)),
            ('Leech', kappa_lattice(24)),
            ('E_8 affine k=1', kappa_affine(248, 30, 1)),
        ]
        for name, kap in positive_families:
            with self.subTest(family=name):
                self.assertGreater(kap, 0, f"kappa({name}) = {kap} should be > 0")


class TestCrossModuleConsistency(unittest.TestCase):
    """Cross-check against shadow_metric_census.py and genus_expansion.py."""

    def test_kappa_vs_shadow_metric_census(self):
        """Verify kappa values match shadow_metric_census.py."""
        from compute.lib.shadow_metric_census import (
            kappa_heisenberg as smc_kappa_heis,
            kappa_free_fermion as smc_kappa_ff,
            kappa_betagamma as smc_kappa_bg,
            kappa_bc as smc_kappa_bc,
            kappa_virasoro as smc_kappa_vir,
            kappa_affine_sl2 as smc_kappa_sl2,
            kappa_affine_slN as smc_kappa_slN,
            kappa_w3 as smc_kappa_w3,
        )
        # Note: smc kappa functions use plain division (not Rational),
        # so we pass Rational inputs to avoid float/Rational mismatch.
        R = Rational
        # Heisenberg
        self.assertEqual(kappa_heisenberg(1), smc_kappa_heis(R(1)))
        # Free fermion
        self.assertEqual(kappa_free_fermion(), smc_kappa_ff())
        # betagamma
        self.assertEqual(kappa_betagamma(1), smc_kappa_bg(R(1)))
        # bc
        self.assertEqual(kappa_bc(0), smc_kappa_bc(R(0)))
        # Virasoro
        self.assertEqual(kappa_virasoro(25), smc_kappa_vir(R(25)))
        # sl_2 at k=1
        self.assertEqual(kappa_affine(3, 2, 1), smc_kappa_sl2(R(1)))
        # sl_3 at k=1
        self.assertEqual(kappa_affine(8, 3, 1), smc_kappa_slN(R(3), R(1)))
        # W_3 at c=2
        self.assertEqual(kappa_wN(3, 2), smc_kappa_w3(R(2)))

    def test_kappa_vs_genus_expansion(self):
        """Verify kappa values match genus_expansion.py."""
        from compute.lib.genus_expansion import (
            kappa_heisenberg as ge_kappa_heis,
            kappa_virasoro as ge_kappa_vir,
            kappa_w3 as ge_kappa_w3,
            kappa_sl2 as ge_kappa_sl2,
            kappa_sl3 as ge_kappa_sl3,
            kappa_g2 as ge_kappa_g2,
        )
        self.assertEqual(kappa_heisenberg(1), ge_kappa_heis(1))
        self.assertEqual(kappa_virasoro(25), ge_kappa_vir(25))
        self.assertEqual(kappa_wN(3, 2), ge_kappa_w3(2))
        self.assertEqual(kappa_affine(3, 2, 1), ge_kappa_sl2(1))
        self.assertEqual(kappa_affine(8, 3, 1), ge_kappa_sl3(1))
        self.assertEqual(kappa_affine(14, 4, 1), ge_kappa_g2(1))

    def test_kappa_vs_lie_algebra_general(self):
        """Verify against the general kappa_km from lie_algebra.py."""
        from compute.lib.lie_algebra import kappa_km
        # sl_2 at k=1: type A, rank 1
        self.assertEqual(kappa_affine(3, 2, 1), kappa_km('A', 1, 1))
        # sl_3 at k=1: type A, rank 2
        self.assertEqual(kappa_affine(8, 3, 1), kappa_km('A', 2, 1))
        # G_2 at k=1: type G, rank 2
        self.assertEqual(kappa_affine(14, 4, 1), kappa_km('G', 2, 1))
        # E_8 at k=1: type E, rank 8
        self.assertEqual(kappa_affine(248, 30, 1), kappa_km('E', 8, 1))

    def test_F1_vs_utils_F_g(self):
        """Verify F_1 matches the general F_g from utils.py."""
        from compute.lib.utils import F_g as utils_Fg
        for family in build_landscape():
            with self.subTest(family=family.name):
                our_F1 = F1(family.kappa)
                utils_F1 = utils_Fg(family.kappa, 1)
                self.assertEqual(our_F1, utils_F1)


class TestLandscapeFunctions(unittest.TestCase):
    """Test the landscape summary functions."""

    def test_landscape_F1_length(self):
        """landscape_F1() returns 15 entries."""
        results = landscape_F1()
        self.assertEqual(len(results), 15)

    def test_landscape_F2_length(self):
        """landscape_F2() returns 15 entries."""
        results = landscape_F2()
        self.assertEqual(len(results), 15)

    def test_landscape_table_keys(self):
        """landscape_table() returns proper keys."""
        table = landscape_table(max_genus=3)
        self.assertEqual(len(table), 15)
        for row in table:
            self.assertIn('name', row)
            self.assertIn('kappa', row)
            self.assertIn('F_1', row)
            self.assertIn('F_2', row)
            self.assertIn('F_3', row)

    def test_landscape_table_F1_matches(self):
        """F_1 from landscape_table matches F_1 from landscape_F1."""
        table = landscape_table(max_genus=2)
        f1_results = landscape_F1()
        for row, f1_row in zip(table, f1_results):
            self.assertEqual(row['name'], f1_row['name'])
            self.assertEqual(row['F_1'], f1_row['F1'])


class TestComplementarity(unittest.TestCase):
    """Verify Koszul duality constraints on kappa (AP24-aware)."""

    def test_virasoro_koszul_dual(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (not 0!).

        AP24: For Virasoro, kappa + kappa' = c/2 + (26-c)/2 = 13.
        """
        for cv in [1, _R(1, 2), 13, 25, 26]:
            with self.subTest(c=cv):
                kap = kappa_virasoro(cv)
                kap_dual = kappa_virasoro(26 - cv)
                self.assertEqual(kap + kap_dual, _R(13))

    def test_km_koszul_anti_symmetry(self):
        """For affine KM: kappa(g_k) + kappa(g_{-k-2h*}) = 0.

        The Feigin-Frenkel involution k -> -k-2h* ensures anti-symmetry.
        """
        # sl_2: h* = 2, dual level = -k-4
        for k in [1, 2, 3, 5]:
            k_dual = -k - 4  # -k - 2*h* for sl_2
            kap = kappa_affine(3, 2, k)
            kap_dual = kappa_affine(3, 2, k_dual)
            self.assertEqual(kap + kap_dual, _R(0),
                             f"sl_2: kappa(k={k}) + kappa(k={k_dual}) should be 0")


class TestGenusHigher(unittest.TestCase):
    """Spot-check F_3 for a few families."""

    def test_F3_heisenberg(self):
        """F_3(H_1) = lambda_3^FP = 31/967680."""
        f3 = Fg(kappa_heisenberg(1), 3)
        self.assertEqual(f3, _R(31, 967680))

    def test_F3_virasoro_26(self):
        """F_3(Vir_{26}) = 13 * 31/967680 = 403/967680."""
        f3 = Fg(kappa_virasoro(26), 3)
        self.assertEqual(f3, _R(13) * _R(31, 967680))
        self.assertEqual(f3, _R(403, 967680))


if __name__ == '__main__':
    unittest.main()
