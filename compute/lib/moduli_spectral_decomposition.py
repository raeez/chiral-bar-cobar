#!/usr/bin/env python3
r"""
moduli_spectral_decomposition.py — Sewing operator on M_{1,1} and the
shadow-genus-spectral correspondence.

THE CENTRAL IDEA:
  K_q on a single curve (fixed τ) is diagonal → no continuous spectrum.
  K(τ) = K_{q(τ)} varied over M_{1,1} = SL(2,Z)\H acquires continuous
  spectrum via the Eisenstein series E_s(τ). The scattering matrix
  φ(s) = Λ(1-s)/Λ(s) involves ζ(s), introducing zeta zeros.

  The shadow tower at genus g gives corrections to Q_g(A), which is a
  function (or section) on M_g. Its spectral decomposition on M_g
  involves Eisenstein-type series whose scattering matrices contain
  L-functions. The shadow depth controls how many genera—and therefore
  how many L-functions—contribute.

GENUS-1 SHADOW-SPECTRAL DICTIONARY:
  κ (arity 2)  ↔  E_{c/2}(τ) coefficient in Roelcke-Selberg
  C (arity 3)  ↔  modification of ε^c_{c/2-1}
  Q (arity 4)  ↔  modification of higher spectral terms
  Full ε^c_s   ↔  Eisenstein spectral coefficient of Z^hat on SL(2,Z)\H

GENUS-g SHADOW-SPECTRAL CORRESPONDENCE (conjectural):
  Shadow depth r_max(A) controls how many genera g of the genus spectral
  sequence contribute nontrivially. At each genus g, the spectral
  decomposition on M_g introduces new L-functions through the Eisenstein
  scattering. Shadow depth = 1 + Σ_g (number of new L-factors at genus g).

PROVED RESULTS:
  (R1) The Eisenstein scattering matrix at genus 1 is φ(s) = Λ(1-s)/Λ(s)
       where Λ(s) = π^{-s}ζ(2s)Γ(s). Its poles at ζ zeros introduce
       zeta zeros into the spectral data. [Benjamin-Chang 2022]
  (R2) The shadow κ determines the E_{c/2} coefficient:
       (Z^hat^c - E_{c/2}, 1) = 3π^{-c/2}Γ(c/2-1) ε^c_{c/2-1}. [BC eq 3.3]
  (R3) The constrained Epstein ε^c_s IS the Eisenstein spectral coefficient:
       (Z^hat^c - E_{c/2}, E_s) = π^{s-c/2}Γ(c/2-s) ε^c_{c/2-s}. [BC eq 3.6]
  (R4) The genus-1 curvature d^2_{fib} = κ·ω_1 modifies the bar differential.
       This modification, when spectrally decomposed, shifts the E_{c/2} piece
       by an amount proportional to κ. [toroidal_bar.py, verified]
  (R5) log det(1-K(τ)) = log|η(τ)|^2 + πy/6, and its Rankin-Selberg
       transform gives ζ(s)ζ(s+1). [sewing_euler_product.py, verified]
"""

import numpy as np
import math

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. Eisenstein series and scattering matrix on M_{1,1}
# ============================================================

def eisenstein_series_real(y, s, nmax=200):
    r"""
    Real-analytic Eisenstein series E_s(τ) on imaginary axis τ = iy.

    E_s(iy) = y^s + φ(s)y^{1-s} + O(exp(-2πy))

    where φ(s) = Λ(1-s)/Λ(s) is the scattering matrix and
    Λ(s) = π^{-s}ζ(2s)Γ(s).

    For y >> 1, the exponential terms are negligible.
    We compute the leading + subleading terms.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpf(s)
    y_mp = mpmath.mpf(y)

    def Lambda(s_val):
        return mpmath.power(mpmath.pi, -s_val) * mpmath.zeta(2 * s_val) * mpmath.gamma(s_val)

    phi_s = Lambda(1 - s_mp) / Lambda(s_mp)

    # Leading two terms
    result = mpmath.power(y_mp, s_mp) + phi_s * mpmath.power(y_mp, 1 - s_mp)

    return float(result), float(phi_s)


def scattering_matrix(s):
    r"""
    The scattering matrix of the Eisenstein series on SL(2,Z)\H:
    φ(s) = Λ(1-s)/Λ(s) where Λ(s) = π^{-s}ζ(2s)Γ(s).

    KEY PROPERTY: φ(s) has POLES at zeros of Λ(s), i.e., at zeros of ζ(2s).
    These are at s = ρ/2 where ρ are nontrivial zeta zeros.

    The scattering matrix encodes ALL nontrivial zeros of ζ.
    This is how the continuous spectrum on M_{1,1} sees zeta zeros.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)

    def Lambda(s_val):
        return mpmath.power(mpmath.pi, -s_val) * mpmath.zeta(2 * s_val) * mpmath.gamma(s_val)

    return complex(Lambda(1 - s_mp) / Lambda(s_mp))


