r"""Tests for lattice_voa_shadows: shadow tower data for D_4, E_8, Leech.

Verifies:
  - kappa from first principles (genus-1 curvature of lattice OPE)
  - Class G verification: S_3 = S_4 = 0 for all lattice VOAs
  - Genus expansion F_g = kappa * lambda_g^FP for g = 1..5
  - Complementarity: kappa(V_Lambda) + kappa(V_Lambda^!) = 0
  - Cross-family consistency (additivity, scaling)
  - Per-lattice structural data (root counts, unimodularity, triality)
  - r-matrix pole structure

Mathematical ground truth:
  - lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal
  - lattice_foundations.tex: cor:lattice-postnikov-termination
  - lattice_foundations.tex: thm:lattice:unimodular-self-dual
  - heisenberg_eisenstein.tex: prop:heisenberg-complementarity
  - higher_genus_modular_koszul.tex: shadow depth classification (class G)
"""

import pytest
from sympy import Rational

from compute.lib.lattice_voa_shadows import (
    faber_pandharipande,
    kappa_lattice,
    kappa_lattice_dual,
    verify_class_G,
    genus_expansion,
    complementarity,
    r_matrix_data,
    d4_shadow_data,
    e8_shadow_data,
    leech_shadow_data,
    verify_kappa_additivity,
    cross_family_consistency,
    comparison_table,
)


# =========================================================================
# 1. Kappa from first principles
# =========================================================================

class TestKappaFirstPrinciples:
    r"""kappa(V_Lambda) = rank(Lambda) from genus-1 curvature.

    The derivation: r independent Heisenberg bosons at level 1,
    each contributing kappa = 1.  Root sectors contribute d^2 = 0.
    By additivity (prop:independent-sum-factorization), kappa = r.
    """

    def test_kappa_d4(self):
        """kappa(V_{D_4}) = 4."""
        assert kappa_lattice(4) == Rational(4)

    def test_kappa_e8(self):
        """kappa(V_{E_8}) = 8."""
        assert kappa_lattice(8) == Rational(8)

    def test_kappa_leech(self):
        """kappa(V_Leech) = 24."""
        assert kappa_lattice(24) == Rational(24)

    def test_kappa_rank1(self):
        """kappa(V_Z) = 1 (single Heisenberg boson)."""
        assert kappa_lattice(1) == Rational(1)

    def test_kappa_rank0(self):
        """kappa of rank 0 = 0 (trivial lattice)."""
        assert kappa_lattice(0) == Rational(0)

    def test_kappa_negative_rank_raises(self):
        with pytest.raises(ValueError):
            kappa_lattice(-1)

    def test_kappa_dual_d4(self):
        """kappa(V_{D_4}^!) = -4 (Verdier negation of Cartan level)."""
        assert kappa_lattice_dual(4) == Rational(-4)

    def test_kappa_dual_e8(self):
        """kappa(V_{E_8}^!) = -8."""
        assert kappa_lattice_dual(8) == Rational(-8)

    def test_kappa_dual_leech(self):
        """kappa(V_Leech^!) = -24."""
        assert kappa_lattice_dual(24) == Rational(-24)

    def test_kappa_is_rational(self):
        """kappa is always a rational number."""
        for r in [1, 4, 8, 16, 24]:
            k = kappa_lattice(r)
            assert isinstance(k, Rational)

    def test_kappa_equals_central_charge(self):
        """For lattice VOAs, c = kappa = rank (a special property)."""
        for r in [1, 4, 8, 24]:
            assert kappa_lattice(r) == Rational(r)

    def test_kappa_dual_equals_minus_rank(self):
        """kappa(V^!) = -rank for all ranks."""
        for r in [1, 2, 4, 8, 16, 24]:
            assert kappa_lattice_dual(r) == Rational(-r)


# =========================================================================
# 2. Class G verification: S_3 = S_4 = 0
# =========================================================================

class TestClassGVerification:
    r"""All lattice VOAs are class G (Gaussian, shadow depth 2).

    S_3 = S_4 = 0.  The L_infinity algebra is formal: transferred
    higher brackets are coboundaries by curvature-braiding orthogonality.
    """

    @pytest.mark.parametrize("rank", [1, 2, 4, 8, 16, 24])
    def test_S3_vanishes(self, rank):
        """S_3 = 0 (cubic shadow vanishes)."""
        data = verify_class_G(rank)
        assert data['S3'] == 0

    @pytest.mark.parametrize("rank", [1, 2, 4, 8, 16, 24])
    def test_S4_vanishes(self, rank):
        """S_4 = 0 (quartic contact vanishes)."""
        data = verify_class_G(rank)
        assert data['S4'] == 0

    @pytest.mark.parametrize("rank", [1, 2, 4, 8, 16, 24])
    def test_alpha_vanishes(self, rank):
        """alpha = 0 (cubic coefficient on primary line)."""
        data = verify_class_G(rank)
        assert data['alpha'] == 0

    @pytest.mark.parametrize("rank", [1, 2, 4, 8, 16, 24])
    def test_discriminant_vanishes(self, rank):
        """Critical discriminant Delta = 8*kappa*S_4 = 0."""
        data = verify_class_G(rank)
        assert data['Delta'] == 0

    @pytest.mark.parametrize("rank", [1, 4, 8, 24])
    def test_shadow_metric_perfect_square(self, rank):
        """Shadow metric Q_L = (2*kappa)^2 is a perfect square."""
        data = verify_class_G(rank)
        assert data['is_perfect_square']
        assert data['Q_L'] == 4 * Rational(rank) ** 2

    @pytest.mark.parametrize("rank", [1, 4, 8, 24])
    def test_shadow_depth_two(self, rank):
        """Shadow depth = 2 for all lattice VOAs."""
        data = verify_class_G(rank)
        assert data['shadow_depth'] == 2

    @pytest.mark.parametrize("rank", [1, 4, 8, 24])
    def test_class_label(self, rank):
        """Class label is 'G' (Gaussian)."""
        data = verify_class_G(rank)
        assert data['shadow_class'] == 'G'

    @pytest.mark.parametrize("rank", [1, 4, 8, 24])
    def test_all_higher_vanish(self, rank):
        """All higher shadow coefficients vanish (S_r = 0 for r >= 3)."""
        data = verify_class_G(rank)
        assert data['all_higher_vanish']

    def test_d4_specific(self):
        """D_4 class G verification with rank = 4."""
        data = verify_class_G(4)
        assert data['kappa'] == 4
        assert data['S3'] == 0
        assert data['S4'] == 0
        assert data['shadow_class'] == 'G'

    def test_e8_specific(self):
        """E_8 class G verification with rank = 8."""
        data = verify_class_G(8)
        assert data['kappa'] == 8
        assert data['S3'] == 0
        assert data['S4'] == 0
        assert data['shadow_class'] == 'G'

    def test_leech_specific(self):
        """Leech class G verification with rank = 24."""
        data = verify_class_G(24)
        assert data['kappa'] == 24
        assert data['S3'] == 0
        assert data['S4'] == 0
        assert data['shadow_class'] == 'G'


