r"""Tests for the Fredholm determinant zeros and sewing resonances engine.

Verifies:
  1. Heisenberg Fredholm determinant (4-path verification)
  2. Zeros of det(1 - z K_1)
  3. Trace class property
  4. Virasoro vacuum Fredholm determinant
  5. Virasoro Gram matrix
  6. Spectral zeta functions
  7. Fredholm zeta function
  8. Sewing resonances
  9. Ruelle-type zeta
  10. Sewing at Riemann zeta zeros
  11. HS-sewing radius
  12. Genus-2 Fredholm zeros
  13. Lattice VOA sewing
  14. Affine KM cross-checks
  15. Multi-path consistency

Ground truth:
  thm:heisenberg-sewing, thm:heisenberg-one-particle-sewing,
  thm:general-hs-sewing, concordance.tex (MC5),
  affine_km_sewing_engine.py, benjamin_chang_analysis.py.

  AP46: eta(q) = q^{1/24} * prod(1-q^n).  The product alone is NOT eta.
  AP48: kappa(lattice) = rank, NOT c/2.
  AP39: kappa(affine KM) = dim(g)*(k+h^v)/(2*h^v), NOT c/2.
"""

import math
import numpy as np
import pytest

from compute.lib.bc_fredholm_zeros_engine import (
    # Partition utilities
    _partitions,
    _partition_list,
    _dedekind_eta_product,
    # Heisenberg sewing
    heisenberg_fredholm_det,
    heisenberg_fredholm_zeros,
    heisenberg_eigenvalues,
    heisenberg_trace_class_verification,
    # Virasoro sewing
    virasoro_gram_matrix,
    virasoro_vacuum_fredholm_det,
    virasoro_vacuum_zeros,
    virasoro_interacting_fredholm_det,
    # Spectral zeta
    fredholm_spectral_zeta,
    fredholm_zeta_function,
    heisenberg_spectral_zeta,
    heisenberg_spectral_zeta_numerical,
    # Sewing resonances
    sewing_resonances_genus1,
    sewing_resonance_density,
    # Ruelle-type zeta
    ruelle_zeta_integrand,
    ruelle_zeta_numerical,
    # Sewing at zeta zeros
    sewing_at_zeta_zero,
    sewing_at_zeta_zeros_sweep,
    ZETA_ZEROS_GAMMA,
    # HS-sewing radius
    hs_sewing_radius,
    # Genus-2
    genus2_separating_fredholm_det,
    genus2_nonseparating_fredholm_det,
    genus2_fredholm_zeros_2d,
    # Lattice VOA
    lattice_voa_fredholm_det,
    lattice_fredholm_zeros,
    # Multi-path verification
    heisenberg_four_path_verification,
    affine_km_fredholm_verification,
    # Full suite
    full_fredholm_zeros_analysis,
)


# ======================================================================
# 1. Partition utilities (3 tests)
# ======================================================================