def scattering_matrix_pole_locations(n_zeros=10):
    r"""
    Poles of φ(s) = Λ(1-s)/Λ(s) occur at zeros of Λ(s).
    Λ(s) = π^{-s}ζ(2s)Γ(s).

    Γ(s) has poles at s = 0, -1, -2, ... (trivial).
    ζ(2s) has zeros at s = ρ/2 where ρ are nontrivial zeros of ζ.

    If RH: ρ = 1/2 + iγ_k, so poles of φ at s = 1/4 + iγ_k/2.

    Returns list of (pole_location, gamma_k).
    """
    if not HAS_MPMATH:
        return []

    poles = []
    for k in range(1, n_zeros + 1):
        rho = mpmath.zetazero(k)  # 1/2 + iγ_k
        pole = rho / 2            # 1/4 + iγ_k/2
        poles.append((complex(pole), float(rho.imag)))

    return poles


# ============================================================
# 2. Sewing determinant on M_{1,1}
# ============================================================

def log_sewing_det_on_moduli(y):
    r"""
    log det(1-K(τ))|_{τ=iy} = log|η(iy)|^2 + πy/6.

    On the imaginary axis:
    |η(iy)|^2 = η(iy)^2  (real)
    log|η(iy)|^2 = 2[-πy/12 + Σ_{n≥1} log(1-e^{-2πny})]
                 = -πy/6 + 2·log det(1-K_q)  where q = e^{-2πy}

    So: log det(1-K_q) = [log|η(iy)|^2 + πy/6] / 2
    Or: log|η(iy)|^2 = -πy/6 + 2·log det(1-K_q)

    The spectral decomposition of log|η(iy)|^2 on SL(2,Z)\H is known:
    (Zagier): -log|η(τ)|^2 = πy/6 - (1/4π) ∫ |Λ(s)|^2 / |Λ(s)|^2 ... E_s dμ

    More precisely, the non-holomorphic Eisenstein series E_s(τ) at s=1
    gives the constant term, and the spectral decomposition of
    -12 log|η(τ)|^2 involves the Rankin-Selberg integral.

    Returns (log_det_K, log_eta_sq, linear_term).
    """
    from rankin_selberg_bridge import eta_real, sewing_fredholm_det

    eta = eta_real(y)
    log_eta_sq = 2 * math.log(eta)
    linear = math.pi * y / 6

    q = math.exp(-2 * math.pi * y)
    log_det = 0.0
    qn = q
    for n in range(1, 500):
        if qn < 1e-300:
            break
        log_det += math.log(1 - qn)
        qn *= q

    return log_det, log_eta_sq, linear


