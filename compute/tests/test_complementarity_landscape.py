"""Tests for the full complementarity landscape.

Verifies ALL complementarity data for ALL standard families:

1. Heisenberg: kappa + kappa' = 0
2. Free fermion: kappa + kappa' = 0
3. Lattice VOAs: kappa + kappa' = 0
4. betagamma/bc: kappa + kappa' = 0
5. Affine KM (all simple types): kappa + kappa' = 0, K = 2*dim(g)
6. Virasoro: kappa + kappa' = 13, K = 26, self-dual at c = 13
7. W_N (N=2..7): kappa + kappa' = rho_N * K_N, verified at multiple levels

Cross-checks:
- K_N formula vs direct computation
- Level independence of complementarity sum
- Self-dual points
- betagamma polynomial symmetry
- Consistency with existing compute modules

References:
    thm:quantum-complementarity-main, rem:koszul-conductor-explicit
    AP1, AP8, AP24, AP25 (CLAUDE.md)
"""
import unittest
from fractions import Fraction

from compute.lib.complementarity_landscape import (
    # Core kappa functions
    kappa_heisenberg, kappa_free_fermion, kappa_lattice,
    kappa_betagamma, kappa_bc, kappa_affine, kappa_virasoro, kappa_wn,
    # Dual kappa functions
    kappa_dual_heisenberg, kappa_dual_free_fermion, kappa_dual_lattice,
    kappa_dual_betagamma, kappa_dual_bc, kappa_dual_affine,
    kappa_dual_virasoro, kappa_dual_wn,
    # Structural invariants
    anomaly_ratio, koszul_conductor_wn, central_charge_sum_affine,
    central_charge_wn, harmonic, self_dual_point_wn, self_dual_point_virasoro,
    # Complementarity sums
    complementarity_sum_heisenberg, complementarity_sum_free_fermion,
    complementarity_sum_lattice, complementarity_sum_betagamma,
    complementarity_sum_affine, complementarity_sum_wn,
    # Data constructors
    datum_heisenberg, datum_free_fermion, datum_lattice,
    datum_betagamma, datum_affine, datum_virasoro, datum_wn,
    # Verification functions
    verify_affine_kappa_antisymmetry, verify_wn_complementarity_level_independence,
    verify_koszul_conductor_formula, verify_betagamma_symmetry,
    verify_central_charge_sum_affine, verify_self_dual_points,
    full_landscape_audit,
    # Landscape tables
    full_complementarity_landscape, landscape_summary_table,
)


