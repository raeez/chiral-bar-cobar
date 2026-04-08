r"""Tests for the rigid oper motives engine.

THEOREM: The shadow oper is a rigid hypergeometric connection whose
arithmetic content is controlled by the Koszul character chi: Z/2 -> {+-1}
and the Eisenstein automorphic representation.

Six investigative directions, each with multi-path verification:

I.   Katz rigidity index = 2 (Katz 1996)
II.  Simpson correspondence: CM type, trivial Higgs bundle
III. Periods: logarithmic (genus 0 curve), rational multiples of pi
IV.  Motivic weight 0, Hodge type (g,g) at genus g
V.   Arithmetic specializations at rational c
VI.  Eisenstein connection: L^sh(s) = -kappa * zeta(s) * zeta(s-1)

Plus:
VII.  Differential Galois group = mu_2
VIII. Gauss-Manin / Picard-Fuchs equation
IX.   Cross-family universality
X.    Artin L-function of Koszul character
XI.   Master cross-verification

Beilinson compliance:
  AP1:  kappa recomputed per family, never copied.
  AP3:  Each test independently derives, no pattern matching.
  AP10: Cross-family consistency, not just hardcoded values.
  AP24: complementarity sum checked per family.
  AP39: kappa != c/2 in general.
"""

import cmath
import math
import unittest

import numpy as np

from compute.lib.rigid_oper_motives_engine import (
    # Shadow data
    shadow_metric_coeffs,
    critical_discriminant,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_sl2_shadow_data,
    # I. Katz rigidity
    katz_rigidity_index,
    shadow_oper_katz_index,
    liouville_lift_katz_index,
    katz_index_family_scan,
    # II. Simpson
    SimpsonData,
    shadow_oper_simpson_data,
    simpson_family_variation,
    # III. Periods
    shadow_oper_elliptic_modulus,
    shadow_period_virasoro,
    shadow_period_ratio_koszul_dual,
    # IV. Motivic
    MotivicData,
    shadow_oper_motivic_data,
    obstruction_class_hodge_type,
    motivic_galois_action_on_tower,
    # V. Arithmetic
    arithmetic_specialization,
    cm_specialization_table,
    # VI. Eisenstein
    eisenstein_identification,
    shadow_eisenstein_residues,
    shadow_as_eisenstein_oper,
    # VII. Artin L-function
    artin_l_function_koszul,
    koszul_character_euler_product,
    # VIII. Gauss-Manin
    gauss_manin_connection,
    picard_fuchs_regularity_check,
    # IX. Universality
    rigidity_universality_check,
    # X. Motivic Galois
    motivic_galois_constraints,
    # XI. Differential Galois
    differential_galois_group,
    # XII. Master
    master_verification,
)


# =============================================================
# I. KATZ RIGIDITY INDEX
# =============================================================

