# P13 Vol I Theorem A/B Consistency Report

Date: 2026-04-24.

Owned file:

- `notes/universal_anomaly_platonic_swarm_20260424/P13_vol1_theoremAB_consistency.md`

Read-only surfaces:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
- `standalones/universal_anomaly_voa_explicit_supplement.tex`
- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `metadata/claims.jsonl`
- Vol I theory files named below.

No target TeX file was edited.

## Claim Attacked

The rectified standalone tries to make the Atiyah--Connes class
\[
  \alpha_X=[m_3,B^{(2)}]_X\in H^2(X,\Omega_X^1)
\]
the bridge from a Calabi--Yau threefold to Volume I Theorem B on the
reference curve. The attack surface is whether this can cite Vol I as
proved, especially Theorem A/B, the ordered bar complex
\[
  B_X^{\mathrm{ord}}(A)=T^c(s^{-1}\bar A),
\]
the Arnold relation, the ordered/modular convolution dGLA, and the
concordance/registry status surface.

## Verdict

The standalone can be made consistent with Vol I, but only after a
strict separation.

The Vol I proved input is:

1. symmetric chiral bar--cobar reconstruction on a smooth curve;
2. strict bar--cobar inversion on the Koszul locus;
3. coderived/completed Positselski comparison under the completed
   pro-conilpotent finite-piece hypotheses;
4. Arnold-relation control of the bar differential and low-degree
   ordered MC identities;
5. finite-degree ordered bar computations in the strongly admissible
   standard landscape.

The standalone's new bridge is not proved by Vol I. It must be stated
as a new comparison theorem or as a conditional hypothesis:
\[
  \operatorname{sp}_{\Sigma,C}(\alpha_X)
  =
  o^{(0)}_3(A_C)
  \in
  H^2\!\left(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\right).
\]
Here
\[
  A_C :=
  \Sp^{\mathrm{ch}}_{\Sigma,C}
  \Phi^{\mathrm{FA}}_3(D^b_{\mathrm{dg}}(X)).
\]
This only kills the first genus-zero bar--cobar obstruction. Full
Theorem B follows only after an independent Koszul/PBW input, a
completed Positselski input, or a separate all-higher closure theorem.

## Exact Vol I Status Map

### Safe proved imports

These may be cited as proved elsewhere relative to the standalone,
provided the hypotheses are copied exactly.

- Symmetric chiral bar--cobar reconstruction:
  `chapters/theory/bar_cobar_adjunction_inversion.tex:1644`,
  `:1654`. The theorem is `thm:bar-cobar-platonic`,
  `\ClaimStatusProvedHere`. It is on a smooth projective curve and uses
  the factorisation bar/cobar adjunction.

- Theorem A properad-level surface:
  `metadata/claims.jsonl` records `thm:A-infinity-2` as
  `ProvedHere` and `cor:classical-A-from-A-infinity-2` as
  `ProvedHere`. The larger `thm:koszul-reflection` package is
  `Conditional`; do not cite the whole package as unconditional.

- Arnold relations:
  `metadata/theorem_registry.md` records `thm:arnold-three`
  `ProvedHere`, `thm:arnold-relations` `ProvedHere`,
  `thm:arnold-jacobi` `ProvedElsewhere`, and
  `thm:arnold-general-n` `ProvedElsewhere`.
  The local bar-construction synthesis says the Arnold relation
  enforces \(d_0^2=0\) at genus zero:
  `chapters/theory/bar_construction.tex:2682`.

- Ordered bar as primitive object and its coinvariant shadow:
  `chapters/theory/bar_construction.tex:125` defines the symmetric bar
  as the \(\Sigma_n\)-coinvariant quotient of the ordered bar.
  `chapters/theory/ordered_associative_chiral_kd.tex:43`,
  `:101`, `:107` distinguish the ordered, symmetric, and
  Francis--Gaitsgory bars.

- Finite-degree \(E_1\) MC identities:
  `chapters/theory/e1_modular_koszul.tex:2340` records
  `thm:e1-mc-finite-degree` as `ProvedHere`.

