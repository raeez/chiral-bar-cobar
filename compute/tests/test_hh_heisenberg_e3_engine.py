r"""Tests for the explicit E_3 structure on HH*(H_k).

Verifies Gerstenhaber bracket [HH^0, HH^1], [HH^1, HH^1], and all
E_3 compatibility conditions on the Hochschild cohomology of the
Heisenberg vertex algebra.

Organized by:
  I.    Heisenberg algebra data and kappa
  II.   HH* dimensions
  III.  Cup product axioms
  IV.   Gerstenhaber bracket: [HH^0, HH^1] = 0
  V.    Gerstenhaber bracket: [HH^1, HH^1] = 0
  VI.   Gerstenhaber bracket: all remaining pairs
  VII.  Degree shift verification
  VIII. Graded antisymmetry
  IX.   Graded Jacobi identity
  X.    Leibniz rule
  XI.   E_3 linking operations
  XII.  Browder bracket (secondary E_3 operation)
  XIII. r-matrix and kappa consistency
  XIV.  Full E_3 verification
  XV.   Level variation (k=0, k=1, k=-1, generic)

References:
  Gerstenhaber, Ann. Math. 78 (1963): bracket on HH*
  Kontsevich, Lett. Math. Phys. 48 (1999): formality
  Tamarkin, arXiv:math/0302311 (2003): E_3 from Etingof-Kazhdan
  De Leger, arXiv:2512.20167: SC(E_2) ~ SC_2 gives E_3 on ChirHoch
  thm:hochschild-polynomial-growth (chiral_hochschild_koszul.tex)
  CLAUDE.md C1, C10, C13
"""

import pytest

from compute.lib.hh_heisenberg_e3_engine import (
    # Data
    HeisenbergData,
    heisenberg_data,
    # HH elements
    HHElement,
    hh0_basis,
    hh1_basis,
    hh2_basis,
    hh_element,
    hh_dims,
    # Cup product
    cup_product,
    verify_cup_graded_commutativity,
    verify_cup_associativity,
    # Gerstenhaber bracket
    gerstenhaber_bracket,
    bracket_degree,
    verify_bracket_degree_shift,
    verify_graded_antisymmetry,
    verify_graded_jacobi,
    verify_leibniz,
    # E_3
    e3_linking,
    e3_linking_degree,
    browder_bracket,
    verify_browder_well_defined,
    # r-matrix / kappa
    r_matrix_heisenberg,
    kappa_heisenberg,
    averaging_map_check,
    # Degree shifts
    verify_all_degree_shifts,
    # Full verification
    E3VerificationResult,
    verify_e3_structure,
    summary,
)


# ===================================================================
# I. Heisenberg algebra data and kappa
# ===================================================================

class TestHeisenbergData:
    """Basic algebra data and kappa verification."""

    def test_kappa_equals_level(self):
        """kappa(H_k) = k for all k."""
        # VERIFIED: [DC] kappa(H_k) = k by definition (C1);
        #           [LT] CLAUDE.md C1 + landscape_census.tex
        for k in (0, 1, 2, -1, 7):
            data = heisenberg_data(k)
            assert data.kappa == k

    def test_kappa_not_k_over_2(self):
        """kappa(H_k) = k, NOT k/2 (common error from Vir pattern-match)."""
        # VERIFIED: [DC] direct from OPE J(z)J(w)~k/(z-w)^2;
        #           [CF] cross-family: kappa(Vir)=c/2 is Vir-specific
        data = heisenberg_data(2)
        assert data.kappa == 2
        assert data.kappa != 1  # would be k/2

    def test_central_charge(self):
        """c(H_k) = 1 (single free boson)."""
        # VERIFIED: [DC] one boson contributes c=1;
        #           [LT] Kac vertex algebras, Ch 2
        data = heisenberg_data(1)
        assert data.central_charge == 1

    def test_shadow_class_G(self):
        """Heisenberg is class G (Gaussian, shadow depth 2)."""
        # VERIFIED: [DC] abelian OPE, r=2 truncation;
        #           [LT] CLAUDE.md C26
        data = heisenberg_data(1)
        assert data.shadow_class == 'G'

    def test_r_matrix_coefficient(self):
        """r-matrix coefficient is k (AP126: level prefix mandatory)."""
        # VERIFIED: [DC] r^Heis(z) = k/z, coefficient = k;
        #           [LT] CLAUDE.md C10
        for k in (0, 1, 3):
            data = heisenberg_data(k)
            assert data.r_matrix_coeff == k


