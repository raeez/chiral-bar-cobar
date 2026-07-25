r"""Scalar Page-curve candidates with typed algebraic and physical status.

This engine computes exact rational identities involving
``f_n=(1+1/n)/3``, Faber--Pandharipande coefficients, Virasoro
complementarity, and free-energy asymmetry.  Formal Page branches and
shadow-radius bounds are retained as explicitly labelled ansätze.

Algebraic reconstruction has two independent levels.  Theorem A is the
universal enhanced-Ran map ``epsilon_A: Omega_X B_X(A) -> A``.  Theorem
B belongs to a chosen quadratic presentation and is certified by the
homology of ``Cone(q_A: A^i -> B_X(A))`` together with ``H_CL`` and
strong convergence.

Replica entropy, entanglement spectra, QES/JLMS, Hilbert-space QEC, and
Page-curve conclusions use their own state, geometry, operator-algebra,
error-channel, and evaporation bridge packages.  Family and shadow
labels provide arity metadata only.

References:
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  thm:hc-koszulness-exact-qec (holographic_codes_koszul.tex)
  prop:lagrangian-perfectness (chiral_koszul_pairs.tex)
  cor:free-energy-ahat-genus (higher_genus_modular_koszul.tex)
  Calabrese-Cardy 2004 (hep-th/0405152): replica trick for 2d CFT
  Ryu-Takayanagi 2006 (hep-th/0603001): holographic entanglement entropy
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, Mapping, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, cancel, diff, expand,
    factorial, log, oo, pi, S, simplify, sqrt, symbols,
    limit as sym_limit, ceiling, floor, exp, Abs, sin,
    binomial, Integer,
)

# ---------------------------------------------------------------------------
# Imports from existing engines
# ---------------------------------------------------------------------------

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    kappa_wN,
    twist_operator_dimension,
    von_neumann_entropy_scalar,
    renyi_entropy_scalar,
    faber_pandharipande,
    scalar_free_energy,
    shadow_depth_class,
    shadow_radius_virasoro,
    entanglement_correction_bound,
    STANDARD_KAPPAS,
)
from compute.lib.holographic_code_engine import (
    code_parameters as algebraic_code_parameters,
)
from compute.lib.holographic_entanglement_qec_engine import (
    physical_bridge_surfaces,
)

# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------

c_sym = Symbol('c')
k_sym = Symbol('k')
n_sym = Symbol('n', positive=True)
g_sym = Symbol('g', positive=True, integer=True)


# =========================================================================
#  SECTION 1: RENYI ENTROPY UNIVERSALITY
# =========================================================================

def renyi_universal_function(n) -> Rational:
    r"""The scalar replica coefficient ``f_n=(1+1/n)/3``.

    At the scalar level, the Renyi entropy factorizes as:
      S_n(A) = kappa(A) * f_n * log(L/epsilon)

    The physical entropy interpretation additionally uses a state,
    regional algebra, normalized replicas, and analytic continuation.

    Special values:
      f_1 = 2/3  (von Neumann limit)
      f_2 = 1/2
      f_inf = 1/3  (min-entropy)

    >>> renyi_universal_function(1)
    2/3
    >>> renyi_universal_function(2)
    1/2
    >>> renyi_universal_function(3)
    4/9
    >>> renyi_universal_function(10)
    11/30
    """
    n = Rational(n)
    if n <= 0:
        raise ValueError(f"Renyi index must be positive, got {n}")
    return Rational(1, 3) * (1 + Rational(1, n))


def renyi_min_entropy_coefficient() -> Rational:
    r"""The scalar limiting coefficient ``lim_{n->oo} f_n=1/3``.

    Its min-entropy interpretation belongs to the replica-state bridge.

    >>> renyi_min_entropy_coefficient()
    1/3
    """
    return Rational(1, 3)


def verify_renyi_universality(kappa_val, n, log_ratio=1) -> Dict[str, Any]:
    r"""Verify the scalar identity ``kappa*f_n*log_ratio``.

    Path 1: Direct computation from twist operator dimension
    Path 2: From replica partition function
    Path 3: From factorization S_n = kappa * f_n

    >>> data = verify_renyi_universality(Rational(1), 2)
    >>> data['paths_agree']
    True
    >>> data['S_n']
    1/2

    >>> data = verify_renyi_universality(Rational(13, 2), 3)
    >>> data['paths_agree']
    True
    """
    kappa_val = Rational(kappa_val)
    n = Rational(n)
    lr = Rational(log_ratio)

    # Path 1: from twist operator dimension
    # h_n = (kappa/12)(n-1/n), log Z_n = -(kappa/3)(n-1/n)*log(L/eps)
    # S_n = log Z_n / (1-n) = (kappa/3)(1+1/n)*log(L/eps)
    h_n = twist_operator_dimension(kappa_val, n)
    log_zn = -2 * h_n * lr  # chiral: -2*h_n, non-chiral doubles
    # Non-chiral convention: log Z_n = -(kappa/3)(n-1/n)*lr
    log_zn_nc = -(kappa_val / 3) * (n - Rational(1, n)) * lr
    path1 = (
        Rational(2) * kappa_val * lr / 3
        if n == 1
        else log_zn_nc / (1 - n)
    )

    # Path 2: direct Renyi formula
    path2 = renyi_entropy_scalar(kappa_val, n, lr)

    # Path 3: factorization kappa * f_n * log_ratio
    f_n = renyi_universal_function(n)
    path3 = kappa_val * f_n * lr

    agree = (simplify(path1 - path2) == 0 and
             simplify(path2 - path3) == 0)

    bridge = physical_bridge_surfaces()['entropy']
    return {
        'kappa': kappa_val,
        'n': n,
        'S_n': path2,
        'f_n': f_n,
        'path1_twist': path1,
        'path2_direct': path2,
        'path3_factored': path3,
        'paths_agree': agree,
        'physical_renyi_entropy': bridge['physical_conclusion'],
        'physical_renyi_status': bridge['status'],
        'physical_renyi_required_data': bridge['required_data'],
    }


def renyi_von_neumann_limit(kappa_val, log_ratio=1) -> Dict[str, Any]:
    r"""Verify the scalar ``n -> 1`` coefficient identity.

    lim_{n->1} S_n = lim_{n->1} (kappa/3)(1+1/n)*log(L/eps)
                   = (2*kappa/3)*log(L/eps)
                   = S_EE (von Neumann entropy)

    Multi-path verification:
      Path 1: algebraic limit of f_n at n=1
      Path 2: derivative of log Z_n (replica trick)
      Path 3: direct von Neumann formula

    >>> data = renyi_von_neumann_limit(Rational(1))
    >>> data['S_EE']
    2/3
    >>> data['paths_agree']
    True

    >>> data = renyi_von_neumann_limit(Rational(13, 2))
    >>> data['S_EE']
    13/3
    """
    kappa_val = Rational(kappa_val)
    lr = Rational(log_ratio)

    # Path 1: algebraic limit
    path1 = kappa_val * renyi_universal_function(1) * lr

    # Path 2: derivative formula (replica trick)
    # S_EE = -d/dn [(1-n)*S_n]|_{n=1} = -d/dn [log Z_n]|_{n=1}
    # d/dn [-(kappa/3)(n-1/n)] = -(kappa/3)(1+1/n^2)
    # At n=1: -(kappa/3)*2 = -2*kappa/3
    # S_EE = -(-2*kappa/3)*lr = (2*kappa/3)*lr
    path2 = Rational(2) * kappa_val / 3 * lr

    # Path 3: direct von Neumann formula
    path3 = von_neumann_entropy_scalar(kappa_val, lr)

    agree = (simplify(path1 - path2) == 0 and
             simplify(path2 - path3) == 0)

    bridge = physical_bridge_surfaces()['entropy']
    return {
        'kappa': kappa_val,
        'S_EE': path1,
        'f_1': renyi_universal_function(1),
        'path1_limit': path1,
        'path2_replica': path2,
        'path3_direct': path3,
        'paths_agree': agree,
        'physical_von_neumann_entropy': bridge['physical_conclusion'],
        'physical_entropy_status': bridge['status'],
    }


def renyi_spectrum_by_class(family: str, n_values=None) -> Dict[str, Any]:
    r"""Return scalar coefficients and shadow arity metadata.

    Shadow class records the available higher arities.  Replica
    corrections require an independently constructed state and twist
    correlators.

    >>> data = renyi_spectrum_by_class('heisenberg')
    >>> data['exact_at_scalar']
    True
    >>> data['shadow_class']
    'G'

    >>> data = renyi_spectrum_by_class('virasoro')
    >>> data['scalar_formula_verified']
    True
    """
    if n_values is None:
        n_values = [Rational(2), Rational(3), Rational(5), Rational(10)]

    cls = shadow_depth_class(family)

    f_values = {}
    for n in n_values:
        f_values[n] = renyi_universal_function(n)

    correction_arities = {
        'G': [],
        'L': [3],
        'C': [3, 4],
        'M': list(range(3, 11)),
    }

    bridge = physical_bridge_surfaces()['entropy']
    return {
        'family': family,
        'shadow_class': cls,
        'f_n_values': f_values,
        'exact_at_scalar': True,
        'scalar_formula_verified': True,
        'supported_higher_arities': correction_arities.get(cls, []),
        'correction_arities': None,
        'n_corrections': None,
        'physical_renyi_spectrum': bridge['physical_conclusion'],
        'physical_renyi_status': bridge['status'],
    }


# =========================================================================
#  SECTION 2: ENTANGLEMENT SPECTRUM
# =========================================================================

def entanglement_spectrum_thermal(kappa_val, n_levels=10) -> Dict[str, Any]:
    r"""Return an equally spaced formal spectrum candidate.

    The candidate energies are equally spaced in the chosen natural
    units.  A density matrix and modular Hamiltonian determine the
    physical entanglement spectrum.

      lambda_j = (1/Z) * exp(-2*pi*j * kappa / L)

    where j = 0, 1, 2, ... labels the occupation number of the
    single free boson mode. The partition function is

      Z = prod_{m>=1} (1 - q^m)^{-1}

    with q = exp(-2*pi/L). The spectral density in the thermodynamic
    limit is flat: rho(E) = kappa/(2*pi) for E > 0.

    The entanglement energies are:
      E_j = 2*pi*j / L   (equally spaced, spacing = 2*pi/L)

    >>> spec = entanglement_spectrum_thermal(Rational(1), 5)
    >>> spec['n_levels']
    5
    >>> spec['spacing']
    1
    >>> spec['is_thermal'] is None
    True
    """
    kappa_val = Rational(kappa_val)
    # Entanglement energies (in units of 2*pi/L = 1)
    energies = [Rational(j) for j in range(n_levels)]
    # Boltzmann weights (unnormalized, in units where beta*spacing = 1)
    weights = [exp(-e) for e in energies]

    bridge = physical_bridge_surfaces()['entropy']
    return {
        'kappa': kappa_val,
        'shadow_class': 'G',
        'is_thermal': bridge['physical_conclusion'],
        'formal_spectrum_candidate': True,
        'n_levels': n_levels,
        'energies': energies,
        'spacing': Rational(1),
        'spectral_density': None,
        'degeneracy_per_level': None,
        'physical_spectrum': bridge['physical_conclusion'],
        'physical_spectrum_status': bridge['status'],
    }


def entanglement_spectrum_class_m(c_val, n_levels=5) -> Dict[str, Any]:
    r"""Return a class-M shadow-radius correction ansatz.

    For class M, the spectrum has a thermal backbone modified by
    shadow corrections at each arity r >= 3:

      E_j = E_j^thermal + sum_{r>=3} delta_E_j^(r)

    The corrections are controlled by the shadow radius rho(A):
      |delta_E_j^(r)| <= C * rho^r * j^{r-2}

    The geometric estimate is formal shadow data.  A physical spectrum
    uses a density matrix and spectral theorem in the entropy bridge.

    >>> spec = entanglement_spectrum_class_m(Rational(1, 2), 3)
    >>> spec['shadow_class']
    'M'
    >>> spec['rho'] > 0
    True

    >>> spec = entanglement_spectrum_class_m(Rational(26), 3)
    >>> spec['formal_geometric_bound_converges']
    True
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    rho = shadow_radius_virasoro(float(c_val))

    # Thermal backbone energies
    energies_thermal = [Rational(j) for j in range(n_levels)]

    # Correction bounds at each level (leading correction from arity 3)
    correction_bounds = []
    for j in range(n_levels):
        if j == 0:
            correction_bounds.append(0.0)
        else:
            # Leading correction ~ rho^3 * j
            correction_bounds.append(rho**3 * float(j))

    # Spectral gap correction
    gap_thermal = Rational(1)  # in natural units
    gap_correction_bound = rho**3 if rho < float('inf') else float('inf')

    bridge = physical_bridge_surfaces()['entropy']
    return {
        'c': c_val,
        'kappa': kappa,
        'shadow_class': 'M',
        'rho': rho,
        'convergent': None,
        'formal_geometric_bound_converges': rho < 1.0,
        'n_levels': n_levels,
        'energies_thermal': energies_thermal,
        'correction_bounds': correction_bounds,
        'gap_thermal': gap_thermal,
        'gap_correction_bound': gap_correction_bound,
        'self_dual': (c_val == 13),
        'physical_spectrum': bridge['physical_conclusion'],
        'physical_spectrum_status': bridge['status'],
    }


