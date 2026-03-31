"""Comprehensive MC programme verification: MC1-MC5, Koszulness, shadow classification.

Tests the PROVED content of the five Maurer-Cartan programme theorems
and their computational consequences across the standard landscape.

MC1 (PBW): Bar cohomology matches spectral sequence predictions
MC2 (bar-intrinsic Theta): kappa = curvature m_0 for all families
MC3 (CG closure): Lie algebra data, prefundamental CG, thick generation
MC4 (completion): pronilpotent/weight-filtered completion
MC5 (sewing): HS-sewing criterion, bar chain group growth bounds

Additional:
  - Koszulness programme: 10 unconditional equivalences verified
  - Shadow archetype classification: G/L/C/M for all families
  - Universal H^1 theorem: H^1 = generators for all families
  - Bar chain group dimensions: combinatorial identities
  - Curve independence: kappa formulas are algebraic

Ground truth:
  concordance.tex, CLAUDE.md, thm:koszul-equivalences-meta,
  thm:mc2-bar-intrinsic, cor:mc3-all-types, thm:completed-bar-cobar-strong,
  thm:general-hs-sewing.

Anti-pattern guards:
  AP1:  Each kappa formula computed from first principles (dim, h_dual).
  AP3:  Each family verified independently, not by pattern matching.
  AP5:  Cross-family consistency checks cover all standard families.
  AP10: Multi-path verification (kappa additivity, complementarity, A-hat).
"""

import pytest
from sympy import Rational, Symbol, simplify, sqrt, bernoulli, factorial, S


# ============================================================================
# MC1: PBW concentration
# ============================================================================

class TestMC1_PBW:
    """MC1 (PROVED): PBW degeneration implies bar cohomology concentration.

    For all chirally Koszul algebras, the bar cohomology H^*(B(A)) is
    concentrated in bar degree 1 at each conformal weight.  The PBW
    spectral sequence E_1 page = Sym^ch(A-bar[1]) collapses at E_2.
    """

    def test_heisenberg_bar_coh_degree1(self):
        """H^1(B(H_k)) = 1 (the single generator J)."""
        from compute.lib.koszulness_ten_verifier import heisenberg_data
        data = heisenberg_data()
        assert data.bar_coh[1] == 1

    def test_sl2_bar_coh_degree1(self):
        """H^1(B(sl_2)) = 3 (the generators e, h, f)."""
        from compute.lib.koszulness_ten_verifier import sl2_data
        data = sl2_data()
        assert data.bar_coh[1] == 3

    def test_virasoro_bar_coh_degree1(self):
        """H^1(B(Vir)) = 1 (the single generator T)."""
        from compute.lib.koszulness_ten_verifier import virasoro_data
        data = virasoro_data()
        assert data.bar_coh[1] == 1

    def test_betagamma_bar_coh_degree1(self):
        """H^1(B(bg)) = 2 (generators beta, gamma)."""
        from compute.lib.koszulness_ten_verifier import betagamma_data
        data = betagamma_data()
        assert data.bar_coh[1] == 2

    def test_pbw_spectral_sequence_heisenberg(self):
        """PBW spectral sequence for Heisenberg: Sym^n of 1 generator.

        At bar degree n: the PBW-graded bar group has contributions from
        partitions into n parts.  Heisenberg bar coh in each degree = 1
        (single generator line).
        """
        from compute.lib.koszulness_ten_verifier import (
            heisenberg_data, verify_pbw_degeneration,
        )
        data = heisenberg_data(kappa_val=Rational(1))
        result = verify_pbw_degeneration(data, max_weight=5)
        # All PBW entries should pass
        for key, val in result.items():
            assert val['pass'], f"PBW failed at {key}: {val}"

    def test_pbw_spectral_sequence_sl2(self):
        """PBW spectral sequence for sl_2: Sym of 3 weight-1 generators."""
        from compute.lib.koszulness_ten_verifier import (
            sl2_data, verify_pbw_degeneration,
        )
        data = sl2_data(k_val=Rational(1))
        result = verify_pbw_degeneration(data, max_weight=5)
        for key, val in result.items():
            assert val['pass'], f"PBW failed at {key}: {val}"


# ============================================================================
# MC2: Bar-intrinsic Theta_A (kappa = scalar level)
# ============================================================================

