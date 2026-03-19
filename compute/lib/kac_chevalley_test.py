"""Kac-Chevalley test: does the Kac determinant factor through the
Chevalley discriminant of the mode space?

For a Gram matrix G of dimension d with eigenvalues λ_1,...,λ_d:
  - Kac determinant = det(G) = ∏ λ_i  (A_0 invariant: product)
  - Chevalley discriminant = ∏_{i<j} (λ_i - λ_j)^2  (A_{d-1} invariant)
  - Characteristic polynomial discriminant = same as Chevalley discriminant

These are DIFFERENT invariants. The question is whether there is a
nontrivial algebraic relation between them as functions of c.

We test this at Virasoro levels 4 and 6, and W_3 level 4.
"""

from __future__ import annotations

from sympy import (
    Matrix, Rational, Symbol, expand, factor, simplify,
    poly, discriminant as sym_discriminant, resultant,
    sqrt, prod as symprod, Poly
)

c = Symbol('c')
lam = Symbol('lambda')


# ═══════════════════════════════════════════════════════════════════════
# 1. VIRASORO LEVEL 4 (2-dimensional)
# ═══════════════════════════════════════════════════════════════════════

def virasoro_level4_gram():
    """Gram matrix on {L_{-4}|0>, L_{-2}^2|0>}."""
    G = Matrix([
        [5*c,       3*c],
        [3*c,       c*(c + 8)/2],
    ])
    return G


def virasoro_level4_analysis():
    """Full eigenvalue analysis of the level-4 Gram matrix."""
    G = virasoro_level4_gram()

    det_G = factor(G.det())
    tr_G = expand(G.trace())

    # Characteristic polynomial: λ^2 - tr(G)λ + det(G)
    char_poly = lam**2 - tr_G * lam + det_G

    # Discriminant of char poly = tr^2 - 4 det
    disc = expand(tr_G**2 - 4 * det_G)
    disc_factored = factor(disc)

    # For 2x2, Chevalley discriminant of A_1 = (λ_1 - λ_2)^2 = disc of char poly
    # So Chevalley disc = disc_factored

    return {
        "G": G,
        "det_G": det_G,
        "tr_G": tr_G,
        "char_poly": char_poly,
        "disc_char_poly": disc_factored,
        "det_G_expected": c**2 * (5*c + 22) / 2,
    }


# ═══════════════════════════════════════════════════════════════════════
# 2. VIRASORO LEVEL 6 (4-dimensional)
# ═══════════════════════════════════════════════════════════════════════