class TestKappaFormulas(unittest.TestCase):
    """Test kappa formulas for all families."""

    # ---- Heisenberg ----

    def test_heisenberg_kappa_is_level(self):
        """kappa(H_k) = k."""
        for k in [1, 2, -3, Fraction(1, 2), Fraction(7, 3)]:
            self.assertEqual(kappa_heisenberg(k), Fraction(k))

    def test_heisenberg_dual(self):
        """kappa'(H_k) = -k."""
        for k in [1, 2, -3, Fraction(1, 2)]:
            self.assertEqual(kappa_dual_heisenberg(k), -Fraction(k))

    def test_heisenberg_sum_zero(self):
        """kappa + kappa' = 0 for Heisenberg."""
        for k in [1, -1, 0, Fraction(1, 2), 100]:
            s = kappa_heisenberg(k) + kappa_dual_heisenberg(k)
            self.assertEqual(s, 0)

    # ---- Free fermion ----

    def test_free_fermion_kappa(self):
        """kappa(free fermion) = 1/4."""
        self.assertEqual(kappa_free_fermion(), Fraction(1, 4))

    def test_free_fermion_dual(self):
        """kappa'(free fermion) = -1/4."""
        self.assertEqual(kappa_dual_free_fermion(), Fraction(-1, 4))

    def test_free_fermion_sum_zero(self):
        """kappa + kappa' = 0 for free fermion."""
        self.assertEqual(kappa_free_fermion() + kappa_dual_free_fermion(), 0)

    # ---- Lattice ----

    def test_lattice_kappa(self):
        """kappa(V_Lambda) = rank."""
        for rank in [1, 4, 8, 16, 24]:
            self.assertEqual(kappa_lattice(rank), Fraction(rank))

    def test_lattice_dual(self):
        """kappa'(V_Lambda) = -rank."""
        for rank in [4, 8, 24]:
            self.assertEqual(kappa_dual_lattice(rank), -Fraction(rank))

    def test_lattice_sum_zero(self):
        """kappa + kappa' = 0 for lattice VOAs."""
        for rank in [1, 4, 8, 16, 24]:
            s = kappa_lattice(rank) + kappa_dual_lattice(rank)
            self.assertEqual(s, 0, f"Failed at rank={rank}")

    def test_lattice_D4(self):
        """D_4 lattice: kappa=4, kappa'=-4, sum=0."""
        self.assertEqual(kappa_lattice(4), 4)
        self.assertEqual(kappa_dual_lattice(4), -4)

    def test_lattice_E8(self):
        """E_8 lattice: kappa=8, kappa'=-8, sum=0."""
        self.assertEqual(kappa_lattice(8), 8)
        self.assertEqual(kappa_dual_lattice(8), -8)

    def test_lattice_Leech(self):
        """Leech lattice: kappa=24, kappa'=-24, sum=0."""
        self.assertEqual(kappa_lattice(24), 24)
        self.assertEqual(kappa_dual_lattice(24), -24)

    # ---- betagamma / bc ----

    def test_betagamma_formula(self):
        """kappa_bg(lam) = 6*lam^2 - 6*lam + 1."""
        self.assertEqual(kappa_betagamma(Fraction(0)), 1)
        self.assertEqual(kappa_betagamma(Fraction(1)), 1)
        self.assertEqual(kappa_betagamma(Fraction(1, 2)), Fraction(-1, 2))
        self.assertEqual(kappa_betagamma(Fraction(2)), 13)

    def test_bc_formula(self):
        """kappa_bc(lam) = -(6*lam^2 - 6*lam + 1)."""
        self.assertEqual(kappa_bc(Fraction(0)), -1)
        self.assertEqual(kappa_bc(Fraction(1)), -1)
        self.assertEqual(kappa_bc(Fraction(1, 2)), Fraction(1, 2))

    def test_betagamma_bc_sum_zero(self):
        """kappa_bg + kappa_bc = 0 for ALL lambda."""
        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 3),
                    Fraction(1, 2), Fraction(2, 3), Fraction(1),
                    Fraction(3, 2), Fraction(2), Fraction(-1)]:
            s = kappa_betagamma(lam) + kappa_bc(lam)
            self.assertEqual(s, 0, f"Failed at lam={lam}")

    def test_betagamma_polynomial_symmetry(self):
        """kappa_bg(lam) = kappa_bg(1-lam): polynomial symmetry, NOT duality."""
        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2)]:
            self.assertEqual(
                kappa_betagamma(lam), kappa_betagamma(1 - lam),
                f"Symmetry failed at lam={lam}"
            )

    def test_betagamma_NOT_self_dual(self):
        """betagamma is NOT self-dual: bg^! = bc (different statistics)."""
        # kappa_bg(lam) != kappa_dual_bg(lam) in general (they have opposite sign)
        for lam in [Fraction(0), Fraction(1), Fraction(2)]:
            kbg = kappa_betagamma(lam)
            kdual = kappa_dual_betagamma(lam)
            self.assertEqual(kdual, -kbg)
            self.assertNotEqual(kbg, kdual)  # nonzero kappa -> not self-dual


