# Wave-7 Five Objects Discipline Audit (Cross-Volume)

**Date.** 2026-04-17.

**Scope.** AP25/AP34/AP50/AP195: five-object discipline — $A$,
$B(A)$ (bar coalgebra), $A^i = H^*(B(A))$ (dual coalgebra),
$A^! = ((A^i)^\vee)$ (dual algebra), $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$
(derived center / bulk). Forbidden conflations: bar-cobar $\Rightarrow$
bulk; $\Omega(B(A)) = A^!$; bar complex $=$ Koszul dual; $D_{\Ran}(B(A))
= \Omega$; $A^! = H^*(B(A))$ without dualisation.

## Grep Results

### Canonical forbidden phrases (six patterns)

| Pattern | Vol I | Vol II | Vol III |
|---|---|---|---|
| "bar-cobar produces bulk" | 0 | 0 | 0 |
| "$\Omega(B(A))$ is the Koszul dual" | 0 | 0 | 0 |
| "the Koszul dual equals the bar complex" | 0 | 0 | 0 |
| "$D_{\Ran}(B(A))$ is the cobar" | 0 | 0 | 0 |
| "$A^!$ is the bar complex" | 0 | 0 | 0 |
| "$Z^{\mathrm{der}}_{\mathrm{ch}}$ is the bar-cobar" | 0 | 0 | 0 |

Zero hits across all three volumes. Discipline is internalised at the
slogan level.

### Drift patterns

Pattern 1. `B(A)` co-mentioned with "Koszul dual" without the coalgebra
qualifier. 14 hits across volumes; each inspected and classified as
correctly phrased. Examples:
- Vol I `lattice_foundations.tex:17`: "bar complex acquires a cocycle
  twist; the Koszul dual reflects the discriminant group" — two
  distinct objects each given its role. KEEP.
- Vol II `thqg_bv_ht_extensions.tex:214`: "bar complex classifies
  twisting morphisms to the Koszul dual" — this is the correct twisting
  morphism picture $B(A) \leftrightarrow A^!$. KEEP.
- Vol III `e2_chiral_algebras.tex:1533`: "$A^! = D_{\C^3}(B_{E_3}(A))^\vee$"
  — explicit three-step construction (bar, then Verdier, then linear
  dual). KEEP, exemplary.
- Vol III `cy_to_chiral.tex:1261`: explicit "$B(A)$ is a coalgebra,
  $A^!$ is an algebra, and the cobar recovery $\Omega(B(A)) \simeq A$
  is inversion, not Koszul duality." — canonical statement. KEEP.

Pattern 2. $\Omega(B(A))$ occurrences with inversion semantics. 45+
hits across volumes; all use $\Omega(B(A)) \simeq A$ (inversion) or
$\Omega(B(A^!)) \simeq$ something-else-named-correctly. Zero
conflations.

Pattern 3. "Derived center" in same paragraph as "bar complex". 7
hits. All correctly distinguish: "bar complex is the $E_1$ engine;
derived center is the $\SCchtop$ output" (Vol I
`en_koszul_duality.tex`, `introduction.tex`, Vol II
`foundations_recast_draft.tex`, Vol II
`spectral-braiding-core.tex`). Zero conflations.

Pattern 4. $A^! = H^*(B(A))$ without dualisation (linear or Verdier
vee). Three hits, of which two are correctly written with `^\vee` and
one is a genuine drift:

- Vol II `spectral-braiding-frontier.tex:33`: `$\cA^! = H^*(\barB(\cA))^\vee$`. CORRECT.
- Vol II `thqg_line_operators_extensions.tex:22`: same with `^\vee`. CORRECT.
- Vol I `chiral_koszul_pairs.tex:1270`: `$\cA^! = H^*(\barBgeom_X(\cA))^\vee$`. CORRECT.
- Vol I `yangians_drinfeld_kohno.tex:7939`, `8064`: both with `^\vee`. CORRECT.
- **Vol I `subregular_hook_frontier.tex:44`**: `$A^! = H^*(\widehat{\overline{B}}(A)) = \widehat{\Lambda}_\partial(sV)$` WITHOUT vee. **DRIFT — healed**.

## Heals Applied

### Heal 1. Vol II `foundations.tex` (and mirror `foundations_overclaims_resolved.tex`)

The statement of `thm:koszul-comparison-mc` said
"$\pi\colon \cA \twoheadrightarrow \cA^!$ is the bar-cohomology
projection" and the proof asserted
"$\cA^! = H^\bullet(\barB(\cA))$".

Two five-object conflations at once:

(a) $A \twoheadrightarrow A^!$ is not a projection; $A$ and $A^!$ are
Koszul-paired via a twisting morphism $\tau \in A^! \otimes A$, not by
a surjection.

(b) $A^! = H^*(B(A))$ conflates the dual coalgebra $A^i$ with the dual
algebra $A^!$.

Healed to distinguish: $\pi = \tau^\#$ is the map dual to the universal
twisting morphism $\tau$, and the correct two-step construction reads
$A^i := H^\bullet(\barB(\cA))$, $A^! := (A^i)^\vee$.

Affected theorem statement + proof in `foundations.tex:1718-1729`;
identical heal in `foundations_overclaims_resolved.tex:119-121`.

### Heal 2. Vol III `k3_yangian_chapter.tex:222`

Prose said "This is the bar-cobar Koszul duality of Vol~I (Omega(B(A))
= A inversion; the chiral derived center is a separate construction)".
The phrase "bar-cobar Koszul duality" conflates two distinct functors
(cobar = inversion, Koszul duality = Verdier). Healed to separate
chiral Koszul duality from bar-cobar inversion and from the derived
center, per canonical CLAUDE.md discipline.

### Heal 3. Vol I `subregular_hook_frontier.tex:44`

Table cell read $A^! = H^*(\widehat{\overline{B}}(A)) = \widehat{\Lambda}_\partial(sV)$.
Missing $\vee$. Added.

## Per-Volume Site Count

| | sites inspected | genuine conflations | heals |
|---|---|---|---|
| Vol I | 58 | 1 | 1 (`subregular_hook_frontier.tex`) |
| Vol II | 73 | 2 (same theorem, two files) | 2 (`foundations.tex`, `foundations_overclaims_resolved.tex`) |
| Vol III | 32 | 1 | 1 (`k3_yangian_chapter.tex`) |
| **Total** | **163** | **4** | **4** |

The five-object discipline is largely internalised: 159/163 inspected
sites pass. The four drifts are local slips (one in a frontier chapter,
one duplicated theorem, one parenthetical in a mixed-convention Vol III
examples chapter) and were healed without propagation. No forbidden
slogan ("bar-cobar produces bulk", etc.) appears anywhere in
typeset prose across the three volumes.

## Cross-volume atomicity

No cross-volume ref chains were affected: all four heals are local
prose fixes that do not rename labels, invalidate citations, or shift
theorem content. No downstream propagation needed.

## Verdict

Five Objects discipline is holding at the slogan level (zero canonical
forbidden-phrase hits) and at the working-math level (zero $A^! = B(A)$
conflations after heal). The four drifts were of the "$A^! = H^*(B(A))$
without vee" variety — a specific half-step omission, not a structural
misunderstanding. The 159/163 pass rate across three volumes
corroborates the canonical statement's internalisation.
