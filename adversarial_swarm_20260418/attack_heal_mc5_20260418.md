# Attack-and-heal: MC5 class M chain-level on the original complex

**Date:** 2026-04-18
**Target:** `chapters/theory/mc5_class_m_chain_level_platonic.tex`
**Status table row:** Vol I MC5 — "PROVED on THREE equivalent ambients of the original complex"
**Mission author:** Raeez Lorgat

## Summary

Adversarial attack on the MC5 class-M chain-level Platonic reconstitution
inscribed in Vol I surfaces one load-bearing defect in the Step 3
Mittag–Leffler argument of `thm:mc5-class-m-chain-level-pro-ambient`. The
defect is a silent weight-grading-vs-weight-filtration conflation: the
proof claims the bar differential "preserves total conformal weight"
and uses that claim to decompose the bar complex as a product over
weights, whereas the load-bearing source of truth
(`eq:bar-weight-preservation` in `prop:standard-strong-filtration`)
establishes only weight-WEAKLY-DECREASING behaviour
($d_{bar}(F_{\leq w} C_N) \subset F_{\leq w} C_N$, not
$d_{bar}(F_{=w} C_N) \subset F_{=w} C_N$). The product decomposition
fails on the raw bar complex; it holds only on the associated graded.

The theorem conclusion survives. The ML condition is rescued by the
finite-dimensional route: each $\cA_{\leq N}$ is finite-dimensional, so
$H^m(C_N)$ is finite-dimensional, so the tower of finite-dimensional
images automatically satisfies Mittag–Leffler. A companion backup route
via clause (iv) filtration-piece stabilisation is recorded alongside.

No downgrade. No change to the status tag. The defect was an
intermediate-route error; the theorem is correct.

The other three attack directions (ambient equivalence, invertibility
of finite-stage homotopy, direct-sum-counterexample persistence) are
refuted: ambient equivalence is sound, the finite-stage homotopy is
well-defined at every generic $c$ (minimal-model and admissible loci
are excluded by the chapter scope statement), and the $S_4 \neq 0$
classes persist in both ambients and are matched by the comparison
map. These attack directions yield no heal requirement.

## Attack directions

### Attack 1. Ambient-equivalence begs the question?

**Claim under attack.** The three ambients (pro-object,
$J$-adic topological, weight-completed) are mathematically equivalent;
the MC5 theorem proved in any one is the MC5 theorem in all three.

**Finding.** Sound. `prop:ambient-equivalence` constructs three
functor pairs. The pro-to-$J$-adic direction requires the source
pro-object to be Mittag–Leffler; in the chiral bar case this holds by
the finite-dimensional route (Attack 2 below). The $J$-adic-to-pro
direction is well-defined because the filtering ideal
$J = \bigoplus_{h>0} \cA_h$ is finitely generated on the weight-graded
algebra. The $J$-adic-to-filtered direction is tautological under the
identification $F^N = J^{(N)}$. All three ambients are three
presentations of one category.

**Verdict.** No defect. The three-way framing is honest.

The only residue is aesthetic: the Platonic theorem is really one
statement with three names. This is already acknowledged in
`rem:ambient-convention` at line 626–644.

### Attack 2. Finite-stage homotopy invertibility

**Claim under attack.** The finite-stage contracting homotopy
$h_N = \sum_{j=1}^{\lfloor N/2 \rfloor} h \cdot m_0^{j-1}$ absorbs the
harmonic discrepancy at every genus $g \geq 0$ and every class-M
algebra.

**Check at edge cases.**

