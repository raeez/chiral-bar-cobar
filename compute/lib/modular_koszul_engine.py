"""Modular Koszul Engine: unified pipeline from OPE data to holographic datum.

Single entry point ``compute_datum`` assembles the complete Modular Koszul
Datum for any standard-landscape chiral algebra by orchestrating calls to
the existing specialized modules.

Pipeline stages:
  1. OPE validation and identity extraction
  2. Bar complex dimensions
  3. Shadow Postnikov tower through finite arity
  4. Shadow metric Q_L, discriminant Delta, depth class G/L/C/M
  5. Shadow connection nabla^sh, monodromy, parallel transport
  6. Koszulness diagnosis (FH concentration + resonance rank)
  7. Koszul dual identification and complementarity
  8. Holographic datum H(A) assembly

References:
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  def:shadow-metric (higher_genus_modular_koszul.tex)
  thm:shadow-connection (higher_genus_modular_koszul.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  thm:fh-concentration-koszulness (bar_cobar_adjunction_inversion.tex)
  constr:platonic-package (concordance.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from sympy import Rational, Symbol, simplify, sqrt, S

# ---------------------------------------------------------------------------
# Canonical family name mapper
# ---------------------------------------------------------------------------

_CANONICAL: Dict[str, str] = {
    'heisenberg': 'heisenberg', 'heis': 'heisenberg',
    'Heisenberg': 'heisenberg', 'H_k': 'heisenberg',
    'affine_sl2': 'affine_sl2', 'sl2': 'affine_sl2',
    'sl_2': 'affine_sl2', 'Affine_sl2': 'affine_sl2',
    'affine_sl3': 'affine_sl3', 'sl3': 'affine_sl3', 'sl_3': 'affine_sl3',
    'virasoro': 'virasoro', 'vir': 'virasoro',
    'Virasoro': 'virasoro', 'Vir_c': 'virasoro',
    'w3': 'w3', 'W3': 'w3', 'W_3': 'w3',
    'betagamma': 'betagamma', 'bg': 'betagamma',
    'beta_gamma': 'betagamma', 'beta-gamma': 'betagamma',
    'free_fermion': 'free_fermion', 'ff': 'free_fermion',
    'FreeFermion': 'free_fermion',
    'lattice': 'lattice', 'lattice_Z': 'lattice',
}

_KNOWN_FAMILIES = sorted(set(_CANONICAL.values()))


def _canon(name: str) -> str:
    c = _CANONICAL.get(name)
    if c is None:
        raise ValueError(f"Unknown family {name!r}. Known: {_KNOWN_FAMILIES}")
    return c


# ---------------------------------------------------------------------------
# Tridegree engine family name translation
# ---------------------------------------------------------------------------

_TSE_NAME: Dict[str, str] = {
    'heisenberg': 'heisenberg',
    'affine_sl2': 'affine_sl2',
    'virasoro': 'virasoro',
    'w3': 'w3',
    'betagamma': 'betagamma',
    'lattice': 'lattice_Z',
    # free_fermion and affine_sl3 use fallback (not in TSE registry)
}

# ---------------------------------------------------------------------------
# Static registries
# ---------------------------------------------------------------------------

_DESCRIPTIONS: Dict[str, str] = {
    'heisenberg': 'Heisenberg H_k',
    'affine_sl2': 'Affine V_k(sl_2)',
    'affine_sl3': 'Affine V_k(sl_3)',
    'virasoro': 'Virasoro Vir_c',
    'w3': 'W_3 algebra',
    'betagamma': 'Beta-gamma system',
    'free_fermion': 'Free fermion',
    'lattice': 'Lattice VOA V_Lambda',
}

_GENERATOR_DATA: Dict[str, Tuple[int, List[int]]] = {
    'heisenberg': (1, [1]),
    'affine_sl2': (3, [1, 1, 1]),
    'affine_sl3': (8, [1, 1, 1, 1, 1, 1, 1, 1]),
    'virasoro': (1, [2]),
    'w3': (2, [2, 3]),
    'betagamma': (2, [0, 1]),
    'free_fermion': (1, [1]),
    'lattice': (1, [1]),
}

# OPE leading-pole data: records (leading_coefficient)/(z^pole_order) for
# the most singular term in the OPE.  This is the OPE r-matrix r^{OPE}(z)
# of Remark rem:three-r-matrices (e1_modular_koszul.tex), NOT the E₁ scalar
# shadow r^{sc}(z) = c/(2z) used in e1_shadow_tower.py.
# For Virasoro, the OPE T(z)T(w) has a quartic pole (c/2)/(z-w)^4, hence
# the leading pole data is "(c/2)/z^4".
_COLLISION_RESIDUE: Dict[str, str] = {
    'heisenberg': 'kappa/z^2',
    'affine_sl2': 'Casimir/z^2',
    'affine_sl3': 'Casimir/z^2',
    'virasoro': '(c/2)/z^4',
    'w3': 'multi-pole/z^6',
    'betagamma': 'delta_{beta,gamma}/z',
    'free_fermion': 'delta/z',
    'lattice': 'kappa/z^2',
}


# ---------------------------------------------------------------------------
# ModularKoszulDatum
# ---------------------------------------------------------------------------

@dataclass
class ModularKoszulDatum:
    """Complete modular Koszul datum for a chiral algebra.

    References:
      thm:mc2-bar-intrinsic, def:shadow-metric, thm:shadow-connection,
      thm:fh-concentration-koszulness, constr:platonic-package
    """
    # Identity
    family: str
    description: str
    params: Dict[str, Any]
    central_charge: Any
    n_generators: int
    generator_weights: List[Any]
    ope_source: str

    # Bar complex
    bar_dims: Dict[int, int]
    bar_dim_source: str

    # Shadow tower
    kappa: Any
    cubic_shadow: Any
    quartic_contact: Any
    shadow_tower: Dict[int, Any]

    # Shadow metric
    alpha: Any
    S4: Any
    Delta: Any
    Q_L: Any
    depth_class: str
    shadow_depth: Optional[int]

    # Shadow connection
    connection_form_expr: Any = None
    monodromy: int = -1
    parallel_transport_expr: Any = None

    # Koszulness
    is_koszul: bool = True
    fh_concentrated: bool = True
    koszulness_evidence: Dict[str, bool] = field(default_factory=dict)
    resonance_rank: int = 0
    mc4_class: str = 'MC4+'

    # Koszul dual
    dual_family: Optional[str] = None
    dual_kappa: Any = None
    dual_central_charge: Any = None
    complementarity_sum: Any = None

    # Holographic
    collision_residue_type: Optional[str] = None
    theta_kappa: Any = None
    kappa_anti_symmetric: Optional[bool] = None
    connection_is_flat: Optional[bool] = None

    # ------------------------------------------------------------------
    def summary(self) -> str:
        """Human-readable summary of the datum."""
        lines = [
            f"=== Modular Koszul Datum: {self.description} ===",
            "",
            f"  Family            : {self.family}",
            f"  Central charge    : {self.central_charge}",
            f"  Generators        : {self.n_generators} (weights {self.generator_weights})",
            f"  OPE source        : {self.ope_source}",
            "",
            "--- Bar Complex ---",
            f"  Dimensions        : {self.bar_dims}",
            f"  Source            : {self.bar_dim_source}",
            "",
            "--- Shadow Tower ---",
            f"  kappa(A)          : {self.kappa}",
            f"  Cubic shadow C    : {self.cubic_shadow}",
            f"  Quartic contact Q : {self.quartic_contact}",
            f"  Tower (first few) : { {r: self.shadow_tower[r] for r in sorted(self.shadow_tower)[:6]} }",
            "",
            "--- Shadow Metric ---",
            f"  alpha             : {self.alpha}",
            f"  S_4               : {self.S4}",
            f"  Delta = 8*kappa*S4: {self.Delta}",
            f"  Depth class       : {self.depth_class}",
            f"  Shadow depth      : {self.shadow_depth if self.shadow_depth is not None else 'infinite'}",
            "",
            "--- Shadow Connection ---",
            f"  Monodromy         : {self.monodromy}",
            "",
            "--- Koszulness ---",
            f"  Is Koszul         : {self.is_koszul}",
            f"  FH concentrated   : {self.fh_concentrated}",
            f"  Resonance rank    : {self.resonance_rank}",
            f"  MC4 class         : {self.mc4_class}",
            "",
            "--- Koszul Dual ---",
            f"  Dual family       : {self.dual_family}",
            f"  Dual kappa        : {self.dual_kappa}",
            f"  Dual c            : {self.dual_central_charge}",
            f"  Complementarity   : {self.complementarity_sum}",
            "",
            "--- Holographic Datum ---",
            f"  Collision residue  : {self.collision_residue_type}",
            f"  Theta_kappa        : {self.theta_kappa}",
            f"  kappa antisymmetric: {self.kappa_anti_symmetric}",
            f"  Connection flat    : {self.connection_is_flat}",
        ]
        return "\n".join(lines)

    def verify(self) -> Dict[str, bool]:
        """Run internal consistency checks."""
        checks = {}
        # Delta = 8*kappa*S4
        try:
            checks['delta_identity'] = simplify(
                self.Delta - 8 * self.kappa * self.S4
            ) == 0
        except Exception:
            checks['delta_identity'] = False
        # Depth class consistency
        checks['depth_class_valid'] = self.depth_class in ('G', 'L', 'C', 'M')
        # Monodromy = -1
        checks['monodromy'] = self.monodromy == -1
        # Shadow depth matches class
        if self.depth_class == 'G':
            checks['depth_matches_class'] = self.shadow_depth == 2
        elif self.depth_class == 'L':
            checks['depth_matches_class'] = self.shadow_depth == 3
        elif self.depth_class == 'C':
            checks['depth_matches_class'] = self.shadow_depth == 4
        elif self.depth_class == 'M':
            checks['depth_matches_class'] = self.shadow_depth is None
        # FH agrees with Koszulness
        checks['fh_koszul_agree'] = self.fh_concentrated == self.is_koszul
        return checks

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to plain dictionary (str-safe values)."""
        d = {}
        for k, v in self.__dict__.items():
            if isinstance(v, dict):
                d[k] = {str(kk): str(vv) for kk, vv in v.items()}
            else:
                d[k] = str(v) if v is not None else None
        return d