class TestAffineKM(unittest.TestCase):
    """Test affine Kac-Moody complementarity."""

    def test_sl2_kappa_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        # dim(sl_2)=3, h^v=2, kappa = 3*(k+2)/(2*2) = 3(k+2)/4
        for k in [1, 2, 3, -1]:
            expected = Fraction(3) * (k + 2) / 4
            self.assertEqual(kappa_affine("A", 1, Fraction(k)), expected)

    def test_sl3_kappa_formula(self):
        """kappa(sl_3, k) = 4(k+3)/3.

        dim(sl_3) = 8, h^v = 3, kappa = 8*(k+3)/6 = 4(k+3)/3.
        """
        for k in [1, 2, 3, -1]:
            expected = Fraction(4) * (k + 3) / 3
            self.assertEqual(kappa_affine("A", 2, Fraction(k)), expected)

    def test_G2_kappa_formula(self):
        """kappa(G_2, k) = 7(k+4)/4.

        dim(G_2) = 14, h^v = 4, kappa = 14*(k+4)/8 = 7(k+4)/4.
        """
        for k in [1, 2, 3]:
            expected = Fraction(7) * (k + 4) / 4
            self.assertEqual(kappa_affine("G", 2, Fraction(k)), expected)

    def test_E8_kappa_formula(self):
        """kappa(E_8, k) = 62(k+30)/15.

        dim(E_8) = 248, h^v = 30, kappa = 248*(k+30)/60 = 62(k+30)/15.
        """
        for k in [1, 2, 3]:
            expected = Fraction(62) * (k + 30) / 15
            self.assertEqual(kappa_affine("E", 8, Fraction(k)), expected)

    def test_all_affine_antisymmetry(self):
        """kappa + kappa' = 0 for ALL affine KM algebras at multiple levels."""
        algebras = [
            ("A", 1), ("A", 2), ("A", 3), ("A", 4),
            ("B", 2), ("B", 3), ("C", 2), ("C", 3),
            ("D", 4), ("G", 2), ("F", 4),
            ("E", 6), ("E", 7), ("E", 8),
        ]
        for lt, rk in algebras:
            for k_val in [Fraction(1), Fraction(2), Fraction(3), Fraction(-1)]:
                _, hv = kappa_affine.__wrapped__(lt, rk, k_val) if hasattr(kappa_affine, '__wrapped__') else (None, None)
                # Just compute and check
                try:
                    kap = kappa_affine(lt, rk, k_val)
                    kap_dual = kappa_dual_affine(lt, rk, k_val)
                    self.assertEqual(
                        kap + kap_dual, 0,
                        f"Failed for {lt}_{rk} at k={k_val}: kappa={kap}, kappa'={kap_dual}"
                    )
                except ValueError:
                    pass  # critical level

    def test_affine_central_charge_sum_is_2dim(self):
        """c(k) + c(k') = 2*dim(g) for affine KM (proved algebraically)."""
        r = verify_central_charge_sum_affine()
        self.assertTrue(r["all_ok"])

    def test_affine_K_values(self):
        """K = c+c' = 2*dim for specific algebras."""
        self.assertEqual(central_charge_sum_affine("A", 1), 6)    # sl_2
        self.assertEqual(central_charge_sum_affine("A", 2), 16)   # sl_3
        self.assertEqual(central_charge_sum_affine("G", 2), 28)   # G_2
        self.assertEqual(central_charge_sum_affine("E", 8), 496)  # E_8
        self.assertEqual(central_charge_sum_affine("D", 4), 56)   # so_8
        self.assertEqual(central_charge_sum_affine("F", 4), 104)  # F_4
        self.assertEqual(central_charge_sum_affine("E", 6), 156)  # E_6
        self.assertEqual(central_charge_sum_affine("E", 7), 266)  # E_7

    def test_affine_critical_level_raises(self):
        """kappa at critical level k=-h^v raises ValueError."""
        with self.assertRaises(ValueError):
            kappa_affine("A", 1, Fraction(-2))  # sl_2, h^v=2
        with self.assertRaises(ValueError):
            kappa_affine("A", 2, Fraction(-3))  # sl_3, h^v=3
        with self.assertRaises(ValueError):
            kappa_affine("E", 8, Fraction(-30))  # E_8, h^v=30