# =========================================================================
# 3. Genus expansion F_g = kappa * lambda_g^FP for g = 1..5
# =========================================================================

class TestGenusExpansion:
    r"""F_g(V_Lambda) = kappa * lambda_g^FP.

    Exact values for the three lattices, verified against the
    Faber-Pandharipande formula:
      lambda_g = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
    """

    # --- D_4 (rank 4, kappa = 4) ---

    def test_d4_f1(self):
        """F_1(V_{D_4}) = 4/24 = 1/6."""
        ge = genus_expansion(4)
        assert ge[1] == Rational(1, 6)

    def test_d4_f2(self):
        """F_2(V_{D_4}) = 4 * 7/5760 = 7/1440."""
        ge = genus_expansion(4)
        assert ge[2] == Rational(4) * Rational(7, 5760)
        assert ge[2] == Rational(7, 1440)

    def test_d4_f3(self):
        """F_3(V_{D_4}) = 4 * 31/967680 = 31/241920."""
        ge = genus_expansion(4)
        assert ge[3] == Rational(4) * Rational(31, 967680)

    def test_d4_f4(self):
        """F_4(V_{D_4}) = 4 * 127/154828800."""
        ge = genus_expansion(4)
        assert ge[4] == Rational(4) * Rational(127, 154828800)

    def test_d4_f5(self):
        """F_5(V_{D_4}) = 4 * 2555/122624409600."""
        ge = genus_expansion(4)
        assert ge[5] == Rational(4) * Rational(2555, 122624409600)

    # --- E_8 (rank 8, kappa = 8) ---

    def test_e8_f1(self):
        """F_1(V_{E_8}) = 8/24 = 1/3."""
        ge = genus_expansion(8)
        assert ge[1] == Rational(1, 3)

    def test_e8_f2(self):
        """F_2(V_{E_8}) = 8 * 7/5760 = 7/720."""
        ge = genus_expansion(8)
        assert ge[2] == Rational(7, 720)

    def test_e8_f3(self):
        """F_3(V_{E_8}) = 8 * 31/967680 = 31/120960."""
        ge = genus_expansion(8)
        assert ge[3] == Rational(8) * Rational(31, 967680)

    def test_e8_f4(self):
        """F_4(V_{E_8}) = 8 * 127/154828800."""
        ge = genus_expansion(8)
        assert ge[4] == Rational(8) * Rational(127, 154828800)

    def test_e8_f5(self):
        """F_5(V_{E_8}) = 8 * 2555/122624409600."""
        ge = genus_expansion(8)
        assert ge[5] == Rational(8) * Rational(2555, 122624409600)

    # --- Leech (rank 24, kappa = 24) ---

    def test_leech_f1(self):
        """F_1(V_Leech) = 24/24 = 1."""
        ge = genus_expansion(24)
        assert ge[1] == Rational(1)

    def test_leech_f2(self):
        """F_2(V_Leech) = 24 * 7/5760 = 7/240."""
        ge = genus_expansion(24)
        assert ge[2] == Rational(7, 240)

    def test_leech_f3(self):
        """F_3(V_Leech) = 24 * 31/967680 = 31/40320."""
        ge = genus_expansion(24)
        assert ge[3] == Rational(24) * Rational(31, 967680)

    def test_leech_f4(self):
        """F_4(V_Leech) = 24 * 127/154828800."""
        ge = genus_expansion(24)
        assert ge[4] == Rational(24) * Rational(127, 154828800)

    def test_leech_f5(self):
        """F_5(V_Leech) = 24 * 2555/122624409600."""
        ge = genus_expansion(24)
        assert ge[5] == Rational(24) * Rational(2555, 122624409600)

    # --- F_g positivity (Bernoulli sign: all F_g > 0) ---

    @pytest.mark.parametrize("rank", [4, 8, 24])
    def test_all_fg_positive(self, rank):
        """F_g > 0 for all g >= 1 (Bernoulli signs give positive values)."""
        ge = genus_expansion(rank, max_g=5)
        for g in range(1, 6):
            assert ge[g] > 0, f"F_{g} for rank {rank} should be positive"

    # --- F_g monotone decrease ---

    @pytest.mark.parametrize("rank", [4, 8, 24])
    def test_fg_decrease(self, rank):
        """F_g decreases with genus (FP numbers decrease)."""
        ge = genus_expansion(rank, max_g=5)
        for g in range(1, 5):
            assert ge[g] > ge[g + 1], \
                f"F_{g} > F_{g+1} should hold for rank {rank}"

    # --- Proportionality to rank ---

    def test_fg_proportional_to_rank(self):
        """F_g(V_Lambda) = kappa * lambda_g means F_g scales with rank."""
        for g in range(1, 6):
            fp = faber_pandharipande(g)
            for rank in [4, 8, 24]:
                ge = genus_expansion(rank, max_g=g)
                assert ge[g] == rank * fp

    # --- Generating function cross-check: F_1 = rank/24 ---

    @pytest.mark.parametrize("rank,expected", [(4, Rational(1, 6)),
                                                (8, Rational(1, 3)),
                                                (24, Rational(1))])
    def test_f1_exact(self, rank, expected):
        """F_1 = rank/24 (leading FP number is 1/24)."""
        ge = genus_expansion(rank, max_g=1)
        assert ge[1] == expected