- Curve-side cyclic deformation ambient:
  `chapters/theory/chiral_hochschild_koszul.tex:3191`,
  `:3530`, `:3642` define the cyclic deformation complex,
  its genus truncation, and the modular cyclic MC ambient.

### Conditional imports

These must remain conditional in the standalone.

- Full ordered \(E_1\) MC element:
  `chapters/theory/e1_modular_koszul.tex:347`,
  `metadata/claims.jsonl` label `thm:e1-mc-element`,
  status `Conditional`.

- Ordered all-genus Theorem A/B:
  `chapters/theory/e1_modular_koszul.tex:2898` and `:2955`,
  labels `thm:e1-theorem-A-modular` and `thm:e1-theorem-B-modular`,
  both `Conditional`.

- Ordered-to-symmetric functoriality and coinvariant shadow:
  `metadata/claims.jsonl` records `thm:av-functoriality` and
  `thm:e1-coinvariant-shadow` as `Conditional`.

- Theorem B as a full package:
  concordance states it as proved at the programme level only with
  exact lanes and hypotheses:
  `chapters/connections/concordance.tex:41--72`.
  The extracted registry records `thm:bar-cobar-inversion-qi` as
  `Conditional` because the theorem includes the off-locus and
  higher-genus conditional clauses. Therefore a standalone citation may
  use the strict Koszul clause or the completed coderived clause, not a
  blanket "Theorem B gives inversion for every admissible stage-two
  algebra."

- Chiral Positselski weight-completed comparison:
  `metadata/claims.jsonl` records `thm:chiral-positselski-weight-completed`
  as `Conditional`. It needs the strict completed surface,
  weight completion, Mittag--Leffler stability, and finite-piece
  hypotheses.

- K3/Humbert global Theorem B surfaces:
  `metadata/claims.jsonl` records `thm:tbsp-global-inversion-all-admissible`,
  `thm:tbsp-module-theorem-B-valpha1`, `thm:tbsp-theorem-B-adjoint`,
  and `thm:tbsp-theorem-B-Vbeta` as `Conditional`. Only the vacuum
  module is marked `ProvedHere`.

## Fatal Findings

### F1. The standalone cites Theorem B with the wrong native object

Anchor:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:290--307`

Current statement:

> The ordered chiral bar complex is \(T^c_C(s^{-1}\bar A)\), and
> Theorem B gives
> \(\Omega_C^{\mathrm{ch}}B_C^{\mathrm{ch}}(A)\simeq A\)
> in \(D^{\mathrm{co}}_{\mathrm{ch}}(C)\) for
> \(A\in\mathcal U^{\mathrm{adm}}(X)\subset\mathcal M_{\mathrm{cx}}(X)\).

This mixes three different Vol I surfaces.

1. Theorem A/B in the symmetric Vol I lane uses the factorisation bar
   \(\bar B_C(A)\) on unordered Ran, not the raw ordered tensor
   coalgebra, unless one first descends by \(R\)-twisted
   \(\Sigma_n\)-coinvariants.
2. The strict quasi-isomorphism is on the Koszul locus
   \(\operatorname{Kosz}(C)\) for the curve-side chiral algebra.
   A CY3 complex-structure locus
   \(\mathcal U^{\mathrm{adm}}(X)\subset\mathcal M_{\mathrm{cx}}(X)\)
   is not a Vol I object until the stage-two functor and derivative on
   deformation complexes are constructed.
3. The coderived statement is not equivalent to an ordinary
   quasi-isomorphism without a collapse hypothesis.

Repair: define \(A_C\), then say:

```tex
Assume \(A_C\) lies in \(\operatorname{Kosz}(C)\).  Then Vol. I
Theorem B gives the strict counit quasi-isomorphism
\[
  \Omega_C^{\mathrm{ch}}\bar B_C^{\mathrm{ch}}(A_C)\xrightarrow{\sim}A_C.
\]
Assume instead the completed pro-conilpotent finite-piece hypotheses
of Vol. I Theorem B.  Then the same counit is a coderived
equivalence.  Promotion to an ordinary quasi-isomorphism requires the
additional collapse hypothesis stated in Vol. I.
```

### F2. The reference-curve paragraph makes Theorem A equal to stage-two specialisation

Anchor:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:279--283`