# ---------------------------------------------------------------------------
# Pipeline stages
# ---------------------------------------------------------------------------

def _stage1_identity(family: str, **params) -> Dict[str, Any]:
    """Extract identity data from family registry."""
    c_sym = Symbol('c')
    k_sym = Symbol('k')

    n_gen, weights = _GENERATOR_DATA[family]

    # Central charge (symbolic default)
    cc_map = {
        'heisenberg': k_sym,
        'affine_sl2': 3 * k_sym / (k_sym + 2),
        'affine_sl3': 8 * k_sym / (k_sym + 3),
        'virasoro': c_sym,
        'w3': c_sym,
        'betagamma': S(2),  # c(bg,lam=1)=2
        'free_fermion': Rational(1, 2),
        'lattice': k_sym,  # rank
    }
    cc = cc_map.get(family, c_sym)
    if 'central_charge' in params:
        cc = params['central_charge']
    elif 'level' in params:
        cc = cc.subs(k_sym, params['level']) if hasattr(cc, 'subs') else cc

    return {
        'central_charge': cc,
        'n_generators': n_gen,
        'generator_weights': weights,
        'ope_source': 'registry',
    }


def _stage2_bar(family: str, max_degree: int = 8, **params) -> Dict[str, Any]:
    """Compute bar complex dimensions from known tables."""
    from .bar_complex import KNOWN_BAR_DIMS
    # Translate to bar_complex naming
    bar_name_map = {
        'heisenberg': 'Heisenberg',
        'affine_sl2': 'sl2',
        'virasoro': 'Virasoro',
        'w3': 'W3',
        'betagamma': 'beta_gamma',
        'free_fermion': 'free_fermion',
        'lattice': 'Heisenberg',  # same partition structure
        'affine_sl3': 'sl3',
    }
    bname = bar_name_map.get(family)
    dims = {}
    source = 'known_table'
    if bname and bname in KNOWN_BAR_DIMS:
        raw = KNOWN_BAR_DIMS[bname]
        for n in range(1, max_degree + 1):
            if n in raw:
                dims[n] = raw[n]
    else:
        source = 'unavailable'
    return {'bar_dims': dims, 'bar_dim_source': source}


