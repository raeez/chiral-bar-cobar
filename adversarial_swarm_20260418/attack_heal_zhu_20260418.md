# Attack-and-heal: Zhu algebra correspondence + Vol I applications

Date: 2026-04-18
Author: Raeez Lorgat
Mission: adversarial audit of Zhu 1996 + Frenkel–Zhu 1992 applications across Vol I
Scope: `chapters/**/*.tex`, `standalone/**/*.tex`

## Phase 1: inventory

### Primary locus (definition + theorem statement)

`chapters/theory/chiral_modules.tex`
- `def:zhu-algebra` (:1844) — standard Zhu (1996) construction.
- `thm:zhu-correspondence` (:1863) — `\ClaimStatusProvedElsewhere` citing Zhu96. Hypothesis: $V$ of countable dimension + $C_2$-cofinite. Conclusions: (i) bijection `simple positive-energy V-mod ↔ simple A(V)-mod`, (ii) lowest-weight correspondence, (iii) finite module count when $\dim A(V) < \infty$.
- `ex:zhu-algebras` (:1885) — applies to $\hat{\fg}_k$ (all $k$), $\Vir_c$, $\cW^k(\fsl_2)$, $\cH_k$.
- `prop:zhu-koszul-compatibility` (:1912) — `\ClaimStatusProvedHere` `A(\hat{\fg}_k) \cong U(\fg) \cong A(\hat{\fg}_{-k-2h^\vee})$ and `A(\cH_k) \cong \bC[\alpha] \cong A(\Sym^{ch}(V^*))`.
- `cor:virasoro-zhu-koszul` (:1972) — `A(\Vir_c) \cong \bC[x] \cong A(\Vir_{26-c})$ for all $c \in \bC$.

### Load-bearing consumers

1. `chapters/theory/higher_genus_modular_koszul.tex:33461` — Verlinde recovery at integrable $V_k(\fsl_2)$: `A(V_k) \cong U(\fsl_2)/(e^{k+1},f^{k+1})` has $k+1$ simples. Used in `prop:verlinde-from-ordered` clause (ii).
2. `chapters/theory/higher_genus_modular_koszul.tex:29812` — "At non-degenerate admissible levels, $L_k(\fg)$ is rational with semisimple Zhu algebra" — scope-qualified.
3. `chapters/theory/higher_genus_foundations.tex:921, 987-989` — Level (v) of modular-functor hierarchy. Zhu~\cite{Zhu96} cited for "genus-$g$ conformal blocks finite-dimensional for all $g$, projectively flat connection".
4. `chapters/theory/chiral_koszul_pairs.tex:1385` — formal-disk reduction to Beilinson–Ginzburg–Soergel `Zhu(A)` (this is a different "Zhu", BGS category O, not the VOA construction; matches `\operatorname{Zhu}` macro convention, correct usage).
5. `chapters/theory/chiral_koszul_pairs.tex:1566-1571` — explicit scope remark: rationality + $C_2$-cofiniteness + semisimple Zhu ≠⇒ chiral Koszulness. Correct discipline.
6. `chapters/theory/chiral_koszul_pairs.tex:6021` — $\dim \ChirHoch^*(W_3) < \infty$ attributed to "Zhu's theorem". MISATTRIBUTION — Zhu controls positive-energy module theory, not chiral Hochschild.
7. `chapters/theory/periodic_cdg_admissible.tex:315-319` — associated graded of admissible $L_k(\fg)$ as direct sum of $A(L_k(\fg))$-modules via Arakawa rationality. Scope: admissible level. Correct.
8. `chapters/theory/theorem_h_off_koszul_platonic.tex:731-735` — (a) vs (K)/(L): Arakawa proof uses Zhu finite-dim as disjoint input. Scope: admissible. Correct.
9. `chapters/theory/existence_criteria.tex:564-571` — open status for $\cW_k(\fg)$ at admissible level: $C_2$-cofinite + finite-dim Zhu do NOT imply chiral Koszulness. Correct discipline.
10. `chapters/theory/shadow_tower_quadrichotomy_platonic.tex:1093-1096` + :1180-1184 — `\cW(p)` tempering via Zhu-bounded Massey RETRACTED (Gurarie 1993 / Flohr 1996 counter-examples). Correct per B91/Wave-1 audit.
11. `chapters/examples/logarithmic_w_algebras.tex:265-274, 740-743, 795-797` — $C_2$-cofiniteness-via-Zhu definition + retraction note. Correct.
12. `chapters/examples/kac_moody.tex:2907` — rational $L_k(\fg)$ at admissible with finite-dim semisimple Zhu, cross-cites `thm:zhu-correspondence`. Scope: admissible. Correct.
13. `chapters/examples/w_algebras.tex:2720, 2728` — Verlinde-chain attribution via Zhu at genus 1 + factorization. Correct chain.
14. `chapters/examples/w_algebras.tex:104-116` — `thm:wn-s-matrix` `\ClaimStatusProvedElsewhere` citing `{FZ92,Arakawa17}`. Correct.
15. `chapters/examples/minimal_model_fusion.tex:3042-3046` — $\cW(2,p)$ minimal model, $p-1$ simples = $\binom{p-1}{2}$. Zhu algebra isomorphism under Koszul dual; references `rem:zhu-koszul-scope`. Correct.
16. `chapters/examples/lattice_foundations.tex:3443-3449` — Zhu algebra as Route C for lattice VOA, comparison with center. Correct.
17. `chapters/examples/free_fields.tex:2267, 2571-2573` — Zhu-level Koszul pairing for Heisenberg. Correct (generic Heisenberg $\cH_k$ is not $C_2$-cofinite in the strict sense; A(H_k)=C[J_0] is the well-defined Zhu algebra without needing $C_2$-cofiniteness — the construction works for any countable VOA; $C_2$-cofiniteness is only needed for clause (iii) finiteness).
18. `chapters/connections/arithmetic_shadows.tex:3073-3074` — Zhu modular invariance for $V^\natural$ (holomorphic $c=24$, $C_2$-cofinite, rational). Correct.
19. `chapters/connections/thqg_introduction_supplement.tex:4330-4333` — Arakawa $C_2$-cofinite coset + Frenkel–Zhu conformal closure. Scope: freely generated or $C_2$-cofinite. Correct.
20. `chapters/connections/thqg_open_closed_realization.tex` — (not inspected individually; same Arakawa/FZ pattern).
21. `chapters/theory/three_hochschild_unification_platonic.tex:57-103, 156-160, 4921-4923` — Zhu functor $\pi_{\rm Zhu}\colon \cA \to A_{\rm mode}$ as a component of the `\Theta_1` map between chiral/topological Hochschild. Scope: this is the generic Zhu-algebra-as-mode-algebra construction, not the $C_2$-cofinite rationality theorem. The claim "For rational $\cA$, $H^0$ is coinvariants = conformal blocks (Zhu)" at :4921-4923 is correctly scope-qualified to rational.

