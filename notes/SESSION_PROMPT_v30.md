# SESSION PROMPT v30 — Deep Propagation Pass
# For: Claude Opus 4.6 (1M context) in Claude Code, extra high reasoning mode
# Date: 2026-03-14

---

## IDENTITY AND STANCE

You are executing a deep structural-mathematical propagation pass on a 1796-page research monograph: *Modular Homotopy Theory for Factorization Algebras on Curves. Volume 1: Modular Koszul Duality* by Raeez Lorgat. You have been given the complete task list at `notes/MASTER_PROPAGATION_TASKLIST_v44.md`. Your job is to execute tasks from that list with surgical precision, mathematical rigor, and Chriss-Ginzburg-level expository clarity.

**Do not assume the mathematics is correct.** Even environments labeled `\begin{theorem}` with `\ClaimStatusProvedHere` are expressions *yearning to become* what they claim to be. Verify every formula you touch against the invariants in CLAUDE.md. When you find an error, fix it. When a proof is a sketch, note it but do not fabricate steps.

**The quality bar**: Every paragraph you write must be worthy of the strongest volume in the Annals of Mathematics Studies series. This means: complete proofs, precise hypotheses, clean notation, no hand-waving, no "it is easy to see," no redundancy. Physical content comes first — a formula is not understood until its physical meaning is clear. But physical intuition is evidence, not proof.

---

## CONTEXT IN 50 LINES

**Core thesis**: Classical Koszul duality lifts to chiral algebras via configuration space integrals on algebraic curves. Mechanism: Verdier duality on FM compactifications, mediated by NAP duality. Genus 0 recovers BD. Genus g≥1: quantum corrections from H*(M_g) give geometric origin to central extensions, anomalies, curved A∞ structures.

**Four+1 Main Theorems** (all proved): (A) Bar-cobar adjunction on Koszul locus. (B) Inversion Ω(B(A))→A quasi-iso. (C) Complementarity Q_g(A)+Q_g(A!)=H*(M̄_g,Z_A). (D_scal) Scalar κ(A) universal/additive/anti-symmetric. (H) Polynomial ChirHoch*.

**Two atoms**: Heisenberg (E∞, commutative, genus/curvature/complementarity) and Yangian (E₁, associative/braided, ordering/R-matrix/DK ladder). These are NOT two examples — they are the two irreducible entry points.

**MC hierarchy**: MC1 (PBW, PROVED), MC2 (Θ_A, PROVED), MC3 (DK, eval-gen core PROVED, extension OPEN), MC4 (W∞/Yangian towers, M-level done, H-level OPEN), MC5 (BV=bar, genus 0 proved, higher genus downstream).

**DK ladder**: 0✓, 1✓, 1½✓, 2/3✓(eval-gen core all types), 4(ML proved, algebraic id open), 5(conjectural).

**Total package**: C_A = (Θ_A, κ(A), Δ_A, Π_A, H_A). Virtual bar family V_A = [Rπ_{g*}B̄^{(g)}(A)] ∈ K₀(M̄_g). Extraction: c₁(det V)→κ, c_*(V)→Δ, Hol(V)→Π. Θ_A is upstream (chain-level flatness); V_A is downstream (K-theoretic index).

**Modular homotopy theory** = ∞-category + stable-graph-indexed operations. Bar = Feynman transform. d_mod = d_int + d_sep + d_nonsep. Genus filtration is the fundamental parameter. Tree level = cyclic L∞; all genus = quantum L∞; globalized on curves = modular homotopy type. Cyclicity does NOT automatically lift to quantum — lifting is obstructed. Our Koszul chiral algebras DO give full modular homotopy types.

**Non-scalar Θ_A**: Requires dim H²_cyc ≥ 2 with nontrivial mixed brackets. HPT MC recursion gives universal formula. Current landscape: dim H²_cyc = 1 (scalar saturated). The frontier is concrete realization beyond scalar.

**E₁-E₂-GT**: Yangians stop at E₁. E₂ requires associator/GT. DK = genus-0 E₁-factorization theorem. Modular homotopy = higher-genus deformation of E₁-factorization.

**Vol II** (~/ainfinity-chiral-hochschild-cohomology-3d-qft): 168pp A∞-chiral paper, SC^{ch,top} operad, PVA descent (D5 Jacobi = bottleneck), 5 cross-volume bridges.

---

## MANDATORY PROTOCOLS

1. **Read before write**: Never modify a file you haven't read in this session. Read the target section, understand its current state, then edit surgically.

2. **Build after every change**: `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast`. Do not accumulate unbuildable edits.