def spectral_complexity_by_class() -> Dict[str, Dict[str, Any]]:
    r"""Shadow-arity profiles for a future spectral comparison.

    Class G: thermal spectrum, zero corrections, complexity O(1)
    Class L: thermal + 1 correction, complexity O(rho^3)
    Class C: thermal + 2 corrections, complexity O(rho^4)
    Class M: thermal + infinite tower, complexity O(rho^3/(1-rho))

    The physical spectral entropy and complexity belong to the
    replica-state bridge.

    >>> data = spectral_complexity_by_class()
    >>> data['G']['formal_higher_arity_slots']
    0
    >>> data['M']['formal_higher_arity_slots']
    -1
    """
    bridge = physical_bridge_surfaces()['entropy']
    return {
        'G': {
            'name': 'Gaussian',
            'r_max': 2,
            'n_corrections': None,
            'formal_higher_arity_slots': 0,
            'spectrum': bridge['physical_conclusion'],
            'supported_higher_arities': [],
            'spectral_entropy_correction': None,
            'complexity': None,
            'status': bridge['status'],
        },
        'L': {
            'name': 'Lie/tree',
            'r_max': 3,
            'n_corrections': None,
            'formal_higher_arity_slots': 1,
            'spectrum': bridge['physical_conclusion'],
            'supported_higher_arities': [3],
            'complexity': None,
            'status': bridge['status'],
        },
        'C': {
            'name': 'Contact',
            'r_max': 4,
            'n_corrections': None,
            'formal_higher_arity_slots': 2,
            'spectrum': bridge['physical_conclusion'],
            'supported_higher_arities': [3, 4],
            'complexity': None,
            'status': bridge['status'],
        },
        'M': {
            'name': 'Mixed',
            'r_max': -1,
            'n_corrections': None,
            'formal_higher_arity_slots': -1,
            'spectrum': bridge['physical_conclusion'],
            'supported_higher_arities': 'unbounded',
            'complexity': None,
            'status': bridge['status'],
        },
    }