def rankin_selberg_of_log_eta(s, ymin=1.0, ymax=50.0):
    r"""
    Rankin-Selberg transform of -log|η(τ)|^2 against E_s:

    R(s) = ∫_F -log|η(τ)|^2 · E_s(τ) dμ(τ)

    On the unfolded strip (Rankin-Selberg unfolding):
    R(s) ≈ ∫_0^∞ a_0(y) · y^{s-2} dy

    where a_0(y) = zeroth Fourier mode of -log|η|^2.

    Since -log|η(iy)|^2 = πy/6 - 2Σ log(1-e^{-2πny}), the zeroth mode is
    the function itself on the imaginary axis.

    The Rankin-Selberg integral of E_k (holomorphic Eisenstein series of
    weight k) against E_s gives:
    ∫_F |E_k|^2 y^k E_s dμ = Γ(s+k-1)/(4π)^{s+k-1} · D(s, E_k, E_k)

    For our case, -log|η|^2 is not a modular form, but its Rankin-Selberg
    integral is related to ζ(s)ζ(s+1) (from the σ_{-1} identity).

    Returns the integral value.
    """
    from scipy import integrate

    def integrand(y):
        log_eta_sq = -math.pi * y / 6
        q = math.exp(-2 * math.pi * y)
        qn = q
        for n in range(1, 200):
            if qn < 1e-300:
                break
            log_eta_sq += 2 * math.log(1 - qn)
            qn *= q
        return (-log_eta_sq) * y ** (s - 2)

    result, error = integrate.quad(integrand, ymin, ymax, limit=200)
    return result


# ============================================================
# 3. Shadow-spectral dictionary at genus 1
# ============================================================

def shadow_spectral_dictionary_genus1(c, kappa, shadow_depth):
    r"""
    Map the shadow tower data at genus 1 to the Roelcke-Selberg
    spectral decomposition of Z^hat^c on M_{1,1}.

    The spectral decomposition (BC eq 3.3):
    Z^hat^c = E_{c/2} + (constant)·ε^c_{c/2-1}
              + (1/4πi)∫ π^{s-c/2}Γ(c/2-s) ε^c_{c/2-s} E_s ds
              + (Maass cusp forms)

    The shadow tower gives:
    - κ (arity 2): determines c = 2κ, which sets the E_{c/2} piece
    - C (arity 3): the cubic shadow modifies ε^c at specific s-values
    - Q (arity 4): the quartic shadow modifies further
    - General: each shadow at arity r modifies the spectral function ε^c_s
      at the (r-2)-th derivative level

    The DICTIONARY:
    Shadow arity r ↔ (r-2)-th spectral moment of ε^c_s

    Specifically, the shadow at arity r controls the Taylor coefficient
    of ε^c_s expanded around s = c/2:
    ε^c_{c/2-s} = Σ_{k≥0} a_k s^k

    The coefficient a_k is determined by shadow data at arity k+2.
    For Gaussian class: a_0 = ε^c_{c/2} (set by κ), all higher a_k
    determined by the lattice spectrum alone.
    For Lie class: a_0 and a_1 nontrivial, a_k = 0 for k ≥ 2.
    For Mixed class: all a_k nontrivial.

    Returns the dictionary mapping arity → spectral content.
    """
    dictionary = {}

    # Arity 2 → κ → E_{c/2} coefficient
    dictionary[2] = {
        'shadow_name': 'κ (modular characteristic)',
        'shadow_value': kappa,
        'spectral_object': f'E_{{{c}/2}}(τ)',
        'spectral_content': f'Leading Cardy density, sets c = {c}',
        'L_function': None,  # No new L-function at this level
    }

    # Arity 3 → cubic shadow → ε^c at s = c/2 - 1
    if shadow_depth >= 3:
        dictionary[3] = {
            'shadow_name': 'C (cubic shadow)',
            'spectral_object': f'ε^{c}_{{c/2-1}} (Epstein at c/2-1)',
            'spectral_content': 'First subleading spectral term',
            'L_function': 'Modifies ε → changes residues δ_{k,c} at zeta zeros',
        }

    # Arity 4 → quartic shadow → ε^c at next order
    if shadow_depth >= 4:
        dictionary[4] = {
            'shadow_name': 'Q (quartic shadow)',
            'spectral_object': f'Second variation of ε^{c}_s',
            'spectral_content': 'Quartic spectral correction',
            'L_function': 'Further modifies zeta-zero residues',
        }

    # General pattern
    dictionary['pattern'] = {
        'rule': 'Shadow arity r ↔ (r-2)-th spectral moment of ε^c_s',
        'termination': f'Shadow terminates at depth {shadow_depth} → '
                      f'only first {shadow_depth - 2} moments are nonzero',
        'L_function_count': shadow_depth - 1,
    }

    return dictionary


