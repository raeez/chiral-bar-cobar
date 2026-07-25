r"""Algebraic invariants and bridge obligations for holographic QEC.

The exact layer consists of scalar identities, shadow arity data, the
universal Theorem A map
``epsilon_A: Omega_X B_X(A) -> A``, and algebra-bound Theorem B
certificates for ``q_A: A^i -> B_X(A)``.  The homology of
``Cone(q_A)``, together with ``H_CL`` and strong convergence, governs
the quadratic verdict.

The physical layer is organized by explicit bridge packages:

* entropy and replica continuation;
* RT/QES geometry and generalized-entropy renormalization;
* Hilbert realization, adjoint, error algebra, and recovery maps;
* OCA/open--closed comparison with the derived chiral centre;
* Tomita--Takesaki, JLMS, tensor-network, chaos, and evaporation data.

The bar object ``B_X(A)`` occupies the twisting-coalgebra slot.  The
physical closed-sector slot is ``Z^der_ch(A)=C^bullet_ch(A,A)`` after a
derived-centre/BRST comparison.  Each function below either computes an
exact algebraic quantity or returns the bridge status beside its formal
candidate.

References:
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  thm:shadow-connection (higher_genus_modular_koszul.tex)
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
  Ryu-Takayanagi 2006 (hep-th/0603001)
  Engelhardt-Wall 2015 (1408.3203)
  Jafferis-Lewkowycz-Maldacena-Suh 2016 (1512.06431)
  Hayden-Preskill 2007 (0708.4025)
  Almheiri-Dong-Harlow 2015 (1411.7041)
  Pastawski-Yoshida-Harlow-Preskill 2015 (1503.06237)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Dict, List, Mapping, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, cancel, diff, expand,
    factorial, log, oo, pi, S, simplify, sqrt, symbols,
    sinh, cosh, exp, cos, sin,
    limit as sym_limit,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    kappa_wN,
    twist_operator_dimension,
    twist_dimension_total,
    renyi_entropy_scalar,
    von_neumann_entropy_scalar,
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


def physical_bridge_surfaces() -> Dict[str, Dict[str, object]]:
    """Return the independent packages required by physical conclusions."""
    return {
        'entropy': {
            'physical_conclusion': None,
            'status': 'CONDITIONAL_ON_REPLICA_STATE_AND_ANALYTIC_CONTINUATION',
            'required_data': (
                'state and regional algebra',
                'normalized replica partition functions',
                'analytic continuation near n=1',
            ),
        },
        'rt_qes': {
            'physical_conclusion': None,
            'status': 'CONDITIONAL_ON_ADS_CFT_RT_QES_BRIDGE',
            'required_data': (
                'bulk geometry and Newton constant',
                'area-operator comparison',
                'renormalized bulk entropy',
                'QES extremization and homology constraint',
            ),
        },
        'hilbert_qec': {
            'physical_conclusion': None,
            'status': 'CONDITIONAL_ON_HILBERT_ERROR_ALGEBRA_AND_RECOVERY_MAPS',
            'required_data': (
                'beta_T',
                'Hilbert realization and adjoint',
                'physical error algebra',
                'encoding and recovery channels',
            ),
        },
        'oca_bulk': {
            'physical_conclusion': None,
            'status': 'CONDITIONAL_ON_OCA_DERIVED_CENTRE_AND_SUBREGION_MAPS',
            'required_data': (
                'OCA/open-closed comparison',
                'derived-centre or BRST equivalence',
                'regional algebras and subregion maps',
            ),
        },
        'modular_jlms': {
            'physical_conclusion': None,
            'status': 'CONDITIONAL_ON_TOMITA_JLMS_OPERATOR_ALGEBRA_PACKAGE',
            'required_data': (
                'von Neumann algebra and cyclic separating state',
                'shadow-to-modular-operator comparison',
                'JLMS code subspace and area operator',
            ),
        },
        'tensor_network': {
            'physical_conclusion': None,
            'status': 'CONDITIONAL_ON_EXPLICIT_TENSORS_ISOMETRIES_AND_NORM_CONTROL',
            'required_data': (
                'network tensors and bond spaces',
                'isometry identities',
                'norm-convergent contraction',
            ),
        },
        'chaos_page': {
            'physical_conclusion': None,
            'status': 'CONDITIONAL_ON_DYNAMICS_OTOC_EVAPORATION_AND_ISLANDS',
            'required_data': (
                'thermal dynamics and OTOCs',
                'radiation algebra and evaporation model',
                'island/QES prescription',
            ),
        },
    }

# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------

c_sym = Symbol('c')
n_sym = Symbol('n', positive=True)
L_sym = Symbol('L', positive=True)
eps_sym = Symbol('epsilon', positive=True)
beta_sym = Symbol('beta', positive=True)
t_sym = Symbol('t')
s_sym = Symbol('s', positive=True)


# =========================================================================
# SECTION 1: RYU-TAKAYANAGI FROM COMPLEMENTARITY
# =========================================================================

def rt_from_kappa(kappa_val, log_ratio):
    r"""Return the scalar entropy candidate determined by ``kappa``.

    The genus-1 shadow obstruction gives obs_1 = kappa * lambda_1^FP
    with lambda_1^FP = 1/24.  The replica trick extracts the
    entanglement entropy from the n -> 1 limit of F_g on the
    n-fold branched cover Sigma_n.

    At genus 0 (the classical/area term):
        S_RT = (2*kappa/3) * log(L/epsilon)

    For Virasoro with kappa = c/2:
        S_RT = (c/3) * log(L/epsilon)

    Under the replica package this is the Calabrese--Cardy coefficient.
    Under the additional AdS3/CFT2 RT bridge it is compared with
    ``Area(gamma_A)/(4G_N)`` using ``1/(4G_N)=c/6``.

    Parameters
    ----------
    kappa_val : the modular characteristic kappa(A)
    log_ratio : ln(L/epsilon), the UV-regulated interval size

    >>> rt_from_kappa(Rational(1, 2), 1)  # c=1
    1/3
    >>> rt_from_kappa(Rational(13, 2), 1)  # c=13
    13/3
    >>> rt_from_kappa(Rational(13), 1)  # c=26
    26/3
    """
    kappa_val = Rational(kappa_val)
    return Rational(2) * kappa_val * log_ratio / 3


def rt_from_complementarity(c_val, log_ratio):
    r"""Return the Virasoro scalar candidate in central-charge variables.

    Theorem C gives the Lagrangian decomposition
        H_g = Q_g(A) + Q_g(A!)
    At genus 1, the scalar projection yields
        kappa(A) + kappa(A!) = 13  (for Virasoro)

    The RT entropy for one summand:
        S_RT(A) = (2*kappa(A)/3) * log(L/epsilon)
    The complementary:
        S_RT(A!) = (2*kappa(A!)/3) * log(L/epsilon)

    Sum: S_RT(A) + S_RT(A!) = (26/3) * log(L/epsilon)

    The physical RT and Page interpretations use their respective bridge
    packages.

    >>> rt_from_complementarity(Rational(1), 1)
    1/3
    >>> rt_from_complementarity(Rational(13), 1)
    13/3
    >>> rt_from_complementarity(Rational(26), 1)
    26/3
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    return rt_from_kappa(kappa, log_ratio)


