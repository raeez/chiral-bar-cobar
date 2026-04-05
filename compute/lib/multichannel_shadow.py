r"""Multi-channel shadow extraction for lattice VOAs.

The scalar shadow obstruction tower projects Theta_A onto a single primary line,
yielding kappa = 24 identically for all 24 Niemeier lattices.  This
module extracts the FULL multi-channel shadow data by decomposing
the bar complex along the root system.

MATHEMATICAL FRAMEWORK
======================

For a lattice VOA V_Lambda with root system R = R_1 + ... + R_s
(direct sum of simple components, all with common Coxeter number h):

  V_Lambda  =  simple-current extension of  tensor_{i=1}^s V_1(g_i)

where V_1(g_i) is the level-1 affine VOA of type g_i.

PRIMARY FIELD CHANNELS
======================

Channel 0 (Vacuum/Virasoro): The stress tensor T.  Generates the
  scalar shadow obstruction tower.  For lattice VOAs: kappa = 24, class G,
  shadow depth 2.  Identical for all 24.

Channel 1 (Weight-1 currents): The 24 Cartan generators j^a plus
  |R| root vectors e^alpha.  Total dimension: 24 + |R|.
  The weight-1 currents j^a have Heisenberg OPE: purely bilinear,
  class G on each line.  The root vectors e^alpha have non-abelian
  OPE (Lie bracket): class L on the current line.

Channel 2 (Lattice vertex operators): For short roots (alpha^2 = 2),
  the vertex operators e^alpha are already in Channel 1 as root vectors.
  For longer vectors alpha with alpha^2 >= 4, the vertex operators
  have weight alpha^2/2 >= 2.

PER-FACTOR SHADOW DECOMPOSITION
================================

The key observation: the bar complex decomposes along the root system.
Each simple factor g_i of the root system R contributes:

  (a) Per-factor kappa:  For the lattice VOA, the per-factor
      contribution to kappa is rank(g_i) (NOT kappa(g_i, 1)),
      because the lattice VOA kappa = rank = 24, and this decomposes
      additively as sum rank(g_i) = 24.

      The per-factor AFFINE kappa (from the standalone V_1(g_i))
      is kappa_aff(g_i, 1) = dim(g_i)*(1+h_i)/(2*h_i), which
      sums to MORE than 24 in general.  The difference arises because
      V_Lambda is a simple-current extension, not a naive tensor product.

  (b) Per-factor shadow class:  Each V_1(g_i) on its current line
      is class L (Lie/tree, depth 3, alpha=1, S_3=1/3, S_4=0).
      But in the lattice VOA, the combined shadow on the SINGLE primary
      line is class G (the Lie brackets from different factors cancel
      via the bilinear Heisenberg structure of the Cartan sector).

  (c) Per-factor bar dimension:  dim H^1(B(V_{g_i, 1})) = dim(g_i),
      the Lie algebra dimension of g_i.

THE MULTI-CHANNEL SHADOW VECTOR
================================

For discrimination, we define the multi-channel shadow vector:

  S_mc(Lambda) = sorted tuple of {(type_i, rank_i, h_i, dim_i, kappa_aff_i)}

This is redundant (type_i determines all others), but each component
is independently visible in the bar complex:
  - rank_i: from the Cartan subalgebra contribution to kappa
  - h_i: from the PBW filtration degree on H^1(B(V_{g_i, 1}))
  - dim_i: from the weight-1 bar dimension of the i-th factor
  - kappa_aff_i: the modular characteristic of the standalone factor

COMPLETENESS: The multi-channel shadow vector is a complete invariant
for the 24 Niemeier lattices (see niemeier_complete_invariant.py for proof).

MINIMAL DISTINGUISHING CHANNELS
=================================

Among the channels available:
  - Channel 0 (scalar kappa): power 0/24
  - Channel 0+ (scalar tower): power 0/24
  - Channel 1a (per-factor rank partition): power 14/24
  - Channel 1b (per-factor Coxeter number): power 24/24 (COMPLETE
    when combined with rank partition, by Niemeier's theorem)
  - Channel 1c (per-factor affine kappa): power 24/24 (COMPLETE
    since kappa_aff is injective on ADE types)
  - Channel 1d (per-factor dim): power 24/24 (COMPLETE since dim
    is injective on ADE types)
  - Channel 2 (genus-2 theta): distinguishes |R|-collision pairs

The minimal complete channel set is {Channel 1b} (Coxeter numbers),
combined with the partition of 24 into ranks.  Equivalently,
{Channel 1c} (affine kappas) alone suffices.

References:
  - niemeier_shadow_atlas.py: scalar shadow data
  - niemeier_bar_nonscalar.py: per-factor bar complex data
  - niemeier_complete_invariant.py: completeness proofs
  - shadow_channel_decomposition.py: general multi-channel theory
  - higher_genus_modular_koszul.tex: thm:shadow-channel-decomposition
"""

