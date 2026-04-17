# Chiral Higher Deligne conjecture — attack-and-heal (2026-04-18)

Target: Vol II `chapters/theory/chiral_higher_deligne.tex` (999 lines, 49KB).
Status-table advertisement (Vol I `CLAUDE.md` Theorem Status → Chiral Higher
Deligne): PROVED (Vol II, 2026-04-16). Four advertised results:

1. `thm:chiral-higher-deligne` — $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is universal
   $E_3$-chiral, acted on by $\SCchtop$ via heptagon edges
   $(3)\leftrightarrow(4)\leftrightarrow(5)$.
2. `thm:H-concentration-via-E3-rigidity` — Thm H concentration is CONSEQUENCE
   of $E_3$-rigidity-at-a-point plus PBW collapse.
3. `thm:chd-ds-hochschild` — $\ChirHoch^\bullet(\cW_k(\fg,f))
   \simeq H^\bullet_{DS}(\ChirHoch^\bullet(V_k(\fg)))$ chain-level $E_2$-chiral
   Gerstenhaber.
4. `cor:universal-holography-class-M` — closes class-M chain-level 3d HT
   holography.

Adversarial posture: assume the metacognitive layer is wrong until verified
from source (`CLAUDE.md` Constitutional Trust Warning). Every
`\ClaimStatusProvedHere` tag is conjectural until the proof body is read end
to end and every cited lemma resolves to an inscribed body, not a forward
reference, a phantomsection, or a cross-volume label in violation of HZ-11.

---

## 1. Inscription check (AP255)

All four advertised results ARE inscribed as `\begin{theorem}` /
`\begin{corollary}` environments with proof bodies; the chapter file exists
on disk at the advertised path. Heptagon-edge cross-references
`\ref{prop:heptagon-edge-34}` and `\ref{prop:heptagon-edge-45}` resolve to
genuine inscriptions in Vol II `chapters/theory/sc_chtop_heptagon.tex` at
lines 794 and 850 respectively.

Cross-volume labels cited in proofs:

- `thm:chiral-positselski-weight-completed` (Vol I
  `theorem_B_scope_platonic.tex:245`) — REAL theorem with proof body.
- `thm:chiral-positselski-7-2` (Vol I `theorem_B_scope_platonic.tex:246`) —
  `\phantomsection` ALIAS on the above. Legitimate alias, not a phantom in
  the AP255 sense.
- `thm:pbw-koszulness-criterion` (Vol I
  `chiral_koszul_pairs.tex:697`) — REAL.
- `thm:hochschild-concentration-E1` (Vol I) — REAL.
- `thm:ds-koszul-intertwine` (Vol I
  `chiral_modules.tex:4348`) — REAL.
- `thm:mc5-class-m-chain-level-pro-ambient` (Vol I
  `mc5_class_m_chain_level_platonic.tex:230`) — REAL.
- `thm:topologization` (Vol I `en_koszul_duality.tex:3073`) — REAL.
- `def:koszul-locus` (Vol I) — REAL.
- `prop:chirhoch1-affine-km` (Vol I `chiral_center_theorem.tex:2133`) — REAL.

Infrastructure labels (heptagon chapter label, universal-holography part
label):

- `ch:sc-chtop-heptagon` — REAL (`sc_chtop_heptagon.tex:22` or nearby).
- `ch:thqg-holographic-reconstruction` — REAL (Vol II
  `chapters/connections/thqg_holographic_reconstruction.tex:6`, self-label
  aliased to dangling reference).
- `ch:thqg-symplectic-polarization` — REAL (Vol II
  `chapters/connections/thqg_symplectic_polarization.tex:27`, self-label
  aliased to dangling reference).
- `part:universal-holography` — NOT FOUND anywhere in Vol II (0 hits across
  `~/chiral-bar-cobar-vol2`). This is cited at `chiral_higher_deligne.tex:68`
  in the prologue: `cf.~\ref{part:universal-holography}`. **AP264
  phantom-ref-to-non-existent-label violation.**