def rt_area_identification(c_val):
    r"""Compare the two formal coefficients entering the RT dictionary.

    In 3d gravity dual to a 2d CFT:
        1/(4*G_N) = c / 6

    The RT formula S = Area/(4*G_N) with Area = 2*log(L/eps) gives:
        S = (c/6) * 2 * log(L/eps) = (c/3) * log(L/eps)

    The shadow identification: Area/(4*G_N) <-> (2*kappa/3) * log(L/eps)
    with kappa = c/2.

    The exact computation checks the coefficient identity.  Geometric
    identification is recorded as a conditional surface.

    >>> data = rt_area_identification(Rational(26))
    >>> data['inv_4GN']
    13/3
    >>> data['kappa']
    13
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    bridge = physical_bridge_surfaces()['rt_qes']
    return {
        'c': c_val,
        'kappa': kappa,
        'inv_4GN': c_val / 6,
        'area_coeff': Rational(2),  # Area = 2 * log(L/eps) for single interval
        'rt_coeff': Rational(2) * kappa / 3,  # S = (2*kappa/3) * log(L/eps)
        'cc_coeff': c_val / 3,  # S = (c/3) * log(L/eps)
        'identification': 'Area/(4G_N) = (2*kappa/3) * log(L/eps)',
        'consistent': (c_val / 6 * 2 == 2 * kappa / 3),
        'coefficient_identity': (c_val / 6 * 2 == 2 * kappa / 3),
        'physical_rt_identification': bridge['physical_conclusion'],
        'physical_rt_status': bridge['status'],
        'physical_rt_required_data': bridge['required_data'],
    }


def rt_three_derivations(c_val, log_ratio=1):
    r"""Three algebraic routes to the same scalar coefficient.

    Path 1: From kappa = c/2 directly.
    Path 2: From the replica trick (n -> 1 limit).
    Path 3: From the complementarity sum and self-consistency.

    Agreement verifies the internal normalization.  The RT interpretation
    is supplied by the geometric bridge.

    >>> data = rt_three_derivations(Rational(26))
    >>> data['path1'] == data['path2'] == data['path3']
    True
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)

    # Path 1: direct from kappa
    path1 = rt_from_kappa(kappa, log_ratio)

    # Path 2: replica trick
    # S_n = (kappa/3)(1+1/n) log(L/eps)
    # lim_{n->1} S_n = (2*kappa/3) log(L/eps)
    path2 = von_neumann_entropy_scalar(kappa, log_ratio)

    # Path 3: complementarity
    # S(A) + S(A!) = (26/3) log(L/eps), so S(A) = (c/3) log(L/eps)
    kappa_dual = kappa_virasoro(26 - c_val)
    total = Rational(2) * (kappa + kappa_dual) / 3 * log_ratio
    path3 = total - von_neumann_entropy_scalar(kappa_dual, log_ratio)

    bridge = physical_bridge_surfaces()['rt_qes']
    return {
        'c': c_val,
        'kappa': kappa,
        'path1': path1,
        'path2': path2,
        'path3': path3,
        'all_agree': (path1 == path2 == path3),
        'physical_rt': bridge['physical_conclusion'],
        'physical_rt_status': bridge['status'],
    }


# =========================================================================
# SECTION 2: QUANTUM EXTREMAL SURFACE
# =========================================================================

def quantum_extremal_surface(kappa_val, log_ratio, genus_corrections=3):
    r"""Compute a formal shadow expansion for a QES comparison.

    The area term is the scalar shadow (genus-0):
        S_area = (2*kappa/3) * log(L/eps)

    The bulk entropy receives contributions from:
    (a) Higher-genus corrections: F_g * correction_g for g >= 1
    (b) Higher-arity shadow corrections: delta_S_r for r >= 3

    S_gen = S_area + S_bulk
    S_bulk = sum_{g=1}^{g_max} F_g(A) * quantum_correction_g

    The factors ``1/(12g)`` below define the formal comparison model.
    A physical generalized entropy uses the replica/QES bridge and its
    renormalized bulk entropy.

    >>> qes = quantum_extremal_surface(Rational(13, 2), 1)
    >>> qes['S_area']
    13/3
    >>> qes['S_area'] > 0
    True
    """
    kappa_val = Rational(kappa_val)
    S_area = Rational(2) * kappa_val * log_ratio / 3

    # Higher-genus corrections from F_g = kappa * lambda_g^FP
    bulk_corrections = []
    S_bulk_total = Rational(0)
    for g in range(1, genus_corrections + 1):
        F_g = scalar_free_energy(kappa_val, g)
        # Formal comparison coefficient chosen for this finite model.
        # A replica derivation belongs to the QES bridge package.
        correction = F_g / (12 * g)
        bulk_corrections.append({
            'genus': g,
            'F_g': F_g,
            'lambda_g': faber_pandharipande(g),
            'correction': correction,
        })
        S_bulk_total += correction

    bridge = physical_bridge_surfaces()['rt_qes']
    return {
        'kappa': kappa_val,
        'S_area': S_area,
        'S_bulk': S_bulk_total,
        'S_gen': S_area + S_bulk_total,
        'formal_scalar_candidate': S_area,
        'formal_shadow_correction': S_bulk_total,
        'formal_generalized_entropy_candidate': S_area + S_bulk_total,
        'genus_corrections': bulk_corrections,
        'area_dominance': S_area / (S_area + abs(S_bulk_total)) if S_bulk_total != 0 else Rational(1),
        'physical_qes': bridge['physical_conclusion'],
        'physical_qes_status': bridge['status'],
        'physical_qes_required_data': bridge['required_data'],
        'note': (
            'The displayed terms form a shadow-side comparison ansatz.  '
            'The QES bridge supplies the area operator, renormalized bulk '
            'entropy, and extremization problem.'
        ),
    }


def qes_area_vs_bulk_ratio(kappa_val, log_ratio=1, g_max=5):
    r"""Ratio in the formal shadow-correction model.

    Both terms are linear in ``kappa`` in this model, so their ratio is
    invariant under nonzero rescaling of ``kappa``.  This checks the
    internal normalization of the chosen coefficients.

    >>> ratio = qes_area_vs_bulk_ratio(Rational(13), 1)
    >>> ratio['ratio'] < Rational(1, 100)
    True
    """
    kappa_val = Rational(kappa_val)
    S_area = Rational(2) * kappa_val * log_ratio / 3
    S_bulk = Rational(0)
    for g in range(1, g_max + 1):
        F_g = scalar_free_energy(kappa_val, g)
        S_bulk += F_g / (12 * g)

    ratio = abs(S_bulk) / S_area if S_area != 0 else oo
    bridge = physical_bridge_surfaces()['rt_qes']
    return {
        'kappa': kappa_val,
        'S_area': S_area,
        'S_bulk': S_bulk,
        'ratio': ratio,
        'formal_small_correction': bool(ratio < Rational(1, 10)),
        'kappa_scale_invariant': True,
        'semiclassical': None,
        'physical_qes': bridge['physical_conclusion'],
        'physical_qes_status': bridge['status'],
    }


def qes_shift_genus1(kappa_val, log_ratio=1):
    r"""Record the symmetry candidate for a genus-one QES shift.

    A physical QES position is determined by stationarity:
        d/dx [S_area(x) + S_bulk(x)] = 0

    The formal normalized genus-one coefficient is
    ``F_1/kappa=1/24``.  Parity gives the zero symmetric candidate.

    >>> shift = qes_shift_genus1(Rational(13, 2))
    >>> shift['formal_symmetric_shift']
    0
    """
    kappa_val = Rational(kappa_val)
    F_1 = scalar_free_energy(kappa_val, 1)

    bridge = physical_bridge_surfaces()['rt_qes']
    return {
        'kappa': kappa_val,
        'F_1': F_1,
        'formal_symmetric_shift': 0,
        'formal_asymmetric_scale': F_1 / kappa_val if kappa_val != 0 else None,
        'symmetric_shift': None,
        'physical_qes_shift': bridge['physical_conclusion'],
        'physical_qes_status': bridge['status'],
        'note': (
            'Parity fixes the formal symmetric candidate.  The physical shift '
            'is obtained from the renormalized generalized-entropy functional.'
        ),
    }


# =========================================================================
# SECTION 3: KNILL-LAFLAMME FROM LAGRANGIAN ISOTROPY
# =========================================================================

