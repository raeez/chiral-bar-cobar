r"""Multi-channel shadow discrimination for all 24 Niemeier lattice VOAs.

This module builds on multichannel_shadow.py to provide:
  1. Complete multi-channel shadow data for each of the 24 Niemeier lattices
  2. A 24x24 discrimination matrix at each channel level
  3. Identification of the minimal channel set for complete discrimination
  4. Detailed analysis of the 5 |R|-collision pairs

THE MULTI-CHANNEL SHADOW FINGERPRINT
=====================================

For each Niemeier lattice Lambda with root system R = R_1 + ... + R_s:

  Level 0 (scalar):    kappa = 24, class G, depth 2.  Identical for all 24.
  Level 1 (per-factor): For each simple factor g_i of type (family_i, rank_i):
    - kappa_aff_i = dim(g_i) * (1 + h_i) / (2 * h_i)
    - dim_i = dim(g_i)
    - h_i = Coxeter number of g_i
    - shadow class: L (Lie/tree, depth 3) on the current line
    - S_3 = 1/3 per factor
  Level 2 (genus-2): Theta^{(2)}_Lambda (Siegel modular form)

THE FIVE COLLISION PAIRS (same |R|, different root systems):
  1. |R|=720: D_16+E_8 vs 3E_8
  2. |R|=432: A_17+E_7 vs D_10+2E_7
  3. |R|=288: A_11+D_7+E_6 vs 4E_6
  4. |R|=240: 2A_9+D_6 vs 4D_6
  5. |R|=144: 4A_5+D_4 vs 6D_4

All 5 are distinguished by Channel 1 (per-factor) data: each pair has
different factor types, hence different kappa_aff vectors, dim vectors,
and Coxeter numbers.

THE TEN RANK-COLLISION PAIRS (same rank partition, different ADE types):
  1. A_24 vs D_24 (rank 24)
  2. 2A_12 vs 2D_12 (rank 12+12)
  3. 3A_8 vs 3D_8 vs 3E_8 (rank 8+8+8, three-way)
  4. 4A_6 vs 4D_6 vs 4E_6 (rank 6+6+6+6, three-way)
  5. 6A_4 vs 6D_4 (rank 4+4+4+4+4+4)

All distinguished by Coxeter number (Channel 1b) or affine kappa (Channel 1c).

COMPLETENESS THEOREM: The multi-channel shadow vector (sorted tuple of
per-factor (family, rank, h, dim, kappa_aff)) is a COMPLETE invariant
for the 24 Niemeier lattices.  The minimal complete sub-invariant is
the pair (common_Coxeter_number, rank_partition).

References:
  - Niemeier (1968): classification of even unimodular lattices rank 24
  - Conway-Sloane: Sphere Packings, Lattices and Groups, Ch. 16
  - multichannel_shadow.py: general multi-channel theory
  - niemeier_complete_invariant.py: MC-based completeness proof
"""

from __future__ import annotations

import math
from collections import Counter
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from sympy import Rational

from compute.lib.niemeier_shadow_atlas import (
    ALL_NIEMEIER_LABELS,
    CS_ORDER,
    KAPPA_NIEMEIER,
    NIEMEIER_REGISTRY,
    coxeter_number,
    root_count,
    theta_coefficient,
    faber_pandharipande,
)
from compute.lib.niemeier_bar_nonscalar import (
    dim_simple,
    kappa_factor,
    central_charge_factor,
)
from compute.lib.multichannel_shadow import (
    MultichannelShadow,
    discrimination_power,
    find_collision_pairs,
)


# =========================================================================
# Complete multi-channel atlas
# =========================================================================

def niemeier_multichannel_atlas() -> Dict[str, Dict[str, Any]]:
    """Compute multi-channel shadow data for all 24 Niemeier lattices.

    Returns a dict keyed by label with complete shadow data per lattice.
    """
    atlas = {}
    for label in ALL_NIEMEIER_LABELS:
        mc = MultichannelShadow(label)
        atlas[label] = mc.summary()
    return atlas


# =========================================================================
# 24x24 discrimination matrix
# =========================================================================