Test file `compute/tests/test_chiral_higher_deligne.py` exists at the Vol II
path and runs the three HZ-IV decorated tests.

**AP255 verdict for the chapter**: all four theorems inscribed, bodies
present, test file present. One phantom `\ref{part:universal-holography}`
(cosmetic, prologue-level).

---

## 2. Load-bearing gap in `thm:H-concentration-via-E3-rigidity`:
   native-vs-derived $E_3$ type confusion (AP195 five-object discipline +
   AP260 scope-without-projector)

The proof body at lines 661–708 contains two formula-level type errors that
together invalidate Step 1–Step 3 of the concentration argument as written.

### 2.1 Step 1 applies `\ref{thm:chiral-higher-deligne}(1)` to the wrong object

Line 664–669:

> Step 1: formal-disc restriction is $E_3$-rigid. Fix a point $x \in X$ and
> restrict $\cA$ to the formal disc $D_x \subset X$. The restricted algebra
> $\cA|_{D_x}$ is an $E_3$-algebra in $\Bbbk$-chain complexes (in the sense
> of Convention~\ref{conv:chd-e3-chiral-meaning}) by
> Thm~\ref{thm:chiral-higher-deligne}(1).

This is a category error. Part (1) of the main theorem (line 467–471)
reads:

> The chiral Hochschild complex
> $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \ChirHoch^\bullet(\cA,\cA)$
> carries a canonical $E_3$-chiral-algebra action ...

The $E_3$-chiral structure lives on $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$,
not on $\cA$. The chapter's own `rem:chd-native-vs-derived` (line 591–599)
states this as a zero-tolerance discipline:

> $\cA$ itself is $E_1$-chiral, not $E_3$. The $E_3$-chiral structure lives
> on $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ as an OUTPUT of the derived-centre
> construction. Writing "$E_3$ on $\cA$" is a type error.

Step 1 commits exactly that type error. The correct object Step 1 should
name is $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$.

### 2.2 Step 2 mis-types chiral PBW as $U_{E_3}$

Line 685–691:

> Step 2: PBW gives polynomial growth. Chiral PBW collapse for $\cA$ in the
> Koszul locus (Vol.~I, Theorem~\ref*{thm:pbw-koszulness-criterion})
> identifies $\cA|_{D_x} = U_{E_3}(V_x)$ where $V_x$ is the space of
> generators restricted to $D_x$, of polynomial growth ...

Chiral PBW identifies a chiral algebra on the Koszul locus with the
$E_1$-chiral envelope of a Lie-like generator datum,
$\cA|_{D_x} = U_{E_1}^{\mathrm{ch}}(V_x)$ (or, after passing to modes, the
$E_1$-topological envelope of the generator Lie algebra). There is no
Vol I theorem that writes $\cA|_{D_x} = U_{E_3}(V_x)$. The identification
$\cA|_{D_x} = U_{E_3}(V_x)$ would require $\cA$ to be an $E_3$-algebra,
which it is not (point 2.1 above).

### 2.3 Lemma `lem:chd-e3-rigidity-point` hypothesis is not met by
   `Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})` either

If we correct Step 1 and Step 2 to reference the derived centre
$R_x := Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$ in place of $\cA|_{D_x}$,
the new question is whether $R_x$ satisfies the hypothesis of
`lem:chd-e3-rigidity-point` (line 617–626):

> Assume $R$ is the $E_3$-envelope of a graded commutative algebra of finite
> growth (i.e., $R = U_{E_3}(V)$ for $V$ a graded vector space with
> $\dim V_n \le p(n)$ for some polynomial $p$).

The derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is NOT an
$E_3$-envelope of a graded vector space. It is the $E_3$-chiral algebra
obtained by applying the derived-centre construction to an $E_1$-chiral
algebra $\cA$; its cohomology is what the theorem is trying to constrain.
Even when $\cA|_{D_x}$ has polynomial growth, there is no structural reason
for $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$ to be presented as
$U_{E_3}(W_x)$ for some polynomial-growth $W_x$; that presentation would
require a chiral analogue of $E_3$-PBW which is nowhere inscribed.