def knill_laflamme_from_complementarity(genus=1):
    r"""Return the Lagrangian input and the physical KL obligation.

    Theorem C gives the Lagrangian decomposition:
        H_g = Q_g(A) + Q_g(A!)

    The Verdier pairing <,>_D satisfies:
        <sigma(v), sigma(w)>_D = -<v, w>_D

    For v, w in Q_g(A) (sigma-eigenvalue +1):
        <v, w>_D = <sigma(v), sigma(w)>_D = -<v, w>_D => <v, w>_D = 0

    This is Verdier isotropy of one Lagrangian summand.

    The Knill-Laflamme condition for quantum error correction:
        P_C E_a^dag E_b P_C = c_{ab} P_C
    requires that error operators act proportionally to the identity
    on the code subspace.

    A one-dimensional Hilbert realization satisfies the compression
    lemma automatically.  The physical KL statement additionally uses
    the adjoint, error algebra, and recovery maps.

    >>> kl = knill_laflamme_from_complementarity(1)
    >>> kl['kl_satisfied'] is None
    True
    >>> kl['mechanism']
    'one-dimensional compression lemma'
    """
    bridge = physical_bridge_surfaces()['hilbert_qec']
    if genus == 1:
        return {
            'genus': 1,
            'dim_Q_g': 1,
            'kl_satisfied': bridge['physical_conclusion'],
            'formal_compression_lemma': True,
            'mechanism': 'one-dimensional compression lemma',
            'proof': (
                'After a Hilbert realization with dim Q_1(A)=1, every '
                'compressed error product is scalar on that line.'
            ),
            'physical_kl_status': bridge['status'],
            'physical_kl_required_data': bridge['required_data'],
        }
    else:
        return {
            'genus': genus,
            'dim_Q_g': None,
            'dimension_status': 'FAMILY_AND_GENUS_COMPUTATION_REQUIRED',
            'kl_satisfied': bridge['physical_conclusion'],
            'mechanism': 'Hilbert/error-algebra analysis at genus g',
            'proof': (
                'The Verdier Lagrangian splitting supplies algebraic isotropy. '
                'The KL matrix is computed from the realized error products.'
            ),
            'isotropy_proved': True,
            'isotropy_status': 'THEOREM_C_LAGRANGIAN_PACKAGE',
            'isotropy_note': (
                'Theorem C supplies Verdier isotropy at the algebraic level.'
            ),
            'physical_kl_status': bridge['status'],
            'physical_kl_required_data': bridge['required_data'],
        }


def kl_error_algebra_structure(family='virasoro'):
    r"""Return the candidate dual-family shadow and error-algebra obligation.

    The complementary Verdier summand is algebraic data.  A physical
    error algebra is selected after the Hilbert realization and adjoint.

    >>> ea = kl_error_algebra_structure('virasoro')
    >>> ea['dual_family']
    'Vir_{26-c}'
    >>> ea['error_space']
    'Q_g(Vir_{26-c})'
    """
    family_data = {
        'heisenberg': {
            'dual_family': 'H_{-k} (negative level)',
            'error_space': 'Q_g(H_{-k})',
            'shadow_class': 'G',
            'arity_profile': 'scalar arity only',
        },
        'affine': {
            'dual_family': 'g_{-k-2h^v} (Feigin-Frenkel dual)',
            'error_space': 'Q_g(g_{-k-2h^v})',
            'shadow_class': 'L',
            'arity_profile': 'scalar and cubic arities',
        },
        'betagamma': {
            'dual_family': 'betagamma_{1-lambda}',
            'error_space': 'Q_g(betagamma_{1-lambda})',
            'shadow_class': 'C',
            'arity_profile': 'scalar, cubic, and quartic arities',
        },
        'virasoro': {
            'dual_family': 'Vir_{26-c}',
            'error_space': 'Q_g(Vir_{26-c})',
            'shadow_class': 'M',
            'arity_profile': 'unbounded arity tower',
        },
    }

    fam_key = family.lower()
    if fam_key not in family_data:
        fam_key = 'virasoro'

    bridge = physical_bridge_surfaces()['hilbert_qec']
    return {
        **family_data[fam_key],
        'physical_error_algebra': bridge['physical_conclusion'],
        'physical_error_algebra_status': bridge['status'],
        'physical_error_algebra_required_data': bridge['required_data'],
    }


def kl_conditions_by_genus(kappa_val, g_max=4):
    r"""Return formal compression data and physical KL status by genus.

    Returns the KL status at each genus level, showing the
    transition from automatic (genus 1) to non-trivial (genus >= 2).

    >>> data = kl_conditions_by_genus(Rational(13, 2), 3)
    >>> data[1]['status']
    'PHYSICAL_BRIDGE_REQUIRED'
    >>> data[2]['status']
    'PHYSICAL_BRIDGE_REQUIRED'
    """
    result = {}
    bridge = physical_bridge_surfaces()['hilbert_qec']
    for g in range(1, g_max + 1):
        if g == 1:
            result[g] = {
                'dim_Q_g': 1,
                'formal_compression_lemma': True,
                'kl_satisfied': bridge['physical_conclusion'],
                'status': 'PHYSICAL_BRIDGE_REQUIRED',
                'physical_kl_status': bridge['status'],
                'note': 'The realized one-dimensional compression is scalar.',
            }
        else:
            # dim Q_g grows with g; exact value depends on family
            F_g = scalar_free_energy(kappa_val, g)
            result[g] = {
                'dim_Q_g': None,
                'dimension_status': 'FAMILY_AND_GENUS_COMPUTATION_REQUIRED',
                'F_g': F_g,
                'kl_satisfied': bridge['physical_conclusion'],
                'status': 'PHYSICAL_BRIDGE_REQUIRED',
                'physical_kl_status': bridge['status'],
                'isotropy': 'proved (Lagrangian)',
                'note': f'Genus {g} uses the realized error-product matrix.',
            }
    return result


# =========================================================================
# SECTION 4: SHADOW DEPTH = CODE STRUCTURE
# =========================================================================

def shadow_depth_code_parameters(family):
    r"""Return the arity profile and physical-code obligation.

    The shadow depth ``r_max(A)`` records the supported arity range of
    the obstruction tower.  Hilbert-space parameters ``[n,k,d]`` arise
    only after a physical code realization.

    Class G supports the scalar arity.  Class L adds the cubic arity;
    class C adds cubic and quartic arities; class M has an unbounded
    arity tower.  The filtered MC package governs formal extension
    between these levels.

    >>> p = shadow_depth_code_parameters('heisenberg')
    >>> p['n_logical'] is None
    True
    >>> p['higher_arity_slots']
    0
    >>> p['code_type']
    'arity_profile_G'
    """
    cls = shadow_depth_class(family)
    bridge = physical_bridge_surfaces()['hilbert_qec']

    code_data = {
        'G': {
            'shadow_class': 'G',
            'r_max': 2,
            'n_logical': None,
            'n_physical': None,
            'n_redundancy': 0,
            'higher_arity_slots': 0,
            'code_type': 'arity_profile_G',
            'code_notation': None,
            'formal_extension_arities': [],
        },
        'L': {
            'shadow_class': 'L',
            'r_max': 3,
            'n_logical': None,
            'n_physical': None,
            'n_redundancy': 1,
            'higher_arity_slots': 1,
            'code_type': 'arity_profile_L',
            'code_notation': None,
            'formal_extension_arities': ['arity 3 (cubic shadow C)'],
        },
        'C': {
            'shadow_class': 'C',
            'r_max': 4,
            'n_logical': None,
            'n_physical': None,
            'n_redundancy': 2,
            'higher_arity_slots': 2,
            'code_type': 'arity_profile_C',
            'code_notation': None,
            'formal_extension_arities': ['arity 3 (cubic)', 'arity 4 (quartic Q)'],
        },
        'M': {
            'shadow_class': 'M',
            'r_max': -1,  # infinite
            'n_logical': None,
            'n_physical': None,
            'n_redundancy': -1,
            'higher_arity_slots': -1,
            'code_type': 'arity_profile_M',
            'code_notation': None,
            'formal_extension_arities': ['all arities r >= 3'],
        },
    }

    return {
        **code_data.get(cls, code_data['M']),
        'recovery_channels': bridge['physical_conclusion'],
        'physical_code_parameters': bridge['physical_conclusion'],
        'physical_code_status': bridge['status'],
        'physical_code_required_data': bridge['required_data'],
    }


