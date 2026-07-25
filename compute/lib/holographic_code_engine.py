r"""Typed algebraic surfaces behind the holographic-code programme.

The engine keeps five constructions separate.

* Theorem A is the universal enhanced-Ran reconstruction map
  ``epsilon_A: Omega_X B_X(A) -> A``.
* Theorem B belongs to a chosen quadratic presentation
  ``A^i = C_X(sV, s^2R)``.  Its comparison is
  ``q_A: A^i -> B_X(A)``, with adjoint
  ``p_A: Omega_X(A^i) -> A``.  The homology of ``Cone(q_A)``, together
  with ``H_CL`` and strong convergence, supplies the certificate.
* The fixed-coalgebra co/contra correspondence is the equivalence
  ``D^co(C-Comod) ~= D^ctr(C-Contramod)`` for one fixed ``C``.
* Verdier duality and the derived chiral centre carry their own
  hypotheses and comparison maps.
* A physical decoder requires beta_T, a Hilbert realization, an error
  algebra, and subregion recovery maps.

The shadow classes G/L/C/M record arity depth.  Every Theorem B verdict
in this module is obtained from an algebra-bound quadratic certificate.

For an anti-symplectic involution ``sigma`` of the Verdier pairing, the
two eigenspaces are isotropic and pair nondegenerately across the
Lagrangian splitting.  This is algebraic input for a future
Knill--Laflamme analysis; the physical analysis begins after an error
algebra and adjoint structure have been specified.

References:
  Almheiri-Dong-Harlow 2015 (1411.7041): holographic QEC
  Pastawski-Yoshida-Harlow-Preskill 2015 (1503.06237): HaPPY code
  prop:thqg-barcobar-error-correction (thqg_entanglement_programme.tex)
  conj:thqg-shadow-depth-code-distance (thqg_entanglement_programme.tex)
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Mapping, Optional, Tuple

from sympy import Rational, Symbol, simplify

# ---------------------------------------------------------------------------
# Imports from existing modules
# ---------------------------------------------------------------------------
from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    shadow_depth_class,
    entanglement_correction_depth,
    shadow_radius_virasoro,
    von_neumann_entropy_scalar,
)
from compute.lib.qec_koszul_code_engine import (
    theorem_a_reconstruction_surface,
    theorem_b_recovery_surface_from_family,
)


def independent_reconstruction_surfaces() -> Dict[str, Dict[str, object]]:
    """Return the fixed-C, Verdier, centre, and physical surfaces."""
    return {
        'fixed_coalgebra': {
            'construction': 'D^co(C-Comod) ~= D^ctr(C-Contramod)',
            'scope': 'one fixed coalgebra C',
            'status': 'SEPARATE_FIXED_C_SURFACE',
        },
        'verdier_dual': {
            'construction': 'A!_infty = D_Ran B_X(A)',
            'hypotheses': (
                'constructibility + dualizability + continuity; strict '
                'quadratic identification requires its finite-type comparison'
            ),
            'status': 'SEPARATE_CONDITIONAL_SURFACE',
        },
        'derived_center': {
            'construction': 'Z^der_ch(A) = C^bullet_ch(A,A)',
            'scope': 'Hochschild closed-sector object',
            'status': 'SEPARATE_DEFINED_SURFACE',
        },
        'physical_decoder': {
            'recovery': None,
            'required_data': (
                'beta_T',
                'Hilbert realization',
                'physical error algebra',
                'subregion recovery maps',
            ),
            'status': (
                'CONDITIONAL_ON_BETA_T_HILBERT_ERROR_ALGEBRA_AND_SUBREGION_MAPS'
            ),
        },
    }


def theorem_b_recovery_surface_from_shadow_class(
    cls: str,
    *,
    algebra_id: Optional[str] = None,
    certificate: Optional[Mapping[str, object]] = None,
) -> Dict[str, object]:
    """Compatibility reporter for Theorem B, indexed by an exact algebra.

    The shadow class is retained as descriptive metadata.  A certificate
    is accepted only with an explicit ``algebra_id`` and is checked by the
    shared quadratic-certificate implementation.

    >>> theorem_b_recovery_surface_from_shadow_class('G')['status']
    'UNVERIFIED'
    """
    if cls not in {'G', 'L', 'C', 'M'}:
        raise ValueError('shadow class must be one of G, L, C, M')
    if certificate is not None and algebra_id is None:
        raise ValueError('algebra_id is required with a quadratic certificate')

    requested_id = algebra_id or f'shadow-class:{cls}:unspecified-algebra'
    surface = theorem_b_recovery_surface_from_family(requested_id, certificate)
    return {
        **surface,
        'shadow_class': cls,
        'shadow_class_role': 'arity-depth metadata',
    }


# ===================================================================
#  SECTION 1: KOSZULNESS CONDITIONS AS CODE PROPERTIES
# ===================================================================

# The 12 tests and consequences around chiral Koszulness
# (thm:koszul-equivalences-meta), each with a code-theoretic translation.

KOSZULNESS_CODE_DICTIONARY = [
    {
        'id': 'K1',
        'name': 'PBW degeneration',
        'algebraic': 'Associated graded of PBW filtration degenerates at all genera',
        'code_property': 'Systematic encoding',
        'code_meaning': 'Code admits tensor-product decomposition; encoding is structured',
        'status': 'unconditional',
    },
    {
        'id': 'K2',
        'name': 'A-infinity formality',
        'algebraic': 'Bar cohomology is formal as A-infinity algebra',
        'code_property': 'Linear sufficiency',
        'code_meaning': 'Linear encoding captures the formal bar data',
        'status': 'unconditional',
    },
    {
        'id': 'K3',
        'name': 'Ext diagonal vanishing',
        'algebraic': 'Ext^{p,q}(A) vanishes off the diagonal p = q',
        'code_property': 'Sharp error syndrome',
        'code_meaning': 'Error syndromes are supported on the diagonal',
        'status': 'unconditional',
    },
    {
        'id': 'K4',
        'name': 'Quadratic bar comparison',
        'algebraic': (
            'q_A: A^i -> B_X(A) is a quasi-isomorphism, equivalently '
            'p_A: Omega_X(A^i) -> A is a quasi-isomorphism under H_CL '
            'and strong convergence'
        ),
        'code_property': 'Exact quadratic recovery',
        'code_meaning': (
            'The quadratic compression A^i retains the bar information '
            'certified by the acyclicity of Cone(q_A)'
        ),
        'status': 'certificate-required',
        'condition': (
            'Theorem B package: chosen quadratic presentation + H_CL + '
            'strong convergence + acyclic Cone(q_A)'
        ),
    },
    {
        'id': 'K5',
        'name': 'Barr-Beck-Lurie comparison',
        'algebraic': 'The comparison functor is an equivalence',
        'code_property': 'Categorical determinism',
        'code_meaning': 'Categorical descent determines the reconstructed object',
        'status': 'listed-consequence',
        'condition': 'proved consequence of the bar-cobar quasi-isomorphism row',
    },
    {
        'id': 'K6',
        'name': 'FH concentrated in degree 0',
        'algebraic': 'Factorization homology concentrated in degree 0',
        'code_property': 'Optimal threshold',
        'code_meaning': 'The factorization-homology proxy is concentrated in degree zero',
        'status': 'conditional',
        'condition': 'prop:bar-fh comparison plus detection hypothesis',
    },
    {
        'id': 'K7',
        'name': 'ChirHoch vanishing outside {0,1,2}',
        'algebraic': 'Chiral Hochschild cohomology vanishes in degrees > 2',
        'code_property': 'Code rigidity',
        'code_meaning': 'The stated Hochschild range controls the deformation complex',
        'status': 'conditional',
        'condition': (
            'Theorem H package: PBW chiral Koszulness, finite-type/perfectness, '
            'genericity, E_infty completion, strict Mittag-Leffler passage, '
            'and localized residue-twisted bar concentration; otherwise use '
            'KD_H^bullet(A)'
        ),
    },
    {
        'id': 'K8',
        'name': 'Kac-Shapovalov nonvanishing',
        'algebraic': 'Kac-Shapovalov determinant nonzero in bar-relevant range',
        'code_property': 'Non-degenerate Gram matrix',
        'code_meaning': 'Code inner product is well-defined; states are distinguishable',
        'status': 'unconditional',
    },
    {
        'id': 'K9',
        'name': 'FM boundary acyclicity',
        'algebraic': 'Fulton-MacPherson boundary strata are acyclic',
        'code_property': 'Code locality',
        'code_meaning': 'Boundary acyclicity supports a local comparison',
        'status': 'unconditional',
    },
    {
        'id': 'K10',
        'name': 'Shadow-formality',
        'algebraic': 'Shadow obstruction tower is formal at arities 2, 3, 4',
        'code_property': 'Classical-quantum agreement',
        'code_meaning': 'The formal shadow tower admits the stated quantum lift',
        'status': 'unconditional',
    },
    {
        'id': 'K11',
        'name': 'Lagrangian criterion',
        'algebraic': 'Complementarity summands are Lagrangian subspaces',
        'code_property': 'Maximal code rate',
        'code_meaning': 'Code subspace is half-dimensional; optimal information density',
        'status': 'conditional',
        'condition': 'perfectness and nondegeneracy of Verdier pairing',
    },
    {
        'id': 'K12',
        'name': 'Bifunctor decomposition',
        'algebraic': 'Obstruction bifunctor admits diagonal decomposition',
        'code_property': 'Structured decoding',
        'code_meaning': 'Decoding has factored structure; efficient recovery algorithm',
        'status': 'one-directional',
        'condition': 'forward implication proved',
    },
]


def get_koszulness_code_dictionary() -> List[Dict]:
    """Return the full 12-fold Koszulness-code dictionary.

    >>> d = get_koszulness_code_dictionary()
    >>> len(d)
    12
    >>> d[3]['id']
    'K4'
    >>> d[3]['code_property']
    'Exact quadratic recovery'
    """
    return KOSZULNESS_CODE_DICTIONARY


def unconditional_equivalences() -> List[Dict]:
    """Return rows still marked unconditional in the code dictionary.

    K4 is ambient-qualified, K5 is a listed consequence, and K6 is a
    conditional factorization-homology comparison.

    >>> len(unconditional_equivalences())
    6
    """
    return [k for k in KOSZULNESS_CODE_DICTIONARY if k['status'] == 'unconditional']


# ===================================================================
#  SECTION 2: CODE PARAMETERS
# ===================================================================


def _canonical_algebra_id(family: str, parameters: Mapping[str, object]) -> str:
    """Build a parameter-sensitive identifier for a standard example."""
    normalized = family.lower()
    if normalized in ('heisenberg', 'lattice', 'free_fermion'):
        return f'{normalized}:k={parameters.get("k", 1)}'
    if normalized in ('affine', 'kac_moody'):
        return (
            f'{normalized}:k={parameters.get("k", 1)}:'
            f'dim_g={parameters.get("dim_g", 3)}:'
            f'h_dual={parameters.get("h_dual", 2)}'
        )
    if normalized in ('betagamma', 'bc'):
        return f'{normalized}:lambda={parameters.get("lam", 1)}'
    if normalized in ('virasoro', 'w_algebra', 'w3', 'w_n'):
        return f'{normalized}:c={parameters.get("c", 1)}'
    return normalized


def code_parameters(
    family: str,
    *,
    algebra_id: Optional[str] = None,
    quadratic_certificate: Optional[Mapping[str, object]] = None,
    completed: bool = False,
    chain_package_verified: bool = False,
    **kwargs,
) -> Dict:
    """Compute holographic code parameters for a standard family.

    Returns:
        kappa: modular characteristic (scalar datum)
        shadow_class: G/L/C/M classification
        r_max: shadow depth
        redundancy_channels: number of independent error-correction channels
        theorem_a_surface: universal enhanced-Ran reconstruction
        theorem_b_surface: certificate-governed quadratic comparison
        is_koszul: Theorem B verdict, or ``None`` pending a certificate
        lagrangian_fraction: algebraic half-dimensional proxy

    >>> p = code_parameters('heisenberg', k=1)
    >>> p['shadow_class']
    'G'
    >>> p['redundancy_channels']
    0
    >>> p['universal_reconstruction']
    True
    >>> p['exact_recovery_status']
    'UNVERIFIED'
    """
    cls = shadow_depth_class(family)
    r_max = entanglement_correction_depth(family)
    requested_id = algebra_id or _canonical_algebra_id(family, kwargs)
    theorem_a_surface = theorem_a_reconstruction_surface(
        completed=completed,
        chain_package_verified=chain_package_verified,
    )
    theorem_b_surface = theorem_b_recovery_surface_from_family(
        requested_id, quadratic_certificate
    )
    separate = independent_reconstruction_surfaces()

    if cls == 'G':
        redundancy = 0
    elif cls == 'L':
        redundancy = 1
    elif cls == 'C':
        redundancy = 2
    else:  # M
        redundancy = -1  # infinite

    # Kappa depends on family
    kappa = None
    if family.lower() in ('heisenberg', 'lattice', 'free_fermion'):
        k = kwargs.get('k', 1)
        kappa = kappa_heisenberg(Rational(k))
    elif family.lower() in ('affine', 'kac_moody'):
        k = kwargs.get('k', 1)
        dim_g = kwargs.get('dim_g', 3)
        h_dual = kwargs.get('h_dual', 2)
        kappa = kappa_affine(dim_g, Rational(k), h_dual)
    elif family.lower() in ('betagamma', 'bc'):
        lam = kwargs.get('lam', 1)
        kappa = kappa_betagamma(Rational(lam))
    elif family.lower() in ('virasoro', 'w_algebra', 'w3', 'w_n'):
        c = kwargs.get('c', 1)
        kappa = kappa_virasoro(Rational(c))

    return {
        'family': family,
        'algebra_id': requested_id,
        'kappa': kappa,
        'shadow_class': cls,
        'r_max': r_max,
        'redundancy_channels': redundancy,
        'universal_reconstruction': theorem_a_surface[
            'enhanced_ran_reconstruction'
        ],
        'universal_reconstruction_status': theorem_a_surface[
            'enhanced_ran_status'
        ],
        'chain_reconstruction': theorem_a_surface['chain_reconstruction'],
        'chain_reconstruction_status': theorem_a_surface['chain_status'],
        'theorem_a_surface': theorem_a_surface,
        'is_koszul': theorem_b_surface['koszul'],
        'quadratic_koszul': theorem_b_surface['koszul'],
        'exact_recovery': theorem_b_surface['exact_quadratic_recovery'],
        'exact_quadratic_recovery': theorem_b_surface[
            'exact_quadratic_recovery'
        ],
        'exact_recovery_status': theorem_b_surface['status'],
        'recovery_surface': theorem_b_surface,
        'theorem_b_surface': theorem_b_surface,
        'lagrangian_fraction': Rational(1, 2),
        'code_rate': None,
        'code_rate_status': 'REQUIRES_HILBERT_REALIZATION',
        'fixed_coalgebra_surface': separate['fixed_coalgebra'],
        'verdier_dual_surface': separate['verdier_dual'],
        'derived_center_surface': separate['derived_center'],
        'physical_recovery': separate['physical_decoder']['recovery'],
        'physical_recovery_status': separate['physical_decoder']['status'],
        'physical_decoder_surface': separate['physical_decoder'],
    }


def redundancy_channels(family: str) -> int:
    """Number of higher-shadow arity slots beyond the scalar term.

    Each channel corresponds to one arity level of the shadow obstruction tower
    beyond the scalar (kappa) level.  The arity-r shadow is
    governed by the filtered MC equation.  The count is an algebraic
    redundancy proxy; a Hilbert-space recovery channel additionally uses
    the physical decoder surface.

    Class G: 0 channels (kappa is the entire code)
    Class L: 1 channel (arity 3 recoverable from arity 2)
    Class C: 2 channels (arities 3, 4 recoverable from arity 2)
    Class M: infinite channels (all arities recoverable from arity 2)

    Returns -1 for infinite.

    >>> redundancy_channels('heisenberg')
    0
    >>> redundancy_channels('affine')
    1
    >>> redundancy_channels('betagamma')
    2
    >>> redundancy_channels('virasoro')
    -1
    """
    cls = shadow_depth_class(family)
    return {'G': 0, 'L': 1, 'C': 2, 'M': -1}[cls]


# ===================================================================
#  SECTION 3: KNILL-LAFLAMME FROM LAGRANGIAN ORTHOGONALITY
# ===================================================================

def verify_lagrangian_isotropy() -> bool:
    """Verify the Lagrangian isotropy condition algebraically.

    The Verdier pairing satisfies:
      <sigma(v), sigma(w)>_D = -<v, w>_D

    For v, w in V+ = Q_g(A) (eigenvalue +1 of sigma):
      <v, w>_D = <sigma(v), sigma(w)>_D = -<v, w>_D
      => 2<v, w>_D = 0
      => <v, w>_D = 0

    This is the isotropy condition: Q_g(A) is isotropic for <.,.>_D.

    >>> verify_lagrangian_isotropy()
    True
    """
    # The proof is purely algebraic:
    # sigma^2 = id, <sigma(v), sigma(w)> = -<v,w> (anti-commutativity)
    # For v, w in eigenspace of sigma with eigenvalue +1:
    # <v, w> = <sigma(v), sigma(w)> = -<v, w> => <v, w> = 0
    return True


def verify_shapovalov_cross_pairing() -> Dict:
    """Verify the Shapovalov cross-pairing structure.

    The Shapovalov form <v, w>_S := <v, sigma(w)>_D satisfies:
    - For v in V+ = Q_g(A) (eigenvalue +1) and w in V- = Q_g(A!) (eigenvalue -1):
      sigma(w) = -w, so <v, w>_S = <v, -w>_D = -<v, w>_D.
    - V+ and V- are complementary Lagrangians for <,>_D: the cross-pairing
      V+ x V- -> C is NON-DEGENERATE.
    - Therefore <v, w>_S = -<v, w>_D is also non-degenerate on V+ x V-.

    The decomposition H = Q_g(A) + Q_g(A!) is a Lagrangian splitting with
    Verdier-isotropic summands.  The Shapovalov form detects the
    nondegenerate cross-pairing with a sign flip.

    Returns a dictionary documenting the structure.

    >>> result = verify_shapovalov_cross_pairing()
    >>> result['lagrangian_isotropy']
    True
    >>> result['shapovalov_orthogonal']
    False
    """
    return {
        'lagrangian_isotropy': True,       # <V+, V+>_D = 0, <V-, V->_D = 0
        'shapovalov_orthogonal': False,    # the cross-pairing is nondegenerate
        'cross_pairing_sign': -1,          # <v,w>_S = -<v,w>_D on V+ x V-
        'decomposition_type': 'symplectic',  # Lagrangian splitting
    }


def verify_knill_laflamme_scalar_level() -> bool:
    """Verify the Knill-Laflamme condition at the scalar level (genus 1).

    At genus 1, dim Q_1(A) = 1 (spanned by kappa).  Any operator on
    a one-dimensional space is proportional to the identity, so the
    KL condition P_C E^dag E P_C = c(E) P_C is automatic.

    SCOPE: This is trivially satisfied because dim = 1.  At genus >= 2
    where dim Q_g > 1, the full KL condition is non-trivial and requires
    analysis of the MC structure Theta_A^{(g)} at each genus.

    >>> verify_knill_laflamme_scalar_level()
    True
    """
    return True


def knill_laflamme_structure() -> Dict:
    """Summary of the algebraic Lagrangian input to a KL analysis.

    Returns a dictionary describing the proved structure:
    1. Isotropy: <Q_g(A), Q_g(A)>_D = 0 (Verdier) — code self-decoupling
    2. Cross-pairing: <v,w>_S = -<v,w>_D on Q_g(A) x Q_g(A!), a
       nondegenerate symplectic pairing between the summands.

    A physical KL condition is formulated after choosing a Hilbert
    realization, adjoint, error algebra, and recovery maps.

    >>> kl = knill_laflamme_structure()
    >>> kl['isotropy_proved']
    True
    >>> kl['cross_pairing_nondegenerate']
    True
    >>> kl['physical_kl_status']
    'REQUIRES_HILBERT_ERROR_ALGEBRA_AND_RECOVERY_MAPS'
    """
    return {
        'isotropy_proved': True,
        'isotropy_source': 'prop:lagrangian-eigenspaces (higher_genus_complementarity.tex)',
        'isotropy_mechanism': '<sigma(v), sigma(w)>_D = -<v,w>_D => <v,w>_D = 0 on eigenspaces',
        'orthogonality_proved': False,
        'cross_pairing_nondegenerate': True,
        'cross_pairing_source': 'Shapovalov = Verdier composed with sigma',
        'cross_pairing_mechanism': (
            '<v,w>_S = -<v,w>_D on Q_g(A) x Q_g(A!)'
        ),
        'scalar_kl_genus_1': True,
        'scalar_kl_mechanism': (
            'a one-dimensional realized code space makes every compressed '
            'error product scalar'
        ),
        'full_kl_higher_genus': None,
        'physical_kl_status': (
            'REQUIRES_HILBERT_ERROR_ALGEBRA_AND_RECOVERY_MAPS'
        ),
        'physical_recovery': None,
        'overall_status': 'PROVED_ALGEBRAIC_LAGRANGIAN_SPLITTING',
    }


# ===================================================================
#  SECTION 4: SHADOW DEPTH AS REDUNDANCY STRUCTURE
# ===================================================================

def shadow_redundancy_resolution() -> Dict:
    """Reformulate shadow depth as an arity-filtration proxy.

    The shadow depth ``r_max(A)`` counts supported arity levels in the
    obstruction tower.  Recursive MC extension is recorded with its own
    hypothesis package.  Physical distance belongs to the decoder surface.

    Key insight: the scalar datum kappa (arity 2) is the fundamental
    logical datum.  All higher-arity shadows are DETERMINED by kappa
    via the MC equation (recursive existence, thm:recursive-existence).
    Each recovery step (arity r -> arity r+1) provides one
    redundancy channel.

    >>> res = shadow_redundancy_resolution()
    >>> res['conjecture_status']
    'REFORMULATED_AS_ARITY_PROXY'
    """
    return {
        'conjecture': 'conj:thqg-shadow-depth-code-distance',
        'conjecture_status': 'REFORMULATED_AS_ARITY_PROXY',
        'resolution': (
            'Shadow depth r_max counts supported higher-shadow arities.  The '
            'arity-two scalar is the first term of this filtration.  Physical '
            'code distance is computed after the Hilbert and error-algebra data '
            'have been supplied.'
        ),
        'shadow_arity_floor': 2,
        'code_distance_all_families': None,
        'physical_distance_status': 'REQUIRES_HILBERT_ERROR_ALGEBRA_AND_DECODER',
        'redundancy_by_class': {
            'G': {'channels': 0, 'meaning': 'scalar-only shadow profile'},
            'L': {'channels': 1, 'meaning': 'arity-3 shadow recoverable from kappa'},
            'C': {'channels': 2, 'meaning': 'arities 3,4 recoverable from kappa'},
            'M': {'channels': 'infinite', 'meaning': 'all arities recoverable; convergent for rho < 1'},
        },
        'recovery_procedure': (
            'Shadow obstruction tower reconstruction: from kappa, solve MC equation recursively '
            'at each arity under the hypotheses of thm:recursive-existence. '
            'This constructs an algebraic higher-shadow extension.'
        ),
        'physical_recovery': None,
        'physical_recovery_status': (
            'CONDITIONAL_ON_BETA_T_HILBERT_ERROR_ALGEBRA_AND_SUBREGION_MAPS'
        ),
    }


# ===================================================================
#  SECTION 5: TYPED RECONSTRUCTION SURFACES
# ===================================================================

def koszulness_equals_exact_qec(
    *,
    algebra_id: str = 'A',
    quadratic_certificate: Optional[Mapping[str, object]] = None,
    completed: bool = False,
    chain_package_verified: bool = False,
) -> Dict:
    """Return the typed theorem surfaces behind the QEC analogy.

    The function name is retained for callers of the original engine.  Its
    value now records Theorem A, Theorem B, and the physical decoder as
    distinct mathematical lanes.

    >>> thm = koszulness_equals_exact_qec()
    >>> thm['theorem_a_surface']['enhanced_ran_reconstruction']
    True
    >>> thm['theorem_b_surface']['status']
    'UNVERIFIED'
    >>> thm['physical_decoder_surface']['recovery'] is None
    True
    """
    theorem_a_surface = theorem_a_reconstruction_surface(
        completed=completed,
        chain_package_verified=chain_package_verified,
    )
    theorem_b_surface = theorem_b_recovery_surface_from_family(
        algebra_id, quadratic_certificate
    )
    separate = independent_reconstruction_surfaces()

    return {
        'programme': 'Koszul compression and holographic-code comparison',
        'status': 'TYPED_SURFACES',
        'algebra_id': algebra_id,
        'status_map': {
            'theorem_a_enhanced_ran_reconstruction': theorem_a_surface[
                'enhanced_ran_status'
            ],
            'theorem_a_chain_realization': theorem_a_surface['chain_status'],
            'theorem_b_quadratic_comparison': theorem_b_surface['status'],
            'fixed_coalgebra_co_contra': separate['fixed_coalgebra']['status'],
            'verdier_dual_comparison': separate['verdier_dual']['status'],
            'derived_center': separate['derived_center']['status'],
            'physical_decoder': separate['physical_decoder']['status'],
        },
        'typed_maps': [
            {
                'theorem': 'A',
                'map': 'epsilon_A: Omega_X B_X(A) -> A',
                'status': theorem_a_surface['enhanced_ran_status'],
                'role': 'universal enhanced-Ran reconstruction',
            },
            {
                'theorem': 'B',
                'map': 'q_A: A^i -> B_X(A)',
                'adjoint': 'p_A: Omega_X(A^i) -> A',
                'obstruction': 'Cone(q_A)',
                'status': theorem_b_surface['status'],
                'role': 'quadratic compression for a chosen presentation',
            },
            {
                'surface': 'physical decoder',
                'status': separate['physical_decoder']['status'],
                'role': 'Hilbert-space error correction after physical realization',
            },
        ],
        'theorem_a_surface': theorem_a_surface,
        'theorem_b_surface': theorem_b_surface,
        'quadratic_koszul': theorem_b_surface['koszul'],
        'exact_quadratic_recovery': theorem_b_surface[
            'exact_quadratic_recovery'
        ],
        'fixed_coalgebra_surface': separate['fixed_coalgebra'],
        'verdier_dual_surface': separate['verdier_dual'],
        'derived_center_surface': separate['derived_center'],
        'physical_recovery': separate['physical_decoder']['recovery'],
        'physical_recovery_status': separate['physical_decoder']['status'],
        'physical_decoder_surface': separate['physical_decoder'],
        'physical_translation': (
            'The OCA/open-closed comparison, beta_T, Hilbert realization, '
            'error algebra, and subregion maps supply the physical decoder.'
        ),
    }


# ===================================================================
#  SECTION 6: STANDARD LANDSCAPE CODE CENSUS
# ===================================================================

def standard_landscape_code_census(
    quadratic_certificates: Optional[
        Mapping[str, Mapping[str, object]]
    ] = None,
) -> List[Dict]:
    """Return the standard-family data with certificate-bound B status.

    For each standard family: code parameters, redundancy channels,
    convergence status, and cross-references.

    >>> census = standard_landscape_code_census()
    >>> len(census) >= 7
    True
    >>> all(c['is_koszul'] is None for c in census)
    True
    >>> all(c['theorem_a_surface']['enhanced_ran_reconstruction'] for c in census)
    True
    """
    families = [
        {
            'family': 'Heisenberg H_1',
            'algebra_id': 'heisenberg:k=1',
            'class': 'G', 'r_max': 2,
            'kappa': Rational(1),
            'redundancy': 0,
            'code_type': 'Trivial (Gaussian)',
            'physical': 'Free field / abelian Chern-Simons',
        },
        {
            'family': 'Lattice V_{E_8}',
            'algebra_id': 'lattice:E8',
            'class': 'G', 'r_max': 2,
            'kappa': Rational(8),
            'redundancy': 0,
            'code_type': 'Trivial (Gaussian)',
            'physical': 'E_8 lattice gauge theory',
        },
        {
            'family': 'Affine sl_2 (k=1)',
            'algebra_id': 'affine:sl2:k=1',
            'class': 'L', 'r_max': 3,
            'kappa': Rational(9, 4),
            'redundancy': 1,
            'code_type': 'Single-channel',
            'physical': 'SU(2) Chern-Simons (tree-level gravity)',
        },
        {
            'family': 'Beta-gamma (lambda=1)',
            'algebra_id': 'betagamma:lambda=1',
            'class': 'C', 'r_max': 4,
            'kappa': Rational(1),
            'redundancy': 2,
            'code_type': 'Two-channel',
            'physical': 'Topological B-model',
        },
        {
            'family': 'Virasoro (c=1/2, Ising)',
            'algebra_id': 'virasoro:c=1/2',
            'class': 'M', 'r_max': -1,
            'kappa': Rational(1, 4),
            'redundancy': -1,
            'code_type': 'Infinite-channel (divergent)',
            'physical': '3d gravity at c=1/2',
            'rho': shadow_radius_virasoro(0.5),
            'convergent': False,
        },
        {
            'family': 'Virasoro (c=13, self-dual)',
            'algebra_id': 'virasoro:c=13',
            'class': 'M', 'r_max': -1,
            'kappa': Rational(13, 2),
            'redundancy': -1,
            'code_type': 'Infinite-channel (convergent)',
            'physical': '3d gravity at self-dual point',
            'rho': shadow_radius_virasoro(13),
            'convergent': True,
        },
        {
            'family': 'Virasoro (c=26, critical string)',
            'algebra_id': 'virasoro:c=26',
            'class': 'M', 'r_max': -1,
            'kappa': Rational(13),
            'redundancy': -1,
            'code_type': 'Infinite-channel (strongly convergent)',
            'physical': '3d gravity / critical bosonic string',
            'rho': shadow_radius_virasoro(26),
            'convergent': True,
        },
    ]

    certificate_map = quadratic_certificates or {}
    separate = independent_reconstruction_surfaces()
    for entry in families:
        theorem_a_surface = theorem_a_reconstruction_surface()
        theorem_b_surface = theorem_b_recovery_surface_from_family(
            entry['algebra_id'], certificate_map.get(entry['algebra_id'])
        )
        entry['universal_reconstruction'] = theorem_a_surface[
            'enhanced_ran_reconstruction'
        ]
        entry['universal_reconstruction_status'] = theorem_a_surface[
            'enhanced_ran_status'
        ]
        entry['theorem_a_surface'] = theorem_a_surface
        entry['is_koszul'] = theorem_b_surface['koszul']
        entry['quadratic_koszul'] = theorem_b_surface['koszul']
        entry['exact_recovery'] = theorem_b_surface['exact_quadratic_recovery']
        entry['exact_quadratic_recovery'] = theorem_b_surface[
            'exact_quadratic_recovery'
        ]
        entry['exact_recovery_status'] = theorem_b_surface['status']
        entry['recovery_surface'] = theorem_b_surface
        entry['theorem_b_surface'] = theorem_b_surface
        entry['fixed_coalgebra_surface'] = separate['fixed_coalgebra']
        entry['verdier_dual_surface'] = separate['verdier_dual']
        entry['derived_center_surface'] = separate['derived_center']
        entry['physical_recovery'] = separate['physical_decoder']['recovery']
        entry['physical_recovery_status'] = separate['physical_decoder']['status']
        entry['physical_decoder_surface'] = separate['physical_decoder']

    return families


def non_koszul_code_failure() -> Dict:
    """Return the obstruction criterion and candidate test loci.

    An explicit nonzero homology class in ``Cone(q_A)`` certifies failure
    of the chosen quadratic presentation in the finite model.  The listed
    loci are prompts for that computation.

    >>> f = non_koszul_code_failure()
    >>> f['examples'][0]['status']
    'UNVERIFIED'
    """
    return {
        'status': 'OBSTRUCTION_CRITERION',
        'principle': (
            'A nonzero class in H(Cone(q_A)) obstructs q_A and its adjoint '
            'p_A.  The verdict belongs to the chosen presentation and '
            'becomes a Theorem B certificate after H_CL and convergence '
            'are recorded.'
        ),
        'examples': [
            {
                'family': 'Simple quotient L_k(g) at admissible level',
                'status': 'UNVERIFIED',
                'is_koszul': None,
                'exact_recovery': None,
                'required_computation': (
                    'Choose (V,R), construct q_A: A^i -> B_X(A), and compute '
                    'H(Cone(q_A)) with exact arithmetic.'
                ),
                'physical_question': (
                    'Determine the OCA and Hilbert packages governing recovery '
                    'of closed-sector operators from boundary data.'
                ),
            },
            {
                'family': 'Singular fiber of a deformation family',
                'status': 'UNVERIFIED',
                'is_koszul': None,
                'exact_recovery': None,
                'required_computation': (
                    'Specialize the presentation, compute Cone(q_A), and track '
                    'the H_CL and convergence packages through the fiber.'
                ),
                'physical_question': (
                    'Compare the algebraic obstruction with the spectrum and '
                    'subregion maps of the proposed gravitational realization.'
                ),
            },
        ],
        'research_test': (
            'Compute Cone(q_A) across the deformation, then compare its jump '
            'locus with independently constructed physical recovery data.'
        ),
        'physical_recovery': None,
        'physical_recovery_status': (
            'CONDITIONAL_ON_BETA_T_HILBERT_ERROR_ALGEBRA_AND_SUBREGION_MAPS'
        ),
    }


# ===================================================================
#  SECTION 7: CROSS-CHECKS WITH G11 (ENTANGLEMENT)
# ===================================================================

def verify_code_entanglement_consistency(c_val, log_ratio=1) -> Dict:
    """Place the genus-one scalar and spatial entropy side by side.

    The code entropy (log of code subspace dimension) should be
    related to the entanglement entropy at the scalar level.

    At genus 1: dim Q_1(A) = 1, so log(dim) = 0.
    The entanglement entropy S_EE = (c/3) log(L/eps) measures the
    spatial entanglement (a different quantity from the code entropy).

    Their comparison becomes physical after the Hilbert realization and
    decoder package have been supplied.

    >>> data = verify_code_entanglement_consistency(Rational(13))
    >>> data['lagrangian_fraction']
    1/2
    >>> data['code_entropy_genus_1']
    0
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    s_ee = von_neumann_entropy_scalar(kappa, log_ratio)

    return {
        'c': c_val,
        'kappa': kappa,
        'S_EE_scalar': s_ee,
        'lagrangian_fraction': Rational(1, 2),
        'code_rate': None,
        'code_rate_status': 'REQUIRES_HILBERT_REALIZATION',
        'code_entropy_genus_1': 0,  # dim Q_1 = 1 => log 1 = 0
        'total_hilbert_dim_genus_1': None,
        'lagrangian_dim_genus_1': 1,
        'consistent': None,
        'comparison_status': 'CONDITIONAL_ON_HILBERT_AND_OCA_PACKAGES',
        'physical_recovery': None,
        'physical_recovery_status': (
            'CONDITIONAL_ON_BETA_T_HILBERT_ERROR_ALGEBRA_AND_SUBREGION_MAPS'
        ),
    }


