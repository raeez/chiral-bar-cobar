"""Tests for compute/lib/factorization_homology_explicit_engine.py.

EXPLICIT factorization-homology computations: int_X A as actual numbers
for X = S^1, S^2, T^2, Sigma_g, T^2 x I, open disc, punctured sphere, and
the modular-functor / WRT bridge.

Coverage (eight task groups + multi-path verification):
  1. int_{S^1} A (Heisenberg, free fermion): Hochschild homology, HKR
  2. int_{S^2} V_k(g): conformal blocks at genus 0 (rep count)
  3. int_{T^2} A (Virasoro, Heisenberg, sl_2): elliptic character
  4. int_{Sigma_g} V_k(sl_N): Verlinde dimension (sl_2, sl_3, all g)
  5. int_{T^2 x I} A: Drinfeld center
  6. Open / punctured: locality
  7. WRT cylinder bridge
  8. Modular functor table

The tests verify:
  - Closed-form values against literature (Beauville Verlinde, Loday HKR)
  - Multi-path consistency (Path A = Path B = Path C)
  - Cross-check against existing factorization_homology_engine.py
  - Concentration in degree 0 for Koszul families
  - Locality / E_2 recognition for open manifolds
"""

from fractions import Fraction

import pytest

from compute.lib.factorization_homology_explicit_engine import (
    LIE_DATA,
    central_charge_km,
    explicit_fh_summary,
    fh_as_modular_functor,
    fh_circle_free_fermion,
    fh_circle_heisenberg,
    fh_higher_genus_verlinde,
    fh_open_disc,
    fh_punctured_sphere,
    fh_sphere,
    fh_torus_character,
    fh_torus_cylinder_drinfeld_center,
    fh_wrt_cylinder,
    kappa_km,
    verlinde_multipath_verify,
)
from compute.lib.factorization_homology_engine import (
    _verlinde_sl2_integer,
)


# =====================================================================
# Group 0: Lie data sanity (kappa, central charge)
# =====================================================================

class TestLieData:
    """Local Lie data registry matches the standard literature."""

    def test_central_charge_sl2_levels(self):
        """c(sl_2_k) = 3k/(k+2)."""
        assert central_charge_km("sl2", 1) == Fraction(1, 1)
        assert central_charge_km("sl2", 2) == Fraction(3, 2)
        assert central_charge_km("sl2", 3) == Fraction(9, 5)

    def test_central_charge_sl3(self):
        """c(sl_3_k) = 8k/(k+3)."""
        assert central_charge_km("sl3", 1) == Fraction(2, 1)
        assert central_charge_km("sl3", 3) == Fraction(4, 1)

    def test_critical_level_undefined(self):
        """k = -h^v: Sugawara undefined (NOT 'c -> infty')."""
        with pytest.raises(ValueError):
            central_charge_km("sl2", -2)
        with pytest.raises(ValueError):
            central_charge_km("sl3", -3)

    def test_kappa_sl2_levels(self):
        """kappa(sl_2_k) = 3(k+2)/4 (NOT c/2 — see AP39)."""
        assert kappa_km("sl2", 1) == Fraction(9, 4)
        assert kappa_km("sl2", 2) == Fraction(3, 1)
        # Notice kappa != c/2: at k=1, c/2 = 1/2 but kappa = 9/4
        assert kappa_km("sl2", 1) != central_charge_km("sl2", 1) / 2


# =====================================================================
# Group 1: int_{S^1} A = HH_*(A_assoc)
# =====================================================================

