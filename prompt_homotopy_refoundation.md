# Homotopy Refoundation: From dg Lie Shadow to L∞ Master

Read and deeply absorb `raeeznotes75.md`, `CLAUDE.md`, and `chapters/connections/concordance.tex` before touching any file. Then execute the following systematic refoundation of both volumes.

## The Single Correction

Every convolution dg Lie algebra in the monograph is a strict model of an underlying L∞-algebra. Every modular bar complex is a strictification of a homotopy coalgebra. The monograph already proves this — thm:modular-quantum-linfty establishes the full quantum L∞ structure on g^mod_A; thm:km-strictification proves KM admits a strict MC element with no higher homotopy corrections; thm:cyclic-linf-graph gives the cyclic L∞ structure via the chiral graph complex; rem:full-homotopy-why explains why the full homotopy level matters. The machinery exists but is organized as supporting material behind the dg Lie definitions. The refoundation makes it the organizing principle.

This is a refoundation of PERSPECTIVE, not CONTENT. You are not adding new mathematics. You are promoting existing proved theorems to their rightful structural role and introducing a naming convention that makes the two levels visible throughout.

## The Two-Level Convention

Introduce and deploy everywhere:

| Symbol | Meaning |
|--------|---------|
| `\Convstr(C,P)` | `Hom_S(C,P)`, the strict pre-Lie/dg Lie model (existing) |
| `\Convinf(C,P)` | The homotopy-invariant L∞ deformation object, well-defined up to L∞-quasi-iso |
| `\Definfmod(\cA)` | Complete filtered cyclic/modular L∞-algebra controlling modular deformations |
| `g^mod_A` | = `\Convstr` applied to the modular operad and End_A (existing def:modular-convolution-dg-lie) |
| `Def^mod_cyc(A)` | = coderivation strict model of `\Definfmod(A)` (existing def:modular-cyclic-deformation-complex) |

The dg Lie algebra is the M-level shadow. The invariant object is L∞.

## Three New Theorem-Packages

Insert into `chapters/theory/higher_genus_modular_koszul.tex` immediately after rem:full-homotopy-why (around line 7000). These theorems CITE existing literature and REFERENCE existing theorems in the monograph — they are organizational, not original.

### Theorem (Operadic Homotopy Convolution)
**Label**: thm:operadic-homotopy-convolution
**Status**: ClaimStatusProvedElsewhere
**Statement**: For any cooperadic/operadic pair (C,P), there is a functorially defined complete filtered L∞-algebra Conv∞(C,P), well-defined up to L∞-quasi-isomorphism, whose MC elements are ∞-twisting morphisms. For strict C,P, the convolution dg Lie algebra Hom_S(C,P) is a strict model.
**Proof sketch**: Cite Loday-Vallette [LV12, Thm 10.3.8] for the operadic L∞ structure via homotopy transfer through the Hom functor, van der Laan [vdL03] for the explicit transferred brackets, and note that the strict dg Lie algebra is the truncation ℓ_1 = D, ℓ_2 = [-,-], ℓ_n = 0 for n ≥ 3.

### Theorem (Modular Homotopy Convolution)
**Label**: thm:modular-homotopy-convolution
**Status**: ClaimStatusProvedHere
**Statement**: For any modular bar datum A, there is a complete filtered cyclic/modular L∞-algebra Def∞^mod(A) controlling modular deformations; the coderivation dg Lie algebra of a chosen completed modular bar model is a strictification. Θ_A is its canonical MC element. The full L∞-MC equation recovers the quantum master equation (eq:quantum-linfty-mc).
**Proof**: This synthesizes thm:modular-quantum-linfty (which already constructs the operations {ℓ_n^(g)}) with the two-level convention. The complete filtered L∞-algebra is the quantum L∞-algebra of thm:modular-quantum-linfty; the dg Lie algebra g^mod_A of def:modular-convolution-dg-lie is the strict model obtained by retaining only ℓ_1^(0) = D and ℓ_2^(0) = [-,-].

### Corollary (Strictification Comparison)
**Label**: cor:strictification-comparison
**Status**: ClaimStatusProvedHere
**Statement**: All dg Lie algebras in this monograph are functorial strict models of the corresponding homotopy-invariant L∞-algebras, and all bar-complex constructions are computations in a chosen strictification. In particular:
- (i) g^mod_A = Convstr of the modular operad and End_A is a strict model of Def∞^mod(A).
- (ii) Def^mod_cyc(A) is a strict model via the coderivation identification.
- (iii) For affine KM algebras at non-critical level, the L∞-algebra is strictly formal: no higher homotopy corrections at any genus (thm:km-strictification). This is the archetype of strictification.
- (iv) The choice of strict model amounts to a choice of contracting homotopy; different choices yield L∞-quasi-isomorphic deformation objects.