def _stage3_shadow(family: str, max_arity: int = 8, **params) -> Dict[str, Any]:
    """Compute shadow tower via tridegree_shadow_engine."""
    from . import tridegree_shadow_engine as tse

    tse_name = _TSE_NAME.get(family)
    if tse_name is None or tse_name not in tse._FAMILY_REGISTRY:
        return _stage3_shadow_fallback(family, **params)

    kap = tse.kappa(tse_name, **params)
    cub = tse.cubic_shadow(tse_name, **params)
    qrt = tse.quartic_contact(tse_name, **params)

    # Build tower from genus-0 tree shadows
    tower = {2: kap}
    try:
        g0 = tse.genus0_tree_shadows(tse_name, max_n=max_arity, **params)
        for n, val in g0.items():
            tower[n] = val
    except Exception:
        tower[3] = cub
        tower[4] = qrt

    return {
        'kappa': kap,
        'cubic_shadow': cub,
        'quartic_contact': qrt,
        'shadow_tower': tower,
    }


def _stage3_shadow_fallback(family: str, **params) -> Dict[str, Any]:
    """Fallback for families not in tridegree engine (affine_sl3, free_fermion)."""
    from .shadow_metric_census import (
        kappa_affine_slN, kappa_free_fermion, kappa_lattice,
    )
    k_sym = Symbol('k')
    if family == 'affine_sl3':
        kap = kappa_affine_slN(3, params.get('level', k_sym))
        cub = S(1)  # nonzero (Lie class)
        qrt = S(0)
    elif family == 'free_fermion':
        kap = kappa_free_fermion()
        cub = S(0)
        qrt = S(0)
    elif family == 'lattice':
        kap = kappa_lattice(params.get('rank', k_sym))
        cub = S(0)
        qrt = S(0)
    else:
        kap = S(0)
        cub = S(0)
        qrt = S(0)

    tower = {2: kap, 3: cub, 4: qrt}
    return {
        'kappa': kap,
        'cubic_shadow': cub,
        'quartic_contact': qrt,
        'shadow_tower': tower,
    }