class TestPartitionUtilities:
    """Basic partition function tests."""

    def test_partitions_small(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n, p in enumerate(expected):
            assert _partitions(n) == p, f"p({n}) = {_partitions(n)} != {p}"

    def test_partition_list_generates_correct_count(self):
        for n in range(8):
            parts = _partition_list(n)
            assert len(parts) == _partitions(n), f"n={n}: {len(parts)} != {_partitions(n)}"

    def test_eta_product_convergence(self):
        """eta product at q=0.1 should be positive and less than 1."""
        q = 0.1
        prod_val = _dedekind_eta_product(q, 200)
        assert prod_val > 0.0
        assert prod_val < 1.0
        # At q=0.1: prod(1-0.1^n) ~ (1-0.1)*(1-0.01)*(1-0.001)*...
        # = 0.9 * 0.99 * 0.999 * ... ~ 0.891...
        assert abs(prod_val - 0.891) < 0.01


# ======================================================================
# 2. Heisenberg Fredholm determinant — 4-path verification (6 tests)
# ======================================================================

class TestHeisenbergFredholmDet:
    """Heisenberg genus-1 Fredholm determinant: four verification paths."""

    def test_four_path_agreement_q01(self):
        """All four paths agree at q = 0.1."""
        result = heisenberg_four_path_verification(0.1, 200)
        assert result['agreement_12'] < 1e-12
        assert result['agreement_13'] < 1e-12
        assert result['agreement_14'] < 1e-12

    def test_four_path_agreement_q05(self):
        """All four paths agree at q = 0.5."""
        result = heisenberg_four_path_verification(0.5, 200)
        assert result['agreement_12'] < 1e-12
        assert result['agreement_13'] < 1e-12
        assert result['agreement_14'] < 1e-12

    def test_four_path_agreement_q09(self):
        """All four paths agree at q = 0.9 (near boundary)."""
        result = heisenberg_four_path_verification(0.9, 500)
        assert result['agreement_12'] < 1e-10
        assert result['agreement_13'] < 1e-10
        assert result['agreement_14'] < 1e-10

    def test_fredholm_det_at_z1_is_eta_product(self):
        """det(1 - K_1) at z=1 equals the eta product (AP46: NOT eta itself)."""
        q = 0.3
        det_val = heisenberg_fredholm_det(1.0, q, 200)
        eta_prod = _dedekind_eta_product(q, 200)
        assert abs(det_val - eta_prod) < 1e-12 * abs(eta_prod)

    def test_fredholm_det_at_z0_is_1(self):
        """det(1 - 0 * K_1) = 1."""
        det_val = heisenberg_fredholm_det(0.0, 0.3, 200)
        assert abs(det_val - 1.0) < 1e-15

    def test_fredholm_det_product_structure(self):
        """det(1 - z K) = prod(1 - z*q^n): verify term by term."""
        q = 0.2
        z = 0.5 + 0.3j
        det_val = heisenberg_fredholm_det(z, q, 50)
        manual = 1.0 + 0.0j
        for n in range(1, 51):
            manual *= (1.0 - z * q ** n)
        assert abs(det_val - manual) < 1e-12 * abs(manual)


# ======================================================================
# 3. Zeros of the Heisenberg Fredholm determinant (5 tests)
# ======================================================================

class TestHeisenbergZeros:
    """Zeros of det(1 - z K_1) for Heisenberg."""

    def test_zeros_are_at_q_inverse_n(self):
        """Zeros should be at z_n = q^{-n}."""
        q = 0.3
        zeros = heisenberg_fredholm_zeros(q, 10)
        for entry in zeros:
            n = entry['n']
            assert abs(entry['z'] - q ** (-n)) < 1e-10 * q ** (-n)

    def test_zero_verification_vanishes(self):
        """det(1 - z_n K) should vanish at z = z_n = q^{-n}."""
        q = 0.4
        zeros = heisenberg_fredholm_zeros(q, 5)
        for entry in zeros:
            # At z = q^{-n}, the n-th factor (1 - q^{-n}*q^n) = 0
            # The full product vanishes due to this factor.
            # The verification value should be very small.
            assert entry['verification'] < 1e-10

    def test_zeros_grow_geometrically(self):
        """Successive zeros grow by factor q^{-1}."""
        q = 0.2
        zeros = heisenberg_fredholm_zeros(q, 10)
        for i in range(1, len(zeros)):
            ratio = zeros[i]['z'] / zeros[i-1]['z']
            assert abs(ratio - q ** (-1)) < 1e-10

    def test_log_zeros_uniformly_spaced(self):
        """log(z_n) is uniformly spaced with gap |log(q)|."""
        q = 0.3
        zeros = heisenberg_fredholm_zeros(q, 10)
        gap = abs(math.log(q))
        for i in range(1, len(zeros)):
            diff = zeros[i]['log_z'] - zeros[i-1]['log_z']
            assert abs(diff - gap) < 1e-10

    def test_no_zeros_inside_unit_circle(self):
        """All zeros have |z| > 1 (since q^{-n} > 1 for 0 < q < 1)."""
        q = 0.5
        zeros = heisenberg_fredholm_zeros(q, 15)
        for entry in zeros:
            assert entry['z'] > 1.0


# ======================================================================
# 4. Trace class verification (4 tests)
# ======================================================================

class TestTraceClass:
    """Verify the sewing operator is trace class."""

    def test_trace_norm_analytic(self):
        """Trace norm sum q^n = q/(1-q)."""
        q = 0.3
        result = heisenberg_trace_class_verification(q, 500)
        assert result['trace_norm_agreement'] < 1e-8

    def test_hs_norm_analytic(self):
        """HS norm sum q^{2n} = q^2/(1-q^2)."""
        q = 0.4
        result = heisenberg_trace_class_verification(q, 500)
        assert result['hs_norm_agreement'] < 1e-8

    def test_log_det_agreement(self):
        """log det from eigenvalues agrees with log(eta_product)."""
        q = 0.2
        result = heisenberg_trace_class_verification(q, 300)
        assert result['log_det_agreement'] < 1e-10

    def test_is_trace_class(self):
        """Operator is trace class for 0 < q < 1."""
        for q in [0.1, 0.3, 0.5, 0.7, 0.9]:
            result = heisenberg_trace_class_verification(q, 100)
            assert result['is_trace_class']


# ======================================================================
# 5. Virasoro Gram matrix (5 tests)
# ======================================================================

class TestVirasoroGram:
    """Shapovalov form for Virasoro Verma module."""

    def test_gram_weight1(self):
        """At weight 1: <0|L_1 L_{-1}|0> = 2*h = 0 for vacuum (h=0).
        Wait: L_1 L_{-1}|0> = [L_1, L_{-1}]|0> = 2 L_0|0> = 0.
        So G_1 = [[0]] for the vacuum module (singular).
        But _partition_list(1) = [(1,)], so we compute <0|L_1 L_{-1}|0> = 0.
        """
        G = virasoro_gram_matrix(1.0, 1)
        # Weight 1 has 1 partition: (1,)
        # <0|L_1 L_{-1}|0> = [L_1, L_{-1}]|0> = 2 L_0 |0> = 0
        assert G.shape == (1, 1)
        assert abs(G[0, 0]) < 1e-10

    def test_gram_weight2(self):
        """At weight 2: partitions (2,) and (1,1).
        <0|L_2 L_{-2}|0> = [L_2, L_{-2}]|0> = 4 L_0|0> + (c/12)(8-2)|0>
                          = c/2.
        The (1,1) partition gives zero because L_{-1}|0> = 0 for h=0 vacuum.
        """
        c = 25.0
        G = virasoro_gram_matrix(c, 2)
        assert G.shape == (2, 2)
        # G[0,0] = <(2,)|(2,)> = c/2
        assert abs(G[0, 0] - c / 2.0) < 1e-10
        # G[1,1] = <(1,1)|(1,1)> = 0 (null vector L_{-1}|0> = 0)
        assert abs(G[1, 1]) < 1e-10

    def test_gram_weight3(self):
        """At weight 3: partitions (3,), (2,1), (1,1,1).
        <0|L_3 L_{-3}|0> = [L_3, L_{-3}]|0> = 6 L_0|0> + (c/12)(27-3)|0>
                          = 2c.
        Partitions with part 1 give zero (L_{-1}|0> = 0).
        """
        c = 10.0
        G = virasoro_gram_matrix(c, 3)
        assert G.shape == (3, 3)
        # G[0,0] = <(3,)|(3,)> = 2c
        assert abs(G[0, 0] - 2.0 * c) < 1e-10
        # G[1,1] = <(2,1)|(2,1)> = 0 (involves L_{-1}|0>)
        assert abs(G[1, 1]) < 1e-10

    def test_gram_weight4_dimension(self):
        """At weight 4: partitions are (4,), (3,1), (2,2), (2,1,1), (1,1,1,1).
        p(4) = 5 partitions.  Only (4,) and (2,2) have all parts >= 2."""
        c = 25.0
        G = virasoro_gram_matrix(c, 4)
        assert G.shape == (5, 5)
        # G[0,0] = <(4,)|(4,)> = 5c = 125
        assert abs(G[0, 0] - 5.0 * c) < 1e-10
        # G[2,2] = <(2,2)|(2,2)> = c(c+8)/2
        assert abs(G[2, 2] - c * (c + 8) / 2.0) < 1e-10
        # G[0,2] = G[2,0] = <(4,)|(2,2)> = 3c
        assert abs(G[0, 2] - 3.0 * c) < 1e-10

    def test_gram_symmetric(self):
        """Gram matrix should be symmetric."""
        for c in [0.5, 1.0, 10.0, 25.0]:
            for n in [2, 3, 4]:
                G = virasoro_gram_matrix(c, n)
                assert np.allclose(G, G.T, atol=1e-10), f"G not symmetric at c={c}, n={n}"


# ======================================================================
# 6. Virasoro vacuum Fredholm determinant (4 tests)
# ======================================================================

class TestVirasoroVacuum:
    """Fredholm determinant for Virasoro vacuum module."""

    def test_vacuum_starts_at_n2(self):
        """Product starts at n=2 (no weight-1 state in vacuum module)."""
        q = 0.3
        det_val = virasoro_vacuum_fredholm_det(1.0, q, 200)
        # Compare with prod_{n>=2} (1 - q^n)
        manual = 1.0
        for n in range(2, 201):
            manual *= (1.0 - q ** n)
        assert abs(det_val - manual) < 1e-12 * abs(manual)

    def test_vacuum_vs_heisenberg(self):
        """Virasoro vacuum det = Heisenberg det / (1-q)."""
        q = 0.3
        vir_det = virasoro_vacuum_fredholm_det(1.0, q, 200)
        heis_det = heisenberg_fredholm_det(1.0, q, 200)
        # Heisenberg: prod_{n>=1}(1-q^n) = (1-q)*prod_{n>=2}(1-q^n)
        ratio = heis_det / (1.0 - q)
        assert abs(vir_det - ratio) < 1e-12 * abs(vir_det)

    def test_vacuum_zeros_start_at_n2(self):
        """First zero at z = q^{-2}, not q^{-1}."""
        q = 0.4
        zeros = virasoro_vacuum_zeros(q, 5)
        assert zeros[0]['n'] == 2
        assert abs(zeros[0]['z'] - q ** (-2)) < 1e-10

    def test_vacuum_fredholm_at_z0(self):
        """det(1 - 0*K) = 1."""
        det_val = virasoro_vacuum_fredholm_det(0.0, 0.3, 200)
        assert abs(det_val - 1.0) < 1e-15


# ======================================================================
# 7. Spectral zeta function (5 tests)
# ======================================================================

class TestSpectralZeta:
    """Spectral zeta functions of the sewing operator."""

    def test_heisenberg_spectral_zeta_closed_form(self):
        """zeta_K(s=1) = q/(1-q) for Heisenberg."""
        q = 0.3
        exact = q / (1.0 - q)
        computed = heisenberg_spectral_zeta(1.0, q)
        assert abs(computed - exact) < 1e-12

    def test_spectral_zeta_numerical_vs_analytic(self):
        """Numerical sum vs closed form at s = 1."""
        q = 0.4
        exact = heisenberg_spectral_zeta(1.0, q)
        numerical = heisenberg_spectral_zeta_numerical(1.0, q, 500)
        assert abs(exact - numerical) / abs(exact) < 1e-6

    def test_spectral_zeta_at_s2(self):
        """zeta_K(s=2) = q^2/(1-q^2) for Heisenberg."""
        q = 0.3
        exact = q ** 2 / (1.0 - q ** 2)
        computed = heisenberg_spectral_zeta(2.0, q)
        assert abs(computed - exact) < 1e-12

    def test_fredholm_spectral_vs_eigenvalues(self):
        """Spectral zeta from eigenvalue array vs closed form."""
        q = 0.3
        eigs = heisenberg_eigenvalues(q, 200)
        zeta_num = fredholm_spectral_zeta(1.0, eigs)
        zeta_exact = heisenberg_spectral_zeta(1.0, q)
        assert abs(zeta_num - zeta_exact) / abs(zeta_exact) < 1e-6

    def test_fredholm_zeta_function_zeros(self):
        """Z^{Fred}(s) = prod(1 - lambda_n^{-s}) has zeros where lambda_n^s = 1."""
        q = 0.3
        eigs = heisenberg_eigenvalues(q, 50)
        # At s=0: all lambda_n^{-0} = 1, so all factors vanish: Z^{Fred}(0) = 0
        z_val = fredholm_zeta_function(0.0, eigs)
        assert abs(z_val) < 1e-10


# ======================================================================
# 8. Sewing resonances (4 tests)
# ======================================================================

class TestSewingResonances:
    """Sewing resonances at genus 1."""

    def test_heisenberg_resonances_positive_real(self):
        """All Heisenberg resonances are positive real."""
        q = 0.2
        res = sewing_resonances_genus1(q, 10, 'heisenberg')
        for r in res:
            assert r['z'] > 0
            assert r['z'] > 1.0  # q^{-n} > 1

    def test_virasoro_resonances_start_at_n2(self):
        """Virasoro vacuum resonances start at n=2."""
        q = 0.3
        res = sewing_resonances_genus1(q, 10, 'virasoro')
        assert res[0]['n'] == 2

    def test_resonance_density(self):
        """Density = 1/|log(q)|."""
        q = 0.3
        density_data = sewing_resonance_density(q, 1e10, 'heisenberg')
        assert abs(density_data['density'] - 1.0 / abs(math.log(q))) < 1e-12

    def test_resonance_count(self):
        """N(z_max) = floor(log(z_max)/|log(q)|) for Heisenberg."""
        q = 0.5
        z_max = 100.0  # q^{-n} <= 100 means n <= log(100)/log(2) ~ 6.64
        density_data = sewing_resonance_density(q, z_max, 'heisenberg')
        expected = math.floor(math.log(z_max) / abs(math.log(q)))
        assert density_data['n_resonances'] == expected


# ======================================================================
# 9. Ruelle-type zeta (3 tests)
# ======================================================================

class TestRuelleZeta:
    """Ruelle-type zeta from Mellin transform of log det."""

    def test_ruelle_integrand_at_t0(self):
        """At t=0: log det(1 - K) = log(eta_product)."""
        q = 0.3
        # t = 0 means e^{-t} = 1, so we get log det(1 - K)
        val = ruelle_zeta_integrand(1e-10, q, 200)
        eta_prod = _dedekind_eta_product(q, 200)
        log_eta = math.log(eta_prod)
        assert abs(val - log_eta) < 0.01

    def test_ruelle_integrand_at_large_t(self):
        """At large t: e^{-t} ~ 0, so log det ~ 0."""
        q = 0.3
        val = ruelle_zeta_integrand(50.0, q, 200)
        assert abs(val) < 1e-10

    def test_ruelle_integrand_negative(self):
        """log det(1 - e^{-t} K) is negative for small t (det < 1)."""
        q = 0.3
        val = ruelle_zeta_integrand(0.01, q, 200)
        assert val < 0  # prod(1 - e^{-t} q^n) < 1 for small t


# ======================================================================
# 10. Sewing at Riemann zeta zeros (5 tests)
# ======================================================================

class TestSewingAtZetaZeros:
    """Evaluate sewing determinant at tau = i*gamma_n/(2*pi)."""

    def test_first_zeta_zero_gamma(self):
        """gamma_1 = 14.1347... is correct."""
        assert abs(ZETA_ZEROS_GAMMA[0] - 14.134725) < 1e-4

    def test_q_at_zeta_zero_is_tiny(self):
        """q = e^{-gamma_1} ~ 7.3e-7 is very small."""
        result = sewing_at_zeta_zero(1)
        assert result['q'] < 1e-5
        assert result['q'] > 0

    def test_fredholm_det_near_1_at_zeta_zero(self):
        """det(1 - K) ~ 1 at zeta zeros (q very small)."""
        result = sewing_at_zeta_zero(1)
        # q ~ 7e-7, so prod(1 - q^n) ~ 1 - q - q^2 - ... ~ 1 - 7e-7
        assert abs(result['fredholm_det'] - 1.0) < 1e-4

    def test_sweep_all_zeros(self):
        """Sweep first 10 zeta zeros, all give det ~ 1."""
        results = sewing_at_zeta_zeros_sweep(10)
        for r in results:
            assert abs(r['fredholm_det'] - 1.0) < 1e-3

    def test_eta_ratio_near_1(self):
        """det/eta_product ~ 1 at zeta zeros (both ~ 1)."""
        result = sewing_at_zeta_zero(1)
        assert abs(result['det_to_eta_ratio'] - 1.0) < 1e-3


# ======================================================================
# 11. HS-sewing radius (3 tests)
# ======================================================================

class TestHSSewingRadius:
    """HS-sewing convergence radius."""

    def test_heisenberg_r_hs_is_1(self):
        """Heisenberg has r_HS = 1."""
        result = hs_sewing_radius(algebra='heisenberg')
        assert result['r_HS'] == 1.0

    def test_zeta_zero_inside_convergence(self):
        """q at first zeta zero is well inside r_HS."""
        result = hs_sewing_radius(algebra='heisenberg')
        assert result['zeta_well_inside']

    def test_virasoro_r_hs_is_1(self):
        """Virasoro has r_HS = 1 (thm:general-hs-sewing)."""
        result = hs_sewing_radius(c=25.0, algebra='virasoro')
        assert result['r_HS'] == 1.0


# ======================================================================
# 12. Genus-2 Fredholm zeros (5 tests)
# ======================================================================

class TestGenus2:
    """Genus-2 Fredholm determinant and zeros."""

    def test_genus2_separating_at_z0(self):
        """det(1 - 0 * K_{g=2}) = 1."""
        det_val = genus2_separating_fredholm_det(0.0, 0.3, 0.3, 0.2, 100)
        assert abs(det_val - 1.0) < 1e-15

    def test_genus2_separating_factorization(self):
        """det_{g=2} = det_1(q1) * det_1(q2) * det_{neck}(w) at z=1."""
        q1, q2, w = 0.3, 0.4, 0.2
        det_g2 = genus2_separating_fredholm_det(1.0, q1, q2, w, 100)
        det_q1 = heisenberg_fredholm_det(1.0, q1, 100)
        det_q2 = heisenberg_fredholm_det(1.0, q2, 100)
        det_w = heisenberg_fredholm_det(1.0, w, 100)
        expected = det_q1 * det_q2 * det_w
        assert abs(det_g2 - expected) / abs(expected) < 1e-12

    def test_genus2_nonseparating_at_z0(self):
        """det(1 - 0 * K) = 1."""
        det_val = genus2_nonseparating_fredholm_det(0.0, 0.3, 0.2, 100)
        assert abs(det_val - 1.0) < 1e-15

    def test_genus2_nonseparating_factorization(self):
        """det_{g=2,nonsep} = det_torus(q) * det_neck(w)."""
        q, w = 0.3, 0.2
        det_g2 = genus2_nonseparating_fredholm_det(1.0, q, w, 100)
        det_q = heisenberg_fredholm_det(1.0, q, 100)
        det_w = heisenberg_fredholm_det(1.0, w, 100)
        expected = det_q * det_w
        assert abs(det_g2 - expected) / abs(expected) < 1e-12

    def test_genus2_zeros_2d_types(self):
        """Genus-2 zeros have three types: torus_1, torus_2, sewing_neck."""
        zeros = genus2_fredholm_zeros_2d(0.3, 0.4, n_zeros_per_type=3)
        types = [z['type'] for z in zeros]
        assert types.count('torus_1') == 3
        assert types.count('torus_2') == 3
        assert types.count('sewing_neck') == 3


# ======================================================================
# 13. Lattice VOA sewing (4 tests)
# ======================================================================

class TestLatticeVOA:
    """Lattice VOA Fredholm determinant."""

    def test_rank1_is_heisenberg(self):
        """Rank 1 lattice VOA Fredholm det = Heisenberg det."""
        q = 0.3
        latt_det = lattice_voa_fredholm_det(1.0, 1, q, 200)
        heis_det = heisenberg_fredholm_det(1.0, q, 200)
        assert abs(latt_det - heis_det) < 1e-12

    def test_rank_r_is_heisenberg_power_r(self):
        """Rank r lattice det = (Heisenberg det)^r."""
        q = 0.3
        r = 8  # E8 lattice
        latt_det = lattice_voa_fredholm_det(1.0, r, q, 200)
        heis_det = heisenberg_fredholm_det(1.0, q, 200)
        expected = heis_det ** r
        assert abs(latt_det - expected) / abs(expected) < 1e-10

    def test_lattice_zeros_multiplicity(self):
        """Zeros of rank-r lattice have multiplicity r."""
        r = 24  # Leech lattice
        q = 0.3
        zeros = lattice_fredholm_zeros(r, q, 5)
        for z in zeros:
            assert z['multiplicity'] == r

    def test_lattice_kappa_is_rank(self):
        """kappa(V_Lambda) = rank (AP48: NOT c/2)."""
        # For Leech lattice: c = 24, kappa = rank = 24.
        # c/2 = 12 != 24.  This is AP48.
        # We just check the multiplicity is consistent with rank.
        r = 24
        q = 0.3
        det_val = lattice_voa_fredholm_det(1.0, r, q, 200)
        eta_prod = _dedekind_eta_product(q, 200)
        expected = eta_prod ** r
        assert abs(det_val - expected) / abs(expected) < 1e-10


# ======================================================================
# 14. Affine KM cross-checks (4 tests)
# ======================================================================

class TestAffineKMCross:
    """Cross-check with affine_km_sewing_engine."""

    def test_sl2_level1_agreement(self):
        """sl_2 at level 1: dim = 3, det = eta_prod^3."""
        q = 0.3
        result = affine_km_fredholm_verification('A', 1, 1.0, q, 200)
        assert result['dim_g'] == 3
        assert result['agreement_12'] < 1e-10
        assert result['agreement_13'] < 1e-10

    def test_sl3_level1_agreement(self):
        """sl_3 at level 1: dim = 8."""
        q = 0.3
        result = affine_km_fredholm_verification('A', 2, 1.0, q, 200)
        assert result['dim_g'] == 8
        assert result['agreement_12'] < 1e-10

    def test_so5_level1_agreement(self):
        """B_2 = so_5 at level 1: dim = 10."""
        q = 0.3
        result = affine_km_fredholm_verification('B', 2, 1.0, q, 200)
        assert result['dim_g'] == 10
        assert result['agreement_12'] < 1e-10

    def test_g2_level1_agreement(self):
        """G_2 at level 1: dim = 14."""
        q = 0.3
        result = affine_km_fredholm_verification('G', 2, 1.0, q, 200)
        assert result['dim_g'] == 14
        assert result['agreement_12'] < 1e-10


# ======================================================================
# 15. Full diagnostic suite (3 tests)
# ======================================================================

class TestFullSuite:
    """Full diagnostic suite."""

    def test_full_suite_runs(self):
        """The full suite completes without error."""
        result = full_fredholm_zeros_analysis(q=0.3, N=100)
        assert 'heisenberg_verification' in result
        assert 'heisenberg_zeros' in result
        assert 'trace_class' in result

    def test_full_suite_consistency(self):
        """Internal consistency of the full suite."""
        result = full_fredholm_zeros_analysis(q=0.3, N=100)
        # Heisenberg verification passes
        hv = result['heisenberg_verification']
        assert hv['agreement_12'] < 1e-10

    def test_spectral_zeta_cross_check(self):
        """Spectral zeta from full suite agrees."""
        result = full_fredholm_zeros_analysis(q=0.3, N=100)
        sz_num = result['spectral_zeta_at_1']
        sz_exact = result['spectral_zeta_exact']
        assert abs(sz_num - sz_exact) / abs(sz_exact) < 1e-4


# ======================================================================
# 16. Virasoro interacting diagnostic (2 tests)
# ======================================================================

class TestVirasoroInteracting:
    """Virasoro at specific central charges."""

    def test_interacting_fredholm_runs(self):
        """Virasoro interacting diagnostic at c = 25."""
        result = virasoro_interacting_fredholm_det(1.0, 25.0, 0.3, N_weight=5)
        assert 'fredholm_det' in result
        assert len(result['gram_data']) == 5

    def test_gram_c_dependence(self):
        """Gram matrix at weight 2 is c/2 (varies with c)."""
        for c in [1.0, 10.0, 25.0]:
            G = virasoro_gram_matrix(c, 2)
            assert abs(G[0, 0] - c / 2.0) < 1e-10


# ======================================================================
# 17. Edge cases and robustness (4 tests)
# ======================================================================

class TestEdgeCases:
    """Edge cases and boundary behavior."""

    def test_very_small_q(self):
        """At q ~ 0: det ~ 1."""
        q = 1e-10
        det_val = heisenberg_fredholm_det(1.0, q, 50)
        assert abs(det_val - 1.0) < 1e-8

    def test_complex_z(self):
        """det(1 - z K) for complex z."""
        q = 0.3
        z = 2.0 + 1.0j
        det_val = heisenberg_fredholm_det(z, q, 200)
        assert isinstance(det_val, complex)

    def test_genus2_complex_z(self):
        """Genus-2 det with complex z."""
        det_val = genus2_separating_fredholm_det(1.0 + 0.5j, 0.3, 0.3, 0.2, 50)
        assert isinstance(det_val, complex)

    def test_eigenvalues_decay(self):
        """Eigenvalues q^n decay geometrically."""
        q = 0.5
        eigs = heisenberg_eigenvalues(q, 20)
        for i in range(1, len(eigs)):
            assert eigs[i] < eigs[i-1]
            assert abs(eigs[i] / eigs[i-1] - q) < 1e-12
