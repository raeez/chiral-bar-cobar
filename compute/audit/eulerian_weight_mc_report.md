# Eulerian Weight Decomposition of the MC Equation

## Summary

The coshuffle bar complex Sym^c(s^{-1}A) decomposes in char 0 via
Eulerian idempotents: Sym^c = bigoplus_{r >= 1} (Lie^c)^{odot r}.
Weight 1 = Harrison/Lie (primitives). Weight r >= 2 = symmetric
decomposables. This report records the precise role of each
Eulerian weight in the MC equation D*Theta + (1/2)[Theta, Theta] = 0.

Engine: `compute/lib/eulerian_weight_mc_engine.py` (10 sections, 1109 lines)
Tests: `compute/tests/test_eulerian_weight_mc_engine.py` (67 tests, all pass)

## Core Results

### 1. Kappa Eulerian weight is determined by desuspended degree parity

At arity 2, S_2 = {id, (12)} acts on (s^{-1}a)^{tensor 2} by the
sign (-1)^{d^2} = (-1)^d where d = |s^{-1}a| = conformal_weight - 1.

- d even (trivial S_2 rep): e_1 acts as 0, e_2 acts as 1.
  Kappa lives ENTIRELY in weight 2 (symmetric).
- d odd (sign S_2 rep): e_1 acts as 1, e_2 acts as 0.
  Kappa lives ENTIRELY in weight 1 (Harrison).

Verified algebraically: e_1 = (1/2)(id - (12)) at n=2 is the
antisymmetrizer. On trivial rep it kills; on sign rep it preserves.

| Family      | Generator   | Conf wt | Desusp deg | Parity | kappa weight |
|-------------|-------------|---------|------------|--------|--------------|
| Heisenberg  | J (alpha)   | 1       | 0          | even   | 2            |
| Virasoro    | T           | 2       | 1          | odd    | 1            |
| Free fermion| psi         | 1       | 0          | even   | 2            |
| bc ghosts   | beta        | 1       | 0          | even   | 2            |
| bc ghosts   | gamma       | 0       | -1         | odd    | 1            |
| W_3         | T           | 2       | 1          | odd    | 1            |
| W_3         | W           | 3       | 2          | even   | 2            |

### 2. Heisenberg kappa = k at weight 2; Virasoro kappa = c/2 at weight 1

Heisenberg (d=0 even): the genus-1 obstruction is the symmetric square
(s^{-1}J)^2 / 2 in Sym^2(Lie^c_1). Harrison at arity >= 2 vanishes
because the free Lie algebra on one even generator is trivial there.

Virasoro (d=1 odd): the genus-1 obstruction is [s^{-1}T, s^{-1}T] in
Lie^c_2. This is nonzero because s^{-1}T is odd: [x,x] != 0 in the
super bracket. The symmetric square Sym^2(Lie_1) vanishes (exterior
square of 1-dim odd space is zero).

This is the OPPOSITE structure: Heisenberg kappa is decomposable,
Virasoro kappa is primitive.

### 3. W_3 kappa decomposes across weights

W_3 has generators T (d=1 odd) and W (d=2 even). At arity 2:

- TT block: sign rep of S_2. e_1 = 1. kappa_TT in weight 1.
- WW block: trivial rep of S_2. e_1 = 0. kappa_WW in weight 2.
- TW/WT block: mixed rep. Matrix [[0,-1],[-1,0]] with eigenvalues +/-1.
  e_1 projects onto sigma-eigenvalue -1 (the antisymmetric combination
  e_TW + e_WT). e_2 projects onto sigma-eigenvalue +1 (e_TW - e_WT).
  Cross-term kappa_TW decomposes into both weights.

Total: kappa(W_3) = kappa_TT [wt 1] + kappa_WW [wt 2] + kappa_TW [wt 1+2].
Since kappa_TW = 0 by weight parity on M_{1,1} (T has weight 2, W has
weight 3; mixed propagator integral vanishes): effective decomposition
is kappa_TT = c/2 [wt 1] + kappa_WW [wt 2], summing to 5c/6.

### 4. The MC equation is NOT weight-graded

The Lie bracket on Hom(Sym^c, A) IS determined by the weight-1
(Harrison) restriction via PBW. But the MC equation also involves:

(a) The differential D, which changes arity (edge contraction, self-sewing)
    and therefore moves between different Eulerian decomposition contexts.
(b) The BV operator Lambda at genus >= 1, which contracts pairs and
    mixes weights.

The bracket does not map weight-j x weight-k to a definite weight at
the output arity because weight is defined per-arity, and the bracket
changes arity.

Result: the MC equation cannot be projected weight-by-weight.
At genus 0 and FIXED arity, per-weight analysis is informative.
At genus >= 1, weight mixing through the BV operator is unavoidable.

### 5. Shadow coefficients S_r and Eulerian weight

For a single generator of desuspended degree d:

- d even: S_n acts trivially on (s^{-1}a)^{tensor r}. The 1-dim
  coinvariant Sym^r is entirely in weight r. Shadow coefficients
  live at maximal weight.