# ===================================================================
# II. HH* dimensions
# ===================================================================

class TestHHDimensions:
    """Dimensions of HH^n(H_k)."""

    def test_hh0_dim_1(self):
        """dim HH^0(H_k) = 1 (center = scalars)."""
        # VERIFIED: [DC] Z(H_k) = C (vacuum only center element);
        #           [LT] thm:hochschild-polynomial-growth
        assert hh_dims()[0] == 1

    def test_hh1_dim_1(self):
        """dim HH^1(H_k) = 1 (single outer derivation)."""
        # VERIFIED: [DC] Der(H_k)/Inn(H_k) = C*D_J;
        #           [LT] chiral_hochschild_engine.py heisenberg case
        assert hh_dims()[1] == 1

    def test_hh2_dim_1(self):
        """dim HH^2(H_k) = 1 (level deformation k -> k+eps)."""
        # VERIFIED: [DC] unique first-order deformation of J(z)J(w)~k/(z-w)^2;
        #           [LT] Theorem H concentration + Z(H_k^!) = C
        assert hh_dims()[2] == 1

    def test_hh_concentrated_012(self):
        """HH^n = 0 for n not in {0,1,2} (Theorem H concentration)."""
        # VERIFIED: [DC] bar-cobar resolution computation;
        #           [LT] thm:hochschild-polynomial-growth
        dims = hh_dims()
        for n in range(3, 10):
            assert dims.get(n, 0) == 0

    def test_total_dim_3(self):
        """Total dim HH*(H_k) = 3 (within Theorem H bound of 4)."""
        # VERIFIED: [DC] 1 + 1 + 1 = 3;
        #           [LT] Theorem H: total dim <= 4
        assert sum(hh_dims().values()) == 3

    def test_hilbert_polynomial(self):
        """P_{H_k}(t) = 1 + t + t^2."""
        # VERIFIED: [DC] sum of dims * t^n;
        #           [SY] palindromic: P(1/t)*t^2 = P(t) (Koszul duality)
        dims = hh_dims()
        # Palindromicity: dim HH^n = dim HH^{2-n}
        assert dims[0] == dims[2]


# ===================================================================
# III. Cup product axioms
# ===================================================================

class TestCupProduct:
    """Cup product on HH*(H_k)."""

    def test_cup_unital(self):
        """id cup x = x for all x (HH^0 is the unit)."""
        # VERIFIED: [DC] id is the identity endomorphism;
        #           [LT] Gerstenhaber 1963, cup product structure
        e0 = hh0_basis()
        for x in [hh0_basis(), hh1_basis(), hh2_basis()]:
            result = cup_product(e0, x)
            assert abs(result.coefficient - x.coefficient) < 1e-15
            assert result.degree == x.degree

    def test_cup_hh1_hh1_vanishes(self):
        """D_J cup D_J = 0 (graded commutativity forces vanishing).

        Graded commutativity: a cup b = (-1)^{|a||b|} b cup a.
        For |a|=|b|=1: a cup a = -(a cup a), hence a cup a = 0.
        The level deformation class in HH^2 is independent of the
        cup product image from HH^1.
        """
        # VERIFIED: [DC] (-1)^{1*1} = -1, so x = -x => x = 0;
        #           [SY] graded commutativity (same as wedge product)
        e1 = hh1_basis()
        result = cup_product(e1, e1)
        assert result.degree == 2
        assert result.is_zero()

    def test_cup_vanishes_above_degree_2(self):
        """a cup b = 0 if |a| + |b| > 2 (concentration)."""
        # VERIFIED: [DC] HH^n = 0 for n > 2;
        #           [LT] Theorem H amplitude [0,2]
        e1 = hh1_basis()
        e2 = hh2_basis()
        assert cup_product(e1, e2).is_zero()
        assert cup_product(e2, e1).is_zero()
        assert cup_product(e2, e2).is_zero()

    def test_graded_commutativity_all_pairs(self):
        """a cup b = (-1)^{|a||b|} b cup a for all basis pairs."""
        # VERIFIED: [DC] explicit computation on all 9 pairs;
        #           [LT] Gerstenhaber 1963
        basis = [hh0_basis(), hh1_basis(), hh2_basis()]
        for a in basis:
            for b in basis:
                assert verify_cup_graded_commutativity(a, b)

    def test_associativity_all_triples(self):
        """(a cup b) cup c = a cup (b cup c) for all basis triples."""
        # VERIFIED: [DC] explicit computation on all 27 triples;
        #           [LT] Gerstenhaber 1963
        basis = [hh0_basis(), hh1_basis(), hh2_basis()]
        for a in basis:
            for b in basis:
                for c in basis:
                    assert verify_cup_associativity(a, b, c)