def virasoro_level6_gram():
    """Gram matrix on {L_{-6}|0>, L_{-4}L_{-2}|0>, L_{-3}^2|0>, L_{-2}^3|0>}.

    Computed using Virasoro commutation relations:
    [L_m, L_n] = (m-n)L_{m+n} + c/12 (m^3 - m) delta_{m+n,0}

    We compute G_{ij} = <0| (state_i)^dagger (state_j) |0> by moving
    all positive modes to the right using commutation relations.
    """
    # Use symbolic computation to build the Gram matrix.
    # States: |1> = L_{-6}|0>, |2> = L_{-4}L_{-2}|0>,
    #         |3> = L_{-3}^2|0>, |4> = L_{-2}^3|0>

    # G[0,0] = <0|L_6 L_{-6}|0> = [L_6, L_{-6}] applied to |0>
    # [L_6, L_{-6}] = 12 L_0 + c/12(216-6) = 0 + c*210/12 = 35c/2
    G00 = 35*c/2

    # G[0,1] = <0|L_6 L_{-4} L_{-2}|0>
    # L_6 L_{-4} = [L_6,L_{-4}] + L_{-4}L_6 = 10 L_2 + L_{-4}L_6
    # <0| (10 L_2 + L_{-4}L_6) L_{-2}|0>
    # = 10 <0|L_2 L_{-2}|0> + <0|L_{-4} L_6 L_{-2}|0>
    # L_2 L_{-2}|0> = [L_2,L_{-2}]|0> = (4L_0 + c/2)|0> = c/2 |0>
    # L_6 L_{-2}|0> = [L_6,L_{-2}]|0> = 8 L_4|0> = 0
    # So G[0,1] = 10 * c/2 = 5c
    G01 = 5*c

    # G[0,2] = <0|L_6 L_{-3}^2|0>
    # L_6 L_{-3} = [L_6,L_{-3}] + L_{-3}L_6 = 9 L_3 + L_{-3}L_6
    # <0|(9 L_3 + L_{-3}L_6) L_{-3}|0>
    # = 9<0|L_3 L_{-3}|0> + <0|L_{-3} L_6 L_{-3}|0>
    # L_3 L_{-3}|0> = [L_3,L_{-3}]|0> = (6L_0 + c/12(27-3))|0> = 2c|0>
    # L_6 L_{-3}|0> = [L_6,L_{-3}]|0> = 9 L_3|0> = 0
    # So G[0,2] = 9 * 2c = 18c
    G02 = 18*c

    # G[0,3] = <0|L_6 L_{-2}^3|0>
    # L_6 L_{-2} = 8 L_4 + L_{-2}L_6
    # <0|(8 L_4 + L_{-2}L_6) L_{-2}^2|0>
    # = 8<0|L_4 L_{-2}^2|0> + <0|L_{-2} L_6 L_{-2}^2|0>
    # <0|L_4 L_{-2}^2|0> = G_{01} from level-4 = 3c (from virasoro_level4)
    # Wait, that's <0|L_4 L_{-2}^2|0> which we computed earlier as 3c.
    # L_6 L_{-2}^2|0>: L_6 L_{-2} = 8L_4 + L_{-2}L_6
    # L_6 L_{-2}^2|0> = (8L_4 + L_{-2}L_6) L_{-2}|0>
    #   = 8 L_4 L_{-2}|0> + L_{-2} L_6 L_{-2}|0>
    #   = 8[L_4,L_{-2}]|0> + L_{-2}[L_6,L_{-2}]|0>
    #   = 8*6*L_2|0> + L_{-2}*8*L_4|0> = 0 + 0 = 0
    # So G[0,3] = 8 * 3c + 0 = 24c
    # Wait let me redo. <0|L_4 L_{-2}^2|0> was computed in level-4 analysis.
    # From virasoro_level4_gram: G[0,1] = <0|L_4 L_{-2}^2|0> = 3c. Yes.
    # And <0|L_{-2} L_6 L_{-2}^2|0> = <0|L_{-2}|0> * (something) ... no.
    # <0|L_{-2} ... but L_{-2}^† = L_2, so <0|L_{-2} = 0.
    # Wait: <0|L_{-2} is NOT <0|L_2. We have <0|L_{-2} = 0 since
    # (L_{-2}|0>)^† = <0|L_2, and <0|L_{-2} = (L_2|0>)^† = 0 since L_2|0>=0.
    # Hmm, no. <0|L_{-2} means the bra obtained by having L_{-2} act on <0| from the right.
    # In the standard inner product, <0|L_{-2} corresponds to <0| applied to L_{-2}(...).
    # Actually <0|L_{-2} = <L_2 0| = 0 since L_2|0>=0. Wait no.
    # (L_n)^† = L_{-n}. So <0|L_{-2} = (L_2|0>)^† bra = 0.
    # So <0|L_{-2}(anything)|0> = 0.
    # Therefore G[0,3] = 8 * 3c = 24c.
    G03 = 24*c

    # G[1,1] = <0|L_2 L_4 L_{-4} L_{-2}|0>
    # L_4 L_{-4} = [L_4,L_{-4}] + L_{-4}L_4 = 8L_0 + 5c + L_{-4}L_4
    # <0|L_2(8L_0 + 5c + L_{-4}L_4)L_{-2}|0>
    # = <0|L_2(5c)L_{-2}|0> + <0|L_2 * 8L_0 L_{-2}|0> + <0|L_2 L_{-4} L_4 L_{-2}|0>
    # L_0 L_{-2}|0> = [L_0,L_{-2}]|0> = 2L_{-2}|0>
    # L_4 L_{-2}|0> = [L_4,L_{-2}]|0> = 6L_2|0> = 0
    # <0|L_2 L_{-2}|0> = c/2
    # So G[1,1] = 5c * c/2 + 8 * <0|L_2 * 2L_{-2}|0> + 0
    #           = 5c^2/2 + 16 * c/2 = 5c^2/2 + 8c = c(5c+16)/2
    G11 = c*(5*c + 16)/2

    # G[1,2] = <0|L_2 L_4 L_{-3}^2|0>
    # L_4 L_{-3} = [L_4,L_{-3}] + L_{-3}L_4 = 7L_1 + L_{-3}L_4
    # <0|L_2(7L_1 + L_{-3}L_4)L_{-3}|0>
    # L_1 L_{-3}|0> = [L_1,L_{-3}]|0> = 4L_{-2}|0>
    # L_4 L_{-3}|0> = [L_4,L_{-3}]|0> = 7L_1|0> = 0
    # <0|L_2 * 7 * 4 L_{-2}|0> = 28 * c/2 = 14c
    # <0|L_2 L_{-3} * 0|0> = 0
    # G[1,2] = 14c
    G12 = 14*c

    # G[1,3] = <0|L_2 L_4 L_{-2}^3|0>
    # L_4 L_{-2} = 6L_2 + L_{-2}L_4
    # <0|L_2(6L_2 + L_{-2}L_4) L_{-2}^2|0>
    # = 6<0|L_2^2 L_{-2}^2|0> + <0|L_2 L_{-2} L_4 L_{-2}^2|0>
    # <0|L_2^2 L_{-2}^2|0> = c(c+8)/2 (from level-4)
    # L_4 L_{-2}^2|0>: L_4 L_{-2} = 6L_2 + L_{-2}L_4
    # L_4 L_{-2}^2|0> = (6L_2 + L_{-2}L_4)L_{-2}|0>
    #   = 6L_2 L_{-2}|0> + L_{-2}L_4 L_{-2}|0>
    #   = 6*(c/2)|0> + L_{-2}*0 = 3c|0>
    # <0|L_2 L_{-2} * 3c|0> = 3c * <0|L_2 L_{-2}|0> ... wait.
    # <0|L_2 L_{-2} (3c|0>) = 3c * <0|L_2 L_{-2}|0> = 3c * c/2
    # G[1,3] = 6*c*(c+8)/2 + 3c*c/2 = 3c(c+8) + 3c^2/2 = (6c^2+48c+3c^2)/2 = c(9c+48)/2
    # Hmm let me redo more carefully.
    # G[1,3] = 6 * c(c+8)/2 + 3c * c/2 = 3c(c+8) + 3c^2/2 = 3c^2 + 24c + 3c^2/2
    #        = (6c^2 + 48c + 3c^2)/2 = (9c^2 + 48c)/2 = c(9c+48)/2
    G13 = c*(9*c + 48)/2

    # G[2,2] = <0|L_3^2 L_{-3}^2|0>
    # L_3 L_{-3} = [L_3,L_{-3}] + L_{-3}L_3 = 6L_0 + 2c + L_{-3}L_3
    # <0|L_3(6L_0 + 2c + L_{-3}L_3)L_{-3}|0>
    # L_0 L_{-3}|0> = 3L_{-3}|0>
    # L_3 L_{-3}|0> = (6*0 + 2c)|0> = 2c|0>  (L_0|0>=0)
    # <0|L_3 * (6*3L_{-3} + 2cL_{-3} + L_{-3}*2c)|0>
    # Wait, let me be more careful.
    # <0|L_3(6L_0 + 2c)L_{-3}|0> + <0|L_3 L_{-3} L_3 L_{-3}|0>
    # = <0|L_3(18+2c)L_{-3}|0> + <0|L_3 L_{-3} * 2c|0>
    # Wait: L_0 L_{-3}|0> = [L_0,L_{-3}]|0> + L_{-3}L_0|0> = 3L_{-3}|0> + 0
    # So (6L_0 + 2c)L_{-3}|0> = (18+2c)L_{-3}|0>
    # <0|L_3 * (18+2c)L_{-3}|0> = (18+2c) * <0|L_3 L_{-3}|0> = (18+2c)*2c
    # And L_3 L_{-3}|0> = 2c|0>, so <0|L_3 L_{-3} L_3 L_{-3}|0> = 2c * <0|L_3 L_{-3}|0> = 2c*2c = 4c^2
    # G[2,2] = 2c(18+2c) + 4c^2 = 36c + 4c^2 + 4c^2 = 8c^2 + 36c = 4c(2c+9)
    G22 = 4*c*(2*c + 9)

    # G[2,3] = <0|L_3^2 L_{-2}^3|0>
    # L_3 L_{-2} = [L_3,L_{-2}] + L_{-2}L_3 = 5L_1 + L_{-2}L_3
    # L_3 L_{-2}^3|0>:
    # = (5L_1 + L_{-2}L_3) L_{-2}^2|0>
    # L_1 L_{-2}^2|0> = 3L_{-3}|0> ... wait, we need L_1 L_{-2}^2|0>.
    # L_1 L_{-2} = [L_1,L_{-2}] + L_{-2}L_1 = 3L_{-1} + L_{-2}L_1
    # L_1 L_{-2}^2|0> = (3L_{-1} + L_{-2}L_1)L_{-2}|0>
    #   = 3L_{-1}L_{-2}|0> + L_{-2}(3L_{-1} + L_{-2}L_1)|0>
    #   = 3L_{-1}L_{-2}|0> + 3L_{-2}L_{-1}|0> + L_{-2}^2 L_1|0>
    #   = 3L_{-1}L_{-2}|0> + 0 + 0  (L_{-1}|0>=0, L_1|0>=0)
    # L_{-1}L_{-2}|0> = [L_{-1},L_{-2}]|0> + L_{-2}L_{-1}|0> = L_{-3}|0>
    # So L_1 L_{-2}^2|0> = 3L_{-3}|0>
    # L_3 L_{-2}^2|0>: need this first.
    # L_3 L_{-2} = 5L_1 + L_{-2}L_3
    # L_3 L_{-2}^2|0> = (5L_1 + L_{-2}L_3)L_{-2}|0>
    #   = 5 L_1 L_{-2}|0> + L_{-2} L_3 L_{-2}|0>
    # L_1 L_{-2}|0> = [L_1,L_{-2}]|0> = 3L_{-1}|0> = 0
    # L_3 L_{-2}|0> = [L_3,L_{-2}]|0> = 5L_1|0> = 0
    # So L_3 L_{-2}^2|0> = 0
    #
    # Then L_3 L_{-2}^3|0> = (5L_1 + L_{-2}L_3)L_{-2}^2|0>
    #   = 5 * 3L_{-3}|0> + L_{-2} * 0 = 15L_{-3}|0>
    #
    # Now L_3^2 L_{-2}^3|0> = L_3 * 15L_{-3}|0> = 15 * 2c|0> = 30c|0>
    # Hmm wait, that gives a scalar. <0|30c|0> = 30c.
    G23 = 30*c

    # G[3,3] = <0|L_2^3 L_{-2}^3|0>
    # Need to compute this step by step.
    # L_2 L_{-2}^3|0>:
    # L_2 L_{-2} = 4L_0 + c/2 + L_{-2}L_2
    # L_2 L_{-2}^3|0> = (4L_0 + c/2 + L_{-2}L_2) L_{-2}^2|0>
    # L_0 L_{-2}^2|0> = [L_0,L_{-2}]L_{-2}|0> + L_{-2}L_0 L_{-2}|0>
    #   = 2L_{-2}^2|0> + L_{-2}*2L_{-2}|0> = 2L_{-2}^2|0> + 2L_{-2}^2|0> = 4L_{-2}^2|0>
    # L_2 L_{-2}^2|0> = (8+c) L_{-2}|0> (from level-4 analysis)
    # So L_2 L_{-2}^3|0> = 4*4L_{-2}^2|0> + (c/2)L_{-2}^2|0> + L_{-2}*(8+c)L_{-2}|0>
    #   = (16 + c/2)L_{-2}^2|0> + (8+c)L_{-2}^2|0>
    #   = (16 + c/2 + 8 + c)L_{-2}^2|0> = (24 + 3c/2)L_{-2}^2|0>
    #
    # L_2^2 L_{-2}^3|0> = L_2 * (24+3c/2)L_{-2}^2|0> = (24+3c/2) * (8+c)L_{-2}|0>
    #   ... wait, L_2 L_{-2}^2|0> = (8+c)L_{-2}|0>
    # So L_2^2 L_{-2}^3|0> = (24+3c/2)(8+c)L_{-2}|0>
    #
    # L_2^3 L_{-2}^3|0> = L_2 * (24+3c/2)(8+c) L_{-2}|0>
    #   = (24+3c/2)(8+c) * L_2 L_{-2}|0>
    #   = (24+3c/2)(8+c) * (c/2)|0>
    #
    # G[3,3] = (24+3c/2)(8+c)(c/2)
    #        = (c/2)(8+c)(24+3c/2)
    #        = (c/2)(8+c)(48+3c)/2
    #        = c(8+c)(48+3c)/4
    #        = c(8+c)*3*(16+c)/4
    #        = 3c(8+c)(16+c)/4
    G33 = 3*c*(8 + c)*(16 + c)/4

    G = Matrix([
        [G00, G01, G02, G03],
        [G01, G11, G12, G13],
        [G02, G12, G22, G23],
        [G03, G13, G23, G33],
    ])
    return G