### 2.4 Net consequence

As written, Steps 1–3 are a non-sequitur. The lemma
`lem:chd-e3-rigidity-point` is an $E_3$-Koszul-duality statement about
enveloping algebras $U_{E_3}(V)$; neither $\cA|_{D_x}$ (wrong operadic type)
nor $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$ (wrong structural
presentation) is of that form. The parallel Shelton–Yuzvinsky proof
acknowledged in the remark at line 701–707 is the only route that actually
reaches concentration; the $E_3$-rigidity route is not.

This is AP195 (five-object conflation — collapsing $\cA$ with
$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$) combined with AP260
(scope-without-constructed-projector — the PBW presentation is asserted to
be $U_{E_3}$ without a constructed comparison between the $E_1$-chiral
envelope and $E_3$-envelope).

---

## 3. Circular routing in clause (2) of `thm:chiral-higher-deligne`

Clause (2) proof at line 545–563 cites Vol I
`thm:chiral-positselski-7-2` to obtain the
$(\SCchtop)^!$-cobar contracting homotopy. The remark
`rem:chd-universality-conditional` (line 488–509) is honest about this:
clause (2) is tagged `\ClaimStatusConditional` with explicit attribution
because the $(\SCchtop)^!$-formulation required is NOT independently
inscribed in Vol I. `thm:chiral-positselski-7-2` is a
`\phantomsection` alias on `thm:chiral-positselski-weight-completed` — that
alias is legitimate, but the $(\SCchtop)^!$-LIFT of that statement, which is
what clause (2) actually uses, is not inscribed anywhere.

The chapter discipline here is sound: the conditional tag plus the explicit
attribution remark make the dependency explicit. No further heal required;
the remark already documents the gap. Flag as an OPEN frontier item
(Vol I needs an inscribed $(\SCchtop)^!$-lift of
`thm:chiral-positselski-weight-completed`).

---

## 4. AP258 chain-level / cohomological drift in `thm:chd-ds-hochschild`

Line 744–746:

> Then at chain level there is an $\infty$-quasi-isomorphism of
> $E_2$-chiral brace algebras (equivalently, a quasi-iso on cohomology of
> the strict Gerstenhaber structures) ...

The parenthetical "equivalently" is false. $\infty$-qi of $E_2$-brace
algebras (chain-level) is strictly stronger than qi on cohomology of
Gerstenhaber structures. Step 3 of the proof (line 780–795) transfers an
$A_\infty$ structure through the DS deformation retract via HPL. The HPL
output is a chain-level $A_\infty$-qi (strong enough to give $\infty$-qi of
$E_2$-brace after the Step-4 intertwining). The cohomological statement is
automatic from the chain-level one, not equivalent to it.

Minor heal: rewrite the parenthetical to "and in particular a quasi-iso on
cohomology of the strict Gerstenhaber structures."

### Compatibility with the $E_3$-extension inherits conditional status

Step 4 (line 803–807) promotes the qi to $E_3$-chiral via Part (2) of
`thm:chiral-higher-deligne`. Part (2) is `\ClaimStatusConditional` on the
positselski lift. Therefore the $E_3$-extension compatibility of
`thm:chd-ds-hochschild` should carry the same conditional status rather
than the current blanket `\ClaimStatusProvedHere`. Two heal options:

(a) Split the theorem header: $E_2$-chiral brace qi
    `\ClaimStatusProvedHere`; $E_3$-chiral compatibility
    `\ClaimStatusConditional` with the same attribution as
    `rem:chd-universality-conditional`.
(b) Tag the entire theorem `\ClaimStatusConditional` on the positselski
    lift.

Option (a) preserves the load-bearing $E_2$-level result at
ProvedHere; option (b) is simpler and more conservative.

---

## 5. `cor:universal-holography-class-M` inherits conditional status