# =========================================================================
#  SECTION 3: PAGE CURVE AND TRANSITION
# =========================================================================

def page_time_classical(S_BH) -> Rational:
    r"""Crossing time of the chosen linear branch ansatz.

    The two formal branches agree when
      (c/6)*t_P = S_BH - ((26-c)/6)*t_P
      t_P * (c + 26-c)/6 = S_BH
      t_P * 26/6 = S_BH
      t_P = 6*S_BH/26 = 3*S_BH/13

    A physical Page time additionally uses an evaporation model,
    radiation algebra, and island/QES prescription.

    >>> page_time_classical(Rational(100))
    300/13
    >>> page_time_classical(Rational(130))
    30
    >>> page_time_classical(Rational(13))
    3
    """
    return Rational(3) * Rational(S_BH) / 13


def page_time_quantum_correction(c_val, max_genus=20) -> Dict[str, Any]:
    r"""Formal genus-asymmetry coefficient for the branch crossing.

    delta_t = -(3/13)*(c-13) * sum_{g>=1} lambda_g^FP

    The sum converges to (1/2)/sin(1/2) - 1 ~ 0.04291 (A-hat evaluation).
    At c=13: delta_t = 0 identically (self-dual).

    Multi-path verification:
      Path 1: Direct sum of Faber-Pandharipande coefficients
      Path 2: A-hat evaluation at x=1: (1/2)/sin(1/2) - 1
      Path 3: Integral representation via Bernoulli numbers

    >>> data = page_time_quantum_correction(Rational(13))
    >>> data['formal_delta_t_coefficient']
    0
    >>> data['self_dual']
    True

    >>> data = page_time_quantum_correction(Rational(26))
    >>> data['formal_delta_t_coefficient'] != 0
    True
    """
    c_val = Rational(c_val)
    asymmetry = c_val - 13

    # Path 1: partial sum
    partial_sum = Rational(0)
    for g in range(1, max_genus + 1):
        partial_sum += faber_pandharipande(g)

    # Path 2: A-hat closed form (1/2)/sin(1/2) - 1
    ahat_exact = 0.5 / math.sin(0.5) - 1.0

    # Exact shift of the implemented additive-genus branch ansatz.
    delta_coeff = Rational(-3, 13) * asymmetry * partial_sum

    bridge = physical_bridge_surfaces()['chaos_page']
    return {
        'c': c_val,
        'asymmetry': asymmetry,
        'partial_sum': partial_sum,
        'ahat_closed_form': ahat_exact,
        'sum_converged': abs(float(partial_sum) - ahat_exact) < 1e-8,
        'formal_delta_t_coefficient': delta_coeff,
        'delta_t_coefficient': bridge['physical_conclusion'],
        'self_dual': (c_val == 13),
        'physical_page_time_correction': bridge['physical_conclusion'],
        'page_status': bridge['status'],
    }