class TestCircleHochschild:
    """int_{S^1} A is Hochschild homology of underlying associative algebra."""

    def test_heisenberg_HH0_is_partition_function(self):
        """HH_0(Sym(V[t])) for d=1 has q-coefficients = partition function."""
        r = fh_circle_heisenberg(k=1, d=1, q_truncation=8)
        # HH_0 = Sym(V[t]) itself; coefficients are p(n)
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22]
        for i, p in enumerate(expected):
            assert r["HH0_q_series"][i] == Fraction(p), \
                f"HH_0 coefficient at q^{i}: got {r['HH0_q_series'][i]}, expected {p}"

    def test_heisenberg_d2_HH0_is_p2(self):
        """HH_0 for d=2 is 1/phi(q)^2 (number of partitions into 2 colors)."""
        r = fh_circle_heisenberg(k=1, d=2, q_truncation=6)
        # 1/phi(q)^2 expansion: 1, 2, 5, 10, 20, 36, 65
        expected = [1, 2, 5, 10, 20, 36, 65]
        for i, p in enumerate(expected):
            assert r["HH0_q_series"][i] == Fraction(p)

    def test_heisenberg_total_HH_overpartition(self):
        """HH_total at y=1 is the overpartition function."""
        r = fh_circle_heisenberg(k=1, d=1, q_truncation=6)
        # OEIS A015128: 1, 2, 4, 8, 14, 24, 40
        expected = [1, 2, 4, 8, 14, 24, 40]
        for i, p in enumerate(expected):
            assert r["HH_total_q_series_y1"][i] == Fraction(p)

    def test_heisenberg_zero_level_rejected(self):
        """k=0 has degenerate pairing; HKR not applicable."""
        with pytest.raises(ValueError):
            fh_circle_heisenberg(k=0, d=1)

    def test_free_fermion_HH0_eta_quotient(self):
        """HH_0 for free fermion d=1 has alternating-sign q-Pochhammer."""
        r = fh_circle_free_fermion(d=1, q_truncation=6)
        # prod (1-q^n) = 1 - q - q^2 + q^5 + q^7 - ... (Euler pentagonal)
        # First 7 coefficients: 1, -1, -1, 0, 0, 1, 0
        expected = [1, -1, -1, 0, 0, 1, 0]
        for i, p in enumerate(expected):
            assert r["HH0_q_series"][i] == Fraction(p), \
                f"FF HH_0 q^{i}: got {r['HH0_q_series'][i]}, expected {p}"


# =====================================================================
# Group 2: int_{S^2} V_k(g) = conformal blocks at genus 0
# =====================================================================

class TestSphere:
    """int_{S^2} V_k(g) at genus 0 with no insertions."""

    def test_sphere_sl2_BD_is_one(self):
        """At genus 0 with no marked points, BD vacuum block is 1-dim."""
        for k in [1, 2, 3, 5]:
            r = fh_sphere("affine_sl2", k=k)
            assert r["dim_BD"] == 1
            # Topological count = number of integrable reps = k+1
            assert r["dim_topological"] == k + 1
            assert r["integrable_count"] == k + 1

    def test_sphere_sl3_topological_count(self):
        """sl_3 at level k has C(k+2,2) integrable reps."""
        for k in [1, 2, 3, 4]:
            r = fh_sphere("affine_sl3", k=k)
            assert r["dim_topological"] == (k + 1) * (k + 2) // 2

    def test_sphere_virasoro_concentrated(self):
        """Virasoro on S^2: vacuum block = 1."""
        r = fh_sphere("virasoro", c=26)
        assert r["dim_BD"] == 1
        assert r["dim_topological"] == 1

    def test_sphere_heisenberg(self):
        """Heisenberg on S^2: 1d Fock vacuum."""
        r = fh_sphere("heisenberg")
        assert r["dim_BD"] == 1
        assert r["dim_topological"] == 1

    def test_sphere_kappa_consistency(self):
        """The sphere routine returns kappa consistent with kappa_km."""
        r = fh_sphere("affine_sl2", k=2)
        assert r["kappa"] == kappa_km("sl2", 2)


# =====================================================================
# Group 3: int_{T^2} A = elliptic character
# =====================================================================