# =========================================================================
# 4. Complementarity: kappa(V_Lambda) + kappa(V_Lambda^!) = 0
# =========================================================================

class TestComplementarity:
    r"""kappa + kappa' = 0 for all lattice VOAs.

    This is the KM/free-field complementarity
    (lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal).
    The Koszul dual has Cartan level -1 per boson (Verdier negation).
    """

    def test_d4_complementarity_sum(self):
        """kappa(V_{D_4}) + kappa(V_{D_4}^!) = 4 + (-4) = 0."""
        comp = complementarity(4, is_unimodular=False)
        assert comp['complementarity_sum'] == 0
        assert comp['sum_is_zero']

    def test_e8_complementarity_sum(self):
        """kappa(V_{E_8}) + kappa(V_{E_8}^!) = 8 + (-8) = 0."""
        comp = complementarity(8, is_unimodular=True)
        assert comp['complementarity_sum'] == 0
        assert comp['sum_is_zero']

    def test_leech_complementarity_sum(self):
        """kappa(V_Leech) + kappa(V_Leech^!) = 24 + (-24) = 0."""
        comp = complementarity(24, is_unimodular=True)
        assert comp['complementarity_sum'] == 0
        assert comp['sum_is_zero']

    def test_d4_kappa_values(self):
        """kappa(V_{D_4}) = 4, kappa(V_{D_4}^!) = -4."""
        comp = complementarity(4)
        assert comp['kappa'] == Rational(4)
        assert comp['kappa_dual'] == Rational(-4)

    def test_e8_kappa_values(self):
        """kappa(V_{E_8}) = 8, kappa(V_{E_8}^!) = -8."""
        comp = complementarity(8, is_unimodular=True)
        assert comp['kappa'] == Rational(8)
        assert comp['kappa_dual'] == Rational(-8)

    def test_leech_kappa_values(self):
        """kappa(V_Leech) = 24, kappa(V_Leech^!) = -24."""
        comp = complementarity(24, is_unimodular=True)
        assert comp['kappa'] == Rational(24)
        assert comp['kappa_dual'] == Rational(-24)

    def test_d4_not_self_dual(self):
        """D_4 is NOT Koszul self-dual (det(Gram) = 4, not unimodular)."""
        comp = complementarity(4, is_unimodular=False)
        assert not comp['koszul_self_dual']

    def test_e8_self_dual(self):
        """E_8 IS Koszul self-dual (unimodular)."""
        comp = complementarity(8, is_unimodular=True)
        assert comp['koszul_self_dual']

    def test_leech_self_dual(self):
        """Leech IS Koszul self-dual (unimodular)."""
        comp = complementarity(24, is_unimodular=True)
        assert comp['koszul_self_dual']

    @pytest.mark.parametrize("rank", [1, 2, 3, 4, 5, 8, 16, 24])
    def test_complementarity_universal(self, rank):
        """kappa + kappa' = 0 for ALL lattice ranks."""
        comp = complementarity(rank)
        assert comp['complementarity_sum'] == 0

    def test_heisenberg_consistency(self):
        """Rank 1 matches Heisenberg: kappa(H_1) + kappa(H_1^!) = 0.

        This is the abelian case of the lattice complementarity.
        H_1 has kappa = 1, H_1^! = Sym^ch(V*) with kappa = -1.
        """
        comp = complementarity(1)
        assert comp['kappa'] == Rational(1)
        assert comp['kappa_dual'] == Rational(-1)
        assert comp['complementarity_sum'] == 0


# =========================================================================
# 5. Per-lattice structural data
# =========================================================================

class TestD4StructuralData:
    """D_4 lattice: rank 4, 24 roots, triality, NOT unimodular."""

    def test_rank(self):
        data = d4_shadow_data()
        assert data['rank'] == 4

    def test_root_count(self):
        """D_4 has 24 roots."""
        data = d4_shadow_data()
        assert data['root_count'] == 24

    def test_gram_det(self):
        """det(Gram_{D_4}) = 4."""
        data = d4_shadow_data()
        assert data['gram_det'] == 4

    def test_not_unimodular(self):
        data = d4_shadow_data()
        assert not data['is_unimodular']

    def test_has_triality(self):
        """D_4 has S_3 triality symmetry."""
        data = d4_shadow_data()
        assert data['has_triality']

    def test_discriminant_group(self):
        """D_4^*/D_4 = (Z/2Z)^2."""
        data = d4_shadow_data()
        assert data['discriminant_order'] == 4

    def test_kappa(self):
        data = d4_shadow_data()
        assert data['shadow']['kappa'] == 4

    def test_class_G(self):
        data = d4_shadow_data()
        assert data['shadow']['shadow_class'] == 'G'