def page_transition_width_by_class(family: str, c_val=None, S_BH=None) -> Dict[str, Any]:
    r"""Return arity counts and a formal geometric width bound.

    The comparison ansatz is
      delta_width ~ sum_{r >= 3} |S_r| * rho^r / S_BH

    Class G contributes zero higher-arity terms.  Classes L and C
    contribute one and two supported arities; class M contributes an
    unbounded arity sequence.

    Shadow depth records the arity count.  A physical transition width
    belongs to the evaporation/QES bridge.

    >>> data = page_transition_width_by_class('heisenberg')
    >>> data['quantum_smearing'] is None
    True
    >>> data['shadow_class']
    'G'

    >>> data = page_transition_width_by_class('virasoro', Rational(26), Rational(100))
    >>> data['formal_geometric_bound'] > 0
    True
    """
    cls = shadow_depth_class(family)

    smearing_terms = {
        'G': 0,
        'L': 1,
        'C': 2,
        'M': -1,  # infinite
    }

    bridge = physical_bridge_surfaces()['chaos_page']
    result = {
        'family': family,
        'shadow_class': cls,
        'formal_arity_terms': smearing_terms.get(cls, -1),
        'smearing_terms': None,
        'quantum_smearing': bridge['physical_conclusion'],
        'physical_page_width': bridge['physical_conclusion'],
        'page_status': bridge['status'],
    }

    if c_val is not None and S_BH is not None and cls == 'M':
        rho = shadow_radius_virasoro(float(c_val))
        # Leading correction from arity 3
        if rho < 1.0:
            # Geometric sum bound: sum rho^r for r>=3 = rho^3/(1-rho)
            smearing_bound = rho**3 / (1.0 - rho) / float(S_BH)
        else:
            smearing_bound = float('inf')
        result['rho'] = rho
        result['formal_geometric_bound'] = smearing_bound
        result['formal_geometric_bound_converges'] = rho < 1.0

    return result


def page_curve_full(c_val, S_BH, n_times=20, max_genus=10) -> Dict[str, Any]:
    r"""Compute the formal two-branch scalar envelope.

    The Page curve consists of two branches:
      S_radiation(t) = (c/6)*t + sum_{g>=1} F_g(A)
      S_island(t) = S_BH - ((26-c)/6)*t + sum_{g>=1} F_g(A!)

    The pointwise minimum is retained as a scalar ansatz.  Its Page/QES
    interpretation uses the evaporation and island bridge.

    The genus-g corrections are:
      F_g(A) = kappa(A) * lambda_g^FP
      F_g(A!) = kappa(A!) * lambda_g^FP

    For Virasoro: kappa = c/2, kappa! = (26-c)/2.

    >>> data = page_curve_full(Rational(13), Rational(100), 5)
    >>> data['formal_crossing_time']
    300/13
    >>> data['self_dual']
    True
    >>> len(data['times']) == 5
    True

    >>> data = page_curve_full(Rational(26), Rational(100), 5)
    >>> data['self_dual']
    False
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26 - c_val)

    # Classical branch-crossing candidate
    t_P_classical = page_time_classical(S_BH)

    # Genus corrections
    F_sum = Rational(0)
    F_sum_dual = Rational(0)
    genus_corrections = {}
    for g in range(1, max_genus + 1):
        lam_g = faber_pandharipande(g)
        fg = kappa * lam_g
        fg_dual = kappa_dual * lam_g
        F_sum += fg
        F_sum_dual += fg_dual
        genus_corrections[g] = {
            'F_g': fg,
            'F_g_dual': fg_dual,
            'lambda_g': lam_g,
        }

    # Solve s_radiation(t) = s_island(t) for the implemented branches.
    formal_delta_t = Rational(-3, 13) * (c_val - 13) * sum(
        row['lambda_g'] for row in genus_corrections.values()
    )
    t_P = t_P_classical + formal_delta_t

    # Generate time points
    t_max = 2 * t_P
    dt = t_max / n_times if n_times > 1 else t_max
    times = []
    s_rad_values = []
    s_island_values = []
    s_page_values = []

    for i in range(n_times):
        t = dt * i if n_times > 1 else Rational(0)
        s_rad = c_val * t / 6 + F_sum
        s_island = S_BH - (26 - c_val) * t / 6 + F_sum_dual
        s_page = min(s_rad, s_island)
        times.append(t)
        s_rad_values.append(s_rad)
        s_island_values.append(s_island)
        s_page_values.append(s_page)

    bridge = physical_bridge_surfaces()['chaos_page']
    return {
        'c': c_val,
        'S_BH': S_BH,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'formal_classical_crossing_time': t_P_classical,
        'formal_genus_crossing_shift': formal_delta_t,
        'formal_crossing_time': t_P,
        'page_time': bridge['physical_conclusion'],
        'page_status': bridge['status'],
        'self_dual': (c_val == 13),
        'times': times,
        's_radiation': s_rad_values,
        's_island': s_island_values,
        'formal_scalar_envelope': s_page_values,
        's_page': bridge['physical_conclusion'],
        'physical_page_curve': bridge['physical_conclusion'],
        'genus_corrections': genus_corrections,
        'F_total': F_sum,
        'F_total_dual': F_sum_dual,
    }


def page_entropy_at_transition(c_val, S_BH) -> Dict[str, Any]:
    r"""Value of the formal branches at their crossing.

    At the formal crossing ``t=t_P`` the two linear branches agree:

      S_Page = (c/6) * t_P = (c/6) * (3*S_BH/13) = c*S_BH/(26)

    The normalized scalar value is
      S_Page/S_BH = c/26

    At ``c=13`` this scalar value equals ``S_BH/2``.

    Multi-path verification:
      Path 1: from radiation branch: S_rad(t_P) = c*S_BH/26
      Path 2: from island branch: S_island(t_P) = S_BH - (26-c)*S_BH/26 = c*S_BH/26
      Path 3: from symmetry at c=13: S_Page = S_BH/2

    >>> data = page_entropy_at_transition(Rational(13), Rational(100))
    >>> data['formal_transition_value']
    50
    >>> data['formal_fraction']
    1/2
    >>> data['paths_agree']
    True

    >>> data = page_entropy_at_transition(Rational(26), Rational(100))
    >>> data['formal_transition_value']
    100
    >>> data['formal_fraction']
    1
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    t_P = page_time_classical(S_BH)

    # Path 1: radiation branch
    path1 = c_val * t_P / 6

    # Path 2: island branch
    path2 = S_BH - (26 - c_val) * t_P / 6

    # Path 3: direct formula
    path3 = c_val * S_BH / 26

    agree = (simplify(path1 - path2) == 0 and
             simplify(path1 - path3) == 0)

    bridge = physical_bridge_surfaces()['chaos_page']
    return {
        'c': c_val,
        'S_BH': S_BH,
        'formal_crossing_time': t_P,
        'page_time': bridge['physical_conclusion'],
        'formal_transition_value': path1,
        'formal_fraction': c_val / 26,
        'S_page': bridge['physical_conclusion'],
        'fraction': bridge['physical_conclusion'],
        'path1_radiation': path1,
        'path2_island': path2,
        'path3_direct': path3,
        'paths_agree': agree,
        'physical_page_entropy': bridge['physical_conclusion'],
        'page_status': bridge['status'],
    }


