# Attack-and-heal: antipode non-lifting + AP263 Hopf→bialgebra rename propagation

**Date.** 2026-04-18.
**Author.** Raeez Lorgat.
**Scope.** Cross-volume propagation across
`/Users/raeez/chiral-bar-cobar` (Vol~I),
`/Users/raeez/chiral-bar-cobar-vol2` (Vol~II),
`/Users/raeez/calabi-yau-quantum-groups` (Vol~III).
**AP block.** AP801--AP820 (this session).

## 1. Summary

CLAUDE.md AP263 is the naming discipline "Hopf-vs-bialgebra naming drift":
a theorem advertised as "quantum group equivalence" or "Hopf algebra
structure" that constructs only a bialgebra because the antipode does not
lift.  The underlying PROVED NEGATIVE lives in Vol~I at
`chapters/theory/ordered_associative_chiral_kd.tex:9510-9673`
(`prop:w-infty-antipode-obstruction`, `\ClaimStatusProvedHere`): the
Yangian antipode $S(T(u)) = T(u)^{-1}$ does not lift to a vertex-algebraic
antipode on $\cW_{1+\infty}[\Psi]$ because of two independent obstructions,
an OPE quartic-pole obstruction vanishing only at $\Psi \in \{1, 2\}$ and a
universal Hopf-axiom residual $-(\Psi-1)/z^2 + z \cdot J$ with a $z \cdot J$
tail that persists at every $\Psi$.

CLAUDE.md records the 2026-04-17 heal of `thm:chiral-qg-equiv` to "chiral
bialgebra equivalence on the Koszul locus" as partial (\textasciitilde 16
sites remained).  This session closes additional sites and classifies the
remaining Hopf mentions.

## 2. Underlying PROVED NEGATIVE, re-verified

The theorem body at Vol~I
`chapters/theory/ordered_associative_chiral_kd.tex:9510-9673` is sound under
direct re-reading:

- (i) Explicit antipode: $S(J) = -J$, $S(T) = -T + (\Psi-1)/\Psi \cdot
  {:}JJ{:}$ via Miura inversion of
  $\psi_1 = J$, $\psi_2 = T + J^2/(2\Psi)$; involutive ($S^2 = \mathrm{id}$).
  Rank-1 computation uses commutativity of the $\psi_i$.
- (ii) OPE obstruction: direct Wick-theorem computation gives
  $S(T)_{(3)} S(T) = c/2 + 2(\Psi-1)(\Psi-2)$, matching the Virasoro
  quartic pole $c/2$ only at $\Psi \in \{1, 2\}$.
- (iii) Hopf-axiom obstruction: four-term expansion of
  $\Delta_z(T) = T \otimes 1 + 1 \otimes T + ((\Psi{-}1)/\Psi) J \otimes J
   + z\,(1 \otimes J)$ produces
  $m_z \circ (S \otimes \mathrm{id}) \circ \Delta_z(T)
   = -(\Psi-1)/z^2 + z \cdot J$.
  The $z \cdot J$ tail is present at all $\Psi$, including the OPE-clean
  locus $\Psi = 1$, proving the two obstructions are independent.

The proof is self-contained: no forward references to uninscribed lemmas,
no cross-volume dependencies.  The two obstruction loci $\{\Psi \in
\{1, 2\}\}$ and $\emptyset$ (the Hopf locus is empty) are disjoint, so
neither reduces to the other.

No adversarial finding against the PROVED NEGATIVE surfaced in this
session.

## 3. Site inventory: Hopf mentions across three volumes

The comprehensive enumeration of `grep -rn 'Hopf'` over
`chapters/`, `standalone/`, `appendices/` of each volume produced the
following classification.  Counts are chapter-file hits (excluding
`notes/`, `compute/`, `adversarial_swarm_*`).

### 3.1 Legitimate Hopf (keep)

These are sites where "Hopf" correctly refers to one of: (A) classical
Hopf algebra on the point-value Yangian fibre; (B) discussion of the
antipode non-lifting obstruction itself (Hopf is being NEGATED); or
(C) a CONJECTURAL Drinfeld-double programme object explicitly named as
"chiral Hopf object" with conditional status.