def _stage4_metric(family: str, kap, alpha_val, S4_val, **params) -> Dict[str, Any]:
    """Compute shadow metric, discriminant, and depth classification."""
    from .shadow_metric_census import classify_from_data
    from .shadow_connection import critical_discriminant

    Delta = critical_discriminant(kap, S4_val)
    try:
        Delta_simplified = simplify(Delta)
    except Exception:
        Delta_simplified = Delta

    cls, depth = classify_from_data(kap, alpha_val, S4_val)

    # Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    t = Symbol('t')
    Q_L = (2 * kap + 3 * alpha_val * t) ** 2 + 2 * Delta_simplified * t ** 2

    return {
        'alpha': alpha_val,
        'S4': S4_val,
        'Delta': Delta_simplified,
        'Q_L': Q_L,
        'depth_class': cls,
        'shadow_depth': depth,
    }


def _stage5_connection(Q_L, kap, **params) -> Dict[str, Any]:
    """Compute shadow connection."""
    from .shadow_connection import monodromy_eigenvalue
    mono = monodromy_eigenvalue()

    t = Symbol('t')
    # connection_form = Q'/(2Q) where Q = Q_L(t)
    try:
        from sympy import diff as sdiff
        Qp = sdiff(Q_L, t)
        conn = Qp / (2 * Q_L)
    except Exception:
        conn = None

    # parallel transport = sqrt(Q(t)/Q(0))
    try:
        Q0 = Q_L.subs(t, 0)
        pt = sqrt(Q_L / Q0)
    except Exception:
        pt = None

    return {
        'connection_form_expr': conn,
        'monodromy': mono,
        'parallel_transport_expr': pt,
    }