def virasoro_level6_analysis():
    """Full eigenvalue analysis of the level-6 Gram matrix."""
    G = virasoro_level6_gram()

    det_G = factor(G.det())
    tr_G = expand(G.trace())

    # Characteristic polynomial
    char_poly_matrix = G - lam * Matrix.eye(4)
    char_poly = factor(char_poly_matrix.det())

    return {
        "G": G,
        "det_G": det_G,
        "tr_G": tr_G,
        "char_poly": char_poly,
    }


# ═══════════════════════════════════════════════════════════════════════
# 3. W_3 LEVEL 4 (3-dimensional)
# ═══════════════════════════════════════════════════════════════════════

def w3_level4_gram():
    """Gram matrix on {L_{-4}|0>, L_{-2}^2|0>, W_{-4}|0>} for the W_3 vacuum module.

    W_{-4}|0> is linearly independent from L_{-4}|0> and L_{-2}^2|0> because
    W has conformal weight 3, so W_{-4}|0> = W_{-3-1}|0> which is NOT L_{-1}W_{-3}|0>
    (since L_{-1}|0> = 0). W_{-4}|0> is a genuine new state at level 4.

    Actually: W_{-n}|0> for n >= 3 are states in the W_3 vacuum module.
    W_{-4}|0> is a level-4 state distinct from L_{-4}|0> and L_{-2}^2|0>.

    The inner products involving W modes use:
    [W_m, W_n] involves the W_3 algebra commutation relations.
    From the W×W OPE (w3_bar.py):
      W_{(5)}W = c/3, W_{(3)}W = 2T, W_{(2)}W = dT,
      W_{(1)}W = (3/10)d^2T + (16/(22+5c))Λ

    In mode language, the key commutator is:
    [W_m, W_{-n}]|0> extracted from the OPE.
    For [W_4, W_{-4}]: this comes from W_{(n)}W with the appropriate mode extraction.

    The W-algebra commutation relation (Zamolodchikov):
    [W_m, W_n] = c/3 * binom(m,5) delta_{m+n,0}
                 + 2(m-n) L_{m+n}
                 + (m-n) * [(m+n+3)(m+n+2)/20 - (m+2)(n+2)/6] * (c/2) ... no.

    Let me use the standard formula. For W_3 (Zamolodchikov 1985):
    [W_m, W_n] = (m-n) [ (2m^2+2n^2-mn-8)/15 * L_{m+n}
                         + beta * Λ_{m+n} ]
                + c/360 * m(m^2-1)(m^2-4) delta_{m+n,0}

    where Λ_n = sum_k :L_k L_{n-k}: (normal-ordered modes) and
    beta = 16/(22+5c).

    For [W_4, W_{-4}]:
    m=4, n=-4, m-n=8, m+n=0
    c/360 * 4*(16-1)*(16-4) = c/360 * 4*15*12 = c/360 * 720 = 2c
    + 8 * [(32+32+16-8)/15 * L_0 + beta * Λ_0]
    = 8 * [72/15 * 0 + beta * Λ_0]  (L_0|0> = 0)
    = 8 beta Λ_0 |0>

    Λ_0|0> = sum_k :L_k L_{-k}: |0>. Normal ordering puts positive modes right.
    :L_k L_{-k}: = L_{-k}L_k for k>0, and L_0^2 for k=0.
    On vacuum: all L_k|0> = 0 for k >= -1 (well, k >= 0 since L_{-1}|0>=0 too).
    Actually L_k|0> = 0 for k >= -1. So :L_k L_{-k}:|0> = L_{-k}L_k|0> = 0 for k >= 1.
    And L_0^2|0> = 0. So Λ_0|0> = 0.

    Therefore [W_4, W_{-4}]|0> = 2c|0>.
    G_{W,W} = <0|W_4 W_{-4}|0> = 2c.

    Cross terms:
    <0|L_4 W_{-4}|0> = <0|[L_4, W_{-4}]|0> = <0|(4-(-4)+1) ...
    Actually [L_m, W_n] = (2m-n) W_{m+n} (since W is primary of weight 3).
    [L_4, W_{-4}] = (2*4-(-4)) W_0 = 12 W_0
    W_0|0> = 0 (W has no zero-mode contribution to vacuum, or rather W_n|0>=0 for n >= -2).
    Wait: W_n|0> = 0 for n >= -2 (since W has weight 3, the mode W_n annihilates for n >= -h+1 = -2).
    So <0|L_4 W_{-4}|0> = 12 * 0 = 0.

    <0|L_2^2 W_{-4}|0>: L_2 W_{-4} = [L_2, W_{-4}] + W_{-4}L_2 = (2*2-(-4))W_{-2} + W_{-4}L_2
    = 8 W_{-2} + W_{-4}L_2
    L_2|0> is not 0... wait, L_n|0> = 0 for n >= -1, so L_2|0> = 0. Yes.
    L_2 W_{-4}|0> = 8 W_{-2}|0> + 0 = 8 W_{-2}|0>
    But W_{-2}|0> = 0 (since -2 >= -2, and W_n|0>=0 for n >= -2).
    So L_2 W_{-4}|0> = 0.
    Then L_2^2 W_{-4}|0> = L_2 * 0 = 0.
    <0|L_2^2 W_{-4}|0> = 0.

    So the Gram matrix is BLOCK DIAGONAL: the W_{-4}|0> state decouples from the Virasoro states.
    """
    # Virasoro block (2x2) — same as virasoro_level4_gram
    G_vir = virasoro_level4_gram()

    # W_{-4} norm
    G_WW = 2*c  # [W_4, W_{-4}] on vacuum = 2c

    # Cross terms all zero
    G = Matrix([
        [G_vir[0,0], G_vir[0,1], 0],
        [G_vir[1,0], G_vir[1,1], 0],
        [0,          0,          G_WW],
    ])
    return G


