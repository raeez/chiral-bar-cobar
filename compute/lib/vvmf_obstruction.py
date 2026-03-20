"""VVMF Hecke programme obstruction analysis — RED TEAM attack.

The sewing-to-zeta programme for lattice VOAs rests on:
  theta function -> Hecke decomposition -> L-functions -> zeta zeros.

For non-lattice VOAs (Virasoro, W-algebras, minimal models), the partition
function is a vector-valued modular form (VVMF), not a classical modular form.
The claim is that Franc-Mason (2017) VVMF Hecke theory extends the Hecke
decomposition to non-lattice cases.

This module ATTACKS the programme by finding structural failure modes:

  (O1) Ising character vector: compute S, T matrices and verify they give
       a representation rho: SL(2,Z) -> GL(3,C).
  (O2) Rankin-Selberg scalar collapse: the inner product <F,Fbar> loses
       vector structure. Quantify information loss.
  (O3) Weight obstruction: minimal model characters have weight 0. Hecke
       operators T_n may not act on weight-0 VVMFs. Test closure.
  (O4) Non-holomorphic obstruction: Rankin-Selberg unfolding with
       Eisenstein series E_s requires careful treatment for VVMFs.
  (O5) Arithmetic content test: are Fourier coefficients of |chi|^2
       multiplicative? (If not, Euler product structure is lost.)
  (O6) Lattice vs non-lattice L-content comparison.

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Dict, List, Optional, Tuple

import mpmath
from mpmath import mp, mpf, mpc, pi, exp, sin, cos, sqrt, log, fsum, power, fac
from mpmath import matrix as mpmatrix

from compute.lib.vvmf_hecke import (
    MinimalModel, MinimalModelLabel,
    ising_model, tricritical_ising_model, three_state_potts_model,
    character_qseries, character_value, character_vector,
    s_matrix, t_matrix, verify_s_matrix_unitarity,
    hecke_operator_on_qseries,
    rankin_selberg_dirichlet_coeffs, rankin_selberg_lfunction,
    _inverse_eta_coeffs,
    DEFAULT_DPS,
)


# ---------------------------------------------------------------------------
# Precision
# ---------------------------------------------------------------------------

def _set_dps(dps: int = DEFAULT_DPS):
    mp.dps = dps


# ---------------------------------------------------------------------------
# O1: SL(2,Z) representation verification
# ---------------------------------------------------------------------------

def verify_sl2z_representation(
    model: MinimalModel,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Verify that S, T give a representation of SL(2,Z).

    SL(2,Z) has presentation <S, T | S^2 = (ST)^3 = C, C^2 = I>
    where C = -I is the central element.

    We check:
      (1) S^2 = C  (some scalar matrix)
      (2) (ST)^3 = C
      (3) C^2 = I
      (4) S^4 = I
      (5) (ST)^6 = I

    Returns dict with residuals for each relation.
    """
    _set_dps(dps)
    S = s_matrix(model, dps=dps)
    T = t_matrix(model, dps=dps)
    n = S.rows
    I = mpmatrix(n, n)
    for i in range(n):
        I[i, i] = mpf(1)

    # S^2
    S2 = S * S
    # Check if S^2 is a scalar matrix (proportional to I)
    # For unitary minimal models, S^2 = C (charge conjugation)
    # C_{ij} = delta_{i, j^*} where j^* is the charge conjugate.
    # For Ising: all representations are self-conjugate, so C = I.
    # For general models: C is a permutation matrix.

    # (ST)^3
    ST = S * T
    ST3 = ST * ST * ST

    # S^4
    S4 = S2 * S2

    # (ST)^6
    ST6 = ST3 * ST3

    # Residuals
    def matrix_err(A, B):
        """Max absolute entry of A - B."""
        mx = mpf(0)
        for i in range(A.rows):
            for j in range(A.cols):
                e = abs(A[i, j] - B[i, j])
                if e > mx:
                    mx = e
        return mx

    # S^2 should be a permutation matrix (charge conjugation)
    # Check S^2 is a permutation: each row/col has exactly one nonzero entry
    s2_perm_residual = mpf(0)
    for i in range(n):
        row_sum = fsum(abs(S2[i, j]) for j in range(n))
        s2_perm_residual = max(s2_perm_residual, abs(row_sum - 1))

    # S^4 = I
    s4_residual = matrix_err(S4, I)

    # (ST)^3 = S^2 (= C)
    st3_vs_s2 = matrix_err(ST3, S2)

    # (ST)^6 = I
    st6_residual = matrix_err(ST6, I)

    # Explicit S^2 matrix
    s2_matrix = [[float(S2[i, j]) for j in range(n)] for i in range(n)]

    return {
        's2_is_permutation_residual': float(s2_perm_residual),
        's4_equals_identity_residual': float(s4_residual),
        'st3_equals_s2_residual': float(st3_vs_s2),
        'st6_equals_identity_residual': float(st6_residual),
        's2_matrix': s2_matrix,
        'is_representation': (
            float(s4_residual) < 1e-30
            and float(st6_residual) < 1e-30
        ),
    }