## Phase 1: Macros and Infrastructure

In `main.tex` preamble, add (check for conflicts first — grep for existing \Conv, \Def macros):
```latex
% Two-level homotopy convention (§\ref{subsec:two-level-convention})
\newcommand{\Convstr}{\operatorname{Conv}_{\mathrm{str}}}
\newcommand{\Convinf}{\operatorname{Conv}_{\infty}}
\newcommand{\Definfmod}{\operatorname{Def}_{\infty}^{\mathrm{mod}}}
```

**Verify**: `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast`

## Phase 2: Core Theorems in higher_genus_modular_koszul.tex

Read the file. Then:

1. After rem:full-homotopy-why (~line 7000), insert a new subsection:
```latex
\subsection{The two-level convention: strict models and homotopy-invariant objects}
\label{subsec:two-level-convention}
```
containing:
- A brief remark (rem:two-level-convention) introducing Convstr/Conv∞/Def∞^mod notation with one-paragraph motivation. The motivation is: the dg Lie algebra suffices for MC elements and the extension tower, but the L∞-algebra is the invariant object that persists under quasi-isomorphic replacements, homotopy transfer, and different choices of contracting homotopy.
- The three theorem-packages above.

2. In rem:unifying-principle (~line 7002), add one sentence after item (1): "More precisely, Def∞^mod(A) is the homotopy-invariant home (Theorem~\ref{thm:modular-homotopy-convolution}); the dg Lie algebra g^mod_A is its strict model (Corollary~\ref{cor:strictification-comparison})."

3. After def:modular-convolution-dg-lie (~line 6874), add:
```latex
\begin{remark}[Homotopy level]\label{rem:homotopy-level-convolution}
The dg~Lie algebra $\mathfrak{g}_\cA^{\mathrm{mod}}$ is a strict model
of the quantum $L_\infty$-algebra
$\Convinf(\{\overline{\mathcal{M}}_{g,n}\}, \operatorname{End}_\cA)$
\textup{(}Theorem~\textup{\ref{thm:modular-quantum-linfty})}: the
operations $\ell_1^{(0)} = D$, $\ell_2^{(0)} = [-,-]$ are the
dg~Lie structure; the higher brackets $\ell_n^{(g)}$ are explicit
homotopy-transferred Feynman amplitudes from the modular operad.
The strict model suffices for all Maurer--Cartan computations in
this monograph
\textup{(}Remark~\textup{\ref{rem:full-homotopy-why})}.
The homotopy-invariant object $\Definfmod(\cA)$ is needed when passing to
quasi-isomorphic replacements, minimal models, or different choices
of contracting homotopy
\textup{(}Theorem~\textup{\ref{thm:modular-homotopy-convolution})}.
\end{remark}
```

**Verify**: build.

## Phase 3: Core Definition Upgrade in chiral_hochschild_koszul.tex

Read the file. Then:

1. After def:modular-cyclic-deformation-complex (~line 1162), add a remark:
```latex
\begin{remark}[Strictification of the modular deformation object]
\label{rem:modular-cyc-strictification}
The modular cyclic deformation complex $\Defcyc^{\mathrm{mod}}(\cA)$
is the strict model of the homotopy-invariant modular deformation
object $\Definfmod(\cA)$
\textup{(}Theorem~\textup{\ref{thm:modular-homotopy-convolution})}.
The cyclic coderivation description is one model, obtained from the
cofree resolution of~$\barB(\cA)$; a different choice of
contracting homotopy produces an $L_\infty$-quasi-isomorphic
deformation complex.  For affine Kac--Moody algebras, the
strict model is already formal: the universal class
$\Theta^{\mathrm{str}}_{\widehat{\fg}_k}$ satisfies the strict
MC equation with all higher $L_\infty$-brackets vanishing
\textup{(}Theorem~\textup{\ref{thm:km-strictification})}.
\end{remark}
```

2. In rem:chriss-ginzburg-modular-cyc (~line 1191), after "satisfying $d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$", add: "This is the strict shadow of the full $L_\infty$-MC equation (Theorem~\ref{thm:modular-homotopy-convolution})."

**Verify**: build.

## Phase 4: Theory Chapter Reframing (Vol I)

For each file below, READ FIRST, then apply ONE targeted edit. Each edit is a remark or a sentence insertion — never a proof rewrite.