def code_rate_by_class(family):
    r"""Return the physical code rate after a Hilbert realization.

    The algebraic Lagrangian fraction is ``1/2`` in finite-dimensional
    perfect symplectic models.  A physical rate ``k/n`` uses an explicit
    Hilbert code and channel.

    >>> code_rate_by_class('heisenberg') is None
    True
    >>> code_rate_by_class('virasoro') is None
    True
    """
    return None


def code_distance_effective(family):
    r"""Return physical code distance after specifying an error model.

    Shadow depth supplies an arity-span proxy.  Distance is defined from
    the weights of logical operators in the realized physical error model.

    >>> code_distance_effective('heisenberg') is None
    True
    >>> code_distance_effective('affine') is None
    True
    >>> code_distance_effective('betagamma') is None
    True
    >>> code_distance_effective('virasoro') is None
    True
    """
    return None


# =========================================================================
# SECTION 5: ENTANGLEMENT WEDGE RECONSTRUCTION FROM THEOREM A
# =========================================================================

def entanglement_wedge_from_bar_cobar(
    family='virasoro',
    *,
    algebra_id: Optional[str] = None,
    quadratic_certificate: Optional[Mapping[str, object]] = None,
    completed: bool = False,
    chain_package_verified: bool = False,
    **kwargs,
):
    r"""Algebraic reconstruction skeleton from the bar-cobar adjunction.

    Theorem A is ``epsilon_A: Omega_X B_X(A) -> A`` in the enhanced
    pro-nilpotent Ran category.  Theorem B is the chosen-presentation
    comparison ``q_A: A^i -> B_X(A)`` and its adjoint ``p_A``.

    The bar complex ``B_X(A)`` is the twisting/coupling coalgebra.
    The physical closed-sector slot is the derived chiral centre after
    an OCA/BRST comparison.

    Reading this algebraic skeleton as an entanglement wedge is recorded
    on the independent OCA bridge surface.

    >>> ew = entanglement_wedge_from_bar_cobar('virasoro', c=13)
    >>> ew['universal_reconstruction']
    True
    >>> ew['reconstruction_map']
    'epsilon_A: Omega_X B_X(A) -> A'
    >>> ew['exact_reconstruction'] is None
    True
    """
    algebraic = algebraic_code_parameters(
        family,
        algebra_id=algebra_id,
        quadratic_certificate=quadratic_certificate,
        completed=completed,
        chain_package_verified=chain_package_verified,
        **kwargs,
    )
    bridge = physical_bridge_surfaces()['oca_bulk']

    return {
        'family': family,
        'algebra_id': algebraic['algebra_id'],
        'is_koszul': algebraic['quadratic_koszul'],
        'universal_reconstruction': algebraic['universal_reconstruction'],
        'universal_reconstruction_status': algebraic[
            'universal_reconstruction_status'
        ],
        'exact_reconstruction': algebraic['exact_quadratic_recovery'],
        'exact_reconstruction_status': algebraic['exact_recovery_status'],
        'reconstruction_map': 'epsilon_A: Omega_X B_X(A) -> A',
        'encoding_map': 'B_X (bar object assignment)',
        'adjunction': 'Theorem A enhanced-Ran reconstruction',
        'quadratic_comparison': 'q_A: A^i -> B_X(A)',
        'quadratic_adjoint': 'p_A: Omega_X(A^i) -> A',
        'quadratic_obstruction': 'Cone(q_A)',
        'wedge_coverage': bridge['physical_conclusion'],
        'physical_bulk_claim': bridge['physical_conclusion'],
        'physical_entanglement_wedge': bridge['physical_conclusion'],
        'physical_entanglement_wedge_status': bridge['status'],
        'physical_entanglement_wedge_required_data': bridge['required_data'],
        'bar_slot': 'B_X(A): twisting/coupling coalgebra',
        'bulk_slot': (
            'Z^der_ch(A) = ChirHoch^*(A,A) after derived-centre/BRST comparison'
        ),
        'shadow_class': shadow_depth_class(family),
        'theorem_a_surface': algebraic['theorem_a_surface'],
        'theorem_b_surface': algebraic['theorem_b_surface'],
        'fixed_coalgebra_surface': algebraic['fixed_coalgebra_surface'],
        'verdier_dual_surface': algebraic['verdier_dual_surface'],
        'derived_center_surface': algebraic['derived_center_surface'],
        'note': (
            'Theorem A reconstructs A from its full bar object.  Theorem B '
            'tests quadratic compression through Cone(q_A).  The OCA bridge '
            'connects the derived centre to a physical regional bulk algebra.'
        ),
    }


def subregion_duality_check(
    family='virasoro',
    *,
    theorem_c_package_verified: bool = False,
    **kwargs,
):
    r"""Verify algebraic subregion complementarity.

    Under the Theorem C package, the two Verdier-complementary shadow
    summands give
        Q_g(A) + Q_g(A!) = H_g

    A physical subregion-duality statement uses the OCA, regional-algebra,
    and recovery-map comparison.

    >>> check = subregion_duality_check('virasoro')
    >>> check['subregion_duality'] is None
    True
    """
    bridge = physical_bridge_surfaces()['oca_bulk']

    return {
        'family': family,
        'algebraic_complementarity': (
            True if theorem_c_package_verified else None
        ),
        'algebraic_complementarity_status': (
            'CERTIFIED' if theorem_c_package_verified else 'THEOREM_C_PACKAGE_REQUIRED'
        ),
        'subregion_duality': bridge['physical_conclusion'],
        'subregion_duality_status': bridge['status'],
        'subregion_duality_required_data': bridge['required_data'],
        'mechanism': 'Lagrangian decomposition (Theorem C)',
        'wedge_A': 'Q_g(A)',
        'wedge_Ac': 'Q_g(A!)',
        'union': 'H_g = Q_g(A) + Q_g(A!)',
        'note': (
            'Theorem C supplies algebraic Lagrangian completeness under its '
            'package.  The OCA and regional-algebra maps supply subregion duality.'
        ),
    }


def greedy_algorithm_from_bar_filtration(
    family='virasoro', *, convergence_verified: bool = False
):
    r"""Return the bar-filtration layer profile and decoder obligation.

    The bar filtration F^p B(A) provides a layered structure
    analogous to the layers of a MERA tensor network.
    The greedy algorithm processes layers from boundary inward:

    Layer p = 1: arity-2 data (kappa, scalar shadow)
    Layer p = 2: arity-3 data (cubic shadow C)
    Layer p = 3: arity-4 data (quartic shadow Q)
    ...
    Layer p = r_max - 1: final supported layer at finite shadow depth

    The filtered MC package governs formal extension between layers.
    A physical greedy decoder uses the Hilbert/error-algebra bridge.

    >>> ga = greedy_algorithm_from_bar_filtration('heisenberg')
    >>> ga['n_layers']
    1
    >>> ga['terminates']
    True
    """
    cls = shadow_depth_class(family)
    depth_map = {'G': 2, 'L': 3, 'C': 4, 'M': -1}
    r_max = depth_map[cls]

    if r_max > 0:
        n_layers = r_max - 1
        terminates = True
    else:
        n_layers = -1
        terminates = False

    bridge = physical_bridge_surfaces()['hilbert_qec']

    return {
        'family': family,
        'shadow_class': cls,
        'r_max': r_max,
        'n_layers': n_layers,
        'terminates': terminates,
        'convergent': True if convergence_verified else None,
        'convergence_status': (
            'CERTIFIED' if convergence_verified else 'CONVERGENCE_PACKAGE_REQUIRED'
        ),
        'physical_greedy_decoder': bridge['physical_conclusion'],
        'physical_greedy_decoder_status': bridge['status'],
        'layers': (
            [f'Layer {p}: arity-{p+1} shadow' for p in range(1, min(n_layers + 1, 5))]
            if n_layers > 0 else
            ['Layer p: arity-(p+1) shadow for all p >= 1']
        ),
    }