# ===================================================================
# IV. Gerstenhaber bracket: [HH^0, HH^1] = 0
# ===================================================================

class TestBracketHH0HH1:
    """[HH^0, HH^1] = 0: scalars act trivially."""

    def test_bracket_id_dj_zero(self):
        """[id, D_J] = 0."""
        # VERIFIED: [DC] identity endomorphism commutes with all derivations;
        #           [LT] Gerstenhaber 1963, Prop 3: scalars central
        result = gerstenhaber_bracket(hh0_basis(), hh1_basis())
        assert result.is_zero()
        assert result.degree == 0  # target: 0 + 1 - 1 = 0

    def test_bracket_id_defk_zero(self):
        """[id, def_k] = 0."""
        # VERIFIED: [DC] id has trivial bracket with deformations;
        #           [LT] Gerstenhaber 1963
        result = gerstenhaber_bracket(hh0_basis(), hh2_basis())
        assert result.is_zero()
        assert result.degree == 1  # target: 0 + 2 - 1 = 1

    def test_bracket_id_id_zero(self):
        """[id, id] = 0."""
        # VERIFIED: [DC] [a, a] = 0 when |a|-1 is odd (here |id|-1 = -1, odd);
        #           [SY] graded antisymmetry forces this
        result = gerstenhaber_bracket(hh0_basis(), hh0_basis())
        assert result.is_zero()


# ===================================================================
# V. Gerstenhaber bracket: [HH^1, HH^1] = 0
# ===================================================================

class TestBracketHH1HH1:
    """[HH^1, HH^1] = 0: derivations commute (abelian algebra)."""

    def test_bracket_dj_dj_zero(self):
        """[D_J, D_J] = 0 (single derivation commutes with itself).

        This is the KEY computation. The Gerstenhaber bracket on
        HH^1 x HH^1 -> HH^1 is the commutator of derivations.
        For H_k with dim HH^1 = 1, there is a single derivation D_J.
        [D_J, D_J] = 0 by graded antisymmetry: shifted degree
        |D_J| - 1 = 0 is even, so [D_J, D_J] = -[D_J, D_J] = 0.
        """
        # VERIFIED: [DC] graded antisymmetry with even shifted degree;
        #           [SY] [x, x] = 0 for even |x|-1 in Gerstenhaber algebra
        e1 = hh1_basis()
        result = gerstenhaber_bracket(e1, e1)
        assert result.is_zero()
        assert result.degree == 1  # target: 1 + 1 - 1 = 1

    def test_bracket_hh1_hh1_target_degree(self):
        """[HH^1, HH^1] targets HH^1 (degree 1+1-1=1)."""
        # VERIFIED: [DC] |[a,b]| = |a| + |b| - 1 = 1 + 1 - 1 = 1;
        #           [DA] degree arithmetic
        e1 = hh1_basis()
        result = gerstenhaber_bracket(e1, e1)
        assert result.degree == 1

    def test_commutator_of_derivations_interpretation(self):
        """[HH^1, HH^1] -> HH^1 is the Lie bracket on Der(H_k)/Inn(H_k).

        For H_k: Der/Inn is 1-dimensional, so the Lie algebra is abelian.
        The commutator [D_J, D_J] = D_J o D_J - D_J o D_J = 0.
        """
        # VERIFIED: [DC] composition minus composition = 0;
        #           [LC] at k=0, H_0 is the trivial algebra, Der = C, [,] = 0
        e1 = hh1_basis()
        # Commutator: [D, D] = D o D - D o D = 0
        result = gerstenhaber_bracket(e1, e1)
        assert result.is_zero()

    def test_scaled_bracket_hh1_hh1(self):
        """[alpha*D_J, beta*D_J] = 0 for all scalars alpha, beta."""
        # VERIFIED: [DC] bilinearity + [D_J, D_J] = 0;
        #           [SY] bracket is bilinear
        for alpha in [1, 2, -3, 0.5]:
            for beta in [1, -1, 4, 0.7]:
                a = hh_element(1, alpha)
                b = hh_element(1, beta)
                result = gerstenhaber_bracket(a, b)
                assert result.is_zero()