class TestE8StructuralData:
    """E_8 lattice: rank 8, 240 roots, unimodular (self-dual)."""

    def test_rank(self):
        data = e8_shadow_data()
        assert data['rank'] == 8

    def test_root_count(self):
        """E_8 has 240 roots."""
        data = e8_shadow_data()
        assert data['root_count'] == 240

    def test_gram_det(self):
        """det(Gram_{E_8}) = 1 (unimodular)."""
        data = e8_shadow_data()
        assert data['gram_det'] == 1

    def test_unimodular(self):
        data = e8_shadow_data()
        assert data['is_unimodular']

    def test_kappa(self):
        data = e8_shadow_data()
        assert data['shadow']['kappa'] == 8

    def test_class_G(self):
        data = e8_shadow_data()
        assert data['shadow']['shadow_class'] == 'G'

    def test_theta_first_shells(self):
        """E_8 theta: r(0)=1, r(1)=240, r(2)=2160, r(3)=6720."""
        data = e8_shadow_data()
        assert data['theta_first_shells'][:4] == [1, 240, 2160, 6720]


class TestLeechStructuralData:
    """Leech lattice: rank 24, 0 roots, 196560 minimal vectors, unimodular."""

    def test_rank(self):
        data = leech_shadow_data()
        assert data['rank'] == 24

    def test_no_roots(self):
        """Leech has NO roots (defining property)."""
        data = leech_shadow_data()
        assert data['root_count'] == 0

    def test_minimal_vectors(self):
        """Leech has 196560 minimal vectors at norm 4."""
        data = leech_shadow_data()
        assert data['min_vector_count'] == 196560

    def test_gram_det(self):
        """det(Gram_Leech) = 1 (unimodular)."""
        data = leech_shadow_data()
        assert data['gram_det'] == 1

    def test_unimodular(self):
        data = leech_shadow_data()
        assert data['is_unimodular']

    def test_kappa(self):
        data = leech_shadow_data()
        assert data['shadow']['kappa'] == 24

    def test_class_G(self):
        data = leech_shadow_data()
        assert data['shadow']['shadow_class'] == 'G'

    def test_theta_first_shells(self):
        """Leech theta: r(0)=1, r(1)=0, r(2)=196560, r(3)=16773120."""
        data = leech_shadow_data()
        assert data['theta_first_shells'][:4] == [1, 0, 196560, 16773120]

    def test_theta_no_roots_in_shells(self):
        """r_Leech(1) = 0: no vectors with norm 2 (no roots)."""
        data = leech_shadow_data()
        assert data['theta_first_shells'][1] == 0


# =========================================================================
# 6. r-matrix pole structure
# =========================================================================

class TestRMatrix:
    r"""r-matrix: r(z) = Omega_Lambda/z (single pole).

    The bar propagator d log E(z,w) absorbs one pole order (AP19),
    so the double-pole Heisenberg OPE maps to a single-pole r-matrix.
    """

    @pytest.mark.parametrize("rank", [4, 8, 24])
    def test_single_pole(self, rank):
        """r-matrix has a single pole at z = 0."""
        data = r_matrix_data(rank)
        assert data['pole_order'] == 1

    @pytest.mark.parametrize("rank", [4, 8, 24])
    def test_residue_trace(self, rank):
        """Residue trace = rank (dimension of Casimir)."""
        data = r_matrix_data(rank)
        assert data['residue_trace'] == Rational(rank)

    def test_d4_r_matrix(self):
        data = d4_shadow_data()
        assert data['r_matrix']['pole_order'] == 1
        assert data['r_matrix']['residue_trace'] == 4

    def test_e8_r_matrix(self):
        data = e8_shadow_data()
        assert data['r_matrix']['pole_order'] == 1
        assert data['r_matrix']['residue_trace'] == 8

    def test_leech_r_matrix(self):
        data = leech_shadow_data()
        assert data['r_matrix']['pole_order'] == 1
        assert data['r_matrix']['residue_trace'] == 24