# =========================================================================
# SECTION 6: MODULAR FLOW FROM THE SHADOW CONNECTION
# =========================================================================

def modular_hamiltonian_from_shadow(kappa_val, log_ratio=1):
    r"""Return the shadow scalar and the modular-operator obligation.

    The Tomita-Takesaki modular operator is Delta = exp(-K) where
    K is the modular Hamiltonian.

    For a single interval [0, L] in the vacuum state:
        K = (2*pi) * integral_0^L dx * w(x) * T(x)
    where w(x) = x*(L-x)/L is the entanglement weight.

    The scalar projection gives:
        K^{scalar} = (2*kappa/3) * log(L/epsilon)

    The comparison with the modular Hamiltonian uses a von Neumann
    algebra, cyclic separating state, and shadow-to-Tomita map.

    The shadow connection has parallel transport
    ``Phi(t)=sqrt(Q(t)/Q(0))``.  The modular bridge tests its comparison
    with Tomita--Takesaki evolution.

    >>> mh = modular_hamiltonian_from_shadow(Rational(13, 2))
    >>> mh['K_scalar']
    13/3
    """
    kappa_val = Rational(kappa_val)
    K_scalar = Rational(2) * kappa_val * log_ratio / 3

    bridge = physical_bridge_surfaces()['modular_jlms']
    return {
        'kappa': kappa_val,
        'K_scalar': K_scalar,
        'shadow_scalar_candidate': K_scalar,
        'S_EE': None,
        'physical_modular_hamiltonian': bridge['physical_conclusion'],
        'physical_modular_status': bridge['status'],
        'physical_modular_required_data': bridge['required_data'],
        'modular_temperature': None,
        'entanglement_weight': 'w(x) = x*(L-x)/L',
        'shadow_connection': 'nabla^sh = d - Q_L\'/(2*Q_L) dt',
        'parallel_transport': 'Phi(t) = sqrt(Q(t)/Q(0))',
    }


def modular_flow_from_connection(kappa_val, S4_val=0, t_val=0):
    r"""Compute the formal shadow-connection velocity.

    The shadow metric ``Q_L(t)`` defines the connection coefficient
        v(t) = -Q'(t) / (2*Q(t))

    At t = 0: v(0) = -3*alpha / kappa (if alpha != 0)
    For the standard case alpha = 0: v(0) = 0 (stationary point).

    A comparison with the Tomita--Takesaki automorphism group is carried
    by the modular bridge surface.

    For the formal Virasoro line, ``Delta=8*kappa*S_4`` distinguishes
    the stationary and nonstationary shadow-connection candidates.

    >>> flow = modular_flow_from_connection(Rational(13, 2))
    >>> flow['v_at_0']
    0
    """
    kappa_val = Rational(kappa_val)
    S4_val = Rational(S4_val)

    # Shadow metric at t = 0: Q(0) = (2*kappa)^2 = 4*kappa^2
    Q_0 = 4 * kappa_val**2
    # Q'(0) = 0 (for alpha = 0)
    Q_prime_0 = Rational(0)

    if Q_0 != 0:
        v_0 = -Q_prime_0 / (2 * Q_0)
    else:
        v_0 = None

    # Critical discriminant
    Delta_crit = 8 * kappa_val * S4_val

    bridge = physical_bridge_surfaces()['modular_jlms']
    return {
        'kappa': kappa_val,
        'S4': S4_val,
        'Q_0': Q_0,
        'Delta_crit': Delta_crit,
        'v_at_0': v_0,
        'flow_type': bridge['physical_conclusion'],
        'shadow_connection_type': (
            'stationary' if Delta_crit == 0 else 'nonstationary'
        ),
        'monodromy': -1,  # Koszul sign
        'physical_modular_flow': bridge['physical_conclusion'],
        'physical_modular_flow_status': bridge['status'],
    }


def modular_temperature(kappa_val, beta=None):
    r"""Return the Rindler temperature candidate and bridge status.

    The entanglement temperature T_ent = 1 / beta_ent is defined by:
        S_EE = (c/3) * log(L/epsilon) = K / T_ent

    In the Rindler approximation: T_ent = 1/(2*pi*a) where a is
    the proper acceleration.  For a single interval:
        T_ent = 1/(2*pi) (in natural units with L = 1)

    The Unruh effect identification: T_Unruh = a/(2*pi).

    >>> mt = modular_temperature(Rational(13, 2))
    >>> mt['rindler_temperature_candidate']
    1/(2*pi)
    """
    kappa_val = Rational(kappa_val)

    bridge = physical_bridge_surfaces()['modular_jlms']
    return {
        'kappa': kappa_val,
        'rindler_temperature_candidate': 1 / (2 * pi),
        'rindler_beta_candidate': 2 * pi,
        'T_ent': bridge['physical_conclusion'],
        'beta_ent': bridge['physical_conclusion'],
        'physical_temperature_status': bridge['status'],
        'K_scalar': Rational(2) * kappa_val / 3,
        'unruh_candidate': 'T_Unruh = a/(2*pi) (proper acceleration a)',
    }


# =========================================================================
# SECTION 7: JLMS FORMULA FROM COMPLEMENTARITY
# =========================================================================

def jlms_formula(kappa_val, log_ratio=1):
    r"""Return the shadow-side scalar candidate for a JLMS comparison.

    Jafferis-Lewkowycz-Maldacena-Suh (2016):
        S(rho_A || sigma_A) = S(rho_a || sigma_a) + <K_A>_rho - <K_A>_sigma

    where:
    - rho_A, sigma_A: boundary states
    - rho_a, sigma_a: bulk states in the entanglement wedge
    - K_A: bulk modular Hamiltonian = Area operator / (4*G_N) + K_bulk

    The shadow side supplies the scalar candidate
    ``(2*kappa/3)log(L/epsilon)`` and the displayed formal correction.

    Theorem C supplies an algebraic Lagrangian splitting.  JLMS requires
    the operator-algebraic code subspace, area operator, and relative
    entropy comparison.

    >>> jlms = jlms_formula(Rational(13, 2))
    >>> jlms['area_contribution']
    13/3
    >>> jlms['decomposition_valid'] is None
    True
    """
    kappa_val = Rational(kappa_val)
    area_contrib = Rational(2) * kappa_val * log_ratio / 3

    # Higher-genus bulk correction (leading order: genus 1)
    F_1 = scalar_free_energy(kappa_val, 1)
    bulk_correction_leading = F_1 / 12

    bridge = physical_bridge_surfaces()['modular_jlms']
    return {
        'kappa': kappa_val,
        'area_contribution': area_contrib,
        'bulk_correction_leading': bulk_correction_leading,
        'total_modular_hamiltonian': bridge['physical_conclusion'],
        'decomposition_valid': bridge['physical_conclusion'],
        'scalar_decomposition_candidate': area_contrib + bulk_correction_leading,
        'physical_jlms': bridge['physical_conclusion'],
        'physical_jlms_status': bridge['status'],
        'physical_jlms_required_data': bridge['required_data'],
        'mechanism': 'Theorem C Lagrangian input plus JLMS bridge',
        'formula': (
            'S(rho_A||sigma_A) = S(rho_a||sigma_a) + <K_A>_rho - <K_A>_sigma '
            'where K_A = (2*kappa/3)*log(L/eps) + bulk_corrections'
        ),
    }


def jlms_relative_entropy_bound(kappa_val, log_ratio=1):
    r"""Record the relative-entropy theorem and JLMS bridge obligation.

    S(rho || sigma) >= 0 (positivity of relative entropy) combined
    with JLMS gives:
        <K_A>_rho - <K_A>_sigma >= -(S(rho_a || sigma_a))

    Positivity applies after the states and regional von Neumann algebras
    are specified.  A bound on shadow corrections additionally requires
    the JLMS comparison map.

    >>> bound = jlms_relative_entropy_bound(Rational(13, 2))
    >>> bound['positivity'] is None
    True
    """
    kappa_val = Rational(kappa_val)

    bridge = physical_bridge_surfaces()['modular_jlms']
    return {
        'kappa': kappa_val,
        'positivity': bridge['physical_conclusion'],
        'relative_entropy_positivity_theorem': (
            'S(rho||sigma) >= 0 for specified normalized states'
        ),
        'shadow_correction_bound': None,
        'physical_jlms_status': bridge['status'],
        'mechanism': 'operator-algebraic relative entropy plus JLMS bridge',
    }