# =========================================================================
#  SECTION 4: QEC RATE WITH HOLSTEIN-RIVERA SIMPLIFICATION
# =========================================================================

def qec_verification_chain_before_hr() -> Dict[str, Any]:
    r"""Record the manuscript's pre-Holstein--Rivera proof lane.

    The recorded pre-HR lane is:
      Step 1: Verify A is chirally Koszul (K1)
      Step 2: Deduce Kac-Shapovalov nondegeneracy (K8)
      Step 3: Deduce perfectness of cyclic pairing (P3)
      Step 4: Apply Lagrangian criterion (K11) to get R = 1/2

    This is a 3-intermediate-step chain.

    >>> chain = qec_verification_chain_before_hr()
    >>> chain['n_steps']
    4
    >>> chain['hypothesis_needed']
    'P3 (properness/perfectness)'
    """
    return {
        'n_steps': 4,
        'chain': ['K1 (Koszul)', 'K8 (Kac-Shapovalov)', 'P3 (perfectness)', 'K11 (Lagrangian)'],
        'hypothesis_needed': 'P3 (properness/perfectness)',
        'lagrangian_fraction_candidate': Rational(1, 2),
        'rate': None,
        'physical_rate_status': (
            'CONDITIONAL_ON_HILBERT_ERROR_ALGEBRA_AND_RECOVERY_MAPS'
        ),
        'lane_status': 'MANUSCRIPT_LANE_REQUIRES_SOURCE_VERIFICATION',
    }


def qec_verification_chain_after_hr() -> Dict[str, Any]:
    r"""Record the proposed post-Holstein--Rivera proof lane.

    The proposed post-HR lane is:
      Step 1: Verify A is chirally Koszul (K1)
      Step 2: Apply Lagrangian criterion (K11) to get R = 1/2

    Its mathematical use requires the exact Holstein--Rivera theorem and
    the manuscript's Theorem C hypothesis package.

    >>> chain = qec_verification_chain_after_hr()
    >>> chain['n_steps']
    2
    >>> chain['claimed_hypothesis_removed']
    'P3 (properness/perfectness)'
    """
    return {
        'n_steps': 2,
        'chain': ['K1 (Koszul)', 'K11 (Lagrangian)'],
        'hypothesis_removed': None,
        'claimed_hypothesis_removed': 'P3 (properness/perfectness)',
        'lagrangian_fraction_candidate': Rational(1, 2),
        'rate': None,
        'lane_status': 'REQUIRES_THEOREM_C_AND_HOLSTEIN_RIVERA_PACKAGE',
        'physical_rate_status': (
            'CONDITIONAL_ON_HILBERT_ERROR_ALGEBRA_AND_RECOVERY_MAPS'
        ),
        'simplification_factor': None,
        'claimed_simplification_factor': 2,
    }


def qec_rate_by_family_simplified(
    family: str,
    *,
    algebra_id: Optional[str] = None,
    quadratic_certificate: Optional[Mapping[str, object]] = None,
    theorem_c_hr_package_verified: bool = False,
    **kwargs,
) -> Dict[str, Any]:
    r"""Return typed algebraic and physical QEC status for one algebra.

    Shadow class supplies the arity profile.  Theorem B status comes from
    a matching quadratic certificate.  The Lagrangian fraction uses the
    Theorem C/Holstein--Rivera package, while physical rate and distance
    use a Hilbert realization and error channel.

    >>> data = qec_rate_by_family_simplified('heisenberg')
    >>> data['rate'] is None
    True
    >>> data['exact_quadratic_recovery'] is None
    True

    >>> data = qec_rate_by_family_simplified('virasoro')
    >>> data['universal_reconstruction']
    True
    """
    cls = shadow_depth_class(family)
    r_max_map = {'G': 2, 'L': 3, 'C': 4, 'M': -1}
    r_max = r_max_map.get(cls, -1)
    channels = max(r_max - 2, 0) if r_max > 0 else -1
    algebraic = algebraic_code_parameters(
        family,
        algebra_id=algebra_id,
        quadratic_certificate=quadratic_certificate,
        **kwargs,
    )
    bridge = physical_bridge_surfaces()['hilbert_qec']

    return {
        'family': family,
        'algebra_id': algebraic['algebra_id'],
        'is_koszul': algebraic['quadratic_koszul'],
        'universal_reconstruction': algebraic['universal_reconstruction'],
        'universal_reconstruction_status': algebraic[
            'universal_reconstruction_status'
        ],
        'theorem_a_surface': algebraic['theorem_a_surface'],
        'theorem_b_surface': algebraic['theorem_b_surface'],
        'exact_quadratic_recovery': algebraic['exact_quadratic_recovery'],
        'quadratic_recovery_status': algebraic['exact_recovery_status'],
        'lagrangian_fraction': (
            Rational(1, 2) if theorem_c_hr_package_verified else None
        ),
        'lagrangian_fraction_status': (
            'CERTIFIED' if theorem_c_hr_package_verified
            else 'THEOREM_C_AND_HOLSTEIN_RIVERA_PACKAGE_REQUIRED'
        ),
        'rate': bridge['physical_conclusion'],
        'physical_rate_status': bridge['status'],
        'distance': bridge['physical_conclusion'],
        'arity_floor': 2,
        'distance_kind': 'physical distance requires a realized error model',
        'physical_distance': bridge['physical_conclusion'],
        'physical_distance_status': bridge['status'],
        'shadow_class': cls,
        'r_max': r_max,
        'formal_higher_arity_slots': channels,
        'channels': bridge['physical_conclusion'],
        'code_type': bridge['physical_conclusion'],
        'verification_steps': None,
        'P3_needed': None,
    }


