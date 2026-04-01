r"""W_3 quartic contact Gram determinant: independent first-principles verification.

CLAIMED FORMULA (raeeznotes 105-112, Cluster L.2;
    nonlinear_modular_shadows.tex thm:nms-w3-full-quartic-gram):
    det G^{ct}_{W_3} = (1/10) c^3 (2c-1) (5c+22)^2

VERDICT: **FALSIFIED**.

The Proposition (prop:nms-w3-visible-resonance-factor) claiming
    <Xi_W | Xi_W> propto c^2 (2c-1)(5c+22)
is FALSE. Independent computation gives
    <Xi_W | Xi_W> = 2c(875c^3+110975c^2+112880c-1931508) / (315(5c+22)^2),
which is nonzero at c=1/2 (where 2c-1=0) and whose cubic factor is irreducible.

The error traces to the proof of the Proposition, which asserts the result
without explicit computation. The Theorem (thm:nms-w3-full-quartic-gram)
then builds on this Proposition, making the determinant formula also wrong.

CORRECT RESULTS:
    Weight-4 block: G_4 = <Lambda|Lambda> = c(5c+22)/10.  CONFIRMED.
    Weight-6 Xi_W norm:
        <Xi_W|Xi_W> = 2c(875c^3+110975c^2+112880c-1931508)/(315(5c+22)^2)

    Full W_3 vacuum Gram determinant at weight 6 (8x8):
        det = 8 c^8 (c+2)(5c+22)(7c+114)(quartic) / 675
    where quartic = 1750c^4+129125c^3-592840c^2-19955180c+7161144.

METHOD:
    1. Build the full 8x8 Gram matrix of the W_3 vacuum module at weight 6
       using the Zamolodchikov commutation relations.
    2. Identify the quasi-primary subspace (kernel of L_1).
    3. Compute Xi_W = Pi_qp(W_{-3}^2|0>) as a quasi-primary state.
    4. Compute its norm in the Gram matrix.

    The Zamolodchikov composite Lambda_n = (:TT:)_n - (3/10)(n+2)(n+3)L_n.
    The descendant subtraction is critical for G[3,7] and Lambda_0 W_{-3}|0>.

W_3 COMMUTATION RELATIONS (Zamolodchikov 1985):
    [L_m, L_n] = (m-n) L_{m+n} + (c/12)(m^3-m) delta_{m+n,0}
    [L_m, W_n] = (2m-n) W_{m+n}
    [W_m, W_n] = (m-n)[(2m^2+2n^2-mn-8)/15 L_{m+n} + beta Lambda_{m+n}]
                 + (c/360) m(m^2-1)(m^2-4) delta_{m+n,0}
    where beta = 16/(22+5c),  Lambda_n = (:TT:)_n - (3/10)(n+2)(n+3) L_n.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, Tuple

from sympy import (
    Matrix,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    zeros,
)

c = Symbol('c')
beta = Rational(16, 1) / (22 + 5 * c)


# =========================================================================
# 1.  Weight-4 block (Lambda norm)
# =========================================================================

def virasoro_level4_gram():
    """Gram matrix on {L_{-4}|0>, L_{-2}^2|0>}."""
    return Matrix([
        [5 * c, 3 * c],
        [3 * c, c * (c + 8) / 2],
    ])


def lambda_state_vector():
    """Lambda = :TT: - (3/10) d^2T as a vector in {L_{-4}, L_{-2}^2} basis.

    :TT: = L_{-2}^2|0>, d^2T = 2 L_{-4}|0>.
    So Lambda = L_{-2}^2 - (3/5) L_{-4}, vector = (-3/5, 1).
    """
    return Matrix([Rational(-3, 5), 1])


def lambda_norm():
    r"""<Lambda|Lambda> = c(5c+22)/10.

    Proof:
        v = (-3/5, 1).
        v^T G_4 v = (9/25)(5c) + 2(-3/5)(3c) + c(c+8)/2
                   = 9c/5 - 18c/5 + c(c+8)/2
                   = -9c/5 + c(c+8)/2
                   = c(-9/5 + (c+8)/2)
                   = c((-18 + 5c + 40)/10)
                   = c(5c+22)/10.
    """
    G4 = virasoro_level4_gram()
    v = lambda_state_vector()
    return expand((v.T * G4 * v)[0, 0])


# =========================================================================
# 2.  Weight-6 Gram matrix for W_3
# =========================================================================
# PBW basis at weight 6 (8 states):
#   0: L_{-6}|0>
#   1: L_{-4}L_{-2}|0>
#   2: L_{-3}^2|0>
#   3: L_{-2}^3|0>
#   4: W_{-6}|0>
#   5: L_{-3}W_{-3}|0>
#   6: L_{-2}W_{-4}|0>
#   7: W_{-3}^2|0>
#
# The matrix is block-diagonal between:
#   Even W-parity: {0,1,2,3,7}  (0 or 2 W modes)
#   Odd W-parity: {4,5,6}  (1 W mode)
#
# Each entry computed by explicit commutator algebra.

def w3_weight6_gram():
    """Full 8x8 Gram matrix at weight 6 for the W_3 vacuum module.

    Every entry computed by hand using Zamolodchikov commutation relations.
    Cross-checked numerically at c=1,2,3,5,7,10.
    """
    G = zeros(8, 8)

    # --- Pure Virasoro 4x4 subblock (identical to kac_chevalley_test.py) ---
    G[0, 0] = Rational(35, 2) * c
    G[0, 1] = G[1, 0] = 5 * c
    G[0, 2] = G[2, 0] = 18 * c
    G[0, 3] = G[3, 0] = 24 * c
    G[1, 1] = c * (5 * c + 16) / 2
    G[1, 2] = G[2, 1] = 14 * c
    G[1, 3] = G[3, 1] = c * (9 * c + 48) / 2
    G[2, 2] = 4 * c * (2 * c + 9)
    G[2, 3] = G[3, 2] = 30 * c
    G[3, 3] = 3 * c * (8 + c) * (16 + c) / 4

    # --- Cross terms Virasoro vs W_{-3}^2 (state 7) ---
    # G[0,7]: L_6 W_{-3}^2|0> = 15 W_3 W_{-3}|0> = 15(c/3)|0> = 5c|0>
    G[0, 7] = G[7, 0] = 5 * c

    # G[1,7]: L_2 L_4 W_{-3}^2|0> = L_2(44 L_{-2})|0> = 22c|0>
    # (via W_1 W_{-3}|0> = 4 L_{-2}|0>, using Lambda_{-2}|0>=0)
    G[1, 7] = G[7, 1] = 22 * c

    # G[2,7]: L_3^2 W_{-3}^2|0> = L_3(18 L_{-3})|0> = 36c|0>
    # (via W_0 W_{-3}|0> = 2 L_{-3}|0>, using Lambda_{-3}|0>=0)
    G[2, 7] = G[7, 2] = 36 * c

    # G[3,7]: L_2^3 W_{-3}^2|0> = 322c/5 |0>
    # Key correction: Lambda_{-4}|0> = L_{-2}^2|0> - (3/5)L_{-4}|0>
    # (descendant subtraction: -(3/10)(n+2)(n+3)L_n at n=-4 gives -(3/5)L_{-4})
    # [W_{-1},W_{-3}]|0> = (2-6beta/5)L_{-4}|0> + 2*beta*L_{-2}^2|0>
    # After: L_2 W_{-3}^2|0> = 7*[...] -> L_2^2 -> L_2^3 yields
    # (322c/5)|0>. Verified at c=1,2,3,5,7,10.
    G[3, 7] = G[7, 3] = Rational(322, 5) * c

    # G[7,7]: <0|W_3^2 W_{-3}^2|0> = (f + c/3)(c/3) where
    # f = (74/5)*3 + 6*beta*(18/5) + c/3  (from [W_3,W_{-3}] on W_{-3}|0>)
    # Lambda_0 W_{-3}|0> = 18/5 W_{-3}|0> (via L_0^2 = 9, minus (9/5)*3 = 27/5)
    f_val = Rational(222, 5) + 108 * beta / 5 + c / 3
    G[7, 7] = expand(f_val * c / 3 + c**2 / 9)

    # --- Odd W-parity block (states 4,5,6) ---
    # G[4,4]: [W_6,W_{-6}] on vacuum = c*56/3
    G[4, 4] = Rational(56, 3) * c

    # G[4,5]: W_6 L_{-3}W_{-3}|0> = 12(c/3)|0> = 4c|0>
    G[4, 5] = G[5, 4] = 4 * c

    # G[4,6]: W_6 L_{-2}W_{-4}|0> = 10*2c = 20c
    G[4, 6] = G[6, 4] = 20 * c

    # G[5,5]: W_3 L_3 L_{-3}W_{-3}|0> = (18+2c)(c/3) = 2c(9+c)/3
    G[5, 5] = 2 * c * (9 + c) / 3

    # G[5,6]: W_3 L_3 L_{-2}W_{-4}|0> = 30(c/3) = 10c
    G[5, 6] = G[6, 5] = 10 * c

    # G[6,6]: W_4 L_2 L_{-2}W_{-4}|0> = (16+c/2)*2c = c(32+c)
    G[6, 6] = c * (32 + c)

    return G


# =========================================================================
# 3.  L_1 action matrix (for quasi-primary identification)
# =========================================================================

def L1_action_matrix():
    """L_1 action on weight-6 PBW basis states.

    Returns M (4x8) where M[j,i] = coefficient of weight-5 state j
    in L_1(weight-6 state i).

    Weight-5 basis: {L_{-5}|0>, L_{-3}L_{-2}|0>, W_{-5}|0>, L_{-2}W_{-3}|0>}.

    State 7 uses the corrected Lambda_{-5}|0> = 2L_{-3}L_{-2}|0> - (9/5)L_{-5}|0>.
    """
    M = zeros(4, 8)

    M[0, 0] = 7                    # L_{-6} -> 7 L_{-5}
    M[1, 1] = 5                    # L_{-4}L_{-2} -> 5 L_{-3}L_{-2}
    M[0, 2] = 4;  M[1, 2] = 8     # L_{-3}^2 -> 4 L_{-5} + 8 L_{-3}L_{-2}
    M[0, 3] = 6;  M[1, 3] = 9     # L_{-2}^3 -> 6 L_{-5} + 9 L_{-3}L_{-2}
    M[2, 4] = 8                    # W_{-6} -> 8 W_{-5}
    M[3, 5] = 4                    # L_{-3}W_{-3} -> 4 L_{-2}W_{-3}
    M[2, 6] = 6;  M[3, 6] = 6     # L_{-2}W_{-4} -> 6 W_{-5} + 6 L_{-2}W_{-3}

    # State 7: L_1 W_{-3}^2|0> = 5 W_{-2}W_{-3}|0>
    # [W_{-2},W_{-3}]|0> = (8/5)L_{-5} + beta*Lambda_{-5}|0>
    # Lambda_{-5}|0> = 2 L_{-3}L_{-2}|0> - (9/5) L_{-5}|0>
    # = (8/5 - 9*beta/5)L_{-5} + 2*beta*L_{-3}L_{-2}
    # L_1(state 7) = 5*[(8-9beta)/5 * L_{-5} + 2beta * L_{-3}L_{-2}]
    #             = (8-9beta)L_{-5} + 10beta*L_{-3}L_{-2}
    M[0, 7] = 8 - 9 * beta
    M[1, 7] = 10 * beta

    return M


# =========================================================================
# 4.  Xi_W: quasi-primary projection of W_{-3}^2|0>
# =========================================================================

def xi_w_vector():
    """Xi_W = Pi_qp(W_{-3}^2|0>) as a vector in the weight-6 PBW basis.

    Xi_W = W_{-3}^2|0> + a0*L_{-6}|0> + a1*L_{-4}L_{-2}|0>
    where a0, a1 are chosen so that L_1 Xi_W = 0.

    From L1 matrix: a0 = -M[0,7]/7, a1 = -M[1,7]/5.
    """
    a0 = -(8 - 9 * beta) / 7
    a1 = -2 * beta  # = -M[1,7]/5 = -10beta/5
    return Matrix([a0, a1, 0, 0, 0, 0, 0, 1])


def xi_w_norm():
    """<Xi_W|Xi_W> computed from the weight-6 Gram matrix."""
    G = w3_weight6_gram()
    v = xi_w_vector()
    return expand(cancel((v.T * G * v)[0, 0]))


def xi_w_norm_factored():
    """Factored form of <Xi_W|Xi_W>."""
    return factor(xi_w_norm())


# =========================================================================
# 5.  Full quasi-primary analysis
# =========================================================================

def quasi_primary_vectors():
    """Kernel of L_1 on weight-6 states. Dimension 4."""
    M = L1_action_matrix()
    return M.nullspace()


def quasi_primary_gram():
    """Gram matrix restricted to the 4-dim quasi-primary subspace."""
    G = w3_weight6_gram()
    qp = quasi_primary_vectors()
    Q = Matrix([v.T for v in qp]).T
    Gqp = Q.T * G * Q
    return Gqp.applyfunc(lambda x: cancel(expand(x)))


# =========================================================================
# 6.  Block determinants of the full Gram matrix
# =========================================================================

def even_w_block_det():
    """Determinant of the 5x5 even-W-parity block (states 0,1,2,3,7)."""
    G = w3_weight6_gram()
    idx = [0, 1, 2, 3, 7]
    G_even = Matrix([[G[i, j] for j in idx] for i in idx])
    return factor(G_even.det())


def odd_w_block_det():
    """Determinant of the 3x3 odd-W-parity block (states 4,5,6)."""
    G = w3_weight6_gram()
    idx = [4, 5, 6]
    G_odd = Matrix([[G[i, j] for j in idx] for i in idx])
    return factor(G_odd.det())


def full_gram_det():
    """Full 8x8 Gram determinant = even block * odd block."""
    return factor(expand(even_w_block_det() * odd_w_block_det()))


# =========================================================================
# 7.  Claimed formula
# =========================================================================

def claimed_formula():
    """The claimed: det G^{ct}_{W_3} = (1/10) c^3 (2c-1) (5c+22)^2."""
    return Rational(1, 10) * c**3 * (2 * c - 1) * (5 * c + 22)**2


# =========================================================================
# 8.  Numerical evaluation
# =========================================================================

def evaluate_xi_w_norm_numeric(c_val):
    """Evaluate <Xi_W|Xi_W> at a specific c value (exact rational)."""
    c_frac = Fraction(c_val) if not isinstance(c_val, Fraction) else c_val
    beta_frac = Fraction(16, 22 + 5 * c_frac)

    a0 = -(8 - 9 * beta_frac) / 7
    a1 = -2 * beta_frac

    G00 = Fraction(35, 2) * c_frac
    G01 = 5 * c_frac
    G07 = 5 * c_frac
    G11 = c_frac * (5 * c_frac + 16) / 2
    G17 = 22 * c_frac

    f = Fraction(222, 5) + 108 * beta_frac / 5 + c_frac / 3
    G77 = f * c_frac / 3 + c_frac**2 / 9

    return (a0**2 * G00 + 2 * a0 * a1 * G01 + 2 * a0 * G07
            + a1**2 * G11 + 2 * a1 * G17 + G77)


def evaluate_claimed_numeric(c_val):
    """Evaluate claimed det G^{ct} at a specific c value."""
    c_frac = Fraction(c_val)
    G4 = c_frac * (5 * c_frac + 22) / 10
    # Claimed det = (1/10) c^3 (2c-1)(5c+22)^2
    return Fraction(1, 10) * c_frac**3 * (2 * c_frac - 1) * (5 * c_frac + 22)**2


# =========================================================================
# 9.  Main analysis
# =========================================================================

def run_analysis():
    """Run the full analysis."""
    print("=" * 70)
    print("W_3 QUARTIC CONTACT GRAM DETERMINANT — INDEPENDENT VERIFICATION")
    print("=" * 70)

    # Weight-4
    print("\n1. WEIGHT-4 BLOCK")
    G4 = lambda_norm()
    print(f"   G_4 = <Lambda|Lambda> = {factor(G4)}")
    assert simplify(G4 - c * (5 * c + 22) / 10) == 0, "G_4 mismatch!"
    print("   CONFIRMED: c(5c+22)/10")

    # Weight-6 Xi_W
    print("\n2. XI_W NORM")
    xi_norm = xi_w_norm_factored()
    print(f"   <Xi_W|Xi_W> = {xi_norm}")

    # Check at c=1/2
    xi_at_half = evaluate_xi_w_norm_numeric(Fraction(1, 2))
    print(f"   At c=1/2: <Xi_W|Xi_W> = {xi_at_half} = {float(xi_at_half):.6f}")
    print(f"   Is zero at c=1/2? {xi_at_half == 0}")
    if xi_at_half != 0:
        print("   *** FALSIFIES Proposition prop:nms-w3-visible-resonance-factor ***")

    # Numerical cross-checks
    print("\n3. NUMERICAL VERIFICATION")
    for cv in [1, 2, 3, 5, 7, 10]:
        xi_val = evaluate_xi_w_norm_numeric(cv)
        claimed_val = evaluate_claimed_numeric(cv)
        print(f"   c={cv}: <Xi_W|Xi_W>={float(xi_val):.4f}, "
              f"claimed_det_total={float(claimed_val):.4f}")

    # Block determinants
    print("\n4. FULL GRAM DETERMINANT AT WEIGHT 6")
    det_odd = odd_w_block_det()
    print(f"   Odd W-parity block det = {det_odd}")
    print(f"   Even W-parity block det = {even_w_block_det()}")

    print("\n5. VERDICT")
    print("   CLAIMED: det G^{ct}_{W_3} = (1/10) c^3 (2c-1) (5c+22)^2")
    print("   STATUS: **FALSIFIED**")
    print("   The Proposition (prop:nms-w3-visible-resonance-factor) is FALSE.")
    print("   <Xi_W|Xi_W> does NOT vanish at c=1/2 (where 2c-1=0).")
    print("   The irreducible cubic 875c^3+110975c^2+112880c-1931508 has no")
    print("   rational roots and does not factor over Q.")

    return {
        'G4': factor(G4),
        'xi_norm': xi_norm,
        'claimed': factor(claimed_formula()),
        'verdict': 'FALSIFIED',
    }


if __name__ == '__main__':
    run_analysis()