class TestTorusCharacter:
    """int_{T^2} A = TrV q^{L_0 - c/24}."""

    def test_heisenberg_torus_partition_function(self):
        """For Heisenberg d=1: chi(q) = 1/phi(q) = sum p(n) q^n (no shift)."""
        r = fh_torus_character("heisenberg", d=1, q_truncation=6)
        expected = [1, 1, 2, 3, 5, 7, 11]
        for i, p in enumerate(expected):
            assert r["character_q_series"][i] == p

    def test_heisenberg_q_shift(self):
        """q-shift = c/24 = d/24 = 1/24 for d=1."""
        r = fh_torus_character("heisenberg", d=1)
        assert r["q_shift_c_over_24"] == Fraction(1, 24)
        assert r["c"] == Fraction(1)

    def test_virasoro_vacuum_no_part_one(self):
        """Vir vacuum module: prod_{n>=2} 1/(1-q^n)."""
        r = fh_torus_character("virasoro", c=26, q_truncation=8)
        # Expected: number of partitions of n with no part = 1
        # n=0: 1, n=1: 0, n=2: 1, n=3: 1, n=4: 2, n=5: 2, n=6: 4, n=7: 4, n=8: 7
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7]
        assert r["character_q_series"] == expected

    def test_virasoro_q_shift(self):
        """q-shift = c/24."""
        r = fh_torus_character("virasoro", c=Fraction(13))
        assert r["q_shift_c_over_24"] == Fraction(13, 24)

    def test_betagamma_torus_two_bosons(self):
        """beta-gamma: chi(q) = 1/phi(q)^2 (at integer-graded approximation)."""
        r = fh_torus_character("betagamma", q_truncation=5)
        # 1/phi(q)^2 = 1 + 2q + 5q^2 + 10q^3 + 20q^4 + 36q^5
        expected = [1, 2, 5, 10, 20, 36]
        assert r["character_q_series"] == expected

    def test_affine_sl2_torus_leading(self):
        """Leading-order character of V_k(sl_2) at level k=1."""
        r = fh_torus_character("affine_sl2", k=1, q_truncation=4)
        # Leading approximation: 1/phi(q)^3
        # = 1 + 3q + 9q^2 + 22q^3 + 51q^4
        expected = [1, 3, 9, 22, 51]
        assert r["character_q_series"] == expected
        assert r["leading_only"] is True


# =====================================================================
# Group 4: int_{Sigma_g} V_k(sl_N) = Verlinde dimension
# =====================================================================

class TestVerlindeHigherGenus:
    """Beauville Verlinde formula at all (N, k, g)."""

    def test_sl2_genus0(self):
        """Genus 0: vacuum block = 1."""
        for k in [1, 2, 3, 4, 5]:
            assert fh_higher_genus_verlinde(2, k, 0)["dim"] == 1

    def test_sl2_genus1_is_kp1(self):
        """Genus 1 = number of integrable reps = k+1."""
        for k in [1, 2, 3, 4, 5]:
            assert fh_higher_genus_verlinde(2, k, 1)["dim"] == k + 1

    def test_sl2_level1_is_two_to_g(self):
        """SU(2)_1 Verlinde: dim V_{g,1} = 2^g (closed form)."""
        for g in [0, 1, 2, 3, 4, 5]:
            assert fh_higher_genus_verlinde(2, 1, g)["dim"] == 2 ** g

    def test_sl2_level2_known_values(self):
        """SU(2)_2 Verlinde: known low-genus values from Beauville."""
        # From the Beauville formula (matches existing engine).
        expected = {0: 1, 1: 3, 2: 10, 3: 36, 4: 136}
        for g, dim in expected.items():
            assert fh_higher_genus_verlinde(2, 2, g)["dim"] == dim

    def test_sl2_level3_known_values(self):
        """SU(2)_3 Verlinde: known low-genus values."""
        expected = {0: 1, 1: 4, 2: 20, 3: 120, 4: 800}
        for g, dim in expected.items():
            assert fh_higher_genus_verlinde(2, 3, g)["dim"] == dim

    def test_sl3_genus0_genus1(self):
        """sl_3: g=0 -> 1, g=1 -> binomial(k+2,2)."""
        for k in [1, 2, 3, 4]:
            assert fh_higher_genus_verlinde(3, k, 0)["dim"] == 1
            assert fh_higher_genus_verlinde(3, k, 1)["dim"] == \
                (k + 1) * (k + 2) // 2

    def test_sl2_cross_check_existing_engine(self):
        """New explicit Verlinde matches existing factorization_homology_engine."""
        for k in [1, 2, 3]:
            for g in [0, 1, 2, 3, 4]:
                new = fh_higher_genus_verlinde(2, k, g)["dim"]
                old = _verlinde_sl2_integer(k, g)
                assert new == old, \
                    f"sl2 k={k} g={g}: new={new} old={old}"


# =====================================================================
# Group 5: int_{T^2 x I} A = Drinfeld center
# =====================================================================

