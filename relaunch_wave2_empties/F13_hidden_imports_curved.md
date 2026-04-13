# F13_hidden_imports_curved (current rerun)

## Findings

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:37` — PROBLEM: the chapter opening says bar-cobar “preserves quasi-isomorphisms because it is a quantum `L_\infty` functor whose Maurer--Cartan moduli are invariant under gauge equivalence,” but the cited homotopy input is `thm:operadic-homotopy-convolution`, whose live statement is only the Robert-Nicoud--Wierstra identification of the convolution algebra as an `s\mathscr L_\infty`-algebra ([algebraic_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:880)). That theorem does not prove bar-cobar quasi-isomorphism invariance. FIX: replace these sentences by a narrower statement: the homotopy-invariant object is the convolution `L_\infty`-algebra, and it is used only to control Maurer--Cartan data under `\infty`-morphisms.

- [CRITICAL] `chapters/theory/bar_cobar_adjunction_curved.tex:41` — PROBLEM: the text says “The precise content of Theorem~A (`thm:bar-cobar-adjunction`) is” the full adjunction with unit, counit, and Verdier compatibility, but the live theorem `thm:bar-cobar-adjunction` in [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1927) is the geometric unit theorem, not the entire package. The paragraph is silently importing the counit and Verdier statements from elsewhere. FIX: split the sentence by source: geometric unit = `thm:bar-cobar-adjunction`; full unit/counit package = `thm:bar-cobar-isomorphism-main`; inversion = `thm:bar-cobar-inversion-qi`; Verdier intertwining = `thm:verdier-bar-cobar`.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:749` — PROBLEM: the Virasoro completion example invokes `Definition~\ref{def:primitive-defect-series}` to describe the primitive-cumulant tail, but this chapter never restates what the primitive-defect series is. The example therefore hides a nonlocal definition at the point where it first matters. FIX: add a one-sentence recap of the defining series here, or state explicitly which earlier section supplies the definition and quote the formula.

- [HIGH] `chapters/theory/bar_cobar_adjunction_curved.tex:1505` — PROBLEM: the MC4 splitting remark introduces `R_\cA` and the resonance rank `\rho(\cA)` by citing `Definition~\ref{def:resonance-rank}`, but the content of that definition is not paraphrased locally. The chapter silently imports the key notion controlling the resonant MC4 lane. FIX: add a short local definition of `R_\cA` and `\rho(\cA)`, or restate the defining formula inline before using the trichotomy.

## Summary

Checked: opening adjunction package, Virasoro completion example, and MC4 splitting lane in `bar_cobar_adjunction_curved.tex` | Findings: 4 | Verdict: FAIL