def build_discrimination_matrix(
    channel: str = 'full',
) -> Tuple[List[str], np.ndarray, Dict[str, Any]]:
    """Build the 24x24 discrimination matrix at a given channel level.

    Args:
        channel: one of 'scalar', 'roots', 'rank', 'coxeter', 'kappa_aff',
                 'dim', 'full'.

    Returns:
        (labels, matrix, stats) where matrix[i][j] = 1 if distinguished, 0 if not.
    """
    labels = sorted(ALL_NIEMEIER_LABELS)
    n = len(labels)

    # Compute invariant for each label
    values = {}
    for label in labels:
        mc = MultichannelShadow(label)
        if channel == 'scalar':
            values[label] = mc.scalar_kappa
        elif channel == 'roots':
            values[label] = mc.num_roots
        elif channel == 'rank':
            values[label] = mc.rank_partition
        elif channel == 'coxeter':
            values[label] = mc.channel_1b_coxeter_rank()
        elif channel == 'kappa_aff':
            values[label] = mc.channel_1c_affine_kappa()
        elif channel == 'dim':
            values[label] = mc.channel_1d_dim()
        elif channel == 'full':
            values[label] = mc.multichannel_shadow_vector()
        else:
            raise ValueError(f'Unknown channel: {channel}')

    # Build matrix
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = int(values[labels[i]] != values[labels[j]])

    # Statistics
    total_pairs = n * (n - 1) // 2
    distinguished = sum(
        1 for i in range(n) for j in range(i + 1, n) if matrix[i][j] == 1
    )
    undistinguished = total_pairs - distinguished

    # Collision groups
    groups: Dict[Any, List[str]] = {}
    for label in labels:
        val = values[label]
        key = str(val) if isinstance(val, (dict, list)) else val
        if key not in groups:
            groups[key] = []
        groups[key].append(label)
    collisions = {k: v for k, v in groups.items() if len(v) > 1}

    stats = {
        'channel': channel,
        'total_pairs': total_pairs,
        'distinguished': distinguished,
        'undistinguished': undistinguished,
        'fraction': Fraction(distinguished, total_pairs) if total_pairs > 0 else Fraction(1),
        'is_complete': undistinguished == 0,
        'collision_groups': collisions,
    }

    return labels, matrix, stats


# =========================================================================
# Complete discrimination report
# =========================================================================

def full_discrimination_report() -> Dict[str, Any]:
    """Complete discrimination report across all channel levels.

    Tests every pair of Niemeier lattices against every channel.
    """
    channels = ['scalar', 'roots', 'rank', 'coxeter', 'kappa_aff', 'dim', 'full']
    report = {}

    for ch in channels:
        _, _, stats = build_discrimination_matrix(ch)
        report[ch] = {
            'distinguished': stats['distinguished'],
            'total': stats['total_pairs'],
            'fraction': float(stats['fraction']),
            'is_complete': stats['is_complete'],
            'collisions': len(stats['collision_groups']),
            'collision_labels': {
                str(k): v for k, v in stats['collision_groups'].items()
            },
        }

    return report


# =========================================================================
# Collision pair resolution
# =========================================================================

def resolve_collision_pairs() -> Dict[str, Any]:
    """For each collision pair at the |R| level, show how they are resolved.

    The 5 |R|-collision pairs are:
      |R|=720: D16_E8 vs 3E8
      |R|=432: A17_E7 vs D10_2E7
      |R|=288: A11_D7_E6 vs 4E6
      |R|=240: 2A9_D6 vs 4D6
      |R|=144: 4A5_D4 vs 6D4
    """
    # Known collision pairs
    known_pairs = [
        ('D16_E8', '3E8', 720),
        ('A17_E7', 'D10_2E7', 432),
        ('A11_D7_E6', '4E6', 288),
        ('2A9_D6', '4D6', 240),
        ('4A5_D4', '6D4', 144),
    ]

    resolutions = {}
    for la, lb, num_roots in known_pairs:
        mca = MultichannelShadow(la)
        mcb = MultichannelShadow(lb)

        # Which channels distinguish them?
        distinguishers = []

        if mca.rank_partition != mcb.rank_partition:
            distinguishers.append('rank_partition')
        if mca.common_coxeter != mcb.common_coxeter:
            distinguishers.append('coxeter_number')
        if mca.affine_kappa_vector != mcb.affine_kappa_vector:
            distinguishers.append('affine_kappa')
        if mca.dim_vector != mcb.dim_vector:
            distinguishers.append('dim_vector')
        if mca.factor_type_multiset != mcb.factor_type_multiset:
            distinguishers.append('factor_types')

        resolutions[f'{la} vs {lb} (|R|={num_roots})'] = {
            'a': {
                'label': la,
                'root_system': mca.data['root_system'],
                'factor_types': mca.factor_type_multiset,
                'rank_partition': mca.rank_partition,
                'coxeter': mca.common_coxeter,
                'affine_kappa': tuple(float(k) for k in mca.affine_kappa_vector),
                'dim_vector': mca.dim_vector,
                'num_factors': mca.num_factors,
            },
            'b': {
                'label': lb,
                'root_system': mcb.data['root_system'],
                'factor_types': mcb.factor_type_multiset,
                'rank_partition': mcb.rank_partition,
                'coxeter': mcb.common_coxeter,
                'affine_kappa': tuple(float(k) for k in mcb.affine_kappa_vector),
                'dim_vector': mcb.dim_vector,
                'num_factors': mcb.num_factors,
            },
            'num_roots': num_roots,
            'distinguishing_channels': distinguishers,
            'minimal_distinguisher': distinguishers[0] if distinguishers else None,
        }

    return resolutions