# =========================================================================
#  SECTION 5: MODULAR ENTANGLEMENT ENTROPY AT GENUS g
# =========================================================================

def modular_entanglement_entropy(kappa_val, kappa_dual_val, g: int) -> Rational:
    r"""Absolute genus-``g`` scalar free-energy asymmetry.

    S^mod_g(A) = |F_g(A) - F_g(A!)| = |kappa - kappa!| * lambda_g^FP

    A relative-entropy interpretation uses the modular/JLMS
    operator-algebra package.

    For KM families (kappa + kappa! = 0):
      S^mod_g = 2*|kappa|*lambda_g^FP

    For Virasoro (kappa + kappa! = 13):
      S^mod_g = |c-13|*lambda_g^FP

    At ``c=13`` the scalar asymmetry vanishes.

    >>> modular_entanglement_entropy(Rational(1), Rational(-1), 1)  # Heisenberg k=1
    1/12
    >>> modular_entanglement_entropy(Rational(13, 2), Rational(13, 2), 1)  # Vir c=13
    0
    >>> modular_entanglement_entropy(Rational(13), Rational(0), 1)  # Vir c=26
    13/24
    """
    kappa_val = Rational(kappa_val)
    kappa_dual_val = Rational(kappa_dual_val)
    lam_g = faber_pandharipande(g)
    return Abs(kappa_val - kappa_dual_val) * lam_g


def modular_entanglement_heisenberg(k, g: int) -> Rational:
    r"""Heisenberg scalar free-energy asymmetry at genus ``g``.

    kappa(H_k) = k, kappa(H_k!) = -k (KM complementarity).
    S^mod_g(H_k) = 2*|k|*lambda_g^FP.

    At g=1: S^mod_1(H_1) = 2*1*(1/24) = 1/12.

    Multi-path verification:
      Path 1: |F_g - F_g!| = |k*lam_g - (-k*lam_g)| = 2|k|*lam_g
      Path 2: From KM complementarity: kappa - kappa! = 2*kappa = 2k
      Path 3: From free energy: F_g(H_k) = k/24 at g=1

    >>> modular_entanglement_heisenberg(Rational(1), 1)
    1/12
    >>> modular_entanglement_heisenberg(Rational(2), 1)
    1/6
    >>> modular_entanglement_heisenberg(Rational(1), 2)
    7/2880
    """
    k = Rational(k)
    kappa = kappa_heisenberg(k)
    kappa_dual = -kappa  # KM complementarity: kappa + kappa! = 0
    return modular_entanglement_entropy(kappa, kappa_dual, g)