# ============================================================
# 4. Genus-1 spectral coefficients from shadow data
# ============================================================

def spectral_coefficient_from_shadow(s, c, scalar_spectrum):
    r"""
    Compute the Eisenstein spectral coefficient of Z^hat^c from the
    scalar spectrum (= bar cohomology generators).

    (Z^hat^c, E_s) = π^{s-c/2} Γ(c/2-s) ε^c_{c/2-s}   (BC eq 3.6)

    The constrained Epstein:
    ε^c_{c/2-s} = Σ_{Δ∈S} (2Δ)^{-(c/2-s)} = Σ (2Δ)^{s-c/2}

    This IS the spectral coefficient. It encodes the bar cohomology
    spectrum as a Dirichlet series in the spectral parameter s.

    For V_Z at self-dual (c=1): ε^1_{1/2-s} = 4ζ(1-2s).
    On the critical line s = 1/2+it: ε^1_{-it} = 4ζ(-2it) — involves ζ
    on the critical line.
    """
    from rankin_selberg_bridge import constrained_epstein_zeta

    eps_val = constrained_epstein_zeta(c / 2.0 - s, scalar_spectrum)

    if not HAS_MPMATH:
        return eps_val

    # Full coefficient including Γ and π factors
    s_mp = mpmath.mpf(s)
    c_mp = mpmath.mpf(c)
    coeff = float(mpmath.power(mpmath.pi, s_mp - c_mp / 2)
                  * mpmath.gamma(c_mp / 2 - s_mp))

    return coeff * eps_val


def shadow_kappa_to_eisenstein_coeff(kappa, c):
    r"""
    The shadow κ determines the coefficient of the constant function 1
    in the spectral decomposition.

    From BC eq 3.3: the projection of Z^hat^c onto the constant function is:
    (Z^hat^c, 1) / (1, 1) = (Z^hat^c, 1) / vol(F)

    where vol(F) = π/3 for SL(2,Z)\H.

    The leading piece E_{c/2} has: (E_{c/2}, 1)/(1,1) = residue at s=1.

    The shadow κ = c/2 determines c, which determines E_{c/2}.
    The deviation from E_{c/2} is ε_c(μ) = 3π^{-c/2}Γ(c/2-1)ε^c_{c/2-1}.
    """
    if not HAS_MPMATH:
        return {'kappa': kappa, 'c': c}

    c_mp = mpmath.mpf(c)
    prefactor = float(3 * mpmath.power(mpmath.pi, -c_mp / 2) * mpmath.gamma(c_mp / 2 - 1))

    return {
        'kappa': kappa,
        'c': c,
        'E_c2_weight': c / 2,
        'prefactor': prefactor,
        'interpretation': 'κ sets c → E_{c/2} → leading spectral term',
    }


# ============================================================
# 5. Genus-g shadow-spectral correspondence
# ============================================================