Current statement:

> Theorem A's bar--cobar equivalence equals the \(E_1\)-chiral
> specialisation of \(\Phi_3(X)\) to \(C\).

Vol I does not prove this equality. Theorem A governs the bar/cobar
adjunction of a chiral algebra already living on a smooth curve. The
stage-two functor
\[
  \Sp^{\mathrm{ch}}_{\Sigma,C}
\]
belongs to the CY-to-chiral bridge, not to Vol I Theorem A itself.

Repair:

```tex
The stage-two functor produces a curve-side chiral algebra \(A_C\).
When \(A_C\) satisfies the hypotheses of Vol. I, Theorem A/B govern
the bar--cobar adjunction and counit of \(A_C\).  The identification
of the derivative of stage two with the Atiyah--Connes obstruction is
the new bridge hypothesis, not a theorem imported from Vol. I.
```

### F3. The ordered convolution dGLA sentence promotes a conditional \(E_1\) surface

Anchor:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:290--295`

The standalone says the ordered bar differential is governed by the
universal obstruction \(\Theta_A\) in the ordered convolution dGLA.

Vol I status is subtler:

- finite-degree \(E_1\) MC identities are proved
  (`thm:e1-mc-finite-degree`);
- the full ordered MC element is conditional
  (`thm:e1-mc-element`);
- the symmetric modular convolution dGLA has proved strict pieces, but
  the homotopy-invariant modular object is conditional in the registry.

Repair:

```tex
At finite genus-zero degree the ordered convolution identities are the
finite-degree Vol. I MC equations.  The full ordered all-genus MC
element and its averaging to the modular convolution object are used
only under the corresponding Vol. I conditional hypotheses.
```

### F4. The B1 bridge target is undefined and too large

Anchor:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:767--775`

Current target:
\[
  \mathrm{Ob}_{\mathrm{bar\text{-}cobar}}(A_X|_C).
\]

Vol I has no such named group. The nearest native target is the
genus-zero arity/weight-three part of the cyclic/modular deformation
complex of the curve-side algebra:
\[
  H^2\!\left(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\right).
\]

Repair:

```tex
\[
  \operatorname{sp}_{\Sigma,C}\colon
  H^2(X,\Omega_X^1)
  \longrightarrow
  H^2\!\left(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\right).
\]
Assume
\[
  \operatorname{sp}_{\Sigma,C}(\alpha_X)=o^{(0)}_3(A_C),
\]
where \(o^{(0)}_3(A_C)\) is the first genus-zero off-diagonal
bar--cobar obstruction.
```

This statement is new. It may be a theorem target, but Vol I does not
prove it.

### F5. Vanishing of the first obstruction is not Theorem B

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:772--775`
- `chapters/theory/bar_cobar_adjunction_inversion.tex:2336--2398`

Vol I explicitly separates first off-diagonal bar classes from full
Koszulness. A first obstruction \(o^{(0)}_3\) can vanish while a later
obstruction \(o^{(0)}_4\), \(o^{(0)}_5\), etc. survives. Therefore
\[
  \alpha_X=0
\]
can imply only
\[
  o^{(0)}_3(A_C)=0
\]
under B1. It cannot imply full Theorem B unless one adds:

- \(A_C\in\operatorname{Kosz}(C)\);
- or completed Positselski hypotheses plus the desired coderived
  conclusion;
- or an all-higher closure theorem
  \(o^{(0)}_{r+1}=F_r(o^{(0)}_3)\) with \(F_r(0)=0\).

### F6. The Arnold relation is being used beyond its Vol I theorem

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:685--710`
- `chapters/theory/bar_construction.tex:1425--1461`
- `chapters/theory/e1_modular_koszul.tex:2340--2365`

Vol I proves Arnold-relation control of:

- \(d_0^2=0\) for the genus-zero bar differential;
- Jacobi/CYBE at degree two;
- finite-degree ordered MC identities.

