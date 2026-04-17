# Wave 11 — Vol II Part II (E_1 Core) Adversarial Attack and Heal

Date: 2026-04-17
Author: Raeez Lorgat
Scope: Vol II (~/chiral-bar-cobar-vol2), Part II "The E_1 Core" (main.tex:1419-1467).

## Part II inventory

Ten chapter inputs (main.tex:1457-1466):

1. `connections/bar-cobar-review.tex` (~202 KB)
2. `connections/line-operators.tex` (~103 KB)
3. `connections/ordered_associative_chiral_kd_core.tex` (~203 KB)
4. `connections/dg_shifted_factorization_bridge.tex` (~89 KB)
5. `connections/thqg_gravitational_yangian.tex` (~118 KB)
6. `connections/typeA_baxter_rees_theta.tex` (~62 KB)
7. `connections/shifted_rtt_duality_orthogonal_coideals.tex` (~42 KB)
8. `connections/casimir_divisor_core_transport.tex` (~50 KB)
9. `theory/unified_chiral_quantum_group.tex` (~71 KB)
10. `theory/super_chiral_yangian.tex` (~58 KB)

## Attack vector verdicts

| # | Vector | Verdict |
|---|--------|---------|
| i | CG deficiency opening | PASS — part-prolog (main.tex:1419-1456) opens with the Part I → Part II transition as a deficiency of the closed-colour symmetric bar (av kills R-matrix); unified chiral QG opens with nine-fold fragmentation as the literature deficiency. |
| ii | AP159 four Yangian types | PASS (mostly). `ordered_associative_chiral_kd_core.tex` §5033 Convention + `dg_shifted_factorization_bridge.tex` §2192 Convention + `shifted_rtt_duality_orthogonal_coideals.tex` §1041 Convention explicitly enumerate the four types. GAP: `unified_chiral_quantum_group.tex` Prologue (§103-157) lists nine "Yangian"-typed fibres without AP159 pointer. HEALED by new Convention (below). |
| iii | AP161 five E_1-chiral notions | PASS (mostly). `bar-cobar-review.tex` §4171 Convention + `ordered_associative_chiral_kd_core.tex` §5001 Convention explicitly collapse to Notion B+E working default; AP244/W5 collapse theorem referenced. GAP: `unified_chiral_quantum_group.tex` Prologue lacks pointer; HEALED. |
| iv | AP170 two Yangian definitions | PASS. Both `ordered_associative_chiral_kd_core.tex` §5068 and `dg_shifted_factorization_bridge.tex` §2234 install the "equivalence open" remark pointing at def:e1-chiral-yangian vs def:chiral-yangian-datum. |
| v | E_1-First Prose Architecture (ordered primitive, av to symmetric) | PASS. Part-prolog makes the ordered bar primitive explicit; `ordered_associative_chiral_kd_core.tex` §5110 Proposition states av(r(z)) = κ for abelian/scalar, av(r(z)) + dim(g)/2 = κ for Kac-Moody (Sugawara shift). |
| vi | Chiral bialgebra not Hopf (Wave-2 heal) | PASS (mostly). `thqg_gravitational_yangian.tex` §1608 Remark "Bialgebra, not Hopf algebra" is explicit; `line-operators.tex` never misasserts chiral Hopf. GAP: `super_chiral_yangian.tex:188` had "graded Hopf bialgebra" (redundant + over-asserts antipode at chiral level). HEALED. `unified_chiral_quantum_group.tex` Prologue sextuple Q_g^{k,f,μ} lists S (antipode) without qualifying that S is classical-fibre data; HEALED with new Remark. |
| vii | FF screening obstruction (Ψ-1)/Ψ at chiral 1-cocycle | PASS. `bar-cobar-review.tex` §4260 Proposition + §4280 Remark explicitly flag Ψ=2 coincidence and the Ψ=3 verification at 2/3 ≠ 1/3; correct formula (Ψ-1)/Ψ inherited downstream. |
| viii | Five Objects discipline (A / B(A) / A^i / A^! / Z^der_ch) | PASS. `ordered_associative_chiral_kd_core.tex` keeps Barchord(A), Cobar, A^!_line, and the derived centre (Part IV dependency) distinct; no "bar-cobar produces bulk" drift detected in Part II. |

## Heal actions

### Heal 1: `super_chiral_yangian.tex:188` (Wave-2 bialgebra-not-Hopf discipline)

"graded Hopf bialgebra" → "graded super-bialgebra" plus explicit scope note that the super-antipode is a separate datum on the classical Etingof-Kazhdan super-Hopf fibre (Geer 2006), not a chiral property of Ysuper_ℏ(g) as E_1-chiral algebra on X.

### Heal 2: `unified_chiral_quantum_group.tex` (AP159/AP161/Wave-2 discipline at the unifier)

Added two tight blocks at the end of the Prologue, before §Setup:

- `\begin{convention}[Yangian-type disambiguation]` (label `conv:ucqg-yangian-types`): explicitly declares Y_ℏ(g) in the nine-fibre list is the classical (type 1, E_1-top on R) Yangian; the dg-shifted, chiral, and spectral types are conversions in `chap:ordered-associative`; the Koszul-dual sextuple slot is chiral Yangian when global and dg-shifted when restricted to a formal disk; av projects spectral R to κ on the symmetric side; affine, shifted, and truncated stay at type 1 with μ as an independent axis; the five E_1-chiral notions collapse to Notion B + Notion E on the Koszul locus (cross-pointer to `conv:ordered-kd-core-five-notions`).

- `\begin{remark}[Bialgebra, not Hopf, at the chiral level]` (label `rem:ucqg-bialgebra-not-hopf`): S in the sextuple Q_g^{k,f,μ} lives on the classical fibre (Nazarov/Molev Berezinian); chiral-level antipode is not automatic, blocked by the two W7-#35 obstructions (OPE obstruction at Ψ∈{1,2} and universal Hopf-axiom obstruction); downstream chapters treat the chiral object as a bialgebra.

### Hygiene: no AP/HZ token in typeset prose; V2-AP26 (hardcoded Part II) fixed to `Part~\ref{part:e1-core}`; referenced `chap:ordered-associative` label verified to exist (line 38 of ordered_associative_chiral_kd_core.tex).

## Residual findings (not healed; not blocking)

- `typeA_baxter_rees_theta.tex` opens with "Yangian frontier" without AP159 pointer; this is acceptable because it is a type-A appendix whose parent chapters already install the convention, but a single cross-pointer would strengthen the opening.
- `casimir_divisor_core_transport.tex` contains no Yangian/Hopf/bialgebra tokens and therefore is AP-clean by omission.

## Files touched

- `chapters/theory/super_chiral_yangian.tex` (1 Edit)
- `chapters/theory/unified_chiral_quantum_group.tex` (3 Edits: Convention + Remark insertion; V2-AP26 Part~II → `\ref{part:e1-core}` fix; `chap:ordered-chiral-KD` → `chap:ordered-associative`)

No commits.
