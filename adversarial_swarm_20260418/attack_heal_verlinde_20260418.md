# Verlinde recovery: adversarial attack and heal

**Date**: 2026-04-18
**Target**: `prop:verlinde-from-ordered` (Vol~I `chapters/theory/higher_genus_modular_koszul.tex:33369-33518`)
**Engine**: `compute/lib/verlinde_ordered_engine.py`
**HZ-IV decorator**: `compute/tests/test_hz_iv_decorators_wave1.py:316-342`
**Prior wave**: `adversarial_swarm_20260417/wave7_verlinde_ds_attack_heal.md` (2026-04-17) concluded SURVIVES.
**This wave**: re-attack with fresh eyes; SCOPE CORRECTIONS + STATUS DOWNGRADE.

Voices: Verlinde 1988; Tsuchiya--Ueno--Yamada 1989; Faltings 1994; Beauville--Laszlo 1994; Kac--Peterson 1984; Zhu 1996; Frenkel--Zhu 1992; Beilinson--Drinfeld factorisation; Francis--Gaitsgory relative Ran; Mok logarithmic factorisation.

---

## Phase 1 — adversarial findings

### (i) The proof splits into five clauses, each with a different epistemic status

The inscribed proposition has five numbered parts. Probing each from first principles:

- **(i) genus 0: $Z_0 = \sum_j S_{0j}^2 = 1$.** S-matrix unitarity. Classical. Moore--Seiberg 1989 / Kac--Peterson 1984. Trivially reproduced from ordered chiral homology at $g = 0$ with no insertions (the space of vacua is one-dimensional).
- **(ii) genus 1: $Z_1 = \sum_j S_{0j}^0 = k+1$.** Integrable representation count. Three equivalent routes — direct $S$-matrix sum, Zhu algebra $A(V_k(\mathfrak{sl}_2)) \cong U(\mathfrak{sl}_2)/(e^{k+1}, f^{k+1})$ of Frenkel--Zhu 1992, and the degree-0 ordered centre at integrable level. The Zhu route through Zhu 1996 Thm 3.3.2 is standard.
- **(iii) general genus $g \geq 2$: $Z_g = \sum_j S_{0j}^{2-2g}$.** The proof reads verbatim: *"The Verlinde formula~\cite{Verlinde88} gives $Z_g = \sum_j S_{0j}^{2-2g}$... From the ordered chiral homology: the symmetric coinvariants of the ordered chain complex compute the conformal blocks via the factorization property (TUY~\cite{TUY89})."* This is **citation-level Verlinde** (Verlinde88) plus **citation-level TUY factorization** (TUY89). The genuine Vol-I content is the identification of conformal blocks with $H^0$ of the bar complex via `prop:conformal-blocks-bar` (`chapters/theory/chiral_modules.tex:540`); everything else is classical.
- **(iv) handle attachment.** The proof reads: *"a genus-$g$ surface with a non-separating cycle cut open gives a genus-$(g{-}1)$ surface with two extra marked points. The bar complex sewing map reglues these marked points, summing over the $k+1$ intermediate representations with the propagator $S_{0j}^{-2}$."* The bar-complex sewing is the load-bearing step; it requires the modular-family extension of Theorem~$A^{\infty,2}$ from a fixed smooth curve $X$ to the Deligne--Mumford boundary of $\overline{\cM}_{g,n}$.
- **(v) separating factorization.** The proof invokes *"Theorem~A for the ordered bar complex on $\Ran^{\mathrm{ord}}$"* — as a **bare-string name with no `\ref{}`**. This is a **ghost reference**. The actual inscribed Theorem~$A^{\infty,2}$ (`thm:A-infinity-2` in `chapters/theory/theorem_A_infinity_2.tex`) is PROVED on a FIXED SMOOTH CURVE only; the modular-family extension including boundary (required for separating degeneration at a node) is CONDITIONAL on GR17 six-functor relative-Ran base change + Mok25 log-FM sewing, both cited at citation level and not inscribed in Vol~I (`rem:A-infinity-2-modular-family-scope`, `theorem_A_infinity_2.tex:918`).