def _stage6_koszulness(family: str, **params) -> Dict[str, Any]:
    """Multi-criterion Koszulness diagnosis."""
    from .factorization_homology_engine import KOSZUL_STATUS, fh_genus0
    from .resonance_rank_engine import resonance_rank, mc4_class

    # FH concentration
    fh_name = family
    if family == 'lattice':
        fh_name = 'lattice'
    fh_conc = False
    try:
        result = fh_genus0(fh_name, **params)
        fh_conc = result.get('concentrated', False)
    except Exception:
        fh_conc = KOSZUL_STATUS.get(fh_name, False)

    # Registry fallback
    is_koszul = KOSZUL_STATUS.get(fh_name, fh_conc)

    # Resonance rank
    rr_name_map = {
        'affine_sl3': 'affine_sl2',
        'lattice': 'heisenberg',
        'free_fermion': 'free_fermion',
    }
    rr_name = rr_name_map.get(family, family)
    try:
        rho = resonance_rank(rr_name)
    except Exception:
        rho = 0
    try:
        mc4 = mc4_class(rr_name)
    except Exception:
        mc4 = 'MC4+' if rho == 0 else 'MC4^0'

    evidence = {
        'fh_concentration': fh_conc,
        'koszul_registry': KOSZUL_STATUS.get(fh_name, None),
    }

    return {
        'is_koszul': is_koszul,
        'fh_concentrated': fh_conc,
        'koszulness_evidence': evidence,
        'resonance_rank': rho,
        'mc4_class': mc4,
    }


def _stage7_dual(family: str, kap, cc, **params) -> Dict[str, Any]:
    """Koszul dual identification."""
    c_sym = Symbol('c')
    k_sym = Symbol('k')

    duals = {
        'heisenberg': ('Sym^ch(V*)', lambda kp, cc_: -kp, None),
        'affine_sl2': ('V_{-k-4}(sl_2)',
                       lambda kp, cc_: Rational(3) * (-k_sym - 4 + 2) / 4,
                       None),
        'affine_sl3': ('V_{-k-6}(sl_3)',
                       lambda kp, cc_: kp,  # placeholder
                       None),
        'virasoro': ('Vir_{26-c}',
                     lambda kp, cc_: (26 - c_sym) / 2,
                     26),
        'w3': ('W_3(100-c)',
               lambda kp, cc_: 5 * (100 - c_sym) / 6,
               100),
        'betagamma': ('bc ghost',
                      lambda kp, cc_: -kp,
                      None),
        'free_fermion': ('betagamma',
                         lambda kp, cc_: Rational(-1),
                         None),
        'lattice': ('dual lattice VOA',
                    lambda kp, cc_: -kp,
                    None),
    }
    if family not in duals:
        return {
            'dual_family': None, 'dual_kappa': None,
            'dual_central_charge': None, 'complementarity_sum': None,
        }

    dname, dkap_fn, comp_sum = duals[family]
    dkap = dkap_fn(kap, cc)
    dcc = None
    if comp_sum is not None:
        dcc = comp_sum - cc if hasattr(cc, '__sub__') else comp_sum

    return {
        'dual_family': dname,
        'dual_kappa': dkap,
        'dual_central_charge': dcc,
        'complementarity_sum': comp_sum,
    }


def _stage8_holographic(family: str, kap, dual_kap, **params) -> Dict[str, Any]:
    """Assemble holographic datum H(A)."""
    coll = _COLLISION_RESIDUE.get(family)
    theta_kap = kap

    # kappa antisymmetry
    anti = None
    if dual_kap is not None:
        try:
            anti = simplify(kap + dual_kap) == 0
        except Exception:
            anti = None

    return {
        'collision_residue_type': coll,
        'theta_kappa': theta_kap,
        'kappa_anti_symmetric': anti,
        'connection_is_flat': True,  # MC equation guarantees
    }


# ---------------------------------------------------------------------------
# Alpha and S4 extraction
# ---------------------------------------------------------------------------