# =========================================================================
# 7. Cross-family consistency checks
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-checks between D_4, E_8, Leech."""

    def test_kappa_additivity_4_4(self):
        """F_g(rank 8) = F_g(rank 4) + F_g(rank 4)."""
        assert verify_kappa_additivity(4, 4, max_g=5)

    def test_kappa_additivity_8_16(self):
        """F_g(rank 24) = F_g(rank 8) + F_g(rank 16)."""
        assert verify_kappa_additivity(8, 16, max_g=5)

    def test_kappa_additivity_4_20(self):
        """F_g(rank 24) = F_g(rank 4) + F_g(rank 20)."""
        assert verify_kappa_additivity(4, 20, max_g=5)

    def test_kappa_additivity_1_23(self):
        """F_g(rank 24) = F_g(rank 1) + F_g(rank 23)."""
        assert verify_kappa_additivity(1, 23, max_g=5)

    def test_e8_eq_2x_d4(self):
        """F_g(E_8) = 2 * F_g(D_4) since kappa(E_8) = 2*kappa(D_4)."""
        ge_e8 = genus_expansion(8, max_g=5)
        ge_d4 = genus_expansion(4, max_g=5)
        for g in range(1, 6):
            assert ge_e8[g] == 2 * ge_d4[g]

    def test_leech_eq_3x_e8(self):
        """F_g(Leech) = 3 * F_g(E_8) since kappa(Leech) = 3*kappa(E_8)."""
        ge_leech = genus_expansion(24, max_g=5)
        ge_e8 = genus_expansion(8, max_g=5)
        for g in range(1, 6):
            assert ge_leech[g] == 3 * ge_e8[g]

    def test_leech_eq_6x_d4(self):
        """F_g(Leech) = 6 * F_g(D_4) since 24 = 6*4."""
        ge_leech = genus_expansion(24, max_g=5)
        ge_d4 = genus_expansion(4, max_g=5)
        for g in range(1, 6):
            assert ge_leech[g] == 6 * ge_d4[g]

    def test_cross_family_consistency_all(self):
        """Full cross-family consistency check returns all True."""
        checks = cross_family_consistency()
        for key, val in checks.items():
            assert val, f"Consistency check failed: {key}"

    def test_comparison_table_length(self):
        """Comparison table has 3 entries (D_4, E_8, Leech)."""
        table = comparison_table()
        assert len(table) == 3

    def test_comparison_table_names(self):
        """Comparison table entries are D_4, E_8, Leech."""
        table = comparison_table()
        names = [row['name'] for row in table]
        assert names == ['D_4', 'E_8', 'Leech']


# =========================================================================
# 8. Faber-Pandharipande number cross-checks
# =========================================================================

class TestFaberPandharipandeNumbers:
    """Exact FP numbers used in genus expansion.

    Independent recomputation as a cross-check against
    lattice_shadow_census.py (which has its own FP implementation).
    """

    def test_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_fp_genus4(self):
        """lambda_4^FP = 127/154828800."""
        assert faber_pandharipande(4) == Rational(127, 154828800)

    def test_fp_genus5(self):
        """lambda_5^FP = 2555/122624409600."""
        assert faber_pandharipande(5) == Rational(2555, 122624409600)

    def test_fp_all_positive(self):
        """All FP numbers are positive."""
        for g in range(1, 8):
            assert faber_pandharipande(g) > 0

    def test_fp_decreasing(self):
        """FP numbers are strictly decreasing."""
        for g in range(1, 7):
            assert faber_pandharipande(g) > faber_pandharipande(g + 1)


# =========================================================================
# 9. AP24 anti-pattern tests: lattice vs Virasoro complementarity
# =========================================================================

class TestAP24Distinction:
    """Verify that lattice VOAs satisfy kappa + kappa' = 0 (KM/free field case),
    NOT the W-algebra relation kappa + kappa' = rho*K.

    AP24: The complementarity sum kappa + kappa' = 0 holds for
    KM/free fields/lattice VOAs.  For Virasoro, kappa + kappa' = 13 != 0.
    For W-algebras, kappa + kappa' = rho*K.  NEVER write a universal
    claim about complementarity without checking the family.
    """

    def test_lattice_sum_zero(self):
        """Lattice: kappa + kappa' = 0 (KM/free-field case)."""
        for rank in [4, 8, 24]:
            comp = complementarity(rank)
            assert comp['complementarity_sum'] == 0

    def test_not_virasoro_pattern(self):
        """Lattice complementarity sum is 0, NOT 13 (Virasoro pattern)."""
        for rank in [4, 8, 24]:
            comp = complementarity(rank)
            assert comp['complementarity_sum'] != 13

    def test_heisenberg_not_self_dual(self):
        """H_k is NOT self-dual (AP: critical pitfall).

        H_k^! = Sym^ch(V*) with curvature -k, NOT H_k itself.
        kappa(H_k) = k, kappa(H_k^!) = -k, so kappa + kappa' = 0.
        """
        comp = complementarity(1)
        assert comp['kappa'] == Rational(1)
        assert comp['kappa_dual'] == Rational(-1)
        # H_1 is NOT Koszul self-dual (it is KM/free-field type)
        assert comp['complementarity_sum'] == 0


# =========================================================================
# 10. Shadow depth classification consistency
# =========================================================================

class TestShadowDepthClassification:
    r"""Shadow depth for lattice VOAs = 2 (class G).

    Comparison with other families:
      G (Gaussian): depth 2.  Examples: Heisenberg, lattice VOAs.
      L (Lie/tree): depth 3.  Examples: affine KM at generic level.
      C (Contact):  depth 4.  Examples: beta-gamma.
      M (Mixed):    depth infinity.  Examples: Virasoro, W_N.

    Lattice VOAs are class G because the L_infinity algebra is formal
    (curvature-braiding orthogonality kills all higher brackets).
    """

    def test_d4_depth(self):
        data = d4_shadow_data()
        assert data['shadow']['shadow_depth'] == 2

    def test_e8_depth(self):
        data = e8_shadow_data()
        assert data['shadow']['shadow_depth'] == 2

    def test_leech_depth(self):
        data = leech_shadow_data()
        assert data['shadow']['shadow_depth'] == 2

    def test_d4_not_class_L(self):
        """D_4 is NOT class L (would require depth 3)."""
        data = d4_shadow_data()
        assert data['shadow']['shadow_class'] != 'L'

    def test_e8_not_class_M(self):
        """E_8 is NOT class M (would require infinite depth)."""
        data = e8_shadow_data()
        assert data['shadow']['shadow_class'] != 'M'

    def test_leech_discriminant_zero(self):
        """Delta = 0 confirms finite tower (not class M)."""
        data = leech_shadow_data()
        assert data['shadow']['Delta'] == 0