### algebraic_foundations.tex
Find the passage that calls the convolution dg Lie algebra "the single algebraic structure underlying bar-cobar duality, Koszul resolutions, and the modular genus tower" (or similar). Add after it: "More precisely, the convolution dg~Lie algebra is a strict model $\Convstr(C,P)$ of the homotopy-invariant $L_\infty$-algebra $\Convinf(C,P)$ (Theorem~\ref{thm:operadic-homotopy-convolution}); the strict model suffices for all explicit computations in this monograph."

### bar_cobar_adjunction_curved.tex
After thm:bar-modular-operad (bar complex as FCom-algebra), add a one-sentence remark: "The FCom-algebra structure is the strict incarnation of the homotopy modular coalgebra on $\barB(\cA)$; the Feynman transform provides the homotopy-invariant formulation (Getzler--Kapranov~\cite[\S5]{GeK98})."

### bar_cobar_adjunction_inversion.tex
At the bar-cobar inversion theorem, add a remark noting that $\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ lifts to an L∞-quasi-isomorphism at the homotopy level, by functoriality of bar-cobar through the L∞-convolution (Theorem~\ref{thm:operadic-homotopy-convolution}).

### higher_genus_complementarity.tex
Where genus-g bar complexes become dg Lie algebras L_g, add a remark that these are genus-truncations (via the complete filtration of Proposition~\ref{prop:modular-deformation-truncation}) of the modular L∞-deformation object Def∞^mod(A).

### higher_genus_foundations.tex
Where the genus tower is first constructed, add a remark framing the tower as the filtration of Def∞^mod(A) by genus, with each stratum gr_g computing deformations at fixed genus.

### quantum_corrections.tex
Where def:tree-level-linfty and def:genus-refined-linfty are defined, add a remark connecting these to the two-level convention: the tree-level L∞ is Conv∞ at genus 0; the genus-refined L∞ is the genus-truncation of Def∞^mod(A).

**Verify**: build after each file.

## Phase 5: Vol II Integration

For each file in `~/chiral-bar-cobar-vol2/chapters/connections/`:

### modular_pva_quantization.tex
This file is the closest to the corrected viewpoint. At the definition of L_mod(C) := Coder(B_mod(C))[-1] (~line 432), add a remark identifying this as the strict model of Def∞^mod, and noting that this chapter's filtered obstruction theory (thm:Ob1, thm:Obg) operates at the strict level because the complete filtration ensures convergence.

### bar-cobar-review.tex
At the convolution dg Lie algebra passage (~line 163-200), add a brief remark noting this is Conv_str in the two-level convention. At the cofree-coderivation principle (~line 649), note that this principle is what makes the strict model computable: it reduces the L∞-deformation theory to coderivations on a cofree coalgebra.

### line-operators.tex
After thm:homotopy-Koszul (the Swiss-cheese homotopy-Koszul theorem), add a remark connecting it to the two-level convention: homotopy-Koszulity is exactly the statement that the bar-cobar adjunction at the L∞ level (Conv∞) is an equivalence, not merely a quasi-isomorphism at the strict level.

After the dg-shifted Yangian introduction, add a sentence noting it is a strict model of a homotopy-coherent meromorphic tensor structure, recoverable from the modular spectral kernel via strictification.

### hochschild.tex
Where Tamarkin's deformation formulation appears (~line 131-160), note the strict/homotopy levels: Tamarkin's *-Lie algebra is the strict model; the homotopy-invariant object is the (d+1)-algebra from Tamarkin's higher structure theorem.

### brace.tex
Where the homotopy Gerstenhaber algebra structure appears, add a brief sentence connecting the brace L∞-structure to Conv∞: the brace operations are the explicit transferred L∞-brackets from the operadic cochain complex.

**Verify**: `cd ~/chiral-bar-cobar-vol2 && make`

## Phase 6: Example Chapter Anchors (Vol I)

For each of these chapters, add ONE remark near the chapter opening that establishes the four-pass pattern. Keep it to 10-15 lines. The pattern is:

> In this chapter, [FAMILY] illustrates the four-level structure of the modular engine:
> (i) the geometric/physical object [SPECIFIC],
> (ii) the strict algebraic model [SPECIFIC],
> (iii) the homotopy-invariant deformation object $\Definfmod$ [SPECIFIC FEATURE],
> (iv) the modular completion with genus tower and shadow calculus [SPECIFIC RESULT].

Apply to:

- **heisenberg_eisenstein.tex**: (i) free boson on curve, (ii) Heisenberg Lie algebra with bar complex, (iii) strictification is trivially formal (ℓ_n = 0 for n ≥ 3), (iv) Gaussian shadow archetype, shadow tower terminates at r=2.

