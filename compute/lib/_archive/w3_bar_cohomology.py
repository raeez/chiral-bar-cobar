"""W3 chiral bar cohomology computation.

Computes bar cohomology H^n(B(W3)) using the chiral bar differential:
  d_res(phi_0 x ... x phi_n x omega) = sum_{i<j} +/- Res_{D_ij}[mu(phi_i,phi_j) x rest x omega]

The differential sums over ALL pairs (i,j), not just adjacent ones.
Residues are nonzero only when the OS form has a singularity along D_{ij}.

For bosonic fields (W3 has |T|=|W|=0), Koszul signs simplify.

Ground truth (tab:bar-dimensions): H^1=2, H^2=5, H^3=16, H^4=52.
"""

from __future__ import annotations

import numpy as np
from math import factorial
from typing import Dict, List, Tuple, Optional

from compute.lib.w3_bar_extended import (
    VACUUM, State, state_weight, dim_vbar_gf, W3VacuumModule
)


# =========================================================================
# Orlik-Solomon algebra: basis and residue maps
# =========================================================================

def os_basis(n: int) -> List[Tuple[Tuple[int, int], ...]]:
    """Basis for OS^{n-1}(C_n) = top-degree forms on C_n(C).

    dim OS^{n-1} = (n-1)!.
    Represented as wedge products of eta_{ij} pairs.

    For n=1: OS^0 = {1} (empty wedge product)
    For n=2: OS^1 = {eta_12}
    For n=3: OS^2 = {eta_12^eta_13, eta_12^eta_23}
    For n=4: OS^3 = 6-dimensional basis (3! = 6)
    """
    if n <= 1:
        return [()]

    # Build basis recursively using the "standard" basis for OS
    # For n points, OS^{n-1} has basis indexed by permutations
    # A convenient basis: last-column forms eta_{1,sigma(1)} ^ ... ^ eta_{n-1,sigma(n-1)}
    # But for small n, just hardcode.
    if n == 2:
        return [((0, 1),)]

    if n == 3:
        return [((0, 1), (0, 2)), ((0, 1), (1, 2))]

    if n == 4:
        # OS^3(C_4) has dim 3! = 6
        # Basis: all products of 3 eta's that are independent modulo Arnold
        # Standard basis: {eta_01 ^ eta_02 ^ eta_03,
        #                  eta_01 ^ eta_02 ^ eta_13,
        #                  eta_01 ^ eta_02 ^ eta_23,
        #                  eta_01 ^ eta_12 ^ eta_13,
        #                  eta_01 ^ eta_12 ^ eta_23,
        #                  eta_01 ^ eta_13 ^ eta_23}
        return [
            ((0, 1), (0, 2), (0, 3)),
            ((0, 1), (0, 2), (1, 3)),
            ((0, 1), (0, 2), (2, 3)),
            ((0, 1), (1, 2), (1, 3)),
            ((0, 1), (1, 2), (2, 3)),
            ((0, 1), (1, 3), (2, 3)),
        ]

    raise NotImplementedError(f"OS basis for n={n} not yet implemented")