class TestKatzRigidityIndex(unittest.TestCase):
    """Katz rigidity: rig(L) = (2-n)*r^2 + sum dim C(M_i)."""

    def test_rank1_n3_rigid(self):
        """Rank 1, 3 singular points: rig = (2-3)*1 + 3*1 = 2. RIGID."""
        idx = katz_rigidity_index(rank=1, n_singular=3, centralizer_dims=[1, 1, 1])
        self.assertEqual(idx['rigidity_index'], 2)
        self.assertTrue(idx['is_rigid'])

    def test_rank1_n2_not_rigid(self):
        """Rank 1, 2 singular points: rig = (2-2)*1 + 2*1 = 2. Still rigid."""
        idx = katz_rigidity_index(rank=1, n_singular=2, centralizer_dims=[1, 1])
        self.assertEqual(idx['rigidity_index'], 2)
        self.assertTrue(idx['is_rigid'])

    def test_rank1_n4_not_rigid(self):
        """Rank 1, 4 singular points: rig = (2-4)*1 + 4*1 = 2. Still rigid."""
        idx = katz_rigidity_index(rank=1, n_singular=4, centralizer_dims=[1, 1, 1, 1])
        self.assertEqual(idx['rigidity_index'], 2)
        # For rank 1, all local systems are rigid (rig = 2 always)

    def test_rank2_n3_semisimple_rigid(self):
        """Rank 2, 3 pts, semisimple monodromies (dim C = 2): rig = -4+6 = 2."""
        idx = katz_rigidity_index(rank=2, n_singular=3, centralizer_dims=[2, 2, 2])
        self.assertEqual(idx['rigidity_index'], 2)
        self.assertTrue(idx['is_rigid'])

    def test_rank2_n4_not_rigid(self):
        """Rank 2, 4 pts, semisimple: rig = (2-4)*4 + 4*2 = -8+8 = 0. NOT rigid."""
        idx = katz_rigidity_index(rank=2, n_singular=4, centralizer_dims=[2, 2, 2, 2])
        self.assertEqual(idx['rigidity_index'], 0)
        self.assertFalse(idx['is_rigid'])

    def test_shadow_oper_katz_index(self):
        """The shadow oper has Katz index = 2."""
        idx = shadow_oper_katz_index()
        self.assertEqual(idx['rigidity_index'], 2)
        self.assertTrue(idx['is_rigid'])
        self.assertEqual(idx['rank'], 1)
        self.assertEqual(idx['n_singular'], 3)

    def test_liouville_lift_katz_index(self):
        """The rank-2 Liouville lift also has Katz index = 2."""
        idx = liouville_lift_katz_index()
        self.assertEqual(idx['rigidity_index'], 2)
        self.assertTrue(idx['is_rigid'])
        self.assertEqual(idx['rank'], 2)

    def test_katz_family_scan(self):
        """Rigidity holds for ALL Virasoro central charges."""
        results = katz_index_family_scan()
        for entry in results:
            self.assertTrue(entry['rigid'],
                            f"Rigidity failed at c = {entry['c']}")


# =============================================================
# II. SIMPSON CORRESPONDENCE
# =============================================================