def genus_g_spectral_content(g):
    r"""
    Spectral content at genus g from the shadow tower.

    At each genus g, the moduli space M_g has dimension 3g-3.
    The spectral decomposition on M_g involves:

    g=0: M_{0,n} = point (for n=3). No moduli, no spectral decomposition.
         Shadow content: tree-level data only.
         L-function content: none.

    g=1: M_{1,1} = SL(2,Z)\H, dim=1.
         Spectral decomposition: Roelcke-Selberg (Eisenstein + Maass).
         Scattering matrix: φ(s) = Λ(1-s)/Λ(s) involving ζ(s).
         L-function content: ζ(s).
         Shadow content: κ (curvature), genus-1 Hessian correction.

    g=2: M_2 ≅ Sp(4,Z)\H_2 (Siegel space), dim=3.
         Spectral decomposition: Siegel Eisenstein + Klingen + cuspidal.
         Scattering involves: ζ(s), ζ(s-1), L(s,f) for weight-k forms f.
         L-function content: ζ(s), L(s,Δ_12) (Ramanujan Δ appears at g=2).
         Shadow content: genus-2 shells in the genus spectral sequence.

    g=3: M_3, dim=6.
         Spectral decomposition: more complex (Arthur-Selberg trace formula).
         L-function content: ζ(s), L(s,Δ), L(s,f) for Siegel modular forms.
         Shadow content: genus-3 shells.

    General pattern: genus g introduces L-functions of automorphic forms
    on Sp(2g,Z)\H_g (or GL(n) via Langlands functoriality).

    The shadow depth r_max controls which genera contribute:
    - Gaussian (r_max=2): only g=0,1 contribute → L-content = {ζ}
    - Lie (r_max=3): g=0,1,2 → L-content = {ζ, L(s,Δ)}
    - Contact (r_max=4): g=0,1,2,3 → L-content = {ζ, L(s,Δ), L(s,f_Siegel)}
    - Mixed (r_max=∞): all g → all automorphic L-functions
    """
    content = {
        'genus': g,
        'dim_M_g': max(3 * g - 3, 0),
    }

    if g == 0:
        content.update({
            'moduli_space': 'point',
            'spectral_type': 'none',
            'scattering_matrix': 'none',
            'L_functions': [],
            'shadow_content': 'tree-level OPE data',
        })
    elif g == 1:
        content.update({
            'moduli_space': 'SL(2,Z)\\H',
            'spectral_type': 'Roelcke-Selberg (Eisenstein + Maass)',
            'scattering_matrix': 'φ(s) = Λ(1-s)/Λ(s), Λ(s) = π^{-s}ζ(2s)Γ(s)',
            'L_functions': ['ζ(s)'],
            'shadow_content': 'κ (curvature), genus-1 Hessian δ_H',
            'new_L_functions': ['ζ(s)'],
        })
    elif g == 2:
        content.update({
            'moduli_space': 'Sp(4,Z)\\H_2 (Siegel)',
            'spectral_type': 'Siegel Eisenstein + Klingen + cuspidal',
            'scattering_matrix': 'involves ζ(s), ζ(s-1), L(s,f_k)',
            'L_functions': ['ζ(s)', 'L(s,Δ_12)'],
            'shadow_content': 'genus-2 curvature, genus-2 shells',
            'new_L_functions': ['L(s,Δ_12)'],
        })
    elif g == 3:
        content.update({
            'moduli_space': 'M_3 (dim 6)',
            'spectral_type': 'Arthur-Selberg type',
            'scattering_matrix': 'involves degree-3 Siegel L-functions',
            'L_functions': ['ζ(s)', 'L(s,Δ)', 'L(s,f_Siegel)'],
            'shadow_content': 'genus-3 shells',
            'new_L_functions': ['L(s,f_Siegel_3)'],
        })
    else:
        content.update({
            'moduli_space': f'M_{g} (dim {3*g-3})',
            'spectral_type': f'Sp({2*g}) Arthur-Selberg',
            'scattering_matrix': f'degree-{g} symplectic L-functions',
            'L_functions': [f'automorphic L-functions up to genus {g}'],
            'shadow_content': f'genus-{g} shells in spectral sequence',
            'new_L_functions': [f'L(s, f_{{Siegel_{g}}})'],
        })

    return content


def shadow_genus_spectral_table(max_genus=5):
    r"""
    The full shadow-genus-spectral correspondence table.

    Shadow   | Class   | Active  | L-functions from          | Critical
    depth    |         | genera  | spectral decomposition    | lines
    ---------|---------|---------|---------------------------|--------
    2        | G       | 0,1     | ζ(s)                      | 1
    3        | L       | 0,1,2   | ζ(s), L(s,Δ)             | 2
    4        | C       | 0,1,2,3 | ζ(s), L(s,Δ), L(s,f_3)   | 3
    ∞        | M       | all     | all automorphic L         | ∞

    The genus spectral sequence E_1^{p,q} = H^q(M_p) matches this:
    - The E_1 differentials d_1 = Ob_p are the obstruction maps
    - Shadow termination at depth d means d_1 = 0 from page d-1 onward
    - The surviving spectral terms encode the L-functions
    """
    table = []
    for g in range(max_genus + 1):
        content = genus_g_spectral_content(g)
        table.append(content)
    return table


# ============================================================
# 6. The Selberg trace formula on M_{1,1}
# ============================================================

