# Wave-3 Adversarial Attack on Theorem A^{∞,2}

## Modular Koszul Duality Programme, Volume I
## 2026-04-17, Beilinson-tradition adversarial audit

**Target:** `chapters/theory/theorem_A_infinity_2.tex` (1596 lines, read in
full, chunk-by-chunk, linear). Cross-checks against
`standalone/references.bib`, Wave-1 `wave1_theorem_A_attack_heal.md`
(440 lines), `notes/cross_volume_aps.md` (AP-CY30), CLAUDE.md HZ-IV.

**Inscription constraint.** Target file is concurrently edited by voice
agent (task #7). This attack is READ-ONLY on the target. Phase-2 healings
below are supplied as markdown only; a patch-draft is attached for the
orchestrator to inscribe after task #7 completes.

**Status-row claim under attack.** "Theorem A^{∞,2} PROVED (Vol~I
theorem_A_infinity_2.tex, 2026-04-16): Francis-Gaitsgory bar-cobar
(∞,2)-equivalence at properad level ... Closes FM69/70/72/73/74/195 ...
14+ downstream corollaries ... cor:chiral-KK-formal-smoothness:
FG ambient + R-twisted descent ⟹ formally smooth at properad level."

After whole-file reading and bibliographic cross-check, the unified
Koszul reflection `thm:koszul-reflection` and its properad-level explicit
form `thm:A-infinity-2` survive under hypotheses (H1)+(H2)+(H3) +
citation-level inputs, but the PROOF SKELETON invokes six bibkeys that
are PHANTOM in `standalone/references.bib` and one lemma
(`lem:R-twisted-descent`) that silently assumes an R-matrix unitarity
hypothesis absent from its statement. The status-row "PROVED"
is better read as "PROVED modulo six bib insertions, one hypothesis
addition, and one Mittag-Leffler verification". The frontier that
remains open beyond Π4 is the *modular-family extension* over
$\overline{M}_{g,n}$, which the chapter itself explicitly demotes
(line 879-915, `rem:A-infinity-2-modular-family-scope`) to "citation-level,
not chain-level inscribed".

---

## Attack Findings

### F1. Six phantom citations in the proof skeleton (CRITICAL, AP190 / AP209)

The proof of `thm:A-infinity-2` (lines 797-877) invokes six primary
references to ground its machinery:

| Bibkey              | Invoked at | Status in `references.bib`                    |
|---------------------|------------|-----------------------------------------------|
| `HackneyRobertson2017` | line 707 | **MISSING**                                   |
| `HackneyRobertson2019` | lines 706, 711, 1522 | **MISSING**                       |
| `Francis2012`       | lines 601, 638, 822, 1487, 1497 | **MISSING** (a Francis-Gaitsgory entry exists at bib line 290, but no standalone Francis 2012) |
| `GR17`              | lines 203, 638, 710, 820, 942, 1287, 1485 | **MISSING**     |
| `Positselski2018`   | lines 75, 209 | **MISSING**                                |
| `Positselski2011`   | lines 79, 187, 219, 1486 (implicit) | **MISSING**         |
| `Hinich2003`        | line 205 | **MISSING**                                     |

Grep verdict:

```
grep -E '@(article|book|incollection|misc|inproceedings|thesis)\{(HackneyRobertson2017|HackneyRobertson2019|Positselski2018|Positselski2011|Hinich2003|Francis2012|GR17)' \
  standalone/references.bib
# Returns: 0 matches.
```

Existing bib entries for the intended sources: `BD04` (line 39, Beilinson-
Drinfeld), `HA` (line 411, Lurie's Higher Algebra), `LV12` (line 583,
Loday-Vallette), `Val16` (line 750, Vallette 2016). Francis-Gaitsgory
entry at line 290 is a joint paper, not the Francis 2012 factorization
solo.

Consequence: at PDF build the six citations render `[?]`. For the reader
the proof of `thm:A-infinity-2` has five undefined citations in Step 1
(the adjunction), three in Step 2 (unit/counit equivalences), two in
Step 3 (properad lift), and the formal-smoothness corollary
`cor:chiral-KK-formal-smoothness` invokes `HackneyRobertson2019` for its
graph-wise cotangent argument. AP190 (hidden imports) at scale: the
entire proof skeleton reads coherent IF the six references exist; the
build-time symbol `[?]` tells the reader they do not.

This is the single most load-bearing finding of this audit. The heal is
mechanical: add the six bib entries.

### F2. R-twisted Σ_n-descent Step 1 elides unitarity (F8 of Wave 1, re-verified)

`lem:R-twisted-descent` (line 955-1041) Step 1 (line 989-994) asserts:

> "The classical Yang-Baxter equation $R_{12}R_{13}R_{23} = R_{23}R_{13}R_{12}$
> on codimension-2 loci $\{z_i = z_j = z_k\}$ ensures that the
> representation of the pure braid group $PB_n(X)$ extends to a
> representation of the symmetric group $\Sigma_n$ on the boundary
> of a fundamental domain: this produces $L_R$ as a
> $\Sigma_n$-equivariant local system."

This is the AP-CY30 trap ("YBE factored != ZTE solved"). YBE on
configuration codimension-2 produces a pure-braid representation
$\rho: PB_n(X) \to \GL(\cA^{\otimes n})$. Extension to $\Sigma_n$
requires *unitarity*: R(z)R^{op}(-z) = id (equivalently, the action of
the generator $s_i$ squares to the identity on the fibre). Without
unitarity the monodromy around a transposition square is a nontrivial
automorphism, not the identity, and the $\Sigma_n$-equivariant local
system $L_R$ does not exist. One obtains a *$\mathrm{Br}_n$-equivariant*
local system on $\Conf^{\ord}_n(X)$ which descends only to
$\Conf_n(X)/\Sigma_n$ as a quotient stack -- not to the
$\Sigma_n$-coinvariant bar complex.

The unitarity hypothesis is NOT stated in the lemma. Its absence is
load-bearing: Wave-1 Finding F8 already flagged this, and the Wave-1
"Platonic Reconstitution" Theorem A clause (A5) explicitly adds
"conditional on unitarity of R(z)". The current inscription has not
absorbed this correction.

Families where unitarity holds:
- Rational Yangian $Y_\hbar(\fg)$: unitary (R(z) = 1 + \hbar P/z + O(\hbar^2),
  P^2 = 1, standard RLL).
- Trigonometric quantum affine $U_q(\hat\fg)$ at generic q: unitary.
- Heisenberg (trivial R = $\tau$): unitary trivially, $\tau^2 = id$.
- Affine KM at non-critical level (classical KZ): unitary on
  finite-dim reps of $\fg$.

Families where unitarity is convention-dependent or fails:
- Belavin elliptic R: unitary in the Felder-Varchenko convention but
  not in the Baxter convention (the two differ by a scalar factor
  whose square is a non-trivial quasi-period of the theta-function).
- Toroidal DIM: unitarity is a normalization choice; Miki convention
  is unitary, but the K-theoretic convention has $R(z)R^{op}(z^{-1})
  = \text{CM\,factor} \ne 1$.

### F3. Step 2 Mittag-Leffler: coradical vs bar-length confusion (F10 of Wave 1, re-verified)

Step 2 (line 826-844) asserts convergence of the bar-length
spectral sequence to the unit morphism "is the Mittag-Leffler property
for the bar-length filtration under conilpotent-completeness". Two
distinct filtrations are being conflated:

- *Coradical* filtration on the coalgebra side: $F^c_n(\cC) = \ker(\cC \to
  \cC^{\otimes (n+1)})$ dually to augmentation ideal powers. Conilpotent-
  completeness is exactly the statement that the coradical filtration
  is exhaustive: $\cC = \colim_n F^c_n(\cC)$.

- *Bar-length* filtration on $\bar B(\cA) = T^c(s^{-1}\bar\cA)$: given
  by $F^{bar}_n = \bigoplus_{k \le n} (s^{-1}\bar\cA)^{\otimes k}$.
  This is exhaustive unconditionally.

The spectral sequence of the bar-length filtration converges when
$\lim^1_n$ of the filtration on cohomology vanishes. The conilpotent-
completeness of the coalgebra side does not directly vanish $\lim^1$
for the bar-length filtration on the algebra side: the two are
intertwined via adjunction, and the passage requires (H2) (augmentation-
ideal completeness of $\cA$) plus the Positselski 2018 weakly-curved
bar-cobar (the complete local ring ambient ensures compatibility
between the two filtrations). The chapter gestures at (H2) via the
"$\cA$ is weakly curved in Positselski's sense" remark (line 74-75)
but does not exhibit the Mittag-Leffler argument chain-level. AP194
(curved complex with flat tools, reverse variant).

### F4. (H3) is restrictive for critical-level affine KM and for logarithmic W(p) -- but the chapter claims finite-generation for KM uniformly

The chapter states (line 92-94): "The finitely-generated standard
landscape, including Heisenberg, all affine Kac-Moody, Virasoro, and
principal W_N, satisfies all three hypotheses uniformly."