- **kac_moody.tex**: (i) WZW model / affine current algebra, (ii) CE complex and bar resolution, (iii) strictly formal by thm:km-strictification (the archetype), (iv) genus tower with κ = k+h∨, Lie/tree shadow archetype, terminates at r=3.

- **beta_gamma.tex**: (i) βγ system / symplectic bosons, (ii) bar complex with quartic contacts, (iii) non-trivial L∞ — higher brackets detect the quartic resonance, (iv) contact/quartic shadow archetype, μ_{βγ}=0, terminates at r=4.

- **w_algebras.tex**: (i) DS reduction of WZW, (ii) BRST complex and W-algebra OPE, (iii) L∞ non-trivial at all arities (quintic forced: o^(5)_Vir ≠ 0 → infinite tower), (iv) mixed cubic-quartic shadow archetype, Q^contact_Vir = 10/[c(5c+22)].

- **yangians_foundations.tex**: (i) rational R-matrix / meromorphic braiding, (ii) RTT presentation and evaluation, (iii) Conv∞ for E1-chiral (non-commutative convolution), (iv) modular Yangian Y^mod_T as pro-MC in pronilpotent completion.

- **lattice_foundations.tex**: (i) lattice VOA from even lattice, (ii) bar complex with cocycle twist, (iii) strictification formal (curvature-braiding orthogonal by thm:lattice:curvature-braiding-orthogonal), (iv) κ = rank(Λ) independent of cocycle.

**Verify**: build.

## Phase 7: Constitution Update

In `concordance.tex`:

1. In rem:constitutional, after "The single-equation principle" paragraph and before "The current status has two strata", insert:

```latex
\emph{The two-level convention.}
Every convolution dg~Lie algebra in this monograph is a strict
model of a homotopy-invariant $L_\infty$-algebra
\textup{(}Theorem~\textup{\ref{thm:operadic-homotopy-convolution}},
Theorem~\textup{\ref{thm:modular-homotopy-convolution})}.
The dg~Lie algebra suffices for Maurer--Cartan elements and the
extension tower; the $L_\infty$-algebra is the invariant object
that persists under quasi-isomorphic replacements and homotopy
transfer.
```

2. In rem:concordance-synthesis, add after the current last sentence: "At the homotopy level, $\Convinf$ unifies all these frameworks: each named framework is a strictification or truncation of the modular $L_\infty$-deformation object $\Definfmod(\cA)$."

**Verify**: build both volumes. Run `make test` on Vol I.

## HARD CONSTRAINTS — VIOLATING ANY OF THESE IS A FAILURE

1. **No formula invention.** Every formula you write must come from an existing theorem in the monograph or a cited reference. If you are unsure whether a formula is correct, do not write it — add a \textup{(}TODO\textup{)} instead.

2. **No proof rewrites.** Every existing proof stays exactly as is. You add remarks AFTER proofs, not inside them.

3. **No ClaimStatus downgrades.** Nothing that is ProvedHere becomes Conjectured.

4. **No \newcommand in chapter files.** Macros only in main.tex preamble.

5. **No new .tex files.** Everything goes into existing files.

6. **Build after every phase.** If it breaks, fix before proceeding.

7. **Read before edit.** Read every file before modifying it. Understand what's there.

8. **Keep each edit ≤ 25 lines of new LaTeX.** This is surgical context-setting, not a rewrite.

9. **Git attribution: Raeez Lorgat only.** No AI attribution anywhere. No co-authored-by.

10. **Respect existing architecture.** The five main theorems, the Chriss-Ginzburg principle, the master object Θ_A, the shadow algebra — all stay exactly as defined. You are adding a LENS (the two-level convention) through which to view them, not changing what they are.

## What "Deeply Fused" Means Operationally

Not: a remark bolted onto each definition saying "this is a strict model."
But: the OPENING SENTENCE of each key section naturally sets up the two levels, so the strict definition arrives already contextualized. The reader never encounters a dg Lie algebra without knowing it is one model of something invariant. The L∞-algebra is not an afterthought — it is the natural context in which the strict model is the computationally convenient choice.

This is achieved by:
- Editing section-opening paragraphs to mention both levels
- Adding remarks that SHOW the homotopy structure (explicit operations, explicit sources) rather than declaring it abstractly
- Using the new macros consistently so the notation itself carries the message
- Connecting every local edit to the global three-theorem framework

The Chriss-Ginzburg aesthetic: each concept is animated by its geometric incarnation, then algebraized into a strict model, then freed to its homotopy-invariant form, then completed modularly. The reader sees the concept LIVE before seeing its abstract home.