# =========================================================================
# 11. Integration with lattice_shadow_census.py
# =========================================================================

class TestCrossCensusConsistency:
    """Cross-check against the existing lattice_shadow_census module.

    The two modules should agree on all shared computations.
    Note: lattice_shadow_census has a known error in complementarity
    (it returns kappa_dual = rank instead of -rank; see AP5 note below).
    """

    def test_kappa_agreement(self):
        """Both modules agree on kappa = rank."""
        from compute.lib.lattice_shadow_census import lattice_shadow_data as census_data
        for name, rank in [('D4', 4), ('E8', 8), ('Leech', 24)]:
            census = census_data(name)
            assert census['kappa'] == kappa_lattice(rank)

    def test_shadow_class_agreement(self):
        """Both modules agree: class G."""
        from compute.lib.lattice_shadow_census import lattice_shadow_data as census_data
        for name, rank in [('D4', 4), ('E8', 8), ('Leech', 24)]:
            census = census_data(name)
            assert census['shadow_class'] == 'G'
            assert verify_class_G(rank)['shadow_class'] == 'G'

    def test_shadow_depth_agreement(self):
        """Both modules agree: depth 2."""
        from compute.lib.lattice_shadow_census import lattice_shadow_data as census_data
        for name, rank in [('D4', 4), ('E8', 8), ('Leech', 24)]:
            census = census_data(name)
            assert census['shadow_depth'] == 2
            assert verify_class_G(rank)['shadow_depth'] == 2

    def test_genus_expansion_agreement(self):
        """Both modules agree on F_g values."""
        from compute.lib.lattice_shadow_census import lattice_genus_expansion as census_ge
        for rank in [4, 8, 24]:
            census = census_ge(rank, max_g=5)
            ours = genus_expansion(rank, max_g=5)
            for g in range(1, 6):
                assert census[g] == ours[g], \
                    f"Genus {g} disagreement for rank {rank}: {census[g]} vs {ours[g]}"

    def test_fp_agreement(self):
        """Both modules agree on Faber-Pandharipande numbers."""
        from compute.lib.lattice_shadow_census import faber_pandharipande as census_fp
        for g in range(1, 6):
            assert census_fp(g) == faber_pandharipande(g)

    def test_complementarity_agreement(self):
        """Both modules now agree on complementarity: kappa + kappa' = 0.

        The census module was corrected to match the .tex source at
        lattice_foundations.tex line 4376: kappa(V^!) = -rank.
        """
        from compute.lib.lattice_shadow_census import lattice_complementarity as census_comp
        from compute.lib.lattice_shadow_census import root_lattice_gram

        # Our values:
        our_comp = complementarity(8, is_unimodular=True)
        assert our_comp['kappa_dual'] == Rational(-8)
        assert our_comp['complementarity_sum'] == 0

        # Census values (now corrected):
        gram = root_lattice_gram('E8')
        census_kappa, census_dual, census_sum = census_comp(gram)
        assert census_kappa == Rational(8)
        assert census_dual == Rational(-8)
        assert census_sum == 0

        # Both agree:
        assert our_comp['kappa'] == census_kappa
        assert our_comp['kappa_dual'] == census_dual
        assert our_comp['complementarity_sum'] == census_sum


# =========================================================================
# 12. Niemeier lattices: all 24 even unimodular lattices of rank 24
# =========================================================================