It does not prove that the weight-three Malcev cocycle of
\(\mathrm{Conf}_3(X)\) is equal to \(\alpha_X\), nor that
Malcev cohomology \(H^3_{\mathrm{Malcev}}\) is canonically
\(H^3_{\mathcal M}(X,\mathbb Q(2))\) in the standalone's convention.
That comparison is a frontier theorem. It should remain conditional or
conjectural and cannot support Theorem B.

## What The Standalone May Cite As Proved Elsewhere

Use the following exact clauses.

1. **Bar/cobar adjunction on a curve.**
   For a smooth projective curve \(C\), the symmetric factorisation
   bar and cobar form the Vol I adjunction. Cite
   `thm:bar-cobar-platonic`, `thm:A-infinity-2`, and
   `cor:classical-A-from-A-infinity-2`, with the caveat that
   `thm:koszul-reflection` as a package is conditional.

2. **Strict inversion on the Koszul locus.**
   If \(A_C\in\operatorname{Kosz}(C)\), then
   \[
     \Omega_C^{\mathrm{ch}}\bar B_C^{\mathrm{ch}}(A_C)\to A_C
   \]
   is a quasi-isomorphism. Cite the strict lane of
   `thm:bar-cobar-inversion-qi` and the concordance statement of
   Theorem B.

3. **Completed coderived inversion.**
   If \(A_C\) satisfies the completed pro-conilpotent finite-piece and
   Mittag--Leffler hypotheses, then the counit is a coderived
   equivalence. Cite `thm:chiral-positselski-weight-completed` only
   with its completion hypotheses.

4. **Arnold square-zero/Jacobi input.**
   The Arnold relation may be cited for \(d_{\bar B}^2=0\), for
   Jacobi/CYBE, and for finite-degree ordered MC identities. It may not
   be cited for the Atiyah--Connes/Malcev equality.

5. **Ordered bar definitions and low-degree standard examples.**
   The ordered bar \(T^c(s^{-1}\bar A)\), \(R\)-twisted descent, and
   standard landscape ordered-bar computations may be cited under the
   strongly admissible hypotheses. The all-genus ordered Theorem A/B
   surfaces remain conditional.

## What Must Stay Conditional

- Existence of the global comparison map
  \(d\Sp^{\mathrm{ch}}_{\Sigma,C}\) from the CY3 cyclic-HKR deformation
  complex to \(\Defcyc^{\mathrm{mod}}(A_C)\).
- Identification
  \(\operatorname{sp}_{\Sigma,C}(\alpha_X)=o^{(0)}_3(A_C)\).
- Any implication from \(\alpha_X=0\) to full Theorem B.
- Any equivalence between CY3 Hodge/coherent classes and curve-side
  bar-cobar obstruction classes.
- Any use of ordinary restriction
  \(H^2(X,\Omega_X^1)\to H^2(C,\Omega_C^1)\); the target is zero.
- All statements that the ordered all-genus \(E_1\) theorem package is
  already proved.
- The weight-three Malcev, graph, motivic, and Duflo faces as
  supports for the bridge.

## Correct B1 Theorem Wording

The following is the Vol I-compatible form.

```tex
\begin{theorem}[First bar--cobar obstruction comparison; conditional]
Fix a smooth projective Calabi--Yau threefold \(X\) with cyclic-HKR
datum \(\mathfrak c_X\), a two-stage specialisation datum
\((\Sigma,C)\), and let
\[
  A_C =
  \Sp^{\mathrm{ch}}_{\Sigma,C}
  \Phi^{\mathrm{FA}}_3(D^b_{\mathrm{dg}}(X)).
\]
Assume \(A_C\) is an augmented complete chiral algebra in the Vol. I
bar--cobar ambient.  Let
\[
  \Defcyc^{\mathrm{mod}}(A_C)
  =
  \operatorname{CoDer}^{\mathrm{cyc}}
  \bigl(\widehat{\bar B}^{\mathrm{ch}}_C(A_C)\bigr)[1]
\]
be the completed modular cyclic deformation complex and let
\(\pi_{3,0}\) denote the genus-zero arity-three projection.

Assume the derivative of stage-two specialisation is defined on the
Atiyah--Connes summand and gives
\[
  \operatorname{sp}_{\Sigma,C}\colon
  H^2(X,\Omega_X^1)\to
  H^2\!\left(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\right).
\]
If
\[
  \operatorname{sp}_{\Sigma,C}(\alpha_X)=o^{(0)}_3(A_C),
\]
then \(\alpha_X=0\) implies the vanishing of the first genus-zero
bar--cobar obstruction of \(A_C\).  If, in addition, \(A_C\) lies in
\(\operatorname{Kosz}(C)\), Vol. I Theorem B gives the strict
bar--cobar counit quasi-isomorphism.  If \(A_C\) satisfies the
completed Positselski hypotheses instead, Vol. I gives the corresponding
coderived equivalence.  No assertion about higher obstructions follows
without an independent closure theorem.
\end{theorem}
```