from __future__ import annotations

import math
from collections import Counter
from fractions import Fraction
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

from sympy import Rational

from compute.lib.niemeier_shadow_atlas import (
    ALL_NIEMEIER_LABELS,
    CS_ORDER,
    KAPPA_NIEMEIER,
    NIEMEIER_REGISTRY,
    coxeter_number,
    root_count,
)
from compute.lib.niemeier_bar_nonscalar import (
    dim_simple,
    kappa_factor,
    central_charge_factor,
    factor_decomposition,
)


# =========================================================================
# Multi-channel shadow data structure
# =========================================================================

class ChannelShadow:
    """Shadow data for a single channel (one simple factor of the root system).

    For a simple Lie algebra g of ADE type at level k = 1:
      - rank: Cartan rank of g
      - h: Coxeter number
      - dim: dimension of g = rank + |roots|
      - kappa_aff: modular characteristic of V_1(g) = dim*(1+h)/(2h)
      - c: central charge of V_1(g) = rank (for simply-laced at k=1)
      - shadow_class: 'L' (Lie/tree, depth 3) on the current line
      - S3: cubic shadow on current line = 1/3
      - S4: quartic shadow = 0 (Jacobi identity)
    """

    def __init__(self, family: str, rank: int, level: int = 1):
        self.family = family
        self.rank = rank
        self.level = level

        self.h = coxeter_number(family, rank)
        self.dim = dim_simple(family, rank)
        self.n_roots = root_count(family, rank)
        self.kappa_aff = kappa_factor(family, rank, k=level)
        self.c = central_charge_factor(family, rank, k=level)
        self.shadow_class = 'L'  # All affine KM are class L on current line
        self.S3 = Rational(1, 3)  # Universal for affine KM on current line
        self.S4 = Rational(0)  # Jacobi identity kills quartic

    @property
    def type_label(self) -> str:
        return f'{self.family}_{self.rank}'

    def as_tuple(self) -> Tuple:
        """Canonical tuple representation for comparison."""
        return (self.family, self.rank, self.h, self.dim, self.kappa_aff)

    def __repr__(self) -> str:
        return (f'ChannelShadow({self.type_label}: rank={self.rank}, '
                f'h={self.h}, dim={self.dim}, kappa_aff={self.kappa_aff})')


# =========================================================================
# Multi-channel shadow for a lattice VOA
# =========================================================================