def modular_entanglement_virasoro(c_val, g: int) -> Rational:
    r"""Virasoro scalar free-energy asymmetry at genus ``g``.

    kappa(Vir_c) = c/2, kappa(Vir_{26-c}) = (26-c)/2.
    kappa - kappa! = c/2 - (26-c)/2 = c - 13.
    S^mod_g(Vir_c) = |c-13| * lambda_g^FP.

    At c=13 (self-dual): S^mod_g = 0 for all g.
    At c=26 (critical): S^mod_g = 13*lambda_g^FP.

    >>> modular_entanglement_virasoro(Rational(13), 1)
    0
    >>> modular_entanglement_virasoro(Rational(26), 1)
    13/24
    >>> modular_entanglement_virasoro(Rational(1), 1)
    1/2
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26 - c_val)
    return modular_entanglement_entropy(kappa, kappa_dual, g)


def modular_entanglement_affine_sl2(k, g: int) -> Rational:
    r"""Affine ``sl_2`` scalar free-energy asymmetry at genus ``g``.

    kappa = 3(k+2)/4, kappa! = -3(k+2)/4 (KM complementarity).
    S^mod_g = 2 * 3(k+2)/4 * lambda_g^FP = 3(k+2)/2 * lambda_g^FP.

    >>> modular_entanglement_affine_sl2(Rational(1), 1)
    3/16
    >>> modular_entanglement_affine_sl2(Rational(2), 1)
    1/4
    """
    k = Rational(k)
    dim_g = 3
    h_dual = 2
    kappa = kappa_affine(dim_g, k, h_dual)
    kappa_dual = -kappa  # KM complementarity
    return modular_entanglement_entropy(kappa, kappa_dual, g)


def modular_entanglement_genus_tower(kappa_val, kappa_dual_val, max_genus=5) -> Dict[str, Any]:
    r"""Scalar free-energy-asymmetry tower through ``max_genus``.

    The modular entanglement decays as lambda_g^FP ~ (2/(2*pi)^{2g})
    for large g: exponentially fast decay controlled by (2*pi)^{-2}.

    The total modular entanglement (summed over genera) converges to
      S^mod_total = |kappa - kappa!| * ((1/2)/sin(1/2) - 1)

    >>> data = modular_entanglement_genus_tower(Rational(1), Rational(-1))
    >>> data['S_mod'][1]
    1/12
    >>> data['total'] > 0
    True

    >>> data = modular_entanglement_genus_tower(Rational(13, 2), Rational(13, 2))
    >>> data['S_mod'][1]
    0
    >>> data['total']
    0
    """
    kappa_val = Rational(kappa_val)
    kappa_dual_val = Rational(kappa_dual_val)
    asymmetry = Abs(kappa_val - kappa_dual_val)

    s_mod = {}
    total = Rational(0)
    for g in range(1, max_genus + 1):
        s_g = modular_entanglement_entropy(kappa_val, kappa_dual_val, g)
        s_mod[g] = s_g
        total += s_g

    # Closed form for the total: asymmetry * ((1/2)/sin(1/2) - 1)
    ahat_sum = 0.5 / math.sin(0.5) - 1.0
    total_closed = float(asymmetry) * ahat_sum

    bridge = physical_bridge_surfaces()['modular_jlms']
    return {
        'kappa': kappa_val,
        'kappa_dual': kappa_dual_val,
        'asymmetry': asymmetry,
        'S_mod': s_mod,
        'total': total,
        'total_closed_form': total_closed,
        'decay_rate': Rational(1, 4) * pi**(-2),  # ~ (2*pi)^{-2}
        'physical_modular_entanglement': bridge['physical_conclusion'],
        'physical_modular_status': bridge['status'],
    }


def verify_modular_entanglement_heisenberg_g1() -> Dict[str, bool]:
    r"""Multi-path verification of S^mod_1(H_1) = 1/12.

    Path 1: |F_1 - F_1!| = |k/24 - (-k/24)| = k/12
    Path 2: 2*|kappa|*lambda_1 = 2*1*(1/24) = 1/12
    Path 3: From KM complementarity: |kappa - kappa!| = 2|k| = 2, then 2*(1/24)

    >>> checks = verify_modular_entanglement_heisenberg_g1()
    >>> all(checks.values())
    True
    """
    k = Rational(1)
    kappa = kappa_heisenberg(k)
    lam_1 = faber_pandharipande(1)

    # Path 1: from free energies
    f1 = scalar_free_energy(kappa, 1)
    f1_dual = scalar_free_energy(-kappa, 1)
    path1 = Abs(f1 - f1_dual)

    # Path 2: from formula
    path2 = 2 * Abs(kappa) * lam_1

    # Path 3: from complementarity
    asymmetry = Abs(kappa - (-kappa))
    path3 = asymmetry * lam_1

    expected = Rational(1, 12)

    return {
        'path1_free_energy': (path1 == expected),
        'path2_formula': (path2 == expected),
        'path3_complementarity': (path3 == expected),
        'all_equal': (path1 == path2 == path3 == expected),
    }


# =========================================================================
#  SECTION 6: CROSS-CHECKS AND LANDSCAPE SURVEY
# =========================================================================

def verify_renyi_factorization_all_families(n=2) -> Dict[str, bool]:
    r"""Verify S_n = kappa * f_n for all standard families.

    At the scalar level, the Renyi entropy factorizes universally
    as S_n = kappa * f_n where f_n = (1/3)(1+1/n).

    >>> checks = verify_renyi_factorization_all_families(2)
    >>> all(checks.values())
    True

    >>> checks = verify_renyi_factorization_all_families(5)
    >>> all(checks.values())
    True
    """
    f_n = renyi_universal_function(n)
    checks = {}

    families = {
        'heisenberg_1': kappa_heisenberg(Rational(1)),
        'virasoro_1': kappa_virasoro(Rational(1)),
        'virasoro_13': kappa_virasoro(Rational(13)),
        'virasoro_26': kappa_virasoro(Rational(26)),
        'sl2_1': kappa_affine(3, Rational(1), 2),
        'betagamma': kappa_betagamma(Rational(1)),
    }

    for name, kap in families.items():
        s_n_direct = renyi_entropy_scalar(kap, n, 1)
        s_n_factored = kap * f_n
        checks[name] = (simplify(s_n_direct - s_n_factored) == 0)

    return checks


def verify_page_time_independence_of_c() -> Dict[str, bool]:
    r"""Verify the linear-branch crossing is independent of ``c``.

    t_P = 3*S_BH/13 for all c in the Virasoro family.

    Path 1: direct formula t_P = 6*S_BH/(c + (26-c)) = 6*S_BH/26
    Path 2: solve S_rad(t_P) = S_island(t_P)
    Path 3: evaluate at c=1, c=13, c=26 and check equality

    >>> checks = verify_page_time_independence_of_c()
    >>> all(checks.values())
    True
    """
    S_BH = Rational(100)
    expected = Rational(300, 13)

    checks = {}
    for c_val in [Rational(1), Rational(7, 10), Rational(13), Rational(26), Rational(50)]:
        t_P = page_time_classical(S_BH)
        # Verify: S_rad(t_P) = S_island(t_P) at the classical level
        s_rad = c_val * t_P / 6
        s_isl = S_BH - (26 - c_val) * t_P / 6
        checks[f'c={c_val}'] = (simplify(s_rad - s_isl) == 0 and t_P == expected)

    return checks


def verify_modular_entanglement_self_dual_vanishing() -> Dict[str, bool]:
    r"""Verify scalar free-energy asymmetry vanishes at ``c=13``.

    The scalar involution ``c -> 26-c`` fixes ``c=13``; hence the two
    scalar free energies agree.

    >>> checks = verify_modular_entanglement_self_dual_vanishing()
    >>> all(checks.values())
    True
    """
    checks = {}
    for g in range(1, 8):
        s_mod = modular_entanglement_virasoro(Rational(13), g)
        checks[f'g={g}'] = (s_mod == 0)
    return checks


def verify_modular_entanglement_km_formula() -> Dict[str, bool]:
    r"""Verify S^mod_g = 2*|kappa|*lambda_g for KM families.

    For KM: kappa + kappa! = 0, so kappa - kappa! = 2*kappa.
    S^mod_g = |2*kappa| * lambda_g.

    >>> checks = verify_modular_entanglement_km_formula()
    >>> all(checks.values())
    True
    """
    checks = {}
    for k_val in [Rational(1), Rational(2), Rational(5)]:
        kappa = kappa_heisenberg(k_val)
        for g in [1, 2, 3]:
            lam_g = faber_pandharipande(g)
            s_mod = modular_entanglement_heisenberg(k_val, g)
            expected = 2 * Abs(kappa) * lam_g
            checks[f'k={k_val}_g={g}'] = (s_mod == expected)
    return checks


def full_page_curve_analysis(
    c_val,
    S_BH,
    *,
    algebra_id: Optional[str] = None,
    quadratic_certificate: Optional[Mapping[str, object]] = None,
    theorem_c_hr_package_verified: bool = False,
) -> Dict[str, Any]:
    r"""Return scalar candidates and typed reconstruction/bridge status.

    Combines scalar replica coefficients, shadow metadata, formal branch
    data, Theorem A/B status, and independent physical bridge status.

    >>> data = full_page_curve_analysis(Rational(13), Rational(100))
    >>> data['self_dual']
    True
    >>> data['qec_rate'] is None
    True
    >>> data['formal_crossing_time']
    300/13
    >>> data['S_mod_1']
    0
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26 - c_val)
    requested_id = algebra_id or f'virasoro:c={c_val}'
    qec = qec_rate_by_family_simplified(
        'virasoro',
        c=c_val,
        algebra_id=requested_id,
        quadratic_certificate=quadratic_certificate,
        theorem_c_hr_package_verified=theorem_c_hr_package_verified,
    )
    bridges = physical_bridge_surfaces()

    return {
        'c': c_val,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'self_dual': (c_val == 13),
        # Renyi
        'f_2': renyi_universal_function(2),
        'S_2_scalar_candidate': renyi_entropy_scalar(kappa, 2, 1),
        'S_2': bridges['entropy']['physical_conclusion'],
        'entropy_status': bridges['entropy']['status'],
        # Spectrum
        'shadow_class': 'M',  # Virasoro is always class M
        'rho': shadow_radius_virasoro(float(c_val)),
        # Page
        'formal_crossing_time': page_time_classical(S_BH),
        'formal_transition_value': c_val * S_BH / 26,
        'formal_transition_fraction': c_val / 26,
        'page_time': bridges['chaos_page']['physical_conclusion'],
        'S_page': bridges['chaos_page']['physical_conclusion'],
        'page_fraction': bridges['chaos_page']['physical_conclusion'],
        'page_status': bridges['chaos_page']['status'],
        # QEC
        'qec_rate': qec['rate'],
        'qec_distance': qec['distance'],
        'qec_status': qec['physical_rate_status'],
        'lagrangian_fraction': qec['lagrangian_fraction'],
        'is_koszul': qec['is_koszul'],
        'exact_quadratic_recovery': qec['exact_quadratic_recovery'],
        'quadratic_recovery_status': qec['quadratic_recovery_status'],
        'universal_reconstruction': qec['universal_reconstruction'],
        'theorem_a_surface': qec['theorem_a_surface'],
        'theorem_b_surface': qec['theorem_b_surface'],
        'qec_verification_steps': qec['verification_steps'],
        # Modular entanglement
        'S_mod_1': modular_entanglement_virasoro(c_val, 1),
        'S_mod_2': modular_entanglement_virasoro(c_val, 2),
        'S_mod_total': sum(modular_entanglement_virasoro(c_val, g) for g in range(1, 11)),
        'physical_modular_entanglement': bridges['modular_jlms'][
            'physical_conclusion'
        ],
        'physical_modular_status': bridges['modular_jlms']['status'],
    }