| File | Lines | Category | Justification |
|------|-------|----------|---------------|
| Vol~I `chapters/examples/yangians_foundations.tex` | 601, 3955 | A | Classical Yangian Hopf-algebra involution at the point value |
| Vol~I `chapters/connections/outlook.tex` | 364 | unrelated | "Hopf fibration" is topology |
| Vol~I `chapters/theory/mc3_five_family_platonic.tex` | 698 | A | Non-reductive Hopf structure of the super-Yangian classical fibre |
| Vol~I `chapters/theory/ordered_associative_chiral_kd.tex` | 8496, 8518, 9500, 9503, 9507, 9511, 9564, 9583, 9992-10000, 10503, 10505 | B | The PROVED NEGATIVE body and its remarks; Hopf is the target of negation |
| Vol~I `chapters/frame/preface.tex` | 1123 | B | "classical antipode does not lift" caveat |
| Vol~I `chapters/theory/introduction.tex` | 2389 | B | "chiral bialgebra equivalence PROVED on ordered Koszul locus; antipode does not lift" |
| Vol~I `standalone/survey_modular_koszul_duality_v2.tex` | 4879-4883 | B | Explicit discussion of the two obstructions |
| Vol~I `standalone/survey_modular_koszul_duality_v2.tex` | 8308-8311 | C | Drinfeld double programme "Hopf object" frontier item |
| Vol~I `standalone/ordered_chiral_homology.tex` | 3485-3538 | B | Dual inscription of the PROVED NEGATIVE |
| Vol~II `chapters/theory/unified_chiral_quantum_group.tex` | 195-213 | B | `rem:ucqg-bialgebra-not-hopf` already correctly inscribed |
| Vol~II `chapters/connections/spectral-braiding-frontier.tex` | 2698, 2714, 2716, 3016, 6106 | C | Drinfeld double programme "chiral Hopf object" in `conj:drinfeld-double-e1-construction` |
| Vol~II `chapters/connections/ordered_associative_chiral_kd_frontier.tex` | 5822, 5914, 6106 | C | "$E_1$-chiral Hopf-like object" / "$E_1$-chiral Hopf object" under `conj:drinfeld-double-e1-construction` |
| Vol~II `chapters/connections/ordered_associative_chiral_kd_core.tex` | 1402-1435 | A | Dimofte $K$-matrix vs classical "primitive (Hopf) coproduct" + Majid double-bosonization classical reference |
| Vol~II `chapters/connections/hochschild.tex` | 5082 | C | "chiral Hopf algebra controlling line-operator braiding" in a conditional derived-center heuristic |
| Vol~II `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex` | 1118 | C | "coideal in a chiral Hopf algebra" under conditional construction |
| Vol~II `chapters/connections/spectral-braiding-core.tex` | 431-432 | A | "Hopf coproduct on a chiral quantum group" referring to the primitive-coproduct class~G case |
| Vol~III `chapters/theory/quantum_groups_foundations.tex` | 304 | A | Classical Hopf algebra $C(\cC, q)$ in a braided category |
| Vol~III `chapters/theory/en_factorization.tex` | 2391 | unrelated | "algebraic Hopf link" (topological Hopf link, unrelated to Hopf algebras) |
| Vol~III `chapters/theory/quantum_chiral_algebras.tex` | 127, 356, 692, 1006, 1037, 1044, 1058, 1477, 1568, 2350 | A | Point-value MTC "Hopf-algebra-in-braided-category" + Dimofte $K$-matrix primitive-coproduct reference |
| Vol~III `chapters/examples/k3_chiral_algebra.tex` | 785 | B | "$E_\infty$ averaging map kills the Hopf structure" retraction |
| Vol~III `chapters/frame/preface.tex` | 1301, 1607 | B-in-context | "$E_1$-chiral Hopf axiom system" naming the five-axiom system whose realisation is class-dependent |
| Vol~III `chapters/theory/introduction.tex` | 1269, 1279, 1281, 1666, 1700 | B-in-context | Same naming convention as preface |
| Vol~III `chapters/theory/e1_chiral_algebras.tex` (Heisenberg `ex:heisenberg-bialgebra`) | 1398, 1422 clauses (i)--(iv) | A | Class-G Heisenberg genuinely satisfies the five-axiom system with primitive $\Delta$ and involutive $S$ |