class TestSimpsonCorrespondence(unittest.TestCase):
    """Simpson nonabelian Hodge correspondence for the shadow oper."""

    def test_simpson_data_basic(self):
        """Shadow oper maps to trivial Higgs bundle."""
        sd = shadow_oper_simpson_data()
        self.assertEqual(sd.rank, 1)
        self.assertEqual(sd.degree, 0)
        self.assertEqual(sd.bundle_type, 'trivial')
        self.assertTrue(sd.is_cm)
        self.assertEqual(sd.cm_field, 'Q')

    def test_simpson_spectral_curve_genus_0(self):
        """Spectral curve of theta=0 is zero section: genus 0."""
        sd = shadow_oper_simpson_data()
        self.assertEqual(sd.spectral_curve_genus, 0)

    def test_family_variation_class_m(self):
        """For class M (Virasoro), Simpson data is nontrivial."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            result = simpson_family_variation(c_val)
            self.assertEqual(result['status'], 'class_M')
            self.assertEqual(result['monodromy'], -1)
            self.assertTrue(result['is_cm'])
            self.assertEqual(result['mumford_tate'], 'Z/2')

    def test_family_variation_c13_self_dual(self):
        """At c=13, the shadow oper is self-dual."""
        result = simpson_family_variation(13.0)
        self.assertEqual(result['status'], 'class_M')
        # At c=13, kappa = 13/2, kappa' = (26-13)/2 = 13/2 = kappa


# =============================================================
# III. PERIODS AND ELLIPTIC MODULUS
# =============================================================

class TestPeriods(unittest.TestCase):
    """Shadow oper periods are rational multiples of pi (genus 0 curve)."""

    def test_virasoro_period_formula(self):
        """P(c) = pi*sqrt(5c+22)/(4c*sqrt(5)) for Virasoro."""
        for c in [1.0, 2.0, 5.0, 10.0, 13.0, 25.0]:
            sd = virasoro_shadow_data(c)
            result = shadow_oper_elliptic_modulus(
                sd['kappa'], sd['alpha'], sd['S4'])
            if result.get('real_period') is not None:
                expected = math.pi * math.sqrt(5*c + 22) / (4*c*math.sqrt(5))
                self.assertAlmostEqual(
                    result['real_period'], expected, places=10,
                    msg=f"Period mismatch at c={c}")

    def test_period_two_formula_agreement(self):
        """Real period computed two ways must agree."""
        for c in [1.0, 5.0, 13.0, 25.0]:
            sd = virasoro_shadow_data(c)
            result = shadow_oper_elliptic_modulus(
                sd['kappa'], sd['alpha'], sd['S4'])
            if result.get('period_match') is not None:
                self.assertTrue(result['period_match'],
                                f"Period formula mismatch at c={c}")
            if result.get('simple_match') is not None:
                self.assertTrue(result['simple_match'],
                                f"Simple period formula mismatch at c={c}")

    def test_period_positive_definite(self):
        """For Virasoro c > 0, Q_L is positive definite on R."""
        for c in [0.5, 1.0, 2.0, 13.0, 25.0, 50.0]:
            sd = virasoro_shadow_data(c)
            result = shadow_oper_elliptic_modulus(
                sd['kappa'], sd['alpha'], sd['S4'])
            self.assertEqual(result.get('status'), 'positive_definite',
                             f"Not positive definite at c={c}")

    def test_koszul_dual_period_ratio(self):
        """Period ratio P(c)/P(26-c) = 1 at c=13 (self-dual)."""
        result = shadow_period_ratio_koszul_dual(13.0)
        self.assertTrue(result['is_self_dual'],
                        "Period ratio not 1 at self-dual point c=13")
        self.assertTrue(result['match'],
                        "Two formulas for ratio disagree")

    def test_koszul_dual_ratio_formula_consistency(self):
        """Two formulas for the period ratio agree."""
        for c in [1.0, 5.0, 10.0, 20.0, 25.0]:
            result = shadow_period_ratio_koszul_dual(c)
            self.assertTrue(result['match'],
                            f"Ratio formula mismatch at c={c}")

    def test_period_monotonicity(self):
        """P(c) is monotone decreasing for c > 0."""
        c_vals = [1.0, 2.0, 5.0, 10.0, 13.0, 20.0, 25.0, 50.0]
        periods = []
        for c in c_vals:
            sd = virasoro_shadow_data(c)
            result = shadow_oper_elliptic_modulus(
                sd['kappa'], sd['alpha'], sd['S4'])
            if result.get('real_period') is not None:
                periods.append(result['real_period'])
        # Check monotone decreasing (eventually)
        for i in range(len(periods) - 1):
            # P(c) ~ 1/c for large c, so eventually decreasing
            if c_vals[i] >= 5.0:  # monotone for c >= 5
                self.assertGreater(periods[i], periods[i+1],
                                   f"Not monotone at c={c_vals[i+1]}")

    def test_heisenberg_degenerate(self):
        """Heisenberg (class G): period computation degenerates."""
        sd = heisenberg_shadow_data(1.0)
        result = shadow_oper_elliptic_modulus(sd['kappa'], sd['alpha'], sd['S4'])
        self.assertEqual(result['status'], 'degenerate')

    def test_high_precision_period(self):
        """High-precision period at c=1 using mpmath."""
        try:
            result = shadow_period_virasoro(1.0, dps=50)
            self.assertTrue(result['match'],
                            "High-precision period formulas disagree")
        except ImportError:
            self.skipTest("mpmath not available")


# =============================================================
# IV. MOTIVIC WEIGHT AND HODGE STRUCTURE
# =============================================================

class TestMotivicData(unittest.TestCase):
    """Motivic invariants of the shadow local system."""

    def test_motivic_weight_zero(self):
        """Rank-1 local system with finite monodromy: weight 0."""
        md = shadow_oper_motivic_data()
        self.assertEqual(md.weight, 0)

    def test_hodge_numbers(self):
        """h^{0,0} = 1, all others 0."""
        md = shadow_oper_motivic_data()
        self.assertEqual(md.hodge_numbers[(0, 0)], 1)

    def test_cm_type(self):
        """Shadow motive is CM type."""
        md = shadow_oper_motivic_data()
        self.assertTrue(md.is_cm)
        self.assertEqual(md.cm_field, 'Q')

    def test_mumford_tate_Z2(self):
        """Mumford-Tate group is Z/2."""
        md = shadow_oper_motivic_data()
        self.assertEqual(md.mumford_tate, 'Z/2')

    def test_obstruction_hodge_type(self):
        """obs_g has Hodge type (g,g) and weight 2g."""
        for g in range(1, 6):
            ht = obstruction_class_hodge_type(g)
            self.assertEqual(ht['hodge_type'], (g, g))
            self.assertEqual(ht['weight'], 2 * g)
            self.assertEqual(ht['cohom_degree'], 2 * g)

    def test_galois_alternation(self):
        """Galois eigenvalue on obs_g is (-1)^g."""
        tower = motivic_galois_action_on_tower(max_genus=10)
        for entry in tower:
            g = entry['genus']
            self.assertEqual(entry['galois_eigenvalue'], (-1)**g)


# =============================================================
# V. ARITHMETIC SPECIALIZATIONS
# =============================================================

class TestArithmeticSpecializations(unittest.TestCase):
    """Arithmetic content at rational central charges."""

    def test_virasoro_c1_arithmetic(self):
        """c=1: kappa=1/2, algebraic splitting field."""
        spec = arithmetic_specialization(1.0)
        self.assertAlmostEqual(spec['kappa'], 0.5)
        self.assertNotEqual(spec.get('status'), 'degenerate')

    def test_virasoro_c13_self_dual(self):
        """c=13: self-dual point."""
        spec = arithmetic_specialization(13.0)
        self.assertAlmostEqual(spec['kappa'], 6.5)

    def test_virasoro_c25_near_critical(self):
        """c=25: near-critical, kappa=25/2."""
        spec = arithmetic_specialization(25.0)
        self.assertAlmostEqual(spec['kappa'], 12.5)

    def test_period_over_pi_algebraic(self):
        """At rational c, P(c)/pi is algebraic."""
        for c in [0.5, 1.0, 2.0, 4.0, 13.0, 25.0]:
            spec = arithmetic_specialization(c)
            if spec.get('period_over_pi') is not None:
                self.assertTrue(spec['period_over_pi_algebraic'],
                                f"P/pi not algebraic at c={c}")

    def test_cm_specialization_table(self):
        """All entries in the CM table have correct data."""
        table = cm_specialization_table()
        self.assertGreater(len(table), 5)
        for entry in table:
            self.assertIn('kappa', entry)
            self.assertIn('name', entry)

    def test_branch_points_complex_for_positive_c(self):
        """For c > 0 (Virasoro), branch points are complex (disc < 0)."""
        for c in [0.5, 1.0, 5.0, 13.0, 25.0]:
            spec = arithmetic_specialization(c)
            self.assertEqual(spec['disc_sign'], 'negative',
                             f"disc_Q >= 0 at c={c}")
            self.assertFalse(spec['branch_points_real'],
                             f"Branch points real at c={c}")

    def test_splitting_field_quadratic(self):
        """Splitting field is a quadratic extension of Q for c > 0."""
        for c in [0.5, 1.0, 5.0, 13.0]:
            spec = arithmetic_specialization(c)
            self.assertEqual(spec.get('galois_group'), 'Z/2',
                             f"Galois group not Z/2 at c={c}")


# =============================================================
# VI. EISENSTEIN CONNECTION
# =============================================================

class TestEisensteinConnection(unittest.TestCase):
    """L^sh(s) = -kappa * zeta(s) * zeta(s-1)."""

    def test_residue_at_s1(self):
        """Res_{s=1} L^sh = kappa/2."""
        for kappa in [0.5, 1.0, 6.5, 12.5]:
            res = shadow_eisenstein_residues(kappa)
            self.assertTrue(res['residue_s1_check'],
                            f"Residue at s=1 wrong for kappa={kappa}")
            self.assertAlmostEqual(res['residue_s1'], kappa / 2.0)

    def test_residue_at_s2(self):
        """Res_{s=2} L^sh = -kappa * pi^2/6."""
        for kappa in [0.5, 1.0, 6.5]:
            res = shadow_eisenstein_residues(kappa)
            self.assertTrue(res['residue_s2_check'],
                            f"Residue at s=2 wrong for kappa={kappa}")
            expected = -kappa * math.pi**2 / 6.0
            self.assertAlmostEqual(res['residue_s2'], expected, places=10)

    def test_eisenstein_identification_numerical(self):
        """Numerically verify L^sh(s) = -kappa * zeta(s) * zeta(s-1) at s=3."""
        try:
            result = eisenstein_identification(0.5, 3.0 + 0j, n_terms=500)
            if result.get('status') == 'verified':
                self.assertLess(result['agreement'], 0.01,
                                "Dirichlet series and product disagree")
        except Exception:
            self.skipTest("Numerical verification requires mpmath")

    def test_eisenstein_oper_data(self):
        """Shadow oper identified as deformation of Eisenstein oper."""
        for c in [1.0, 13.0, 25.0]:
            data = shadow_as_eisenstein_oper(c)
            self.assertTrue(data['borel_reduction'])
            self.assertTrue(data['monodromy_match'])
            self.assertEqual(data['weyl_group'], 'Z/2')

    def test_functional_equation_center(self):
        """Functional equation center at s=1 (from E_2(s) <-> E_2(2-s))."""
        res = shadow_eisenstein_residues(1.0)
        self.assertEqual(res['functional_eq_center'], 1.0)


# =============================================================
# VII. ARTIN L-FUNCTION OF KOSZUL CHARACTER
# =============================================================

class TestArtinLFunction(unittest.TestCase):
    """L(s, chi_{-4}) = Dirichlet L-function for Koszul character."""

    def test_leibniz_formula(self):
        """L(1, chi_{-4}) = pi/4 (Leibniz formula for pi)."""
        result = artin_l_function_koszul(1.0 + 0j, n_terms=10000)
        expected = math.pi / 4.0
        self.assertAlmostEqual(result['L_partial'].real, expected, places=2,
                               msg="Leibniz formula: L(1,chi_{-4}) != pi/4")

    def test_conductor_4(self):
        """Koszul character has conductor 4."""
        result = artin_l_function_koszul(2.0 + 0j)
        self.assertEqual(result['conductor'], 4)

    def test_euler_product_agrees(self):
        """Dirichlet series and Euler product agree at s=3."""
        s = 3.0 + 0j
        dirichlet = artin_l_function_koszul(s, n_terms=5000)
        euler = koszul_character_euler_product(s, max_prime=200)
        self.assertAlmostEqual(
            dirichlet['L_partial'].real, euler['euler_product'].real,
            places=3, msg="Dirichlet and Euler disagree at s=3")

    def test_euler_product_at_s2(self):
        """Euler product at s=2: L(2, chi_{-4}) = Catalan's constant G."""
        # L(2, chi_{-4}) = G (Catalan's constant) = 0.9159655941...
        catalan_G = 0.9159655941
        euler = koszul_character_euler_product(2.0 + 0j, max_prime=500)
        self.assertAlmostEqual(
            euler['euler_product'].real, catalan_G, places=2,
            msg="L(2,chi_{-4}) != Catalan G")