This is the theorem the paper yearns for. Proving it would be a new
result: it would identify a CY3 cyclic-HKR obstruction with the first
curve-side chiral bar--cobar obstruction.

## Required Edits For Integration

These are not made by P13, but they are necessary for Vol I
consistency.

1. Replace the standalone's `\cU^{\mathrm{adm}}(X)\subset\cM_{\mathrm{cx}}(X)`
   in the Theorem B paragraph by \(A_C\in\operatorname{Kosz}(C)\) or by
   the completed Positselski hypotheses.

2. Replace
   `\mathrm{Ob}_{\mathrm{bar\text{-}cobar}}(A_X|_C)` by
   \(H^2(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C))\).

3. Change every "Theorem A equals stage-two specialisation" sentence to
   "Theorem A/B govern the curve-side chiral algebra produced by
   stage two when its hypotheses hold."

4. Declare the ordered all-genus \(E_1\) MC and ordered Theorem A/B
   surfaces conditional, except for finite-degree MC identities and
   standard-landscape ordered-bar computations.

5. Move the Malcev/Arnold weight-three equality out of the proof path.
   It is a conditional frontier realisation of \(\alpha_X\), not a Vol I
   theorem.

6. Use \(\bar B_C^{\mathrm{ch}}\) for Theorem A/B. Use
   \(B_C^{\mathrm{ord}}\) only in the ordered lane, followed by
   \(R\)-twisted \(\Sigma_n\)-coinvariant descent when invoking the
   symmetric Vol I theorem.

## Commands Run

No build was run.

Representative commands:

```bash
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md
sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md
sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md
sed -n '1,260p' metadata/theorem_registry.md
sed -n '1,260p' chapters/connections/concordance.tex
sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md
rg -n -F 'Theorem A' chapters standalones metadata
rg -n -F 'Theorem B' chapters standalones metadata
rg -n -F 'ordered bar' chapters standalones metadata
rg -n -F 'Arnold' chapters standalones metadata
rg -n -F 'convolution' chapters/theory chapters/connections standalones metadata
rg -n -F 'alpha_X' standalones notes/universal_anomaly_platonic_swarm_20260424
sed -n '120,180p' chapters/theory/bar_construction.tex
sed -n '2680,2735p' chapters/theory/bar_construction.tex
sed -n '40,150p' chapters/theory/ordered_associative_chiral_kd.tex
sed -n '330,375p' chapters/theory/e1_modular_koszul.tex
sed -n '2328,2365p' chapters/theory/e1_modular_koszul.tex
sed -n '2890,2985p' chapters/theory/e1_modular_koszul.tex
sed -n '1638,1695p' chapters/theory/bar_cobar_adjunction_inversion.tex
sed -n '1990,2115p' chapters/theory/bar_cobar_adjunction_inversion.tex
sed -n '2328,2405p' chapters/theory/bar_cobar_adjunction_inversion.tex
sed -n '3190,3215p' chapters/theory/chiral_hochschild_koszul.tex
sed -n '3530,3585p' chapters/theory/chiral_hochschild_koszul.tex
sed -n '3640,3735p' chapters/theory/chiral_hochschild_koszul.tex
```

## Files Changed

- Created
  `notes/universal_anomaly_platonic_swarm_20260424/P13_vol1_theoremAB_consistency.md`.

No target TeX file, metadata file, or cross-volume file was edited.