## Phase 2: attack

### Finding F1 — `chiral_koszul_pairs.tex:6021` attribution error (AP272 folklore cross-lemma)

"Formal smoothness: $\dim \ChirHoch^*(W_3) < \infty$ (verified by Zhu's theorem)".

Zhu's theorem (Zhu 1996 Thm 2.2.1/2.2.2/4.4.1) produces (i) the bijection of simple modules + (ii) genus-$1$ modular invariance of characters. It does NOT verify finiteness of chiral Hochschild cohomology. ChirHoch finiteness for $W_3$ is established by Vol I `thm:main-koszul-hoch` (Theorem H polynomial concentration in degrees {0,1,2}) on the Koszul locus, via the bar complex + Shelton–Yuzvinsky Koszulity of the pure-braid Orlik–Solomon algebra, NOT via Zhu's theorem.

Structural diagnosis: the author conflated "Zhu algebra is well-behaved for $W_3$" with "chiral Hochschild is finite-dimensional". Zhu algebra controls the POSITIVE-ENERGY MODULE CATEGORY (finite many simples iff $\dim A(V) < \infty$ + rationality in Zhu sense); chiral Hochschild is computed on the bar complex from the OPE, which is a separate invariant.

### Finding F2 — `higher_genus_foundations.tex:921, 987-989` citation under-scoping (AP309 primary-source-for-weaker-claim)

Level (v) of the modular-functor hierarchy cites "Zhu's theorem~\cite{Zhu96}" for the conclusion "genus-$g$ conformal blocks are finite-dimensional for all $g$, with a projectively flat connection".