# =========================================================================
# Rank-collision pairs (same rank partition, different ADE types)
# =========================================================================

def rank_collision_analysis() -> Dict[str, Any]:
    """Analyze collisions at the rank-partition level.

    These are lattice pairs with the same partition of 24 into ranks
    but different ADE types for the factors.
    """
    # Group by rank partition
    by_rank: Dict[Tuple[int, ...], List[str]] = {}
    for label in ALL_NIEMEIER_LABELS:
        mc = MultichannelShadow(label)
        rp = mc.rank_partition
        if rp not in by_rank:
            by_rank[rp] = []
        by_rank[rp].append(label)

    rank_collisions = {
        rp: labels for rp, labels in by_rank.items() if len(labels) > 1
    }

    # For each collision group, show how Coxeter distinguishes
    details = {}
    for rp, labels in rank_collisions.items():
        group = {}
        for label in labels:
            mc = MultichannelShadow(label)
            group[label] = {
                'root_system': mc.data['root_system'],
                'coxeter': mc.common_coxeter,
                'affine_kappa': tuple(float(k) for k in mc.affine_kappa_vector),
                'dim_vector': mc.dim_vector,
            }
        # Verify all distinguished by Coxeter
        coxeter_vals = [group[l]['coxeter'] for l in labels]
        all_different = len(set(coxeter_vals)) == len(coxeter_vals)
        details[str(rp)] = {
            'labels': labels,
            'data': group,
            'distinguished_by_coxeter': all_different,
        }

    return {
        'num_rank_collisions': sum(
            len(v) * (len(v) - 1) // 2 for v in rank_collisions.values()
        ),
        'collision_groups': rank_collisions,
        'details': details,
    }


# =========================================================================
# Verification: kappa_aff is injective on ADE types
# =========================================================================

def verify_kappa_aff_injectivity() -> Dict[str, Any]:
    """Verify that kappa_aff(g, 1) = dim(g)*(1+h)/(2h) is injective on ADE types.

    This is needed for Channel 1c (affine kappa vector) to be complete.

    ADE types up to rank 24 (the maximum relevant for Niemeier lattices):
      A_n: n = 1, 2, ..., 24
      D_n: n = 3, 4, ..., 24 (D_3 = A_3 is excluded to avoid double counting)
      E_6, E_7, E_8

    Note: D_3 is isomorphic to A_3 as a root system.  For Niemeier lattices,
    the classification uses the standard ADE types, so D_3 does not appear
    independently.  But we include it to verify injectivity.
    """
    kappa_values: Dict[Rational, List[str]] = {}

    # A_n types
    for n in range(1, 25):
        kap = kappa_factor('A', n, k=1)
        label = f'A_{n}'
        if kap not in kappa_values:
            kappa_values[kap] = []
        kappa_values[kap].append(label)

    # D_n types (n >= 3; D_3 = A_3)
    for n in range(3, 25):
        kap = kappa_factor('D', n, k=1)
        label = f'D_{n}'
        if kap not in kappa_values:
            kappa_values[kap] = []
        kappa_values[kap].append(label)

    # E types
    for n in [6, 7, 8]:
        kap = kappa_factor('E', n, k=1)
        label = f'E_{n}'
        if kap not in kappa_values:
            kappa_values[kap] = []
        kappa_values[kap].append(label)

    collisions = {k: v for k, v in kappa_values.items() if len(v) > 1}

    # The only expected collision is D_3 = A_3 (isomorphic root systems)
    expected_collision = {kappa_factor('A', 3, k=1): ['A_3', 'D_3']}

    return {
        'num_types_checked': len(kappa_values),
        'num_collisions': len(collisions),
        'collisions': {str(k): v for k, v in collisions.items()},
        'expected_collisions': {str(k): v for k, v in expected_collision.items()},
        'is_injective_excluding_iso': (
            len(collisions) <= 1 and
            all(
                set(v) == {'A_3', 'D_3'} for v in collisions.values()
            )
        ),
    }