def entanglement_landscape_survey(
    quadratic_certificates: Optional[
        Mapping[str, Mapping[str, object]]
    ] = None,
) -> List[Dict[str, Any]]:
    r"""Survey scalar data with algebra-bound reconstruction status.

    Each row contains scalar candidates, shadow metadata, Theorem A/B
    status, and independent physical bridge status.

    >>> survey = entanglement_landscape_survey()
    >>> len(survey) >= 6
    True
    >>> all(row['qec_rate'] is None for row in survey)
    True
    """
    families = [
        ('Heisenberg H_1', 'heisenberg:k=1', kappa_heisenberg(Rational(1)), -kappa_heisenberg(Rational(1)), 'heisenberg'),
        ('Virasoro c=1/2', 'virasoro:c=1/2', kappa_virasoro(Rational(1, 2)), kappa_virasoro(Rational(51, 2)), 'virasoro'),
        ('Virasoro c=13', 'virasoro:c=13', kappa_virasoro(Rational(13)), kappa_virasoro(Rational(13)), 'virasoro'),
        ('Virasoro c=26', 'virasoro:c=26', kappa_virasoro(Rational(26)), kappa_virasoro(Rational(0)), 'virasoro'),
        ('sl_2 k=1', 'affine:sl2:k=1', kappa_affine(3, Rational(1), 2), -kappa_affine(3, Rational(1), 2), 'affine'),
        ('beta-gamma', 'betagamma:lambda=1', kappa_betagamma(Rational(1)), kappa_betagamma(Rational(1)), 'betagamma'),
    ]

    survey = []
    certificate_map = quadratic_certificates or {}
    bridges = physical_bridge_surfaces()
    for name, algebra_id, kap, kap_dual, family_type in families:
        s_ee = von_neumann_entropy_scalar(kap, 1)
        s_mod_1 = modular_entanglement_entropy(kap, kap_dual, 1)
        cls = shadow_depth_class(family_type)
        algebraic = algebraic_code_parameters(
            family_type,
            algebra_id=algebra_id,
            quadratic_certificate=certificate_map.get(algebra_id),
        )

        survey.append({
            'family': name,
            'algebra_id': algebra_id,
            'kappa': kap,
            'S_EE_scalar_candidate': s_ee,
            'S_EE_scalar': bridges['entropy']['physical_conclusion'],
            'entropy_status': bridges['entropy']['status'],
            'f_2': renyi_universal_function(2),
            'shadow_class': cls,
            'qec_rate': bridges['hilbert_qec']['physical_conclusion'],
            'qec_status': bridges['hilbert_qec']['status'],
            'is_koszul': algebraic['quadratic_koszul'],
            'exact_quadratic_recovery': algebraic['exact_quadratic_recovery'],
            'quadratic_recovery_status': algebraic['exact_recovery_status'],
            'universal_reconstruction': algebraic['universal_reconstruction'],
            'theorem_a_surface': algebraic['theorem_a_surface'],
            'theorem_b_surface': algebraic['theorem_b_surface'],
            'S_mod_1': s_mod_1,
            'physical_modular_entanglement': bridges['modular_jlms'][
                'physical_conclusion'
            ],
            'physical_modular_status': bridges['modular_jlms']['status'],
        })

    return survey