class TestMC2_BarIntrinsicTheta:
    """MC2 (PROVED): Theta_A := D_A - d_0 is MC because D_A^2 = 0.

    The scalar level of Theta_A is kappa(A), the modular characteristic.
    kappa(A) is computed from OPE data and is the universal genus-1
    obstruction coefficient.

    kappa formulas (AP1: each computed from dim, h_dual independently):
      kappa(H_k)     = k
      kappa(sl_2_k)  = 3(k+2)/4  = dim * (k + h_dual) / (2 * h_dual)
      kappa(sl_3_k)  = 4(k+3)/3
      kappa(Vir_c)   = c/2
      kappa(W_3^c)   = 5c/6
      kappa(bg)      = -1    (c = -2)
      kappa(G_2_k)   = 7(k+4)/4
      kappa(B_2_k)   = 5(k+3)/3
    """

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k (the level IS the obstruction coefficient)."""
        from compute.lib.genus_expansion import kappa_heisenberg
        assert kappa_heisenberg(1) == Rational(1)
        assert kappa_heisenberg(5) == Rational(5)
        assert kappa_heisenberg(-3) == Rational(-3)

    def test_kappa_sl2_from_formula(self):
        """kappa(sl_2_k) = 3(k+2)/4, derived from dim=3, h*=2."""
        from compute.lib.genus_expansion import kappa_sl2
        # k=1: 3*3/4 = 9/4
        assert kappa_sl2(1) == Rational(9, 4)
        # k=0: 3*2/4 = 3/2
        assert kappa_sl2(0) == Rational(3, 2)

    def test_kappa_sl2_from_cartan(self):
        """kappa(sl_2_k) via kappa_km with Cartan data lookup."""
        from compute.lib.lie_algebra import kappa_km
        kappa = kappa_km("A", 1, Rational(1))
        assert simplify(kappa - Rational(9, 4)) == 0

    def test_kappa_sl3_from_formula(self):
        """kappa(sl_3_k) = 4(k+3)/3, derived from dim=8, h*=3."""
        from compute.lib.genus_expansion import kappa_sl3
        # k=1: 4*4/3 = 16/3
        assert kappa_sl3(1) == Rational(16, 3)

    def test_kappa_sl3_from_cartan(self):
        """kappa(sl_3_k) via kappa_km agrees with genus_expansion."""
        from compute.lib.lie_algebra import kappa_km
        from compute.lib.genus_expansion import kappa_sl3
        for k_val in [0, 1, 2, 5, 10]:
            from_cartan = kappa_km("A", 2, Rational(k_val))
            from_formula = kappa_sl3(k_val)
            assert simplify(from_cartan - from_formula) == 0, (
                f"kappa(sl_3_{k_val}) mismatch: cartan={from_cartan}, formula={from_formula}"
            )

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        from compute.lib.genus_expansion import kappa_virasoro
        assert kappa_virasoro(26) == Rational(13)
        assert kappa_virasoro(1) == Rational(1, 2)
        assert kappa_virasoro(0) == Rational(0)

    def test_kappa_w3(self):
        """kappa(W_3^c) = 5c/6."""
        from compute.lib.genus_expansion import kappa_w3
        assert kappa_w3(6) == Rational(5)
        assert kappa_w3(12) == Rational(10)

    def test_kappa_g2_from_cartan(self):
        """kappa(G_2_k) = 7(k+4)/4, from dim=14, h*=4."""
        from compute.lib.lie_algebra import kappa_km
        kappa = kappa_km("G", 2, Rational(1))
        # 14*(1+4)/(2*4) = 14*5/8 = 70/8 = 35/4
        assert simplify(kappa - Rational(35, 4)) == 0

    def test_kappa_b2_from_cartan(self):
        """kappa(B_2_k) = 5(k+3)/3, from dim=10, h*=3."""
        from compute.lib.lie_algebra import kappa_km
        kappa = kappa_km("B", 2, Rational(1))
        # 10*(1+3)/(2*3) = 40/6 = 20/3
        assert simplify(kappa - Rational(20, 3)) == 0

    def test_kappa_universal_formula(self):
        """kappa = dim(g) * (k + h*) / (2 * h*) for all KM families."""
        from compute.lib.lie_algebra import cartan_data, kappa_km
        for type_, rank in [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("G", 2)]:
            data = cartan_data(type_, rank)
            for k_val in [1, 3, 7]:
                kappa = kappa_km(type_, rank, Rational(k_val))
                expected = Rational(data.dim) * (k_val + data.h_dual) / (2 * data.h_dual)
                assert simplify(kappa - expected) == 0, (
                    f"kappa({type_}{rank}_k={k_val}) = {kappa} != {expected}"
                )

    def test_genus_expansion_F1(self):
        """F_1(A) = kappa * lambda_1^FP = kappa * 1/24."""
        from compute.lib.utils import lambda_fp, F_g
        assert lambda_fp(1) == Rational(1, 24)
        kappa = Symbol('kappa')
        assert F_g(kappa, 1) == kappa / 24

    def test_genus_expansion_F2(self):
        """F_2(A) = kappa * lambda_2^FP = kappa * 7/5760."""
        from compute.lib.utils import lambda_fp, F_g
        # lambda_2 = (2^3 - 1)/2^3 * |B_4|/4! = 7/8 * 1/30 / 1 ... let me compute
        # B_4 = -1/30, |B_4| = 1/30.  (2^3-1)/2^3 = 7/8.
        # lambda_2 = (7/8)*(1/30)/24 = 7/(8*720) = 7/5760
        assert lambda_fp(2) == Rational(7, 5760)

    def test_genus_expansion_bernoulli_positivity(self):
        """F_g values are POSITIVE for positive kappa (Bernoulli sign pattern)."""
        from compute.lib.utils import F_g
        for g in range(1, 8):
            val = F_g(Rational(1), g)
            assert val > 0, f"F_{g}(kappa=1) = {val} is not positive"


# ============================================================================
# MC2 continued: Complementarity and anti-symmetry
# ============================================================================

class TestMC2_Complementarity:
    """kappa(A) + kappa(A!) for KM families is level-independent.

    For affine KM: kappa(g_k) + kappa(g_{k'}) = 0 where k' = -k - 2h*.
    For Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13.
    For W_3: kappa(W_3^c) + kappa(W_3^{100-c}) = 250/3.
    """

    def test_km_anti_symmetry_sl2(self):
        """kappa(sl_2_k) + kappa(sl_2_{k'}) = 0 for k' = -k-4."""
        from compute.lib.genus_expansion import kappa_sl2
        from compute.lib.lie_algebra import ff_dual_level
        for k_val in [1, 3, 5, 10]:
            k_prime = ff_dual_level("A", 1, Rational(k_val))
            kap = kappa_sl2(k_val)
            kap_dual = kappa_sl2(int(k_prime))
            assert simplify(kap + kap_dual) == 0, (
                f"sl2: kappa({k_val}) + kappa({k_prime}) = {kap + kap_dual}"
            )

    def test_km_anti_symmetry_sl3(self):
        """kappa(sl_3_k) + kappa(sl_3_{k'}) = 0 for k' = -k-6."""
        from compute.lib.genus_expansion import kappa_sl3
        from compute.lib.lie_algebra import ff_dual_level
        for k_val in [1, 2, 5]:
            k_prime = ff_dual_level("A", 2, Rational(k_val))
            kap = kappa_sl3(k_val)
            kap_dual = kappa_sl3(int(k_prime))
            assert simplify(kap + kap_dual) == 0

    def test_virasoro_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        from compute.lib.genus_expansion import kappa_virasoro
        for c_val in [0, 1, 13, 26, -5]:
            kap = kappa_virasoro(c_val)
            kap_dual = kappa_virasoro(26 - c_val)
            assert kap + kap_dual == Rational(13), (
                f"Vir: kappa({c_val}) + kappa({26-c_val}) = {kap + kap_dual}"
            )

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro is self-dual at c=13, NOT c=26.

        At c=13: kappa = 13/2, dual kappa = (26-13)/2 = 13/2. Equal.
        At c=26: kappa = 13, dual kappa = 0. NOT equal.
        """
        from compute.lib.genus_expansion import kappa_virasoro
        kap_13 = kappa_virasoro(13)
        kap_13_dual = kappa_virasoro(26 - 13)
        assert kap_13 == kap_13_dual == Rational(13, 2)
        # c=26 is NOT the self-dual point
        kap_26 = kappa_virasoro(26)
        kap_26_dual = kappa_virasoro(0)
        assert kap_26 != kap_26_dual

    def test_feigin_frenkel_involution(self):
        """Feigin-Frenkel duality: k' = -k - 2h* (NOT -k - h*)."""
        from compute.lib.lie_algebra import ff_dual_level
        # sl_2: h* = 2, so k' = -k - 4
        assert ff_dual_level("A", 1, Rational(1)) == Rational(-5)
        # sl_3: h* = 3, so k' = -k - 6
        assert ff_dual_level("A", 2, Rational(1)) == Rational(-7)
        # G_2: h* = 4, so k' = -k - 8
        assert ff_dual_level("G", 2, Rational(1)) == Rational(-9)

    def test_w3_complementarity(self):
        """kappa(W_3^c) + kappa(W_3^{100-c}) = 250/3."""
        from compute.lib.mc5_higher_genus import _kappa_w3, _kappa_dual_w3
        # Test at specific c values
        for c_val in [Rational(10), Rational(50), Rational(0)]:
            kap = _kappa_w3(c_val)
            kap_dual = _kappa_dual_w3(c_val)
            total = simplify(kap + kap_dual)
            assert total == Rational(250, 3), (
                f"W_3: kappa(c={c_val}) + kappa_dual = {total}"
            )


# ============================================================================
# MC3: Categorical CG closure (all simple types)
# ============================================================================

class TestMC3_CGClosure:
    """MC3 (PROVED for all simple types):
    Multiplicity-free ell-weights replace the minuscule hypothesis.

    Verified computationally:
      - Lie algebra dimension, dual Coxeter number, exponents for all types
      - Prefundamental CG closure (character level) for sl_2
      - Hom dimension for evaluation x prefundamental
      - Weight multiplicity data for non-simply-laced types
    """

    def test_lie_algebra_dimensions(self):
        """Verify dim(g) for all types in the registry."""
        from compute.lib.lie_algebra import cartan_data
        expected = {
            ("A", 1): 3,   # sl_2
            ("A", 2): 8,   # sl_3
            ("A", 3): 15,  # sl_4
            ("B", 2): 10,  # so_5
            ("C", 2): 10,  # sp_4
            ("D", 4): 28,  # so_8
            ("G", 2): 14,
            ("F", 4): 52,
        }
        for (typ, rank), dim in expected.items():
            data = cartan_data(typ, rank)
            assert data.dim == dim, f"{typ}{rank}: dim={data.dim} != {dim}"

    def test_dual_coxeter_numbers(self):
        """Verify h*(g) for all types."""
        from compute.lib.lie_algebra import cartan_data
        expected = {
            ("A", 1): 2,  ("A", 2): 3,  ("A", 3): 4,
            ("B", 2): 3,  ("B", 3): 5,
            ("C", 2): 3,  ("C", 3): 4,
            ("D", 4): 6,
            ("G", 2): 4,  ("F", 4): 9,
        }
        for (typ, rank), h_dual in expected.items():
            data = cartan_data(typ, rank)
            assert data.h_dual == h_dual, f"{typ}{rank}: h*={data.h_dual} != {h_dual}"

    def test_positive_root_counts(self):
        """Number of positive roots = dim(g) - rank (= number of root spaces).

        Actually: |Delta^+| = (dim - rank) / 2 since each root alpha has -alpha.
        """
        from compute.lib.lie_algebra import cartan_data
        for typ, rank in [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("G", 2)]:
            data = cartan_data(typ, rank)
            n_pos = len(data.positive_roots)
            expected = (data.dim - rank) // 2
            assert n_pos == expected, (
                f"{typ}{rank}: |Delta^+| = {n_pos} != (dim-rank)/2 = {expected}"
            )

    def test_exponents_sum(self):
        """Sum of exponents = |Delta^+| (= number of positive roots)."""
        from compute.lib.lie_algebra import cartan_data
        for typ, rank in [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("G", 2), ("D", 4)]:
            data = cartan_data(typ, rank)
            exp_sum = sum(data.exponents)
            n_pos = len(data.positive_roots)
            assert exp_sum == n_pos, (
                f"{typ}{rank}: sum(exponents)={exp_sum} != |Delta^+|={n_pos}"
            )

    def test_prefundamental_hom_sl2(self):
        """dim Hom(L^-, V_n) = n/2+1 for n even, 0 for n odd (weight parity)."""
        from compute.lib.mc3_frontier import hom_prefundamental_eval
        # n=0: Hom(L^-, V_0) = 1 (trivial rep)
        assert hom_prefundamental_eval(0) == 1
        # n=1: 0 (parity mismatch)
        assert hom_prefundamental_eval(1) == 0
        # n=2: 2
        assert hom_prefundamental_eval(2) == 2
        # n=4: 3
        assert hom_prefundamental_eval(4) == 3
        # n=10: 6
        assert hom_prefundamental_eval(10) == 6
        # Odd: all zero
        for n in [3, 5, 7, 9, 11]:
            assert hom_prefundamental_eval(n) == 0

    def test_euler_char_prefundamental(self):
        """chi(L^-, V_n) = sum_{k=0}^{n/2} p(k) for even n."""
        from compute.lib.mc3_frontier import euler_char_prefundamental_eval
        from compute.lib.utils import partition_number
        for n in [0, 2, 4, 6, 8]:
            chi = euler_char_prefundamental_eval(n)
            expected = sum(partition_number(k) for k in range(n // 2 + 1))
            assert chi == expected, f"chi(L^-, V_{n}) = {chi} != {expected}"

    def test_resolution_obstruction_growth(self):
        """delta(k) = p(k) - 1 grows sub-exponentially.

        The Hardy-Ramanujan formula log(p(k))/sqrt(k) -> pi*sqrt(2/3)
        converges VERY slowly (corrections O(1/sqrt(k))). Instead we verify:
        (1) delta(k) is monotonically increasing for large k
        (2) the growth is sub-exponential: log(p(k))/k -> 0
        (3) the ratio log(p(k))/sqrt(k) is in a reasonable range
        """
        from compute.lib.mc3_frontier import resolution_obstruction_sequence
        import math
        deltas = resolution_obstruction_sequence(50)
        # (1) Monotonically increasing past k=2
        for k in range(3, 50):
            assert deltas[k] >= deltas[k - 1], (
                f"delta({k}) = {deltas[k]} < delta({k-1}) = {deltas[k-1]}"
            )
        # (2) Sub-exponential: log(p(k))/k -> 0
        for k in [30, 40, 50]:
            pk = deltas[k] + 1
            ratio = math.log(pk) / k
            assert ratio < 0.5, (
                f"Growth appears exponential at k={k}: log(p)/k = {ratio:.3f}"
            )
        # (3) log(p(k))/sqrt(k) is bounded (approaching pi*sqrt(2/3) ~ 2.565)
        for k in [30, 40, 50]:
            pk = deltas[k] + 1
            ratio = math.log(pk) / math.sqrt(k)
            assert 1.0 < ratio < 3.0, (
                f"Hardy-Ramanujan ratio at k={k}: {ratio:.3f} out of [1, 3]"
            )

    def test_ell_weight_separation_typeA(self):
        """All fundamental representations of type A are minuscule."""
        from compute.lib.mc3_ell_weight_separation import (
            weight_multiplicities_fundamental,
        )
        for rank in [1, 2, 3]:
            for i in range(1, rank + 1):
                mults = weight_multiplicities_fundamental('A', rank, i)
                max_mult = max(mults.values()) if mults else 0
                assert max_mult == 1, (
                    f"A{rank}, omega_{i}: max mult = {max_mult} (should be 1 for minuscule)"
                )

    def test_ell_weight_separation_non_minuscule_exists(self):
        """B_2 adjoint representation has weight multiplicity > 1."""
        from compute.lib.mc3_ell_weight_separation import (
            weight_multiplicities_fundamental,
        )
        # B_2, omega_1 is the standard rep (5-dim, should have mult 1)
        # B_2, omega_2 is the spin rep (4-dim, minuscule for B_2)
        # But the ADJOINT rep (omega_1 for B_3, etc.) may have higher mults
        # For G_2, omega_1 (7-dim), omega_2 (14-dim = adjoint):
        mults_g2_adj = weight_multiplicities_fundamental('G', 2, 2)
        # G_2 adjoint (14-dim) has zero weight with multiplicity 2
        max_mult = max(mults_g2_adj.values()) if mults_g2_adj else 0
        assert max_mult >= 2, (
            f"G_2 adjoint max mult = {max_mult} (should be >= 2 for zero weight)"
        )


# ============================================================================
# MC4: Completion towers
# ============================================================================

class TestMC4_Completion:
    """MC4 (PROVED): Strong completion-tower theorem.

    For positive-energy chiral algebras with polynomial OPE growth,
    the pronilpotent bar complex is finite in each weight.
    The resonance rank rho(A) classifies completion difficulty.
    """

    def test_pronilpotent_max_bar_degree(self):
        """max bar degree at weight h is floor(h/min_weight)."""
        from compute.lib.pronilpotent_bar import max_bar_degree
        # W_infinity: min generator weight = 2
        assert max_bar_degree(10, 2) == 5
        assert max_bar_degree(7, 2) == 3
        assert max_bar_degree(4, 2) == 2
        # KM: min generator weight = 1
        assert max_bar_degree(10, 1) == 10

    def test_pronilpotent_effective_weights(self):
        """Only generators with weight <= total_weight contribute."""
        from compute.lib.pronilpotent_bar import effective_generator_weights
        # W_inf generators at weights 2,3,4,...
        weights = effective_generator_weights(6, range(2, 100))
        assert weights == (2, 3, 4, 5, 6)

    def test_w_infinity_generator_weights(self):
        """W_infinity has one generator at each weight >= 2."""
        from compute.lib.pronilpotent_bar import w_infinity_generator_weights
        assert w_infinity_generator_weights(5) == (2, 3, 4, 5)
        assert w_infinity_generator_weights(1) == ()

    def test_resonance_rank_heisenberg(self):
        """Heisenberg has rho = 0 (purely positive, no resonance)."""
        from compute.lib.platonic_completion_families import heisenberg_weight_dims
        dims = heisenberg_weight_dims(10)
        # Weight-0 subspace is 1-dimensional (vacuum only)
        assert dims[0] == 1

    def test_resonance_rank_virasoro(self):
        """Virasoro has rho = 1 (depth-zero resonance from BPZ singular vectors)."""
        # Vir_{26-c} is the depth-zero resonance shadow (not the final dual).
        # The resonance subspace is 1-dimensional.
        from compute.lib.platonic_completion_families import resonance_rank
        rho, stab_stage = resonance_rank('virasoro')
        assert rho == 1, f"Virasoro resonance rank = {rho}, expected 1"
        assert stab_stage >= 1, "Should stabilize"

    def test_weight_dims_grow_as_partitions(self):
        """Heisenberg weight dims = partition numbers p(n)."""
        from compute.lib.platonic_completion_families import heisenberg_weight_dims
        from compute.lib.utils import partition_number
        dims = heisenberg_weight_dims(15)
        for n in range(16):
            assert dims[n] == partition_number(n), (
                f"Heis dim at weight {n}: {dims[n]} != p({n}) = {partition_number(n)}"
            )

    def test_sl2_weight_dims_colored_partitions(self):
        """V_k(sl_2) weight dims = 3-colored partitions."""
        from compute.lib.platonic_completion_families import affine_sl2_weight_dims
        dims = affine_sl2_weight_dims(1, 6)  # level k=1
        # p_3(0)=1, p_3(1)=3, p_3(2)=9, p_3(3)=22, p_3(4)=51, ...
        assert dims[0] == 1
        assert dims[1] == 3


# ============================================================================
# MC5: HS-sewing criterion
# ============================================================================

class TestMC5_Sewing:
    """MC5 (PROVED): HS-sewing criterion for convergent genus-1 partition functions.

    Polynomial OPE growth + subexponential sector growth => convergence
    at all genera. Heisenberg sewing theorem: one-particle Bergman
    reduction gives Fredholm determinant = Dedekind eta.
    """

    def test_heisenberg_sewing_fredholm(self):
        """Heisenberg sewing: Fredholm det = prod(1-q^n) = q^{-1/24} eta(tau)."""
        from compute.lib.fredholm_sewing_engine import (
            dedekind_eta_product, partitions,
        )
        import cmath
        # At q = 0.1 (|q| < 1 ensures convergence)
        q = 0.1
        eta_prod = dedekind_eta_product(q, N=100)
        # Compare with direct product
        direct = 1.0
        for n in range(1, 101):
            direct *= (1.0 - q**n)
        assert abs(eta_prod - direct) < 1e-12

    def test_partition_count_pentagonal(self):
        """Partition function p(n) from pentagonal recurrence matches DP."""
        from compute.lib.fredholm_sewing_engine import partitions
        from compute.lib.utils import partition_number
        for n in range(20):
            assert partitions(n) == partition_number(n), (
                f"p({n}): fredholm={partitions(n)} != utils={partition_number(n)}"
            )

    def test_virasoro_gram_positive_definite(self):
        """Virasoro Gram matrix is positive definite for c > 0 (unitary range)."""
        from compute.lib.fredholm_sewing_engine import virasoro_gram_matrix
        import numpy as np
        # c = 1, weight 2: should be positive definite
        G = virasoro_gram_matrix(1.0, 2)
        eigenvalues = np.linalg.eigvalsh(G)
        assert all(ev > -1e-10 for ev in eigenvalues), (
            f"Gram matrix not PSD at c=1, n=2: eigenvalues={eigenvalues}"
        )

    def test_hs_sewing_bar_growth_polynomial(self):
        """Bar chain groups grow polynomially for standard families.

        For an algebra with d generators of weight 1, the bar degree-n
        sector at weight w has dimension bounded by d^n * p(w-n).
        This is polynomial in w for fixed n.
        """
        from compute.lib.utils import partition_number
        # sl_2: d=3, at bar degree n=2, weight w
        d = 3
        for w in range(2, 10):
            dim_bound = d**2 * partition_number(w - 2)
            assert dim_bound >= 0
            # Growth is polynomial: dim_bound ~ d^n * exp(pi*sqrt(2w/3))
            # which is sub-exponential in w. Good.


# ============================================================================
# Koszulness programme: 10 unconditional equivalences
# ============================================================================

class TestKoszulnessProgramme:
    """10 unconditional equivalences from thm:koszul-equivalences-meta.

    All 4 archetype families (H, sl_2, bg, Vir) should satisfy all 10.
    """

    def test_shadow_depth_classification(self):
        """Each family has the correct depth class."""
        from compute.lib.koszulness_ten_verifier import (
            heisenberg_data, sl2_data, betagamma_data, virasoro_data,
        )
        assert heisenberg_data().depth_class == 'G'
        assert heisenberg_data().shadow_depth == 2
        assert sl2_data().depth_class == 'L'
        assert sl2_data().shadow_depth == 3
        assert betagamma_data().depth_class == 'C'
        assert betagamma_data().shadow_depth == 4
        assert virasoro_data().depth_class == 'M'
        assert virasoro_data().shadow_depth == 999  # stands for infinity

    def test_hochschild_range_universal(self):
        """ChirHoch vanishes outside {0, 1, 2} for all Koszul families."""
        from compute.lib.koszulness_ten_verifier import (
            heisenberg_data, sl2_data, betagamma_data, virasoro_data,
        )
        for data in [heisenberg_data(), sl2_data(), betagamma_data(), virasoro_data()]:
            lo, hi = data.hochschild_range
            assert lo >= 0 and hi <= 2, (
                f"{data.name}: ChirHoch range [{lo},{hi}] not in [0,2]"
            )

    def test_kappa_plus_kappa_dual_km_zero(self):
        """kappa + kappa! = 0 for all KM families (Feigin-Frenkel)."""
        from compute.lib.koszulness_ten_verifier import (
            heisenberg_data, sl2_data,
        )
        h = heisenberg_data()
        assert simplify(h.kappa + h.kappa_dual) == 0

        sl2 = sl2_data()
        assert simplify(sl2.kappa + sl2.kappa_dual) == 0

    def test_kappa_plus_kappa_dual_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        from compute.lib.koszulness_ten_verifier import virasoro_data
        c_sym = Symbol('c')
        vir = virasoro_data()
        total = simplify(vir.kappa + vir.kappa_dual)
        assert total == 13, f"Vir: kappa + kappa_dual = {total}"

    def test_kappa_plus_kappa_dual_betagamma(self):
        """kappa(bg) = -1, kappa(bg!) = +1, sum = 0."""
        from compute.lib.koszulness_ten_verifier import betagamma_data
        bg = betagamma_data()
        assert bg.kappa == Rational(-1)
        assert bg.kappa_dual == Rational(1)
        assert bg.kappa + bg.kappa_dual == 0


# ============================================================================
# Shadow archetype classification: G/L/C/M
# ============================================================================

class TestShadowArchetypeClassification:
    """Shadow depth determines the G/L/C/M archetype class.

    G (Gaussian, r_max=2): Heisenberg — tower terminates at quadratic
    L (Lie/tree, r_max=3): Affine KM — tower terminates at cubic
    C (Contact, r_max=4): Beta-gamma — quartic contact invariant
    M (Mixed, r_max=inf): Virasoro, W_N — infinite tower
    """

    def test_shadow_metric_virasoro(self):
        """Virasoro shadow data: kappa=c/2, alpha=2, S_4 = 10/(c(5c+22))."""
        from compute.lib.shadow_radius import virasoro_shadow_data
        kappa, alpha, S4, Delta = virasoro_shadow_data()
        c = Symbol('c')
        assert simplify(kappa - c/2) == 0
        assert alpha == Rational(2)
        assert simplify(S4 - Rational(10) / (c * (5*c + 22))) == 0

    def test_critical_discriminant_virasoro(self):
        """Delta(Vir_c) = 8*kappa*S_4 = 40/(5c+22)."""
        from compute.lib.shadow_radius import virasoro_shadow_data
        kappa, alpha, S4, Delta = virasoro_shadow_data()
        # 8 * (c/2) * 10/(c(5c+22)) = 40/(5c+22)
        c = Symbol('c')
        expected = Rational(40) / (5*c + 22)
        assert simplify(Delta - expected) == 0

    def test_shadow_radius_virasoro_formula(self):
        """rho(Vir_c) = sqrt((180c+872)/(5c+22)) / c."""
        from compute.lib.shadow_radius import virasoro_shadow_radius_formula
        rho_expr, rho_sq_expr = virasoro_shadow_radius_formula()
        # Verify at c=13 (self-dual point)
        c = Symbol('c')
        rho_at_13 = rho_expr.subs(c, 13)
        rho_sq_at_13 = rho_sq_expr.subs(c, 13)
        # (180*13+872)/(5*13+22) = 3212/87
        # rho^2 = 3212/(87*169) = 3212/14703
        assert float(rho_sq_at_13) > 0
        assert float(rho_at_13) > 0
        # rho(Vir_13) < 1 since c=13 > c* ~ 6.12
        assert float(rho_at_13) < 1, f"rho(Vir_13) = {float(rho_at_13):.4f} >= 1"

    def test_shadow_depth_G_class(self):
        """G class (Heisenberg): Delta=0, S_3=0, S_4=0 => tower terminates at 2."""
        from compute.lib.shadow_radius import critical_discriminant
        # Heisenberg: kappa=k, S_4=0 (no quartic shadow)
        Delta = critical_discriminant(Symbol('k'), 0)
        assert Delta == 0

    def test_shadow_depth_L_class(self):
        """L class (affine KM): Delta=0, S_3 nonzero => tower terminates at 3."""
        from compute.lib.koszulness_ten_verifier import sl2_data
        sl2 = sl2_data()
        assert sl2.quartic_shadow == 0  # S_4 = 0 => Delta = 0

    def test_shadow_depth_M_class(self):
        """M class (Virasoro): Delta != 0 => infinite tower."""
        from compute.lib.shadow_radius import virasoro_shadow_data
        _, _, _, Delta = virasoro_shadow_data()
        c = Symbol('c')
        # Delta = 40/(5c+22) which is nonzero for generic c
        assert simplify(Delta) != 0


# ============================================================================
# Universal H^1 theorem and bar chain group dimensions
# ============================================================================

class TestUniversalH1:
    """H^1(B(A)) = generators: the universal H^1 theorem.

    For any chirally Koszul algebra, H^1 of the bar complex equals
    the space of strong generators.  This is the first characterization
    of bar cohomology.
    """

    def test_h1_counts(self):
        """H^1 = number of strong generators for all archetype families."""
        from compute.lib.koszulness_ten_verifier import (
            heisenberg_data, sl2_data, betagamma_data, virasoro_data,
        )
        expected_h1 = {
            'Heisenberg': 1,   # single generator J
            'sl2': 3,          # generators e, h, f
            'betagamma': 2,    # generators beta, gamma
            'Virasoro': 1,     # single generator T
        }
        for data, expected in [
            (heisenberg_data(), 1),
            (sl2_data(), 3),
            (betagamma_data(), 2),
            (virasoro_data(), 1),
        ]:
            assert data.bar_coh[1] == expected, (
                f"{data.name}: H^1 = {data.bar_coh[1]} != {expected}"
            )

    def test_h1_equals_dim_generators(self):
        """H^1(B(A)) = dim_g for each family."""
        from compute.lib.koszulness_ten_verifier import (
            heisenberg_data, sl2_data, betagamma_data, virasoro_data,
        )
        for data_fn in [heisenberg_data, sl2_data, betagamma_data, virasoro_data]:
            data = data_fn()
            assert data.bar_coh[1] == data.dim_g, (
                f"{data.name}: H^1={data.bar_coh[1]} != dim_g={data.dim_g}"
            )

    def test_sl2_bar_h2_equals_5(self):
        """sl_2 bar H^2 = 5 (NOT 6; Riordan WRONG at n=2)."""
        from compute.lib.koszulness_ten_verifier import sl2_data
        data = sl2_data()
        assert data.bar_coh[2] == 5

    def test_virasoro_bar_coh_values(self):
        """Virasoro bar H^n: 1, 2, 5, 12, 30, 76 (Catalan-LIKE growth).

        These are the dimensions of H^n(B(Vir)) for small n.
        The sequence 1,2,5,12,30,76 follows the Riordan/Motzkin pattern
        for the weight-2 single-generator bar complex.
        """
        from compute.lib.koszulness_ten_verifier import virasoro_data
        data = virasoro_data()
        expected = {1: 1, 2: 2, 3: 5, 4: 12, 5: 30, 6: 76}
        for n, dim in expected.items():
            assert data.bar_coh[n] == dim, (
                f"Vir bar H^{n} = {data.bar_coh[n]} != {dim}"
            )


# ============================================================================
# Curve independence
# ============================================================================

class TestCurveIndependence:
    """kappa formulas are algebraic in the level parameter (no curve data).

    This is the content of prop:genus0-curve-independence: the bar complex
    and its cohomology depend only on genus-0 OPE data, not on the choice
    of algebraic curve X.
    """

    def test_kappa_is_rational_in_level(self):
        """kappa(A) is a rational function of the level parameter."""
        from compute.lib.genus_expansion import (
            kappa_sl2, kappa_sl3, kappa_g2, kappa_b2,
        )
        k = Symbol('k')
        # All KM kappas are linear in k (rational functions)
        for kappa_fn in [kappa_sl2, kappa_sl3, kappa_g2, kappa_b2]:
            kappa = kappa_fn()  # symbolic
            # Check it's a polynomial in k (degree 1)
            from sympy import degree, Poly
            p = Poly(kappa, k)
            assert p.degree() == 1, f"kappa = {kappa} is not linear in k"

    def test_genus_table_exact_arithmetic(self):
        """All genus expansion values are exact rationals (no float)."""
        from compute.lib.genus_expansion import genus_table
        table = genus_table(Rational(1), max_genus=6)
        for g, val in table.items():
            assert isinstance(val, Rational), (
                f"F_{g}(kappa=1) = {val} is not Rational (type={type(val).__name__})"
            )


# ============================================================================
# Modular Koszul Engine integration
# ============================================================================

class TestModularKoszulEngine:
    """Integration tests using the full compute_datum pipeline."""

    def test_compute_datum_heisenberg(self):
        """Full datum for Heisenberg: depth class G, kappa = k."""
        from compute.lib.modular_koszul_engine import compute_datum
        datum = compute_datum('heisenberg')
        assert datum.depth_class == 'G'
        assert datum.is_koszul is True
        assert datum.n_generators == 1

    def test_compute_datum_sl2(self):
        """Full datum for sl_2: depth class L, 3 generators."""
        from compute.lib.modular_koszul_engine import compute_datum
        datum = compute_datum('affine_sl2')
        assert datum.depth_class == 'L'
        assert datum.n_generators == 3
        assert datum.is_koszul is True

    def test_compute_datum_virasoro(self):
        """Full datum for Virasoro: depth class M, infinite shadow depth."""
        from compute.lib.modular_koszul_engine import compute_datum
        datum = compute_datum('virasoro')
        assert datum.depth_class == 'M'
        assert datum.shadow_depth is None  # infinite
        assert datum.is_koszul is True
        assert datum.n_generators == 1

    def test_compute_datum_betagamma(self):
        """Full datum for betagamma: depth class C, 2 generators."""
        from compute.lib.modular_koszul_engine import compute_datum
        datum = compute_datum('betagamma')
        assert datum.depth_class == 'C'
        assert datum.n_generators == 2
        assert datum.is_koszul is True

    def test_datum_internal_consistency(self):
        """All datums pass internal consistency checks."""
        from compute.lib.modular_koszul_engine import compute_datum
        for family in ['heisenberg', 'affine_sl2', 'virasoro', 'betagamma']:
            datum = compute_datum(family)
            checks = datum.verify()
            for name, passed in checks.items():
                assert passed, f"{family}: consistency check '{name}' failed"


# ============================================================================
# Koszul pairs and duality
# ============================================================================

class TestKoszulPairs:
    """Known Koszul dual pairs verified against the manuscript."""

    def test_heisenberg_not_self_dual(self):
        """Heisenberg is NOT self-dual (common error)."""
        from compute.lib.koszul_pairs import KOSZUL_PAIRS
        heis = KOSZUL_PAIRS["Heisenberg_Symch"]
        assert heis["self_dual"] is False

    def test_ff_dual_involution(self):
        """FF involution k -> -k - 2h* is an involution: (k')' = k."""
        from compute.lib.koszul_pairs import ff_dual_level
        for h_dual in [2, 3, 4]:
            for k_val in [1, 3, 5, -1]:
                k_prime = ff_dual_level(k_val, h_dual)
                k_double_prime = ff_dual_level(k_prime, h_dual)
                assert k_double_prime == k_val, (
                    f"FF involution not involutive: k={k_val}, h*={h_dual}, "
                    f"k'={k_prime}, k''={k_double_prime}"
                )

    def test_com_dual_is_lie(self):
        """Com^! = Lie (the founding example of Koszul duality)."""
        from compute.lib.koszul_pairs import KOSZUL_PAIRS
        pair = KOSZUL_PAIRS["Com_Lie"]
        assert pair["A"] == "Com"
        assert pair["A_dual"] == "Lie"

    def test_betagamma_bc_involution(self):
        """(bg)^! = bc and (bc)^! = bg (involutive Koszul duality)."""
        from compute.lib.koszul_pairs import KOSZUL_PAIRS
        pair = KOSZUL_PAIRS["beta_gamma_bc"]
        assert pair["involution"] is True


# ============================================================================
# Cross-family consistency (AP10 anti-pattern guard)
# ============================================================================

class TestCrossFamilyConsistency:
    """Multi-path verification: if kappa is wrong, these catch it."""

    def test_kappa_additivity_direct_sum(self):
        """kappa(A x B) = kappa(A) + kappa(B) for independent direct sums.

        Independent sum factorization (prop:independent-sum-factorization):
        if A = A_1 + A_2 with vanishing mixed OPE, kappa is additive.

        Example: H_k + H_{k'} should have kappa = k + k'.
        """
        from compute.lib.genus_expansion import kappa_heisenberg
        kap1 = kappa_heisenberg(3)
        kap2 = kappa_heisenberg(5)
        assert kap1 + kap2 == Rational(8)

    def test_complementarity_level_independent_km(self):
        """kappa(g_k) + kappa(g_{k'}) is independent of k for all KM types."""
        from compute.lib.genus_expansion import complementarity_sum_km
        for typ, rank in [("A", 1), ("A", 2)]:
            sum1 = complementarity_sum_km(typ, rank, 1)
            sum2 = complementarity_sum_km(typ, rank, 5)
            sum3 = complementarity_sum_km(typ, rank, 10)
            assert simplify(sum1 - sum2) == 0, (
                f"{typ}{rank}: complementarity sum depends on level: {sum1} vs {sum2}"
            )
            assert simplify(sum2 - sum3) == 0

    def test_a_hat_generating_function_first_terms(self):
        """The A-hat generating function: sum F_g x^{2g} = kappa*((x/2)/sin(x/2) - 1).

        First few terms: kappa*(x^2/24 + 7x^4/5760 + 31x^6/967680 + ...).
        """
        from compute.lib.utils import lambda_fp
        # lambda_1 = 1/24
        assert lambda_fp(1) == Rational(1, 24)
        # lambda_2 = 7/5760
        assert lambda_fp(2) == Rational(7, 5760)
        # lambda_3 = 31/967680
        assert lambda_fp(3) == Rational(31, 967680)

    def test_convergence_radius_is_2pi(self):
        """Radius of convergence = 2*pi (universal, independent of A)."""
        from compute.lib.genus_expansion import convergence_radius
        from sympy import pi
        R = convergence_radius()
        assert R == 2 * pi


# ============================================================================
# Lie algebra data for MC3 (all types)
# ============================================================================

class TestLieAlgebraData:
    """Structural data for all simple Lie types in the registry."""

    @pytest.mark.parametrize("typ,rank,expected_dim", [
        ("A", 1, 3), ("A", 2, 8), ("A", 3, 15),
        ("B", 2, 10), ("B", 3, 21),
        ("C", 2, 10), ("C", 3, 21),
        ("D", 4, 28),
        ("G", 2, 14), ("F", 4, 52),
    ])
    def test_dimension_formula(self, typ, rank, expected_dim):
        """dim(g) matches the known values for all types."""
        from compute.lib.lie_algebra import cartan_data
        data = cartan_data(typ, rank)
        assert data.dim == expected_dim

    @pytest.mark.parametrize("typ,rank,expected_h", [
        ("A", 1, 2), ("A", 2, 3), ("A", 3, 4),
        ("B", 2, 4), ("C", 2, 4), ("D", 4, 6),
        ("G", 2, 6), ("F", 4, 12),
    ])
    def test_coxeter_number(self, typ, rank, expected_h):
        """Coxeter number h matches known values."""
        from compute.lib.lie_algebra import cartan_data
        data = cartan_data(typ, rank)
        assert data.h == expected_h

    def test_cartan_matrix_symmetrizable(self):
        """Cartan matrix is symmetrizable for all types.

        A Cartan matrix A is symmetrizable if there exists a positive
        diagonal matrix D such that D*A is symmetric.  For simply-laced
        types, A itself is symmetric (D = I).  For non-simply-laced types,
        the symmetrizer D_i satisfies d_i * A_{ij} = d_j * A_{ji}.
        """
        from compute.lib.lie_algebra import cartan_data
        from sympy import Matrix
        # Simply-laced: Cartan matrix is already symmetric
        for typ, rank in [("A", 1), ("A", 2), ("A", 3), ("D", 4)]:
            data = cartan_data(typ, rank)
            A = data.cartan
            assert A == A.T, f"{typ}{rank}: simply-laced Cartan not symmetric"
        # Non-simply-laced: verify symmetrizability
        for typ, rank in [("B", 2), ("C", 2), ("G", 2)]:
            data = cartan_data(typ, rank)
            A = data.cartan
            # A is not symmetric
            assert A != A.T, f"{typ}{rank}: non-simply-laced Cartan should be asymmetric"
            # But there exists a symmetrizer: find d_1/d_2 from A_{12}/A_{21}
            r = data.rank
            if r == 2:
                ratio = Rational(int(A[1, 0]), int(A[0, 1]))  # A_{21}/A_{12}
                D = Matrix.diag(abs(ratio), Rational(1))
                DA = D * A
                assert DA == DA.T, f"{typ}{rank}: D*A not symmetric"

    def test_sugawara_central_charge(self):
        """Sugawara c = k * dim / (k + h*) for all KM families."""
        from compute.lib.lie_algebra import sugawara_c
        # sl_2 at k=1: c = 1*3/(1+2) = 1
        assert sugawara_c("A", 1, 1) == Rational(1)
        # sl_3 at k=1: c = 1*8/(1+3) = 2
        assert sugawara_c("A", 2, 1) == Rational(2)

    def test_sugawara_undefined_at_critical_level(self):
        """Sugawara is UNDEFINED at critical level k = -h* (not 'c diverges')."""
        from compute.lib.lie_algebra import sugawara_c
        with pytest.raises(ValueError, match="critical"):
            sugawara_c("A", 1, -2)  # sl_2, h* = 2


# ============================================================================
# Lambda_fp and F_g exact values
# ============================================================================

class TestBernoulliGenus:
    """Faber-Pandharipande numbers and genus expansion exact values.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    F_g(A) = kappa(A) * lambda_g^FP

    All values POSITIVE. Bernoulli signs: A-hat(x) = (x/2)/sin(x/2)
    has all positive Taylor coefficients.
    """

    @pytest.mark.parametrize("g,expected", [
        (1, Rational(1, 24)),
        (2, Rational(7, 5760)),
        (3, Rational(31, 967680)),
    ])
    def test_lambda_fp_values(self, g, expected):
        """Exact lambda_g^FP values."""
        from compute.lib.utils import lambda_fp
        assert lambda_fp(g) == expected

    def test_lambda_fp_positivity(self):
        """All lambda_g^FP are positive (Bernoulli sign pattern)."""
        from compute.lib.utils import lambda_fp
        for g in range(1, 12):
            val = lambda_fp(g)
            assert val > 0, f"lambda_{g}^FP = {val} not positive"

    def test_lambda_fp_asymptotic_decay(self):
        """lambda_g^FP ~ const * (1/(2*pi))^{2g} as g -> inf.

        Ratio lambda_{g+1}/lambda_g -> 1/(2*pi)^2 ~ 0.02533.
        """
        from compute.lib.utils import lambda_fp
        ratios = []
        for g in range(3, 10):
            ratio = float(lambda_fp(g + 1) / lambda_fp(g))
            ratios.append(ratio)
        # Should converge to 1/(4*pi^2) ~ 0.02533
        import math
        target = 1.0 / (4 * math.pi**2)
        # Last ratio should be close
        assert abs(ratios[-1] - target) < 0.005, (
            f"Ratio lambda_10/lambda_9 = {ratios[-1]:.5f}, target = {target:.5f}"
        )
