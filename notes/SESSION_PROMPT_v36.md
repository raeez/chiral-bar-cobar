# SESSION PROMPT v36 — The Reforging
# For: Claude Opus 4.6 (1M context) in Claude Code, extra high reasoning mode
# Date: 2026-03-14
# Companion file: notes/REFORGE_MANIFEST.md (387 concrete findings, every file)
# Build: 1781pp, 0 undef, 0 overfull, 6005 tests pass

---

## 0. WHO YOU ARE

You are rewriting the prose of a 1,781-page research monograph. Not auditing — rewriting. Not planning — executing. The mathematical skeleton is sound: 1,595 tagged claims, five main theorems proved, control plane clean. What remains is that too much of the text *tells* the reader what the mathematics does instead of *showing* it. Your job is to make the text show.

The target is Chriss--Ginzburg *Representation Theory and Complex Geometry*: a book where the Springer resolution appears on page 3, the reader computes a Borel--Moore homology group on page 7, and the equivariant K-theory localization theorem arrives with a worked example of the flag variety before the general statement is even formulated. That book never explains what it is about to do. It does the thing and lets the mathematics speak.

This monograph lives at the intersection of homotopical algebra (Loday--Vallette), algebraic geometry on curves (Beilinson--Drinfeld), and vertex algebra theory (Frenkel--Ben-Zvi). Its core revelation is that the logarithmic kernel $\eta_{ij} = d\log(z_i - z_j)$ on Fulton--MacPherson configuration spaces turns the OPE of a chiral algebra into a factorization coalgebra whose differential is nilpotent at genus 0 and curved at genus $g \geq 1$, with the curvature controlled by a single scalar $\kappa(\cA)$ whose generating function is $\hat{A}(ix) - 1$. That sentence contains more mathematics than most of the passages you will cut.

**Do not assume the mathematics is correct.** Treat every claim as an expression reaching toward what it aspires to be. A `\ClaimStatusProvedHere` is an aspiration to theoremhood; a proof is an aspiration to truth. Read skeptically but edit charitably: if a proof aspires and mostly succeeds, sharpen it; if it fails, mark it for the author's attention but do not fabricate mathematics.

---

## 1. THE DISEASE AND ITS CURE

The manuscript has one disease with six symptoms. The disease is **telling instead of showing**.

### Symptom 1: Throat-clearing
*"In this chapter we construct the bar complex step by step, showing how it emerges from the configuration space geometry."*

**Cure**: Delete the sentence. Begin with the bar complex.

### Symptom 2: Echo
A theorem followed by a remark restating the theorem in different words.

**Cure**: Delete the remark. The theorem spoke.

### Symptom 3: Scope bloat
A 25-line remark after a conjecture explaining which master conjecture it contributes to, what homotopy template it instantiates, and which future programme it serves.

**Cure**: One parenthetical — "(contributing to MC3)" — or nothing.

### Symptom 4: Physics prose in proof bodies
*"In the path integral picture, the anomaly arises from the regularization of the functional determinant..."* — inside a `\begin{proof}`.

**Cure**: Move to a remark. Proofs are mathematics.

### Symptom 5: Premature abstraction
A 200-line general framework followed by "we now specialize to the Heisenberg algebra."

**Cure**: Begin with Heisenberg. State the general definition after the reader has seen what it generalizes.

### Symptom 6: Mechanical reduction chains
Fifteen consecutive propositions each removing one entry from a packet, with proofs consisting of "by the preceding proposition."

**Cure**: State the final result. Give the proof. The intermediate steps are not mathematics — they are bookkeeping. If the bookkeeping matters (e.g., for computational verification), move it to an appendix or a computational remark.

---

## 2. THE THREE RULES

Every edit must satisfy at least one:

1. **Fewer words, same mathematics.** A 10-line paragraph becomes 3 lines. A 25-line scope remark becomes 1 line.
2. **More mathematics, same words.** A vague sentence ("the bar complex captures the essential data") becomes a precise one ("$\barB^n(\cA) = \Gamma(\overline{C}_{n+1}(X), \cA^{\boxtimes(n+1)} \otimes \Omega^n_{\log})$").
3. **Show replaces tell.** An explanation of what a construction does is replaced by the construction itself. A summary of what a chapter proves is replaced by the statement of the theorem.

If an edit satisfies none of these, do not make it.

---

## 3. WHAT NOT TO TOUCH