The corollary is tagged `\ClaimStatusProvedHere` at line 836. Its proof
routes through `thm:chd-ds-hochschild` (which inherits the Part (2)
conditionality of `thm:chiral-higher-deligne` — see §4 above) and through
Costello–Francis–Gwilliam arXiv:2602.12412 §4. The CFG input is cited at
citation level, not independently inscribed, so the corollary is also
"chain-level on the weight-completed ambient assuming CFG25 §4 identifies
the class L derived centre with the 3d HT bulk".

The ambient-qualification (weight-completed vs. direct-sum) is honestly
inscribed at line 850–862. But the cascade of citation-level dependencies
(positselski lift + CFG §4 + Gaiotto–Witten Sugawara reduction cited at
line 873) is not reflected in the status tag. Heal: downgrade to
`\ClaimStatusConditional` with an explicit attribution remark listing the
three citation-level inputs.

---

## 6. Phantom `\ref{part:universal-holography}`

Prologue line 68: `cf.~\ref{part:universal-holography}`. Zero matches for
`\label{part:universal-holography}` across Vol II. This is a cosmetic
AP264 phantom ref — the build will emit `[?]` or a warning. Heal: either
(a) introduce `\phantomsection\label{part:universal-holography}` at the
relevant part-introduction file in Vol II (likely
`chapters/connections/part_vi_*.tex` or equivalent), or (b) retarget the
ref to `ch:thqg-holographic-reconstruction` (which exists).

---

## 7. Test file tautology residue

`test_chiral_higher_deligne.py::test_chd_e3_action_structural` is a HZ-IV-
W8-C heal (Wave 9 lint, 2026-04-17) — the assertion that chapter /
Tamarkin / Kontsevich / Francis all produce identity-arity on the basic
brace and binary arity on $B^{(n)}$ is non-tautological in that the four
values are computed via distinct combinatorial recipes, but the check is
that four hard-coded $(1,1)$ and $(2,2)$ tuples agree. This is the
AP287/AP288 frontier: the disjoint-sources labels are sound, the body
agreement is structural, and no numerical observable beyond input/output
count is available at this primitive level.

Recommendation: tag with a module-level `# HZ-IV-W8-B FLAG` per Wave-10
protocol, since this is primitive-by-construction rather than a vacuous
body. (The test body is not tautological in the AP277 sense — it does
reconstruct the arity from four distinct recipes — but all four recipes
land on the same two tuples by structural inevitability.)

---

## 8. Summary of heals (priority order)

| # | Severity | Heal | Target |
|---|----------|------|--------|
| 1 | CRITICAL | Rewrite `thm:H-concentration-via-E3-rigidity` proof Steps 1–2 to replace $\cA|_{D_x}$ with $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$ and to replace $U_{E_3}$ with the correct operadic envelope; alternatively, tag the theorem `\ClaimStatusConditional` on an inscribed $E_3$-PBW analogue for derived chiral centres, or retract to `\ClaimStatusConjectured` and preserve the Shelton–Yuzvinsky route as the sole route to Thm H. | Vol II `chiral_higher_deligne.tex:661-708` |
| 2 | MODERATE | Inherit conditional status from clause (2) of `thm:chiral-higher-deligne` into `thm:chd-ds-hochschild` $E_3$-compatibility and into `cor:universal-holography-class-M`. Option (a) split-header or (b) blanket conditional tag. | Vol II `chiral_higher_deligne.tex:738-757, 835-862` |
| 3 | MINOR | Rewrite the "equivalently" parenthetical in `thm:chd-ds-hochschild` statement to "and in particular" (AP258 chain-vs-cohomology drift). | Vol II `chiral_higher_deligne.tex:744-746` |
| 4 | MINOR | Heal phantom `\ref{part:universal-holography}` — either inscribe the label at the appropriate part file or retarget to `ch:thqg-holographic-reconstruction`. | Vol II `chiral_higher_deligne.tex:68` |
| 5 | FRONTIER | Inscribe in Vol I an $(\SCchtop)^!$-lift of `thm:chiral-positselski-weight-completed`, or explicitly downgrade clause (2) of `thm:chiral-higher-deligne` to `\ClaimStatusConjectured`. | Vol I `theorem_B_scope_platonic.tex` |
| 6 | COSMETIC | Flag `test_chd_e3_action_structural` with `# HZ-IV-W8-B FLAG` per Wave-10 protocol. | Vol II `compute/tests/test_chiral_higher_deligne.py` |