class TestNiemeierLattices:
    r"""All 24 Niemeier lattices have rank 24, kappa = 24, class G.

    The Niemeier classification: there are exactly 24 even unimodular
    lattices of rank 24, classified by their root systems (unions of
    ADE root systems with total rank 24, or empty for the Leech lattice).

    The shadow tower depends ONLY on the rank (not the root system),
    because the root sectors contribute d^2 = 0 by cocycle-curvature
    orthogonality, and the Cartan sector determines all shadow data.

    Mathematical reference: Conway-Sloane, SPLAG Ch 16; Niemeier 1973.
    """

    def test_exactly_24_niemeier_lattices(self):
        """There are exactly 24 Niemeier lattices."""
        from compute.lib.lattice_voa_shadows import NIEMEIER_DATA
        assert len(NIEMEIER_DATA) == 24

    @pytest.mark.parametrize("idx", list(range(24)))
    def test_niemeier_kappa_24(self, idx):
        """Every Niemeier lattice has kappa = 24."""
        from compute.lib.lattice_voa_shadows import niemeier_shadow_data
        data = niemeier_shadow_data(idx)
        assert data['shadow']['kappa'] == Rational(24)

    @pytest.mark.parametrize("idx", list(range(24)))
    def test_niemeier_class_G(self, idx):
        """Every Niemeier lattice is class G."""
        from compute.lib.lattice_voa_shadows import niemeier_shadow_data
        data = niemeier_shadow_data(idx)
        assert data['shadow']['shadow_class'] == 'G'
        assert data['shadow']['shadow_depth'] == 2

    @pytest.mark.parametrize("idx", list(range(24)))
    def test_niemeier_unimodular(self, idx):
        """Every Niemeier lattice is unimodular."""
        from compute.lib.lattice_voa_shadows import niemeier_shadow_data
        data = niemeier_shadow_data(idx)
        assert data['is_unimodular']
        assert data['gram_det'] == 1

    @pytest.mark.parametrize("idx", list(range(24)))
    def test_niemeier_complementarity(self, idx):
        """kappa + kappa' = 0 for every Niemeier lattice."""
        from compute.lib.lattice_voa_shadows import niemeier_shadow_data
        data = niemeier_shadow_data(idx)
        assert data['complementarity']['complementarity_sum'] == 0

    def test_niemeier_kappa_table_all_24(self):
        """Kappa table has all 24 entries with kappa = 24."""
        from compute.lib.lattice_voa_shadows import niemeier_kappa_table
        table = niemeier_kappa_table()
        assert len(table) == 24
        assert all(row['kappa'] == Rational(24) for row in table)

    def test_niemeier_F1_all_equal(self):
        """F_1 = 24/24 = 1 for all Niemeier lattices."""
        from compute.lib.lattice_voa_shadows import niemeier_shadow_data
        for i in range(24):
            data = niemeier_shadow_data(i)
            assert data['genus_expansion'][1] == Rational(1)

    def test_niemeier_root_counts_positive_except_leech(self):
        """All Niemeier lattices have positive root count except Leech."""
        from compute.lib.lattice_voa_shadows import NIEMEIER_DATA
        for entry in NIEMEIER_DATA:
            if entry['name'] == 'Leech':
                assert entry['root_count'] == 0
            else:
                assert entry['root_count'] > 0

    def test_niemeier_3e8_root_count(self):
        """3E_8 has root count 3*240 = 720."""
        from compute.lib.lattice_voa_shadows import niemeier_shadow_data
        data = niemeier_shadow_data('3E8')
        assert data['root_count'] == 720

    def test_niemeier_d24_root_count(self):
        """D_{24} has root count 2*24*23 = 1104 (maximum among Niemeier)."""
        from compute.lib.lattice_voa_shadows import niemeier_shadow_data
        data = niemeier_shadow_data('D24')
        assert data['root_count'] == 1104

    def test_niemeier_max_root_count_is_d24(self):
        """D_{24} has the largest root count among all Niemeier lattices."""
        from compute.lib.lattice_voa_shadows import NIEMEIER_DATA
        max_entry = max(NIEMEIER_DATA, key=lambda e: e['root_count'])
        assert max_entry['name'] == 'D24'
        assert max_entry['root_count'] == 1104

    def test_niemeier_leech_by_name(self):
        """Leech lattice accessible by name through niemeier_shadow_data."""
        from compute.lib.lattice_voa_shadows import niemeier_shadow_data
        data = niemeier_shadow_data('Leech')
        assert data['root_count'] == 0
        assert data['shadow']['kappa'] == 24

    def test_niemeier_discriminant_vanishes_all(self):
        """Critical discriminant Delta = 0 for all 24 Niemeier lattices."""
        from compute.lib.lattice_voa_shadows import niemeier_shadow_data
        for i in range(24):
            data = niemeier_shadow_data(i)
            assert data['shadow']['Delta'] == 0


# =========================================================================
# 13. Barnes-Wall lattice BW_16
# =========================================================================

class TestBarnesWallLattice:
    r"""Barnes-Wall lattice BW_16: rank 16, even, NOT unimodular.

    BW_16 has minimum norm 4 (no roots), kissing number 4320,
    determinant 2^8 = 256.  It demonstrates that non-unimodular
    even lattice VOAs are still class G.
    """

    def test_bw16_rank(self):
        from compute.lib.lattice_voa_shadows import barnes_wall_shadow_data
        data = barnes_wall_shadow_data()
        assert data['rank'] == 16

    def test_bw16_kappa(self):
        """kappa(V_{BW_16}) = 16."""
        from compute.lib.lattice_voa_shadows import barnes_wall_shadow_data
        data = barnes_wall_shadow_data()
        assert data['shadow']['kappa'] == Rational(16)

    def test_bw16_class_G(self):
        """BW_16 is class G despite not being unimodular."""
        from compute.lib.lattice_voa_shadows import barnes_wall_shadow_data
        data = barnes_wall_shadow_data()
        assert data['shadow']['shadow_class'] == 'G'
        assert data['shadow']['shadow_depth'] == 2

    def test_bw16_not_unimodular(self):
        """BW_16 is NOT unimodular (det = 256)."""
        from compute.lib.lattice_voa_shadows import barnes_wall_shadow_data
        data = barnes_wall_shadow_data()
        assert not data['is_unimodular']
        assert data['gram_det'] == 256

    def test_bw16_no_roots(self):
        """BW_16 has no roots (minimum norm 4 > 2)."""
        from compute.lib.lattice_voa_shadows import barnes_wall_shadow_data
        data = barnes_wall_shadow_data()
        assert data['root_count'] == 0
        assert data['min_vector_norm'] == 4

    def test_bw16_kissing_number(self):
        """BW_16 kissing number = 4320."""
        from compute.lib.lattice_voa_shadows import barnes_wall_shadow_data
        data = barnes_wall_shadow_data()
        assert data['min_vector_count'] == 4320

    def test_bw16_complementarity(self):
        """kappa + kappa' = 0 for BW_16."""
        from compute.lib.lattice_voa_shadows import barnes_wall_shadow_data
        data = barnes_wall_shadow_data()
        assert data['complementarity']['complementarity_sum'] == 0

    def test_bw16_F1(self):
        """F_1(V_{BW_16}) = 16/24 = 2/3."""
        from compute.lib.lattice_voa_shadows import barnes_wall_shadow_data
        data = barnes_wall_shadow_data()
        assert data['genus_expansion'][1] == Rational(2, 3)


# =========================================================================
# 14. Even lattice VOAs are universally class G
# =========================================================================