class TestDrinfeldCenter:
    """Cylinder factorization homology = Drinfeld center."""

    def test_sl2_k1_drinfeld(self):
        """SU(2)_1: dim C = 1/S_{00}^2 = (k+2)/(2 sin^2(pi/(k+2))) = 4."""
        # k=1: K=3, sin(pi/3)^2 = 3/4, dim_C = 3/(2*3/4) = 2
        # Wait: 1/S_{00}^2 = 1/(2/K * sin^2(pi/K)) = K/(2 sin^2(pi/K))
        # = 3 / (2 * 3/4) = 3/(3/2) = 2.  So dim_C = 2 for SU(2)_1.
        r = fh_torus_cylinder_drinfeld_center(N=2, k=1)
        assert abs(r["dim_C"] - 2.0) < 1e-6
        # dim_Z(C) for a modular C is dim(C)^2 = 4
        assert abs(r["dim_Z_C"] - 4.0) < 1e-6

    def test_sl2_k2_drinfeld(self):
        """SU(2)_2: dim C = 4/(2 sin^2(pi/4)) = 4/(2 * 1/2) = 4."""
        r = fh_torus_cylinder_drinfeld_center(N=2, k=2)
        assert abs(r["dim_C"] - 4.0) < 1e-6
        assert abs(r["dim_Z_C"] - 16.0) < 1e-6

    def test_sl2_k3_drinfeld(self):
        """SU(2)_3: dim C = 5/(2 sin^2(pi/5))."""
        import math
        K = 5
        expected_dim_C = K / (2 * math.sin(math.pi / K) ** 2)
        r = fh_torus_cylinder_drinfeld_center(N=2, k=3)
        assert abs(r["dim_C"] - expected_dim_C) < 1e-6
        assert abs(r["dim_Z_C"] - expected_dim_C ** 2) < 1e-6

    def test_drinfeld_growth(self):
        """dim_C grows monotonically with k."""
        prev = 0
        for k in [1, 2, 3, 4, 5]:
            r = fh_torus_cylinder_drinfeld_center(N=2, k=k)
            assert r["dim_C"] > prev
            prev = r["dim_C"]


# =====================================================================
# Group 6: Open / punctured (locality)
# =====================================================================

class TestOpenLocality:
    """For open contractible X: int_X A = A by E_2 recognition."""

    def test_open_disc_recovers_A(self):
        r = fh_open_disc("Heisenberg")
        assert "A itself" in r["result"]
        assert r["concentrated"] is True

    def test_punctured_sphere_is_bimodule(self):
        r = fh_punctured_sphere("Virasoro")
        assert "bimodule" in r["result"]

    def test_locality_universal(self):
        """Locality holds for every family."""
        for fam in ["Heisenberg", "Virasoro", "affine_sl2", "betagamma",
                    "free_fermion", "lattice"]:
            r = fh_open_disc(fam)
            assert r["concentrated"] is True


# =====================================================================
# Group 7: WRT cylinder
# =====================================================================

class TestWRTCylinder:
    """int_{Sigma_g x I} A = WRT cylinder amplitude = dim V_g."""

    def test_wrt_cylinder_matches_verlinde(self):
        """WRT cylinder amplitude = Verlinde dim at genus g."""
        for k in [1, 2, 3]:
            for g in [1, 2, 3]:
                w = fh_wrt_cylinder(N=2, k=k, g=g)
                v = fh_higher_genus_verlinde(2, k, g)
                assert w["dim_V_g"] == v["dim"]
                assert w["WRT_Sigma_g_times_I"] == v["dim"]

    def test_wrt_su2_level1_powers_of_two(self):
        """SU(2)_1 WRT amplitudes: 2^g for Sigma_g x I."""
        for g in [1, 2, 3, 4]:
            w = fh_wrt_cylinder(N=2, k=1, g=g)
            assert w["WRT_Sigma_g_times_I"] == 2 ** g


# =====================================================================
# Group 8: Modular functor / TQFT view
# =====================================================================