---

## 9. Status-table propagation (CLAUDE.md)

Current Vol I `CLAUDE.md` status-table entry for Chiral Higher Deligne
advertises four results as PROVED. Post-audit reality:

- `thm:chiral-higher-deligne` part (1) and (3) PROVED; part (2)
  Conditional on the phantom positselski lift. Already honestly tagged.
- `thm:H-concentration-via-E3-rigidity` — **as written contains a native-
  vs-derived type error**; either rewrite or downgrade. Until rewrite,
  concentration survives via the parallel Shelton–Yuzvinsky route of Vol I
  `thm:hochschild-concentration-E1`, so Theorem H itself is not at risk —
  only the claim that concentration is a Koszul-dual CONSEQUENCE rather
  than a parallel mechanism is at risk.
- `thm:chd-ds-hochschild` $E_2$-level PROVED; $E_3$-compatibility
  Conditional.
- `cor:universal-holography-class-M` Conditional via the cascade.

Propagate the stratified status to:

- `CLAUDE.md` lines 510–517 (Chiral Higher Deligne status row).
- Vol I `chapters/frame/preface.tex:1716` reference to
  `V2-thm:chiral-higher-deligne` — already explicitly notes the weight-
  completed vs. uncompleted direct-sum scope. No change.
- Vol I `chapters/examples/chiral_moonshine_unified.tex:491` reference to
  `V2-thm:chd-ds-hochschild` — already correctly scopes via "that bridge
  scopes to...". No change.
- Vol I `chapters/theory/chiral_climax_platonic.tex:930` reference to
  `thm:H-concentration-via-E3-rigidity` — needs update to reflect the
  type-error gap if heal #1 option (c) retract is chosen.
- Vol I `chapters/frame/programme_overview_platonic.tex:185` reference to
  `chap:chiral-higher-deligne` — cosmetic, no content change required.

---

## 10. Answers to the mission questions

(i) **Inscription**: four advertised results all inscribed with proof
bodies; test file present; heptagon edges (3)↔(4) and (4)↔(5) both
inscribed as `prop:heptagon-edge-34` and `prop:heptagon-edge-45` in Vol II
`sc_chtop_heptagon.tex`. Not phantomsection-masked.

(ii) **Universal $E_3$ meaning**: universal in the sense of an operadic
universal property — clause (2) says every $\SCchtop$-open/closed pair
$(B, \cA)$ with $B$ acting on $\cA$ factors uniquely (up to homotopy)
through $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$. This is the universal
property dualising Deligne–Tamarkin for $E_2$. The proof is constructive
at $E_2$ level (explicit multi-input braces $B^{(n_1, \ldots, n_k)}$ at
Def 2.2) and existence-only at the $E_3$ upgrade (Dunn additivity +
heptagon edge 4↔5).

(iii) **Heptagon edge labels**: edges (3)↔(4) and (4)↔(5) both exist at
propositional form. Edge (3)↔(4) is labelled "Chiral Deligne–Tamarkin for
$\SCchtop$" at Vol II `sc_chtop_heptagon.tex:729`; edge (4)↔(5) appears in
the context of "QME equals convolution MC" (line 825) and the
propositional-form edge (line 849). Neither edge is Drinfeld centre /
half-braiding / Costello–Tamarkin transfer in the naive sense; the
heptagon labels faces (6) = Drinfeld centre face, (3) = Chiral Deligne–
Tamarkin, (5) = Convolution MC / Lagrangian section. The labeling in the
status-table narrative of Vol I `CLAUDE.md` is not literally faithful to
the Vol II heptagon chapter's edge conventions; this is a minor narrative
drift, not a mathematical problem.

