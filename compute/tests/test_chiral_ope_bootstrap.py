"""Tests for chiral OPE bootstrap from bar/shadow data.

Verifies:
  - OPE data creation for standard families
  - Shadow extraction (forward direction)
  - OPE reconstruction from shadow (inverse direction)
  - Roundtrip consistency
  - Jacobi/Borcherds identity
  - Normal ordering from quartic contact
  - W_3 bootstrap
  - Koszulness classification
  - Period-OPE bridge for lattice VOAs

Ground truth:
  - thm:bar-cobar-inversion (bar_cobar_adjunction_inversion.tex)
  - thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  - prop:shadow-formality-low-arity (concordance.tex)
  - thm:nms-virasoro-quartic (nonlinear_modular_shadows.tex)
  - thm:nms-finite-termination (nonlinear_modular_shadows.tex)
  - thm:shadow-archetype-classification (chap:e1-modular-koszul)
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, oo, limit

import importlib.util
import os

# Load module
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'chiral_ope_bootstrap',
    os.path.join(_lib_dir, 'chiral_ope_bootstrap.py')
)
_boot = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_boot)

OPEData = _boot.OPEData

c = Symbol('c')
k = Symbol('k')


# ============================================================
# OPE data tests
# ============================================================

class TestOPEData:
    """Test OPE data creation for standard families."""

    def test_virasoro_ope(self):
        """T(z)T(w) ~ c/2/(z-w)^4 + 2T/(z-w)^2 + dT/(z-w)."""
        vir = OPEData.from_virasoro(c)
        assert vir.get("T", "T", "vac", 3) == c / 2
        assert vir.get("T", "T", "T", 1) == Rational(2)
        assert vir.get("T", "T", "dT", 0) == Rational(1)

    def test_virasoro_generators(self):
        """Virasoro has a single generator T."""
        vir = OPEData.from_virasoro()
        assert vir.generators == ["T"]
        assert vir.conformal_weights["T"] == 2

    def test_virasoro_max_pole(self):
        """T-T OPE has max pole at order 3 (quartic pole)."""
        vir = OPEData.from_virasoro(c)
        assert vir.max_pole("T", "T") == 3

    def test_virasoro_numeric(self):
        """Virasoro at c=1/2 (Ising model): kappa = 1/4."""
        vir = OPEData.from_virasoro(Rational(1, 2))
        assert vir.get("T", "T", "vac", 3) == Rational(1, 4)

    def test_affine_sl2_ope(self):
        """J^a J^b ~ k*kappa/(z-w)^2 + [a,b]/(z-w)."""
        aff = OPEData.from_affine("sl2", k)
        # h-h double pole
        assert aff.get("h", "h", "vac", 1) == 2 * k
        # e-f double pole
        assert aff.get("e", "f", "vac", 1) == k
        # e-f bracket
        assert aff.get("e", "f", "h", 0) == Rational(1)
        # h-e bracket
        assert aff.get("h", "e", "e", 0) == Rational(2)

    def test_affine_central_charge(self):
        """c = 3k/(k+2) for affine sl2."""
        aff = OPEData.from_affine("sl2", k)
        assert simplify(aff.central_charge - 3 * k / (k + 2)) == 0

    def test_affine_skew_symmetry(self):
        """Skew symmetry: f_{(0)}e = -e_{(0)}f = -h."""
        aff = OPEData.from_affine("sl2", k)
        assert aff.get("f", "e", "h", 0) == Rational(-1)
        assert aff.get("e", "f", "h", 0) == Rational(1)

    def test_heisenberg_ope(self):
        """J(z)J(w) ~ k/(z-w)^2."""
        heis = OPEData.from_heisenberg(k)
        assert heis.get("J", "J", "vac", 1) == k
        # No simple pole (abelian)
        assert heis.get("J", "J", "J", 0) == 0

    def test_heisenberg_abelian(self):
        """Heisenberg is abelian: no bracket."""
        heis = OPEData.from_heisenberg(k)
        assert heis.max_pole("J", "J") == 1

    def test_betagamma_ope(self):
        """beta(z)gamma(w) ~ 1/(z-w)."""
        bg = OPEData.from_betagamma()
        assert bg.get("beta", "gamma", "vac", 0) == Rational(1)
        assert bg.get("gamma", "beta", "vac", 0) == Rational(-1)

    def test_betagamma_central_charge(self):
        """beta-gamma central charge = 2."""
        bg = OPEData.from_betagamma()
        assert bg.central_charge == 2

    def test_pole_structure_virasoro(self):
        """Virasoro T-T pole structure has 3 terms."""
        vir = OPEData.from_virasoro(c)
        poles = vir.pole_structure("T", "T")
        assert 3 in poles  # quartic pole
        assert 1 in poles  # double pole
        assert 0 in poles  # simple pole

    def test_pole_structure_heisenberg(self):
        """Heisenberg J-J pole structure has 1 term."""
        heis = OPEData.from_heisenberg(k)
        poles = heis.pole_structure("J", "J")
        assert 1 in poles  # double pole
        assert len(poles) == 1


# ============================================================
# Shadow from OPE tests
# ============================================================

class TestShadowFromOPE:
    """Test forward direction: OPE -> shadow coefficients."""

    def test_virasoro_S2(self):
        """S_2 = c/4 for Virasoro (half of highest pole)."""
        vir = OPEData.from_virasoro(c)
        S = _boot.shadow_from_ope(vir)
        # S_2 = C^vac_{TT,3} / 2 = (c/2) / 2 = c/4
        assert simplify(S[2] - c / 4) == 0

    def test_virasoro_S3(self):
        """S_3 = 2 for Virasoro (conformal weight coupling)."""
        vir = OPEData.from_virasoro(c)
        S = _boot.shadow_from_ope(vir)
        assert S[3] == Rational(2)

    def test_virasoro_S4(self):
        """S_4 = 10/(c(5c+22)) for Virasoro (quartic contact)."""
        vir = OPEData.from_virasoro(c)
        S = _boot.shadow_from_ope(vir)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(S[4] - expected) == 0

    def test_virasoro_S4_numeric_c1(self):
        """S_4 at c=1: 10/(1*27) = 10/27."""
        vir = OPEData.from_virasoro(Rational(1))
        S = _boot.shadow_from_ope(vir)
        assert S[4] == Rational(10, 27)

    def test_virasoro_S4_numeric_c26(self):
        """S_4 at c=26: 10/(26*152) = 10/3952 = 5/1976."""
        vir = OPEData.from_virasoro(Rational(26))
        S = _boot.shadow_from_ope(vir)
        assert S[4] == Rational(10, 3952)

    def test_affine_S2(self):
        """S_2 = k for affine sl2 (from <h|h> = 2k)."""
        aff = OPEData.from_affine("sl2", k)
        S = _boot.shadow_from_ope(aff)
        # Only h-h has a self-pairing double pole: C^vac_{hh,1} = 2k
        # e-e, f-f have no self-pairing
        # S_2 = 2k / 2 = k
        assert simplify(S[2] - k) == 0

    def test_affine_S3(self):
        """S_3 = 1 for affine sl2 (bracket [e,f] = h)."""
        aff = OPEData.from_affine("sl2", k)
        S = _boot.shadow_from_ope(aff)
        assert S[3] == Rational(1)

    def test_affine_S4_zero(self):
        """S_4 = 0 for affine (Jacobi kills quartic)."""
        aff = OPEData.from_affine("sl2", k)
        S = _boot.shadow_from_ope(aff)
        assert S[4] == 0

    def test_heisenberg_S2(self):
        """S_2 = k/2 for Heisenberg (from <J|J> = k)."""
        heis = OPEData.from_heisenberg(k)
        S = _boot.shadow_from_ope(heis)
        assert simplify(S[2] - k / 2) == 0

    def test_heisenberg_S3_zero(self):
        """S_3 = 0 for Heisenberg (abelian, no bracket)."""
        heis = OPEData.from_heisenberg(k)
        S = _boot.shadow_from_ope(heis)
        assert S[3] == 0

    def test_heisenberg_S4_zero(self):
        """S_4 = 0 for Heisenberg (Gaussian, tower terminates at 2)."""
        heis = OPEData.from_heisenberg(k)
        S = _boot.shadow_from_ope(heis)
        assert S[4] == 0

    def test_betagamma_S2(self):
        """S_2 for beta-gamma system."""
        bg = OPEData.from_betagamma()
        S = _boot.shadow_from_ope(bg)
        # beta-beta and gamma-gamma have no self-poles.
        # S_2 = 0 (sum of C^vac_{aa,max_pole} over generators, divided by 2)
        # Actually: max_pole(beta,beta) = -1, max_pole(gamma,gamma) = -1.
        # So S_2 = 0.
        assert S[2] == 0

    def test_betagamma_S4_zero(self):
        """S_4 = 0 for beta-gamma on weight-shift line."""
        bg = OPEData.from_betagamma()
        S = _boot.shadow_from_ope(bg)
        assert S[4] == 0

    def test_shadow_higher_arities_heisenberg(self):
        """Heisenberg: S_r = 0 for all r >= 3."""
        heis = OPEData.from_heisenberg(k)
        S = _boot.shadow_from_ope(heis, max_arity=6)
        for r in range(3, 7):
            assert S[r] == 0, f"S_{r} should be 0 for Heisenberg"

    def test_shadow_higher_arities_affine(self):
        """Affine: S_r = 0 for all r >= 4."""
        aff = OPEData.from_affine("sl2", k)
        S = _boot.shadow_from_ope(aff, max_arity=6)
        for r in range(4, 7):
            assert S[r] == 0, f"S_{r} should be 0 for affine"


# ============================================================
# OPE from shadow (inverse direction) tests
# ============================================================

class TestOPEFromShadow:
    """Test inverse direction: shadow -> OPE reconstruction."""

    def test_virasoro_roundtrip(self):
        """OPE -> shadow -> OPE recovers Virasoro coefficients."""
        vir = OPEData.from_virasoro(c)
        rt = _boot.verify_roundtrip(vir)
        assert rt['all_match'], f"Virasoro roundtrip failed: {rt['matches']}"

    def test_affine_roundtrip(self):
        """OPE -> shadow -> OPE recovers affine sl2 coefficients."""
        aff = OPEData.from_affine("sl2", k)
        rt = _boot.verify_roundtrip(aff)
        assert rt['all_match'], f"Affine roundtrip failed: {rt['matches']}"

    def test_heisenberg_roundtrip(self):
        """OPE -> shadow -> OPE recovers Heisenberg coefficients."""
        heis = OPEData.from_heisenberg(k)
        rt = _boot.verify_roundtrip(heis)
        assert rt['all_match'], f"Heisenberg roundtrip failed: {rt['matches']}"

    def test_virasoro_ope_from_shadow_quartic_pole(self):
        """Virasoro reconstruction recovers C^vac_{TT,3} = c/2."""
        vir_recon = _boot.virasoro_ope_from_shadow(c)
        assert simplify(vir_recon.get("T", "T", "vac", 3) - c / 2) == 0

    def test_virasoro_ope_from_shadow_double_pole(self):
        """Virasoro reconstruction recovers C^T_{TT,1} = 2."""
        vir_recon = _boot.virasoro_ope_from_shadow(c)
        assert vir_recon.get("T", "T", "T", 1) == Rational(2)

    def test_virasoro_ope_from_shadow_simple_pole(self):
        """Virasoro reconstruction recovers C^{dT}_{TT,0} = 1."""
        vir_recon = _boot.virasoro_ope_from_shadow(c)
        assert vir_recon.get("T", "T", "dT", 0) == Rational(1)

    def test_affine_ope_from_shadow_double_pole(self):
        """Affine reconstruction recovers h-h double pole = 2k."""
        aff_recon = _boot.affine_ope_from_shadow(k)
        assert simplify(aff_recon.get("h", "h", "vac", 1) - 2 * k) == 0

    def test_affine_ope_from_shadow_bracket(self):
        """Affine reconstruction recovers [e,f] = h."""
        aff_recon = _boot.affine_ope_from_shadow(k)
        assert aff_recon.get("e", "f", "h", 0) == Rational(1)
        assert aff_recon.get("f", "e", "h", 0) == Rational(-1)


# ============================================================
# Jacobi identity tests
# ============================================================

class TestBootstrapConsistency:
    """Test consistency checks and Jacobi identity."""

    def test_affine_jacobi_efh(self):
        """Jacobi identity [e,[f,h]] = [[e,f],h] + [f,[e,h]] for sl2."""
        aff = OPEData.from_affine("sl2", k)
        residual = _boot.jacobi_from_ope(aff, "e", "f", "h")
        assert residual == 0

    def test_affine_jacobi_hef(self):
        """Jacobi identity [h,[e,f]] = [[h,e],f] + [e,[h,f]] for sl2."""
        aff = OPEData.from_affine("sl2", k)
        residual = _boot.jacobi_from_ope(aff, "h", "e", "f")
        assert residual == 0

    def test_affine_jacobi_fhe(self):
        """Jacobi identity with (f,h,e) ordering."""
        aff = OPEData.from_affine("sl2", k)
        residual = _boot.jacobi_from_ope(aff, "f", "h", "e")
        assert residual == 0

    def test_heisenberg_jacobi_trivial(self):
        """Heisenberg: Jacobi identity trivially satisfied (abelian)."""
        heis = OPEData.from_heisenberg(k)
        residual = _boot.jacobi_from_ope(heis, "J", "J", "J")
        assert residual == 0

    def test_mc_arity2_always_consistent(self):
        """MC at arity 2 is always consistent (scalar kappa)."""
        S = {2: c / 4, 3: Rational(2), 4: Rational(10) / (c * (5 * c + 22))}
        check = _boot.bootstrap_consistency_check(S)
        assert check[2]['consistent'] is True

    def test_mc_arity3_consistent(self):
        """MC at arity 3: cubic cocycle condition satisfied."""
        S = {2: c / 4, 3: Rational(2), 4: Rational(10) / (c * (5 * c + 22))}
        check = _boot.bootstrap_consistency_check(S)
        assert check[3]['consistent'] is True

    def test_mc_arity4_lie_consistent(self):
        """MC at arity 4: Lie type (Q=0) is consistent."""
        S = {2: k, 3: Rational(1), 4: Rational(0)}
        check = _boot.bootstrap_consistency_check(S)
        assert check[4]['consistent'] is True

    def test_mc_arity4_virasoro_consistent(self):
        """MC at arity 4: Virasoro nontrivial quartic is consistent."""
        S = {2: c / 4, 3: Rational(2), 4: Rational(10) / (c * (5 * c + 22))}
        check = _boot.bootstrap_consistency_check(S)
        assert check[4]['consistent'] is True


# ============================================================
# Normal ordering tests
# ============================================================

class TestNormalOrdering:
    """Test normal ordering extraction from quartic contact."""

    def test_quartic_contact_virasoro(self):
        """Virasoro: Lambda = :TT: - (3/10) d^2T."""
        Q = Rational(10) / (c * (5 * c + 22))
        S_2 = c / 4
        S_3 = Rational(2)
        result = _boot.normal_ordering_from_quartic(Q, S_2, S_3)
        assert result['normal_ordering_coeff'] == Rational(3, 10)
        assert result['type'] == 'non-Lie (genuine normal ordering)'

    def test_quartic_determines_composite(self):
        """Nontrivial quartic determines composite operator coupling."""
        Q = Rational(10) / (c * (5 * c + 22))
        result = _boot.normal_ordering_from_quartic(Q, c / 4, Rational(2))
        # coupling_squared = Q * lambda_norm = 10/(c(5c+22)) * c(5c+22)/10 = 1
        coupling_sq = result['coupling_squared']
        assert simplify(coupling_sq - 1) == 0

    def test_lie_no_normal_ordering(self):
        """Lie type (Q=0): no normal ordering ambiguity."""
        result = _boot.normal_ordering_from_quartic(Rational(0), k, Rational(1))
        assert result['type'] == 'Lie (no normal ordering)'
        assert result['composite_norm'] == 0

    def test_lambda_norm_formula(self):
        """Lambda norm = c(5c+22)/10."""
        Q = Rational(10) / (c * (5 * c + 22))
        result = _boot.normal_ordering_from_quartic(Q, c / 4, Rational(2))
        expected_norm = c * (5 * c + 22) / 10
        assert simplify(result['composite_norm'] - expected_norm) == 0


# ============================================================
# W_3 bootstrap tests
# ============================================================

class TestW3Bootstrap:
    """Test W_3 algebra bootstrap."""

    def test_w3_generators(self):
        """W_3 has generators T (weight 2) and W (weight 3)."""
        w3 = _boot.w3_bootstrap(c)
        assert w3['generators'] == ['T', 'W']
        assert w3['conformal_weights'] == {'T': 2, 'W': 3}

    def test_w3_b_squared(self):
        """b^2 = 16/(22+5c) for W_3."""
        w3 = _boot.w3_bootstrap(c)
        expected = Rational(16) / (22 + 5 * c)
        assert simplify(w3['b_squared'] - expected) == 0

    def test_w3_nonlinear_term(self):
        """The non-linear coupling 2b^2 in the W-W OPE."""
        w3 = _boot.w3_bootstrap(c)
        expected = Rational(32) / (22 + 5 * c)
        assert simplify(w3['non_linear_term'] - expected) == 0

    def test_w3_tt_ope(self):
        """T-T OPE in W_3 matches Virasoro."""
        w3 = _boot.w3_bootstrap(c)
        assert w3['ope_coeffs'][("T", "T", "vac", 3)] == c / 2
        assert w3['ope_coeffs'][("T", "T", "T", 1)] == Rational(2)

    def test_w3_ww_highest_pole(self):
        """W-W OPE highest pole: c/3 / (z-w)^6."""
        w3 = _boot.w3_bootstrap(c)
        assert w3['ope_coeffs'][("W", "W", "vac", 5)] == c / 3

    def test_w3_shadow_S2(self):
        """W_3 shadow: S_2 = 5c/12."""
        w3 = _boot.w3_bootstrap(c)
        assert simplify(w3['S_2'] - 5 * c / 12) == 0

    def test_w3_lambda_norm(self):
        """Lambda norm c(5c+22)/10 in W_3 context."""
        w3 = _boot.w3_bootstrap(c)
        expected = c * (5 * c + 22) / 10
        assert simplify(w3['lambda_norm'] - expected) == 0

    def test_w3_composite_operator(self):
        """W_3 composite operator is Lambda = :TT: - (3/10) d^2T."""
        w3 = _boot.w3_bootstrap(c)
        assert 'Lambda' in w3['composite_operator']


# ============================================================
# Bootstrap uniqueness tests
# ============================================================

class TestBootstrapUniqueness:
    """Test bootstrap uniqueness analysis."""

    def test_koszul_unique_full_tower(self):
        """Koszul algebras: full tower determines OPE uniquely."""
        S = {2: c / 4, 3: Rational(2), 4: Rational(10) / (c * (5 * c + 22))}
        result = _boot.bootstrap_uniqueness_test(S)
        assert result['full_tower']['unique'] is True

    def test_underdetermined_at_arity2(self):
        """At arity 2 alone: not unique (many algebras share same kappa)."""
        S = {2: c / 4, 3: Rational(2), 4: Rational(10) / (c * (5 * c + 22))}
        result = _boot.bootstrap_uniqueness_test(S)
        assert result['arity_2']['unique'] is False

    def test_underdetermined_at_arity3(self):
        """At arity 3: not unique (cubic determines bracket, not full VOA)."""
        S = {2: c / 4, 3: Rational(2), 4: Rational(10) / (c * (5 * c + 22))}
        result = _boot.bootstrap_uniqueness_test(S)
        assert result['arity_3']['unique'] is False

    def test_abelian_not_unique_at_arity4(self):
        """Abelian with Q=0: not unique at arity 4."""
        S = {2: k / 2, 3: Rational(0), 4: Rational(0)}
        result = _boot.bootstrap_uniqueness_test(S)
        assert result['arity_4']['unique'] is False

    def test_lie_not_unique_at_arity4(self):
        """Lie type (Q=0, C != 0): not unique at arity 4."""
        S = {2: k, 3: Rational(1), 4: Rational(0)}
        result = _boot.bootstrap_uniqueness_test(S)
        assert result['arity_4']['unique'] is False


# ============================================================
# Koszulness classification tests
# ============================================================

class TestKoszulnessClassification:
    """Test shadow-depth Koszulness classification."""

    def test_heisenberg_gaussian(self):
        """Heisenberg: Gaussian type, depth 2."""
        S = {2: k / 2, 3: Rational(0), 4: Rational(0), 5: Rational(0)}
        result = _boot.shadow_determines_koszulness(S)
        assert result['archetype'] == 'G'
        assert result['shadow_depth'] == 2
        assert result['koszul'] is True

    def test_affine_lie_tree(self):
        """Affine sl2: Lie/tree type, depth 3."""
        S = {2: k, 3: Rational(1), 4: Rational(0), 5: Rational(0), 6: Rational(0)}
        result = _boot.shadow_determines_koszulness(S)
        assert result['archetype'] == 'L'
        assert result['shadow_depth'] == 3
        assert result['koszul'] is True

    def test_betagamma_contact(self):
        """beta-gamma: contact type, depth 4."""
        # beta-gamma has nontrivial quartic on the full weight/contact slice
        # but S_4 != 0 in the mixed directions.  We model the contact type.
        S = {2: Rational(1), 3: Rational(0), 4: Rational(1, 10),
             5: Rational(0), 6: Rational(0)}
        result = _boot.shadow_determines_koszulness(S)
        assert result['archetype'] == 'C'
        assert result['shadow_depth'] == 4
        assert result['koszul'] is True

    def test_virasoro_mixed(self):
        """Virasoro: mixed type, infinite depth."""
        S = {2: c / 4, 3: Rational(2), 4: Rational(10) / (c * (5 * c + 22)),
             5: Rational(120) / (c**2 * (5 * c + 22))}
        result = _boot.shadow_determines_koszulness(S)
        assert result['archetype'] == 'M'
        assert result['shadow_depth'] is None  # infinite
        assert result['koszul'] is True

    def test_all_standard_landscape_koszul(self):
        """ALL standard landscape algebras are Koszul."""
        # This is a fundamental result: shadow depth classifies COMPLEXITY
        # of Koszul algebras, not Koszulness itself.
        for S in [
            {2: k / 2, 3: Rational(0), 4: Rational(0)},  # Heisenberg
            {2: k, 3: Rational(1), 4: Rational(0)},       # affine
            {2: c / 4, 3: Rational(2), 4: Rational(10) / (c * (5 * c + 22))},  # Vir
        ]:
            result = _boot.shadow_determines_koszulness(S)
            assert result['koszul'] is True


# ============================================================
# Period-OPE bridge tests
# ============================================================

class TestPeriodOPEBridge:
    """Test period-OPE bridge for lattice VOAs."""

    def test_lattice_rank1_shadow(self):
        """Rank-1 lattice (Z-lattice): S_2 = kappa = rank = 1."""
        S = {2: Rational(1), 3: Rational(0), 4: Rational(0)}
        result = _boot.period_ope_bridge(1, S)
        assert result['rank'] == 1
        assert result['kappa'] == Rational(1)
        assert result['shadow_depth'] == 2

    def test_lattice_gaussian_archetype(self):
        """Lattice VOAs are Gaussian type (depth 2)."""
        S = {2: Rational(8), 3: Rational(0), 4: Rational(0)}
        result = _boot.period_ope_bridge(8, S)
        assert result['archetype'] == 'G'

    def test_lattice_self_dual_e8(self):
        """E_8 lattice (rank 8, self-dual): S_2 = kappa = rank = 8."""
        S = {2: Rational(8), 3: Rational(0), 4: Rational(0)}
        result = _boot.period_ope_bridge(8, S)
        assert result['self_dual'] is True  # 8 == rank

    def test_lattice_not_self_dual(self):
        """Non-self-dual lattice: kappa != rank."""
        S = {2: Rational(1), 3: Rational(0), 4: Rational(0)}
        result = _boot.period_ope_bridge(3, S)
        assert result['self_dual'] is False  # 1 != 3

    def test_lattice_partition_function_type(self):
        """Lattice partition function = theta_Lambda / eta^rank."""
        S = {2: Rational(1)}
        result = _boot.period_ope_bridge(1, S)
        assert 'theta_Lambda' in result['partition_function_type']

    def test_leech_lattice(self):
        """Leech lattice (rank 24, self-dual): S_2 = kappa = rank = 24."""
        S = {2: Rational(24), 3: Rational(0), 4: Rational(0)}
        result = _boot.period_ope_bridge(24, S)
        assert result['rank'] == 24
        assert result['kappa'] == 24
        assert result['self_dual'] is True  # 24 == rank


# ============================================================
# Virasoro quintic shadow test
# ============================================================

class TestVirasoroHigherShadows:
    """Test higher shadows for Virasoro."""

    def test_virasoro_quintic_formula(self):
        """o^(5)_Vir = 120 / (c^2(5c+22))."""
        vir = OPEData.from_virasoro(c)
        S = _boot.shadow_from_ope(vir, max_arity=5)
        expected = Rational(120) / (c**2 * (5 * c + 22))
        assert simplify(S[5] - expected) == 0

    def test_virasoro_quintic_numeric_c1(self):
        """Virasoro quintic at c=1: 120/(1*27) = 40/9."""
        vir = OPEData.from_virasoro(Rational(1))
        S = _boot.shadow_from_ope(vir, max_arity=5)
        assert S[5] == Rational(120, 27)

    def test_virasoro_quintic_forced_nonzero(self):
        """Virasoro quintic is FORCED nonzero (infinite tower)."""
        vir = OPEData.from_virasoro(c)
        S = _boot.shadow_from_ope(vir, max_arity=5)
        assert S[5] != 0

    def test_affine_quintic_zero(self):
        """Affine quintic is zero (tower terminates at 3)."""
        aff = OPEData.from_affine("sl2", k)
        S = _boot.shadow_from_ope(aff, max_arity=5)
        assert S[5] == 0


# ============================================================
# Pole structure utility tests
# ============================================================

class TestOPEPoleStructure:
    """Test pole structure utility function."""

    def test_virasoro_pole_list(self):
        """Virasoro T-T pole list: [(3, {vac:c/2}), (1, {T:2}), (0, {dT:1})]."""
        vir = OPEData.from_virasoro(c)
        poles = _boot.ope_pole_structure(vir, "T", "T")
        # Should be sorted by descending pole order
        assert poles[0][0] == 3  # highest pole first
        assert poles[-1][0] == 0  # lowest pole last

    def test_affine_ef_pole_list(self):
        """Affine e-f pole list: [(1, {vac:k}), (0, {h:1})]."""
        aff = OPEData.from_affine("sl2", k)
        poles = _boot.ope_pole_structure(aff, "e", "f")
        assert len(poles) == 2
        assert poles[0][0] == 1  # double pole
        assert poles[1][0] == 0  # simple pole

    def test_heisenberg_pole_list(self):
        """Heisenberg J-J pole list: [(1, {vac:k})]."""
        heis = OPEData.from_heisenberg(k)
        poles = _boot.ope_pole_structure(heis, "J", "J")
        assert len(poles) == 1
        assert poles[0][0] == 1