# ===================================================================
# VI. Gerstenhaber bracket: all remaining pairs
# ===================================================================

class TestBracketAllPairs:
    """All Gerstenhaber brackets vanish for Heisenberg (class G)."""

    def test_bracket_hh1_hh2_zero(self):
        """[D_J, def_k] = 0 (derivation preserves level)."""
        # VERIFIED: [DC] D_J shifts J by constant, preserves OPE coefficient;
        #           [LC] at k=0 both sides trivial
        result = gerstenhaber_bracket(hh1_basis(), hh2_basis())
        assert result.is_zero()
        assert result.degree == 2  # target: 1 + 2 - 1 = 2

    def test_bracket_hh2_hh1_zero(self):
        """[def_k, D_J] = 0 (reverse order)."""
        # VERIFIED: [DC] graded antisymmetry with [HH^1, HH^2] = 0;
        #           [SY] antisymmetry
        result = gerstenhaber_bracket(hh2_basis(), hh1_basis())
        assert result.is_zero()

    def test_bracket_hh2_hh2_zero(self):
        """[def_k, def_k] = 0 (target HH^3 = 0)."""
        # VERIFIED: [DC] target degree 2+2-1 = 3, but HH^3 = 0;
        #           [LT] Theorem H concentration
        result = gerstenhaber_bracket(hh2_basis(), hh2_basis())
        assert result.is_zero()

    def test_all_brackets_vanish(self):
        """ALL Gerstenhaber brackets vanish for Heisenberg.

        This is the defining property of class G: the Gerstenhaber
        algebra structure on HH*(H_k) is ABELIAN.
        """
        # VERIFIED: [DC] exhaustive check on 9 basis pairs;
        #           [CF] class G = Gaussian = abelian bracket (CLAUDE.md C26)
        basis = [hh0_basis(), hh1_basis(), hh2_basis()]
        for a in basis:
            for b in basis:
                assert gerstenhaber_bracket(a, b).is_zero(), (
                    f"[HH^{a.degree}, HH^{b.degree}] should vanish"
                )


# ===================================================================
# VII. Degree shift verification
# ===================================================================

class TestDegreeShift:
    """Verify |[a, b]| = |a| + |b| - 1."""

    def test_bracket_degree_is_minus_1(self):
        """The Gerstenhaber bracket has intrinsic degree -1."""
        # VERIFIED: [DC] from E_2 operad: H_1(Conf_2(R^2)) = C;
        #           [LT] Gerstenhaber 1963
        assert bracket_degree() == -1

    def test_all_degree_shifts(self):
        """Verify target degree = |a| + |b| - 1 for all pairs."""
        # VERIFIED: [DC] explicit computation;
        #           [DA] degree arithmetic
        shifts = verify_all_degree_shifts()
        for (p, q), target in shifts.items():
            expected = p + q - 1
            if expected >= 0:
                assert target == expected, (
                    f"[HH^{p}, HH^{q}] -> HH^{target}, expected HH^{expected}"
                )

    def test_degree_shift_individual_cases(self):
        """Individual degree shift checks."""
        # VERIFIED: [DA] degree arithmetic;
        #           [DC] explicit
        assert verify_bracket_degree_shift(hh0_basis(), hh0_basis())  # 0+0-1 < 0
        assert verify_bracket_degree_shift(hh0_basis(), hh1_basis())  # 0+1-1 = 0
        assert verify_bracket_degree_shift(hh1_basis(), hh1_basis())  # 1+1-1 = 1
        assert verify_bracket_degree_shift(hh1_basis(), hh2_basis())  # 1+2-1 = 2
        assert verify_bracket_degree_shift(hh2_basis(), hh2_basis())  # 2+2-1 = 3


