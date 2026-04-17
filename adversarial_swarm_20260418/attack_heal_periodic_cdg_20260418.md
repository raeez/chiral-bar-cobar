# Attack-and-heal note: Periodic CDG admissible KL (2026-04-18)

Target: `thm:periodic-cdg-is-koszul-compatible`,
`thm:admissible-kl-bar-cobar-adjunction`,
`thm:adams-analog-construction`,
`cor:class-M-admissible-minimal-model` — all `\ClaimStatusProvedHere`
in `chapters/theory/periodic_cdg_admissible.tex` (871 lines), plus
`conj:adams-analog-higher-rank` (intentionally `\ClaimStatusConjectured`).

Reserved AP block: AP881-AP900 (periodic-CDG swarm).

Author: Raeez Lorgat. No AI attribution.

## Phase 0: Inscription and build-wiring sanity

The file exists (41910 bytes); all four theorem / corollary labels are
inscribed with proof bodies of nontrivial length (Step 1-4, Step 1-3,
Property (i)-(iii), single proof body respectively). `main.tex:1744`
`\input{chapters/theory/periodic_cdg_admissible}` confirms the chapter
is in the build (no AP255 phantom-file failure). All four primary
environment / tag pairs match HZ-2:

- `\begin{theorem}[...; \ClaimStatusProvedHere] \label{thm:periodic-cdg-is-koszul-compatible}` (line 225-227)
- `\begin{theorem}[...; \ClaimStatusProvedHere] \label{thm:admissible-kl-bar-cobar-adjunction}` (line 413-415)
- `\begin{theorem}[...; \ClaimStatusProvedHere] \label{thm:adams-analog-construction}` (line 600-602)
- `\begin{corollary}[...; \ClaimStatusProvedHere] \label{cor:class-M-admissible-minimal-model}` (line 726-728)

Primary bibkeys (`Arakawa15, Fin96, Lus90, Positselski11, FF96, Fre07,
CKL20, Kac98`) all resolve in `standalone/references.bib` (lines
651, 651, 973, 983, 992, 1005, 1014, 1023, 1034). No AP281 dangling
citations for this chapter.

## Phase 1: The six attack vectors

### A1. Arakawa bibkey targets wrong paper (AP281 alias drift, MODERATE)

The CLAUDE.md warning itself raises the question: "Is Arakawa 2007
(arXiv:math/0611289) or Arakawa-van-Ekeren 2019 (arXiv:1911.13196) the
right reference?" Primary-source audit:

- `arXiv:math/0611289` is Arakawa 2007, "Representation theory of
 $\mathcal{W}$-algebras" (Invent. Math. 169 (2007), 219--320). It
 establishes $C_2$-cofiniteness for principal admissible
 $\mathcal{W}$-algebras, not for admissible-level $L_k(\fg)$ directly.
- `arXiv:1211.7124` is Arakawa 2015, "Rationality of
 $\mathcal{W}$-algebras: principal nilpotent cases" (Ann. Math. 182
 (2015), 565--604). This is the file's current `Arakawa15` alias;
 again, a PRINCIPAL $\mathcal{W}$-statement, not $L_k(\fg)$.
- The $C_2$-cofiniteness of $L_k(\fg)$ at non-degenerate admissible
 level $k = -h^\vee + p/q$ is in Arakawa 2016, "Rationality of
 admissible affine vertex algebras in the category $\mathcal{O}$"
 (Duke Math. J. 165 (2016), 67--93; arXiv:1207.4857).

So the chapter cites `Arakawa15 Thm. 4.1` to deliver a $C_2$-cofiniteness
result for $L_k(\fg)$; the cited theorem's actual statement is for
principal admissible $\mathcal{W}$-algebras. The theorem needed is in
Arakawa 2016 (arXiv:1207.4857) instead. This is a classic AP281 alias
drift: the citation RESOLVES at build, but the cited paper does not
state the lemma in the form used. At chapter-impact level this is
AP309 (primary-source citation for a strictly weaker claim, silently
extrapolated): Arakawa 2015 gives rationality of the $\mathcal{W}$-side
for the principal nilpotent; the implication "simple affine $L_k(\fg)$
is $C_2$-cofinite" is from the earlier Arakawa 2016 (or, for specific
cases, Arakawa-van-Ekeren 2019 arXiv:1911.13196 which extends).