- $c = 0$ (trivial Virasoro). $S_4(\mathrm{Vir}_0) = 10/[0 \cdot 22]$
  is undefined. This central charge is excluded by the chapter scope
  statement (line 119–125: "Virasoro $\mathrm{Vir}_c$ at generic $c$
  (outside the minimal-model and admissible loci)"). The minimal
  $(p,q) = (2,3)$ model includes $c = 0$.
- $c = -22/5$ ($(p,q) = (2,5)$ Lee–Yang). $S_4$ has a pole. Excluded
  by "admissible loci" in the scope statement.
- $c = 13$ (Virasoro self-dual). $S_4 = 10/(13 \cdot 87) = 10/1131$,
  finite and nonzero. Homotopy well-defined.
- $c = 26$ (ghost). $S_4 = 10/(26 \cdot 152) = 10/3952$, finite.
  Homotopy well-defined.

**Verdict.** The finite-stage homotopy is well-defined at every
generic $c$ in the chapter's scope. The excluded loci are already
excluded. No defect.

### Attack 3. Mittag–Leffler at fixed cohomological degree

**Claim under attack.** Step 3 of the proof argues ML by bigrading
$(m, w)$ and claiming the bar complex decomposes as a product over
conformal weights $w$.

**First-principles check.** The source of truth for the bar
differential's weight behaviour is
`prop:standard-strong-filtration` at
`bar_cobar_adjunction_curved.tex:1116`. The OPE formula
\[
\operatorname{wt}(a_{(n)} b) = \operatorname{wt}(a) + \operatorname{wt}(b) - n - 1,
\qquad n \geq 0,
\]
gives $\operatorname{wt}(a_{(n)} b) < \operatorname{wt}(a) + \operatorname{wt}(b)$
whenever $n \geq 1$. Equation (1218) records this as
$d_{\mathrm{bar}}(F_{\leq w} C_N) \subset F_{\leq w} C_N$. The bar
differential is weight WEAKLY-DECREASING, not weight-preserving.

**Consequence.** The decomposition
$\bar B^{\mathrm{ch},(g)}(\cA_{\leq N}) = \prod_w \bar B^{\mathrm{ch},(g)}(\cA_{\leq N})_w$
as chain complexes is FALSE on the raw bar complex. It holds only on
the associated graded
$\operatorname{gr}^\bullet \bar B^{\mathrm{ch},(g)}(\cA_{\leq N})$.

The Step 3 argument of the Wave-5 rewrite was routed through this
false decomposition. The ML invocation at fixed $m$ was then argued
as "product of $(m,w)$-bigraded stabilisations", which requires the
decomposition to hold. This is the load-bearing defect.

**Rescue.** ML holds at fixed $m$ by a different route. Each
$\cA_{\leq N}$ is finite-dimensional
(`prop:standard-strong-filtration(ii)`). Bar words at cohomological
degree $m$ have bounded bar length $r$ in each genus (by the
genus-$g$ conformal-weight budget of the factorisation structure),
so $H^m(C_N)$ is finite-dimensional. The tower of images
$\operatorname{im}(H^m(C_{N+k}) \to H^m(C_N))$ is a decreasing
sequence of finite-dimensional subspaces of a finite-dimensional
vector space, hence stabilises for $k$ large. This is the ML
condition (Weibel 1994 Prop 3.5.7).

A backup route refines `prop:standard-strong-filtration(iv)`: the
filtration piece $F_{\leq w} C_N$ stabilises at $N \geq w$, so the
induced filtration on $H^m(C_N)$ has stable pieces at every $w$.
Exhaustion of the filtration on each finite-dimensional $C_N$
collapses the intersection of transition images to a
finite-dimensional limit.

**Verdict.** Load-bearing defect in the ROUTE (not the conclusion).
Healed by replacing the weight-preservation-as-decomposition argument
with the finite-dimensional ML route; backup via filtration-piece
stabilisation recorded alongside.

Honest attribution of the bar differential's weight behaviour is now
inscribed as `rem:mc5-honest-weight-filtration` following Step 3.

**Related discipline.** The shadow obstruction tower for class M does
not terminate (`cor:virasoro-postnikov-nontermination`), so the
filtration spectral sequence has nonzero differentials on every page.
This does NOT obstruct the pro-ambient ML conclusion, which is
secured by the finite-dimensional route, not by spectral-sequence
collapse. The honest remark makes this clear.

### Attack 4. Direct-sum counterexample persistence

**Claim under attack.** $S_4(\mathrm{Vir}_c) = 10/[c(5c+22)]$ is a
nonzero weight-4 bar-cohomology class whose existence forces "direct-sum
chain-level MC5 class M" to be false. Does it persist in the
pro-ambient?

**Check.** At finite stage $N \geq 4$, the weight-4 bar complex of
$\bar B(\mathrm{Vir}_{c, \leq N})$ is finite-dimensional and has a
class representing $S_4$. The comparison $f_g^{(\leq N)}$ between BV
and bar sides is strict at this stage (Step 1): both sides carry the
class, and $f_g^{(\leq N)}$ matches them. The class persists in both
and is paired by the comparison.

The "direct-sum failure" is NOT that the class exists but that an
INFINITE PRODUCT of classes (one for each $r \geq 4$) cannot be
represented as a bounded bar-word in $\mathrm{Ch}(\mathrm{Vect})$; in
the pro/J-adic/weight-completed ambient, the inverse limit
accommodates the unbounded product.

**Verdict.** The obstruction in $\mathrm{Ch}(\mathrm{Vect})$ is to
bounded direct-sum representability of an infinite product of classes,
not to the existence of each class individually. The pro-ambient
accommodates the product. No defect in the pro-ambient claim.

## Heals inscribed

1. **Step 3 rewrite** in `mc5_class_m_chain_level_platonic.tex:303–392`.
   The weight-preservation-as-decomposition argument is replaced by a
   finite-dimensional ML route (Route (a)) with a filtration-piece
   backup (Route (b)). The theorem statement at line 251–256 is
   refreshed to name finite-dimensionality of the stage cohomologies
   as the ML mechanism.

2. **`rem:mc5-honest-weight-filtration`** added after Step 3. Records
   that the bar differential is weakly weight-decreasing (filtration
   preservation) not weight-preserving (grading preservation); that
   the product decomposition holds only on the associated graded; and
   that the class-M spectral sequence nontermination
   (`cor:virasoro-postnikov-nontermination`) does not obstruct the
   pro-ambient ML conclusion.

3. **CLAUDE.md MC5 row** annotated with the Wave 12b heal record. The
   row's headline theorem status is unchanged.

## Propagation audit

Grep across the three volumes:

```
grep -rn 'thm:mc5-class-m-chain-level-pro-ambient\|thm:mc5-class-m-topological-chain-level-j-adic' \
  /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups
```

Consumer files carrying `\ref{thm:mc5-class-m-chain-level-pro-ambient}` or
`\ref{thm:mc5-class-m-topological-chain-level-j-adic}`:

- Vol I: `chapters/frame/preface.tex`, `chapters/theory/mc5_genus0_genus1_wall_platonic.tex`
- Vol II: `chapters/frame/preface.tex`, `chapters/theory/chiral_higher_deligne.tex`, `main.tex` (include directives only)
- Vol III: `chapters/theory/phi_universal_trace_platonic.tex`

The heal changes only the Step 3 internal route; the theorem statement
(pro-object chain-level qi with ML in every cohomological degree) is
unchanged. Consumer references remain valid. No consumer-side edits
required.

`thm:completed-bar-cobar-strong` (Vol I `bar_cobar_adjunction_curved.tex`)
and `prop:bv-bar-class-m-weight-completed` (Vol II `bv_brst.tex`) are
untouched; their statements are independent of the pro-ambient route.

## Test suite status

`compute/tests/test_mc5_class_m_chain_level_platonic.py` carries three
HZ-IV decorators with symbolic bodies (AP287 structural-impossibility
primitive tautology pattern). The test bodies do not check the
weight-decomposition claim; they check Mittag–Leffler stabilisation
abstractly and homotopy-sum truncation symbolically. The heal does
not invalidate any existing test; the test file's `_mittag_leffler_stabilises`
stub returns `True` once enough stages are present, consistent with the
finite-dimensional route. No test updates required.

## Epistemic status after heal

`thm:mc5-class-m-chain-level-pro-ambient`: `\ClaimStatusProvedHere`
preserved. The chain-level qi conclusion holds via:

- Step 1 (finite-stage strict qi via harmonic-absorbing homotopy
  $h_N$): unchanged, sound at generic $c$.
- Step 2 (tower compatibility via
  `prop:standard-strong-filtration(iv)`): unchanged, sound.
- Step 3 (ML via finite-dimensionality): REWRITTEN. Correct route.
- Step 4 (pro-qi from Steps 1-3): unchanged.

`cor:mc5-class-m-chain-level-on-inverse-limit`: `\ClaimStatusProvedHere`
preserved. The Milnor exact-sequence argument is unaffected by the
Step 3 heal.

`prop:ambient-equivalence`: `\ClaimStatusProvedHere` preserved. The
functorial equivalence of the three ambients is sound.

`thm:mc5-class-m-topological-chain-level-j-adic`: `\ClaimStatusProvedHere`
preserved. Its ML invocation routes through
`thm:mc5-class-m-chain-level-pro-ambient` Step 3, now via the healed
finite-dimensional route.

## Build / test verification

The repository environment at audit time does not include a `pdflatex`
binary, so `make fast` is not runnable in-session. The edits were
validated via the following structural checks:

- `\begin{…}` / `\end{…}` balance in `mc5_class_m_chain_level_platonic.tex`:
  26 / 26 (balanced).
- No `\end{…>` or `\begin{…>` typo (FM7 discipline).
- No em-dashes (AP29 / AP41 discipline).
- No AI-slop tokens (HZ-10 discipline).
- Label `rem:mc5-honest-weight-filtration` unique across all three
  volumes.
- `\cite{Weibel94}` resolves (defined at
  `standalone/references.bib:897`).

`make fast` and `make test` must be run in a TeX-equipped environment
before any commit. The audit file records this constraint for the
committer.

## Attribution

All inscriptions authored by Raeez Lorgat.