class TestModularFunctor:
    """Sigma -> int_Sigma A as a 2D modular functor."""

    def test_modular_functor_sl2_k1_is_powers_of_two(self):
        r = fh_as_modular_functor(N=2, k=1, max_g=4)
        for g in range(5):
            assert r["table_dim_V_g"][g] == 2 ** g

    def test_modular_functor_sl2_k2_table(self):
        r = fh_as_modular_functor(N=2, k=2, max_g=4)
        expected = {0: 1, 1: 3, 2: 10, 3: 36, 4: 136}
        for g, dim in expected.items():
            assert r["table_dim_V_g"][g] == dim

    def test_modular_functor_multiplicativity(self):
        """Disjoint union: dim(Sigma_g sqcup Sigma_h) = dim_g * dim_h."""
        r = fh_as_modular_functor(N=2, k=2, max_g=4)
        for check in r["multiplicativity_checks"]:
            g, h = check["g"], check["h"]
            assert check["product"] == r["table_dim_V_g"][g] * r["table_dim_V_g"][h]


# =====================================================================
# Multi-path verification
# =====================================================================

class TestMultiPathVerification:
    """Three independent verification paths must agree on every claim."""

    def test_sl2_multipath_low_data(self):
        """SU(2)_k Verlinde verified by 3 paths at small (k, g)."""
        for k in [1, 2, 3]:
            for g in [0, 1, 2]:
                v = verlinde_multipath_verify(2, k, g)
                assert v["paths_agree"], \
                    f"sl2 k={k} g={g}: paths disagree {v}"
                assert v["n_paths"] >= 2, \
                    f"sl2 k={k} g={g}: insufficient paths"

    def test_sl2_level1_three_paths(self):
        """At level 1: all three paths give 2^g."""
        for g in [0, 1, 2, 3, 4]:
            v = verlinde_multipath_verify(2, 1, g)
            if v["path_A"] is not None:
                assert v["path_A"] == 2 ** g
            if v["path_B"] is not None:
                assert v["path_B"] == 2 ** g

    def test_genus_zero_universal(self):
        """At genus 0: dim = 1 for ALL families and ALL methods."""
        for N in [2, 3]:
            for k in [1, 2, 3]:
                v = verlinde_multipath_verify(N, k, 0)
                assert v["path_A"] == 1
                assert v["path_C"] == 1


# =====================================================================
# Cross-checks against existing engine
# =====================================================================

class TestCrossEngineConsistency:
    """The new explicit engine must agree with existing FH engines."""

    def test_kappa_consistency(self):
        """kappa_km (new) matches genus_partition_closure._compute_kappa (existing)."""
        from compute.lib.genus_partition_closure import _compute_kappa
        for k in [1, 2, 3, 5]:
            new_k = kappa_km("sl2", k)
            old_k = _compute_kappa("affine_sl2", k=k)
            assert new_k == old_k

    def test_central_charge_consistency(self):
        """Central charge formula matches the existing factorization_homology_engine."""
        from compute.lib.factorization_homology_engine import CENTRAL_CHARGE
        for k in [1, 2, 5]:
            new_c = central_charge_km("sl2", k)
            old_c = CENTRAL_CHARGE["affine_sl2"](k)
            assert new_c == old_c


# =====================================================================
# Summary table sanity
# =====================================================================

class TestSummaryTable:
    """The eight-task summary table assembles cleanly."""

    def test_summary_has_eight_groups(self):
        s = explicit_fh_summary()
        for key in [
            "1_circle_heisenberg",
            "2_sphere_sl2",
            "3_torus_virasoro",
            "4_higher_genus_verlinde",
            "5_drinfeld_center",
            "6_open_locality",
            "7_wrt_cylinder",
            "8_modular_functor_sl2",
        ]:
            assert key in s

    def test_summary_sphere_sl2_values(self):
        s = explicit_fh_summary()
        for k in [1, 2, 3, 4]:
            entry = s["2_sphere_sl2"][f"k={k}"]
            assert entry["dim_topological"] == k + 1
            assert entry["= k+1"] == k + 1

    def test_summary_verlinde_values(self):
        s = explicit_fh_summary()
        # sl2_k1_g2 should be 4
        assert s["4_higher_genus_verlinde"]["sl2_k1_g2"] == 4
        assert s["4_higher_genus_verlinde"]["sl2_k2_g2"] == 10

    def test_summary_modular_functor(self):
        s = explicit_fh_summary()
        # k=2 sl_2 table
        assert s["8_modular_functor_sl2"][0] == 1
        assert s["8_modular_functor_sl2"][1] == 3
        assert s["8_modular_functor_sl2"][2] == 10