class MultichannelShadow:
    """Multi-channel shadow extraction for a lattice VOA V_Lambda.

    Given a Niemeier lattice Lambda with root system R = R_1 + ... + R_s,
    computes the channel-projected shadow data for each simple factor.

    The scalar (Channel 0) shadow is kappa = 24 for all 24 lattices.
    The per-factor (Channel 1) shadow carries the root system information.
    """

    def __init__(self, label: str):
        if label not in NIEMEIER_REGISTRY:
            raise ValueError(f'Unknown Niemeier lattice: {label}')

        self.label = label
        self.data = NIEMEIER_REGISTRY[label]
        self.components = self.data['components']

        # Build per-factor channel shadows
        self.channels: List[ChannelShadow] = []
        for fam, n in self.components:
            self.channels.append(ChannelShadow(fam, n, level=1))

    @property
    def num_factors(self) -> int:
        return len(self.channels)

    @property
    def is_leech(self) -> bool:
        return self.num_factors == 0

    # ----- Channel 0: Scalar shadow (universal) -----

    @property
    def scalar_kappa(self) -> int:
        """Channel 0: scalar kappa = 24 for all Niemeier lattices."""
        return KAPPA_NIEMEIER

    @property
    def scalar_shadow_class(self) -> str:
        """Channel 0: shadow class = G for all lattice VOAs."""
        return 'G'

    @property
    def scalar_shadow_depth(self) -> int:
        """Channel 0: shadow depth = 2 for all lattice VOAs."""
        return 2

    # ----- Channel 1: Per-factor shadow data -----

    @property
    def rank_partition(self) -> Tuple[int, ...]:
        """Sorted partition of 24 into per-factor ranks."""
        if self.is_leech:
            return ()
        return tuple(sorted([ch.rank for ch in self.channels], reverse=True))

    @property
    def coxeter_numbers(self) -> Tuple[int, ...]:
        """Sorted Coxeter numbers of all factors."""
        if self.is_leech:
            return ()
        return tuple(sorted([ch.h for ch in self.channels], reverse=True))

    @property
    def common_coxeter(self) -> Optional[int]:
        """Common Coxeter number (all factors have the same h by Niemeier)."""
        if self.is_leech:
            return None
        return self.channels[0].h

    @property
    def affine_kappa_vector(self) -> Tuple[Rational, ...]:
        """Sorted per-factor affine kappa values.

        kappa_aff(g_i, 1) = dim(g_i) * (1 + h_i) / (2 * h_i).
        This is a COMPLETE invariant: injective on ADE types.
        """
        if self.is_leech:
            return ()
        return tuple(sorted([ch.kappa_aff for ch in self.channels]))

    @property
    def affine_kappa_sum(self) -> Rational:
        """Sum of per-factor affine kappas.

        NOT equal to 24 in general (differs from lattice kappa = rank = 24).
        """
        if self.is_leech:
            return Rational(24)
        return sum(ch.kappa_aff for ch in self.channels)

    @property
    def dim_vector(self) -> Tuple[int, ...]:
        """Sorted per-factor Lie algebra dimensions."""
        if self.is_leech:
            return ()
        return tuple(sorted([ch.dim for ch in self.channels]))

    @property
    def total_lie_dim(self) -> int:
        """Total Lie algebra dimension = sum dim(g_i)."""
        return sum(ch.dim for ch in self.channels)

    @property
    def weight_1_bar_dim(self) -> int:
        """Dimension of weight-1 sector of bar complex = 24 + |R|."""
        return 24 + self.data['num_roots']

    @property
    def num_roots(self) -> int:
        return self.data['num_roots']

    @property
    def factor_type_multiset(self) -> Tuple[Tuple[str, int, int], ...]:
        """Canonical multiset of (family, rank, multiplicity)."""
        count: Dict[Tuple[str, int], int] = {}
        for ch in self.channels:
            key = (ch.family, ch.rank)
            count[key] = count.get(key, 0) + 1
        return tuple(sorted(
            (fam, n, mult) for (fam, n), mult in count.items()
        ))

    # ----- Multi-channel shadow vector (the main invariant) -----

    def multichannel_shadow_vector(self) -> Tuple:
        """The complete multi-channel shadow vector.

        Returns a sorted tuple of per-factor channel data,
        which is a COMPLETE invariant for all 24 Niemeier lattices.
        """
        if self.is_leech:
            return ('Leech',)
        return tuple(sorted(ch.as_tuple() for ch in self.channels))

    # ----- Channel 1 sub-channels -----

    def channel_1a_rank_partition(self) -> Tuple[int, ...]:
        """Channel 1a: rank partition alone. Power: 14/24."""
        return self.rank_partition

    def channel_1b_coxeter_rank(self) -> Tuple[Optional[int], Tuple[int, ...]]:
        """Channel 1b: (common Coxeter, rank partition). Power: 24/24 (COMPLETE)."""
        return (self.common_coxeter, self.rank_partition)

    def channel_1c_affine_kappa(self) -> Tuple[Rational, ...]:
        """Channel 1c: sorted affine kappa vector. Power: 24/24 (COMPLETE)."""
        return self.affine_kappa_vector

    def channel_1d_dim(self) -> Tuple[int, ...]:
        """Channel 1d: sorted dimension vector. Power: 24/24 (COMPLETE)."""
        return self.dim_vector

    def channel_2_genus2_theta(self) -> int:
        """Channel 2: genus-2 representation number r_2(diag(1,1)).

        Distinguishes some |R|-collision pairs beyond genus-1 theta.
        """
        from compute.lib.niemeier_shadow_atlas import genus2_diag11_rep
        return genus2_diag11_rep(self.label)

    # ----- Genus-g per-channel shadow -----

    def genus_g_per_channel(self, g: int) -> Dict[str, Any]:
        """Per-channel genus-g shadow data.

        At genus g, the scalar shadow is F_g = 24 * lambda_g^FP.
        The per-channel contribution from factor i is rank(g_i) * lambda_g^FP
        (since each factor contributes its rank to the total kappa = 24).

        The per-factor AFFINE shadow would be kappa_aff(g_i) * lambda_g^FP,
        but this does NOT sum to F_g = 24 * lambda_g^FP.

        The correct per-factor contribution to the lattice VOA shadow is
        kappa_lattice(g_i) = rank(g_i), giving:
          F_g = sum_i rank(g_i) * lambda_g^FP = 24 * lambda_g^FP.
        """
        from compute.lib.niemeier_shadow_atlas import faber_pandharipande
        if g < 1:
            raise ValueError(f'Genus must be >= 1, got {g}')
        lambda_g = faber_pandharipande(g)
        per_channel = {}
        for ch in self.channels:
            key = ch.type_label
            if key in per_channel:
                per_channel[key] = {
                    'kappa_lattice': per_channel[key]['kappa_lattice'] + ch.rank,
                    'shadow_g': per_channel[key]['shadow_g'] + Rational(ch.rank) * lambda_g,
                    'multiplicity': per_channel[key]['multiplicity'] + 1,
                }
            else:
                per_channel[key] = {
                    'kappa_lattice': ch.rank,
                    'shadow_g': Rational(ch.rank) * lambda_g,
                    'multiplicity': 1,
                }

        return {
            'genus': g,
            'total_shadow': Rational(24) * lambda_g,
            'lambda_g': lambda_g,
            'per_channel': per_channel,
        }

    # ----- Summary -----

    def summary(self) -> Dict[str, Any]:
        """Complete summary of multi-channel shadow data."""
        return {
            'label': self.label,
            'root_system': self.data['root_system'],
            'num_roots': self.num_roots,
            'num_factors': self.num_factors,
            'is_leech': self.is_leech,
            # Channel 0
            'scalar_kappa': self.scalar_kappa,
            'scalar_class': self.scalar_shadow_class,
            'scalar_depth': self.scalar_shadow_depth,
            # Channel 1
            'rank_partition': self.rank_partition,
            'common_coxeter': self.common_coxeter,
            'affine_kappa_vector': self.affine_kappa_vector,
            'affine_kappa_sum': self.affine_kappa_sum,
            'dim_vector': self.dim_vector,
            'total_lie_dim': self.total_lie_dim,
            'weight_1_bar_dim': self.weight_1_bar_dim,
            'factor_types': self.factor_type_multiset,
            # Invariants
            'multichannel_vector': self.multichannel_shadow_vector(),
        }