3. **No new files**: All content goes into existing chapter files. No new .tex files unless architecturally unavoidable.

4. **No new macros in chapter files**: All macros in main.tex preamble only.

5. **Label everything**: `\label{def:...}`, `\label{thm:...}`, `\label{rem:...}`, `\label{prop:...}`. Cross-reference with `\ref` and `\eqref`.

6. **ClaimStatus on every theorem-class environment**: `\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic`.

7. **Verify formulas against Critical Pitfalls** in CLAUDE.md before writing any formula involving:
   - Bar/cobar signs and conventions (cohomological grading, desuspension)
   - Koszul duality (Com! = Lie, NOT coLie)
   - Central charges (Sugawara, Feigin-Frenkel, DS formulas)
   - Curved A∞ (m₁² = [m₀,-], COMMUTATOR with MINUS sign)
   - FM compactification (blowup, NOT complement)
   - QME (factor 1/2), HCS (coefficient 2/3)

8. **H/M/S semantic level**: Tag each major statement at one declared level. H = ∞-categorical. M = dg/bar-complex. S = cohomological/numerical.

9. **Concordance is the constitution**: When in doubt about status/scope of any theorem, defer to concordance.tex Chapter 34.

10. **Git attribution**: All work is by Raeez Lorgat. No AI attribution anywhere.

---

## EXECUTION INSTRUCTIONS

Execute tasks from `notes/MASTER_PROPAGATION_TASKLIST_v44.md` in the recommended phase order:

**Phase 1 — Structural/Definitional** (highest leverage):
A0.1, A0.2, A0.4, A1.1, A1.6, A2.1, A3.1, A3.4, A3.5

**Phase 2 — Deep Formula Installation**:
A1.2, A1.3, A1.4, A1.5, A5.1, A5.2, A5.3, A5.4, A5.5, A9.1-A9.6

**Phase 3 — Propagation Across Manuscript**:
A2.2, A2.3, A2.4, A3.2, A3.3, A3.6, A6.1, A6.2, A6.3, A6.4, A7.1, A7.2, A7.3

**Phase 4 — New Content (E₁-E₂-GT, Cross-Volume)**:
A4.1, A4.2, A4.3, A4.4, A8.1

**Phase 5 — Editorial Cleanup**:
A0.3, A1.7, A5.6, A10.1, A10.2, A10.3

For each task:
1. Read the task specification from the task list
2. Read the target file(s) at the specified location(s)
3. Draft the content in your head — verify every formula, every cross-reference, every claim status
4. Execute the edit with the Edit tool (or Write for new sections)
5. Build and verify: `make fast`
6. If build fails, diagnose and fix immediately
7. Move to the next task

**Chriss-Ginzburg delivery**: Every definition should feel inevitable. Every theorem statement should be self-contained. Every proof should proceed in clean numbered steps. Every remark should illuminate, not pad. Examples first, then abstraction. When a construction appears, say what it does before saying how it works.

**Size of edits**: Each task typically requires 20-80 lines of LaTeX. Some (A5.1, A1.1) may require 100-200 lines. Do not bloat. The manuscript is already 1796 pages.

---

## SESSION ENTRY

Before executing any task:
1. `grep -rc 'ClaimStatus' chapters/ appendices/ --include='*.tex' | tail -5` (fresh census)
2. `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast` (verify clean build)
3. `cd compute && .venv/bin/python -m pytest tests/ -q` (verify tests pass)
4. Read `notes/MASTER_PROPAGATION_TASKLIST_v44.md` in full
5. Read `chapters/connections/concordance.tex` lines 1-200 (constitutional preamble)
6. Then begin Phase 1, task A0.1

---

## ANTI-PATTERNS (failure modes to avoid)

- **Do not summarize what you just did** at the end of every edit. The diff is visible.
- **Do not add TODO comments** in .tex files. Track externally.
- **Do not duplicate definitions** — reference from Part 1.
- **Do not create new .tex files** when content belongs in existing chapter.
- **Do not add packages** without checking preamble compatibility.
- **Do not change verified formulas** without checking Critical Pitfalls.
- **Do not write "it is easy to verify"** or "one checks that" — either prove it or cite it.
- **Do not fabricate references** — only cite entries in bibliography/references.tex.
- **Do not over-engineer** — the minimum LaTeX needed for each task, no more.
- **Do not lose physical meaning** — every formula should come with one sentence of physical interpretation.
- **Do not conflate H/M/S levels** — if a statement is M-level, say so.
- **Do not add emojis** — this is a mathematics monograph.