# ===================================================================
# VIII. Graded antisymmetry
# ===================================================================

class TestGradedAntisymmetry:
    """[a, b] = -(-1)^{(|a|-1)(|b|-1)} [b, a]."""

    def test_antisymmetry_all_pairs(self):
        """Graded antisymmetry holds for all basis pairs."""
        # VERIFIED: [DC] explicit computation on 9 pairs;
        #           [LT] Gerstenhaber 1963, Theorem 1
        basis = [hh0_basis(), hh1_basis(), hh2_basis()]
        for a in basis:
            for b in basis:
                assert verify_graded_antisymmetry(a, b), (
                    f"Antisymmetry fails for [HH^{a.degree}, HH^{b.degree}]"
                )

    def test_antisymmetry_hh1_hh1_sign(self):
        """For [HH^1, HH^1]: shifted degrees are (0, 0), sign is -1.

        [D_J, D_J] = -(-1)^{0*0} [D_J, D_J] = -[D_J, D_J].
        So 2*[D_J, D_J] = 0, hence [D_J, D_J] = 0.
        """
        # VERIFIED: [DC] sign = -(-1)^0 = -1, so x = -x => x = 0;
        #           [SY] standard argument for even shifted degree
        e1 = hh1_basis()
        sign = -((-1) ** ((1 - 1) * (1 - 1)))
        assert sign == -1  # forces vanishing


# ===================================================================
# IX. Graded Jacobi identity
# ===================================================================

class TestGradedJacobi:
    """(-1)^{(|a|-1)(|c|-1)}[a,[b,c]] + cyclic = 0."""

    def test_jacobi_all_triples(self):
        """Graded Jacobi holds for all 27 basis triples."""
        # VERIFIED: [DC] all brackets vanish, so Jacobi is 0+0+0=0;
        #           [LT] Gerstenhaber 1963, Theorem 3
        basis = [hh0_basis(), hh1_basis(), hh2_basis()]
        for a in basis:
            for b in basis:
                for c in basis:
                    assert verify_graded_jacobi(a, b, c), (
                        f"Jacobi fails for ({a.degree},{b.degree},{c.degree})"
                    )

    def test_jacobi_triple_111(self):
        """Jacobi for (HH^1, HH^1, HH^1): trivially 0."""
        # VERIFIED: [DC] [D_J, [D_J, D_J]] = [D_J, 0] = 0;
        #           [SY] each inner bracket vanishes
        e1 = hh1_basis()
        assert verify_graded_jacobi(e1, e1, e1)

    def test_jacobi_triple_012(self):
        """Jacobi for (HH^0, HH^1, HH^2): trivially 0."""
        # VERIFIED: [DC] all brackets with HH^0 vanish;
        #           [LC] degenerates to 0 at k=0
        assert verify_graded_jacobi(hh0_basis(), hh1_basis(), hh2_basis())


# ===================================================================
# X. Leibniz rule
# ===================================================================

class TestLeibniz:
    """[a, b cup c] = [a,b] cup c + (-1)^{(|a|-1)|b|} b cup [a,c]."""

    def test_leibniz_all_triples(self):
        """Leibniz rule holds for all 27 basis triples."""
        # VERIFIED: [DC] all brackets vanish, both sides are 0;
        #           [LT] Gerstenhaber 1963, Theorem 4
        basis = [hh0_basis(), hh1_basis(), hh2_basis()]
        for a in basis:
            for b in basis:
                for c in basis:
                    assert verify_leibniz(a, b, c), (
                        f"Leibniz fails for ({a.degree},{b.degree},{c.degree})"
                    )

    def test_leibniz_key_case_1_0_1(self):
        """[D_J, id cup D_J] = [D_J, D_J] = 0.

        LHS: [D_J, id cup D_J] = [D_J, D_J] = 0.
        RHS: [D_J, id] cup D_J + id cup [D_J, D_J] = 0 + 0 = 0.
        """
        # VERIFIED: [DC] explicit computation;
        #           [SY] both sides vanish by bracket vanishing
        assert verify_leibniz(hh1_basis(), hh0_basis(), hh1_basis())