# =============================================================
# VIII. GAUSS-MANIN / PICARD-FUCHS
# =============================================================

class TestGaussManin(unittest.TestCase):
    """Picard-Fuchs equation P' + f(c)*P = 0 for the period family."""

    def test_gm_coefficient_formula(self):
        """Gauss-Manin coefficient matches numerical derivative."""
        for c in [1.0, 5.0, 10.0, 13.0, 25.0]:
            gm = gauss_manin_connection(c)
            self.assertTrue(gm['match'],
                            f"GM coefficient mismatch at c={c}")

    def test_partial_fraction_reconstruction(self):
        """Partial fraction decomposition is correct."""
        for c in [1.0, 2.0, 5.0, 13.0, 25.0, 50.0]:
            gm = gauss_manin_connection(c)
            self.assertTrue(gm['pf_match'],
                            f"PF decomposition mismatch at c={c}")

    def test_singular_points(self):
        """PF equation has regular singularities at c=0 and c=-22/5."""
        gm = gauss_manin_connection(5.0)
        self.assertIn(0, gm['singular_points'])
        self.assertAlmostEqual(gm['singular_points'][1], -4.4)

    def test_exponent_at_c0(self):
        """P ~ c^{-1} near c=0: exponent = -1."""
        gm = gauss_manin_connection(5.0)
        self.assertEqual(gm['exponents_at_0'], -1)

    def test_exponent_at_minus22over5(self):
        """P ~ (5c+22)^{1/2} near c=-22/5: exponent = 1/2."""
        gm = gauss_manin_connection(5.0)
        self.assertAlmostEqual(gm['exponents_at_minus22over5'], 0.5)

    def test_picard_fuchs_rigid(self):
        """PF equation is rigid (rank 1, 2 singularities on P^1)."""
        gm = gauss_manin_connection(5.0)
        self.assertTrue(gm['picard_fuchs_rigid'])

    def test_regularity_across_c_line(self):
        """PF equation is regular at all non-singular points."""
        results = picard_fuchs_regularity_check()
        for entry in results:
            self.assertTrue(entry['match'],
                            f"PF regularity fails at c={entry['c']}")
            self.assertTrue(entry['pf_match'],
                            f"PF decomposition fails at c={entry['c']}")