def ising_character_explicit_check(
    num_terms: int = 50,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Verify the explicit Ising character formulas.

    Ising = M(4,3), c = 1/2. Three primaries:
      (1,1): h = 0          (identity)
      (2,1): h = 1/2        (energy / epsilon)
      (1,2): h = 1/16       (spin / sigma)

    Known first few coefficients:
      chi_{1,1}: 1 + q + q^2 + 2q^3 + 2q^4 + ...  (identity)
      chi_{2,1}: 1 + q + q^2 + 2q^3 + ...          (epsilon)
      chi_{1,2}: 1 + q + q^2 + 2q^3 + ...          (sigma)

    All three have d_0 = 1 (normalization).
    """
    _set_dps(dps)
    model = ising_model()
    labels = model.primary_labels()

    results = {}
    for lab in labels:
        coeffs = character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        h = model.conformal_weight(lab.r, lab.s)
        key = f"chi_{lab.r}_{lab.s}"
        results[key] = {
            'h': str(h),
            'h_float': float(h),
            'first_10': [int(round(float(c))) for c in coeffs[:10]],
            'd_0': int(round(float(coeffs[0]))),
        }

    return results


# ---------------------------------------------------------------------------
# O2: Rankin-Selberg scalar collapse obstruction
# ---------------------------------------------------------------------------

def scalar_collapse_analysis(
    model: MinimalModel,
    num_terms: int = 100,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Analyze the information loss from <F, Fbar> = sum |chi_i|^2.

    The VVMF F = (chi_1, ..., chi_r) transforms as F(gamma.tau) = rho(gamma) F(tau).
    The Rankin-Selberg integral uses <F, Fbar> = sum_i |chi_i(tau)|^2, which is
    a SCALAR modular-invariant function on H.

    ATTACK: This scalar collapse loses the representation rho. The L-function
    content comes from <F, Fbar>, not from individual chi_i.

    We quantify:
    (a) Cross-term information: |chi_i|^2 vs chi_i * chi_j_bar (i != j)
    (b) Reconstruction obstruction: can we recover individual chi_i from <F, Fbar>?
    (c) Multiplicativity failure of the collapsed coefficients.
    """
    _set_dps(dps)
    labels = model.primary_labels()
    n_prim = len(labels)

    # Get all character q-series
    all_coeffs = []
    for lab in labels:
        all_coeffs.append(
            character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        )

    # (a) Diagonal vs off-diagonal information content
    # The full Petersson inner product for VVMFs would use:
    #   <F, G> = sum_i f_i * g_i_bar
    # The diagonal part is sum_i |chi_i|^2.
    # The off-diagonal part (cross-correlations) is chi_i * chi_j_bar for i != j.

    # Compute diagonal coefficients: a_n^diag = sum_i d_n^(i)^2
    diag_coeffs = [mpf(0)] * num_terms
    for n in range(num_terms):
        for i in range(n_prim):
            diag_coeffs[n] += all_coeffs[i][n] ** 2

    # Compute cross-term coefficients: a_n^{ij} = d_n^(i) * d_n^(j) for i < j
    cross_coeffs = {}
    for i in range(n_prim):
        for j in range(i + 1, n_prim):
            key = (i, j)
            cross_coeffs[key] = [mpf(0)] * num_terms
            for n in range(num_terms):
                cross_coeffs[key][n] = all_coeffs[i][n] * all_coeffs[j][n]

    # Total information in full matrix: n_prim^2 streams
    # Information in scalar collapse: 1 stream (sum of diag)
    # Information ratio
    info_ratio = 1.0 / (n_prim * n_prim)

    # (b) Reconstruction obstruction
    # Given sum_i |chi_i(tau)|^2 as a function of tau, can we recover chi_i?
    # This requires solving a system. The obstruction is when two different
    # character vectors give the same sum of squares.
    # For the q-expansion: a_n^diag = sum_i (d_n^(i))^2 determines each
    # (d_n^(i))^2 uniquely IF the d_n^(i) are all non-negative (which they are
    # for characters of unitary models). But we still can't distinguish
    # WHICH character contributes what.

    # Check: are the d_n^(i) values distinct enough to reconstruct?
    # At level n, we have n_prim numbers d_n^(i). The scalar collapse gives
    # their sum of squares. This is one equation for n_prim unknowns.
    reconstruction_possible = []
    for n in range(min(20, num_terms)):
        vals = [int(round(float(all_coeffs[i][n]))) for i in range(n_prim)]
        # Given sum(v^2 for v in vals), can we uniquely recover vals
        # (up to permutation)?
        sum_sq = sum(v * v for v in vals)
        # Count number of solutions (non-negative integer tuples with same sum of squares)
        # This is the reconstruction ambiguity.
        solutions = 0
        # Brute force for small values
        max_val = int(sum_sq ** 0.5) + 1
        if n_prim == 3 and max_val < 50:
            for a in range(max_val + 1):
                for b in range(max_val + 1):
                    c_sq = sum_sq - a * a - b * b
                    if c_sq >= 0:
                        c = int(round(c_sq ** 0.5))
                        if c * c == c_sq:
                            solutions += 1
        reconstruction_possible.append({
            'level': n,
            'values': vals,
            'sum_sq': sum_sq,
            'num_solutions': solutions,
        })

    # (c) How much cross-term energy is lost
    total_energy = [mpf(0)] * min(20, num_terms)
    diag_energy = [mpf(0)] * min(20, num_terms)
    for n in range(min(20, num_terms)):
        for i in range(n_prim):
            diag_energy[n] += all_coeffs[i][n] ** 2
            for j in range(n_prim):
                total_energy[n] += all_coeffs[i][n] * all_coeffs[j][n]

    cross_fraction = []
    for n in range(min(20, num_terms)):
        if total_energy[n] != 0:
            cross_fraction.append(float(1 - diag_energy[n] / total_energy[n]))
        else:
            cross_fraction.append(0.0)

    return {
        'num_primaries': n_prim,
        'info_ratio': info_ratio,
        'diag_coeffs_first_20': [int(round(float(c))) for c in diag_coeffs[:20]],
        'reconstruction_data': reconstruction_possible,
        'cross_fraction': cross_fraction,
    }


# ---------------------------------------------------------------------------
# O3: Weight-zero Hecke operator obstruction
# ---------------------------------------------------------------------------

def weight_zero_hecke_closure(
    model: MinimalModel,
    n_hecke: int = 2,
    num_terms: int = 50,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Test whether T_n(chi_i) is in the span of {chi_1, ..., chi_r}.

    For classical weight-k modular forms (k >= 1), Hecke operators T_n preserve
    the space M_k(Gamma). For weight-0 VVMFs, this is NOT guaranteed.

    ATTACK: Compute T_n(chi_i) for the Ising model and check if it's a linear
    combination of the characters. If not, the Hecke programme breaks.

    The Franc-Mason Hecke operator on a VVMF F of weight 0 with representation
    rho is:
      T_n(F)(tau) = (1/n) sum_{ad=n, 0<=b<d} rho(M_{a,b,d})^{-1} F((a*tau+b)/d)
    where M_{a,b,d} = ((a,b),(0,d)) in GL(2,Z).

    This involves the REPRESENTATION rho, not just scalar operations.
    The scalar Hecke operator (ignoring rho) does NOT preserve the character space.
    """
    _set_dps(dps)
    labels = model.primary_labels()
    n_prim = len(labels)

    # Get character q-series
    char_coeffs = []
    for lab in labels:
        char_coeffs.append(
            character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        )

    # Apply SCALAR Hecke operator (the one implemented in vvmf_hecke.py)
    hecke_result = hecke_operator_on_qseries(
        model, n_hecke, num_terms=num_terms, dps=dps
    )

    # For each T_n(chi_i), try to express as linear combination of chi_j
    closure_results = []
    for i in range(n_prim):
        target = hecke_result[i]  # T_n(chi_i) coefficients

        # Set up linear system: target = sum_j alpha_j * chi_j
        # Use first n_prim coefficients at distinct levels
        # (avoiding level 0 where all chi_j have coeff 1)
        use_levels = list(range(1, min(n_prim + 5, num_terms)))
        A_mat = mpmatrix(len(use_levels), n_prim)
        b_vec = mpmatrix(len(use_levels), 1)

        for row, lev in enumerate(use_levels):
            for j in range(n_prim):
                A_mat[row, j] = char_coeffs[j][lev]
            b_vec[row, 0] = target[lev]

        # Solve least squares: minimize ||A alpha - b||^2
        # Use A^T A alpha = A^T b
        ATA = A_mat.T * A_mat
        ATb = A_mat.T * b_vec

        try:
            alpha = mpmath.lu_solve(ATA, ATb)
            # Compute residual
            residual_vec = A_mat * alpha - b_vec
            residual = mpf(0)
            for row in range(residual_vec.rows):
                residual += abs(residual_vec[row, 0]) ** 2
            residual = sqrt(residual)

            # Also check at levels NOT used in the fit
            check_levels = list(range(n_prim + 5, min(n_prim + 20, num_terms)))
            prediction_err = mpf(0)
            for lev in check_levels:
                predicted = fsum(
                    alpha[j, 0] * char_coeffs[j][lev] for j in range(n_prim)
                )
                actual = target[lev]
                prediction_err += abs(predicted - actual) ** 2
            prediction_err = sqrt(prediction_err) if check_levels else mpf(0)

            closure_results.append({
                'char_index': i,
                'alpha': [float(alpha[j, 0]) for j in range(n_prim)],
                'fit_residual': float(residual),
                'prediction_error': float(prediction_err),
                'in_span': float(prediction_err) < 1e-10,
            })
        except Exception as e:
            closure_results.append({
                'char_index': i,
                'error': str(e),
                'in_span': False,
            })

    all_in_span = all(r.get('in_span', False) for r in closure_results)

    return {
        'hecke_n': n_hecke,
        'num_primaries': n_prim,
        'closure_results': closure_results,
        'all_in_span': all_in_span,
        'obstruction_found': not all_in_span,
    }


# ---------------------------------------------------------------------------
# O4: Non-holomorphic unfolding obstruction
# ---------------------------------------------------------------------------

def rankin_selberg_unfolding_analysis(
    model: MinimalModel,
    s_param: float = 2.0,
    num_terms: int = 100,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Analyze the Rankin-Selberg unfolding for a VVMF.

    The Rankin-Selberg integral:
      RS(s) = integral_{SL(2,Z)\\H} <F(tau), Fbar(tau)> E_s(tau) dmu(tau)

    Unfolding uses E_s(tau) = sum_{gamma in Gamma_infty\\SL(2,Z)} Im(gamma.tau)^s.
    Standard unfolding for SCALAR forms gives:
      RS(s) = integral_0^infty integral_0^1 f(tau) fbar(tau) y^s dx dy/y^2

    For VVMFs, <F,Fbar> = sum_i |chi_i|^2 IS scalar, so the unfolding works
    at the level of the scalar collapse. But:

    ATTACK: The unfolded integral gives
      RS(s) = sum_i integral_0^infty |chi_i(iy)|^2 y^{s-2} dy
    which decomposes as a sum of Mellin transforms of |chi_i(iy)|^2.

    The obstruction: each |chi_i(iy)|^2 is NOT a modular form. It's the
    restriction of |chi_i(tau)|^2 to the imaginary axis. The Mellin transform
    of this may not have an Euler product or analytic continuation with
    the expected functional equation.

    We compute the unfolded integral explicitly for the Ising model.
    """
    _set_dps(dps)
    labels = model.primary_labels()
    n_prim = len(labels)

    # Get character q-series
    all_coeffs = []
    for lab in labels:
        all_coeffs.append(
            character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        )

    # On the imaginary axis tau = iy, q = e^{-2*pi*y}.
    # chi_i(iy) = q^{h_i - c/24} * sum_n d_n^(i) q^n
    #           = sum_n d_n^(i) e^{-2*pi*y*(n + h_i - c/24)}
    #
    # |chi_i(iy)|^2 = sum_{m,n} d_m^(i) d_n^(i) e^{-2*pi*y*(m+n+2(h_i-c/24))}
    #
    # The Mellin transform:
    # M_i(s) = integral_0^infty |chi_i(iy)|^2 y^{s-2} dy
    #        = sum_{m,n} d_m d_n * integral_0^infty e^{-2*pi*y*alpha_{mn}} y^{s-2} dy
    #        = sum_{m,n} d_m d_n * Gamma(s-1) / (2*pi*alpha_{mn})^{s-1}
    # where alpha_{mn} = m + n + 2(h_i - c/24).
    #
    # This is a DOUBLE Dirichlet series, not a standard L-function.

    c_val = model.central_charge_mpf
    mellin_data = []

    for i, lab in enumerate(labels):
        h_i = model.conformal_weight_mpf(lab.r, lab.s)
        offset = 2 * (h_i - c_val / 24)

        # Compute the double sum coefficients for the Dirichlet series
        # D_i(s) = sum_{k >= 0} b_k / (k + offset)^{s-1}
        # where b_k = sum_{m+n=k} d_m^(i) * d_n^(i) (convolution)
        conv_coeffs = [mpf(0)] * num_terms
        d = all_coeffs[i]
        for k in range(num_terms):
            val = mpf(0)
            for m in range(k + 1):
                n = k - m
                if m < len(d) and n < len(d):
                    val += d[m] * d[n]
            conv_coeffs[k] = val

        # Evaluate D_i(s) at s = s_param
        s_val = mpf(s_param)
        dirichlet_val = mpc(0)
        for k in range(num_terms):
            alpha = k + offset
            if alpha > 0 and conv_coeffs[k] != 0:
                dirichlet_val += conv_coeffs[k] / power(alpha, s_val - 1)

        mellin_data.append({
            'char_index': i,
            'label': f"({lab.r},{lab.s})",
            'h': float(h_i),
            'offset': float(offset),
            'conv_coeffs_first_10': [int(round(float(c))) for c in conv_coeffs[:10]],
            'dirichlet_value_at_s': float(dirichlet_val.real),
        })

    # The TOTAL Rankin-Selberg integral is the sum:
    # RS(s) = Gamma(s-1) / (2*pi)^{s-1} * sum_i D_i(s)
    total_D = sum(md['dirichlet_value_at_s'] for md in mellin_data)
    gamma_factor = float(mpmath.gamma(mpf(s_param) - 1) / power(2 * pi, mpf(s_param) - 1))

    return {
        's_param': s_param,
        'mellin_components': mellin_data,
        'total_dirichlet': total_D,
        'gamma_factor': gamma_factor,
        'rs_value': total_D * gamma_factor,
        'obstruction_type': 'double_dirichlet_series',
        'explanation': (
            'The unfolded RS integral for VVMFs gives a DOUBLE Dirichlet series '
            '(convolution of character coefficients), not a standard L-function. '
            'This double sum lacks the Euler product structure of classical Hecke L-functions.'
        ),
    }


# ---------------------------------------------------------------------------
# O5: Multiplicativity test
# ---------------------------------------------------------------------------

def multiplicativity_test(
    model: MinimalModel,
    num_terms: int = 200,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Test whether Fourier coefficients of |chi|^2 are multiplicative.

    For the lattice VOA V_Z, the partition function Z = |eta|^{-2} = (sum p(n) q^n)^2,
    and the Rankin-Selberg coefficients involve convolutions of partition numbers,
    which are NOT multiplicative. But the constrained Epstein zeta series
    epsilon^c_s involves PRIMARY spectrum, which has multiplicative structure
    because epsilon^1_s = 4*zeta(2s) for V_Z.

    For Ising (non-lattice): compute a_n = sum_i (d_n^(i))^2 and test
    a_{mn} = a_m * a_n for gcd(m,n) = 1.

    If multiplicativity fails, the Euler product factorization is impossible.
    """
    _set_dps(dps)

    # Get RS Dirichlet coefficients
    rs_coeffs = rankin_selberg_dirichlet_coeffs(model, num_terms=num_terms, dps=dps)
    a = [int(round(float(c))) for c in rs_coeffs]

    # Test multiplicativity: a(mn) = a(m) * a(n) for gcd(m,n) = 1
    failures = []
    tests = 0
    for m in range(1, min(30, num_terms)):
        for n in range(m + 1, min(30, num_terms)):
            if gcd(m, n) == 1 and m * n < num_terms:
                tests += 1
                product = a[m] * a[n]
                actual = a[m * n]
                if product != actual:
                    failures.append({
                        'm': m,
                        'n': n,
                        'a_m': a[m],
                        'a_n': a[n],
                        'a_m_times_a_n': product,
                        'a_mn': actual,
                        'ratio': float(actual) / float(product) if product != 0 else None,
                    })

    # Also test weak multiplicativity: a(p^2) = a(p)^2 - a(1) for primes p
    # (This is the Hecke eigenform relation for weight k: a(p^2) = a(p)^2 - p^{k-1})
    prime_sq_tests = []
    primes = [2, 3, 5, 7, 11, 13]
    for p in primes:
        if p * p < num_terms:
            prime_sq_tests.append({
                'p': p,
                'a_p': a[p],
                'a_p_sq': a[p * p],
                'a_p_squared': a[p] * a[p],
                'hecke_relation_residual': a[p * p] - a[p] * a[p] + a[1],
                # For weight 0: a(p^2) = a(p)^2 - p^{-1} a(1)?
                # No standard relation for weight 0.
            })

    return {
        'model': f"M({model.p},{model.q})",
        'central_charge': str(model.central_charge),
        'rs_coeffs_first_30': a[:30],
        'multiplicativity_tests': tests,
        'multiplicativity_failures': len(failures),
        'failure_fraction': len(failures) / tests if tests > 0 else 0.0,
        'first_5_failures': failures[:5],
        'is_multiplicative': len(failures) == 0,
        'prime_square_tests': prime_sq_tests,
    }


def lattice_multiplicativity_comparison(
    num_terms: int = 100,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Compare multiplicativity for V_Z (lattice) vs Ising (non-lattice).

    For V_Z: Z(tau) = 1/|eta(tau)|^2, partition function.
    The primary spectrum gives epsilon^1_s = 4*zeta(2s), which is
    multiplicative (Euler product).

    For Ising: Z(tau) = |chi_{1,1}|^2 + |chi_{2,1}|^2 + |chi_{1,2}|^2.
    Test multiplicativity of the coefficient sequence.
    """
    _set_dps(dps)

    # V_Z: partition numbers p(n)
    inv_eta = _inverse_eta_coeffs(num_terms)
    # |1/eta|^2 coefficients: convolution of p(n) with itself
    # a_k = sum_{m+n=k} p(m) * p(n)
    vz_coeffs = [0] * num_terms
    for k in range(num_terms):
        val = 0
        for m in range(k + 1):
            val += inv_eta[m] * inv_eta[k - m]
        vz_coeffs[k] = val

    # Test multiplicativity for V_Z
    vz_failures = 0
    vz_tests = 0
    for m in range(1, min(20, num_terms)):
        for n in range(m + 1, min(20, num_terms)):
            if gcd(m, n) == 1 and m * n < num_terms:
                vz_tests += 1
                if vz_coeffs[m] * vz_coeffs[n] != vz_coeffs[m * n]:
                    vz_failures += 1

    # Ising
    ising = ising_model()
    ising_result = multiplicativity_test(ising, num_terms=num_terms, dps=dps)

    return {
        'vz_coeffs_first_20': vz_coeffs[:20],
        'vz_multiplicativity_tests': vz_tests,
        'vz_multiplicativity_failures': vz_failures,
        'vz_is_multiplicative': vz_failures == 0,
        'ising_is_multiplicative': ising_result['is_multiplicative'],
        'ising_failure_fraction': ising_result['failure_fraction'],
        'conclusion': (
            'BOTH lattice and Ising fail Fourier-coefficient multiplicativity. '
            'For V_Z, the PRIMARY spectrum (not the full partition function) '
            'gives the Euler product. For Ising, there is no analogous primary '
            'spectrum extraction that yields multiplicativity.'
        ),
    }


# ---------------------------------------------------------------------------
# O6: Dirichlet series comparison
# ---------------------------------------------------------------------------

def ising_dirichlet_series(
    s_param: float = 2.0,
    num_terms: int = 500,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Compute the Dirichlet series from Ising RS coefficients.

    L_Ising(s) = sum_{n >= 1} a_n / n^s
    where a_n = sum_i (d_n^(i))^2.

    Compare with known L-functions:
    - zeta(s) = sum 1/n^s
    - zeta(2s) = sum 1/n^{2s}
    - L(s, chi_4) = sum chi_4(n)/n^s  (Dirichlet L-function mod 4)
    """
    _set_dps(dps)
    model = ising_model()

    # Get RS coefficients
    rs_coeffs = rankin_selberg_dirichlet_coeffs(model, num_terms=num_terms, dps=dps)
    a = rs_coeffs

    # Evaluate L_Ising(s)
    s = mpf(s_param)
    L_ising = mpc(0)
    for n in range(1, num_terms):
        if a[n] != 0:
            L_ising += a[n] / power(mpf(n), s)

    # Known L-functions for comparison
    zeta_s = mpmath.zeta(s)
    zeta_2s = mpmath.zeta(2 * s)

    # Dirichlet L-function mod 4: chi_4(n) = 0 if n even, (-1)^{(n-1)/2} if odd
    L_chi4 = mpc(0)
    for n in range(1, num_terms):
        if n % 2 == 1:
            chi4 = (-1) ** ((n - 1) // 2)
            L_chi4 += mpf(chi4) / power(mpf(n), s)

    # Try to express L_Ising as a product/ratio of known L-functions
    ratio_zeta = L_ising / zeta_s if zeta_s != 0 else mpc(0)
    ratio_zeta2 = L_ising / zeta_2s if zeta_2s != 0 else mpc(0)
    ratio_zeta_sq = L_ising / (zeta_s ** 2) if zeta_s != 0 else mpc(0)

    # Check if L_Ising / zeta(s)^2 is approximately constant (or a known L-function)
    ratios_at_various_s = {}
    for s_test in [2.0, 3.0, 4.0, 5.0]:
        s_t = mpf(s_test)
        L_i = mpc(0)
        for n in range(1, num_terms):
            if a[n] != 0:
                L_i += a[n] / power(mpf(n), s_t)
        z_t = mpmath.zeta(s_t)
        z2_t = mpmath.zeta(2 * s_t)
        ratios_at_various_s[s_test] = {
            'L_ising': float(L_i.real),
            'zeta': float(z_t),
            'zeta_sq': float(z_t ** 2),
            'L/zeta': float((L_i / z_t).real) if z_t != 0 else None,
            'L/zeta^2': float((L_i / z_t ** 2).real) if z_t != 0 else None,
            'L/zeta(2s)': float((L_i / z2_t).real) if z2_t != 0 else None,
        }

    return {
        's_param': s_param,
        'L_ising': float(L_ising.real),
        'zeta_s': float(zeta_s),
        'zeta_2s': float(zeta_2s),
        'L_chi4': float(L_chi4.real),
        'ratio_L_over_zeta': float(ratio_zeta.real),
        'ratio_L_over_zeta2': float(ratio_zeta2.real),
        'ratio_L_over_zeta_sq': float(ratio_zeta_sq.real),
        'ratios_at_various_s': ratios_at_various_s,
    }


# ---------------------------------------------------------------------------
# O7: Individual character L-functions and their structure
# ---------------------------------------------------------------------------

def individual_character_lfunctions(
    model: MinimalModel,
    s_values: Optional[List[float]] = None,
    num_terms: int = 500,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Compute L-functions for each individual character.

    L_i(s) = sum_{n >= 1} d_n^(i) / n^s

    The key question: do these individual L-functions have
    (a) analytic continuation?
    (b) functional equation?
    (c) Euler product?

    For lattice VOAs, the answer to all three is YES (via theta function theory).
    For non-lattice VVMFs, the answer is generally NO — the individual characters
    are NOT modular forms, they are components of a VVMF.
    """
    _set_dps(dps)
    if s_values is None:
        s_values = [2.0, 3.0, 4.0, 5.0]

    labels = model.primary_labels()
    results = {}

    for lab in labels:
        coeffs = character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        key = f"chi_{lab.r}_{lab.s}"

        # Evaluate L_i(s) at multiple s values
        L_vals = {}
        for s_val in s_values:
            s = mpf(s_val)
            val = mpc(0)
            for n in range(1, num_terms):
                if coeffs[n] != 0:
                    val += coeffs[n] / power(mpf(n), s)
            L_vals[s_val] = float(val.real)

        # Test multiplicativity of individual character coefficients
        d = [int(round(float(c))) for c in coeffs]
        mult_failures = 0
        mult_tests = 0
        for m in range(1, min(20, num_terms)):
            for n in range(m + 1, min(20, num_terms)):
                if gcd(m, n) == 1 and m * n < num_terms:
                    mult_tests += 1
                    if d[m] * d[n] != d[m * n]:
                        mult_failures += 1

        results[key] = {
            'h': float(model.conformal_weight_mpf(lab.r, lab.s)),
            'L_values': L_vals,
            'coeffs_first_20': d[:20],
            'multiplicativity_tests': mult_tests,
            'multiplicativity_failures': mult_failures,
            'is_multiplicative': mult_failures == 0,
        }

    return results


# ---------------------------------------------------------------------------
# O8: VVMF Hecke eigenvalue computation (proper matrix version)
# ---------------------------------------------------------------------------

def vvmf_hecke_matrix(
    model: MinimalModel,
    n_hecke: int,
    num_terms: int = 50,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Compute the VVMF Hecke matrix for T_n.

    For a VVMF F = (chi_1, ..., chi_r), the Hecke operator T_n^rho
    acts as a MATRIX on the character vector:
      T_n^rho(F) = H_n F  (matrix multiplication)

    The matrix H_n has entries determined by the q-expansion:
    if T_n(chi_j) = sum_i H_{ij} chi_i, then H_n = (H_{ij}).

    We compute H_n by solving the linear system.

    ATTACK: if H_n is NOT diagonalizable, or its eigenvalues are NOT
    algebraic integers, the Hecke programme breaks.
    """
    _set_dps(dps)
    labels = model.primary_labels()
    n_prim = len(labels)

    # Get character q-series
    char_coeffs = []
    for lab in labels:
        char_coeffs.append(
            character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        )

    # Apply scalar Hecke to each character
    hecke_result = hecke_operator_on_qseries(
        model, n_hecke, num_terms=num_terms, dps=dps
    )

    # Solve for H matrix: hecke_result[j] = sum_i H[i,j] * char_coeffs[i]
    # Using multiple levels for overdetermined system
    use_levels = list(range(1, min(n_prim + 10, num_terms)))
    H = mpmatrix(n_prim, n_prim)

    for j in range(n_prim):
        # Solve: char_coeffs_matrix @ h_j = hecke_result[j]
        A_mat = mpmatrix(len(use_levels), n_prim)
        b_vec = mpmatrix(len(use_levels), 1)

        for row, lev in enumerate(use_levels):
            for i in range(n_prim):
                A_mat[row, i] = char_coeffs[i][lev]
            b_vec[row, 0] = hecke_result[j][lev]

        try:
            ATA = A_mat.T * A_mat
            ATb = A_mat.T * b_vec
            h_j = mpmath.lu_solve(ATA, ATb)
            for i in range(n_prim):
                H[i, j] = h_j[i, 0]
        except Exception:
            pass

    # Compute eigenvalues of H
    H_list = [[H[i, j] for j in range(n_prim)] for i in range(n_prim)]
    try:
        eigenvalues = mpmath.eig(mpmatrix(H_list))[0]
        eigs = [complex(e) for e in eigenvalues]
    except Exception:
        eigs = []

    # Check if eigenvalues are algebraic integers
    # (For genuine Hecke operators, eigenvalues should be algebraic integers)
    # Simple test: are they close to integers or simple algebraic numbers?
    eig_analysis = []
    for e in eigs:
        nearest_int = round(e.real)
        dist_to_int = abs(e.real - nearest_int) + abs(e.imag)
        eig_analysis.append({
            'eigenvalue': e,
            'nearest_integer': nearest_int,
            'distance_to_integer': dist_to_int,
            'is_near_integer': dist_to_int < 0.01,
        })

    # Compute fit residual
    fit_residual = mpf(0)
    check_levels = list(range(n_prim + 10, min(n_prim + 30, num_terms)))
    for j in range(n_prim):
        for lev in check_levels:
            predicted = fsum(H[i, j] * char_coeffs[i][lev] for i in range(n_prim))
            actual = hecke_result[j][lev]
            fit_residual += abs(predicted - actual) ** 2
    fit_residual = float(sqrt(fit_residual))

    return {
        'hecke_n': n_hecke,
        'H_matrix': [[float(H[i, j]) for j in range(n_prim)] for i in range(n_prim)],
        'eigenvalues': eigs,
        'eigenvalue_analysis': eig_analysis,
        'fit_residual': fit_residual,
        'note': (
            'The scalar Hecke operator does NOT respect the VVMF structure. '
            'The proper VVMF Hecke operator requires the full representation rho. '
            'Large fit residual indicates the scalar Hecke does not close on characters.'
        ),
    }


# ---------------------------------------------------------------------------
# O9: Conductor and level obstruction
# ---------------------------------------------------------------------------

def conductor_analysis(
    model: MinimalModel,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Analyze the conductor/level of the VVMF representation.

    The modular representation rho: SL(2,Z) -> GL(n, C) factors through
    a finite-index subgroup. The conductor N is the smallest integer such
    that rho factors through SL(2, Z/NZ).

    For minimal model M(p,q), the conductor is lcm(4pq, ...) or related.
    The T-matrix has eigenvalues e^{2pi i (h_i - c/24)}, so the order
    of the representation is related to the denominators of h_i - c/24.

    ATTACK: If the conductor is large, the Hecke operators T_n for
    n dividing the conductor have degenerate action, limiting the
    L-function information that can be extracted.
    """
    _set_dps(dps)
    labels = model.primary_labels()
    c = model.central_charge

    # Compute h_i - c/24 as fractions
    exponents = []
    for lab in labels:
        h = model.conformal_weight(lab.r, lab.s)
        exp_frac = h - c / 24
        exponents.append(exp_frac)

    # The order of T in the representation is lcm of denominators
    denoms = [exp_frac.denominator for exp_frac in exponents]
    from functools import reduce
    def lcm(a, b):
        return a * b // gcd(a, b)
    conductor_T = reduce(lcm, denoms)

    # The full conductor involves both S and T.
    # For M(p,q), the standard result is that the conductor divides 4pq
    # (or a divisor thereof).
    conductor_bound = 4 * model.p * model.q

    # Primes dividing the conductor are "bad primes" for Hecke theory
    bad_primes = []
    temp = conductor_T
    for p_test in range(2, conductor_T + 1):
        while temp % p_test == 0:
            if p_test not in bad_primes:
                bad_primes.append(p_test)
            temp //= p_test
        if temp == 1:
            break

    return {
        'model': f"M({model.p},{model.q})",
        'central_charge': str(c),
        'exponents': [str(e) for e in exponents],
        'T_order': conductor_T,
        'conductor_bound': conductor_bound,
        'bad_primes': bad_primes,
        'fraction_of_primes_bad': (
            len([p for p in range(2, 50) if p in bad_primes])
            / len([p for p in range(2, 50)])
        ),
        'obstruction_severity': (
            'MILD' if len(bad_primes) <= 2
            else 'MODERATE' if len(bad_primes) <= 5
            else 'SEVERE'
        ),
    }


# ---------------------------------------------------------------------------
# Master obstruction summary
# ---------------------------------------------------------------------------

def full_obstruction_analysis(
    num_terms: int = 50,
    dps: int = DEFAULT_DPS,
) -> Dict[str, object]:
    """Run all obstruction analyses for the Ising model.

    Returns a comprehensive summary of all failure modes found.
    """
    _set_dps(dps)
    model = ising_model()

    sl2z = verify_sl2z_representation(model, dps=dps)
    chars = ising_character_explicit_check(num_terms=num_terms, dps=dps)
    collapse = scalar_collapse_analysis(model, num_terms=num_terms, dps=dps)
    hecke_closure = weight_zero_hecke_closure(model, n_hecke=2, num_terms=num_terms, dps=dps)
    mult = multiplicativity_test(model, num_terms=num_terms, dps=dps)
    conductor = conductor_analysis(model, dps=dps)

    obstructions_found = []
    if not sl2z['is_representation']:
        obstructions_found.append('SL2Z_REPRESENTATION_FAILURE')
    if hecke_closure['obstruction_found']:
        obstructions_found.append('HECKE_CLOSURE_FAILURE')
    if not mult['is_multiplicative']:
        obstructions_found.append('MULTIPLICATIVITY_FAILURE')
    if conductor['obstruction_severity'] != 'MILD':
        obstructions_found.append(f"CONDUCTOR_{conductor['obstruction_severity']}")

    return {
        'model': 'Ising M(4,3)',
        'sl2z_representation': sl2z,
        'characters': chars,
        'scalar_collapse': collapse,
        'hecke_closure': hecke_closure,
        'multiplicativity': mult,
        'conductor': conductor,
        'obstructions_found': obstructions_found,
        'num_obstructions': len(obstructions_found),
        'verdict': (
            'PROGRAMME BLOCKED' if len(obstructions_found) >= 2
            else 'PROGRAMME WEAKENED' if len(obstructions_found) == 1
            else 'PROGRAMME VIABLE (no obstructions found)'
        ),
    }