(iv) **Concentration consequence vs hypothesis**: the inversion claim IS
made — concentration of Thm H is presented as a CONSEQUENCE of
$E_3$-rigidity plus PBW, inverting the traditional direction. BUT the
proof has the native-vs-derived type error documented in §2. If the heal
in §2 is option (c) retract, then Thm H reverts to its Vol I form with the
Shelton–Yuzvinsky / PBW proof as the primary; the Vol II re-parsing
becomes a programmatic suggestion rather than a proved inversion. The old
PBW + Orlik–Solomon proof is NOT redundant; it is the sole inscribed
route under the current state of affairs. If heal #1 option (a) rewrite
succeeds (inscribing an $E_3$-PBW analogue for derived chiral centres),
both routes survive as independent verifications.

(v) **DS-Hochschild chain-level scope**: the HPL transfer (Step 3 of the
proof) is a chain-level $A_\infty$-qi construction, which gives chain-
level $E_2$-chiral brace qi when combined with the Step-4 intertwining.
The "equivalently" parenthetical is mislabelled; chain-level is strictly
stronger. The $E_3$-extension is Conditional via the Part (2)
conditionality of the main theorem. Heal #3 (minor) rewrites the
parenthetical.

(vi) **Cor:universal-holography-class-M soundness given MC5 Wave-14
filtration-vs-grading heal**: the corollary's ambient-qualification
(weight-completed / pro-ambient only) is consistent with MC5 as presently
inscribed in Vol I (`thm:mc5-class-m-chain-level-pro-ambient`, Vol I
`mc5_class_m_chain_level_platonic.tex:230`). The chapter itself
acknowledges that direct-sum-ambient class-M chain-level is "genuinely
false" (line 856), and invokes the weight-completed ambient where
bar-cobar and DS BRST both converge. The Wave-14 filtration-vs-grading
correction of MC5 does not change this framing — it tightens the proof of
the MC5 theorem, not the ambient it lives in. The cascade of
conditionalities (positselski lift + CFG25 §4 + Gaiotto–Witten) means the
corollary is better tagged Conditional than ProvedHere, but the ambient
itself is not unsound.

---

## 11. Verdict

**Substantial mathematical content is sound**; the chapter's $E_2$-level
structure (algebraic = geometric HKR-type identification, multi-input
braces with Stasheff coherence through degree 4, chiral Deligne-Tamarkin
at the formal disc, $E_2$-chiral brace qi for DS reduction) is a genuine
contribution with proper attribution.

**Three localized gaps**:

- (CRITICAL) Native-vs-derived type error in
  `thm:H-concentration-via-E3-rigidity` Steps 1–2, which as written do not
  verify the hypothesis of the applied `lem:chd-e3-rigidity-point`. Thm H
  concentration survives via the Shelton–Yuzvinsky route. The $E_3$-rigidity
  re-parsing of Thm H is not currently proved.
- (MODERATE) Clause (2) of the main theorem is honestly conditional on an
  uninscribed Vol I lift; the cascading conditionality into
  `thm:chd-ds-hochschild` $E_3$-compatibility and
  `cor:universal-holography-class-M` is not reflected in the status tags.
- (MINOR) "Equivalently" parenthetical at line 745 is the AP258 chain-
  level / cohomological drift.

**Recommended CLAUDE.md status-row update** (suggested text, not yet
applied):

> **Chiral Higher Deligne** | PROVED at $E_2$-chiral level; $E_3$-upgrade
> Conditional on the uninscribed $(\SCchtop)^!$-lift of chiral Positselski
> (Vol I frontier). `thm:chiral-higher-deligne` clauses (1) and (3)
> ProvedHere; clause (2) Conditional. `thm:chd-ds-hochschild` $E_2$-level
> ProvedHere; $E_3$-compatibility Conditional.
> `thm:H-concentration-via-E3-rigidity` **AS WRITTEN contains a native-
> vs-derived type error** (Steps 1–2 apply $E_3$ structure to $\cA$ rather
> than to $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$; Step 2 mis-types chiral
> PBW as $U_{E_3}$); the parallel Shelton–Yuzvinsky proof in Vol I
> `thm:hochschild-concentration-E1` is unaffected. Pending rewrite of
> Steps 1–2 or retraction to `\ClaimStatusConjectured`.
> `cor:universal-holography-class-M` ambient-qualified (weight-completed /
> pro-ambient; direct-sum false), cascading Conditional on
> positselski-lift + CFG25 §4.