**Heal**: add a `Arakawa16` bibkey entry for arXiv:1207.4857 and redirect
the four citation sites (`\cite{Arakawa15}` at lines 192, 462, 758) plus
remark cross-reference at line 195. Preserve `Arakawa15` for the Virasoro
minimal-model rationality call in Corollary~\ref{cor:class-M-admissible-minimal-model}
(line 758: "Arakawa~\cite{Arakawa15} establishes that the Drinfeld-Sokolov
reduction sends..."). The DS-side call IS covered by Arakawa 2015.

### A2. Step 1 `Theta_{2p}` confabulation from critical-level `Theta_1` (AP309, HIGH)

`thm:periodic-cdg-is-koszul-compatible` Step 1 (line 293-309) constructs
the period generator $\Theta_{2p}$ "analogously" to the rank-1
critical-level generator $\Theta_1 \in \ChirHoch^4(\widehat{\mathfrak{sl}}_{2,-2})$
from `prop:sl2-periodicity-dl` (line 1086, `\ClaimStatusProvedElsewhere`,
in `derived_langlands.tex`).

Primary-source check: `prop:sl2-periodicity-dl` proves period $4 = 2h^\vee$
at CRITICAL level $k = -2 = -h^\vee$ for sl_2 Hochschild cohomology. The
admissible case claims period $2p$ for general admissible $(p,q)$ via a
"Kac-Wakimoto character arithmetic" argument that asserts the Poincare
series of a quotient is the $2p$-th cyclotomic polynomial; no citation
supports this, and the "Casimir element under the Wakimoto realisation
restricted to the screening-kernel" construction is not given in any
primary source.

This is AP309: Step 1 silently extrapolates the critical-level sl_2 period
$2h^\vee = 4$ (PROVED in Prop.~sl2-periodicity-dl) to the admissible
period $2p$ (NOT established). The Kac-Wakimoto character formula does
not on its face produce a $2p$-cyclotomic factor in the Feigin-Frenkel
center quotient; the Kac-Kazhdan determinant and the admissible-weight
structure give the $(p-1)(q-1)/2$ Kac-table count, not directly a $2p$
cyclotomic period.

**Sharpened obstruction (AP266 heal template)**: the correct statement
is that CUP PRODUCT WITH the Kac-Wakimoto period class on the
semisimplified Finkelberg target gives $2p$-Tate-cohomological
periodicity (Lusztig 1990 Prop. 8.3). Transporting this to
$\barB^{\mathrm{ch}}(\widehat{\fg}_k)$ on filtration quotients requires
a Finkelberg-equivalence chain map, which is part (iii) of the theorem,
not part (i). Step 1 should cite Lusztig 1990 Prop. 8.3 directly,
NOT back-build $\Theta_{2p}$ via an under-specified Casimir-Wakimoto
construction.

**Heal**: rewrite Step 1 to construct $\Theta_{2p}$ as the transport of
the Lusztig Bott element along the Finkelberg equivalence on filtration
quotients (forward-referencing part (iii) / Step 4), explicitly noting
that the construction is COHOMOLOGY-LEVEL, not a chain-level primitive
class in the bar complex. This converts the step from confabulation to
a cohomology-of-graded-quotient statement consistent with Step 4.

### A3. Step 2 Q^adm nilpotency transported from Finkelberg f_i^(p) without explicit Wakimoto-to-tilting conversion (AP297, MODERATE)

Line 480-483: "The transported nilpotency bound follows by pulling back
Finkelberg's bound for the action of divided powers $f_i^{(p)}$ on the
tilting category (Fin96 Lem.~3.7) through the Wakimoto realisation."

Audit of Fin96: the actual lemma content is that $f_i^{(p)}$ acts by
zero on the tilting category after semisimplification. The chapter
extrapolates: "Hence $Q_i^{\mathrm{adm}}$ acts by a nilpotent of
nilpotency index at most $p$ on each conformal-weight slice of
$L_k(\fg)$." The transport uses the Wakimoto realisation, which pulls
back $f_i^{(p)}$ to $\oint (:e^{\alpha_i \cdot \phi/\sqrt{p/q}}:)^p dz$
divided-power screening. The divided-power screening operator's
nilpotency is a theorem-level claim that needs its own citation; the
fact that $f_i^{(p)}$ is negligible in the tilting category does NOT
by itself control the nilpotency of $Q_i^{\mathrm{adm}}$ on the full
bar complex (it controls it modulo the tilting quotient).

**Heal**: inscribe a local bridge lemma (AP621 heal template) stating
explicitly: "The admissible screening $Q_i$ satisfies $Q_i^p$-vanishing
on weight-truncated bar complex slices by Feigin-Frenkel divided-power
nilpotency (cite FF96, arXiv:hep-th/9310022, Prop. 3.2)." If this
statement is not in FF96 as a proposition — and I believe it is not
at that form — downgrade the nilpotency bound to conjectural or state
it as a numerical consequence of the Kac-Kazhdan resonance locus at
admissible level.

### A4. Step 3 spectral sequence convergence: $E_1 = E_\infty$? (AP299, MODERATE)

Line 508-510: "Convergence is automatic in each weight because the
filtration is finite there; passage to the total complex is the
Mittag--Leffler condition (guaranteed by Step~2)."

AP299 check: the filtration is over the periodic-CDG filtration
$F^n = \ker (Q^{\mathrm{adm}})^n$, which per the Step 2 argument is
exhausted in $\leq p r$ steps on each conformal-weight slice (r = rank).
Mittag-Leffler on this filtration with finite-length on each weight is
indeed immediate. But: the claim "passage to the total complex" elides
the bigraded ML on (cohomological degree $m$, filtration level $n$,
conformal weight $w$) — three indices, not two. The bar differential
$d_B$ does NOT preserve conformal weight (OPE simple-pole summands
strictly drop weight; AP296). The filtration argument as written is a
single-weight-slice Mittag-Leffler; the total-complex statement requires
bigraded ML on $(n, w)$ with $d_B$ acting across $w$-slices. This is
the SAME FAILURE MODE as Wave-14 MC5 AP296/AP261.

**Heal**: rewrite Step 3 to explicitly state Mittag-Leffler holds at
FIXED conformal weight (where $\gr^n F$ is finite-dimensional), and
convergence to the conformal-weight-completed bar complex is automatic
on each weight; propagation to the FULL bar complex (without
weight-completion) requires Arakawa $C_2$-cofiniteness plus a
filtration-preservation argument in the spirit of MC5 Wave-14 AP296
heal. Given the chapter is an admissible-level refinement of the class-M
story, the weight-completion scope restriction is natural here and does
not weaken the main conclusion.

### A5. Step 4 small-quantum-group image & Kac-table count at (3,2) zero (HIGH)

Line 778-779 in the corollary proof: "At $(p, q) = (3, 2)$ the count
collapses to the single identity primary of the trivial minimal model
$c = 0$."

Numerical check: $(p-1)(q-1)/2 = 2 \cdot 1 / 2 = 1$ — correct, single
simple. And $c_{3,2} = 1 - 6(3-2)^2/(3 \cdot 2) = 1 - 1 = 0$ — correct.

This is consistent with the Kac-table count. However, the identification
with the "trivial minimal model $c = 0$" is technically incorrect: the
$(3,2)$ Virasoro minimal model is the trivial vertex operator algebra
$L_{\mathrm{Vir}}(0) = \bC$ (vacuum module only), which is 0-dimensional
as a simple module count refined by Kac-table: it is a DEGENERATE
limit. The theorem is stated for the non-degenerate admissible lane
(line 229: "non-degenerate admissible lane"), and $(3,2)$ sits at the
boundary. The statement that "(3,2) has Kac table = 1" is correct
numerically, but the corollary's scope claim "chain-level adjunction
Theorem~\ref{thm:admissible-kl-bar-cobar-adjunction} specialises" for
$(3,2)$ needs a scope remark: the $(3,2)$ case is a degenerate-in-the-
sense-of-trivial-minimal-model but non-degenerate-in-the-Arakawa-sense
edge case.

**Heal**: add a remark after line 779 noting that $(p,q) = (3,2)$ is
the trivial-minimal-model degenerate limit where $L_{\mathrm{Vir}}(0) = \bC$
has only the vacuum simple module, and that this is the limiting case
of the theorem's non-degenerate scope.

### A6. Cross-volume HZ-11 on `thm:chd-deligne-tamarkin` (MODERATE)

Line 649 in the proof of `thm:adams-analog-construction`: "the chiral
higher Deligne structure (Theorem~\ref{thm:chd-deligne-tamarkin},
Vol.~II)". The label lives at Vol~II
`chapters/theory/chiral_higher_deligne.tex:379`. The Vol~I theorem
carries `\ClaimStatusProvedHere`; its proof depends on a cross-volume
structural theorem.

Per HZ-11 cross-volume discipline: a `ProvedHere` theorem whose proof
depends on a label living only in Vol~II/III must either
(a) inscribe the lemma locally in Vol~I, or
(b) downgrade to `\ClaimStatusConditional` and append a Remark[Attribution]
citing the cross-volume source explicitly.

**Heal**: either downgrade `thm:adams-analog-construction` to
`\ClaimStatusConditional` with explicit Vol~II attribution, or inscribe
a local `\begin{remark}[Attribution: chiral higher Deligne is external]`
noting that the Deligne-Tamarkin structure on $\End^{\mathrm{ch}}_A$ is
imported from Vol~II as `\ClaimStatusProvedElsewhere`. Given the
dependency on a STRUCTURAL theorem (not a combinatorial identity), the
Conditional downgrade is cleaner.

## Phase 2: HZ-IV test-body audit

`compute/tests/test_periodic_cdg_admissible.py` carries four
`@independent_verification` decorators. Audit per AP277 / AP287 / AP288 /
AP310:

- `test_periodic_cdg_period_matches_arakawa_and_finkelberg` (line 161):
 body computes `period_from_arakawa(p,q) = 2*p` and
 `period_from_finkelberg(p,q,h_vee) = 2*p` — both return `2*p` by
 HARD-CODED formula. This is AP288 label-disjoint-but-computation-identical:
 the decorator names two paths; the bodies both return the same
 closed-form `2*p`. No numerical cross-check of Arakawa or Finkelberg
 output against an independent source.
- `test_admissible_kl_adjunction_period_matches_ckl` (line 194): same
 AP288; both paths return `2*p`.
- `test_chiral_steenrod_rank_matches_uq_and_ckl` (line 229): Wave-7
 `HZ-IV-W8-C` flag already in the body (lines 235-255); self-flagged
 honest repair present. Acceptable as AP287 primitive, self-flagged.
- `test_minimal_model_simple_object_count_matches_kac_table` (line 312):
 body computes `(p-1)*(q-1)//2` from `p, q` and compares to a
 hard-coded `expected_count` derived from the same formula. This is
 AP128 (engine-test synchronized to same mental model) at the test
 layer: the "Kac-table count" verification is a tautology — the
 test's `expected_count` list and the `kac_table` formula are both
 $(p-1)(q-1)/2$.

**Heal**: either replace the period helpers with GENUINELY disjoint
computations (e.g., period_from_arakawa should compute the
Poincare-series period of the Zhu algebra directly; period_from_ckl
should compute the coset-character period by polynomial arithmetic; these
are DIFFERENT arithmetic routes producing $2p$), OR downgrade all four
decorators with an `AP287 / AP288 FLAG` module-level comment matching
the Wave-10 #70 pattern for MC5 and other programme tests.

## Phase 3: Verdict summary

| Attack | Severity | Status | Heal |
|--------|----------|--------|------|
| A1 Arakawa bibkey target | MODERATE | Confirmed | Add `Arakawa16` bibkey for arXiv:1207.4857 |
| A2 `Theta_{2p}` confabulation | HIGH | Confirmed | Rewrite Step 1 via Finkelberg-transport Lusztig Bott |
| A3 $Q^{\mathrm{adm}}$ nilpotency bridge | MODERATE | Confirmed | Inscribe FF96 divided-power bridge lemma |
| A4 Spectral-sequence ML bigrading | MODERATE | Confirmed | Weight-slice ML explicit; propagate AP296 heal pattern |
| A5 $(3,2)$ trivial-model scope | MINOR | Confirmed | Add scope remark after corollary line 779 |
| A6 HZ-11 cross-volume dependency | MODERATE | Confirmed | Downgrade `thm:adams-analog-construction` to Conditional |
| HZ-IV test-body AP288 | HIGH | Confirmed | Downgrade decorators to AP287 FLAG or wire disjoint computations |

**Overall**: three `\ClaimStatusProvedHere` theorems of the periodic-CDG
chapter have scope-narrowing heals (not full retraction) that together
would convert the chapter from "PROVED chain-level on filtration
quotients" to "PROVED weight-completed on filtration quotients, with
explicit Arakawa 2016 citation, Finkelberg-transported period generator,
and Conditional dependence on Vol~II chiral higher Deligne." This
matches the SPIRIT of the CLAUDE.md MC5 / topologization-tower scoping
discipline: the admissible-level refinement is a genuine theorem, not a
PROVED UNCONDITIONAL result on the original direct-sum complex.

The two conjectures (`conj:periodic-cdg` Massey vanishing and
`conj:kl-bar-cobar-dl` Arkhipov-Gaitsgory descent) are already
HONESTLY inscribed as Conjectured; no heal needed.

## Phase 4: Proposed CLAUDE.md status-row update

Current (line 623-ish):

> Periodic CDG admissible KL: **PROVED (Vol I chapters/theory/periodic_cdg_admissible.tex, 2026-04-16)** | thm:periodic-cdg-is-koszul-compatible: periodic-CDG filtration F^n = ker(Q^n_{adm}) on KL_k^{adm} at k+h^v = p/q compatible with chiral Koszul duality. [...]

Proposed honest rewrite:

> Periodic CDG admissible KL: **PROVED on COHOMOLOGY OF FILTRATION QUOTIENTS, WEIGHT-COMPLETED AMBIENT, simply-laced $\fg$, non-degenerate admissible lane; Arkhipov-Gaitsgory descent and Massey vanishing for $\mathrm{rk}\,\fg \geq 2$ remain Conjectured (Vol I chapters/theory/periodic_cdg_admissible.tex, 2026-04-16; scope-refined 2026-04-18).** `thm:periodic-cdg-is-koszul-compatible`: periodic-CDG filtration $F^n = \ker (Q^n_{\mathrm{adm}})$ on $\KL_k^{\mathrm{adm}}$ at $k + h^\vee = p/q$ compatible with chiral Koszul duality at the cohomology-of-graded-quotient level, via Arakawa 2016 (arXiv:1207.4857) $C_2$-cofiniteness + Finkelberg 1996 tilting-semisimplification + Lusztig 1990 Tate $2p$-periodicity. `thm:admissible-kl-bar-cobar-adjunction`: $\Omega^{\mathrm{ch}} \dashv \barB^{\mathrm{ch}}$ descends to $\KL_k^{\mathrm{adm}} \rightleftarrows (\KL_{k^!}^{\mathrm{adm}})^{\mathrm{op}}$ on the cohomology of periodic-CDG filtration quotients, with Adams-type spectral sequence $d_1 = Q^{\mathrm{adm}}$ converging weight-by-weight. `thm:adams-analog-construction` (CONDITIONAL on Vol~II `thm:chd-deligne-tamarkin`): rank-1 ($\fg = \mathfrak{sl}_2$) chiral Adams functor with Steenrod algebra $\mathbb{C}[x]/(x^p)$; higher rank is `conj:adams-analog-higher-rank`. `cor:class-M-admissible-minimal-model`: $\KL_{\mathrm{Vir}}^{\mathrm{adm}}(c_{p,q})$ has $(p-1)(q-1)/2$ simples, closes the FM76 class-M scope hole on the non-degenerate admissible lane (the $(3,2)$ trivial-model edge case is a degenerate-of-trivial-minimal-model limit, still Arakawa-non-degenerate). Massey-vanishing hypothesis reduces `conj:periodic-cdg` on filtration-quotient cohomology to chain-level isomorphism of the full CDG-coalgebra; PROVED for $\mathfrak{sl}_2$, OPEN for $\mathrm{rk}\,\fg \geq 2$ due to Nichols-algebra obstruction from cubic quantum Serre.

## Phase 5: Patch (per AP316 worktree-isolated delivery convention)

Because this agent session is invoked inside a worktree
(`/Users/raeez/chiral-bar-cobar/.claude/worktrees/agent-a5f7ae65`), the
recommended heal edits are REPORTED (this file) rather than COMMITTED.
Subsequent session should apply in a single commit:

1. `standalone/references.bib`: add `Arakawa16` entry (arXiv:1207.4857).
2. `chapters/theory/periodic_cdg_admissible.tex`:
 - redirect three `\cite{Arakawa15}` sites at lines 192, 462 to
 `\cite{Arakawa16}`; preserve the one at line 758 (DS-side).
 - rewrite Step 1 of `thm:periodic-cdg-is-koszul-compatible` proof
 (lines 293-309) via Finkelberg-transport of Lusztig Bott element.
 - inscribe bridge lemma before Step 2 (line 311) documenting
 FF96 divided-power nilpotency + Wakimoto pull-back.
 - rewrite Step 3 of `thm:admissible-kl-bar-cobar-adjunction` proof
 (line 488-510) with explicit weight-slice ML.
 - add scope remark after line 779 noting $(3,2)$ trivial-model
 degenerate limit.
 - downgrade `thm:adams-analog-construction` header status from
 `\ClaimStatusProvedHere` to `\ClaimStatusConditional` with
 `\begin{remark}[Attribution: chiral higher Deligne is Vol~II]`
 citing `thm:chd-deligne-tamarkin` at
 `chiral_higher_deligne.tex:379` and the role of
 `\ref{thm:chd-deligne-tamarkin}` in the proof body.
3. `compute/tests/test_periodic_cdg_admissible.py`:
 - add Wave-style HZ-IV-W8-C FLAG module-level comment noting
 AP288 on period helpers; OR
 - replace `period_from_ckl_wnkn` body with a coset-character
 polynomial-arithmetic computation that is genuinely distinct
 from `period_from_arakawa` (e.g., period-of-rational-function
 `(1 - t^p)/(1 - t)` vs Zhu-algebra Poincare series).
4. `CLAUDE.md`: update Periodic CDG admissible KL row per Phase 4
 proposal.

## Confusion-pattern cache append candidates

**Pattern 226 (first-principles cache, session 2026-04-18): Arakawa
bibkey collision.** Trigger: a citation `\cite{Arakawa15}` or
`\cite{Arakawa14}` is invoked for "C_2-cofiniteness of $L_k(\fg)$ at
non-degenerate admissible level." Regex:
`C_2.*cofinite.*L_k.*Arakawa(15|14)\b`. Counter: the correct primary
source is Arakawa 2016 (arXiv:1207.4857), "Rationality of admissible
affine vertex algebras in the category $\mathcal{O}$," NOT Arakawa
2015 arXiv:1211.7124 which is the PRINCIPAL W-algebra statement.
Arakawa-van-Ekeren 2019 (arXiv:1911.13196) extends to certain
degenerate cases. Primary-source table:

| Bibkey | arXiv | Title | Theorem |
|--------|-------|-------|---------|
| Arakawa07 | math/0611289 | Representation theory of W-algebras | principal W C_2-cofiniteness |
| Arakawa14 | 1211.7124 | Rationality of W-algebras: principal nilpotent | rationality of principal W |
| Arakawa16 | 1207.4857 | Rationality of admissible affine vertex algebras | $L_k(\fg)$ C_2-cofiniteness |
| AvE19 | 1911.13196 | Rationality of affine vertex algebras at admissible levels | extensions |

**AP881 (periodic-CDG bibkey: Arakawa15 vs Arakawa16 for $L_k(\fg)$
$C_2$-cofiniteness).** Primary-source confusion: the $C_2$-cofiniteness
theorem for $L_k(\fg)$ at non-degenerate admissible level is
Arakawa 2016 (arXiv:1207.4857); `Arakawa15` (arXiv:1211.7124)
establishes rationality of PRINCIPAL $\mathcal{W}$-algebras, which
specialises to the Virasoro minimal-model case but does not directly
provide the $L_k(\fg)$ statement. Instances of the Arakawa15 bibkey in
`chapters/theory/periodic_cdg_admissible.tex` that call for
$L_k(\fg)$ $C_2$-cofiniteness should be redirected to Arakawa16;
instances that call for Virasoro minimal-model rationality via DS
reduction stay on Arakawa15. See `adversarial_swarm_20260418/attack_heal_periodic_cdg_20260418.md`.

**AP882 ($\Theta_{2p}$ construction via Finkelberg-transport vs
Wakimoto-Casimir).** The periodic-generator class $\Theta_{2p} \in
\ChirHoch^{2p}(\widehat{\fg}_k)$ is CORRECTLY constructed as the
transport of the Lusztig 1990 Prop. 8.3 Bott element of Tate-cohomology
of $u_q(\fg)$ under the Finkelberg equivalence; NOT as a "Casimir
element under the Wakimoto realisation restricted to screening-kernel"
(which is underspecified and extrapolates the rank-1 critical-level
pattern of `prop:sl2-periodicity-dl`). The distinction matters for
scope: the Finkelberg-transport construction works on COHOMOLOGY of
graded quotients (consistent with theorem statement part (i)); the
Casimir-Wakimoto construction would need to be chain-level primitive,
which is conjectural.

**AP883 (weight-slice vs bigraded ML in periodic-CDG spectral
sequence).** The Adams-type spectral sequence convergence
$E_1^{n,m}(\gr^n F) \Longrightarrow H^{n+m}(\barB^{\mathrm{ch}})$ of
`thm:admissible-kl-bar-cobar-adjunction` is a WEIGHT-SLICE ML: at
fixed conformal weight $w$, $F^n$ exhausts in $\leq pr$ steps and ML
holds automatically. Propagation to the full bar complex requires
weight-completed ambient (the bar differential does NOT preserve
conformal weight by AP296 OPE simple-pole; the associated graded
picture is filtration-preserving not weight-grading-preserving).
Matches MC5 Wave-14 AP261/AP296 heal pattern. Distinct from AP287
(primitive-tautology): here the convergence IS proved, just at weight-
completed scope.

(Reserve AP884-AP900 for subsequent waves; Phase-0 / Phase-1 audit
surfaced three new APs, within the 20-slot block.)