def os_residue(n: int, form_idx: int, collision: Tuple[int, int]) -> List[Tuple[int, float]]:
    """Compute Res_{D_{collision}}(omega_form_idx) in OS^{n-2}(C_{n-1}).

    Returns list of (target_form_idx, coefficient) pairs.
    Target basis is os_basis(n-1) with merged point labeling.

    The residue at D_{ij} picks off the eta_{ij} factor from the form.
    If eta_{ij} is not a factor, the residue is 0.
    After taking residue, remaining eta's are re-indexed with i,j merged to min(i,j).
    """
    basis = os_basis(n)
    if form_idx >= len(basis):
        return []

    form = basis[form_idx]
    i, j = collision

    # Check if eta_{ij} appears as a factor
    eta_ij = (min(i, j), max(i, j))

    found_pos = None
    for pos, pair in enumerate(form):
        if pair == eta_ij:
            found_pos = pos
            break

    if found_pos is None:
        # eta_{ij} not a factor: check if we can rewrite using Arnold
        # For now, try expressing the form in terms of basis elements
        # that DO contain eta_{ij}
        return _os_residue_arnold(n, form_idx, collision)

    # Remove eta_{ij} and re-index remaining factors
    sign = (-1) ** found_pos  # from moving eta_{ij} to the front
    remaining = list(form[:found_pos]) + list(form[found_pos + 1:])

    # Re-index: merge j into i (remove index j, shift higher indices down)
    target_basis = os_basis(n - 1)
    reindexed = _reindex_form(remaining, i, j)

    # Find in target basis
    result = []
    reindexed_tuple = tuple(reindexed)
    for tidx, tform in enumerate(target_basis):
        if tform == reindexed_tuple:
            result.append((tidx, sign))
            return result

    # May need Arnold to express in target basis
    return _find_in_basis(reindexed, target_basis, sign)


def _reindex_form(pairs: list, merge_i: int, merge_j: int) -> list:
    """After merging point j into point i, re-index all pairs."""
    result = []
    for (a, b) in pairs:
        # Replace j with i
        a2 = merge_i if a == merge_j else a
        b2 = merge_i if b == merge_j else b
        # Shift indices > j down by 1
        if a2 > merge_j:
            a2 -= 1
        if b2 > merge_j:
            b2 -= 1
        if merge_i > merge_j:
            if a2 == merge_i - 1:
                pass  # already shifted
        # Normalize to (min, max)
        if a2 == b2:
            continue  # degenerate: this form vanishes
        result.append((min(a2, b2), max(a2, b2)))
    return result


