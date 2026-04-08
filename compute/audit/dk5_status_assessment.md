# DK-5 Status Assessment

## The gap: MC3 (proved) vs DK-5 (open)

MC3 proves thick generation of Rep_fd(Y(g)) by evaluation modules
for ALL simple types (cor:mc3-all-types), giving a braided monoidal
equivalence on the evaluation-generated core:

    Rep_fd(Y(g))|_eval ~ C_eval(A)

DK-5 is the full triple bridge:

    Fact_{E1}(Y(g)) ~ Mod^comp(Y^dg_A) ~ Rep^spec(QG(R_A))^op

The gap decomposes into four precise sub-targets (B1-B4), recorded
in rem:bridge-theorem-programme and concordance.tex:

### Sub-target B1: full O-Koszulness
Extend the Koszul duality equivalence from the evaluation-generated
core to the full category O (or its appropriate completion).
STATUS: OPEN. The evaluation-core equivalence (DK-2/3) is proved via
sectorwise convergence (cor:dk23-all-types). Extension requires
pro-nilpotent completion and thick generation beyond evaluation objects.

### Sub-target B2: tower completion
The completed bar-cobar equivalence for the inverse limit.
STATUS: PARTIALLY PROVED. The Mittag-Leffler condition for the RTT
tower is proved (thm:rtt-mittag-leffler). The strong completion tower
theorem (thm:completed-bar-cobar-strong) gives the formal framework.
What remains is the algebraic identification of the limit with an
RTT-adapted dg model.

### Sub-target B3: boundary/line realization
Identify the boundary algebra as an E1-module over the Yangian.
STATUS: OPEN. This is the HT boundary/line route.

### Sub-target B4: spectral quantum group comparison
The comparison with Latyntsev's spectral quantum group QG^spec(R_A).
STATUS: OPEN. The CG constraint (rem:unified-dk-hierarchy) forces the
DK-5 functor to intertwine the prefundamental TQ system with the
QQ-system, giving a strong structural constraint.

### Bridge Criterion Theorem (thm:bridge-criterion)
B1 + B2 + B4 => full bridge. So B3 is not needed if the other
three are supplied.

## DK-4 vs DK-5 (the two-step decomposition)

DK-4 (conj:dk4-formal-moduli): the tangent Lie algebra g_A of the
factorization formal moduli problem equals the dg-shifted Yangian
Y^dg_A. The H-level target exists unconditionally (Lurie's formal
moduli theorem); the content is the algebraic identification.
STATUS: ML proved; algebraic identification open.

DK-5 (conj:dk5-infty-pbw): given DK-4 and post-core DK-3 extension,
the remaining step is the infinity-categorical PBW theorem for the
factorization Lie algebra g_A.
STATUS: OPEN. Depends on DK-4.

## What the E1 primacy work provides

The session's work (categorical_dk_e1_report.md,
categorical_e1_primacy_report.md) establishes:

### 1. Conceptual clarification
DK is the E1-primitive genus-0 ancestor of the scalar Koszul duality
data. The averaging map av: g^{E1}_A ->> g^mod_A is surjective but
NOT injective (non-splitting, thm:e1-primacy(iv)). The Drinfeld
associator Phi_KZ lives in ker(av) at arity 3.

### 2. Non-splitting obstruction is genuine
The kernel ker(av) is nontrivial: the Casimir product [O_12, O_23]
lies purely in the sign representation of S_3, so av annihilates it.
Cross-arity leakage (D maps ker(av_3) partly into im(av_2)) prevents
any dg Lie section. This is PROVED and computationally verified (47
tests in e1_nonsplitting_obstruction_engine.py).

### 3. Structural constraint on DK-5
The non-splitting means that the braided category C_line = A!-mod
contains strictly more data than its center Z(C_line). This is
expected: the R-matrix and associator are the additional E1 data.
But it also means that any DK-5 functor must preserve this extra
structure, constraining the possible constructions.

### 4. Three bar complexes, three layers
- B(A) (symmetric, E_infty): Theorem A, Verdier intertwining
- B^ord(A) (ordered, E_1): DK bridge, R-matrix, Yangian
- averaging map av: B^ord -> B (surjective, non-split)

This clarifies that DK-5 lives entirely in the E1 world. The passage
to the E_infty world (Theorems A-D) goes through av, losing the
associator data.

## New leverage from the session's work

### Modest
The E1 primacy theorem and non-splitting obstruction are dg Lie level
results. They do not directly close any of B1-B4. However:

(a) The conceptual identification of DK as "un-averaged Koszul duality"
    correctly locates DK-5 within the formal moduli framework: the
    factorization formal moduli problem (def:factorization-formal-moduli)
    is the E1 version of Theorem A's formal moduli.

(b) The non-splitting at arity 3 (Drinfeld associator) constrains B4:
    the spectral quantum group QG^spec(R_A) must have a non-trivial
    associator that maps to the Drinfeld associator under the DK-5
    functor.

(c) The CG constraint (prefundamental TQ/QQ intertwining) combined
    with E1 primacy suggests that the restricted DK-5
    (conj:restricted-dk5) on the evaluation-generated core is the
    natural intermediate target. Two of three ingredients are proved:
    thick generation (all types) and DK-2/3 (evaluation core).
    The missing piece is DK-4 restricted to the generated sector.

## Tools that would close DK-5

### For the restricted DK-5 (conj:restricted-dk5)
The most accessible target. Two of three ingredients proved.
Missing: DK-4 on the evaluation-generated core, i.e., identifying
the tangent Lie algebra restricted to evaluation modules with the
dg-shifted Yangian restricted to the same sector.

Needed tools:
- Explicit computation of the tangent complex T_* F_A on evaluation
  modules (reduce to finite-dimensional linear algebra)
- Comparison with Y^dg_A via the RTT generators on evaluation data
- This is a finite-dimensional problem at each evaluation point

### For the full DK-5 (conj:dk5-infty-pbw)
The hard target. Requires:
1. Post-core DK-3 extension: extend the sectorwise convergence beyond
   evaluation modules. Needs categorical completion technology.
2. DK-4: full tangent Lie algebra identification. Needs the algebraic
   identification of g_A with Y^dg_A as filtered complete dg Lie
   algebras (not just at the H-level).
3. Infinity-PBW: the exponential/group passage from the Lie algebra
   to its formal group. This is the deepest input and likely requires
   new technology in factorization algebra homotopy theory.

### Key external inputs
- Latyntsev's spectral quantum group (2023): provides the target B4
- Lurie's formal moduli (DAG X): provides the abstract framework
- Francis-Gaitsgory pro-nilpotent completion: provides categorical
  completion technology
- Chari-Moura multiplicity-free q-characters: already used for MC3

## Assessment

The gap between MC3 and DK-5 is substantial but well-organized.
The Bridge Criterion (B1+B2+B4 => full bridge) reduces the problem
to three precise inputs. The restricted DK-5 on the evaluation core
is the natural intermediate target with two of three ingredients
proved. The session's E1 primacy work provides conceptual clarity
(correctly locating DK within formal moduli) and structural constraints
(non-splitting, CG intertwining), but does not directly close any
sub-target.

The most productive next step would be attacking restricted DK-4
on the evaluation-generated core: this is a finite-dimensional
problem at each evaluation point and would immediately yield the
restricted DK-5 (conj:restricted-dk5).