def jlms_complementarity_consistency(c_val, log_ratio=1):
    r"""Check the Virasoro scalar sum used by a JLMS comparison.

    For Virasoro at c:
        K_A = (2*kappa(c)/3)*log(L/eps) (area)
        K_{A!} = (2*kappa(26-c)/3)*log(L/eps) (complementary area)
        K_A + K_{A!} = (26/3)*log(L/eps) (complementarity sum)

    The computation below verifies only the scalar coefficient identity.

    >>> data = jlms_complementarity_consistency(Rational(13))
    >>> data['K_sum']
    26/3
    >>> data['scalar_identity_holds']
    True
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26 - c_val)

    K_A = Rational(2) * kappa * log_ratio / 3
    K_Ac = Rational(2) * kappa_dual * log_ratio / 3

    bridge = physical_bridge_surfaces()['modular_jlms']
    scalar_identity = K_A + K_Ac == Rational(26, 3) * log_ratio
    return {
        'c': c_val,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'K_A': K_A,
        'K_Ac': K_Ac,
        'K_sum': K_A + K_Ac,
        'expected_sum': Rational(26, 3) * log_ratio,
        'scalar_identity_holds': scalar_identity,
        'consistent': bridge['physical_conclusion'],
        'physical_jlms_status': bridge['status'],
    }


# =========================================================================
# SECTION 8: TENSOR NETWORK (BAR COMPLEX AS MERA)
# =========================================================================

def bar_complex_as_tensor_network(
    family='virasoro',
    *,
    algebra_id: Optional[str] = None,
    quadratic_certificate: Optional[Mapping[str, object]] = None,
    **kwargs,
):
    r"""Return the bar filtration and tensor-network bridge obligation.

    The components of ``B(A)=direct_sum_{g,n} B^{(g,n)}(A)`` provide
    arity-indexed multilinear data:

    - Each tensor B^{(g,n)}: n-valent vertex with g loops
    - The bar filtration F^p: p layers from boundary to bulk
    - The differential d_bar: contraction of edges
    - The coproduct Delta: splitting of vertices

    The proposed MERA comparison assigns:
    - MERA layers <-> bar filtration layers (arity)
    - Disentanglers <-> bar differential (collision)
    - Isometries <-> cobar reconstruction

    The precise algebraic structure is a coalgebra with coproduct.  Its
    layers carry the arity index, and the proposed RG analogy uses the
    arity filtration.  A literal MERA realization belongs to the tensor
    network bridge surface.

    >>> tn = bar_complex_as_tensor_network('virasoro')
    >>> tn['n_layers']
    'infinite (class M)'
    >>> tn['is_exact'] is None
    True
    """
    cls = shadow_depth_class(family)
    depth_map = {'G': 2, 'L': 3, 'C': 4, 'M': -1}
    r_max = depth_map[cls]

    if r_max > 0:
        n_layers = str(r_max - 1)
    else:
        n_layers = 'infinite (class M)'

    algebraic = algebraic_code_parameters(
        family,
        algebra_id=algebra_id,
        quadratic_certificate=quadratic_certificate,
        **kwargs,
    )
    bridge = physical_bridge_surfaces()['tensor_network']
    return {
        'family': family,
        'algebra_id': algebraic['algebra_id'],
        'shadow_class': cls,
        'n_layers': n_layers,
        'is_exact': algebraic['exact_quadratic_recovery'],
        'exact_contraction_status': algebraic['exact_recovery_status'],
        'universal_reconstruction': algebraic['universal_reconstruction'],
        'theorem_a_surface': algebraic['theorem_a_surface'],
        'theorem_b_surface': algebraic['theorem_b_surface'],
        'tensor_type': 'bar complex B^{(g,n)}(A)',
        'filtration': 'arity filtration (bar filtration)',
        'differential': 'bar differential d_bar (collision/contraction)',
        'reconstruction': 'epsilon_A: Omega_X B_X(A) -> A (Theorem A)',
        'physical_tensor_network': bridge['physical_conclusion'],
        'tensor_network_status': bridge['status'],
        'tensor_network_required_data': bridge['required_data'],
        'analogy': {
            'MERA_layer': 'bar filtration layer (arity p)',
            'MERA_disentangler': 'bar differential (collision limit)',
            'MERA_isometry': 'cobar functor (reconstruction)',
            'MERA_RG': 'arity filtration candidate',
        },
    }


def bond_dimension_from_shadow(kappa_val, r):
    r"""Return a normalized shadow-coefficient ratio candidate.

    The normalized shadow ratio is

        chi_r ~ |S_r| / |S_2| = |S_r| / kappa

    A family-specific decay estimate may take the form
        chi_r ~ rho^r for class M algebras.

    Conversion of this ratio into a bond dimension belongs to the
    explicit tensor-network package.

    >>> bd = bond_dimension_from_shadow(Rational(13, 2), 2)
    >>> bd['normalized_shadow_ratio']
    1
    """
    kappa_val = Rational(kappa_val)

    if r == 2:
        chi = Rational(1)  # normalized
    elif r >= 3 and kappa_val != 0:
        # For the scalar shadow on a single line, the ratio
        # S_r / kappa is given by the shadow generating function.
        # At leading order: chi_r ~ rho^{r-2}
        # We compute the abstract ratio here.
        chi = None  # requires the family-specific coefficient S_r
    else:
        chi = None

    bridge = physical_bridge_surfaces()['tensor_network']
    return {
        'kappa': kappa_val,
        'arity': r,
        'normalized_shadow_ratio': chi,
        'chi': bridge['physical_conclusion'],
        'bond_dimension': bridge['physical_conclusion'],
        'bond_dimension_status': bridge['status'],
        'note': 'S_r / kappa is a shadow coefficient ratio.',
    }


def mera_depth_vs_shadow_depth():
    r"""Compare arity-layer counts with a future MERA realization.

    The arity filtration has one, two, three, or unbounded layers for
    classes G, L, C, and M.  The tensor-network bridge determines the
    MERA depth and convergence.

    >>> data = mera_depth_vs_shadow_depth()
    >>> data['G']['arity_layers']
    1
    >>> data['M']['arity_layers']
    'unbounded'
    """
    bridge = physical_bridge_surfaces()['tensor_network']
    return {
        'G': {'arity_layers': 1, 'mera_depth': None, 'convergent': None,
              'status': bridge['status']},
        'L': {'arity_layers': 2, 'mera_depth': None, 'convergent': None,
              'status': bridge['status']},
        'C': {'arity_layers': 3, 'mera_depth': None, 'convergent': None,
              'status': bridge['status']},
        'M': {
            'arity_layers': 'unbounded',
            'mera_depth': None,
            'convergent': None,
            'status': bridge['status'],
        },
    }


# =========================================================================
# SECTION 9: HOLOGRAPHIC RENYI ENTROPY FROM GENUS-n SHADOW
# =========================================================================

def holographic_renyi_entropy(kappa_val, n_replica, log_ratio):
    r"""Return the scalar replica candidate at index ``n``.

    The n-th Renyi entropy is computed on the n-fold branched cover
    Sigma_n.  The genus-0 contribution gives:

        S_n^{scalar} = (kappa/3)(1 + 1/n) log(L/epsilon)

    Under the replica and AdS/CFT bridge packages this is compared with
    the Dong (2014) holographic Renyi expression:
        S_n = Area(cosmic_brane_n) / (4*G_N * n)

    where the cosmic brane has tension T_n = (n-1)/(4*G_N*n).

    The full expansion includes higher-genus corrections on Sigma_n:
        S_n = S_n^{scalar} + sum_{g>=1} delta_S_n^{(g)}

    >>> holographic_renyi_entropy(Rational(13, 2), 2, 1)
    13/4
    >>> holographic_renyi_entropy(Rational(13, 2), 1, 1)
    13/3
    """
    kappa_val = Rational(kappa_val)
    n_replica = Rational(n_replica)

    if n_replica == 1:
        # Von Neumann limit
        return Rational(2) * kappa_val * log_ratio / 3

    return renyi_entropy_scalar(kappa_val, n_replica, log_ratio)


def renyi_spectrum(kappa_val, log_ratio, n_max=6):
    r"""Scalar replica-candidate spectrum for ``n=1,...,n_max``.

    The spectrum is monotonically decreasing:
        S_1 >= S_2 >= S_3 >= ...

    and bounded below by S_inf = (kappa/3) * log(L/epsilon).

    >>> spec = renyi_spectrum(Rational(13, 2), 1)
    >>> all(spec[n] >= spec[n+1] for n in range(1, len(spec)))
    True
    """
    kappa_val = Rational(kappa_val)
    result = {}

    for n in range(1, n_max + 1):
        result[n] = holographic_renyi_entropy(kappa_val, n, log_ratio)

    return result


def renyi_monotonicity_check(kappa_val, log_ratio=1, n_max=10):
    r"""Verify monotonicity of the scalar replica-candidate sequence.

    A necessary consistency check: S_n is non-increasing in n.

    >>> renyi_monotonicity_check(Rational(13, 2))
    True
    >>> renyi_monotonicity_check(Rational(1, 4))
    True
    """
    kappa_val = Rational(kappa_val)
    spec = renyi_spectrum(kappa_val, log_ratio, n_max)

    for n in range(1, n_max):
        if spec[n] < spec[n + 1]:
            return False
    return True


def renyi_min_entropy(kappa_val, log_ratio):
    r"""Limit of the scalar replica-candidate sequence.

    S_inf = (kappa/3) * log(L/epsilon)

    This is half the von Neumann entropy:
        S_inf = S_1 / 2

    >>> renyi_min_entropy(Rational(13, 2), 1)
    13/6
    >>> renyi_min_entropy(Rational(13, 2), 1) == von_neumann_entropy_scalar(Rational(13, 2), 1) / 2
    True
    """
    kappa_val = Rational(kappa_val)
    return kappa_val * log_ratio / 3


def cosmic_brane_tension(n_replica, c_val):
    r"""Return the cosmic-brane tension candidate in the AdS3 dictionary.

    T_n = (n-1) / (4*G_N * n)

    The equality ``1/(4*G_N)=c/6`` belongs to the geometric bridge.

    T_n = (n-1) * c / (6*n)

    >>> cosmic_brane_tension(2, Rational(26))
    13/6
    >>> cosmic_brane_tension(1, Rational(26))
    0
    """
    n_replica = Rational(n_replica)
    c_val = Rational(c_val)
    return (n_replica - 1) * c_val / (6 * n_replica)


# =========================================================================
# SECTION 10: HAYDEN-PRESKILL FROM SHADOW CONNECTION MONODROMY
# =========================================================================

def hayden_preskill_scrambling(kappa_val, beta_val=None):
    r"""Return shadow monodromy and the chaos/decoupling obligation.

    The shadow connection nabla^sh = d - Q'/(2Q) dt has:
    - Monodromy -1 (Koszul sign) around each zero of Q
    - The zeros of Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
      occur at t_* = -2*kappa / (3*alpha +/- i*sqrt(2*Delta))

    A physical scrambling-time comparison would use

        t_scramble = (1/lambda_L) * log(S_thermal)

    where:
    - lambda_L = 2*pi / beta is the Lyapunov exponent
      (MSS bound: lambda_L <= 2*pi*T)
    - S_thermal = (c/3) * log(beta / (pi * epsilon))
      is the thermal entropy

    Saturation of the MSS bound is tested from thermal OTOCs in a
    specified dynamical system.

    >>> hp = hayden_preskill_scrambling(Rational(13, 2))
    >>> hp['monodromy']
    -1
    >>> hp['lyapunov_saturates_MSS'] is None
    True
    """
    kappa_val = Rational(kappa_val)

    bridge = physical_bridge_surfaces()['chaos_page']
    result = {
        'kappa': kappa_val,
        'monodromy': -1,  # Koszul sign
        'monodromy_source': 'shadow connection around zeros of Q_L',
        'lyapunov_exponent': bridge['physical_conclusion'],
        'lyapunov_saturates_MSS': bridge['physical_conclusion'],
        'scrambling_time': bridge['physical_conclusion'],
        'chaos_page_status': bridge['status'],
        'chaos_page_required_data': bridge['required_data'],
        'candidate_scrambling_formula': 't_scramble = (beta/(2*pi)) * log(S)',
    }

    if beta_val is not None:
        beta_val = Rational(beta_val)
        lambda_L = 2 * pi / beta_val
        # Thermal entropy at finite temperature
        # S_thermal ~ (c/3) * (pi * L / beta) for high temperature
        # t_scramble ~ (beta / (2*pi)) * log(c)
        result['beta'] = beta_val
        result['lambda_L_symbolic'] = lambda_L

    return result


def decoupling_time(kappa_val, log_S=None):
    r"""Return the decoupling candidate and physical bridge status.

    The Hayden--Preskill candidate is

        t_decouple = t_scramble + O(1)
                   = (1/lambda_L) * log(S) + O(1)

    The displayed arity refinement is a formal comparison ansatz.  The
    chaos/Page bridge supplies the thermal dynamics, radiation algebra,
    and recovery criterion.

    >>> dt = decoupling_time(Rational(13, 2))
    >>> dt['scrambling_is_koszul'] is None
    True
    """
    kappa_val = Rational(kappa_val)

    bridge = physical_bridge_surfaces()['chaos_page']
    return {
        'kappa': kappa_val,
        'formula_candidate': 't_decouple = (1/lambda_L) * log(S) + O(1)',
        'decoupling_time': bridge['physical_conclusion'],
        'scrambling_is_koszul': None,
        'physical_decoupling_status': bridge['status'],
        'physical_decoupling_required_data': bridge['required_data'],
        'formal_arity_ansatz': (
            't_r ~ (1/lambda_L) * r * log(1/rho)'
        ),
    }


def page_time_from_complementarity(c_val, log_ratio=1):
    r"""Compute the Virasoro scalar self-duality point.

    At ``c=13`` the two scalar candidates agree.  A Page-time statement
    additionally uses an evaporation model, radiation algebra, and
    island/QES prescription.

    The complementarity sum:
        S(A) + S(A!) = (26/3) * log(L/eps)
    is the exact scalar identity computed here.

    >>> pt = page_time_from_complementarity(Rational(13))
    >>> pt['scalar_self_dual_point']
    True
    >>> pt['S_A']
    13/3
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26 - c_val)

    S_A = Rational(2) * kappa * log_ratio / 3
    S_Ac = Rational(2) * kappa_dual * log_ratio / 3

    bridge = physical_bridge_surfaces()['chaos_page']
    if S_A < S_Ac:
        scalar_branch = 'A'
    elif S_A == S_Ac:
        scalar_branch = 'self_dual'
    else:
        scalar_branch = 'A_dual'

    return {
        'c': c_val,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'S_A': S_A,
        'S_Ac': S_Ac,
        'S_total': S_A + S_Ac,
        'scalar_self_dual_point': (S_A == S_Ac),
        'is_page_point': bridge['physical_conclusion'],
        'self_dual_c': Rational(13),
        'page_time': bridge['physical_conclusion'],
        'page_status': bridge['status'],
        'scalar_branch': scalar_branch,
        'phase': bridge['physical_conclusion'],
    }