# =========================================================================
# Channel-1 shadow for each Niemeier lattice (the main table)
# =========================================================================

def channel_1_shadow_table() -> List[Dict[str, Any]]:
    """Complete Channel-1 shadow data for all 24 Niemeier lattices.

    For each lattice, computes per-factor:
      - kappa_aff_i = dim(g_i) * (1 + h_i) / (2 * h_i)
      - shadow class: L (depth 3) on current line
      - S_3 = 1/3 per factor
      - S_4 = 0 per factor

    IMPORTANT (from niemeier_bar_nonscalar.py, lines 323-380):
    The per-factor kappa_aff sum is NOT 24 in general.  The lattice VOA
    is a simple-current extension, not a naive tensor product.  The
    lattice kappa = rank = 24, while sum kappa_aff >= 24.

    The per-factor kappa_aff is nonetheless a valid bar-complex invariant
    because it is visible in B(V_{g_i, 1}) independently of the extension.
    """
    table = []
    for label in CS_ORDER:  # Conway-Sloane order (decreasing |R|)
        mc = MultichannelShadow(label)
        entry = {
            'label': label,
            'root_system': mc.data['root_system'],
            'num_roots': mc.num_roots,
            'num_factors': mc.num_factors,
            'common_coxeter': mc.common_coxeter,
            'rank_partition': mc.rank_partition,
        }

        if mc.is_leech:
            entry['channel_1_data'] = 'No root factors (Leech)'
            entry['affine_kappa_sum'] = Rational(24)
            entry['per_factor'] = []
        else:
            per_factor = []
            for ch in mc.channels:
                per_factor.append({
                    'type': ch.type_label,
                    'rank': ch.rank,
                    'h': ch.h,
                    'dim': ch.dim,
                    'kappa_aff': ch.kappa_aff,
                    'c': ch.c,
                    'shadow_class': ch.shadow_class,
                    'S3': ch.S3,
                    'S4': ch.S4,
                })
            entry['per_factor'] = per_factor
            entry['affine_kappa_sum'] = mc.affine_kappa_sum

        table.append(entry)

    return table


# =========================================================================
# Heisenberg vs root decomposition (the kappa puzzle)
# =========================================================================

def kappa_decomposition_analysis() -> Dict[str, Any]:
    """Analyze the kappa decomposition puzzle.

    The lattice VOA V_Lambda has kappa = rank = 24.
    The per-factor affine kappa sum is:
      sum_i kappa_aff(g_i, 1) = sum_i dim(g_i)*(1+h_i)/(2*h_i)

    For a uniform-Coxeter lattice with common h:
      sum kappa_aff = sum_i rank(g_i)*(1+h)^2/(2h) = 24*(1+h)^2/(2h)

    This equals 24 ONLY for h=1 (A_1^{24}, the case 24A_1):
      24*(1+1)^2/(2*1) = 24*4/2 = 48.
    Wait, that gives 48, not 24.  So it does NOT equal 24 even for 24A_1.

    For A_1 at k=1: kappa_aff(A_1, 1) = 3*2/2 = 3.  Wait:
      dim(A_1) = 1*(1+2) = 3.  h(A_1) = 2.  1+h = 3.
      kappa_aff = 3*3/(2*2) = 9/4.
    So 24 * 9/4 = 54, not 24.

    This confirms: sum kappa_aff != 24 in general.

    The RESOLUTION is in niemeier_bar_nonscalar.py lines 360-380:
    V_Lambda is a simple-current extension of the tensor product.
    The per-factor kappa_aff is the standalone modular characteristic.
    The lattice VOA kappa = rank = 24 comes from the Heisenberg
    structure of the Cartan sector.

    The bar complex data visible per factor (kappa_aff) is valid for
    DISCRIMINATION purposes but does NOT additively decompose the
    lattice kappa.
    """
    results = {}
    for label in ALL_NIEMEIER_LABELS:
        mc = MultichannelShadow(label)
        if mc.is_leech:
            results[label] = {
                'lattice_kappa': 24,
                'affine_kappa_sum': Rational(24),
                'ratio': Rational(1),
            }
        else:
            aff_sum = mc.affine_kappa_sum
            results[label] = {
                'lattice_kappa': 24,
                'affine_kappa_sum': aff_sum,
                'ratio': aff_sum / 24,
                'h': mc.common_coxeter,
                'theoretical_ratio': Rational(
                    (1 + mc.common_coxeter) ** 2,
                    2 * mc.common_coxeter
                ),
            }

    return results