- **Theorem statements.** Do not change `\begin{theorem}...\end{theorem}` content.
- **Displayed mathematics.** Do not change anything inside `\[...\]`, `\begin{equation}`, `\begin{align}`, or inline `$...$` containing formulas.
- **Proof logic.** Do not change the mathematical argument of any proof. You may cut prose preamble within proofs ("We now verify the three conditions..."), but not the verification itself.
- **Labels, ClaimStatus tags, cross-references.** These are load-bearing infrastructure.
- **Section structure.** Do not move sections, reorder chapters, or rename sections.

You are recasting the prose *around* the mathematical skeleton. The skeleton is frozen.

---

## 4. EXECUTION

### Step 1: Read `notes/REFORGE_MANIFEST.md`

This file contains 387 concrete findings across every .tex file in the manuscript, organized by file with line ranges, categories, and prescribed actions (CUT / COMPRESS / SHARPEN). It is your marching orders.

### Step 2: Process files in manifest order

For each file in the manifest:

1. Read the file at the specified line ranges.
2. Execute the prescribed action for each finding:
   - **CUT**: Delete the passage entirely. Verify no `\ref{}` targets are lost.
   - **COMPRESS**: Rewrite to 30% of current length. Preserve mathematical content.
   - **SHARPEN**: Rewrite for precision. Replace vague language with exact mathematics.
3. After every 3 files, run `make fast` to verify the build.

### Step 3: The five systemic passes

After processing individual findings, make five monograph-wide passes:

**Pass A: Kill boilerplate remark pairs.** Every chapter and appendix opens with `\begin{remark}[Governing question]` + `\begin{remark}[H/M/S route]`. There are 57 such remarks across 29 files. Delete all of them. If a governing question contains genuine mathematical content (e.g., introduction.tex), compress it to the chapter's opening sentence without a remark wrapper.

**Pass B: Kill terminal echo paragraphs.** Many chapters end with a paragraph beginning "The computations of this chapter confirm..." or "The preceding analysis demonstrates...". Delete all of them. The chapter's theorems are its summary.

**Pass C: Compress scope remarks.** Every conjecture is followed by a scope remark. Compress each to at most 3 lines. The pattern "(Contributing to Conjecture~\ref{conj:master-dk-kl}.)" as a parenthetical within the conjecture statement itself replaces a 20-line remark.

**Pass D: Collapse mechanical reduction chains.** Two locations:
- `bar_cobar_construction.tex` lines 5300-15051: ~80 propositions mechanically decomposing W-infinity seed packets. Collapse to: one theorem (stage-4 packet), one theorem (stage-5 packet), one residual-frontier conjecture. Move the mechanical decomposition to a computational appendix or compress to a remark sketching the reduction.
- `yangians.tex` lines 8806-10000: ~15 propositions on DK-5 formal categorical extension. Collapse to: one formal extension lemma, one Yangian corollary, one spectral corollary.

**Pass E: Excise physics prose from proofs and reference appendices.**
- `bv_brst.tex`: move all "In the path integral picture..." and "Physically, this corresponds to..." out of `\begin{proof}` into adjacent remarks.
- `holomorphic_topological.tex`: cut physics vignettes with no computation (AGT analogies tables, D-brane speculation, tikzpicture Witten diagrams).
- `w_algebras_framework.tex`: cut or compress the "Holographic interpretation" subsection (lines 2097-2148) and the "Main theorems re-summary" (lines 2150-2214).
- `homotopy_transfer.tex`: cut the "Historical origins" section (lines 17-60) that cites string field theory and Fukaya categories without computing anything.

---

## 5. MATHEMATICAL INVARIANTS — SACRED

If a rewrite touches prose near any of these, verify correctness:

- Cohomological grading: $|d| = +1$, bar uses desuspension $s^{-1}$
- $\mathrm{Com}^! = \mathrm{Lie}$ (NOT coLie). Heisenberg NOT self-dual.
- Bar differential: $d_{\mathrm{bracket}}^2 \neq 0$; full $d^2 = 0$ via Borcherds.
- Sugawara: $c = k\dim\mathfrak{g}/(k + h^\vee)$, UNDEFINED at $k = -h^\vee$.
- FM compactification: blowup, NOT $X^n \setminus \Delta$.
- QME factor $\tfrac{1}{2}$. HCS coefficient $\tfrac{2}{3}$. $\Lambda = {:}TT{:} - \tfrac{3}{10}\partial^2 T$ (MINUS).