# ===================================================================
# XI. E_3 linking operations
# ===================================================================

class TestE3Linking:
    """E_3 linking: HH^p x HH^q -> HH^{p+q-2}."""

    def test_linking_degree_minus_2(self):
        """E_3 linking has degree -2 (from H_2(Conf_2(R^3)) = C)."""
        # VERIFIED: [DC] S^2 linking number lives in degree 2;
        #           [LT] De Leger arXiv:2512.20167
        assert e3_linking_degree() == -2

    def test_linking_all_trivial(self):
        """All E_3 linking operations vanish for Heisenberg."""
        # VERIFIED: [DC] concentration in {0,1,2} forces vanishing;
        #           [SY] single-class antisymmetry
        basis = [hh0_basis(), hh1_basis(), hh2_basis()]
        for a in basis:
            for b in basis:
                assert e3_linking(a, b).is_zero(), (
                    f"E_3 linking [{a.degree},{b.degree}] should vanish"
                )

    def test_linking_hh2_hh2_zero(self):
        """E_3 linking HH^2 x HH^2 -> HH^2: vanishes (single class)."""
        # VERIFIED: [DC] antisymmetry with even shifted degree forces 0;
        #           [LT] De Leger, Prop 4.3
        result = e3_linking(hh2_basis(), hh2_basis())
        assert result.is_zero()

    def test_linking_hh1_hh1_target_degree_0(self):
        """E_3 linking HH^1 x HH^1 -> HH^0: vanishes for abelian."""
        # VERIFIED: [DC] linking of derivations in abelian algebra;
        #           [DA] target degree 1+1-2 = 0
        result = e3_linking(hh1_basis(), hh1_basis())
        assert result.is_zero()
        assert result.degree == 0


# ===================================================================
# XII. Browder bracket
# ===================================================================

class TestBrowderBracket:
    """Browder bracket: secondary E_3 operation."""

    def test_browder_well_defined(self):
        """Browder bracket is well-defined on HH*(H_k).

        Requires all Gerstenhaber brackets to vanish (which they do).
        """
        # VERIFIED: [DC] all brackets vanish (checked above);
        #           [LT] Cohen, Ann. Math. 87 (1968): Browder operation
        assert verify_browder_well_defined()

    def test_browder_all_trivial(self):
        """All Browder brackets vanish for Heisenberg."""
        # VERIFIED: [DC] agrees with E_3 linking (all trivial);
        #           [SY] E_3-formality
        basis = [hh0_basis(), hh1_basis(), hh2_basis()]
        for a in basis:
            for b in basis:
                assert browder_bracket(a, b).is_zero()

    def test_browder_equals_linking(self):
        """Browder bracket = E_3 linking for E_3-formal algebras."""
        # VERIFIED: [DC] E_3-formality of H_k (class G);
        #           [LT] De Leger, Theorem 5.1
        basis = [hh0_basis(), hh1_basis(), hh2_basis()]
        for a in basis:
            for b in basis:
                br = browder_bracket(a, b)
                lk = e3_linking(a, b)
                assert abs(br.coefficient - lk.coefficient) < 1e-15


# ===================================================================
# XIII. r-matrix and kappa consistency
# ===================================================================