Zhu 1996 proves: (a) construction of $A(V)$; (b) simple-module bijection; (c) genus-$1$ modular invariance of characters assuming $C_2$-cofiniteness (Thm 4.4.1). Zhu does NOT prove higher-genus finite-dimensionality of conformal blocks; that is Tsuchiya–Ueno–Yamada 1989 at the factorization level, Nagatomo–Tsuchiya 2005 / Huang 2005 for rigorous bundle + projective flat connection statements on $\overline{\cM}_{g,n}$ for $C_2$-cofinite VOAs, and Damiolini–Gibney–Tarasca 2021 for the sheaf-of-coinvariants bundle construction.

Citing Zhu 1996 alone for the "all $g$" statement over-attributes — the higher-genus content is a strictly stronger classical theorem than what Zhu inscribed.

### Finding F3 (non-issue) — scope mismatch of `thm:zhu-correspondence` hypothesis vs `ex:zhu-algebras` application

Superficial: `thm:zhu-correspondence` hypothesises $V$ countable + $C_2$-cofinite, but examples include $\Vir_c$, $\cH_k$, $V^k(\fg)$ at generic levels — none of which are $C_2$-cofinite.

Resolution: the BIJECTION clause (i) and LOWEST-WEIGHT clause (ii) of Zhu 1996 (Thm 2.2.1–2.2.2) work for any countable VOA with positive-energy modules; $C_2$-cofiniteness is needed only for clause (iii) FINITENESS of the module count. The examples use clauses (i)–(ii), which are fine. No heal needed: a one-line scope remark inside `thm:zhu-correspondence` would improve legibility but the mathematics is correct as inscribed (and AP254 / AP266 favour not over-inscribing).

### Finding F4 (non-issue) — `cor:virasoro-zhu-koszul` and `prop:zhu-koszul-compatibility`

These identifications $A(\Vir_c) \cong \bC[x] \cong A(\Vir_{26-c})$ and $A(\hat{\fg}_k) \cong U(\fg) \cong A(\hat{\fg}_{-k-2h^\vee})$ follow from Frenkel–Zhu 1992 Prop 3.4.1 (Kac–Moody) and Thm 4.1 (Virasoro), which DO NOT require $C_2$-cofiniteness — Frenkel–Zhu compute $A(V)$ directly via the surjection $V/\sum L_{-n}V \to A(V)$ + zero-mode bracket, for any countable VOA. Scope discipline is correct; the propositions stand as `\ClaimStatusProvedHere`.

### Finding F5 (non-issue) — Frenkel–Zhu genus-1 at genus $g$

Question: are Frenkel–Zhu 1992 zhu-gradings (genus 1) applied correctly to deformation arguments at genus $g$?

Search trace: the Frenkel–Zhu citations in `higher_genus_modular_koszul.tex` are confined to the $Z_1 = k+1$ genus-1 count (prop:verlinde-from-ordered clause (ii)) and do not extend to deformation arguments at $g \geq 2$. The $g \geq 2$ recoveries use Verlinde 1988 + TUY89 + `thm:A-infinity-2` modular-family extension (itself CONDITIONAL per `rem:A-infinity-2-modular-family-scope`). No deformation-to-higher-genus step in Vol I silently uses FZ92 outside its genus-1 domain.

## Phase 3: heal

### Heal H1 (F1) — correct the ChirHoch attribution

`chapters/theory/chiral_koszul_pairs.tex:6021`: replace the Zhu-theorem attribution with `thm:main-koszul-hoch` (Theorem H polynomial concentration) and clarify that Zhu algebra controls positive-energy module theory, not chiral Hochschild.

Before:
```
\item Formal smoothness: $\dim \ChirHoch^*(W_3) < \infty$ (verified by Zhu's theorem)
```

After:
```
\item Formal smoothness: $\dim \ChirHoch^*(W_3) < \infty$ (verified by Theorem~\ref{thm:main-koszul-hoch} polynomial concentration; the Zhu algebra $A(W_3)$ controls positive-energy module theory, not chiral Hochschild dimension directly)
```

### Heal H2 (F2) — expand citation at higher-genus modular-functor level

`chapters/theory/higher_genus_foundations.tex:921-922, 987-989`: expand the "Zhu's theorem" citation for the all-$g$ modular-functor conclusion to the correct primary-source chain Zhu + TUY89 + Nagatomo–Tsuchiya + Huang + DGT21.

Both sites inscribed. New bibkeys `NagatomoTsuchiya05`, `Huang05`, `DGT21` added to `standalone/references.bib` following the `TUY89` entry block.

### Heal H3 (constitutional) — no new AP block needed