class TestWAlgebras(unittest.TestCase):
    """Test W-algebra complementarity."""

    def test_anomaly_ratio_values(self):
        """rho_N = H_N - 1 for small N."""
        self.assertEqual(anomaly_ratio(2), Fraction(1, 2))
        self.assertEqual(anomaly_ratio(3), Fraction(5, 6))
        self.assertEqual(anomaly_ratio(4), Fraction(13, 12))
        self.assertEqual(anomaly_ratio(5), Fraction(77, 60))

    def test_koszul_conductor_values(self):
        """K_N = 2(N-1)(2N^2+2N+1) for small N."""
        self.assertEqual(koszul_conductor_wn(2), 26)
        self.assertEqual(koszul_conductor_wn(3), 100)
        self.assertEqual(koszul_conductor_wn(4), 246)
        self.assertEqual(koszul_conductor_wn(5), 488)
        self.assertEqual(koszul_conductor_wn(6), 850)
        self.assertEqual(koszul_conductor_wn(7), 1356)

    def test_koszul_conductor_polynomial(self):
        """K_N = 4N^3 - 2N - 2 (equivalent form)."""
        for N in range(2, 15):
            self.assertEqual(
                koszul_conductor_wn(N),
                4 * N ** 3 - 2 * N - 2,
                f"Polynomial form failed at N={N}"
            )

    def test_koszul_conductor_vs_direct(self):
        """K_N formula matches c(k) + c(k') computed directly."""
        r = verify_koszul_conductor_formula(max_N=10)
        self.assertTrue(r["all_ok"])

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c in [0, 1, 13, 26, Fraction(1, 2), Fraction(7, 10)]:
            self.assertEqual(kappa_virasoro(c), Fraction(c) / 2)

    def test_virasoro_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        for c in [0, 1, 13, 26, Fraction(1, 2), 100, -50]:
            s = kappa_virasoro(c) + kappa_dual_virasoro(c)
            self.assertEqual(s, 13, f"Failed at c={c}")

    def test_virasoro_self_dual_c13(self):
        """Virasoro self-dual at c=13, NOT c=26 (AP8)."""
        self.assertEqual(self_dual_point_virasoro(), Fraction(13))
        kap = kappa_virasoro(Fraction(13))
        kap_dual = kappa_dual_virasoro(Fraction(13))
        self.assertEqual(kap, kap_dual)
        self.assertEqual(kap, Fraction(13, 2))

    def test_virasoro_NOT_self_dual_c26(self):
        """c=26 is NOT the self-dual point (AP8)."""
        kap = kappa_virasoro(Fraction(26))
        kap_dual = kappa_dual_virasoro(Fraction(26))
        self.assertNotEqual(kap, kap_dual)
        self.assertEqual(kap, 13)
        self.assertEqual(kap_dual, 0)

    def test_w3_kappa(self):
        """kappa(W_3, c) = 5c/6."""
        for c in [2, 50, 100, -10]:
            self.assertEqual(kappa_wn(3, Fraction(c)), Fraction(5) * c / 6)

    def test_w3_sum(self):
        """kappa(W_3) + kappa'(W_3) = 250/3."""
        expected = Fraction(250, 3)
        for c in [2, 50, 80, -10]:
            s = kappa_wn(3, Fraction(c)) + kappa_dual_wn(3, Fraction(c))
            self.assertEqual(s, expected, f"Failed at c={c}")

    def test_w3_self_dual_c50(self):
        """W_3 self-dual at c=50."""
        self.assertEqual(self_dual_point_wn(3), Fraction(50))

    def test_w4_kappa(self):
        """kappa(W_4, c) = 13c/12."""
        self.assertEqual(kappa_wn(4, Fraction(12)), Fraction(13))
        self.assertEqual(kappa_wn(4, Fraction(24)), Fraction(26))

    def test_w4_K_and_self_dual(self):
        """W_4: K=246, self-dual at c=123."""
        self.assertEqual(koszul_conductor_wn(4), 246)
        self.assertEqual(self_dual_point_wn(4), Fraction(123))

    def test_w4_sum(self):
        """kappa(W_4) + kappa'(W_4) = 533/2."""
        expected = anomaly_ratio(4) * koszul_conductor_wn(4)
        self.assertEqual(expected, Fraction(533, 2))
        for c in [1, 123, 200]:
            s = kappa_wn(4, Fraction(c)) + kappa_dual_wn(4, Fraction(c))
            self.assertEqual(s, expected)

    def test_w5_kappa(self):
        """kappa(W_5, c) = 77c/60."""
        self.assertEqual(kappa_wn(5, Fraction(60)), Fraction(77))

    def test_w5_K_and_self_dual(self):
        """W_5: K=488, self-dual at c=244."""
        self.assertEqual(koszul_conductor_wn(5), 488)
        self.assertEqual(self_dual_point_wn(5), Fraction(244))

    def test_w5_sum(self):
        """kappa(W_5) + kappa'(W_5) = 9394/15."""
        expected = anomaly_ratio(5) * koszul_conductor_wn(5)
        self.assertEqual(expected, Fraction(9394, 15))
        for c in [1, 244, 400]:
            s = kappa_wn(5, Fraction(c)) + kappa_dual_wn(5, Fraction(c))
            self.assertEqual(s, expected)

    def test_wn_level_independence(self):
        """kappa + kappa' is level-independent for W_N (N=2..7)."""
        for N in range(2, 8):
            r = verify_wn_complementarity_level_independence(N)
            self.assertTrue(r["all_ok"], f"Level independence failed for W_{N}")

    def test_wn_self_dual_points(self):
        """W_N self-dual at c = K_N/2."""
        for N in range(2, 8):
            c_star = self_dual_point_wn(N)
            kap = kappa_wn(N, c_star)
            kap_dual = kappa_dual_wn(N, c_star)
            self.assertEqual(kap, kap_dual, f"Not self-dual at c*={c_star} for W_{N}")

    def test_virasoro_is_w2(self):
        """Virasoro = W_2: same kappa, K, rho, self-dual point."""
        for c in [1, 13, 26]:
            self.assertEqual(kappa_virasoro(c), kappa_wn(2, Fraction(c)))
        self.assertEqual(koszul_conductor_wn(2), 26)
        self.assertEqual(anomaly_ratio(2), Fraction(1, 2))
        self.assertEqual(self_dual_point_wn(2), Fraction(13))