**Finding**: clauses (iv) and (v) rely on modular-family Theorem~A at the boundary, which is EXPLICITLY CONDITIONAL. The proposition is tagged `\ClaimStatusProvedHere` but its parts (iv)--(v) are load-bearing on Vol-I material labelled CONDITIONAL by its own `rem:A-infinity-2-modular-family-scope`. This is an AP287 (cross-volume ProvedHere discipline without attribution tag) violation scoped to Vol~I internal HZ-11.

### (ii) The ghost reference at line 33505

Line 33505 reads:

> (Theorem~A for the ordered bar complex on $\Ran^{\mathrm{ord}}$)

Zero `\ref{}` anywhere in the parenthetical. Grep for the exact string across all three volumes finds it at this single site. This is a **naming-reference-without-label** pattern (AP241 advertised-but-not-inscribed variant / AP286 tactical close without semantic heal): the name stabilises on the reader's memory of Theorem~A, without the commitment of `\ref{thm:A-infinity-2}` that would trigger the scope remark at `theorem_A_infinity_2.tex:918`.

### (iii) Engine's "three independent code paths" are algebraically identical

`verlinde_Z2_three_paths` (engine, `compute/lib/verlinde_ordered_engine.py:420-479`) returns three values:

- `z2_direct = sum(S0 ** -2)` (direct $S$-matrix summation)
- `z2_handle = sum(H * sector_g1)` with `H = S0 ** -2` and `sector_g1 = ones(k+1)` — reduces to `sum(S0 ** -2)`
- `z2_qdim = s00 ** -2 * sum(d ** -2)` with `d = S0 / s00` — reduces to `sum(S0 ** -2)` after cancellation

The engine's docstring at line 436 admits the collapse verbatim: *"All three are algebraically identical but follow different code paths."* The three "paths" are three code-level rewrites of the single trigonometric identity $\sum_j S_{0j}^{-2}$, not three disjoint mathematical derivations.

This is the AP288 pattern (decorator-label vs test-body computation disjointness; Wave-12 catalogue) specialised: the engine-level label-disjointness is genuine (three function names, three formulas) while the computation-level disjointness is vacuous (all three evaluate the same trigonometric sum). Stronger than AP277 because the decorator prose is sound (three code paths agree, cross-validated against a hardcoded table from Bakalov--Kirillov Table 3.1), but the word "independent" in the decorator context overstates: code-level independent, mathematically tautological.

### (iv) HZ-IV decorator at boundary genera is genuinely disjoint

`test_hz_iv_decorators_wave1.py:316-342` carries three paths:

- $Z_0 = 1$ from $S$-matrix unitarity (Moore--Seiberg 1989 modular-category axiom);
- $Z_1 = k+1$ from WZW representation count (Gepner--Witten 1986);
- Beauville--Laszlo 1994 / Faltings 1994 moduli-of-bundles $\dim H^0(\cM_G(\Sigma_g), L^k)$ = Verlinde number.

These ARE mutually disjoint (modular-category axioms vs. WZW representation theory vs. algebraic geometry of bundle moduli). The test body `test_verlinde_from_ordered_boundary_checks` verifies only $Z_0 = 1$ and $Z_1 = k+1$ numerically for $k \in \{1, \ldots, 5\}$. The third path (Beauville--Laszlo) is **not** exercised in the test body at $g \geq 2$; it is a literature pointer that backs the decorator prose but does not fire in code. The decorator's disjointness claim is sound at boundary genera ($g \in \{0, 1\}$); at $g \geq 2$ the decorator relies on the citation-level Beauville--Laszlo identification, not on a constructive engine-level verification.

### (v) Bibkey audit

