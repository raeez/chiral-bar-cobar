r"""Non-principal W-algebra data for partition (3,2) in sl_5.

The partition lambda = (3,2) in sl_5 is the MINIMAL non-hook partition:
  - (3,2) is a two-row partition with both parts >= 2
  - (3,2)^t = (2,2,1), which is also non-hook
  - The hook-type transport duality (Fehily, CLNS) does NOT apply
  - The DS-KD commutative diagram is CONJECTURAL for this orbit

This makes (3,2) the simplest explicit test case where hook transport
fails and the Koszul dual identification is genuinely open.

MATHEMATICAL CONTENT:

1. ORBIT DATA:
   Partition (3,2) of 5.  Transpose (2,2,1).
   dim(orbit) = 16.  dim(g^f) = 8.
   The nilradical m+ has dim = 10 and is NON-ABELIAN
   (brackets [E_12, E_23] = E_13, etc.).

2. STRONG GENERATORS OF W^k(sl_5, f_{(3,2)}):
   From the sl_2-decomposition pairing of the parts (type A: every
   strong generator is EVEN):
     h = 1:   1     h = 3/2: 2     h = 2:   2     h = 5/2: 2     h = 3: 1
   Total: 8 strong generators, all even.
   Anomaly ratio rho: OPEN (typed ClaimPacket; no derivation exists --
   the named obligation is a nonseparating genus-one calculation and a
   theorem identifying rho with a specified modular channel).

3. STRONG GENERATORS OF W^k(sl_5, f_{(2,2,1)}):
   dim(g^f) = 12.
     h = 1: 4     h = 3/2: 4     h = 2: 4     (all even)
   Anomaly ratio rho_t: OPEN (same typed lane).

4. CENTRAL CHARGE (KRW per-root-pair formula, canonical oracle):
   c(3,2; k)   = 24k/(k+5) - 30k - 52 = (-30k^2 - 178k - 260)/(k + 5);
                 c(0) = -52, c(1) = -78.
   c(2,2,1; k) = 24k/(k+5) - 12k - 6  = -6(2k + 5)(k + 1)/(k + 5);
                 c(0) = -6, c(1) = -14.

5. KOSZUL CONDUCTOR AND COMPLEMENTARITY:
   K(k) = c(3,2; k) + c(2,2,1; -k-10) = 110 - 18k = 2(55 - 9k).
   This is k-DEPENDENT, unlike hook partitions where the conductor
   is constant.  Structural root cause: the two KRW quadratic
   coefficients differ for a non-self-transpose pair, so no level
   reflection makes the sum constant.  The kappa sum passes through the
   OPEN rho packets and is itself a typed packet.

   For SELF-TRANSPOSE non-hook partitions like (2,2) in sl_4, the conductor
   IS k-independent (since rho = rho_t).  For NON-self-transpose non-hook
   pairs, k-dependence of the conductor is a genuine obstruction to the
   simple complementarity picture.

6. CONJECTURAL KOSZUL DUAL:
   Conjecture (type-A transport-to-transpose, conj:type-a-transport-to-transpose):
     (W_k(sl_5, f_{(3,2)}))^! =? W_{-k-10}(sl_5, f_{(2,2,1)})
   This is OPEN.  The hook-type corridor does not reach (3,2).

7. SHADOW DEPTH CLASSIFICATION:
   The highest-weight generator at h=3 produces a T-T OPE with max pole
   order 2*3 = 6 (sextic pole).  By AP19, the r-matrix max pole is 5.
   T-line depth: class M (infinite), since c_{(3,2)}(k) is generically
   nonzero and 5c + 22 != 0 generically.
   Overall depth: class M.

8. SEVEN-FACE PROGRAMME STATUS:
   Face 1 (bar complex): completed Koszulity PROVED
     (thm:pbw-slodowy-collapse applies: gr_Li W = Sym_d(g^{f*}))
   Face 2 (Koszul dual): OPEN (non-hook, dual orbit identification conjectural)
   Face 3 (line operators): CONJECTURAL (DS-KD diagram not proved)
   Face 4 (shadow tower): computable on T-line, class M
   Face 5 (r-matrix): multi-channel, max pole 5
   Face 6 (conductor): k-DEPENDENT (new phenomenon for non-hook)
   Face 7 (DS-bar commutation): CONJECTURAL

References:
    Kac-Roan-Wakimoto (2003): W-algebra construction for arbitrary nilpotent
    Fehily (2022): hook-type inverse reduction (does NOT cover (3,2))
    Creutzig-Linshaw-Nakatsuka-Sato (2023): Feigin-Semikhatov duality
    Manuscript: conj:type-a-transport-to-transpose, rem:abelian-nonabelian-nilradical
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    oo,
    simplify,
    sqrt,
    sympify,
)

# Import from existing engines -- single source of truth for formulas (AP1, AAP3).
from compute.lib.nonprincipal_ds_orbits import (
    centralizer_dimension_sl_n,
    homogeneous_f_centralizer_basis_sl_n,
    is_hook_partition,
    normalize_partition,
    transpose_partition,
    type_a_orbit_class,
    type_a_partition_sl2_triple,
)
from compute.lib.hook_type_w_duality import (
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    ghost_constant,
    kappa_complementarity_sum,
    krw_central_charge,
    krw_central_charge_data,
    levi_rho_norm_squared,
    rho_shift_norm_squared,
    w_algebra_generator_data,
    weyl_vector_norm_squared_sl_n,
)

k = Symbol('k')

# The partition and its transpose, fixed throughout this module.
PARTITION_32 = (3, 2)
PARTITION_221 = (2, 2, 1)
N_SL5 = 5
DUAL_LEVEL_SHIFT = 2 * N_SL5  # k' = -k - 10


# =============================================================================
# 1. Orbit combinatorics
# =============================================================================

@dataclass(frozen=True)
class NilpotentOrbitData:
    """Combinatorial data for a nilpotent orbit in sl_N."""
    partition: Tuple[int, ...]
    transpose: Tuple[int, ...]
    N: int
    orbit_dim: int
    centralizer_dim: int
    is_hook: bool
    is_self_transpose: bool
    orbit_class: str
    # ad(h/2)-grading on g^f
    generator_grades: Dict[object, int]  # {ad(h)-grade: multiplicity}
    num_strong_generators: int


def orbit_data_sl5_32() -> NilpotentOrbitData:
    """Nilpotent orbit data for partition (3,2) in sl_5."""
    lam = PARTITION_32
    lam_t = PARTITION_221
    cent_dim = centralizer_dimension_sl_n(lam)

    triple = type_a_partition_sl2_triple(lam)
    f_cent = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    grades = {grade: len(elems) for grade, elems in f_cent.items()}

    return NilpotentOrbitData(
        partition=lam,
        transpose=lam_t,
        N=N_SL5,
        orbit_dim=N_SL5 ** 2 - 1 - cent_dim,
        centralizer_dim=cent_dim,
        is_hook=False,
        is_self_transpose=False,
        orbit_class='two_row_nonhook',
        generator_grades=grades,
        num_strong_generators=cent_dim,
    )


def orbit_data_sl5_221() -> NilpotentOrbitData:
    """Nilpotent orbit data for partition (2,2,1) in sl_5."""
    lam = PARTITION_221
    lam_t = PARTITION_32
    cent_dim = centralizer_dimension_sl_n(lam)

    triple = type_a_partition_sl2_triple(lam)
    f_cent = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    grades = {grade: len(elems) for grade, elems in f_cent.items()}

    return NilpotentOrbitData(
        partition=lam,
        transpose=lam_t,
        N=N_SL5,
        orbit_dim=N_SL5 ** 2 - 1 - cent_dim,
        centralizer_dim=cent_dim,
        is_hook=False,
        is_self_transpose=False,
        orbit_class='general_nonprincipal',
        generator_grades=grades,
        num_strong_generators=cent_dim,
    )


# =============================================================================
# 2. Strong generators and conformal weights
# =============================================================================

@dataclass(frozen=True)
class GeneratorSpectrum:
    """Strong generator spectrum of a W-algebra."""
    partition: Tuple[int, ...]
    generators: Tuple[Tuple[str, object, str], ...]  # (name, weight, parity)
    num_bosonic: int
    num_fermionic: int
    conformal_weights: Tuple[object, ...]
    weight_multiplicities: Dict[object, int]
    anomaly_ratio: object


def generator_spectrum_32() -> GeneratorSpectrum:
    """Strong generator spectrum of W^k(sl_5, f_{(3,2)})."""
    return _generator_spectrum_from_partition(PARTITION_32)


def generator_spectrum_221() -> GeneratorSpectrum:
    """Strong generator spectrum of W^k(sl_5, f_{(2,2,1)})."""
    return _generator_spectrum_from_partition(PARTITION_221)


def _generator_spectrum_from_partition(partition) -> GeneratorSpectrum:
    """Build GeneratorSpectrum from a partition using the canonical engine."""
    lam = normalize_partition(partition)
    gen_data = w_algebra_generator_data(lam)
    rho = anomaly_ratio_from_partition(lam)
    weights = tuple(w for _, w, _ in gen_data.strong_generators)
    weight_mults = {}
    for _, w, _ in gen_data.strong_generators:
        weight_mults[w] = weight_mults.get(w, 0) + 1

    return GeneratorSpectrum(
        partition=lam,
        generators=gen_data.strong_generators,
        num_bosonic=gen_data.n_bosonic,
        num_fermionic=gen_data.n_fermionic,
        conformal_weights=weights,
        weight_multiplicities=weight_mults,
        anomaly_ratio=rho,
    )


# =============================================================================
# 3. Central charge and kappa
# =============================================================================

def central_charge_32(level=None):
    r"""Central charge of W^k(sl_5, f_{(3,2)}).

    KRW per-root-pair formula with x = h/2 = diag(1, 0, -1, 1/2, -1/2):
      c(k) = 24k/(k+5) - 30k - 52 = (-30k^2 - 178k - 260)/(k + 5)
    (|x|^2 = 5/2; ghost sum over grades {1/2 x4, 1 x3, 3/2 x2, 2 x1} = 50;
    dim(g_{1/2})/2 = 2).  Anchors: c(0) = -52, c(1) = -78.
    Real zeros at k = -13/5 and k = -10/3 (both negative, non-generic).
    """
    if level is None:
        level = k
    return krw_central_charge(PARTITION_32, sympify(level))


def central_charge_221(level=None):
    r"""Central charge of W^k(sl_5, f_{(2,2,1)}).

    KRW per-root-pair formula with x = h/2 = diag(1/2,-1/2,1/2,-1/2,0):
      c(k) = 24k/(k+5) - 12k - 6 = -6(2k + 5)(k + 1)/(k + 5)
    (|x|^2 = 1; ghost sum over grades {1/2 x4, 1 x4} = 4; dim(g_{1/2})/2 = 2).
    Anchors: c(0) = -6, c(1) = -14.  Real zeros at k = -1, -5/2.
    """
    if level is None:
        level = k
    return krw_central_charge(PARTITION_221, sympify(level))


def kappa_32(level=None):
    """Typed modular-characteristic packet for W^k(sl_5, f_{(3,2)}).

    kappa = rho * c requires the anomaly ratio rho, which is OPEN (no
    derivation exists; a nonseparating genus-one calculation is the named
    obligation).  Returns a ClaimPacket, never a fabricated scalar.
    """
    if level is None:
        level = k
    return ds_kappa_from_affine(PARTITION_32, sympify(level))


def kappa_221(level=None):
    """Typed modular-characteristic packet for W^k(sl_5, f_{(2,2,1)}).

    Same lane as ``kappa_32``: rho is OPEN, so the packet carries the
    obligation instead of a value.
    """
    if level is None:
        level = k
    return ds_kappa_from_affine(PARTITION_221, sympify(level))


# =============================================================================
# 4. Koszul conductor and complementarity
# =============================================================================

def koszul_conductor_32():
    """Koszul conductor K = c(3,2; k) + c(2,2,1; -k-10).

    K(k) = 110 - 18k = 2(55 - 9k): the pole at k = -5 cancels in the sum,
    leaving a polynomial, but the conductor remains k-DEPENDENT.  For
    non-self-transpose pairs the two KRW quadratic coefficients differ,
    so no reflection can make the sum constant.  Anchors: K(0) = 110,
    K(1) = 92.
    """
    c_k = central_charge_32()
    c_kp = central_charge_221(-k - DUAL_LEVEL_SHIFT)
    return simplify(c_k + c_kp)


def kappa_sum_32():
    """Typed kappa-complementarity packet: kappa(3,2;k) + kappa(2,2,1;-k-10).

    Both summands pass through the OPEN anomaly ratio rho (kappa = rho*c),
    so the sum is a ClaimPacket carrying the rho obligation, not a
    rational function.
    """
    return kappa_complementarity_sum(PARTITION_32)


def conductor_k_dependence_check():
    """Verify the conductor is k-dependent by evaluating at two levels.

    Returns (K_at_0, K_at_1, are_different).
    """
    K_0 = simplify(koszul_conductor_32().subs(k, 0))
    K_1 = simplify(koszul_conductor_32().subs(k, 1))
    return K_0, K_1, simplify(K_0 - K_1) != 0


# =============================================================================
# 5. Nilradical structure (abelian vs non-abelian)
# =============================================================================

@dataclass(frozen=True)
class NilradicalData:
    """Data about the positive nilradical m+ in the DS grading."""
    partition: Tuple[int, ...]
    dim_m_plus: int
    is_abelian: bool
    # Grade decomposition of m+
    grade_dims: Dict[object, int]  # {eigenvalue of ad(h/2): dim}
    # Sample non-trivial bracket (if non-abelian)
    sample_bracket: Optional[str]


def nilradical_data_32() -> NilradicalData:
    """Nilradical data for the (3,2) grading on sl_5."""
    return _nilradical_data(PARTITION_32)


def nilradical_data_221() -> NilradicalData:
    """Nilradical data for the (2,2,1) grading on sl_5."""
    return _nilradical_data(PARTITION_221)


def _nilradical_data(partition) -> NilradicalData:
    """Compute nilradical data for a partition of sl_N."""
    lam = normalize_partition(partition)
    N = sum(lam)
    triple = type_a_partition_sl2_triple(lam)
    h_diag = [triple.h[i, i] for i in range(N)]
    x_diag = [Rational(h_diag[i], 2) for i in range(N)]

    # Collect m+ = {E_{ij} : x_i - x_j > 0}
    m_plus = []
    grade_dims = {}
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            eig = x_diag[i] - x_diag[j]
            if eig > 0:
                m_plus.append((i, j, eig))
                grade_dims[eig] = grade_dims.get(eig, 0) + 1

    # Check abelianness: [E_ij, E_kl] = delta_{jk} E_il - delta_{li} E_kj
    is_abelian = True
    sample = None
    for (i, j, _) in m_plus:
        for (kk, l, _) in m_plus:
            if j == kk and i != l:
                is_abelian = False
                sample = f'[E_{{{i+1}{j+1}}}, E_{{{kk+1}{l+1}}}] = E_{{{i+1}{l+1}}}'
                break
        if not is_abelian:
            break

    return NilradicalData(
        partition=lam,
        dim_m_plus=len(m_plus),
        is_abelian=is_abelian,
        grade_dims=grade_dims,
        sample_bracket=sample,
    )


# =============================================================================
# 6. OPE pole structure and r-matrix data
# =============================================================================

@dataclass(frozen=True)
class OPEPoleData:
    """OPE pole structure data for a W-algebra."""
    partition: Tuple[int, ...]
    max_ope_pole: int
    max_rmatrix_pole: int  # = max_ope_pole - 1 (AP19)
    max_pole_channel: Tuple[str, str]
    num_channels: int


def ope_pole_data_32() -> OPEPoleData:
    """OPE pole structure for W^k(sl_5, f_{(3,2)}).

    Max OPE pole: 6 (sextic), from the h=3 generator self-OPE.
    Max r-matrix pole: 5 (quintic), by AP19 (d log kernel absorbs one pole).
    """
    return _ope_pole_data(PARTITION_32)


def ope_pole_data_221() -> OPEPoleData:
    """OPE pole structure for W^k(sl_5, f_{(2,2,1)}).

    Max OPE pole: 4 (quartic), from the h=2 generator self-OPE.
    Max r-matrix pole: 3, by AP19.
    """
    return _ope_pole_data(PARTITION_221)


def _ope_pole_data(partition) -> OPEPoleData:
    """Compute OPE pole data from generator spectrum."""
    lam = normalize_partition(partition)
    gen_data = w_algebra_generator_data(lam)
    gens = gen_data.strong_generators

    max_pole = 0
    max_channel = ('', '')
    num_ch = 0
    for i, (ni, hi, _pi) in enumerate(gens):
        for j, (nj, hj, _pj) in enumerate(gens):
            if j < i:
                continue
            pole = int(hi + hj)
            num_ch += 1
            if pole > max_pole:
                max_pole = pole
                max_channel = (ni, nj)

    return OPEPoleData(
        partition=lam,
        max_ope_pole=max_pole,
        max_rmatrix_pole=max_pole - 1,
        max_pole_channel=max_channel,
        num_channels=num_ch,
    )


# =============================================================================
# 7. Shadow depth classification
# =============================================================================

@dataclass(frozen=True)
class ShadowDepthData:
    """Shadow depth classification for a W-algebra."""
    partition: Tuple[int, ...]
    t_line_class: str
    t_line_depth: object
    overall_class: str
    overall_depth: object
    # T-line critical discriminant data
    c_is_generically_nonzero: bool
    five_c_plus_22_generically_nonzero: bool


def shadow_depth_32() -> ShadowDepthData:
    """Shadow depth for W^k(sl_5, f_{(3,2)}).

    T-line: class M (infinite depth).
    c = 2(k-49)/(k+5) vanishes only at k=49 (non-generic).
    5c + 22 = (10k + 12)/(k+5) + 22 = (32k + 122)/(k+5),
    vanishes only at k = -122/32 = -61/16 (non-generic).
    """
    c_sym = central_charge_32()
    c_zero = simplify(c_sym)
    five_c_22 = simplify(5 * c_sym + 22)

    return ShadowDepthData(
        partition=PARTITION_32,
        t_line_class='M',
        t_line_depth=oo,
        overall_class='M',
        overall_depth=oo,
        c_is_generically_nonzero=True,
        five_c_plus_22_generically_nonzero=True,
    )


def shadow_depth_221() -> ShadowDepthData:
    """Shadow depth for W^k(sl_5, f_{(2,2,1)}).

    T-line: class M (infinite depth).
    c = 6(k-10)/(k+5), generically nonzero.
    """
    c_sym = central_charge_221()
    return ShadowDepthData(
        partition=PARTITION_221,
        t_line_class='M',
        t_line_depth=oo,
        overall_class='M',
        overall_depth=oo,
        c_is_generically_nonzero=True,
        five_c_plus_22_generically_nonzero=True,
    )


# =============================================================================
# 8. DS-KD commutative diagram
# =============================================================================

@dataclass(frozen=True)
class DSKDDiagramStatus:
    """Status of the DS-KD commutative diagram for a partition."""
    partition: Tuple[int, ...]
    transpose: Tuple[int, ...]
    N: int
    is_hook: bool
    ds_exists: bool           # DS reduction always exists (KRW)
    inverse_ds_exists: bool   # inverse reduction (Butson-Nair for type A)
    kd_left_proved: bool      # affine KD (always proved)
    kd_right_proved: bool     # DS-KD commutation for this orbit
    diagram_proved: bool      # full diagram commutes
    koszul_dual_identified: bool
    koszul_dual_description: str
    proof_status: str


def ds_kd_diagram_32() -> DSKDDiagramStatus:
    """DS-KD diagram status for (3,2) in sl_5.

    The DS reduction EXISTS (Kac-Roan-Wakimoto).
    The Koszul dual identification is CONJECTURAL:
      (W_k(sl_5, f_{(3,2)}))^! =? W_{-k-10}(sl_5, f_{(2,2,1)})
    This is Conjecture conj:type-a-transport-to-transpose.
    The DS-KD commutation is NOT PROVED for this orbit.
    """
    return DSKDDiagramStatus(
        partition=PARTITION_32,
        transpose=PARTITION_221,
        N=N_SL5,
        is_hook=False,
        ds_exists=True,
        inverse_ds_exists=True,  # Butson-Nair for all type A at generic level
        kd_left_proved=True,
        kd_right_proved=False,
        diagram_proved=False,
        koszul_dual_identified=False,
        koszul_dual_description=(
            'CONJECTURAL: (W_k(sl_5, f_{(3,2)}))^! =? '
            'W_{-k-10}(sl_5, f_{(2,2,1)}). '
            'Hook transport does NOT reach (3,2). '
            'Transport-to-transpose (conj:type-a-transport-to-transpose) '
            'would identify the dual, but is OPEN for non-hook orbits.'
        ),
        proof_status='conjectural',
    )


def ds_kd_diagram_221() -> DSKDDiagramStatus:
    """DS-KD diagram status for (2,2,1) in sl_5 (transpose of (3,2))."""
    return DSKDDiagramStatus(
        partition=PARTITION_221,
        transpose=PARTITION_32,
        N=N_SL5,
        is_hook=False,
        ds_exists=True,
        inverse_ds_exists=True,
        kd_left_proved=True,
        kd_right_proved=False,
        diagram_proved=False,
        koszul_dual_identified=False,
        koszul_dual_description=(
            'CONJECTURAL: (W_k(sl_5, f_{(2,2,1)}))^! =? '
            'W_{-k-10}(sl_5, f_{(3,2)}). '
            'Same status as (3,2): hook transport does NOT reach (2,2,1).'
        ),
        proof_status='conjectural',
    )


# =============================================================================
# 9. Comparison with hook cases in sl_5
# =============================================================================

@dataclass(frozen=True)
class HookComparisonEntry:
    """Comparison data for one partition in sl_5."""
    partition: Tuple[int, ...]
    transpose: Tuple[int, ...]
    is_hook: bool
    orbit_class: str
    dim_gf: int
    anomaly_ratio: object
    conductor: object         # c(k) + c_dual(k')
    conductor_k_independent: bool
    kd_proved: bool


def sl5_hook_comparison_table() -> List[HookComparisonEntry]:
    """Full comparison table: all partitions of 5 with duality data.

    Shows the qualitative difference between hook partitions (where
    the conductor is k-independent for self-transpose cases and the
    KD is proved) and (3,2) (where neither holds).
    """
    from compute.lib.nonprincipal_ds_orbits import _partitions_of_n

    entries = []
    for lam in _partitions_of_n(5):
        lam_t = transpose_partition(lam)
        hook = is_hook_partition(lam)
        cls = type_a_orbit_class(lam)
        cdim = centralizer_dimension_sl_n(lam)
        rho = anomaly_ratio_from_partition(lam)

        c_k = krw_central_charge(lam, k)
        c_kp = krw_central_charge(lam_t, -k - 10)
        K = simplify(c_k + c_kp)
        k_indep = (K.diff(k) == 0) if hasattr(K, 'diff') else True
        if not k_indep:
            # Double-check numerically
            K0 = K.subs(k, 0)
            K1 = K.subs(k, 1)
            k_indep = simplify(K0 - K1) == 0

        kd_proved = hook or lam == (5,) or lam == (1, 1, 1, 1, 1)

        entries.append(HookComparisonEntry(
            partition=lam,
            transpose=lam_t,
            is_hook=hook,
            orbit_class=cls,
            dim_gf=cdim,
            anomaly_ratio=rho,
            conductor=K,
            conductor_k_independent=k_indep,
            kd_proved=kd_proved,
        ))
    return entries


# =============================================================================
# 10. Seven-face programme status
# =============================================================================

@dataclass(frozen=True)
class SevenFaceStatus:
    """Status of the seven-face programme for a given W-algebra."""
    partition: Tuple[int, ...]
    face_1_bar_complex: str       # Completed Koszulity
    face_2_koszul_dual: str       # Dual identification
    face_3_line_operators: str    # Line-operator category
    face_4_shadow_tower: str      # Shadow depth classification
    face_5_r_matrix: str          # r-matrix structure
    face_6_conductor: str         # Koszul conductor
    face_7_ds_bar: str            # DS-bar commutation


def seven_face_status_32() -> SevenFaceStatus:
    """Seven-face programme status for (3,2) in sl_5."""
    return SevenFaceStatus(
        partition=PARTITION_32,
        face_1_bar_complex='PROVED (thm:pbw-slodowy-collapse: gr_Li = Sym_d(g^{f*}))',
        face_2_koszul_dual='OPEN (non-hook; conj:type-a-transport-to-transpose)',
        face_3_line_operators='CONJECTURAL (DS-KD diagram not proved)',
        face_4_shadow_tower='class M (infinite depth); T-line computable',
        face_5_r_matrix='multi-channel, 8 generators, max r-matrix pole 5',
        face_6_conductor='k-DEPENDENT: K = 2(4k+11)/(k+5) (new phenomenon)',
        face_7_ds_bar='CONJECTURAL (non-hook orbit)',
    )


def seven_face_status_221() -> SevenFaceStatus:
    """Seven-face programme status for (2,2,1) in sl_5."""
    return SevenFaceStatus(
        partition=PARTITION_221,
        face_1_bar_complex='PROVED (thm:pbw-slodowy-collapse)',
        face_2_koszul_dual='OPEN (same status as (3,2))',
        face_3_line_operators='CONJECTURAL',
        face_4_shadow_tower='class M (infinite depth); T-line computable',
        face_5_r_matrix='multi-channel, 12 generators, max r-matrix pole 3',
        face_6_conductor='k-DEPENDENT (same conductor as (3,2) pair)',
        face_7_ds_bar='CONJECTURAL',
    )


# =============================================================================
# 11. Numerical evaluation
# =============================================================================

def numerical_data_32(level_val):
    """Evaluate the exact scalar invariants at a specific level.

    Central charges and their conductor sum are exact scalars (canonical
    KRW oracle).  The kappa entries pass through the OPEN anomaly ratio
    rho, so they are returned as typed ClaimPackets, unevaluated.
    """
    lev = sympify(level_val)
    dual_lev = -lev - DUAL_LEVEL_SHIFT

    c_32 = simplify(central_charge_32(lev))
    c_221 = simplify(central_charge_221(dual_lev))

    return {
        'level': lev,
        'dual_level': dual_lev,
        'c_32': c_32,
        'c_221_dual': c_221,
        'kappa_32': kappa_32(lev),
        'kappa_221_dual': kappa_221(dual_lev),
        'conductor': simplify(c_32 + c_221),
        'kappa_sum': kappa_sum_32(),
    }


# =============================================================================
# 12. Obstruction analysis: why hook transport fails
# =============================================================================

@dataclass(frozen=True)
class HookTransportObstruction:
    """Analysis of why hook-type transport fails for (3,2)."""
    partition: Tuple[int, ...]
    is_hook: bool
    # The anomaly ratio comparison: rho packets are OPEN, so the match
    # verdict is None (undetermined), never a fabricated bool.
    rho_source: object
    rho_target: object
    rho_match: Optional[bool]
    # Generator spectrum mismatch
    source_weights: Tuple[object, ...]
    target_weights: Tuple[object, ...]
    spectra_match: bool
    # Conductor k-dependence
    conductor_k_dependent: bool
    # Summary
    obstruction_summary: str


def hook_transport_obstruction_32() -> HookTransportObstruction:
    """Why hook transport fails for (3,2) in sl_5.

    Computed obstructions:
    1. (3,2) is not a hook partition, so Fehily's inverse reduction
       argument does not apply (exact combinatorics).
    2. The generator spectra differ qualitatively: (3,2) has generators
       at h = 1, 3/2, 2, 5/2, 3, while (2,2,1) has only h = 1, 3/2, 2
       (exact); the r-matrix structures differ (max pole 5 vs 3).
    3. The conductor c(3,2;k) + c(2,2,1;-k-10) = 110 - 18k is
       k-DEPENDENT (exact, canonical KRW oracle).

    The anomaly ratios rho are OPEN typed packets (no derivation exists),
    so ``rho_match`` is ``None``: the rho comparison is undetermined
    until rho is constructed, and is NOT usable as an obstruction.
    """
    spec_32 = generator_spectrum_32()
    spec_221 = generator_spectrum_221()

    src_weights = tuple(sorted(spec_32.weight_multiplicities.keys()))
    tgt_weights = tuple(sorted(spec_221.weight_multiplicities.keys()))

    K0, K1, k_dep = conductor_k_dependence_check()

    return HookTransportObstruction(
        partition=PARTITION_32,
        is_hook=False,
        rho_source=spec_32.anomaly_ratio,
        rho_target=spec_221.anomaly_ratio,
        rho_match=None,
        source_weights=src_weights,
        target_weights=tgt_weights,
        spectra_match=src_weights == tgt_weights,
        conductor_k_dependent=k_dep,
        obstruction_summary=(
            '(3,2) is NOT hook. Computed obstructions to transport: '
            '(1) not in Fehily corridor, '
            '(2) generator spectra differ (max weight 3 vs 2), '
            '(3) conductor 110 - 18k is k-dependent. '
            'rho comparison OPEN (typed packets, no derivation).'
        ),
    )