class TestWNCentralCharge(unittest.TestCase):
    """Test W_N central charge from DS reduction."""

    def test_virasoro_central_charge(self):
        """c(W_2, k) = 1 - 6(k+1)^2/(k+2)."""
        # At k=1: c = 1 - 6*4/3 = 1 - 8 = -7
        self.assertEqual(central_charge_wn(2, Fraction(1)), Fraction(-7))
        # At k=0: c = 1 - 6*1/2 = 1 - 3 = -2
        self.assertEqual(central_charge_wn(2, Fraction(0)), Fraction(-2))

    def test_w3_central_charge(self):
        """c(W_3, k) = 2 - 24(k+2)^2/(k+3)."""
        # At k=1: c = 2 - 24*9/4 = 2 - 54 = -52
        self.assertEqual(central_charge_wn(3, Fraction(1)), Fraction(-52))

    def test_c_sum_equals_K(self):
        """c(k) + c(k') = K_N for all N and k."""
        for N in range(2, 8):
            K = koszul_conductor_wn(N)
            for k in [Fraction(1), Fraction(2), Fraction(3), Fraction(-1)]:
                if k + N == 0:
                    continue
                k_dual = -k - 2 * N
                if k_dual + N == 0:
                    continue
                c_sum = central_charge_wn(N, k) + central_charge_wn(N, k_dual)
                self.assertEqual(c_sum, K, f"Failed for W_{N} at k={k}")