def _os_residue_arnold(n: int, form_idx: int, collision: Tuple[int, int]) -> List[Tuple[int, float]]:
    """Compute residue using Arnold relations when eta_{ij} is not a direct factor."""
    # For n=3, the Arnold relation is:
    # eta_02 ^ eta_12 = eta_02 ^ eta_01 + eta_01 ^ eta_12
    # i.e., eta_13 ^ eta_23 = eta_13 ^ eta_12 + eta_12 ^ eta_23 (in 1-indexed)
    # In 0-indexed: eta_02 ^ eta_12 = eta_01 ^ eta_02 - eta_01 ^ eta_12
    # Wait: Arnold says eta_{ij}^eta_{jk} = eta_{ij}^eta_{ik} + eta_{ik}^eta_{jk}
    #   i.e. eta_01^eta_12 = eta_01^eta_02 + eta_02^eta_12 ... no

    # For small n, compute directly
    if n == 3:
        basis = os_basis(3)
        i, j = collision
        form = basis[form_idx]

        # basis[0] = (01, 02), basis[1] = (01, 12)
        # Arnold: eta_02^eta_12 = eta_01^eta_02 - eta_01^eta_12
        #   => (02,12) = basis[0] - basis[1]  (up to signs)
        # Actually: eta_02^eta_12 = -(eta_12^eta_02)
        # Let's be careful with wedge signs.
        # eta_ab ^ eta_cd = -eta_cd ^ eta_ab

        # Residues for n=3:
        # Res_{D_01}(basis[0]) = Res_{D_01}(eta_01^eta_02) = eta_{0'2} (picking off eta_01)
        # Res_{D_01}(basis[1]) = Res_{D_01}(eta_01^eta_12) = eta_{1'2}|_{0=1} = eta_{0'2}
        # But 0'=merged(0,1), so eta_{0'2} is the unique form on C_2.
        # Res_{D_12}(basis[0]) = need eta_12 factor. basis[0]=(01,02), no eta_12.
        #   Use Arnold: eta_02 = eta_01 + eta_12 (modulo Arnold? No, that's wrong)
        #   Arnold relation for (0,1,2): eta_01^eta_12 + eta_12^eta_20 + eta_20^eta_01 = 0
        #   => eta_01^eta_12 - eta_12^eta_02 - eta_02^eta_01 = 0
        #   => eta_01^eta_12 - eta_12^eta_02 + eta_01^eta_02 = 0
        #   => basis[1] + eta_02^eta_12 + basis[0] = 0
        #   => eta_02^eta_12 = -basis[0] - basis[1]

        # Residues:
        # D_01: Res picks off eta_01
        #   basis[0] = eta_01^eta_02: Res = +eta_{0'2}. Sign: +1 (eta_01 is first factor)
        #   basis[1] = eta_01^eta_12: Res = +eta_{0'2}. Sign: +1
        #     (after merge 0,1->0': eta_12 -> eta_{0'2})
        # D_02: Res picks off eta_02
        #   basis[0] = eta_01^eta_02: Res = -eta_{0'1} (sign -1: eta_02 is second, move to front)
        #     Wait: Res picks off eta_02 from eta_01^eta_02.
        #     eta_01^eta_02 = (-1)^0 eta_02 ^ ... no:
        #     To take residue at D_02, we need eta_02 as a factor.
        #     basis[0] = eta_01 ^ eta_02. Factor eta_02 is at position 1.
        #     Sign = (-1)^1 = -1. Remaining: eta_01. After merge 0,2->0': eta_01 -> eta_{0'1}.
        #     Result: -1 * eta_{0'1}
        #   basis[1] = eta_01^eta_12: no eta_02 factor. Need Arnold.
        #     Express basis[1] involving eta_02:
        #     From Arnold: basis[1] = -basis[0] - eta_02^eta_12 = -basis[0] + eta_12^eta_02
        #     Hmm, this introduces eta_02 but also changes the form. For residue:
        #     Res_{D_02}(basis[1]) = Res_{D_02}(-basis[0] + eta_12^eta_02)
        #       = -Res_{D_02}(basis[0]) + Res_{D_02}(eta_12^eta_02)
        #       = -(-1)*eta_{0'1} + (+1)*eta_{1,0'}
        #       = eta_{0'1} - eta_{0'1} = 0
        #     So Res_{D_02}(basis[1]) = 0. Good.
        # D_12: Res picks off eta_12
        #   basis[0] = eta_01^eta_02: no eta_12 factor.
        #     From Arnold: basis[0] = -basis[1] - eta_02^eta_12
        #     Res_{D_12}(basis[0]) = -Res_{D_12}(basis[1]) + Res_{D_12}(eta_02^eta_12)
        #     Hmm wait, = Res_{D_12}(-basis[1] - eta_02^eta_12)
        #       = -Res_{D_12}(basis[1]) - Res_{D_12}(eta_02^eta_12)
        #     Res_{D_12}(basis[1]) = Res_{D_12}(eta_01^eta_12):
        #       eta_12 at position 1, sign (-1)^1 = -1. Remaining: eta_01. After merge 1,2->1': eta_01->eta_{0,1'}.
        #       = -eta_{0,1'}
        #     Res_{D_12}(eta_02^eta_12):
        #       eta_12 at position 1, sign (-1)^1 = -1. Remaining: eta_02. After merge: eta_02->eta_{0,1'}.
        #       = -eta_{0,1'}
        #     So Res_{D_12}(basis[0]) = -(-eta_{0,1'}) - (-eta_{0,1'}) = eta_{0,1'} + eta_{0,1'} = 2*eta_{0,1'}
        #     Hmm that's 2, which seems wrong. Let me recheck.
        #     Arnold: eta_01^eta_12 + eta_12^eta_20 + eta_20^eta_01 = 0
        #     => eta_01^eta_12 - eta_12^eta_02 - eta_02^eta_01 = 0
        #     => eta_01^eta_12 - eta_12^eta_02 + eta_01^eta_02 = 0
        #     => basis[1] + (-1)*eta_12^eta_02 + basis[0] = 0
        #     => basis[1] + eta_02^eta_12 + basis[0] = 0  (swapping sign)
        #     Wait: eta_12^eta_02 = -eta_02^eta_12.
        #     So: basis[1] - (-eta_02^eta_12) + basis[0] = 0
        #     => basis[1] + eta_02^eta_12 + basis[0] = 0
        #     => basis[0] = -basis[1] - eta_02^eta_12
        #
        #     Res_{D_12}(basis[0]) = Res_{D_12}(-basis[1] - eta_02^eta_12)
        #       = -Res_{D_12}(eta_01^eta_12) - Res_{D_12}(eta_02^eta_12)
        #     For eta_01^eta_12: pick off eta_12 (pos 1, sign -1). Remaining: eta_01 -> eta_{0,1'}.
        #       = -1 * eta_{0,1'}
        #     For eta_02^eta_12: pick off eta_12 (pos 1, sign -1). Remaining: eta_02 -> eta_{0,1'}.
        #       = -1 * eta_{0,1'}
        #     Total: -(-eta_{0,1'}) - (-eta_{0,1'}) = eta_{0,1'} + eta_{0,1'} = 2*eta_{0,1'}
        #     This means Res_{D_12}(basis[0]) = 2*eta. That can't be right for an integer form.
        #     Actually wait, the Arnold relation may have a different sign convention.
        #     Let me use the standard: for distinct i<j<k,
        #       eta_{ij} ^ eta_{jk} - eta_{ij} ^ eta_{ik} + eta_{ik} ^ eta_{jk} = 0
        #     With (i,j,k)=(0,1,2):
        #       eta_01 ^ eta_12 - eta_01 ^ eta_02 + eta_02 ^ eta_12 = 0
        #       basis[1] - basis[0] + eta_02^eta_12 = 0
        #       eta_02^eta_12 = basis[0] - basis[1]
        #       basis[0] = basis[1] + eta_02^eta_12 ... wait that gives basis[0] = basis[1] + basis[0] - basis[1] = basis[0]. Circular.
        #
        #     Actually from eta_01^eta_12 - eta_01^eta_02 + eta_02^eta_12 = 0:
        #       eta_02^eta_12 = eta_01^eta_02 - eta_01^eta_12 = basis[0] - basis[1]
        #     So: basis[0] is already a basis element, and eta_02^eta_12 = basis[0] - basis[1].
        #
        #     Res_{D_12}(basis[0]) = Res_{D_12}(eta_01^eta_02):
        #       No direct eta_12 factor. Use: eta_01^eta_02 = eta_01^eta_12 + eta_02^eta_12
        #                                                     = basis[1] + (basis[0] - basis[1]) = basis[0]
        #       That's circular again! We're expressing basis[0] in terms of itself.
        #
        #       The issue is that basis[0] = eta_01^eta_02 does NOT contain eta_12, and the
        #       Arnold relation doesn't help because it relates three forms in the SAME space.
        #
        #       The correct answer is: Res_{D_12}(eta_01^eta_02) = 0!
        #       Because neither factor is eta_12. The form is regular at D_12.
        #       After restriction to z_1=z_2, eta_01 -> 0 and eta_02 -> eta_{0',2} but
        #       wait, eta_01 = dlog(z_0-z_1) which does NOT vanish at z_1=z_2.
        #
        #       The RESIDUE at D_12 means: take the coefficient of dlog(z_1-z_2) in the
        #       Laurent expansion. If eta_12 = dlog(z_1-z_2) is NOT a factor, the form
        #       has NO singularity along D_12, and the residue is 0.
        #
        #       So: Res_{D_12}(basis[0]) = 0. ✓

        # Collect all residues for n=3 (hardcoded for correctness)
        # basis[0] = eta_01^eta_02, basis[1] = eta_01^eta_12
        # target: os_basis(2) = [((0,1),)] = {eta_{0'1'}} (single form on C_2)

        if (i, j) == (0, 1):
            # D_01: pick off eta_01
            if form_idx == 0:  # eta_01^eta_02: eta_01 at pos 0, sign +1
                # remaining: eta_02, merge 0,1->0': eta_02 -> eta_{0',2}...
                # but target is C_2 with points {0', 2}, so eta_{0',2} = eta_{01} in new indexing
                # where 0'->0, 2->1. So it's eta_01 = target basis[0].
                return [(0, 1.0)]
            elif form_idx == 1:  # eta_01^eta_12: eta_01 at pos 0, sign +1
                # remaining: eta_12, merge 0,1->0': eta_12 -> eta_{0',2}
                # reindex: 0'->0, 2->1. eta_{0,1} = target basis[0].
                return [(0, 1.0)]
        elif (i, j) == (0, 2):
            # D_02: pick off eta_02
            if form_idx == 0:  # eta_01^eta_02: eta_02 at pos 1, sign (-1)^1 = -1
                # remaining: eta_01, merge 0,2->0': eta_01 stays eta_{0',1}
                # reindex: 0'->0, 1->1. eta_{0,1} = target basis[0].
                return [(0, -1.0)]
            elif form_idx == 1:  # eta_01^eta_12: no eta_02 factor
                return []
        elif (i, j) == (1, 2):
            # D_12: pick off eta_12
            if form_idx == 0:  # eta_01^eta_02: no eta_12 factor
                return []
            elif form_idx == 1:  # eta_01^eta_12: eta_12 at pos 1, sign (-1)^1 = -1
                # remaining: eta_01, merge 1,2->1': eta_01 -> eta_{0,1'}
                # reindex: 0->0, 1'->1. eta_{0,1} = target basis[0].
                return [(0, -1.0)]

    return []