All citations used in the proposition + scope remarks resolve in `bibliography/references.tex`: `Verlinde88` (:1706), `TUY89` (:1308), `Zhu96` (:1294), `FZ92` (:583), `GR17` (:631), `Mok25` (:1022), `Beauville` (:132). No AP264 / AP281 phantom citations.

### (vi) Small-case numerical cross-check

Manuscript table lines 33419--33426:

- $Z_2(1) = 4$: computed $\sum_{j=0}^{1} S_{0j}^{-2}$ with $S_{00} = S_{01} = 1/\sqrt{2}$ gives $2 + 2 = 4$. ✓
- $Z_2(2) = 10$: Faltings 1994 Table 1 gives $h^0(\cM_{\SU(2)}(\Sigma_2), L^2) = 10$. ✓
- $Z_g(1) = 2^g$: the pointed-MTC case $k = 1$ has $S_{00} = S_{01} = 1/\sqrt{2}$ so $Z_g = 2 \cdot (1/\sqrt{2})^{2-2g} = 2^g$. ✓

Numerical content of the proposition survives. The scope issue is structural, not arithmetical.

---

## Phase 2 — surviving core

After attack, the surviving mathematical content of `prop:verlinde-from-ordered`:

- **Classical** (parts i--iii): Verlinde 1988 formula + TUY 1989 factorisation + Vol-I bar-complex/conformal-block identification `prop:conformal-blocks-bar`. This is a WINDOW through which the Vol-I ordered bar complex framework recovers the classical Verlinde count. The novelty is the ordered dictionary (each isospin channel $j$ corresponds to a weight-$S_{0j}^{2-2g}$ block of ordered bar coinvariants), not the integers themselves.
- **Conditional** (parts iv--v): bar-complex sewing at the boundary is the modular-family extension of Theorem~$A^{\infty,2}$, load-bearing on GR17 + Mok25 (cited not inscribed).

The Vol-I-novel content connected to Verlinde lives downstream: `rem:verlinde-shadow-truncation` (the shadow tower $\{F_g\}$ is the generic-level ancestor of Verlinde, with $Z_g$ recovered at integer $k$ as ranks of the modular functor) and `thm:verlinde-polynomial-family` (closed forms $P_g(n) = n^{g-1}(n^2-1) R_{g-2}(n^2)$ through genus~6, with leading coefficient $\zeta(2g-2)/(2^{g-2} \pi^{2g-2})$).

---

## Phase 3 — heal

### Edit 1 — `chapters/theory/higher_genus_modular_koszul.tex`

(a) Proposition `\ClaimStatus` tag `\ClaimStatusProvedHere` → `\ClaimStatusProvedElsewhere` (the load-bearing steps are Verlinde 1988 + TUY 1989 + Zhu 1996 + Frenkel--Zhu 1992; the Vol-I contribution is the bar-complex window via `prop:conformal-blocks-bar`, not the Verlinde integers).

(b) Line 33505 ghost reference *"Theorem~A for the ordered bar complex on $\Ran^{\mathrm{ord}}$"* → *"Theorem~$A^{\infty,2}$, \ref{thm:A-infinity-2}, applied to the ordered bar complex on $\Ran^{\mathrm{ord}}(X)$"*.

(c) Added honest scope sentence in the proof of clause (v): *"Clauses (iv) and (v) are conditional on the modular-family extension of Theorem~$A^{\infty,2}$ from a fixed smooth curve to the Deligne--Mumford boundary of $\overline{\cM}_{g,n}$; that extension is cited at citation level (Francis--Gaitsgory relative Ran six-functor base change~\cite{GR17}, Mok logarithmic factorization sewing~\cite{Mok25}) and is not inscribed in Vol~I (Remark~\ref{rem:A-infinity-2-modular-family-scope})."*