class TestBetagammaDetails(unittest.TestCase):
    """Detailed tests for betagamma complementarity."""

    def test_betagamma_symmetry(self):
        """kappa_bg(lam) = kappa_bg(1-lam) for all lam."""
        r = verify_betagamma_symmetry()
        self.assertTrue(r["all_ok"])

    def test_betagamma_standard_values(self):
        """Standard bg values: lam=0 or 1 gives kappa=1, lam=1/2 gives kappa=-1/2."""
        self.assertEqual(kappa_betagamma(Fraction(0)), 1)
        self.assertEqual(kappa_betagamma(Fraction(1)), 1)
        self.assertEqual(kappa_betagamma(Fraction(1, 2)), Fraction(-1, 2))

    def test_betagamma_at_lambda2(self):
        """bg at lambda=2: c=26, kappa=13 (same as Virasoro at c=26)."""
        self.assertEqual(kappa_betagamma(Fraction(2)), 13)

    def test_bc_is_negative_bg(self):
        """kappa_bc = -kappa_bg for all lambda."""
        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2)]:
            self.assertEqual(kappa_bc(lam), -kappa_betagamma(lam))

    def test_dual_identities(self):
        """kappa_dual_bg = kappa_bc and kappa_dual_bc = kappa_bg."""
        for lam in [Fraction(0), Fraction(1, 2), Fraction(1)]:
            self.assertEqual(kappa_dual_betagamma(lam), kappa_bc(lam))
            self.assertEqual(kappa_dual_bc(lam), kappa_betagamma(lam))


class TestSelfDualPoints(unittest.TestCase):
    """Test self-dual points for all W-algebra families."""

    def test_all_self_dual_points(self):
        """Verify self-dual points for Virasoro and W_N."""
        r = verify_self_dual_points()

        # Virasoro
        self.assertTrue(r["virasoro"]["c_13_self_dual"])
        self.assertTrue(r["virasoro"]["c_26_NOT_self_dual"])

        # W_N
        for N in range(2, 8):
            self.assertTrue(r[f"W_{N}"]["self_dual"], f"W_{N} not self-dual at c*")

    def test_self_dual_kappa_values(self):
        """At self-dual point: kappa = kappa' = rho * K / 2."""
        for N in range(2, 8):
            c_star = self_dual_point_wn(N)
            kap = kappa_wn(N, c_star)
            kap_dual = kappa_dual_wn(N, c_star)
            self.assertEqual(kap, kap_dual)
            expected = anomaly_ratio(N) * koszul_conductor_wn(N) / 2
            self.assertEqual(kap, expected)


class TestComplementarityDatum(unittest.TestCase):
    """Test the ComplementarityDatum data structures."""

    def test_heisenberg_datum(self):
        d = datum_heisenberg(Fraction(1))
        self.assertEqual(d.kappa, 1)
        self.assertEqual(d.kappa_dual, -1)
        self.assertEqual(d.kappa_sum, 0)

    def test_free_fermion_datum(self):
        d = datum_free_fermion()
        self.assertEqual(d.kappa, Fraction(1, 4))
        self.assertEqual(d.kappa_dual, Fraction(-1, 4))
        self.assertEqual(d.kappa_sum, 0)

    def test_lattice_datum(self):
        d = datum_lattice(8)
        self.assertEqual(d.kappa, 8)
        self.assertEqual(d.kappa_dual, -8)
        self.assertEqual(d.kappa_sum, 0)

    def test_betagamma_datum(self):
        d = datum_betagamma(Fraction(1))
        self.assertEqual(d.kappa, 1)
        self.assertEqual(d.kappa_dual, -1)
        self.assertEqual(d.kappa_sum, 0)

    def test_affine_datum(self):
        d = datum_affine("A", 1, Fraction(1))
        self.assertEqual(d.kappa, Fraction(9, 4))
        self.assertEqual(d.kappa_dual, Fraction(-9, 4))
        self.assertEqual(d.kappa_sum, 0)
        self.assertEqual(d.K, 6)

    def test_virasoro_datum(self):
        d = datum_virasoro(Fraction(13))
        self.assertEqual(d.kappa, Fraction(13, 2))
        self.assertEqual(d.kappa_dual, Fraction(13, 2))
        self.assertEqual(d.kappa_sum, 13)
        self.assertEqual(d.K, 26)
        self.assertEqual(d.rho, Fraction(1, 2))
        self.assertEqual(d.self_dual, 13)

    def test_wn_datum(self):
        d = datum_wn(3, Fraction(50))
        self.assertEqual(d.kappa, Fraction(125, 3))
        self.assertEqual(d.kappa_dual, Fraction(125, 3))
        self.assertEqual(d.kappa_sum, Fraction(250, 3))
        self.assertEqual(d.K, 100)
        self.assertEqual(d.rho, Fraction(5, 6))
        self.assertEqual(d.self_dual, 50)