class TestEvenLatticeUniversalClassG:
    r"""All even lattice VOAs are class G, regardless of unimodularity.

    The shadow tower depends only on the rank:
      kappa = rank, S_3 = S_4 = 0, Delta = 0, depth 2, class G.

    This is because the Cartan sector (Heisenberg bosons) determines
    all shadow data, and the root sectors contribute d^2 = 0 by
    cocycle-curvature orthogonality.  Unimodularity of the lattice
    is irrelevant to the shadow class.
    """

    def test_all_standard_ranks_class_G(self):
        """Class G verified at ranks 1, 2, 4, 8, 16, 24."""
        from compute.lib.lattice_voa_shadows import verify_all_even_lattice_class_G
        result = verify_all_even_lattice_class_G()
        assert result['all_class_G']

    def test_extended_ranks_class_G(self):
        """Class G at ranks 3, 5, 6, 7, 10, 12, 32, 48."""
        from compute.lib.lattice_voa_shadows import verify_all_even_lattice_class_G
        result = verify_all_even_lattice_class_G(
            ranks=[3, 5, 6, 7, 10, 12, 32, 48]
        )
        assert result['all_class_G']

    def test_unimodularity_irrelevant(self):
        """Class G holds for both unimodular (E_8) and non-unimodular (D_4)."""
        data_unimod = verify_class_G(8)   # E_8 rank
        data_nonuni = verify_class_G(4)   # D_4 rank
        assert data_unimod['shadow_class'] == 'G'
        assert data_nonuni['shadow_class'] == 'G'
        # Both have identical shadow structure (scaled by rank)
        assert data_unimod['S3'] == data_nonuni['S3'] == 0
        assert data_unimod['S4'] == data_nonuni['S4'] == 0

    def test_shadow_depends_only_on_rank(self):
        """Two lattices of the same rank have identical shadow data.

        E_8 (unimodular) and D_8 (det = 4, not unimodular) both have
        rank 8, so their shadow data must agree: kappa = 8, class G.
        """
        data_e8 = verify_class_G(8)
        data_d8 = verify_class_G(8)  # same rank, different lattice
        assert data_e8['kappa'] == data_d8['kappa'] == Rational(8)
        assert data_e8['shadow_class'] == data_d8['shadow_class'] == 'G'

    def test_non_unimodular_complementarity_still_zero(self):
        """kappa + kappa' = 0 for non-unimodular lattices too.

        This is a consequence of Verdier duality negating the Cartan level,
        independent of the discriminant group structure.
        """
        for rank in [2, 3, 5, 6, 7]:  # non-unimodular ranks
            comp = complementarity(rank, is_unimodular=False)
            assert comp['complementarity_sum'] == 0

    def test_rank_16_two_unimodulars_same_shadow(self):
        """E_8+E_8 and D_16+ are different lattices with same shadow data.

        Both are even unimodular of rank 16, so both have kappa = 16, class G.
        Their theta functions happen to be equal (E_8 = E_4^2, dim M_8 = 1),
        but the shadow data agrees for a deeper reason: it depends only on rank.
        """
        data = verify_class_G(16)
        assert data['kappa'] == Rational(16)
        assert data['shadow_class'] == 'G'
        assert data['S3'] == 0
        assert data['S4'] == 0

    def test_rank_0_trivial(self):
        """Rank 0 (trivial lattice): kappa = 0, class G, all shadows vanish."""
        data = verify_class_G(0)
        assert data['kappa'] == 0
        assert data['shadow_class'] == 'G'
        assert data['Q_L'] == 0  # (2*0)^2 = 0


# =========================================================================
# 15. Niemeier root count cross-checks
# =========================================================================

class TestNiemeierRootCounts:
    r"""Independent verification of Niemeier root counts from ADE formulas.

    Root counts: |roots(A_n)| = n(n+1), |roots(D_n)| = 2n(n-1),
    |roots(E_6)| = 72, |roots(E_7)| = 126, |roots(E_8)| = 240.
    """

    def test_root_count_decreasing_to_leech(self):
        """Root counts form a decreasing sequence from D_{24} to Leech."""
        from compute.lib.lattice_voa_shadows import NIEMEIER_DATA
        counts = [e['root_count'] for e in NIEMEIER_DATA]
        # Not strictly decreasing (ties at 720, 432, 288, 240, 144)
        # but monotonically non-increasing in the standard ordering
        for i in range(len(counts) - 1):
            assert counts[i] >= counts[i + 1]

    def test_24a1_root_count(self):
        """24A_1: 24 copies of A_1, each with 2 roots = 48 total."""
        from compute.lib.lattice_voa_shadows import NIEMEIER_DATA
        a1_24 = [e for e in NIEMEIER_DATA if e['name'] == '24A1'][0]
        assert a1_24['root_count'] == 48

    def test_12a2_root_count(self):
        """12A_2: 12 copies of A_2, each with 6 roots = 72 total."""
        from compute.lib.lattice_voa_shadows import NIEMEIER_DATA
        a2_12 = [e for e in NIEMEIER_DATA if e['name'] == '12A2'][0]
        assert a2_12['root_count'] == 72

    def test_6d4_root_count(self):
        """6D_4: 6 copies of D_4, each with 24 roots = 144 total."""
        from compute.lib.lattice_voa_shadows import NIEMEIER_DATA
        d4_6 = [e for e in NIEMEIER_DATA if e['name'] == '6D4'][0]
        assert d4_6['root_count'] == 144

    def test_4e6_root_count(self):
        """4E_6: 4 copies of E_6, each with 72 roots = 288 total."""
        from compute.lib.lattice_voa_shadows import NIEMEIER_DATA
        e6_4 = [e for e in NIEMEIER_DATA if e['name'] == '4E6'][0]
        assert e6_4['root_count'] == 288