F1 is an instance of AP272 (unstated-cross-lemma via folklore citation); F2 is an instance of AP309 (primary-source citation for a strictly weaker claim silently extrapolated to the stronger claim). Both APs are already in the catalogue and apply cleanly. Per AP314 (inscription-rate outpaces audit capacity), I do not inscribe AP1221–AP1240 here — the two findings are adequately covered by the existing patterns.

## Phase 4: propagation audit

Search `chapters/**/*.tex` + `standalone/**/*.tex` for other sites claiming higher-genus modular-functor properties "by Zhu's theorem":

- `chiral_koszul_pairs.tex:6021` (F1 heal applied).
- `higher_genus_foundations.tex:921, 987` (F2 heal applied).
- No additional hits for the "by Zhu's theorem" idiom applied to higher-genus content.

AP5 propagation check: the FZ92 + Zhu96 attributions in `higher_genus_modular_koszul.tex:33600-33624` (Verlinde recovery attribution remark) are correctly scoped to genus-1 (FZ92 presentation of $A(V_k(\fsl_2))$ + Zhu96 modular invariance of characters). No propagation needed.

## Phase 5: verification

### Bibkey audit (AP281)

Three new bibkeys added: `NagatomoTsuchiya05`, `Huang05`, `DGT21`. Verified no prior entries via `grep` before insert.

### Line-count changes

- `chapters/theory/chiral_koszul_pairs.tex` :6021 — +1 sentence fragment, same line count.
- `chapters/theory/higher_genus_foundations.tex` :921 — +3 lines (citation chain expansion).
- `chapters/theory/higher_genus_foundations.tex` :987 — +4 lines (citation chain expansion).
- `standalone/references.bib` — +27 lines (three new `@article` entries).

### HZ-11 cross-volume label discipline

All ref targets are Vol I local (`thm:main-koszul-hoch` in `chiral_hochschild_koszul.tex:1791`; `thm:A-infinity-2` in `theorem_A_infinity_2.tex`; `rem:A-infinity-2-modular-family-scope` inscribed). No cross-volume citations introduced; HZ-11 satisfied.

### Constitutional metadata hygiene

Per CLAUDE.md hygiene rule: no `AP\d+` tokens in typeset content; the manuscript heals use mathematical phrasing ("polynomial concentration", "positive-energy module theory") rather than AP labels. The AP labels appear only in this report file + CLAUDE.md.

## Summary

Two genuine findings + three non-issues. Both findings heal via citation refinement — no mathematical content is retracted, no theorem is downgraded.

- F1 MISATTRIBUTION (AP272): Zhu's theorem cited where Theorem H was meant. Healed at `chiral_koszul_pairs.tex:6021`.
- F2 SCOPE EXTENSION (AP309): Zhu 1996 cited for higher-genus modular-functor conclusions. Healed at `higher_genus_foundations.tex:921, 987` with TUY + Nagatomo–Tsuchiya + Huang + DGT primary-source chain. Bibkeys added.

No CLAUDE.md theorem-status row needs update — neither F1 nor F2 changes the scope of any inscribed theorem; they refine internal proof-chain attributions.

Per AP316 (worktree-isolated Agent delivery discipline): this audit was conducted in the main working tree; no worktree cleanup needed. Edits are live at the main-branch paths cited.

## Appendix — key scope facts for future audits

1. Zhu 1996 construction $A(V) = V/O(V)$ works for ANY countable VOA; $C_2$-cofiniteness is not needed for the construction, only for rationality clause (iii).
2. Zhu 1996 Thm 2.2.1–2.2.2 (bijection of simples) requires only positive-energy + countable; $C_2$-cofiniteness strengthens this to a finite count.
3. Zhu 1996 Thm 4.4.1 (genus-1 modular invariance of characters) requires $C_2$-cofiniteness.
4. Higher-genus finite-dimensional conformal blocks + projective flat connection: TUY89 (factorization), Nagatomo–Tsuchiya 2005 ($\PP^1$ rigorous), Huang 2005 (differential equations + duality), DGT21 (sheaf of coinvariants). The "all $g$" statement should not be attributed to Zhu 1996 alone.
5. Frenkel–Zhu 1992 computes $A(V)$ explicitly for $V = V^k(\fg)$ (Prop 3.4.1) and $V = \Vir_c$ (Thm 4.1); these results are level-independent / $c$-independent and do not require $C_2$-cofiniteness.
6. Zhu algebra finiteness ≠⇒ chiral Hochschild finiteness ≠⇒ chiral Koszulness. Each property is a separate theorem-level assertion.