class TestLandscapeTable(unittest.TestCase):
    """Test the full landscape table generation."""

    def test_landscape_not_empty(self):
        data = full_complementarity_landscape()
        self.assertGreater(len(data), 20)

    def test_all_kappa_sums_correct(self):
        """Every datum in the landscape has kappa + kappa' = kappa_sum."""
        for d in full_complementarity_landscape():
            computed = d.kappa + d.kappa_dual
            self.assertEqual(
                computed, d.kappa_sum,
                f"Sum mismatch for {d.display_name}: {computed} != {d.kappa_sum}"
            )

    def test_summary_table(self):
        rows = landscape_summary_table()
        self.assertGreater(len(rows), 15)
        # Check at least one free-field and one W-algebra
        families = [r["family"] for r in rows]
        self.assertIn("Heisenberg", families)
        self.assertIn("W_3", families)


class TestFullAudit(unittest.TestCase):
    """Run the full landscape audit."""

    def test_full_audit_passes(self):
        """The complete audit of all families passes."""
        audit = full_landscape_audit()
        self.assertTrue(
            audit["affine_antisymmetry"]["all_ok"],
            "Affine antisymmetry failed"
        )
        self.assertTrue(
            audit["affine_cc_sum"]["all_ok"],
            "Affine central charge sum failed"
        )
        self.assertTrue(
            audit["koszul_conductor"]["all_ok"],
            "Koszul conductor formula failed"
        )
        self.assertTrue(
            audit["wn_level_independence"]["all_ok"],
            "W_N level independence failed"
        )
        self.assertTrue(
            audit["betagamma_symmetry"]["all_ok"],
            "betagamma symmetry failed"
        )
        self.assertTrue(
            audit["free_field_sums"]["all_ok"],
            "Free field sums failed"
        )


class TestCrossCheck(unittest.TestCase):
    """Cross-checks with existing compute modules."""

    def test_kappa_matches_envelope_shadow_functor(self):
        """kappa values match envelope_shadow_functor.py."""
        try:
            from compute.lib.envelope_shadow_functor import (
                kappa_heisenberg as esf_heis,
                kappa_virasoro as esf_vir,
                kappa_w3 as esf_w3,
                kappa_wN as esf_wn,
                kappa_betagamma as esf_bg,
            )
            self.assertEqual(
                kappa_heisenberg(Fraction(1)),
                esf_heis(Fraction(1))
            )
            self.assertEqual(
                kappa_virasoro(Fraction(13)),
                esf_vir(Fraction(13))
            )
            self.assertEqual(
                kappa_wn(3, Fraction(50)),
                esf_w3(Fraction(50))
            )
            self.assertEqual(
                kappa_wn(4, Fraction(12)),
                esf_wn(4, Fraction(12))
            )
            self.assertEqual(
                kappa_betagamma(Fraction(1)),
                esf_bg(Fraction(1))
            )
        except ImportError:
            self.skipTest("envelope_shadow_functor not available")

    def test_kappa_matches_theorem_c(self):
        """kappa values match theorem_c_complementarity.py."""
        try:
            from compute.lib.theorem_c_complementarity import (
                kappa as tc_kappa,
                kappa_dual as tc_kappa_dual,
                complementarity_sum as tc_sum,
            )
            # Heisenberg
            self.assertEqual(
                kappa_heisenberg(Fraction(1)),
                tc_kappa("heisenberg", k=1)
            )
            # Virasoro
            self.assertEqual(
                kappa_virasoro(Fraction(13)),
                tc_kappa("virasoro", c=13)
            )
            # sum
            self.assertEqual(
                complementarity_sum_wn(2),
                tc_sum("virasoro", c=1)
            )
        except ImportError:
            self.skipTest("theorem_c_complementarity not available")

    def test_K_N_matches_ds_shadow_functor(self):
        """K_N values match ds_shadow_functor.py."""
        try:
            from compute.lib.ds_shadow_functor import (
                koszul_conductor_wN as dsf_K,
            )
            for N in range(2, 8):
                self.assertEqual(
                    koszul_conductor_wn(N),
                    dsf_K(N),
                    f"K_{N} mismatch"
                )
        except ImportError:
            self.skipTest("ds_shadow_functor not available")