def w3_level4_analysis():
    """Analysis of the W_3 level-4 Gram matrix."""
    G = w3_level4_gram()
    det_G = factor(G.det())
    tr_G = expand(G.trace())

    # Characteristic polynomial
    char_poly_matrix = G - lam * Matrix.eye(3)
    char_poly = factor(char_poly_matrix.det())

    return {
        "G": G,
        "det_G": det_G,
        "tr_G": tr_G,
        "char_poly": char_poly,
    }


# ═══════════════════════════════════════════════════════════════════════
# 4. DISCRIMINANT COMPUTATIONS
# ═══════════════════════════════════════════════════════════════════════

def char_poly_discriminant_2x2(tr, det):
    """Discriminant of λ^2 - tr*λ + det = (tr^2 - 4*det)."""
    return expand(tr**2 - 4*det)


def char_poly_as_sympy_poly(G):
    """Return characteristic polynomial of G as a sympy Poly in lambda."""
    n = G.shape[0]
    M = G - lam * Matrix.eye(n)
    p = expand(M.det())
    # The char poly is det(G - λI) = (-1)^n (λ^n - tr λ^{n-1} + ... + (-1)^n det)
    return Poly(p, lam)


def poly_discriminant(p):
    """Discriminant of a polynomial (product of squared differences of roots)."""
    return p.discriminant()