- d odd: S_n acts by sign. Lambda^r(1-dim) = 0 for r >= 2. The
  single-generator sector contributes nothing at arity >= 2.

For Virasoro (d=1 odd): the single-generator-no-derivatives sector
contributes 0 at arity >= 2. ALL nontrivial S_r comes from the
derivative tower: partial^k T has desuspended degree 1+k, alternating
between odd (k even) and even (k odd). The even-degree derivatives
provide the symmetric-weight components that populate the shadow tower.

At arity 3: e_1 acts as 0 on BOTH trivial and sign reps of S_3
(verified computationally for the 1-dim representations). So S_3 for
a single generator (in either parity) lives entirely in weight >= 2.

Pattern for Virasoro: e_1 on sign rep of S_n = 0 for all n >= 2.
This means Harrison contributes 0 from the base generator at all
arities >= 2. The entire shadow tower beyond kappa is built from
derivatives and multi-field insertions.

### 6. The derivative tower mechanism

For conformal weight h, the k-th derivative partial^k(generator) has
desuspended degree h + k - 1. The parity alternates:

| k | Virasoro (h=2) | Heisenberg (h=1) |
|---|----------------|------------------|
| 0 | d=1 (odd)      | d=0 (even)       |
| 1 | d=2 (even)     | d=1 (odd)        |
| 2 | d=3 (odd)      | d=2 (even)       |
| 3 | d=4 (even)     | d=3 (odd)        |

This alternation provides generators of BOTH parities at the bar level,
enabling nontrivial Eulerian decomposition at all arities. This is the
mechanism by which Virasoro has infinite shadow depth despite having a
single generator of odd desuspended degree: the derivatives supply the
even-degree fields that fill the symmetric Eulerian components.

For Heisenberg: the base generator (even) already sits in the symmetric
component. But derivatives (starting at d=1 odd) could in principle
contribute Harrison terms. They do not, because Heisenberg has class G
(shadow depth 2): all S_r = 0 for r >= 3.

## Verification Summary

67 tests in 11 groups:
- Group 1 (6 tests): Eulerian idempotent algebraic properties (e_1^2=e_1, e_1+complement=id, trace)
- Group 2 (6 tests): Koszul sign computation (AP45 compliance, all generator types)
- Group 3 (9 tests): Kappa Eulerian weight for Heisenberg, Virasoro, free fermion (single gen)
- Group 4 (7 tests): W_3 multi-generator decomposition (TT/WW/mixed blocks)
- Group 5 (7 tests): MC equation weight structure (not graded, bracket from wt 1, differential mixes)
- Group 6 (4 tests): Shadow tower Eulerian weights at arity 1, 2, 3+
- Group 7 (6 tests): Eulerian weight dimension counts (trivial and sign reps at n=2,3)
- Group 8 (7 tests): Derivative tower parity alternation for Virasoro and Heisenberg
- Group 9 (4 tests): Arity-3 Eulerian decomposition (Harrison vanishes for 1-dim at n=3)
- Group 10 (7 tests): Cross-consistency (multi-path: weight sums, F_1 ratios, structural theorem)
- Group 11 (4 tests): Permutation algebra utilities (composition, inverse, group algebra)

Multi-path verification of central claim (kappa weight determined by parity):
1. Direct computation via Eulerian idempotent action on S_2 representations
2. Cross-check: e_1^2 = e_1 confirms genuine projection
3. Consistency: weight fractions sum to 1 (completeness)
4. Parameter sweep: all even degrees give weight 2, all odd give weight 1
5. Cross-family: F_1(Vir_c) = F_1(H_k) when kappa values match (c=2k)

## Manuscript Implications

1. The Heisenberg-Virasoro dichotomy (kappa weight 2 vs weight 1) is a
   REPRESENTATION-THEORETIC fact tracing to the parity of conformal
   weight minus 1. It is not a dynamical property of the MC equation.

2. For multi-generator algebras (W_3, W_N), the channel decomposition of
   kappa into weight-1 and weight-2 components follows from the per-generator
   desuspended degree parities. The cross-channel corrections at genus >= 2
   (delta_F_g^cross) involve mixed Eulerian weight components.

3. The infinite shadow depth of Virasoro (class M) despite having a single
   generator with odd desuspended degree (which kills the coinvariant space
   at arity >= 2) is resolved by the derivative tower: partial^k T for odd k
   provides even-degree fields in the bar complex.

4. The MC equation is not weight-graded, but the bracket structure IS
   determined by the Harrison (weight-1) restriction. This is a precise
   version of the statement that "the Lie bracket is determined by Lie^c."

Cross-references:
- rem:three-bar-complexes (bar_construction.tex:1741): Eulerian decomposition stated
- ex:com-lie-prototype (algebraic_foundations.tex:1364): Harrison complex definition
- thm:shadow-formality-identification (higher_genus_modular_koszul.tex): shadow = L_inf formality
- thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex): MC element construction