### 3.2 AP263 violations (healed this session)

| File | Line(s) before | Type | Healing |
|------|---------------|------|---------|
| Vol~I `standalone/cy_quantum_groups_6d_hcs.tex` | 546 | Subsection title | Renamed "The CoHA carries $\Eone$-chiral Hopf data" $\to$ "The CoHA carries $\Eone$-chiral bialgebra data" |
| Vol~I `standalone/cy_quantum_groups_6d_hcs.tex` | 551, 554 | Proposition title + body | Renamed "CoHA Hopf data" $\to$ "CoHA $\Eone$-chiral bialgebra data"; "an $\Eone$-chiral Hopf algebra" $\to$ "an $\Eone$-chiral bialgebra"; inserted forward pointer to `rem:v3-qg-antipode` and Vol~I `prop:w-infty-antipode-obstruction` |
| Vol~I `standalone/cy_quantum_groups_6d_hcs.tex` | 574-581 | Proposition (H5) clause | Relabelled "Hopf axiom" $\to$ "Classical antipode, non-lifting at the chiral level"; body rewritten to state that the classical Yangian antipode does not lift, with the CoHA declared a chiral bialgebra not a chiral Hopf algebra |
| Vol~III `chapters/theory/e1_chiral_algebras.tex` | after 1182 | Scope remark insertion | Appended "Scope of (H5): class~$\mathbf{G}$ versus non-class-$\mathbf{G}$ landscape" paragraph to `rem:e1-hopf-axiom-summary`, making explicit that (H5) is realised on the nose only for class~G, with the W_{1+∞} case forbidden by Vol~I `prop:w-infty-antipode-obstruction` |
| Vol~III `chapters/theory/e1_chiral_algebras.tex` | 1422 | Conjecture body | "carries an $E_1$-chiral Hopf algebra structure" $\to$ "carries an $E_1$-chiral bialgebra structure (axioms (H1)--(H4))" in `conj:w1inf-e1-bialgebra` |
| Vol~III `chapters/theory/e1_chiral_algebras.tex` | 1431-1433 | Conjecture (ii) clause | Relabelled "Antipode" $\to$ "Classical antipode, non-lifting at the chiral level" and inserted pointer to Vol~I `prop:w-infty-antipode-obstruction` |

### 3.3 AP40 violation swept during the AP263 heal

| File | Line | Before | After |
|------|------|--------|-------|
| Vol~I `standalone/cy_quantum_groups_6d_hcs.tex` | 1008-1014 | `\begin{proposition}[7d hCS boundary algebra]` with `\ClaimStatusConjectured` | `\begin{conjecture}[7d hCS boundary algebra]`; label retargeted `prop:7d-hcs-boundary-algebra` $\to$ `conj:7d-hcs-boundary-algebra`; no external consumers in the manuscript so no cross-volume propagation needed |

## 4. Remaining AP263 frontier (catalogued, not healed this session)

The AP186 shallow-correction discipline and the constitutional trust
warning both counsel against bulk AP263 prose substitution without a
first-principles pass per site.  The following sites carry "Hopf" in a
chiral-algebra context and require per-site classification:

- Vol~II `chapters/connections/spectral-braiding-frontier.tex` at
  `rem:drinfeld-double-programme`, `conj:drinfeld-double-antipode`,
  `conj:drinfeld-double-e1-construction`: the "chiral Hopf object"
  and "quasi-triangular chiral Hopf object" are CONJECTURAL programme
  targets.  Correct AP263 reading: KEEP, because the object is not
  constructed, so the Hopf label is a target attribute not a realised
  structure.
- Vol~II `chapters/connections/ordered_associative_chiral_kd_frontier.tex`
  `5822, 5914, 6106`: identical analysis.
- Vol~II `chapters/connections/hochschild.tex:5082` "chiral Hopf algebra
  controlling line-operator braiding": used heuristically in a derived-center
  discussion.  Recommended heal: replace "chiral Hopf algebra" with "chiral
  bialgebra with Drinfeld coproduct" in the surrounding prose, pending
  first-principles read of the full paragraph.