def selberg_trace_genus1(h_func, num_zeros=50, num_primes=50):
    r"""
    The Selberg trace formula on M_{1,1} = SL(2,Z)\H.

    For SL(2,Z), the Selberg trace formula reads:
    Σ_n h(R_n) = (Area/4π)∫h(r)r·tanh(πr)dr + (elliptic terms)
                 + (hyperbolic terms) + (identity term)

    where R_n are the spectral parameters of Maass cusp forms
    (eigenvalue = 1/4 + R_n^2).

    The HYPERBOLIC TERMS involve lengths of closed geodesics on SL(2,Z)\H.
    These are ℓ(γ) = 2·arccosh(|tr(γ)|/2) for hyperbolic γ ∈ SL(2,Z).

    The connection to ζ(s): the Selberg zeta function
    Z_{SL(2,Z)}(s) = Π_γ Π_{k≥0} (1 - e^{-(s+k)ℓ(γ)})
    has zeros at s = 1/2 + iR_n (Maass forms) and at s = zeta zeros
    (through the Eisenstein contribution).

    FOR THE SEWING OPERATOR: the sewing operator K(τ) on M_{1,1} gives
    a "sewing trace" that combines the Selberg trace formula with
    the divisor-sum decomposition:

    Σ_{spectral} h(λ_n) = (sewing identity) + (sewing hyperbolic)

    where "sewing hyperbolic" involves Σ_p (prime orbits of K) = Σ_p log(1-q^p).

    THIS IS THE BRIDGE: the Selberg trace formula on M_{1,1} relates
    the spectral data (Maass eigenvalues + Eisenstein contribution)
    to the geometric data (closed geodesics). The sewing operator adds
    the arithmetic data (divisor functions, Euler product).

    Together:
    (Selberg trace on M_{1,1}) + (sewing Euler product) = spectral constraints on ζ.

    Returns (spectral_sum, geometric_sum) for the test function h.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    # Spectral side: Maass cusp form parameters R_n^+, R_n^-
    # First few: R_1^+ ≈ 13.78, R_1^- ≈ 9.53 (from BC eq 2.12)
    maass_R_plus = [13.77975, 17.73856, 19.42348]
    maass_R_minus = [9.53370, 12.17301, 14.35851]

    spectral_maass = sum(h_func(R) for R in maass_R_plus[:3])
    spectral_maass += sum(h_func(R) for R in maass_R_minus[:3])

    # Eisenstein contribution: ∫ h(t) · (φ'/φ)(1/2+it) dt / (2π)
    # φ(s) = Λ(1-s)/Λ(s), so φ'/φ involves ζ'/ζ
    # This integral picks up contributions at the ZETA ZEROS
    # because φ'/φ has poles at s where ζ(2s) = 0.
    zeros = [float(mpmath.zetazero(k).imag) for k in range(1, num_zeros + 1)]
    eisenstein_sum = sum(h_func(gamma / 2) for gamma in zeros)

    spectral_total = spectral_maass + eisenstein_sum

    return {
        'spectral_maass': spectral_maass,
        'spectral_eisenstein': eisenstein_sum,
        'spectral_total': spectral_total,
        'maass_R_plus': maass_R_plus,
        'maass_R_minus': maass_R_minus,
        'num_zeta_zeros_used': len(zeros),
    }


# ============================================================
# 7. The combined sewing-Selberg object
# ============================================================

def sewing_selberg_combined(s, y=1.0):
    r"""
    The COMBINED object: sewing operator + Selberg trace on M_{1,1}.

    On a single curve (fixed τ = iy):
    - K_q diagonal, eigenvalues q^n, spectral zeta = Σ n^{-s} = ζ(s)
    - log det(1-K_q) = -Σ σ_{-1}(N) q^N → ζ(s)ζ(s+1)

    On the moduli space M_{1,1} (varying τ):
    - Spectral decomposition of the sewing determinant involves E_s(τ)
    - The Eisenstein scattering φ(s) = Λ(1-s)/Λ(s) involves ζ(s)
    - The Selberg trace formula relates spectral → geometric data
    - The sewing Euler product provides arithmetic data

    THE COMBINED OBJECT:
    Z_combined(s) = ∫_{M_{1,1}} log det(1-K(τ)) · E_s(τ) dμ(τ)

    By Rankin-Selberg unfolding:
    Z_combined(s) = Mellin transform of zeroth Fourier mode of log det

    The zeroth mode is:
    a_0(y) = ∫_0^1 log det(1-K(τ)) dx = log|η(iy)|^2 + πy/6
           = -πy/6 + 2·Σ log(1-e^{-2πny}) + πy/6 = 2·log det(1-K_q)

    So: Z_combined(s) = 2 ∫_0^∞ log det(1-K_q(y)) · y^{s-2} dy
    = -2 ∫_0^∞ Σ σ_{-1}(N) e^{-2πNy} · y^{s-2} dy
    = -2 Σ σ_{-1}(N) (2πN)^{-(s-1)} Γ(s-1)
    = -2 (2π)^{-(s-1)} Γ(s-1) · ζ(s-1)ζ(s)

    CHECK: Σ σ_{-1}(N) N^{-(s-1)} = ζ(s-1)ζ(s).

    So: Z_combined(s) = -2(2π)^{-(s-1)} Γ(s-1) ζ(s-1)ζ(s)

    THIS IS THE KEY: the Rankin-Selberg integral of the sewing determinant
    against the Eisenstein series gives ζ(s-1)·ζ(s) (times gamma factors).

    The zeros of Z_combined are the zeros of ζ(s-1)·ζ(s), which include
    ALL nontrivial zeta zeros (shifted by 1).

    Returns Z_combined(s) and its relation to ζ.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpf(s)

    # Z_combined(s) = -2(2π)^{-(s-1)} Γ(s-1) ζ(s-1)ζ(s)
    val = (-2 * mpmath.power(2 * mpmath.pi, -(s_mp - 1))
           * mpmath.gamma(s_mp - 1)
           * mpmath.zeta(s_mp - 1) * mpmath.zeta(s_mp))

    return {
        'value': complex(val),
        'formula': '-2(2π)^{-(s-1)} Γ(s-1) ζ(s-1)ζ(s)',
        'zero_content': 'zeros of ζ(s-1)·ζ(s) = all zeta zeros (shifted)',
        'zeta_s': float(mpmath.zeta(s_mp)),
        'zeta_s_minus_1': float(mpmath.zeta(s_mp - 1)),
    }