# ═══════════════════════════════════════════════════════════════════════
# 5. MAIN ANALYSIS
# ═══════════════════════════════════════════════════════════════════════

def run_analysis():
    """Run the full Kac-Chevalley analysis."""
    results = {}

    # ── Level 4 Virasoro ──
    print("=" * 70)
    print("1. VIRASORO LEVEL 4 (2-dimensional)")
    print("=" * 70)

    a4 = virasoro_level4_analysis()
    print(f"  G = {a4['G'].tolist()}")
    print(f"  det(G) = {a4['det_G']}")
    print(f"  expected det = {factor(a4['det_G_expected'])}")
    print(f"  match: {simplify(a4['det_G'] - a4['det_G_expected']) == 0}")

    tr4 = a4['tr_G']
    det4 = expand(a4['det_G'])
    disc4 = factor(char_poly_discriminant_2x2(tr4, det4))
    print(f"  tr(G) = {tr4}")
    print(f"  disc(char poly) = tr^2 - 4 det = {disc4}")

    # The Chevalley discriminant of A_1 is just (λ_1 - λ_2)^2 = disc of char poly
    print(f"\n  Kac det = {factor(det4)}")
    print(f"  Chevalley disc (A_1) = {disc4}")

    # Check: do they share common factors in c?
    det4_factors = factor(det4)
    disc4_factors = disc4
    print(f"\n  det(G) factored = {det4_factors}")
    print(f"  disc factored = {disc4_factors}")
    results["level4_det"] = det4_factors
    results["level4_disc"] = disc4_factors

    # ── Level 6 Virasoro ──
    print("\n" + "=" * 70)
    print("2. VIRASORO LEVEL 6 (4-dimensional)")
    print("=" * 70)

    a6 = virasoro_level6_analysis()
    print(f"  det(G) = {a6['det_G']}")

    # Compute discriminant of char poly
    G6 = virasoro_level6_gram()
    cp6 = char_poly_as_sympy_poly(G6)
    print(f"  char poly degree = {cp6.degree()}")
    print(f"  char poly = {cp6.expr}")

    print("  Computing discriminant of degree-4 char poly...")
    disc6 = factor(poly_discriminant(cp6))
    print(f"  disc(char poly) = {disc6}")
    results["level6_det"] = a6['det_G']
    results["level6_disc"] = disc6

    # ── W_3 Level 4 ──
    print("\n" + "=" * 70)
    print("3. W_3 LEVEL 4 (3-dimensional)")
    print("=" * 70)

    aw3 = w3_level4_analysis()
    print(f"  G = {aw3['G'].tolist()}")
    print(f"  det(G) = {aw3['det_G']}")
    print(f"  Block diagonal: Virasoro 2x2 + W-scalar 1x1")
    print(f"  det = det(G_Vir) * 2c = c^2(5c+22)/2 * 2c = c^3(5c+22)")

    expected_det_w3 = c**3 * (5*c + 22)
    print(f"  expected det = {factor(expected_det_w3)}")
    print(f"  match: {simplify(expand(aw3['det_G']) - expected_det_w3) == 0}")

    # Char poly discriminant for the 3x3
    # Since block-diagonal, eigenvalues are {eigenvalues of 2x2 block, 2c}
    # The A_2 discriminant is (λ1-λ2)^2(λ1-λ3)^2(λ2-λ3)^2
    G_w3 = w3_level4_gram()
    cp_w3 = char_poly_as_sympy_poly(G_w3)
    print(f"  char poly = {cp_w3.expr}")
    disc_w3 = factor(poly_discriminant(cp_w3))
    print(f"  disc(char poly) = {disc_w3}")
    results["w3_level4_det"] = aw3['det_G']
    results["w3_level4_disc"] = disc_w3

    # ── Summary ──
    print("\n" + "=" * 70)
    print("4. VERDICT: KAC-CHEVALLEY CONNECTION")
    print("=" * 70)

    print("""
  The Kac determinant det(G) = product of eigenvalues.
  The Chevalley discriminant = product of (λ_i - λ_j)^2.

  These are ALGEBRAICALLY INDEPENDENT invariants of the eigenvalue set:
    - det(G) is the elementary symmetric polynomial e_d(λ_1,...,λ_d)
    - disc is the square of the Vandermonde determinant

  At level 4 (d=2):
    det(G) = c^2(5c+22)/2
    disc   = (see above)

  The SHARED VANISHING LOCUS is the key test:
    - det(G) = 0 when c = 0 or c = -22/5
    - disc = 0 when two eigenvalues COINCIDE (which may happen at different c values)

  If det(G) | disc (det divides disc), that would be a genuine factorization.
  If not, the connection is SPURIOUS.
""")

    # Test divisibility for level 4
    det4_poly = Poly(expand(a4['det_G']), c)
    disc4_poly = Poly(expand(char_poly_discriminant_2x2(tr4, expand(a4['det_G']))), c)
    print(f"  Level 4: det(G) as poly in c: {det4_poly.expr}")
    print(f"  Level 4: disc as poly in c: {disc4_poly.expr}")

    # Check if det divides disc
    q, r = disc4_poly.div(det4_poly)
    print(f"  disc / det: quotient = {q.expr}, remainder = {r.expr}")
    divides_4 = r.is_zero
    print(f"  det(G) | disc(char poly) at level 4? {divides_4}")

    # Test divisibility for level 6
    det6_poly = Poly(expand(G6.det()), c)
    disc6_poly = Poly(expand(poly_discriminant(cp6)), c)
    q6, r6 = disc6_poly.div(det6_poly)
    divides_6 = r6.is_zero
    print(f"  det(G) | disc(char poly) at level 6? {divides_6}")

    # Test divisibility for W_3
    det_w3_poly = Poly(expand(G_w3.det()), c)
    disc_w3_poly = Poly(expand(poly_discriminant(cp_w3)), c)
    q_w3, r_w3 = disc_w3_poly.div(det_w3_poly)
    divides_w3 = r_w3.is_zero
    print(f"  det(G) | disc(char poly) at W_3 level 4? {divides_w3}")

    # Check shared zeros
    print("\n  SHARED ZERO ANALYSIS:")
    print("  Level 4:")
    print(f"    det(G) zeros: c=0 (double), c=-22/5")
    disc4_expanded = expand(char_poly_discriminant_2x2(tr4, expand(a4['det_G'])))
    disc4_at_0 = disc4_expanded.subs(c, 0)
    disc4_at_m225 = simplify(disc4_expanded.subs(c, Rational(-22, 5)))
    print(f"    disc at c=0: {disc4_at_0}")
    print(f"    disc at c=-22/5: {disc4_at_m225}")

    # The real question: does (5c+22) appear as a factor of disc?
    disc4_f = factor(disc4_expanded)
    print(f"    disc factored: {disc4_f}")
    print(f"    Does (5c+22) divide disc? Check if disc(c=-22/5)=0: {disc4_at_m225 == 0}")

    print("\n  CONCLUSION:")
    if disc4_at_m225 == 0:
        print("  The Kac zero c=-22/5 IS a zero of the Chevalley discriminant.")
        print("  This means eigenvalues COINCIDE when the Kac det vanishes — GENUINE connection.")
    else:
        print("  The Kac zero c=-22/5 is NOT a zero of the Chevalley discriminant.")
        print("  The connection is SPURIOUS at level 4.")

    return results


if __name__ == "__main__":
    run_analysis()