---

## 6. WHAT SUCCESS LOOKS LIKE

**Before (current manuscript, typical remark)**:
```latex
\begin{remark}[Scope]
This theorem is proved under the hypothesis that $\cA$ is Koszul.
The Koszul hypothesis is essential: without it, the spectral sequence
need not degenerate, and the bar-cobar adjunction need not be an
equivalence. For non-Koszul algebras, one must pass to the coderived
category (see \S X.Y). The theorem contributes to MC1 of the master
conjecture hierarchy.

\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~II
(equivalence of homotopy categories). At H-level: an equivalence of
$\Eone$-monoidal $\infty$-categories. The M-level model is the
braided monoidal bar-cobar dg category.
(Contributing to Conjecture~\ref{conj:master-dk-kl}.)
\end{remark}
```

**After (Chriss--Ginzburg)**:
```latex
% [Remark deleted. The Koszul hypothesis is in the theorem statement.
%  The coderived reference is in §X.Y. The MC1 parenthetical is metadata.]
```

**Before (current manuscript, chapter opening)**:
```latex
\begin{remark}[Governing question]
The governing question of this chapter is how the logarithmic kernel
on configuration spaces produces the bar transform, and why Verdier
duality gives the correct inverse on the Koszul locus.
\end{remark}

\begin{remark}[H/M/S route; Convention~\ref{conv:hms-levels}]
This chapter is primarily H/M-level. It builds the model-level bar
and cobar constructions explicitly and promotes inversion to H-level
only on the printed Koszul locus.
\end{remark}

The logarithmic 1-form $\eta_{ij} = d\log(z_i - z_j)$ of
\S\ref{sec:the-seed}, planted on a configuration space of $n$~points
and integrated against the OPE data of a chiral algebra, grows into
a functor: the bar construction.
```

**After (Chriss--Ginzburg)**:
```latex
The logarithmic 1-form $\eta_{ij} = d\log(z_i - z_j)$, integrated
against the OPE data of a chiral algebra on a configuration space
$\overline{C}_n(X)$, defines the bar construction.
```

Three paragraphs become one sentence. The mathematics is identical. The governing question and H/M/S route were telling; the logarithmic form is showing.

---

## 7. ANTI-FAILURE MODES

**F1: Over-cutting.** Before deleting a remark, check: does it contain a `\label{}` referenced elsewhere? Does it contain a mathematical fact (not a restatement) that would be lost? If yes, keep the fact, cut the framing.

**F2: Formula perturbation.** Do NOT touch displayed math. Do not "improve" notation. Do not reorder terms. The 1,595 cross-referenced claims form a fragile web; touching one formula risks breaking a reference chain.

**F3: Beautification without compression.** Swapping "we now construct" for "the following construction" is not a rewrite. Every edit must reduce word count or increase precision.

**F4: Structural rearrangement.** Do not move sections. Do not reorder definitions. If you believe a structural change is needed, record it in a note but do not execute.

**F5: Fabricating mathematics.** When compressing a passage, do not invent claims that the original text did not make. If the original says "one can show" and does not show, mark it for the author rather than filling in a proof you cannot verify.

---

## 8. ESTIMATED SCOPE

| Category | Finding count | Est. lines cut/compressed | Files touched |
|----------|--------------|--------------------------|---------------|
| Boilerplate remark pairs | 57 | ~170 | 29 |
| Echo remarks | ~100 | ~1500 | 20 |
| Scope bloat | ~40 | ~600 | 15 |
| Physics in proofs | ~20 | ~300 | 6 |
| Mechanical reduction chains | 2 mega-findings | ~9000 | 2 |
| Dead remarks | ~40 | ~400 | 15 |
| Table creep | ~10 | ~200 | 5 |
| Terminal echoes | ~15 | ~200 | 15 |
| **Total** | **~387** | **~12,000** | **~30** |

The manuscript should shrink from ~128K to ~116K lines — every line that remains doing serious work.

---

## 9. COMPLETION CRITERION

The session is complete when:

1. Every finding in `REFORGE_MANIFEST.md` has been executed or explicitly deferred with justification.
2. All five systemic passes (A--E) have been completed.
3. `make fast` builds cleanly.
4. The total line count has decreased by at least 5,000 lines.
5. A spot-check of 10 random chapter openings shows zero boilerplate remark pairs.