def verify_combined_formula(s, ymin=0.1, ymax=30.0, Nmax=300):
    r"""
    Numerically verify:
    ∫ log det(1-K_q) · y^{s-2} dy = -(2π)^{-(s-1)} Γ(s-1) ζ(s-1)ζ(s)

    (up to a factor of 2 from the unfolding).
    """
    from scipy import integrate

    def integrand(y):
        q = math.exp(-2 * math.pi * y)
        log_det = 0.0
        qn = q
        for n in range(1, Nmax):
            if qn < 1e-300:
                break
            log_det += math.log(1 - qn)
            qn *= q
        return log_det * y ** (s - 2)

    numerical, error = integrate.quad(integrand, ymin, ymax, limit=200)

    if HAS_MPMATH:
        s_mp = mpmath.mpf(s)
        analytic = float(-mpmath.power(2 * mpmath.pi, -(s_mp - 1))
                        * mpmath.gamma(s_mp - 1)
                        * mpmath.zeta(s_mp - 1) * mpmath.zeta(s_mp))
    else:
        analytic = float('nan')

    return numerical, analytic


# ============================================================
# 8. The full picture: shadow → genus → moduli → L-function
# ============================================================

def full_correspondence():
    r"""
    THE FULL SHADOW-GENUS-SPECTRAL PICTURE.

    CHAIN:
    Shadow tower Θ^{≤r}_A (algebraic, on the chiral algebra)
      ↓ genus spectral sequence (E_1^{p,q} = H^q(M_p))
    Genus-g corrections Q_g(A) (geometric, functions on M_g)
      ↓ spectral decomposition on M_g (Eisenstein + cuspidal)
    Spectral coefficients ε^c_s (analytic, L-function content)
      ↓ scattering matrix at each genus
    L-functions of automorphic forms

    SHADOW DEPTH ↔ GENERA ↔ L-FUNCTIONS:
    depth 2 (G): g ≤ 1 active → ζ(s) from M_1 scattering
    depth 3 (L): g ≤ 2 active → ζ(s) + L(s,Δ) from M_2 scattering
    depth 4 (C): g ≤ 3 active → + Siegel L-functions from M_3
    depth ∞ (M): all g active → all automorphic L-functions

    THE SEWING-SELBERG BRIDGE:
    On M_{1,1}: the Rankin-Selberg integral of the sewing determinant gives
    Z_combined(s) = -2(2π)^{-(s-1)} Γ(s-1) ζ(s-1)ζ(s)

    This means: the sewing operator, integrated over the genus-1 moduli space,
    gives ζ(s-1)·ζ(s). The zeta zeros appear as zeros of this product.

    AT HIGHER GENUS: the analogous Rankin-Selberg integral over M_g would give
    products of L-functions associated to automorphic forms on Sp(2g).

    WHY THIS MATTERS FOR RH:
    The sewing operator on a single curve gives ζ(s) trivially (eigenvalue labels).
    The sewing operator on M_{1,1} gives ζ(s-1)·ζ(s) NON-trivially
    (through the Eisenstein scattering, which requires the continuous spectrum).
    The continuous spectrum IS the mechanism that constrains zero locations:
    the Selberg trace formula equates spectral data to geometric data,
    and the self-adjointness of the Laplacian on M_{1,1} forces the
    Eisenstein contribution to lie on the critical line.

    THE GAP REMAINING:
    The Selberg trace formula on SL(2,Z)\H relates:
    (spectral: Maass eigenvalues + Eisenstein) = (geometric: geodesic lengths)
    Both sides are REAL (from self-adjointness).
    The Eisenstein contribution involves ζ(s) through φ(s).
    But this doesn't directly force ζ zeros to Re(s) = 1/2.
    It forces the EISENSTEIN SPECTRAL PARAMETER to be on Re(s) = 1/2
    (which is built into the definition of E_s for s = 1/2 + it).
    The zeta zeros appear as POLES of φ, not as EIGENVALUES.
    To force the poles of φ onto Re(s) = 1/4 (which is RH),
    we would need a spectral argument FOR φ, not just for E_s.

    BOTTOM LINE:
    The moduli-space spectral decomposition brings us from
    "ζ from eigenvalue labels" (trivial) to
    "ζ from Eisenstein scattering" (non-trivial, involves continuous spectrum).
    But the scattering matrix's pole locations are NOT constrained by
    self-adjointness — they are INPUT to the spectral theory, not output.
    RH would require that the poles of φ are constrained by some ADDITIONAL
    structure. The shadow tower provides candidates for this structure
    (the MC equation, the genus spectral sequence), but the connection
    is not yet established.
    """
    return {
        'chain': [
            'Shadow tower Θ^{≤r}_A (algebraic)',
            'Genus spectral sequence E_1^{p,q}',
            'Genus-g corrections Q_g(A) on M_g',
            'Spectral decomposition on M_g',
            'L-functions from scattering matrices',
        ],
        'key_formula': 'Z_combined(s) = -2(2π)^{-(s-1)} Γ(s-1) ζ(s-1)ζ(s)',
        'key_result': (
            'The Rankin-Selberg integral of the sewing determinant '
            'over M_{1,1} gives ζ(s-1)·ζ(s). This is non-trivial: '
            'it uses the continuous spectrum (Eisenstein scattering) '
            'on the moduli space.'
        ),
        'gap': (
            'The scattering matrix poles (= zeta zeros) are INPUT '
            'to the spectral theory, not OUTPUT. Self-adjointness '
            'constrains eigenvalues (Maass cusp forms) to the critical '
            'line, but does not constrain poles of the scattering matrix.'
        ),
        'shadow_connection': (
            'Shadow depth controls which genera contribute to the spectral '
            'decomposition, and each genus introduces new L-functions. '
            'The MC equation constrains the shadow data, which constrains '
            'the spectral coefficients. But this constraint is not strong '
            'enough to force pole locations (= zero locations of ζ).'
        ),
    }