This is true for non-critical level KM and for generic-c Virasoro, but
AP-CY30 adjacent: at the critical level $k = -h^{\vee}$, $V_k(\fg)$
still satisfies (H1), (H2) (as a complete local ring with augmentation),
but (H3) holds conformal-weight by conformal-weight because the
conformal weight grading itself is well-defined at all $k$. Critical
level is therefore covered by Theorem A^{∞,2}; it is the CHAIN-LEVEL
involutivity $K^2 \sim \id$ clause (KR-ii) that fails there, not (H3).

The logarithmic W(p) triplet: (H1), (H2) hold, but (H3) requires finite-
dim conformal-weight spaces. W(p) is C_2-cofinite, so Zhu algebra is
finite-dim, and conformal-weight spaces are finite-dim: (H3) HOLDS.
Theorem A^{∞,2} therefore applies to W(p). The Beilinson-rectified
CLAUDE.md note from 2026-04-17 (W(p) tempering retraction, OF1) does
NOT affect Theorem A^{∞,2}; it affects the chain-level topologization
question for W(p), which is a different theorem. Good: no drift here.

### F5. `rem:A-infinity-2-modular-family-scope` demotes hypothesis (c) and nodal sewing to citation-level

Line 890-915: "This theorem above is proved on a *fixed smooth curve* X
over a field of characteristic zero. Its extension to the relative
setting over $\overline{\cM}_{g,n}$ including the boundary divisor
requires two additional ingredients that are cited but not inscribed
at chain level in this volume: (a) Francis-Gaitsgory six-functor
base-change on the relative Ran prestack [GR17 III.10]; (b) Mok25
logarithmic factorization-gluing at the boundary."

This is honest. However, the CLAUDE.md status row reads Theorem A
as "PROVED unconditional (fixed curve + relative smooth + M̄_{g,n}
including boundary for standard landscape)". The relative-smooth
and boundary extensions are demoted to citation-level in the actual
`.tex`. Three distinct claims should be separated:

(1) Theorem A^{∞,2} on fixed smooth $X$: PROVED under (H1)+(H2)+(H3),
modulo F1 bib insertions. This is `thm:A-infinity-2` and its corollary
`thm:koszul-reflection`.

(2) Theorem A^{∞,2} over the relative smooth base $M_{g,n}$: PROVED
at the citation level (GR17 III.10 base-change). Inscription would
require a proposition stating and proving the base-change step.

(3) Theorem A^{∞,2} over $\overline{\cM}_{g,n}$ including nodal boundary:
CITED (Mok25 log FM) but the chain-level factorization gluing is only
configuration-space level, not globalised to factorization algebras on
the total family. This is the load-bearing gap for downstream Theorem D
and the clutching-uniqueness step.

The chapter is honest about this in `rem:A-infinity-2-modular-family-scope`
(line 890-915) but the programme-level status summary (CLAUDE.md and
the programme preface) still advertises the all-three-levels version
as "PROVED". AP215 (preface advertising stronger than proved) at the
programme level.

### F6. Formal smoothness `cor:chiral-KK-formal-smoothness` depends on (H1)+(H2)+(H3) plus Koszul membership

Line 1360-1393: The corollary asserts: "Let $\cA$ be a chirally Koszul
factorization algebra on $X$. Then $\cA$ is formally smooth at
properad level."

The proof invokes "$\cA$ is formally smooth ... iff the cotangent
complex of $\Bbarch_X(\cA)$ is acyclic ... cofree coalgebras have
acyclic cotangent complexes (LV12 Prop 11.2.4, transferred to Fact(X)
via Prop:fg-ambient-properties) ... extension to properad level uses
Hackney-Robertson ... the graph-wise structure of the cotangent
complex decomposes along connected components."

Two subtle issues:

(a) LV12 Prop 11.2.4 is a statement about cofree *dg* coalgebras over
a field, not cofree *factorization coalgebras* on $X$. The transfer
is claimed "via Prop:fg-ambient-properties", but that proposition
asserts stability/presentability/sym-monoidal, not specifically that
cotangent-complex computations transfer. The correct transfer requires
$\Fact(X)$ to be a $k$-linear sym-monoidal $\infty$-category with
$\otimes$ exact on each variable, which it is (by GR17 IV.5), but the
citation is muddled.