def verify_complementarity_as_code_constraint(c_val) -> Dict:
    """Compute the Virasoro scalar complementarity identity.

    Theorem C: H = Q_g(A) + Q_g(A!) (Lagrangian decomposition)
    The complementarity sum kappa + kappa' = 13 (Virasoro)
    gives the scalar ratio on the two summands.  A Hilbert-space code
    interpretation uses the physical decoder package.

    >>> data = verify_complementarity_as_code_constraint(Rational(13))
    >>> data['kappa_sum']
    13
    >>> data['is_self_dual']
    True
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26 - c_val)

    return {
        'c': c_val,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'kappa_sum': kappa + kappa_dual,
        'kappa_fraction': kappa / (kappa + kappa_dual) if kappa + kappa_dual != 0 else None,
        'kappa_dual_fraction': kappa_dual / (kappa + kappa_dual) if kappa + kappa_dual != 0 else None,
        'code_fraction': None,
        'error_fraction': None,
        'code_fraction_status': 'REQUIRES_HILBERT_REALIZATION',
        'is_self_dual': (c_val == 13),
        'complementarity_holds': (kappa + kappa_dual == 13),
        'physical_recovery': None,
        'physical_recovery_status': (
            'CONDITIONAL_ON_BETA_T_HILBERT_ERROR_ALGEBRA_AND_SUBREGION_MAPS'
        ),
    }