def page_curve_profile(log_ratio=1, n_points=13):
    r"""Return the symmetric Virasoro scalar envelope.

    S_EE(c) = min(S(c), S(26-c))
            = min((c/3), (26-c)/3) * log(L/eps)

    The scalar envelope has a cusp at the self-dual point ``c=13``.
    A physical Page curve uses the chaos/Page bridge package.

    Returns list of (c, S_EE) pairs.

    >>> profile = page_curve_profile()
    >>> profile[0]['scalar_branch']
    'A'
    >>> profile[-1]['scalar_branch']
    'A_dual'
    """
    result = []
    bridge = physical_bridge_surfaces()['chaos_page']
    for i in range(n_points + 1):
        c_val = Rational(2 * i)  # c = 0, 2, 4, ..., 26
        kappa = kappa_virasoro(c_val)
        kappa_dual = kappa_virasoro(26 - c_val)
        S_A = Rational(2) * kappa * log_ratio / 3
        S_Ac = Rational(2) * kappa_dual * log_ratio / 3

        # Symmetric scalar envelope: min(S_A, S_Ac)
        S_page = min(S_A, S_Ac) if c_val != 13 else S_A

        if S_A < S_Ac:
            scalar_branch = 'A'
        elif S_A == S_Ac:
            scalar_branch = 'self_dual'
        else:
            scalar_branch = 'A_dual'

        result.append({
            'c': c_val,
            'kappa': kappa,
            'S_A': S_A,
            'S_Ac': S_Ac,
            'S_page': S_page,
            'scalar_envelope': S_page,
            'scalar_branch': scalar_branch,
            'phase': bridge['physical_conclusion'],
            'physical_page_curve': bridge['physical_conclusion'],
            'page_status': bridge['status'],
        })

    return result