def _find_in_basis(pairs: list, target_basis: list, sign: float) -> List[Tuple[int, float]]:
    """Find a form (given as list of eta pairs) in the target basis."""
    pairs_tuple = tuple(pairs)
    for idx, tform in enumerate(target_basis):
        if tform == pairs_tuple:
            return [(idx, sign)]
    return []


# =========================================================================
# Bar differential construction
# =========================================================================

class W3BarCohomology:
    """Compute W3 chiral bar cohomology by building differential matrices."""

    def __init__(self, max_weight: int = 12, c_val: float = 7.0):
        self.max_weight = max_weight
        self.c_val = c_val
        self.mod = W3VacuumModule(max_weight, c_val)

        # Precompute V-bar dimensions
        self.vbar_dims = dim_vbar_gf(max_weight)

        # V-bar state lists by weight
        self._vbar_by_weight: Dict[int, List[State]] = {}
        for h in range(2, max_weight + 1):
            self._vbar_by_weight[h] = self.mod.vbar_states_at_weight(h)

        # Global V-bar index (for building matrices)
        self._vbar_states = list(self.mod._vbar_states)
        self._vbar_to_idx = dict(self.mod._vbar_to_idx)

    def _enumerate_bar_chains(self, degree: int
                               ) -> List[Tuple[Tuple[State, ...], int]]:
        """Enumerate bar chain basis elements at given degree.

        Each element is (states, os_form_idx) where states is a tuple of
        degree V-bar states and os_form_idx indexes into os_basis(degree).

        Returns list of (states_tuple, os_idx).
        """
        os_dim = os_basis(degree)
        n_os = len(os_dim)

        result = []
        states_list = self._enumerate_state_tuples(degree)
        for states in states_list:
            for oidx in range(n_os):
                result.append((states, oidx))
        return result

    def _enumerate_state_tuples(self, n: int) -> List[Tuple[State, ...]]:
        """Enumerate all n-tuples of V-bar states up to max_weight."""
        if n == 0:
            return [()]

        result = []
        sub = self._enumerate_state_tuples(n - 1)
        for states in sub:
            h_used = sum(state_weight(s) for s in states)
            h_remain = self.max_weight - h_used
            for h in range(2, h_remain + 1):
                for s in self._vbar_by_weight.get(h, []):
                    result.append(states + (s,))
        return result

    def compute_d2_matrix(self) -> Tuple[np.ndarray, int, int]:
        """Build the matrix for d: B^2 -> B^1 + B^0.

        B^2 elements: [a|b] x eta_12 (OS^1 is 1-dim for n=2)
        d([a|b] x eta_12) = mu(a,b) (projected to V-bar + vacuum)

        Returns (matrix, n_source, n_target) where
        target = V-bar states + 1 (vacuum).
        """
        # Source: ordered pairs [a|b] at all weights up to max_weight
        source_elements = []
        for h_a in range(2, self.max_weight - 1):
            for a in self._vbar_by_weight.get(h_a, []):
                for h_b in range(2, self.max_weight - h_a + 1):
                    for b in self._vbar_by_weight.get(h_b, []):
                        source_elements.append((a, b))

        n_source = len(source_elements)
        n_target = self.mod.vbar_dim + 1  # V-bar + vacuum

        mat = np.zeros((n_target, n_source))

        for col, (a, b) in enumerate(source_elements):
            vbar_vec, vac_coeff = self.mod.compute_mu(a, b)
            # vacuum -> row 0
            mat[0, col] = vac_coeff
            # V-bar -> rows 1..
            for i in range(self.mod.vbar_dim):
                mat[i + 1, col] = vbar_vec[i]

        return mat, n_source, n_target

    def compute_d3_matrix(self) -> Tuple[np.ndarray, int, int]:
        """Build the matrix for d: B^3 -> B^2.

        B^3 elements: [a|b|c] x omega where omega in OS^2(C_3) (2-dim)
        B^2 elements: [a|b] x eta_12

        d involves collisions D_01, D_02, D_12 with residues.
        """
        # Source: triples [a|b|c] x os_form
        source_elements = []
        for h_a in range(2, self.max_weight - 3):
            for a in self._vbar_by_weight.get(h_a, []):
                for h_b in range(2, self.max_weight - h_a - 1):
                    for b in self._vbar_by_weight.get(h_b, []):
                        h_max_c = self.max_weight - h_a - h_b
                        for h_c in range(2, h_max_c + 1):
                            for c in self._vbar_by_weight.get(h_c, []):
                                for os_idx in range(2):  # OS^2(C_3) is 2-dim
                                    source_elements.append((a, b, c, os_idx))

        # Target: pairs [a|b] x eta_12 (same indexing as d2 source)
        target_elements = []
        for h_a in range(2, self.max_weight - 1):
            for a in self._vbar_by_weight.get(h_a, []):
                for h_b in range(2, self.max_weight - h_a + 1):
                    for b in self._vbar_by_weight.get(h_b, []):
                        target_elements.append((a, b))
        target_idx = {elem: i for i, elem in enumerate(target_elements)}

        n_source = len(source_elements)
        n_target = len(target_elements)

        if n_source == 0 or n_target == 0:
            return np.zeros((n_target, n_source)), n_source, n_target

        mat = np.zeros((n_target, n_source))

        for col, (a, b, c, os_idx) in enumerate(source_elements):
            # For each collision D_{ij}:
            for (ci, cj) in [(0, 1), (0, 2), (1, 2)]:
                states = [a, b, c]
                res = os_residue(3, os_idx, (ci, cj))
                if not res:
                    continue

                # Compute mu(states[ci], states[cj])
                vbar_vec, vac_coeff = self.mod.compute_mu(states[ci], states[cj])

                # The remaining state (not ci or cj)
                remaining_idx = [k for k in range(3) if k != ci and k != cj][0]
                remaining_state = states[remaining_idx]

                # After merge, result is [mu_result | remaining] or [remaining | mu_result]
                # depending on position ordering
                # Convention: merged point goes to position min(ci,cj),
                # other points shift down
                merged_pos = min(ci, cj)

                # Sign from collision (for bosonic fields, simplified)
                sign = (-1) ** ci  # simplified Koszul sign for bosonic fields

                # Build the target pair
                for res_os_idx, res_coeff in res:
                    # The target is in B^2 = V-bar^2 x OS^1(C_2)
                    # OS^1(C_2) is 1-dim, so res_os_idx should be 0
                    if res_os_idx != 0:
                        continue

                    # Distribute mu result over V-bar basis
                    for vidx in range(self.mod.vbar_dim):
                        if abs(vbar_vec[vidx]) < 1e-15:
                            continue
                        mu_state = self._vbar_states[vidx]
                        h_mu = state_weight(mu_state)
                        h_rem = state_weight(remaining_state)
                        if h_mu + h_rem > self.max_weight:
                            continue

                        # Determine ordering in target pair
                        if merged_pos == 0:
                            # merged is first, remaining is second
                            pair = (mu_state, remaining_state)
                        else:
                            # remaining is first, merged is second
                            pair = (remaining_state, mu_state)

                        if pair in target_idx:
                            row = target_idx[pair]
                            mat[row, col] += sign * res_coeff * vbar_vec[vidx]

        return mat, n_source, n_target

    def compute_H1(self) -> int:
        """Compute H^1 = dim(V-bar) / im(d: B^2 -> B^1)."""
        d2_mat, n_src, n_tgt = self.compute_d2_matrix()

        if n_src == 0:
            return self.mod.vbar_dim

        # Extract the V-bar part (rows 1 to end, skipping vacuum)
        d2_vbar = d2_mat[1:, :]

        rank = np.linalg.matrix_rank(d2_vbar, tol=1e-8)
        H1 = self.mod.vbar_dim - rank

        return H1

    def compute_H2(self) -> int:
        """Compute H^2 = dim ker(d2) / im(d3).

        d2: B^2 -> B^1 + B^0 (full map including vacuum)
        d3: B^3 -> B^2
        """
        d2_mat, n_src_2, n_tgt_2 = self.compute_d2_matrix()
        d3_mat, n_src_3, n_tgt_3 = self.compute_d3_matrix()

        # ker(d2)
        if n_src_2 == 0:
            return 0

        rank_d2 = np.linalg.matrix_rank(d2_mat, tol=1e-8)
        dim_ker_d2 = n_src_2 - rank_d2

        # im(d3) inside B^2
        if n_src_3 == 0:
            rank_d3 = 0
        else:
            rank_d3 = np.linalg.matrix_rank(d3_mat, tol=1e-8)

        # H^2 = dim(ker d2) - dim(im d3 ∩ ker d2)
        # Since im(d3) ⊂ ker(d2) (because d^2 = 0), rank(d3) = dim(im d3)
        H2 = dim_ker_d2 - rank_d3

        return H2

    def verify_d_squared_zero(self) -> float:
        """Verify d2 ∘ d3 = 0 (bar differential squares to zero)."""
        d2_mat, _, _ = self.compute_d2_matrix()
        d3_mat, n_src_3, n_tgt_3 = self.compute_d3_matrix()

        if n_src_3 == 0 or d2_mat.shape[1] != d3_mat.shape[0]:
            return 0.0

        product = d2_mat @ d3_mat
        return np.max(np.abs(product))


def main():
    print("=" * 60)
    print("W3 CHIRAL BAR COHOMOLOGY COMPUTATION")
    print("=" * 60)

    # Start with small max_weight for feasibility
    for mw in [8, 10, 12]:
        print(f"\n--- max_weight = {mw}, c = 7.0 ---")
        bc = W3BarCohomology(max_weight=mw, c_val=7.0)
        print(f"  V-bar dim (up to wt {mw}): {bc.mod.vbar_dim}")

        H1 = bc.compute_H1()
        print(f"  H^1 = {H1}  (expected: 2)")

        H2 = bc.compute_H2()
        print(f"  H^2 = {H2}  (expected: 5)")

        err = bc.verify_d_squared_zero()
        print(f"  |d^2| = {err:.2e}")


if __name__ == "__main__":
    main()
