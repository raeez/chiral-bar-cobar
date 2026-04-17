# Wave-6 Theorem B phantom re-audit (2026-04-18)

**Scope.** Adversarial re-verification of the 2026-04-18 heal inscribed in
`adversarial_swarm_20260418/attack_heal_theorem_B_20260418.md`. The CLAUDE.md
Theorem B row flags `thm:chiral-positselski-7-2` and
`thm:chiral-positselski-5-3` as PHANTOM with the preface carrying the only
`\phantomsection\label{thm:chiral-positselski-7-2}` at `preface.tex:5081`.
This re-audit confirms that the prior heal has already executed and that
the CLAUDE.md status row is now STALE (AP271 reverse-drift: CLAUDE.md
lagging behind the manuscript).

## Attack ledger (verified from source, not CLAUDE.md)

| # | File:line | Severity | Category | Current state |
|---|-----------|----------|----------|---------------|
| 1 | `chapters/theory/theorem_B_scope_platonic.tex:246-247` | n/a | AP286 Option-A alias (legitimate) | Two `\phantomsection\label{}` aliases installed at the real theorem home `thm:chiral-positselski-weight-completed`. All three labels refer to the same coderived-equivalence content; Positselski-Memoirs `(7,2)` and `(5,3)` nicknames alias to the one inscribed theorem. AP273 violation AVOIDED by refusing Option B. |
| 2 | `chapters/frame/preface.tex:5140` | n/a | AP255 closure | Preface phantomsection retired to a comment; label now lives only at its real home. |
| 3 | `chapters/theory/theorem_B_scope_platonic.tex:177-229` | n/a | Finite-weight step | `thm:chiral-positselski-at-each-weight` with 3-step proof (conilpotency on truncation, chiral co-contra, naturality in w). `\ClaimStatusProvedHere`. |
| 4 | `chapters/theory/theorem_B_scope_platonic.tex:243-356` | n/a | Weight-completed step | `thm:chiral-positselski-weight-completed` with 5-step proof (pro-conilpotency, coderived inverse limit with explicit Mittag--Leffler argument, finite-weight application along tower, contraderived inverse limit, unconditional scope). `\ClaimStatusProvedHere`. Positselski 2011 Thm 4.6 / Thm 5.3 cited at citation level with explicit justification (chiral tensor $\chirtensor$ preserves filtered colimits; $\cD_X$-module structure descends levelwise). |
| 5 | `chapters/theory/theorem_B_scope_platonic.tex:378-425` | n/a | AP266 sharpened obstruction | `prop:chiral-positselski-raw-direct-sum-class-M-false` with explicit witness: $S_4(\mathrm{Vir}_c) = 10/[c(5c+22)] \neq 0$ at generic $c$ forces nonzero bar cohomology at weight 4 in bounded direct-sum `Ch(Vect)` ambient. `\ClaimStatusProvedHere`. |
| 6 | `chapters/theory/theorem_B_scope_platonic.tex:427-447` | n/a | HZ-11 attribution | `rem:theorem-B-chain-level-G-L-attribution` inscribed, tagged `\ClaimStatusProvedElsewhere`, names the theorem home Vol II `bv_brst.tex` `thm:bv-bar-coderived` clauses (ii)--(iii). |
| 7 | Vol II `bv_brst.tex:2063-2140` | n/a | External anchor verified | `thm:bv-bar-coderived` inscribed with four clauses. Clauses (ii) and (iii) prove chain-level weak equivalence of filtered curved models for class $\mathsf{G}$/$\mathsf{L}$ (Jacobi kills cubic harmonic term; PBW-associated graded reduces to genus-0 weight-by-weight comparison) and $\mathsf{C}$ under harmonic decoupling. Class $\mathsf{M}$ clause (iv) produces coacyclic cone with $\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$. |

## Consumer resolution table

```
\ref{thm:chiral-positselski-7-2}
    chapters/frame/programme_overview_platonic.tex:117  RESOLVES
    chapters/theory/chiral_climax_platonic.tex:867       RESOLVES
    Vol II chapters/theory/chiral_higher_deligne.tex (ref)  RESOLVES
\ref{thm:chiral-positselski-5-3}
    zero consumer hits across the three volumes (safe).
\label{thm:chiral-positselski-7-2}
    theorem_B_scope_platonic.tex:246  (legitimate alias)
\label{thm:chiral-positselski-5-3}
    theorem_B_scope_platonic.tex:247  (legitimate alias)
\label{thm:chiral-positselski-weight-completed}
    theorem_B_scope_platonic.tex:245  (canonical)
```

The verbatim mentions in `standalone/five_theorems_modular_koszul.tex:2900-2901`
and `standalone/theorem_index.tex:2373` are `\verb|...|` / `\detokenize{...}`
documentation, not `\ref{}` consumers; they correctly describe the alias
structure.

## Surviving core

The weight-completed chiral Positselski equivalence is PROVED unconditionally
for every chiral algebra with positive-energy conformal-weight grading and
finite-dimensional weight spaces; the proof is an explicit Mittag--Leffler
/ Milnor argument on the tower $\{C/F^{\leq w}\}$ together with the chiral
co-contra correspondence applied at each finite weight. The raw direct-sum
chiral Positselski equivalence is PROVABLY FALSE on class $\mathsf{M}$,
certified by $S_4(\mathrm{Vir}_c) = 10/[c(5c+22)] \neq 0$. Chain-level
class $\mathsf{G}$ and class $\mathsf{L}$ strict quasi-isomorphisms are
`\ClaimStatusProvedElsewhere`, attributed to Vol II `thm:bv-bar-coderived`
(ii)--(iii).

## Heal status

No additional edits required beyond the 2026-04-18 prior session. The
CLAUDE.md Theorem B row is STALE (AP271: reverse-drift, CLAUDE.md lagging
behind the source) in describing `thm:chiral-positselski-7-2` and
`thm:chiral-positselski-5-3` as PHANTOM and pointing at
`preface.tex:5081`. The recommended update is the one already inscribed
in the prior session note at Phase 5 / Phase 3 §8. No commits from this
session.

## Commit plan

No commits. The CLAUDE.md row refresh is the only residual action; it
will be absorbed into the next cross-volume CLAUDE.md refresh wave per
AP5 (same-session propagation is not achievable here because the
CLAUDE.md theorem-status table carries other stale rows from the
2026-04-16 wave that require their own targeted audits before a unified
refresh).