(d) Added honest sentence on engine paths: *"The three numerical code paths in `verlinde_Z2_three_paths` (direct $S$-matrix sum, quantum-dimension rewrite, and handle recursion seeded from $Z_1$) are algebraically identical rewrites of $\sum_j S_{0j}^{-2}$ and agree as trigonometric identities; they supply code-level cross-validation but do not constitute three genuinely disjoint derivations."*

(e) New remark `rem:verlinde-from-ordered-scope` inscribed immediately after the proof, recording what is proved elsewhere (Verlinde 1988 + TUY 1989 + Zhu 1996 + Frenkel--Zhu 1992 + `prop:conformal-blocks-bar`), what is conditional (modular-family Theorem~$A^{\infty,2}$ extension), and what is Vol-I-novel (shadow tower as generic-level ancestor; Verlinde polynomial family).

### Edit 2 — `standalone/theorem_index.tex`

Row for `prop:verlinde-from-ordered`: `\texttt{ProvedHere}` → `\texttt{ProvedElsewhere}` (line 986).

### Edit 3 — `CLAUDE.md`

Verlinde-recovery status row rewritten with full scope breakdown: boundary-genera unconditional; $g \geq 2$ citation-level; clauses (iv)--(v) conditional on modular-family Theorem~$A^{\infty,2}$ extension; engine paths algebraically identical rewrites (AP288 scope-remark); Vol-I-novel content localised to `rem:verlinde-shadow-truncation` and `thm:verlinde-polynomial-family`.

---

## Phase 4 — new confusion patterns registered

No new AP block-allocations needed: all findings fit within existing patterns.

- AP287 (cross-volume ProvedHere discipline without attribution) applied intra-Vol-I to `prop:verlinde-from-ordered` invoking conditional `thm:A-infinity-2` modular-family scope.
- AP288 (decorator-label vs test-body computation disjointness) applied to `verlinde_Z2_three_paths` three-path label vs single-trigonometric-identity computation.
- AP286 (tactical phantomsection vs semantic heal) — the bare-string "Theorem~A for the ordered bar complex on $\Ran^{\mathrm{ord}}$" at line 33505 is a NAMING drift (no `\ref{}`), the extreme case of AP286 where even the phantomsection alias was not deployed.

---

## Phase 5 — propagation

- Vol~II grep for `prop:verlinde-from-ordered`: zero hits.
- Vol~III grep for `prop:verlinde-from-ordered`: zero hits.
- Vol~I consumers: `chapters/frame/preface.tex:4321` prose cite (preface prose, scope carried by proposition itself; no edit).
- Vol~I internal consumers at `higher_genus_modular_koszul.tex:33700` (`rem:verlinde-via-zhu` cites clause~(ii) — scope unchanged for clause~(ii) since it is classical-via-Zhu).
- Bibliography entries verified: `Verlinde88`, `TUY89`, `Zhu96`, `FZ92`, `GR17`, `Mok25`, `Beauville` all defined.

---

## Verdict

`prop:verlinde-from-ordered` SURVIVES with SCOPE DOWNGRADE: status `\ClaimStatusProvedHere` → `\ClaimStatusProvedElsewhere`; clauses (iv)--(v) explicitly conditional on modular-family Theorem~$A^{\infty,2}$ extension; ghost Theorem~A reference retargeted to `\ref{thm:A-infinity-2}`; engine's three-path claim rewritten as algebraically identical code-level rewrites; honest scope remark `rem:verlinde-from-ordered-scope` inscribed recording what is classical, what is conditional, and what is Vol-I-novel (shadow-tower generic-level ancestor + Verlinde polynomial family). The CLAUDE.md status row is rewritten to match.

Wave-7 (2026-04-17) had concluded SURVIVES without noticing (a) the bare-string Theorem~A reference at line 33505 evading the modular-family scope remark, (b) the tension between `\ClaimStatusProvedHere` and the conditional status of the load-bearing modular-family Theorem~A, or (c) the algebraic collapse of the "three independent code paths" in `verlinde_Z2_three_paths`. Wave-18 (today) heals all three.