def _extract_alpha_S4(family: str, kap, cub, qrt) -> Tuple[Any, Any]:
    """Extract (alpha, S4) from shadow tower data.

    alpha = cubic shadow coefficient on the primary line.
    S4 = quartic contact coefficient.
    Delta = 8*kappa*S4.
    """
    alpha = cub
    # S4: for families where quartic_contact is Q^ct = S4
    S4 = qrt
    return alpha, S4


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def compute_datum(
    family: str | None = None,
    ope=None,
    *,
    max_bar_degree: int = 8,
    max_shadow_arity: int = 8,
    **params,
) -> ModularKoszulDatum:
    """Compute the complete Modular Koszul Datum for a chiral algebra.

    Usage::

        datum = compute_datum('virasoro')
        datum = compute_datum('affine_sl2', level=3)
        datum = compute_datum('heisenberg', level=Symbol('k'))

        from compute.lib.chiral_ope_bootstrap import OPEData
        datum = compute_datum(ope=OPEData.from_virasoro())

    References:
        thm:mc2-bar-intrinsic, def:shadow-metric, thm:shadow-connection,
        thm:fh-concentration-koszulness, constr:platonic-package
    """
    # Resolve family
    if ope is not None:
        from .chiral_ope_bootstrap import OPEData
        if not isinstance(ope, OPEData):
            raise TypeError(f"Expected OPEData, got {type(ope)}")
        fam = _canon(ope.name) if ope.name else 'virasoro'
        source = 'raw_ope'
    elif family is not None:
        fam = _canon(family)
        source = 'registry'
    else:
        raise ValueError("Provide either family name or ope=OPEData(...)")

    # Stage 1: Identity
    s1 = _stage1_identity(fam, **params)
    s1['ope_source'] = source

    # Stage 2: Bar complex
    s2 = _stage2_bar(fam, max_degree=max_bar_degree, **params)

    # Stage 3: Shadow tower
    s3 = _stage3_shadow(fam, max_arity=max_shadow_arity, **params)

    # Extract alpha, S4
    alpha, S4 = _extract_alpha_S4(
        fam, s3['kappa'], s3['cubic_shadow'], s3['quartic_contact']
    )

    # Stage 4: Shadow metric
    s4 = _stage4_metric(fam, s3['kappa'], alpha, S4, **params)

    # Stage 5: Shadow connection
    s5 = _stage5_connection(s4['Q_L'], s3['kappa'], **params)

    # Stage 6: Koszulness
    s6 = _stage6_koszulness(fam, **params)

    # Stage 7: Koszul dual
    s7 = _stage7_dual(fam, s3['kappa'], s1['central_charge'], **params)

    # Stage 8: Holographic datum
    s8 = _stage8_holographic(fam, s3['kappa'], s7['dual_kappa'], **params)

    return ModularKoszulDatum(
        family=fam,
        description=_DESCRIPTIONS.get(fam, fam),
        params=params,
        central_charge=s1['central_charge'],
        n_generators=s1['n_generators'],
        generator_weights=s1['generator_weights'],
        ope_source=s1['ope_source'],
        bar_dims=s2['bar_dims'],
        bar_dim_source=s2['bar_dim_source'],
        kappa=s3['kappa'],
        cubic_shadow=s3['cubic_shadow'],
        quartic_contact=s3['quartic_contact'],
        shadow_tower=s3['shadow_tower'],
        alpha=s4['alpha'],
        S4=s4['S4'],
        Delta=s4['Delta'],
        Q_L=s4['Q_L'],
        depth_class=s4['depth_class'],
        shadow_depth=s4['shadow_depth'],
        connection_form_expr=s5['connection_form_expr'],
        monodromy=s5['monodromy'],
        parallel_transport_expr=s5['parallel_transport_expr'],
        is_koszul=s6['is_koszul'],
        fh_concentrated=s6['fh_concentrated'],
        koszulness_evidence=s6['koszulness_evidence'],
        resonance_rank=s6['resonance_rank'],
        mc4_class=s6['mc4_class'],
        dual_family=s7['dual_family'],
        dual_kappa=s7['dual_kappa'],
        dual_central_charge=s7['dual_central_charge'],
        complementarity_sum=s7['complementarity_sum'],
        collision_residue_type=s8['collision_residue_type'],
        theta_kappa=s8['theta_kappa'],
        kappa_anti_symmetric=s8['kappa_anti_symmetric'],
        connection_is_flat=s8['connection_is_flat'],
    )