# =========================================================================
# Discrimination engine
# =========================================================================

def compute_all_multichannel() -> Dict[str, MultichannelShadow]:
    """Compute multi-channel shadow for all 24 Niemeier lattices."""
    return {label: MultichannelShadow(label) for label in ALL_NIEMEIER_LABELS}


def discrimination_matrix(
    channel_func,
    labels: Optional[List[str]] = None,
) -> Tuple[List[str], List[List[bool]]]:
    """Build 24x24 discrimination matrix for a channel function.

    channel_func: function label -> hashable invariant value.
    Entry (i,j) is True if channel_func distinguishes lattice i from j.
    """
    if labels is None:
        labels = sorted(ALL_NIEMEIER_LABELS)
    values = {lab: channel_func(lab) for lab in labels}
    n = len(labels)
    matrix = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = True
            else:
                matrix[i][j] = (values[labels[i]] != values[labels[j]])
    return labels, matrix


def discrimination_power(
    channel_func,
    labels: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Compute discriminating power of a channel function.

    Returns: pairs distinguished, total pairs, collision groups, completeness.
    """
    if labels is None:
        labels = sorted(ALL_NIEMEIER_LABELS)
    values = {lab: channel_func(lab) for lab in labels}

    groups: Dict[Any, List[str]] = {}
    for lab in labels:
        val = values[lab]
        # Make hashable
        if isinstance(val, dict):
            key = str(sorted(val.items()))
        elif isinstance(val, list):
            key = tuple(val)
        else:
            key = val
        if key not in groups:
            groups[key] = []
        groups[key].append(lab)

    collisions = {k: v for k, v in groups.items() if len(v) > 1}
    n = len(labels)
    total_pairs = n * (n - 1) // 2
    undistinguished = sum(
        len(v) * (len(v) - 1) // 2 for v in collisions.values()
    )
    distinguished = total_pairs - undistinguished

    return {
        'distinguished_pairs': distinguished,
        'total_pairs': total_pairs,
        'fraction': Fraction(distinguished, total_pairs) if total_pairs > 0 else Fraction(1),
        'is_complete': undistinguished == 0,
        'num_collision_groups': len(collisions),
        'collision_groups': {str(k): v for k, v in collisions.items()},
        'num_distinct_values': len(groups),
    }


def find_collision_pairs(
    channel_func,
    labels: Optional[List[str]] = None,
) -> List[Tuple[str, str]]:
    """Find all pairs not distinguished by a channel function."""
    if labels is None:
        labels = sorted(ALL_NIEMEIER_LABELS)
    values = {lab: channel_func(lab) for lab in labels}
    pairs = []
    for i, la in enumerate(labels):
        for lb in labels[i + 1:]:
            va = values[la]
            vb = values[lb]
            if isinstance(va, dict):
                va = str(sorted(va.items()))
            if isinstance(vb, dict):
                vb = str(sorted(vb.items()))
            if va == vb:
                pairs.append((la, lb))
    return pairs


# =========================================================================
# Channel function wrappers (for use with discrimination engine)
# =========================================================================

def _channel_0(label: str) -> int:
    """Channel 0: scalar kappa. Power: 0/24."""
    return KAPPA_NIEMEIER


def _channel_0_tower(label: str) -> Tuple[int, ...]:
    """Channel 0+: full scalar tower. Power: 0/24."""
    return (KAPPA_NIEMEIER, 0, 0, 0, 0, 0, 0, 0)


def _channel_1a(label: str) -> Tuple[int, ...]:
    """Channel 1a: rank partition. Power: 14/24."""
    return MultichannelShadow(label).channel_1a_rank_partition()


def _channel_1b(label: str) -> Tuple:
    """Channel 1b: (Coxeter, rank partition). Power: 24/24."""
    return MultichannelShadow(label).channel_1b_coxeter_rank()


def _channel_1c(label: str) -> Tuple:
    """Channel 1c: affine kappa vector. Power: 24/24."""
    return MultichannelShadow(label).channel_1c_affine_kappa()


def _channel_1d(label: str) -> Tuple[int, ...]:
    """Channel 1d: dimension vector. Power: 24/24."""
    return MultichannelShadow(label).channel_1d_dim()


def _channel_full(label: str) -> Tuple:
    """Full multi-channel vector. Power: 24/24."""
    return MultichannelShadow(label).multichannel_shadow_vector()


def _num_roots(label: str) -> int:
    """Number of roots. Power: 19/24."""
    return NIEMEIER_REGISTRY[label]['num_roots']


# =========================================================================
# All-channel discrimination analysis
# =========================================================================

def full_discrimination_analysis() -> Dict[str, Any]:
    """Run discrimination analysis for all channel levels.

    Returns a comprehensive report on which channels distinguish what.
    """
    channels = {
        'Channel 0 (scalar kappa)': _channel_0,
        'Channel 0+ (scalar tower)': _channel_0_tower,
        'Channel 1a (rank partition)': _channel_1a,
        'Channel 1b (Coxeter + rank)': _channel_1b,
        'Channel 1c (affine kappa)': _channel_1c,
        'Channel 1d (dim vector)': _channel_1d,
        'Full multi-channel': _channel_full,
        'Num roots (theta series)': _num_roots,
    }

    results = {}
    for name, func in channels.items():
        dp = discrimination_power(func)
        results[name] = {
            'distinguished': dp['distinguished_pairs'],
            'total': dp['total_pairs'],
            'fraction': float(dp['fraction']),
            'is_complete': dp['is_complete'],
            'collisions': dp['num_collision_groups'],
        }

    return results


# =========================================================================
# Collision pair analysis
# =========================================================================

def collision_pair_analysis() -> Dict[str, Any]:
    """Detailed analysis of collision pairs at each channel level.

    The 5 known |R|-collision pairs:
      |R|=720:  D16_E8 vs 3E8
      |R|=432:  A17_E7 vs D10_2E7
      |R|=288:  A11_D7_E6 vs 4E6
      |R|=240:  2A9_D6 vs 4D6
      |R|=144:  4A5_D4 vs 6D4

    These are ALL distinguished by Channel 1 (per-factor) data.
    """
    root_collisions = find_collision_pairs(_num_roots)
    rank_collisions = find_collision_pairs(_channel_1a)
    coxeter_collisions = find_collision_pairs(_channel_1b)
    kappa_collisions = find_collision_pairs(_channel_1c)

    details = {}
    for la, lb in root_collisions:
        mca = MultichannelShadow(la)
        mcb = MultichannelShadow(lb)
        details[f'{la} vs {lb}'] = {
            'num_roots': mca.num_roots,
            'rank_partition_a': mca.rank_partition,
            'rank_partition_b': mcb.rank_partition,
            'coxeter_a': mca.common_coxeter,
            'coxeter_b': mcb.common_coxeter,
            'affine_kappa_a': tuple(float(k) for k in mca.affine_kappa_vector),
            'affine_kappa_b': tuple(float(k) for k in mcb.affine_kappa_vector),
            'dim_a': mca.dim_vector,
            'dim_b': mcb.dim_vector,
            'distinguished_by_rank': mca.rank_partition != mcb.rank_partition,
            'distinguished_by_coxeter': mca.common_coxeter != mcb.common_coxeter,
            'distinguished_by_kappa': mca.affine_kappa_vector != mcb.affine_kappa_vector,
            'distinguished_by_dim': mca.dim_vector != mcb.dim_vector,
        }

    return {
        'root_collision_pairs': root_collisions,
        'rank_collision_pairs': rank_collisions,
        'coxeter_collision_pairs': coxeter_collisions,
        'kappa_collision_pairs': kappa_collisions,
        'details': details,
        'summary': {
            'root_collisions': len(root_collisions),
            'rank_collisions': len(rank_collisions),
            'coxeter_collisions': len(coxeter_collisions),
            'kappa_collisions': len(kappa_collisions),
        }
    }


# =========================================================================
# Minimal distinguishing channel set
# =========================================================================

def minimal_distinguishing_channels() -> Dict[str, Any]:
    """Find the minimal channel set that distinguishes all 24 Niemeier lattices.

    The hierarchy of channels:
      Channel 0 (kappa): 0 pairs distinguished
      Channel 0+ (tower): 0 pairs distinguished
      |R| (roots): 19/24 distinguished (5 collision pairs)
      Channel 1a (rank): 14/24 (10 collision pairs)
      Channel 1b (Coxeter+rank): 24/24 COMPLETE
      Channel 1c (kappa_aff): 24/24 COMPLETE
      Channel 1d (dim): 24/24 COMPLETE

    The minimal SINGLE complete channel is 1b, 1c, or 1d (all equivalent
    in power for ADE types, since the ADE map (family, rank) -> each of
    these is injective).

    But the minimal INFORMATION needed is the common Coxeter number h
    (a single integer) plus the rank partition (a partition of 24):
    this is 1b, and it is PROVABLY minimal by Niemeier's theorem.
    """
    # Check each channel independently
    channels = [
        ('Channel 0 (kappa)', _channel_0),
        ('|R| (root count)', _num_roots),
        ('Channel 1a (rank partition)', _channel_1a),
        ('Channel 1b (Coxeter + rank)', _channel_1b),
        ('Channel 1c (affine kappa)', _channel_1c),
        ('Channel 1d (dim vector)', _channel_1d),
    ]

    results = []
    for name, func in channels:
        dp = discrimination_power(func)
        results.append({
            'channel': name,
            'distinguished': dp['distinguished_pairs'],
            'total': dp['total_pairs'],
            'is_complete': dp['is_complete'],
            'num_distinct': dp['num_distinct_values'],
        })

    # Find first complete channel
    minimal = None
    for r in results:
        if r['is_complete']:
            minimal = r['channel']
            break

    return {
        'channel_hierarchy': results,
        'minimal_complete_channel': minimal,
        'reason': (
            'Channel 1b (common Coxeter number h plus rank partition) '
            'is the minimal complete invariant by Niemeier\'s classification theorem. '
            'Equivalently, Channel 1c (sorted affine kappa vector) or '
            'Channel 1d (sorted dimension vector) suffice, since the map '
            '(family, rank) -> kappa_aff is injective on ADE types.'
        ),
    }