# =========================================================================
# SECTION 11: CROSS-FAMILY CENSUS AND CONSISTENCY
# =========================================================================

def full_qec_census(
    quadratic_certificates: Optional[
        Mapping[str, Mapping[str, object]]
    ] = None,
):
    r"""Return algebraic statuses and physical bridge obligations by family.

    For each standard family, compute:
    - kappa, shadow class, code parameters
    - RT entropy, QES structure, KL status
    - Tensor network depth, Renyi spectrum

    >>> census = full_qec_census()
    >>> len(census) >= 6
    True
    >>> all(c['universal_reconstruction'] for c in census)
    True
    >>> all(c['exact_reconstruction'] is None for c in census)
    True
    """
    families = [
        ('Heisenberg', 'heisenberg', 'heisenberg:k=1', Rational(1)),
        ('Affine sl_2 (k=1)', 'affine', 'affine:sl2:k=1', Rational(9, 4)),
        ('Beta-gamma', 'betagamma', 'betagamma:lambda=1', Rational(1)),
        ('Virasoro c=1/2', 'virasoro', 'virasoro:c=1/2', Rational(1, 4)),
        ('Virasoro c=13', 'virasoro', 'virasoro:c=13', Rational(13, 2)),
        ('Virasoro c=26', 'virasoro', 'virasoro:c=26', Rational(13)),
    ]

    census = []
    certificate_map = quadratic_certificates or {}
    bridges = physical_bridge_surfaces()
    for name, family, algebra_id, kappa in families:
        cls = shadow_depth_class(family)
        code_params = shadow_depth_code_parameters(family)
        scalar_entropy_candidate = rt_from_kappa(kappa, 1)
        scalar_replica_candidate = holographic_renyi_entropy(kappa, 2, 1)
        algebraic = algebraic_code_parameters(
            family,
            algebra_id=algebra_id,
            quadratic_certificate=certificate_map.get(algebra_id),
        )

        census.append({
            'name': name,
            'family': family,
            'algebra_id': algebra_id,
            'kappa': kappa,
            'shadow_class': cls,
            'code_type': code_params['code_type'],
            'code_notation': code_params['code_notation'],
            'n_redundancy': code_params['n_redundancy'],
            'scalar_entropy_candidate': scalar_entropy_candidate,
            'scalar_replica_candidate_n2': scalar_replica_candidate,
            'rt_entropy': bridges['rt_qes']['physical_conclusion'],
            'renyi_2': bridges['entropy']['physical_conclusion'],
            'entropy_status': bridges['entropy']['status'],
            'qes_status': bridges['rt_qes']['status'],
            'kl_genus_1': bridges['hilbert_qec']['physical_conclusion'],
            'kl_status': bridges['hilbert_qec']['status'],
            'universal_reconstruction': algebraic['universal_reconstruction'],
            'universal_reconstruction_status': algebraic[
                'universal_reconstruction_status'
            ],
            'exact_reconstruction': algebraic['exact_quadratic_recovery'],
            'exact_reconstruction_status': algebraic['exact_recovery_status'],
            'is_koszul': algebraic['quadratic_koszul'],
            'theorem_a_surface': algebraic['theorem_a_surface'],
            'theorem_b_surface': algebraic['theorem_b_surface'],
            'physical_entanglement_wedge': bridges['oca_bulk'][
                'physical_conclusion'
            ],
            'physical_entanglement_wedge_status': bridges['oca_bulk']['status'],
            'page_curve': bridges['chaos_page']['physical_conclusion'],
            'page_curve_status': bridges['chaos_page']['status'],
        })

    return census


def cross_check_rt_renyi_limit(kappa_val, log_ratio=1):
    r"""Check the scalar ``n -> 1`` coefficient identity.

    S_EE = lim_{n->1} S_n(kappa, n, log_ratio)
         = lim_{n->1} (kappa/3)(1+1/n) log_ratio
         = (2*kappa/3) log_ratio

    >>> cross_check_rt_renyi_limit(Rational(13, 2))
    True
    """
    kappa_val = Rational(kappa_val)
    rt = rt_from_kappa(kappa_val, log_ratio)
    vn = von_neumann_entropy_scalar(kappa_val, log_ratio)
    return rt == vn


def cross_check_complementarity_sum(c_val, log_ratio=1):
    r"""Check the Virasoro scalar complementarity sum.

    >>> cross_check_complementarity_sum(Rational(1))
    True
    >>> cross_check_complementarity_sum(Rational(13))
    True
    >>> cross_check_complementarity_sum(Rational(26))
    True
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26 - c_val)
    total = rt_from_kappa(kappa, log_ratio) + rt_from_kappa(kappa_dual, log_ratio)
    return total == Rational(26, 3) * log_ratio


def cross_check_area_identification(c_val):
    r"""Check equality of the two formal RT coefficients.

    The two computations:
    Path 1: 1/(4*G_N) = c/6, Area = 2*log(L/eps), so S = c/3 * log(L/eps)
    Path 2: kappa = c/2, S = (2*kappa/3) * log(L/eps) = c/3 * log(L/eps)

    >>> cross_check_area_identification(Rational(26))
    True
    >>> cross_check_area_identification(Rational(1))
    True
    """
    c_val = Rational(c_val)
    path1 = c_val / 3  # from 1/(4G_N) * Area
    kappa = kappa_virasoro(c_val)
    path2 = Rational(2) * kappa / 3  # from kappa
    return path1 == path2


def cross_check_renyi_monotonicity_all_families():
    r"""Verify monotonicity of the scalar replica candidates.

    >>> cross_check_renyi_monotonicity_all_families()
    True
    """
    for name, kappa in STANDARD_KAPPAS.items():
        if kappa <= 0:
            continue  # skip ghost (negative kappa)
        if not renyi_monotonicity_check(kappa):
            return False
    return True


def cross_check_min_entropy_half_vn():
    r"""Verify the scalar limiting identity ``S_inf=S_1/2``.

    The min-entropy is half the von Neumann entropy:
        S_inf = (kappa/3) = (1/2) * (2*kappa/3) = S_1 / 2

    >>> cross_check_min_entropy_half_vn()
    True
    """
    for name, kappa in STANDARD_KAPPAS.items():
        if kappa <= 0:
            continue
        s_inf = renyi_min_entropy(kappa, 1)
        s_vn = von_neumann_entropy_scalar(kappa, 1)
        if s_inf != s_vn / 2:
            return False
    return True