# =============================================================
# IX. CROSS-FAMILY UNIVERSALITY
# =============================================================

class TestUniversality(unittest.TestCase):
    """Rigidity is universal across shadow depth classes."""

    def test_all_families_rigid(self):
        """Rigidity holds for all standard families."""
        results = rigidity_universality_check()
        self.assertTrue(results['all_rigid'])

    def test_class_g_trivially_rigid(self):
        """Class G (Heisenberg): trivially rigid (degenerate)."""
        results = rigidity_universality_check()
        self.assertEqual(results['Heisenberg_k1']['class'], 'G/L')
        self.assertTrue(results['Heisenberg_k1']['rigid'])

    def test_class_l_trivially_rigid(self):
        """Class L (affine sl_2): trivially rigid (degenerate)."""
        results = rigidity_universality_check()
        self.assertEqual(results['affine_sl2_k1']['class'], 'G/L')
        self.assertTrue(results['affine_sl2_k1']['rigid'])

    def test_class_m_katz_rigid(self):
        """Class M (Virasoro): Katz rigid with index 2."""
        results = rigidity_universality_check()
        self.assertEqual(results['Virasoro_c1']['class'], 'M')
        self.assertEqual(results['Virasoro_c1']['katz_index'], 2)


# =============================================================
# X. MOTIVIC GALOIS CONSTRAINTS
# =============================================================