- Vol~II `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:1118`:
  "coideal in a chiral Hopf algebra defined as the orthogonal complement of a
  subalgebra under the bar pairing".  Recommended heal: rename to "coideal in a
  chiral bialgebra", pending verification that the coideal construction does
  not invoke antipode.
- Vol~III `chapters/theory/e1_chiral_algebras.tex` title of
  `def:e1-chiral-antipode` and `rem:e1-hopf-axiom-summary`: retained as
  the obstruction-target naming (class-G realisation is genuine;
  non-class-G inscription now carries the scope remark added this session).
  Retagging the definition from "$E_1$-chiral Hopf algebra" to
  "$E_1$-chiral bialgebra with antipode when it lifts" is a semantic
  restructure that touches a full chapter plus several downstream
  (en_factorization, quantum_groups_foundations, braided_factorization);
  deferred to a dedicated AP263 chapter rectification.
- Vol~III `chapters/theory/introduction.tex` and
  `chapters/frame/preface.tex` parallel usage (lines 1269-1700 and
  1301, 1607): same issue, same deferred resolution.
- Vol~III `chapters/theory/quantum_chiral_algebras.tex`
  "chiral quantum group is the Hopf-algebra-in-braided-category structure on
  $\Rep^{\Etwo}(A^!)$" (lines 356, 1006, 1037, 1044, 1058, 1568, 2350):
  classical Hopf-in-braided-category is the POINT-VALUE representation
  category; this is AP263 category-A (legitimate classical Hopf) in every
  instance I spot-checked, but deserves a dedicated first-principles sweep.

## 5. Commit-gate status

No commits produced in this session.  Files edited in-tree; patch file
emitted at
`/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260418/patches/patch_antipode_hopf_bialgebra_20260418.patch`.

Build status: NOT RUN this session (the hook flagged 1680+ edits
accumulated since last build, but building is out-of-scope for a
propagation-and-heal task).  Per Session Protocol step 9 and the
PreToolUse commit-hook warning, before any commit of these edits the
session-end builder must run:

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II (N/A this session)
cd ~/calabi-yau-quantum-groups && make fast                       # Vol III
make test                                                         # Fast tests
```

Authorship: Raeez Lorgat only.  No AI attribution anywhere.  No
em-dashes introduced.  HZ-1..HZ-11 verified on the edited regions:
- HZ-1 (level prefix): no r-matrix writes in this session.
- HZ-2 (environment matches tag): `\begin{conjecture}` with
  `\ClaimStatusConjectured` at the 7d hCS conjecture; the renamed Vol~III
  `conj:w1inf-e1-bialgebra` remains `\begin{conjecture}` with
  `\ClaimStatusConjectured`.
- HZ-5 (label discipline): new label `conj:7d-hcs-boundary-algebra` grep'd
  across three volumes; zero matches; uniqueness established.
- HZ-8 (proof after conjecture): no new proof blocks introduced.
- HZ-10 (AI slop): grep'd edited regions for
  `notably|crucially|remarkably|interestingly|furthermore|moreover|delve|leverage|tapestry|cornerstone`;
  zero hits.
- HZ-11 (cross-volume ProvedHere): no new ProvedHere theorems; the
  Vol~III inscriptions remain Conjectured.

## 6. Follow-up items

Flagged during this session but out of scope:
- Vol~III `chapters/theory/e1_chiral_algebras.tex` pre-existing AP24/AP8
  violations at lines 534, 738, 2482 (now 2491-2493 after the (H5) scope
  remark insertion): `\kappa_{\mathrm{ch}}(H_k) + \kappa_{\mathrm{ch}}(H_k^!)
  = k + (-k) = 0` untagged for family scope; `\kappa_{\mathrm{ch}} +
  \kappa_{\mathrm{BKM}} = 0$` untagged; "$\Vir_{13}$ Koszul self-dual under
  $c \mapsto 26-c$" needs the explicit $c = 13$ scope qualifier.  Not the
  subject of this AP263 propagation but flagged by the hook and forwarded.
- Full chapter-level AP263 sweep of Vol~III `e1_chiral_algebras.tex`
  `def:e1-chiral-antipode` + `rem:e1-hopf-axiom-summary` naming discipline
  (deferred per Section~4).
- Vol~II `chapters/connections/hochschild.tex:5082` and
  `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:1118`
  per-site heals (deferred per Section~4).