class TestHarmonicNumbers(unittest.TestCase):
    """Test harmonic number computation."""

    def test_harmonic_values(self):
        self.assertEqual(harmonic(1), Fraction(1))
        self.assertEqual(harmonic(2), Fraction(3, 2))
        self.assertEqual(harmonic(3), Fraction(11, 6))
        self.assertEqual(harmonic(4), Fraction(25, 12))
        self.assertEqual(harmonic(5), Fraction(137, 60))

    def test_anomaly_ratio_from_harmonic(self):
        """rho_N = H_N - 1."""
        for N in range(2, 10):
            self.assertEqual(anomaly_ratio(N), harmonic(N) - 1)


class TestComplementarityFormula(unittest.TestCase):
    """Test the complementarity theorem: kappa + kappa' = rho * K."""

    def test_free_field_class(self):
        """All free-field systems: kappa + kappa' = 0."""
        self.assertEqual(complementarity_sum_heisenberg(Fraction(1)), 0)
        self.assertEqual(complementarity_sum_free_fermion(), 0)
        self.assertEqual(complementarity_sum_lattice(24), 0)
        self.assertEqual(complementarity_sum_betagamma(Fraction(1)), 0)

    def test_affine_class(self):
        """All affine KM: kappa + kappa' = 0."""
        for lt, rk in [("A", 1), ("A", 2), ("B", 2), ("G", 2), ("E", 8)]:
            self.assertEqual(
                complementarity_sum_affine(lt, rk), 0,
                f"Failed for {lt}_{rk}"
            )

    def test_w_algebra_class(self):
        """All W_N: kappa + kappa' = rho_N * K_N ≠ 0."""
        expected = {
            2: Fraction(13),       # Virasoro
            3: Fraction(250, 3),   # W_3
            4: Fraction(533, 2),   # W_4
            5: Fraction(9394, 15), # W_5
        }
        for N, exp in expected.items():
            self.assertEqual(
                complementarity_sum_wn(N), exp,
                f"Failed for W_{N}: got {complementarity_sum_wn(N)}, expected {exp}"
            )

    def test_w_algebra_nonzero(self):
        """W_N complementarity sum is NEVER zero for N >= 2."""
        for N in range(2, 15):
            s = complementarity_sum_wn(N)
            self.assertNotEqual(s, 0, f"W_{N} sum unexpectedly zero")

    def test_complementarity_sum_formula(self):
        """kappa + kappa' = rho * K for W_N, verified algebraically."""
        for N in range(2, 10):
            rho = anomaly_ratio(N)
            K = Fraction(koszul_conductor_wn(N))
            expected = rho * K
            # Verify via kappa functions at generic c
            c = Fraction(7)  # arbitrary
            s = kappa_wn(N, c) + kappa_dual_wn(N, c)
            self.assertEqual(s, expected, f"Formula failed for W_{N}")


class TestAP24Compliance(unittest.TestCase):
    """Anti-pattern AP24 compliance: kappa + kappa' ≠ 0 for W-algebras."""

    def test_virasoro_sum_is_13_not_0(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        s = kappa_virasoro(Fraction(1)) + kappa_dual_virasoro(Fraction(1))
        self.assertEqual(s, 13)
        self.assertNotEqual(s, 0)

    def test_w3_sum_nonzero(self):
        """AP24: kappa(W_3) + kappa'(W_3) = 250/3, NOT 0."""
        s = kappa_wn(3, Fraction(2)) + kappa_dual_wn(3, Fraction(2))
        self.assertEqual(s, Fraction(250, 3))
        self.assertNotEqual(s, 0)

    def test_km_sum_IS_zero(self):
        """AP24: kappa(g_k) + kappa'(g_k) = 0 for KM. This is the CORRECT case."""
        s = kappa_affine("A", 1, Fraction(1)) + kappa_dual_affine("A", 1, Fraction(1))
        self.assertEqual(s, 0)


if __name__ == "__main__":
    unittest.main()