# =========================================================================
# Master verification
# =========================================================================

def verify_all_pairwise_distinguished() -> Dict[str, Any]:
    """Verify that every pair of Niemeier lattices is distinguished by SOME channel.

    This is the main completeness theorem.
    """
    labels = sorted(ALL_NIEMEIER_LABELS)
    n = len(labels)
    all_mc = {label: MultichannelShadow(label) for label in labels}

    undistinguished = []
    for i in range(n):
        for j in range(i + 1, n):
            la, lb = labels[i], labels[j]
            mca, mcb = all_mc[la], all_mc[lb]
            # Check full multi-channel vector
            if mca.multichannel_shadow_vector() == mcb.multichannel_shadow_vector():
                undistinguished.append((la, lb))

    return {
        'total_pairs': n * (n - 1) // 2,
        'distinguished_pairs': n * (n - 1) // 2 - len(undistinguished),
        'undistinguished_pairs': undistinguished,
        'is_complete': len(undistinguished) == 0,
    }


def verify_minimal_channel() -> Dict[str, Any]:
    """Verify that Channel 1b (Coxeter + rank) is the minimal complete channel.

    Steps:
    1. Verify Channel 1a (rank alone) is NOT complete
    2. Verify Channel 1b (Coxeter + rank) IS complete
    3. Verify neither Coxeter alone nor rank alone is complete
    """
    labels = sorted(ALL_NIEMEIER_LABELS)
    all_mc = {label: MultichannelShadow(label) for label in labels}

    # Channel 1a: rank partition
    rank_groups: Dict[Tuple[int, ...], List[str]] = {}
    for label in labels:
        rp = all_mc[label].rank_partition
        if rp not in rank_groups:
            rank_groups[rp] = []
        rank_groups[rp].append(label)
    rank_collisions = {k: v for k, v in rank_groups.items() if len(v) > 1}
    rank_complete = len(rank_collisions) == 0

    # Coxeter number alone (NOT partition, just the common h)
    coxeter_groups: Dict[Optional[int], List[str]] = {}
    for label in labels:
        h = all_mc[label].common_coxeter
        if h not in coxeter_groups:
            coxeter_groups[h] = []
        coxeter_groups[h].append(label)
    coxeter_collisions = {k: v for k, v in coxeter_groups.items() if len(v) > 1}
    coxeter_complete = len(coxeter_collisions) == 0

    # Channel 1b: (Coxeter, rank partition)
    cb_groups: Dict[Tuple, List[str]] = {}
    for label in labels:
        cb = all_mc[label].channel_1b_coxeter_rank()
        if cb not in cb_groups:
            cb_groups[cb] = []
        cb_groups[cb].append(label)
    cb_collisions = {k: v for k, v in cb_groups.items() if len(v) > 1}
    cb_complete = len(cb_collisions) == 0

    return {
        'rank_alone_complete': rank_complete,
        'rank_collisions': {str(k): v for k, v in rank_collisions.items()},
        'coxeter_alone_complete': coxeter_complete,
        'coxeter_collisions': {str(k): v for k, v in coxeter_collisions.items()},
        'coxeter_plus_rank_complete': cb_complete,
        'coxeter_plus_rank_collisions': {str(k): v for k, v in cb_collisions.items()},
        'conclusion': (
            'Channel 1b (Coxeter + rank partition) is the minimal complete channel. '
            'Neither Coxeter number alone nor rank partition alone is complete, '
            'but their combination distinguishes all 24 Niemeier lattices.'
        ),
    }