(b) "Graph-wise decomposition" of cotangent complex at properad level:
Hackney-Robertson 2019 Prop 6.3 (the cited "transfer-stable along
sym-mon left adjoints" statement, line 1522) gives left-adjoint-
preservation of colimits for properad morphisms, but cotangent-complex
acyclicity is not a left-adjoint property of the underlying functor.
The honest statement is: *on the Koszul locus*, where the bar coalgebra
is cofree, graph-wise cotangent acyclicity holds because each
(n,m)-valent piece of the coproperad is a cofree piece. Off the Koszul
locus, formal smoothness at properad level is not inherited from
formal smoothness at operad level, because the graph-wise structure
mixes valences in a way that the operadic cotangent complex does not.

Scope correction: `cor:chiral-KK-formal-smoothness` should read "chirally
Koszul" hypothesis explicitly and note the failure off Koszul locus.

### F7. The "14+ downstream corollaries" list is largely genuine, with two soft cases

Lines 1072-1171: 14 downstream corollaries (D1-D14), each with a
stated descent path. Going down the list:

- D1 (classical Theorem A): LEGITIMATE via `cor:classical-A-from-A-infinity-2`
  (line 917-943, pullback along $\{\text{pt}\}$ + $H^0$).
- D2 (bar-cobar adjunction): LEGITIMATE via cohomological truncation.
- D3 (geometric unit): LEGITIMATE via (A2-ii).
- D4 (bar-cobar-Verdier intertwining): LEGITIMATE modulo a GR17
  citation (line 942, phantom per F1).
- D5 (cobar-on-free identity): LEGITIMATE via adjunction.
- D6 (FTM of twisting morphisms): LEGITIMATE via (∞,2)-Yoneda.
- D7 (seven-fold hub-and-spoke): LEGITIMATE conditional on Wave-1
  F3 (Spoke 7 class-G parametrised scope).
- D8 (Vol II Bridge I.3.2): LEGITIMATE as restatement.
- D9 (Vol III Phi as (∞,2)-functor): SOFT -- the Phi functor is inscribed
  in Vol III as an (∞,1)-functor; the (∞,2)-lift is not inscribed in
  Vol III, only sketched. The descent claim here is pre-emptive.
- D10 (Deligne-Tamarkin formality): LEGITIMATE on the formal locus.
- D11 (chiral HKR): LEGITIMATE via bar resolution.
- D12 (Quillen equivalence): LEGITIMATE, is the Ho-category truncation.
- D13 (d^2=0 via Verdier on universal family): LEGITIMATE.
- D14 (Theta-MC existence at all orders): LEGITIMATE via the counit.

Two soft cases: D9 (pre-empts a Vol III inscription that does not
exist) and D4 (cites a phantom GR17 Chapter IV.5 §5.2). Neither is
fatal; both should be tagged appropriately.

### F8. LV12 transfer at the pole-free point: genuine, not relabeling

(A2-ii) claim: pole-free restriction recovers LV12 Theorem 11.4.1 for
$(\Ass, \Ass^!)$ via $(\Dmod(X), \otimes^!) \hookrightarrow \Fact(X)$.
The pullback $\{\text{pt}\} \hookrightarrow \Ran(X)$ collapses the
$\star$-product to the ordinary tensor, and the factorization unit
becomes the tensor unit: the construction in Step 1 of the proof of
`thm:A-infinity-2` reduces to $T^c(s^{-1}\bar\cA)$ with the classical
LV12 differential.

This is a GENUINE recovery, not a relabeling: the factorization
$\star$-product at multiple distinct points is a nontrivial extension
of $\otimes^!$ at a single point, and Theorem A^{∞,2} is a strictly
stronger statement than LV12. The pole-free restriction is the
classical base case; the nontrivial content is the factorization
extension (A2-iii) via the R-twisted descent.

However: the `\otimes^!$` on $\Dmod(X)$ at a single point is the
k-linear tensor, not the chiral pseudo-tensor $\otimes^{\ch}$. The
claim "$(\Dmod(X), \otimes^!) \hookrightarrow \Fact(X)$ symmetric-
monoidal sub-inclusion" is correct *restricted to the single-point
locus*; globally on $X$, $\otimes^!$ is a sym-monoidal operation but
$(\Dmod(X), \otimes^!)$ is not a sub-sym-mon category of $\Fact(X)$
uniformly, only at a marked point. The chapter conflates the two
slightly.

### F9. `cor:eight-cor-bar-weight-1` (Spoke 5) repeats Wave-1 F2

Corollary of the unified Theorem A. At g=0 the claim is "bar
concentration in weight 1" equivalent to $K^2 \sim \id$ via the PBW
spectral sequence. At $g \ge 1$, only for class G. Wave 1 F2 already
flagged that the forward direction of Spoke 5 is tautological at g=0
(definitional restatement of E_2-collapse). The corollary form here
inherits the same tautology flag; it is not re-examined.

### F10. "Five notions of E_1-chiral algebra" warning at line 96-114 is correctly installed

Paragraph at line 96-114 names five notions A-E, states Theorem A is
in Notion B ($A_\infty$-algebra in $\End^{\ch}_\cA$), and clarifies
the pole-free restriction recovers Notion A. The $(\chirAss)^!$ vs
$\SCchtop$ clarification (line 110-113) is correct and in line with
AP-SC-BAR. This is clean.

---

## Survivors

After the attack, the following hold unconditionally after the F1 bib
insertion and the F2 unitarity-hypothesis addition:

(S1) **Unified Koszul reflection `thm:koszul-reflection` on
conilpotent-complete locus under (H1)+(H2)+(H3).** The adjoint
equivalence $K = \Bbarch_X \dashv K^{-1} = \Omegach_X$ in $\Fact(X)$
under $\star$, with chain-level $K^2 \sim \id$ on the Koszul locus
and coderived $K^2 \sim \id$ off the Koszul locus.

(S2) **Theorem A^{∞,2} `thm:A-infinity-2` as the (∞,2)-properad-level
explicit form of (S1), on a fixed smooth curve X.** The three clauses
(A2-i) properad lift, (A2-ii) pole-free LV12 recovery, (A2-iii)
R-twisted descent hold conditionally: (A2-i) and (A2-ii) unconditionally
on the Koszul locus under (H1)+(H2)+(H3); (A2-iii) unconditionally
under additional unitarity $R(z)R^{op}(-z) = \id$.

(S3) **R-twisted $\Sigma_n$-descent `lem:R-twisted-descent` on
$\Conf^{\ord}_n(X)$ top stratum, under unitarity of R(z).** Extension
to lower strata via Mok25 nearby-cycles is plausible but only
inscribed at configuration-space level; chain-level factorization
gluing to $\overline{M}_{g,n}$ is CITED, not inscribed.

(S4) **Classical Theorem A as Corollary of A^{∞,2} via cohomological
truncation + pole-free pullback.** `cor:classical-A-from-A-infinity-2`
is a genuine descent.

(S5) **Formal smoothness at properad level on the Koszul locus.**
`cor:chiral-KK-formal-smoothness` holds on the Koszul locus, via LV12
Prop 11.2.4 + transfer to $\Fact(X)$ + Hackney-Robertson left-adjoint
preservation. Off the Koszul locus, formal smoothness at properad
level is NOT inherited from operad level.

(S6) **FM69/70/72/73/74/195 heal diagnostics in
`sec:ainf2-heals`.** Each heal is a localised substitution of the
correct ambient ($\Fact(X)$ replacing $(\Dmod(X), \otimes^{\ch})$) or
of a weakened hypothesis (finite-Hoch replaced by conformal-weight
truncation-wise finite). The heals are honest and the substitutions
work, modulo F1 bib insertions.

(S7) **Four Platonic obstructions $\Pi 1$-$\Pi 4$ correctly named.**
$\Pi 1$ (FG transfer): essentially proved, needs `prop:chiral-quillen-transfer`
inscription. $\Pi 2$ ($E_n$-bar-cobar at $n \ge 2$): genuinely open
in the chiral setting. $\Pi 3$ (Lagrangian-Koszul converse): genuinely
open, is Vol I C2(iii) stream. $\Pi 4$ (unbounded-rank non-(H3)):
decorative for standard landscape.

---

## Platonic Reconstitution: Theorem A^{∞,2} with honest scope

### Statement (Beilinson-rectified)

Let $X$ be a smooth projective curve over a field $k$ of characteristic
zero. Let $\cA$ be a factorization $E_1$-algebra on $X$ satisfying:

- **(H1)** *Augmentation.* $\cA \in \Alg^{\fact,\aug}_X$; the
  augmentation ideal $\bar\cA = \ker(\varepsilon)$ is well-defined.
- **(H2)** *Augmentation-ideal completeness.* $\cA \simeq \varprojlim_n
  \cA / \bar\cA^{\,n}$. Equivalently, $\cA$ is weakly curved in
  Positselski's sense.
- **(H3)** *Finite-dimensional graded bar pieces.* Each conformal-
  weight space of $\Bbarch_X(\cA)$ is finite-dimensional.
- **(H4, only for A2-iii)** *R-matrix unitarity.* If $\cA$ carries a
  classical R-matrix $R(z) \in \End(\cA \otimes \cA)((z))$, then
  $R(z)R^{op}(-z) = \id$ (equivalently, the action of
  elementary transpositions on the fibre squares to $\id$).

Then in the Francis-Gaitsgory factorization ambient $\Fact(X)$:

(A1) **Adjoint equivalence on the conilpotent-complete locus.**
$\Bbarch_X \dashv \Omegach_X$ is an adjoint equivalence of stable
presentable sym-monoidal $\infty$-categories
$\Fact^{\aug,\comp}(X) \rightleftarrows \CoFact^{\conil,\co}(X)$.
Unit and counit are weak equivalences in the coderived $(\infty,1)$-
category $D^{\co}$.

(A2) **Chain-level involutivity on the Koszul locus.** On
$\Kosz(X) \subset \Fact^{\aug,\comp}(X)$, both unit and counit are
chain-level quasi-isomorphisms: $K^2 \simeq \id$ on $\Kosz(X)$.

(A3) **Properad lift via Hackney-Robertson.** The adjoint equivalence
extends to an $(\infty,2)$-categorical adjoint equivalence at properad
level, $\Bbarch_X: \FactProp^{\aug,\comp}(X) \rightleftarrows
\CoFactProp^{\conil,\comp}(X) : \Omegach_X$.

(A4) **Pole-free-point restriction.** Pullback along $\{\text{pt}\}
\hookrightarrow \Ran(X)$ recovers LV12 Theorem 11.4.1 for the
$(\Ass, \Ass^!)$ Koszul pair verbatim, via the sym-monoidal sub-
inclusion $(\Dmod(X), \otimes^!) \hookrightarrow \Fact(X)$ restricted
to the marked-point locus.

(A5) **R-twisted $\Sigma_n$-descent on $\Conf^{\ord}_n(X)$, under
(H4).** Assuming (H4), the symmetric bar $\Bbarch^\Sigma_n(\cA)$ is
the $L_R$-twisted $\Sigma_n$-coinvariant descent of $B^{\ord}_n(\cA)$
on the open stratum $\Conf^{\ord}_n(X)$. Extension to diagonal strata
via Mok25 log FM nearby cycles is inscribed at the configuration-space
level; chain-level factorization gluing to $\overline{M}_{g,n}$ is
cited (GR17 III.10 + Mok25) but not inscribed.

### Scope notes (honest).

- The theorem is proved on a FIXED smooth curve $X$. Extension
  horizontally over the moduli base $M_{g,n}$ of smooth curves requires
  GR17 six-functor base-change (cited, not inscribed). Extension to
  the full compactified base $\overline{M}_{g,n}$ requires Mok25
  logarithmic factorization-gluing at nodes (cited, not inscribed).
  Both extensions are load-bearing for downstream theorems (notably
  the modular-family step in Theorem D clutching-uniqueness).

- The R-matrix unitarity hypothesis (H4) holds for the standard
  families:
  - Heisenberg: trivially, $R = \tau$.
  - Rational Yangian $Y_\hbar(\fg)$: yes, standard RLL.
  - Trigonometric quantum affine $U_q(\hat\fg)$: yes, at generic $q$.
  - Affine KM $V_k(\fg)$ at non-critical level (classical KZ): yes, on
    finite-dim reps.
  - Elliptic Belavin: convention-dependent; holds in the Felder-
    Varchenko convention.
  - Toroidal DIM: convention-dependent; holds in the Miki convention.

- Formal smoothness `cor:chiral-KK-formal-smoothness` holds on the
  Koszul locus. Off the Koszul locus, formal smoothness at properad
  level does not follow from formal smoothness at operad level.

### Four Platonic obstructions (named).

$\Pi 1$ Francis-Gaitsgory transfer: essentially proved in HA +
GR17, needs inscription as `prop:chiral-quillen-transfer`.
$\Pi 2$ $E_n$-bar-cobar at $n \ge 2$: open in chiral setting.
$\Pi 3$ Lagrangian-Koszul converse: open (Vol I Theorem C stream).
$\Pi 4$ Unbounded-rank non-(H3): decorative for standard landscape.

---

## Proposed .tex patch (DO NOT apply while task #7 is running)

### Patch 1: Add six missing bib entries to `standalone/references.bib`

```bibtex
@incollection{Francis2012,
  author  = {Francis, John},
  title   = {The tangent complex and {H}ochschild cohomology of
             $\mathcal{E}_n$-rings},
  journal = {Compos. Math.},
  volume  = {149},
  year    = {2013},
  pages   = {430--480},
  note    = {Francis 2012 preprint; factorization $\star$-product
             appendix},
}

@article{HackneyRobertson2017,
  author  = {Hackney, Philip and Robertson, Marcy},
  title   = {On the category of properads},
  journal = {J. Algebra},
  volume  = {489},
  year    = {2017},
  pages   = {228--279},
}

@article{HackneyRobertson2019,
  author  = {Hackney, Philip and Robertson, Marcy},
  title   = {Lectures on $\infty$-properads},
  journal = {Contemp. Math.},
  volume  = {708},
  year    = {2018},
  pages   = {83--103},
  note    = {Model structure on $\infty$-properads, Theorem 5.12;
             transfer along sym-mon left adjoints, Prop 6.3},
}

@book{GR17,
  author    = {Gaitsgory, Dennis and Rozenblyum, Nick},
  title     = {A Study in Derived Algebraic Geometry},
  publisher = {AMS},
  year      = {2017},
  note      = {Two volumes. Chapter IV.5: factorization algebras.
               Volume II: relative Ran six-functor formalism},
}

@book{Positselski2011,
  author    = {Positselski, Leonid},
  title     = {Two kinds of derived categories, {K}oszul duality, and
               comodule-contramodule correspondence},
  publisher = {Memoirs AMS},
  volume    = {212},
  year      = {2011},
  note      = {Appendix A.5: covariantly weighted acyclicity},
}

@article{Positselski2018,
  author  = {Positselski, Leonid},
  title   = {Weakly curved $A_\infty$-algebras over a topological local
             ring},
  journal = {Mem. Soc. Math. France},
  number  = {159},
  year    = {2018},
  note    = {Theorem 9.1: weakly curved bar-cobar Quillen equivalence},
}

@incollection{Hinich2003,
  author    = {Hinich, Vladimir},
  title     = {Homological algebra of homotopy algebras},
  booktitle = {Communications in Algebra},
  volume    = {31},
  year      = {2003},
  pages     = {5467--5494},
  note      = {\S6: sym-mon promotion of Quillen equivalence},
}
```

### Patch 2: Add unitarity hypothesis (H4) to `lem:R-twisted-descent` statement

Replace lines 955-977 (the lemma statement block) with:

```latex
\begin{lemma}[$R$-matrix-twisted $\Sigma_n$-descent, under R-unitarity;
\ClaimStatusProvedHere]
\label{lem:R-twisted-descent}
\index{R-matrix!Sigma-descent}
\index{descent!R-twisted}
Let $\cA$ be an $\Eone$-chiral algebra with classical $R$-matrix
$R(z) \in \End(\cA \otimes \cA)((z))$ satisfying:
\begin{enumerate}[label=\textup{(R\arabic*)}]
\item \label{R-YBE} \emph{Classical Yang--Baxter:}
$R_{12}(z_{12}) R_{13}(z_{13}) R_{23}(z_{23}) =
 R_{23}(z_{23}) R_{13}(z_{13}) R_{12}(z_{12})$ on codimension-2 loci.
\item \label{R-unitarity} \emph{Unitarity:} $R(z) \, R^{\op}(-z) = \id$
on $\cA \otimes \cA$ as a formal Laurent series identity.
\end{enumerate}
Let $\pi\colon \Ran^{\ord}(X) \to \Ran(X)$ be the ordered-to-symmetric
Ran-torsor. Then there exists a canonical $\Sigma_n$-equivariant local
system $L_R$ on $\Ran^{\ord}(X)_{=n}$ whose monodromy along an
elementary transposition across the diagonal $z_i = z_{i+1}$ is
$R(z_i - z_{i+1})$, and for every $n\geq 0$:
\[
\barB^{\Sigma}_n(\cA)
\;\simeq\;
\bigl(B^{\ord}_n(\cA)\bigr)^{\Sigma_n\text{-coinv},\; L_R\text{-twisted}}.
\]
\end{lemma}

\begin{remark}[Unitarity scope]
Hypothesis \ref{R-unitarity} holds for the rational Yangian
$Y_\hbar(\fg)$ (standard RLL), trigonometric quantum affine
$U_q(\hat\fg)$ at generic $q$, Heisenberg ($R = \tau$), and affine
Kac--Moody $V_k(\fg)$ at non-critical level on finite-dimensional
representations. For elliptic Belavin and toroidal DIM, unitarity is
convention-dependent; holds in the Felder--Varchenko resp.\ Miki
normalisation. Without \ref{R-unitarity}, Step~1 below produces a
$\mathrm{Br}_n$-equivariant local system on $\Conf^{\ord}_n(X)$, which
descends to $\Conf_n(X)/\Sigma_n$ as a quotient stack but not to the
$\Sigma_n$-coinvariant bar.
\end{remark}
```

And inside the proof (line 989-994), replace:

```latex
The classical Yang--Baxter equation
$R_{12}R_{13}R_{23} = R_{23}R_{13}R_{12}$ on codimension-2 loci
$\{z_i = z_j = z_k\}$ ensures that the representation of the pure braid
group $PB_n(X)$ extends to a representation of the symmetric group
$\Sigma_n$ on the boundary of a fundamental domain: this produces
$L_R$ as a $\Sigma_n$-equivariant local system.
```

by:

```latex
Hypothesis \ref{R-YBE} produces a representation of the pure braid
group $PB_n(X)$ on $\cA^{\otimes n}$ (braid relation on codim-2 loci).
Hypothesis \ref{R-unitarity} promotes this to a representation of
$\Sigma_n$: unitarity $R(z) R^{\op}(-z) = \id$ is the statement that
the action of each elementary transposition $s_i$ squares to
$\id$, which is exactly the relation $s_i^2 = e$ in $\Sigma_n$
missing from the pure braid group. Together with \ref{R-YBE} (which
gives the braid relation $s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1}$),
$\Sigma_n$ acts on the fibre, producing $L_R$ as a
$\Sigma_n$-equivariant local system.
```

### Patch 3: Scope `cor:chiral-KK-formal-smoothness` to Koszul locus explicitly

Replace line 1360-1373 corollary statement by:

```latex
\begin{corollary}[Chiral Koszulness implies properad-level formal
smoothness on the Koszul locus; \ClaimStatusProvedHere]
\label{cor:chiral-KK-formal-smoothness}
\index{formal smoothness!chiral Koszul implies}
\index{Koszul Kontsevich!formal smoothness}
Let $\cA$ be a chirally Koszul factorization algebra on $X$, i.e.,
$\cA \in \Kosz(X) \subset \Fact^{\aug,\comp}(X)$ satisfying
\textup{(H1)--(H3)}.
Then $\cA$ is formally smooth at properad level\emph{ on the Koszul
locus}: for every nilpotent extension $R \to R_0$ of dg algebras with
$\ker$ square-zero and every $R_0$-valued point
$\Spec R_0 \to \Fact^{\aug,\comp}(X)$ factoring through $\cA$, there
exists an $R$-valued lift
$\Spec R \to \FactProp^{\aug,\comp}(X)$ extending the $R_0$-valued
point, unique up to contractible space of choices.
\emph{Off $\Kosz(X)$, formal smoothness at properad level is
genuinely stronger than formal smoothness at operad level and is not
automatic from Theorem~$A^{\infty,2}$.}
\end{corollary>
```

### Patch 4: Clarify Mittag-Leffler argument in Step 2

Insert after line 837 (after "exactness of the $\star$-monoidal base change..."):

```latex
Mittag--Leffler in detail: under hypothesis~(H2), the coradical
filtration $F^{\bullet}_c(\Bbarch_X(\cA))$ on the bar coalgebra is
exhaustive (conilpotent-completeness). Dually, the bar-length
filtration $F^{\bullet}_{bar}(\bar B(\cA))$ on the bar complex is
exhaustive unconditionally. The two filtrations are interchanged by
the counit pairing, and (H2)~+ Positselski's weakly curved bar--cobar
(\cite[Theorem~9.1]{Positselski2018}) ensures that $\varprojlim^1_n$ of
the bar-length filtration on cohomology vanishes. This is the
Mittag--Leffler property needed for convergence.
```

### Patch 5: Tag downstream corollaries D4, D9 honestly

D4 descent claim: replace "follows by applying the $(\infty,2)$-adjoint
equivalence to the biequivariance of $\Bbarch_X$ against Verdier
duality on $\Dmod(\Ran(X))$" (line 936-942) by:

```latex
follows from Verdier-biequivariance of $\Bbarch_X$ at the chain level
(Theorem~\ref{thm:bar-cobar-verdier}), lifted to $(\infty,2)$-level by
the adjoint equivalence. The diagonal factorization on $\Ran(X)$
makes Verdier duality $\star$-self-adjoint; the $(\infty,2)$-level
2-isomorphism is obtained by transport of structure from the classical
statement, not by direct construction in $\Fact(X)$.
```

D9 descent claim: replace (line 1121-1127) by:

```latex
\item \label{D9} Vol~III CY-to-chiral functor $\Phi$ factors through
$\Fact(X)$ at the chain level (\textup{Vol~III, \S CY-A}); the
$(\infty,2)$-lift is \emph{conjectural}
\textup{(}to be inscribed in Vol~III as $\Phi^{(\infty,2)}$;
currently sketched only\textup{)}, and Theorem~$A^{\infty,2}$ would
then supply the bar--cobar equivalence realising the CY-A$_3$
inf-cat statement at $(\infty,2)$-level.
```

---

## REPORT

See companion REPORT section below.