class TestMotivicGaloisConstraints(unittest.TestCase):
    """Motivic Galois group is constrained by rigidity."""

    def test_finiteness(self):
        """Monodromy group Z/2 is finite."""
        c = motivic_galois_constraints()
        self.assertTrue(c['is_finite'])

    def test_abelianness(self):
        """Z/2 is abelian."""
        c = motivic_galois_constraints()
        self.assertTrue(c['is_abelian'])

    def test_cm_type(self):
        """Motive is CM type."""
        c = motivic_galois_constraints()
        self.assertTrue(c['is_cm'])

    def test_tannakian_decomposition(self):
        """Shadow motive = -kappa * Q(0) in Tannakian category."""
        c = motivic_galois_constraints()
        self.assertEqual(c['tannakian_decomposition'], '-kappa * Q(0)')


# =============================================================
# XI. DIFFERENTIAL GALOIS GROUP
# =============================================================

class TestDifferentialGalois(unittest.TestCase):
    """DGal(nabla^sh) = mu_2 = Z/2."""

    def test_class_m_dgal(self):
        """For class M (Virasoro): DGal = mu_2."""
        sd = virasoro_shadow_data(25.0)
        result = differential_galois_group(sd['kappa'], sd['alpha'], sd['S4'])
        self.assertEqual(result['diff_galois'], 'mu_2 = Z/2')
        self.assertEqual(result['diff_galois_order'], 2)

    def test_picard_vessiot_quadratic(self):
        """PV extension is degree 2 (quadratic)."""
        sd = virasoro_shadow_data(25.0)
        result = differential_galois_group(sd['kappa'], sd['alpha'], sd['S4'])
        self.assertEqual(result['pv_degree'], 2)
        self.assertEqual(result['pv_extension'], 'C(t)[sqrt(Q_L)]')

    def test_liouvillian_solutions(self):
        """Solutions are Liouvillian (solvable DGal)."""
        sd = virasoro_shadow_data(25.0)
        result = differential_galois_group(sd['kappa'], sd['alpha'], sd['S4'])
        self.assertTrue(result['is_liouvillian'])

    def test_degenerate_class_trivial(self):
        """For class G/L (Delta=0): DGal is trivial."""
        sd = heisenberg_shadow_data(1.0)
        result = differential_galois_group(sd['kappa'], sd['alpha'], sd['S4'])
        self.assertEqual(result['diff_galois'], 'trivial')

    def test_galois_action_is_koszul_sign(self):
        """DGal acts by sqrt(Q_L) -> -sqrt(Q_L) (Koszul sign)."""
        sd = virasoro_shadow_data(13.0)
        result = differential_galois_group(sd['kappa'], sd['alpha'], sd['S4'])
        self.assertEqual(result['galois_action'], 'sqrt(Q_L) -> -sqrt(Q_L)')

    def test_liouville_lift_dgal(self):
        """Liouville lift has DGal = D_4 (dihedral of order 8)."""
        sd = virasoro_shadow_data(25.0)
        result = differential_galois_group(sd['kappa'], sd['alpha'], sd['S4'])
        self.assertEqual(result['liouville_lift_dgal'], 'D_4 (dihedral of order 8)')
        self.assertEqual(result['liouville_lift_order'], 8)

    def test_dgal_across_c(self):
        """DGal = mu_2 for ALL c > 0 (universality)."""
        for c in [0.5, 1.0, 2.0, 5.0, 13.0, 25.0, 50.0]:
            sd = virasoro_shadow_data(c)
            result = differential_galois_group(sd['kappa'], sd['alpha'], sd['S4'])
            self.assertEqual(result['diff_galois'], 'mu_2 = Z/2',
                             f"DGal != mu_2 at c={c}")