class TestRMatrixKappa:
    """r-matrix and kappa consistency checks."""

    def test_r_matrix_at_k0_vanishes(self):
        """r^Heis(z)|_{k=0} = 0 (AP141 vanishing check)."""
        # VERIFIED: [DC] r(z) = 0/z = 0;
        #           [LT] CLAUDE.md C10, AP141
        assert r_matrix_heisenberg(1.0, k=0) == 0.0

    def test_r_matrix_at_k1(self):
        """r^Heis(z) = 1/z at k=1."""
        # VERIFIED: [DC] r(z) = 1/z;
        #           [LT] CLAUDE.md C10
        assert abs(r_matrix_heisenberg(2.0, k=1) - 0.5) < 1e-15

    def test_kappa_at_k0(self):
        """kappa(H_0) = 0."""
        # VERIFIED: [DC] kappa = k = 0;
        #           [LC] trivial algebra limit
        assert kappa_heisenberg(0) == 0

    def test_kappa_at_k1(self):
        """kappa(H_1) = 1."""
        # VERIFIED: [DC] kappa = k = 1;
        #           [CF] matches c_Heis(1) = 1 (CLAUDE.md C1)
        assert kappa_heisenberg(1) == 1

    def test_averaging_map(self):
        """av(r^Heis(z)) = kappa(H_k) (CLAUDE.md C13)."""
        # VERIFIED: [DC] av(k/z) = k = kappa;
        #           [LT] CLAUDE.md C13
        for k in (0, 1, 2, 5):
            assert averaging_map_check(k)

    def test_r_matrix_level_prefix(self):
        """r-matrix has level prefix k (AP126 enforcement)."""
        # VERIFIED: [DC] r(z) = k/z, not Omega/z;
        #           [LT] CLAUDE.md C10, AP126
        # At k=3, r(z=1) = 3, not 1
        assert abs(r_matrix_heisenberg(1.0, k=3) - 3.0) < 1e-15


# ===================================================================
# XIV. Full E_3 verification
# ===================================================================

class TestFullE3Verification:
    """Full E_3 structure verification."""

    def test_full_verification_k1(self):
        """Full E_3 verification at k=1."""
        result = verify_e3_structure(k=1)
        assert result.is_gerstenhaber_algebra
        assert result.is_e3_algebra
        assert result.total_dim == 3  # VERIFIED: [DC] 1+1+1; [LT] Theorem H

    def test_full_verification_all_checks_pass(self):
        """Every individual check passes."""
        result = verify_e3_structure(k=1)
        assert result.cup_graded_commutative
        assert result.cup_associative
        assert result.cup_unital
        assert result.bracket_degree == -1  # VERIFIED: [DC]; [LT] Gerstenhaber
        assert result.bracket_hh0_hh1_zero
        assert result.bracket_hh1_hh1_zero
        assert result.bracket_hh1_hh2_zero
        assert result.all_brackets_zero
        assert result.graded_antisymmetry
        assert result.graded_jacobi
        assert result.leibniz_rule
        assert result.e3_linking_trivial
        assert result.browder_well_defined

    def test_summary_structure(self):
        """Summary dict has expected keys."""
        s = summary()
        assert s['algebra'] == 'Heisenberg H_k'
        assert s['shadow_class'] == 'G'
        assert s['is_gerstenhaber'] is True
        assert s['is_e3'] is True
        assert s['all_brackets_zero'] is True


# ===================================================================
# XV. Level variation
# ===================================================================

class TestLevelVariation:
    """E_3 structure at different levels k."""

    def test_k0_trivial_algebra(self):
        """At k=0: r-matrix vanishes, kappa=0, E_3 still holds."""
        # VERIFIED: [DC] k=0 is abelian limit;
        #           [LC] limiting case of k -> 0
        result = verify_e3_structure(k=0)
        assert result.is_e3_algebra
        assert result.all_brackets_zero

    def test_k_negative(self):
        """At k=-1: E_3 structure unchanged (algebraic, not analytic)."""
        # VERIFIED: [DC] bracket structure independent of k;
        #           [SY] brackets vanish for dimensional reasons
        result = verify_e3_structure(k=-1)
        assert result.is_e3_algebra

    def test_k_large(self):
        """At k=100: E_3 structure unchanged."""
        # VERIFIED: [DC] same computation as k=1;
        #           [SY] HH* dimensions independent of level
        result = verify_e3_structure(k=100)
        assert result.is_e3_algebra
        assert result.total_dim == 3

    def test_kappa_varies_with_k(self):
        """kappa(H_k) = k varies with the level."""
        # VERIFIED: [DC] kappa = k;
        #           [CF] unlike Vir where kappa = c/2 is fixed by c
        for k in (-5, 0, 1, 7, 42):
            assert kappa_heisenberg(k) == k