---

## 12. Patch (not applied; pending user authorization)

Per AP316 no-commit discipline, patches listed as diff sketches rather
than applied. Three heals chosen as the minimum set restoring honest
scope without rewriting hard mathematics:

### Patch 1 — Heal #2, option (b) blanket conditional tags

```diff
--- a/chapters/theory/chiral_higher_deligne.tex
+++ b/chapters/theory/chiral_higher_deligne.tex
@@ -738 +738 @@
-\begin{theorem}[DS-Hochschild chain-level compatibility;
-\ClaimStatusProvedHere]%
+\begin{theorem}[DS-Hochschild chain-level compatibility;
+$E_2$-level \ClaimStatusProvedHere; $E_3$-compatibility
+\ClaimStatusConditional]%
@@ -835 +835 @@
-\begin{corollary}[Universal holography, class M, ambient-qualified;
-\ClaimStatusProvedHere]%
+\begin{corollary}[Universal holography, class M, ambient-qualified;
+\ClaimStatusConditional]%
```

### Patch 2 — Heal #3, minor prose rewrite

```diff
@@ -744 +744 @@
-an $\infty$-quasi-isomorphism of $E_2$-chiral brace algebras (equivalently,
-a quasi-iso on cohomology of the strict Gerstenhaber structures)
+an $\infty$-quasi-isomorphism of $E_2$-chiral brace algebras, hence in
+particular a quasi-isomorphism on cohomology of the strict Gerstenhaber
+structures,
```

### Patch 3 — Heal #1, option (c) retract concentration-via-rigidity

The cleanest option until an $E_3$-PBW analogue for derived chiral
centres is inscribed: downgrade
`thm:H-concentration-via-E3-rigidity` to `\ClaimStatusConjectured` and
add a retraction remark naming the type-error gap.

```diff
@@ -648 +648 @@
-\begin{theorem}[Concentration via $E_3$-rigidity;
-\ClaimStatusProvedHere]%
+\begin{conjecture}[Concentration via $E_3$-rigidity;
+\ClaimStatusConjectured]%
@@ -659 +659 @@
-\end{theorem}
+\end{conjecture}
@@ -710,+new @@
+\begin{remark}[Retraction: type error in Steps 1--2]%
+\label{rem:chd-e3-rigidity-type-error}%
+The proof above as inscribed contains a native-vs-derived type error:
+Step 1 writes ``$\cA|_{D_x}$ is an $E_3$-algebra'' but the main theorem
+places the $E_3$-chiral structure on $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$,
+not on $\cA$ itself (\emph{rem:chd-native-vs-derived}). Step 2 writes
+``$\cA|_{D_x} = U_{E_3}(V_x)$'' but chiral PBW gives an $E_1$-chiral
+envelope, not an $E_3$-envelope. Replacing $\cA|_{D_x}$ with
+$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$ corrects Step 1 but not
+Step 2, because the derived chiral centre is not presented as
+$U_{E_3}(W_x)$ for any polynomial-growth $W_x$ under any inscribed
+theorem. The statement is therefore downgraded to
+\ClaimStatusConjectured; the parallel route of Vol.~I
+\ref*{thm:hochschild-concentration-E1} via chiral PBW and
+Shelton--Yuzvinsky Orlik--Solomon Koszulity proves concentration by a
+disjoint mechanism and is unaffected. The inversion "concentration is a
+Koszul-dual consequence of $E_3$-rigidity" remains a valid \emph{program
+direction} pending an inscribed $E_3$-PBW analogue for derived chiral
+centres.
+\end{remark}
```

### Patch 4 — Heal #4, phantom ref

```diff
@@ -68 +68 @@
-(cf.~\ref{part:universal-holography})
+(cf.~\ref{ch:thqg-holographic-reconstruction})
```

Patches listed for user review; no commit made, per AP316 and pre-commit
gate discipline.
