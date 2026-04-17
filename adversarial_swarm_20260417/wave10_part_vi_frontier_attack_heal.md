# Wave 10 — Vol I Part VI (Outlook / Open Frontiers) attack & heal

Target: `chapters/connections/outlook.tex` (690 lines, authoritative Vol I
Part VI inventory of frontier status). Companion frontier-topic chapters
`frontier_modular_holography_platonic.tex` (5460 lines) and
`subregular_hook_frontier.tex` (1751 lines) are explicitly OUT OF SCOPE for
this wave — they are topic chapters, not frontier-register chapters. The
frontier register lives in `outlook.tex` §"Open frontiers" (lines 255–290)
and in the five-theorem summary table (lines 16–64). The canonical
bookkeeping document is `FRONTIER.md` (§§1–3, 2026-04-17 Beilinson
rectification).

The role of this wave is to synchronise the typeset Part VI register with
FRONTIER.md §§1–3 after the 2026-04-16/17 closure wave, surface one
overclaimed closure that survived into the typeset prose, and add honest
cross-volume cross-refs.

## Attack findings

1. **Theorem-D row overclaims (table, lines 49–56)**. The row states
 "$\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$ for uniform-weight algebras at
 all genera" unconditionally. Per FRONTIER.md CL2 (2026-04-17
 downgrade), the modular-family extension of Theorem A over
 $\overline{\mathcal M}_{g,n}$ is CONDITIONAL on Francis–Gaitsgory
 six-functor base-change for the relative Ran prestack. Theorem D's
 all-genera universality propagates through the clutching-uniqueness
 proposition, which itself sits over the modular-family A. Theorem D
 at $g\geq 2$ also rests on the Faber $\lambda_g$-conjecture as a
 primary-source citation for the socle-evaluation step (AP225 residue).
 The honest status is: genus-$1$ unconditional; $g\geq 2$ conditional on
 (a) Francis–Gaitsgory base change, (b) Faber $\lambda_g$-conjecture.

2. **"Class~M chain-level false" is stale (line 269)**. FRONTIER.md §3
 "CLOSED DURING AUDIT (former OF1)" records that chain-level class M is
 PROVED on the original complex via `thm:mc5-class-m-chain-level-pro-ambient`
 + `thm:mc5-class-m-topological-chain-level-j-adic` on three equivalent
 ambients (pro-object, J-adic topological, filtered-completed). The
 direct-sum "genuine falsity" is an ambient-choice artefact scoped to
 bounded $\mathrm{Ch}(\mathrm{Vect})$, NOT the ambient of the raw bar
 complex with its weight topology. The typeset line is misleading.

3. **MC3 "resolved for all simple types" overclaims (line 265–267)**.
 FRONTIER.md CL10: "Extension to full $\mathrm{DK}_g$ unconditional in
 type A modulo `conj:dk-compacts-completion`; CONJECTURAL elsewhere.
 Silent non-coverage: logarithmic W, N=2 SCA, cosets, non-rational
 lattice, roots of unity." Also OF8: non-principal W beyond hook-type
 is GENUINELY OPEN (Wave-2 adversarial attack failed). The "all simple
 types via multiplicity-free $\ell$-weights and categorical closure"
 phrasing reads as full closure; it needs the DK-compacts qualifier and
 a pointer to hook-type only for non-principal.

4. **"Open frontiers" §enumerates 3 items, FRONTIER.md tracks 25**.
 Lines 272–290 list only (1) non-principal W duality, (2)
 factorization-envelope technology, (3) analytic sewing, (4)
 holographic modular Koszul datum. Missing high-priority genuine open
 items per FRONTIER.md §3 (Wave-1-refined):
 - OF4–5 merged: Givental $R$-matrix extraction of $A_{\mathrm{cross}}$
 from $A_2$ Frobenius CohFT;
 - OF9 D-module purity converse for Virasoro / $\mathcal W$;
 - OF11 full chiral QG beyond formal disk (elliptic finite-$\hbar$;
 toroidal global; g=2 DDYBE);
 - OF13 the Grand Completion (modular-graph pronilpotent closure,
 cumulant recognition, jet principle);
 - OF14 analytic realization three-layer gap (partially covered as
 "analytic sewing" but the three layers — sewing envelope for
 interacting algebras, metric independence at chain level, downstream
 — are not individuated);
 - OF15 scalar saturation Layer 1 beyond algebraic families;
 - OF19 CY-A_3 chain-level explicit for non-formal CY_3 (Vol III
 cross-ref);
 - AP225 residue for $g\geq 3$ Faber $\lambda_g$-conjecture.

5. **Cross-volume bridges §is a 6-line stub (lines 622–629)**. It
 mentions Vol II only; no Vol III cross-ref; no pointer to Vol II Part
 VIII frontier or Vol III frontier register.

6. **No AP/HZ tokens, no AI slop, no em-dashes, no phantom-closed
 inventory overclaim beyond the three above**. The chapter is otherwise
 CG-compliant.

## Heal strategy (surgical, non-destructive)

Four edits:

- **(H1)** Theorem-D table row: add honest conditional qualifier for
 $g\geq 2$ pointing to FRONTIER.md CL2 + Faber $\lambda_g$-conjecture.
- **(H2)** "Open frontiers" opening paragraph (lines 259–270): correct
 the stale "class~M chain-level false" statement; pin the direct-sum
 scope.
- **(H3)** MC3 "all simple types" sentence (lines 265–267): add the
 `conj:dk-compacts-completion` qualifier + hook-type-only scope pointer
 for non-principal.
- **(H4)** Expand the enumerated "Active growth directions" list (lines
 272–290) to include the missing genuine open frontiers OF4–5, OF9,
 OF11, OF13, OF14 refinement, OF19 cross-volume, AP225 residue.
- **(H5)** Expand "Cross-volume bridges" §to point to Vol II Part VIII
 (3d holographic-topological frontier) and Vol III frontier register.

All edits preserve the CG rhetorical standard (no AI slop, no
em-dashes, no AP/HZ tokens, Russian-school compression, Beilinson
falsification framing — each new open item names a concrete
falsification test or a concrete proof inscription target rather than
vague "conjecture").

## Russian-school voice compliance

- Gelfand: open items framed as "what limits forward progress" — each
 residue carries a specific inscription target, not a vague hope.
- Beilinson: falsification tests where available (g=3 cross-channel
 numerical check, admissible $L_k(\mathfrak{sl}_3)$ already inscribed
 as falsification theorem, generic-$\Omega$ DDYBE tolerance ladder).
- Drinfeld: compression — each item one or two sentences, pointing to
 the FRONTIER.md identifier and the inscription target file path.

## Propagation

No AP5 propagation needed — `outlook.tex` is internal to Vol I and the
FRONTIER.md closures it synchronises with are already propagated. No
Vol II / Vol III edits.

## Build risk

Zero new macros, zero new labels beyond `\phantomsection` stubs already
present. All `\ref`s point to labels that already exist in the
manuscript. Build-safe.