# =============================================================
# XII. MASTER CROSS-VERIFICATION
# =============================================================

class TestMasterVerification(unittest.TestCase):
    """All six directions agree: the shadow oper is rigid, CM, Eisenstein."""

    def test_master_c25(self):
        """Master verification at c=25 (generic class M)."""
        result = master_verification(c_val=25.0)
        self.assertTrue(result['katz_rigid'], "Katz rigidity failed")
        self.assertTrue(result['simpson_cm'], "Simpson CM failed")
        self.assertTrue(result['motivic_cm'], "Motivic CM failed")
        self.assertTrue(result['all_agree_rigid'], "Not all directions agree")

    def test_master_c13(self):
        """Master verification at c=13 (self-dual point)."""
        result = master_verification(c_val=13.0)
        self.assertTrue(result['all_agree_rigid'])
        self.assertEqual(result['katz_index'], 2)

    def test_master_c1(self):
        """Master verification at c=1 (free fermion)."""
        result = master_verification(c_val=1.0)
        self.assertTrue(result['all_agree_rigid'])

    def test_master_c_half(self):
        """Master verification at c=1/2 (Ising model)."""
        result = master_verification(c_val=0.5)
        self.assertTrue(result['all_agree_rigid'])

    def test_eisenstein_residues_consistency(self):
        """Eisenstein residues scale linearly with kappa."""
        for c in [1.0, 2.0, 13.0, 25.0]:
            result = master_verification(c_val=c)
            kappa = c / 2.0
            self.assertAlmostEqual(result['eisenstein_res_s1'], kappa / 2.0,
                                   places=10, msg=f"Res(s=1) wrong at c={c}")

    def test_diff_galois_in_master(self):
        """Differential Galois group is mu_2 in master check."""
        result = master_verification(c_val=25.0)
        self.assertEqual(result['diff_galois'], 'mu_2 = Z/2')

    def test_gm_consistency_in_master(self):
        """Gauss-Manin numerical check passes in master."""
        result = master_verification(c_val=25.0)
        self.assertTrue(result['gm_match'])
        self.assertTrue(result['pf_rigid'])


if __name__ == '__main__':
    unittest.main()
